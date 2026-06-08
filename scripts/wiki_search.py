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


# ── rerank semantic cu Claude (folosește ANTHROPIC_API_KEY din Anthropic Console) ──

# Model ieftin pentru rerank. Schimbabil cu --rerank-model. Haiku 4.5 = $1/$5 per 1M:
# un rerank (≈1,5K tokens in + ~200 out pe ~12 candidați) costă sub $0,003.
RERANK_MODEL = "claude-haiku-4-5"

_RERANK_SCHEMA = {
    "type": "object",
    "properties": {
        "ranking": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "module": {"type": "string"},
                    "relevance": {"type": "integer"},  # 0–100
                },
                "required": ["module", "relevance"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["ranking"],
    "additionalProperties": False,
}


def _rerank_with_claude(query: str, candidates: list[dict], model: str) -> dict | None:
    """Reordonează semantic candidații cu un apel Claude ieftin.

    Întoarce {module: relevance} sau None dacă apelul eșuază (lipsă cheie/egress/SDK) —
    caz în care căutarea cade pe ordinea lexicală. Cheia se ia din mediu
    (ANTHROPIC_API_KEY), exact cea din Anthropic Console.
    """
    try:
        import anthropic
    except ImportError:
        print("⚠️  pachetul `anthropic` lipsește (pip install anthropic) — folosesc lexical.",
              file=sys.stderr)
        return None
    try:
        client = anthropic.Anthropic()  # citește ANTHROPIC_API_KEY din mediu
        listing = "\n".join(
            f"- {c['module']}: {(c.get('summary') or '')[:300]}" for c in candidates
        )
        resp = client.messages.create(
            model=model,
            max_tokens=1024,
            system=(
                "Ești un asistent care selectează module Odoo relevante pentru o întrebare. "
                "Primești o întrebare și o listă de module candidate (nume tehnic + sumar). "
                "Întoarce un scor de relevanță 0–100 pentru fiecare modul candidat, unde 100 = "
                "răspunde direct la întrebare, 0 = irelevant. Bazează-te pe sensul întrebării, "
                "nu doar pe cuvinte comune. Include doar module din lista dată."
            ),
            messages=[{"role": "user", "content": f"Întrebare: {query}\n\nModule candidate:\n{listing}"}],
            output_config={"format": {"type": "json_schema", "schema": _RERANK_SCHEMA}},
        )
        text = next(b.text for b in resp.content if b.type == "text")
        ranking = json.loads(text).get("ranking", [])
        return {r["module"]: r["relevance"] for r in ranking}
    except Exception as e:
        print(f"⚠️  rerank Claude eșuat ({e}) — folosesc lexical.", file=sys.stderr)
        return None


def search(query: str, k: int = 5, rerank: bool = False,
           rerank_model: str = RERANK_MODEL, candidates: int = 12,
           alpha: float = 0.5) -> list[dict]:
    """alpha = ponderea pe similaritatea semantică (cosine) în blend, 0..1.
    0 = doar lexical, 1 = doar vectori. Implicit 0.5 (egal). Ignorat fără vectori."""
    chunks, meta = _load()
    lex = _lexical_scores(query, chunks)
    vec = _vector_scores(query, chunks, meta)
    if vec is not None:
        lo, hi = min(lex), max(lex) or 1.0
        lex_n = [(s - lo) / (hi - lo + 1e-9) for s in lex]
        final = [(1 - alpha) * a + alpha * b for a, b in zip(lex_n, vec)]
    else:
        final = lex
    ranked = sorted(zip(chunks, final), key=lambda x: x[1], reverse=True)
    ranked = [(c, s) for c, s in ranked if s > 0]

    if rerank and ranked:
        # etapa 1 (retrieval lexical) → candidați; etapa 2 (Claude) → reordonare semantică
        shortlist = [c for c, _ in ranked[:candidates]]
        scores = _rerank_with_claude(query, shortlist, rerank_model)
        if scores:
            reranked = sorted(shortlist, key=lambda c: scores.get(c["module"], -1), reverse=True)
            out = []
            for c in reranked[:k]:
                rel = scores.get(c["module"], 0)
                if rel <= 0:
                    continue
                out.append({
                    "module": c["module"], "friendly_name": c.get("friendly_name"),
                    "path": c["path"], "summary": c.get("summary"),
                    "dependencies": c.get("dependencies", []), "score": rel,
                    "scorer": f"claude:{rerank_model}",
                })
            return out

    out = []
    for c, score in ranked[:k]:
        out.append({
            "module": c["module"], "friendly_name": c.get("friendly_name"),
            "path": c["path"], "summary": c.get("summary"),
            "dependencies": c.get("dependencies", []), "score": round(score, 4),
            "scorer": "lexical",
        })
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description="Caută module în indexul wiki.")
    ap.add_argument("query", help="întrebarea / cuvinte cheie")
    ap.add_argument("-k", type=int, default=5, help="câte rezultate (implicit 5)")
    ap.add_argument("--json", action="store_true", help="ieșire JSON")
    ap.add_argument("--rerank", action="store_true",
                    help="reordonare semantică cu Claude (necesită ANTHROPIC_API_KEY + egress)")
    ap.add_argument("--rerank-model", default=RERANK_MODEL,
                    help=f"modelul de rerank (implicit {RERANK_MODEL})")
    ap.add_argument("--candidates", type=int, default=12,
                    help="câți candidați lexicali trimit la rerank (implicit 12)")
    ap.add_argument("--alpha", type=float, default=0.5,
                    help="pondere semantică (cosine) în blend, 0..1 (implicit 0.5; 1 = doar vectori)")
    args = ap.parse_args()

    results = search(args.query, k=args.k, rerank=args.rerank,
                     rerank_model=args.rerank_model, candidates=args.candidates,
                     alpha=args.alpha)
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
