---
name: wiki-query
description: Răspunde la întrebări despre modulele Odoo documentate în acest wiki, folosind indexul de retrieval (.index/chunks.json) plus citirea paginilor <modul>/index.md. Recuperează modulele relevante, citește documentația lor și răspunde cu citări către pagini. Folosește când utilizatorul întreabă "ce modul face X", "spune-mi despre modulul Y", "ce module depind de Z", "care modul rezolvă ...".
---

# Interogare wiki module Odoo (răspuns)

Latura de **interogare** a acestui wiki. NU regenerează documentația (aceea se face din
monorepo-ul Odoo cu skill-ul `wiki-module`) și NU rulează Odoo — citește doar paginile din
acest repo și răspunde.

> **Căi:** acest skill presupune că rădăcina proiectului deschis în Claude Code este **acest
> repo wiki** (`wiki_module_odoo`). Toate căile sunt relative la rădăcină: `scripts/...`,
> `<modul>/index.md`, `.index/...`. Dacă lucrezi în schimb din monorepo-ul Odoo, prefixează cu
> `wiki_module_odoo/`.

Sursa de retrieval este indexul determinist din `.index/`, construit de `scripts/wiki_index.py`.
Retrieval-ul e **hibrid**: lexical implicit, vectorial automat dacă `.index/meta.json` are
`embedding.enabled == true`. Tu, ca agent, nu te ocupi de embeddings — `scripts/wiki_search.py`
o face transparent.

## Argumente

`$ARGUMENTS` este întrebarea utilizatorului în limbaj natural (ex: „ce modul face export către
SAGA?", „care module extind account.move?", „spune-mi despre `l10n_ro_stock_sheet`").

## Pași de execuție

### 1. Asigură indexul

Verifică dacă există `.index/chunks.json`. Dacă **lipsește** sau pare vechi (au apărut pagini noi
de la ultima construire), reconstruiește-l — e ieftin, determinist și nu are nevoie de codul
Odoo, doar de paginile markdown din acest repo:

```bash
python3 scripts/wiki_index.py
```

Nu reconstrui indexul la fiecare întrebare dacă există deja și e recent.

### 2. Recuperează modulele relevante

```bash
python3 scripts/wiki_search.py "<întrebarea>" -k 6 --json
```

Întoarce top-K module cu `module`, `path`, `summary`, `dependencies`, `score`.

- Dacă întrebarea **numește explicit un modul** (`l10n_ro_stock_sheet`), sari peste scor și
  țintește direct `<modul>/index.md`.
- Dacă scorurile sunt toate mici/zero, completează cu o căutare lexicală directă:
  `Grep -ri "<termen cheie>" . --include=index.md -l`. Asta acoperă cazurile în care formularea
  diferă de text (limita retrieval-ului lexical — vezi nota despre vectori).

### 3. Citește și sintetizează

1. Citește integral paginile `<modul>/index.md` ale modulelor de top (de obicei 2–4). Nu te baza
   doar pe sumar — răspunsul corect e în pagină (Funcționalități, Componente, Conexiuni).
2. Urmărește **linkurile de dependențe/conexiuni** (`[dep](../dep/index.md)`) dacă întrebarea
   cere relații între module.
3. Pentru „ce depinde de X" / „ce extinde X", caută X în câmpurile `dependencies`/`connections`:
   `Grep -rl "(\\.\\./X/index\\.md)" . --include=index.md` sau filtrează JSON-ul din pasul 2.

### 4. Răspunde

- În **română corectă, cu diacritice**, concis și business.
- **Citează mereu** modulele cu link Markdown relativ către pagina lor, ex:
  `[deltatech_saga](deltatech_saga/index.md)`.
- Distinge clar ce e **documentat** de ce **presupui**. Dacă wiki-ul nu acoperă întrebarea,
  spune asta — nu inventa. Dacă modulul lipsește complet din wiki, semnalează că trebuie
  documentat (ingestie din monorepo cu `wiki-module`).
- Nu lista module irelevante doar pentru că au apărut cu scor mic în retrieval.

## Notă: lexical vs. vectorial (hibrid)

Implicit retrieval-ul e **lexical** — potrivire pe termeni. Merge foarte bine când întrebarea
folosește cuvinte care apar în documentație. Limita lui: o întrebare parafrazată poate rata —
de-aia pasul 2 are fallback pe `Grep`, iar arhitectura e pregătită pentru vectori.

Pentru căutare **semantică**: configurează providerul în `scripts/wiki_index.py`
(`EMBED_PROVIDER/EMBED_MODEL/EMBED_DIM` + `embed_texts`), rulează `python3 scripts/wiki_index.py
--embed`, și gata — `wiki_search.py` combină automat cosine cu lexicalul, folosind același model
salvat în `.index/meta.json`. Nicio schimbare în acest skill. Atenție: mediul trebuie să aibă
egress către providerul de embeddings, atât la `--embed` cât și la fiecare interogare semantică.
