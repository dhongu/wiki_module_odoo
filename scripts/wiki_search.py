#!/usr/bin/env python3
"""Retrieval peste indexul wiki — latura de INTEROGARE a RAG-ului hibrid.

Citește `wiki_module_odoo/.index/chunks.json` (+ `meta.json`) și întoarce cele mai
relevante module pentru o întrebare, ca să știi ce pagini `index.md` să citești.

MOD LEXICAL (implicit): scoring prin suprapunere de termeni cu ponderare idf, plus
boost pentru potrivire pe numele tehnic și pe dependențe. Rapid, fără egress.

MOD VECTORIAL (când meta.json: embedding.enabled == true): embeduiește query-ul cu
EXACT modelul/dimensiunea din meta.json (prin `wiki_index.embed_texts` — aceeași
funcție ca la ingestie) și combină cosine similarity cu scorul lexical. Asta e
garanția consistenței model↔dimensiune; dacă meta.json nu se potrivește cu
`vectors.npy`, scriptul refuză să ruleze vectorial și cade pe lexical.

Folosire:
    python3 wiki_module_odoo/scripts/wiki_search.py "storno pe clasa 6" -k 5
    python3 wiki_module_odoo/scripts/wiki_search.py "export SAGA" --json
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

WIKI_DIR = Path(__file__).resolve().parent.parent
INDEX_DIR = WIKI_DIR / ".index"

_WORD_RE = re.compile(r"[a-z0-9_ăâîșţțşáàéíóú]+", re.IGNORECASE)
# diacritice → ascii, pentru potrivire tolerantă
_FOLD = str.maketrans("ăâîșşțţ", "aaisstt")


def _tokens(text: str) -> list[str]:
    return [w.lower().translate(_FOLD) for w in _WORD_RE.findall(text or "")]


def _load() -> tuple[list[dict], dict]:
    chunks_path = INDEX_DIR / "chunks.json"
    if not chunks_path.exists():
        sys.exit("Index inexistent. Rulează întâi: python3 "
                 "wiki_module_odoo/scripts/wiki_index.py")
    chunks = json.loads(chunks_path.read_text(encoding="utf-8"))
    meta_path = INDEX_DIR / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    return chunks, meta


def _lexical_scores(query: str, chunks: list[dict]) -> list[float]:
    q_tokens = set(_tokens(query))
    if not q_tokens:
        return [0.0] * len(chunks)
    # idf pe corpus
    df: Counter[str] = Counter()
    doc_tokens: list[Counter] = []
    for c in chunks:
        toks = Counter(_tokens(c.get("text", "")))
        doc_tokens.append(toks)
        for t in toks:
            df[t] += 1
    n = len(chunks)
    idf = {t: math.log(1 + n / (1 + df.get(t, 0))) for t in q_tokens}

    scores = []
    for c, toks in zip(chunks, doc_tokens):
        s = sum(idf[t] * (1 + math.log(toks[t])) for t in q_tokens if toks.get(t))
        # boost: query menționează numele tehnic / o dependență
        name = c.get("module", "").lower()
        if name and name in query.lower():
            s += 5.0
        if any(d.lower() in query.lower() for d in c.get("dependencies", [])):
            s += 1.0
        scores.append(s)
    return scores


def _vector_scores(query: str, chunks: list[dict], meta: dict) -> list[float] | None:
    """Cosine cu vectorii din .npy. Întoarce None dacă nu se poate (cade pe lexical)."""
    emb = meta.get("embedding", {})
    if not emb.get("enabled"):
        return None
    vec_path = INDEX_DIR / "vectors.npy"
    if not vec_path.exists():
        return None
    try:
        import numpy as np
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import wiki_index  # aceeași funcție de embedding ca la ingestie
        mat = np.load(vec_path)
        if mat.shape[0] != len(chunks) or (emb.get("dim") and mat.shape[1] != emb["dim"]):
            print("⚠️  vectors.npy nu se potrivește cu meta.json — folosesc lexical.",
                  file=sys.stderr)
            return None
        qv = np.asarray(wiki_index.embed_texts([query]), dtype="float32")[0]
        mat_n = mat / (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-9)
        qv_n = qv / (np.linalg.norm(qv) + 1e-9)
        return (mat_n @ qv_n).tolist()
    except Exception as e:  # provider indisponibil, fără egress etc.
        print(f"⚠️  embedding query eșuat ({e}) — folosesc lexical.", file=sys.stderr)
        return None


def search(query: str, k: int = 5) -> list[dict]:
    chunks, meta = _load()
    lex = _lexical_scores(query, chunks)
    vec = _vector_scores(query, chunks, meta)
    if vec is not None:
        lo, hi = min(lex), max(lex) or 1.0
        lex_n = [(s - lo) / (hi - lo + 1e-9) for s in lex]
        final = [0.5 * a + 0.5 * b for a, b in zip(lex_n, vec)]
    else:
        final = lex
    ranked = sorted(zip(chunks, final), key=lambda x: x[1], reverse=True)
    out = []
    for c, score in ranked[:k]:
        if score <= 0:
            continue
        out.append({
            "module": c["module"], "friendly_name": c.get("friendly_name"),
            "path": c["path"], "summary": c.get("summary"),
            "dependencies": c.get("dependencies", []), "score": round(score, 4),
        })
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Caută module în indexul wiki.")
    ap.add_argument("query", help="întrebarea / cuvinte cheie")
    ap.add_argument("-k", type=int, default=5, help="câte rezultate (implicit 5)")
    ap.add_argument("--json", action="store_true", help="ieșire JSON")
    args = ap.parse_args()

    results = search(args.query, k=args.k)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return
    if not results:
        print("Niciun modul relevant găsit.")
        return
    for r in results:
        print(f"[{r['score']}] {r['module']} — {r['friendly_name']}")
        print(f"        {r['path']}")
        if r["summary"]:
            print(f"        {r['summary'][:160]}…")


if __name__ == "__main__":
    main()
