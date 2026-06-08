#!/usr/bin/env python3
"""Construiește indexul de interogare al wiki-ului din paginile `index.md`.

Latura de INGESTIE a RAG-ului hibrid. Rulează rar (după fiecare regenerare wiki):
parsează `wiki_module_odoo/<modul>/index.md`, extrage metadatele + textul căutabil
și scrie un catalog determinist în `wiki_module_odoo/.index/`:

  - chunks.json : un chunk per modul (catalog pentru retrieval lexical)
  - meta.json   : info build + configurarea embeddings (model, dimensiune, provider)

Mod LEXICAL (implicit): nu se generează vectori, doar catalogul. `wiki_search.py`
caută lexical peste `text`. Zero egress, zero dependențe externe.

Mod VECTORIAL (opțional, cu --embed): generează `vectors.npy` și înregistrează în
meta.json modelul + dimensiunea. ATENȚIE — `wiki_search.py` TREBUIE să embeduiască
query-ul cu EXACT același model/dimensiune (citite din meta.json), altfel
similaritatea returnează gunoi. De-aia funcția de embedding stă aici, într-un singur
loc, și e referită de ambele laturi.

Folosire:
    python3 wiki_module_odoo/scripts/wiki_index.py            # rebuild catalog (lexical)
    python3 wiki_module_odoo/scripts/wiki_index.py --embed    # + vectori (necesită provider + numpy)
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

WIKI_DIR = Path(__file__).resolve().parent.parent  # .../wiki_module_odoo
INDEX_DIR = WIKI_DIR / ".index"

# ── parsare pagină ──────────────────────────────────────────────────────────

_META_RE = {
    "module": re.compile(r"\*\*Nume Tehnic:\*\*\s*`([^`]+)`"),
    "version": re.compile(r"\*\*Versiune:\*\*\s*`([^`]+)`"),
    "github": re.compile(r"\*\*Cale:\*\*\s*(\S+)"),
    "local_path": re.compile(r"\*\*Cale Local[ăa]:\*\*\s*`([^`]+)`"),
    "last_ingest": re.compile(r"\*\*Ultima Ingestie:\*\*\s*`([^`]+)`"),
}
_FRIENDLY_RE = re.compile(r"^#\s+(.+?)\s*\(localizat", re.MULTILINE)
# tokeni de modul: linkuri [x](../x/index.md) sau text `x`
_DEP_TOKEN_RE = re.compile(r"\[([^\]]+)\]\([^)]*index\.md\)|`([a-z0-9_]+)`")


def _section(body: str, num: int) -> str:
    """Întoarce textul brut al secțiunii `#### {num}. ...` până la următorul `####`."""
    m = re.search(rf"^####\s*{num}\.\s.*?$(.*?)(?=^####\s|\Z)", body,
                  re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else ""


def _bullets(text: str) -> list[str]:
    out = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")):
            # curăță bold-ul de tip "**Titlu:** rest"
            clean = re.sub(r"\*\*([^*]+)\*\*", r"\1", line[2:]).strip()
            if clean:
                out.append(clean)
    return out


def _module_tokens(text: str) -> list[str]:
    seen, out = set(), []
    for link_label, code in _DEP_TOKEN_RE.findall(text):
        tok = (link_label or code).strip()
        if tok and tok not in seen:
            seen.add(tok)
            out.append(tok)
    return out


def parse_page(md_path: Path) -> dict | None:
    body = md_path.read_text(encoding="utf-8")
    chunk: dict = {"path": f"{md_path.parent.name}/index.md"}
    for key, rx in _META_RE.items():
        m = rx.search(body)
        chunk[key] = m.group(1) if m else None
    fm = _FRIENDLY_RE.search(body)
    chunk["friendly_name"] = fm.group(1).strip() if fm else md_path.parent.name
    # fallback nume tehnic = numele folderului
    chunk["module"] = chunk.get("module") or md_path.parent.name

    summary = _section(body, 1)
    features = _bullets(_section(body, 2))
    chunk["summary"] = " ".join(summary.split())
    chunk["features"] = features
    chunk["dependencies"] = _module_tokens(_section(body, 3))
    chunk["connections"] = _module_tokens(_section(body, 5))

    # text căutabil / de embeduit: nume + sumar + funcționalități
    chunk["text"] = "\n".join(
        [chunk["friendly_name"], chunk["module"], chunk["summary"], *features]
    ).strip()
    return chunk if chunk["text"] else None


# ── embeddings (SEAM HIBRID — un singur loc, partajat cu wiki_search.py) ──────

# Provider de embeddings: OpenAI. Cheia se citește din mediu (OPENAI_API_KEY) —
# NICIODATĂ hardcodată aici, ca să nu ajungă în git. Aceleași valori sunt citite la
# query de wiki_search.py din .index/meta.json (consistență model↔dimensiune).
EMBED_PROVIDER = "openai"
EMBED_MODEL = "text-embedding-3-small"
EMBED_DIM = 1536

_EMBED_BATCH = 256  # câte texte pe apel; OpenAI acceptă liste mari


def embed_texts(texts: list[str]) -> "list[list[float]]":
    """Transformă texte în vectori cu OpenAI. Folosit IDENTIC de ingestie și query.

    Necesită `pip install openai` + egress + OPENAI_API_KEY în mediu. Întoarce o listă
    de vectori de lungime EMBED_DIM.
    """
    from openai import OpenAI  # lazy: doar în mod vectorial

    client = OpenAI()  # citește OPENAI_API_KEY din mediu
    out: list[list[float]] = []
    for i in range(0, len(texts), _EMBED_BATCH):
        batch = [t.replace("\n", " ") for t in texts[i:i + _EMBED_BATCH]]
        resp = client.embeddings.create(model=EMBED_MODEL, input=batch)
        out.extend(d.embedding for d in resp.data)
    return out


# ── build ────────────────────────────────────────────────────────────────────

def build(embed: bool = False) -> dict:
    pages = sorted(p for p in WIKI_DIR.glob("*/index.md"))
    chunks = [c for c in (parse_page(p) for p in pages) if c]

    INDEX_DIR.mkdir(exist_ok=True)
    (INDEX_DIR / "chunks.json").write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    meta = {
        "built": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "module_count": len(chunks),
        "embedding": {
            "enabled": bool(embed),
            "provider": EMBED_PROVIDER,
            "model": EMBED_MODEL,
            "dim": EMBED_DIM,
        },
    }

    if embed:
        import numpy as np  # lazy: doar în mod vectorial
        vectors = np.asarray(embed_texts([c["text"] for c in chunks]), dtype="float32")
        if EMBED_DIM and vectors.shape[1] != EMBED_DIM:
            raise ValueError(f"Dimensiune {vectors.shape[1]} != EMBED_DIM {EMBED_DIM}")
        np.save(INDEX_DIR / "vectors.npy", vectors)
        meta["embedding"]["dim"] = int(vectors.shape[1])

    (INDEX_DIR / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return meta


def main() -> None:
    ap = argparse.ArgumentParser(description="Construiește indexul de interogare al wiki-ului.")
    ap.add_argument("--embed", action="store_true",
                    help="generează și vectori (.npy) — necesită provider configurat + numpy")
    args = ap.parse_args()
    meta = build(embed=args.embed)
    mode = "lexical+vectorial" if meta["embedding"]["enabled"] else "lexical"
    print(f"Index construit ({mode}): {meta['module_count']} module → {INDEX_DIR}")


if __name__ == "__main__":
    main()
