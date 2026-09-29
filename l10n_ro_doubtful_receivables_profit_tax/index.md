# Romania - Doubtful Receivables in Corporate Income Tax (localizat la `l10n_ro_doubtful_receivables_profit_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_doubtful_receivables_profit_tax`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_doubtful_receivables_profit_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_doubtful_receivables_profit_tax`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul-punte între evidența creanțelor incerte și impozitul pe profit. Preia automat partea nedeductibilă a ajustărilor pentru deprecierea creanțelor (contul 491) în calculul declarației D101 și în registrul de evidență fiscală, astfel încât contabilul să nu mai transcrie manual diferențele permanente. Se instalează automat când ambele module de bază sunt prezente și nu are meniuri proprii.

#### 2. Funcționalități Cheie

- **Alimentează calculul D101:** partea nedeductibilă a ajustărilor 491 postate în perioadă se adaugă la cheltuielile nedeductibile. Rândul „(+) Ajustări nedeductibile pentru creanțe" arată cât din total provine din creanțe, cu un buton către dosarele respective (**Contabilitate → Impozit pe profit → Calcul impozit**, după **Calculează**).
- **Alimentează registrul de evidență fiscală** (OMFP 870/2005) cu **câte un rând per creanță**, nu un total pe cont. Fiecare rând are valoarea contabilă (ajustarea constituită), valoarea fiscală (partea deductibilă), diferența permanentă și temeiul legal propriu (art. 26 alin. (1) lit. c) sau lit. j) Cod fiscal, cu mențiune separată când condițiile nu sunt îndeplinite și ajustarea e integral nedeductibilă). Rândurile apar la **Generează** în **Contabilitate → Impozit pe profit → Registru de evidență fiscală**.
- **Semnalează dubla numărare:** dacă există o regulă `l10n.ro.tax.adjustment` activă pe contul de cheltuială cu ajustările (6814), pe calculul D101 apare un avertisment; modulul nu corectează tăcut situația. Soluția este ștergerea regulii.
- **Verificare încrucișată:** totalul rândurilor de creanțe din registru trebuie să fie egal cu câmpul din D101 al aceluiași an; o diferență înseamnă că registrul trebuie regenerat.
- **Nu acoperă:** pierderea din scoaterea din evidență (654), ajustarea bazei de TVA (D300) și evidența extracontabilă 8034.

Fluxul detaliat pas cu pas se găsește în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_doubtful_receivables](../l10n_ro_doubtful_receivables/index.md)
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute` (extins): câmpurile `l10n_ro_doubtful_non_deductible` (suma nedeductibilă din dosare), `l10n_ro_doubtful_count` și `l10n_ro_doubtful_rule_overlap`. Suprascrie `_fill_from_accounting` (adaugă suma la `adj_nondeduc`) și adaugă `action_l10n_ro_open_doubtful`. Dosarele luate în calcul sunt cele în stările `adjusted`, `recovered`, `written_off`, cu nota de ajustare postată în perioadă.
- `l10n.ro.tax.register` (extins): `_generate_doubtful_lines` și suprascrierea `action_generate` adaugă un rând de tip `nondeduc` per creanță ajustată în anul fiscal, cu contul de cheltuială din setările companiei.

**Vizualizări**

- `view_profit_tax_compute_form_doubtful`: extinde formularul de calcul D101 cu câmpul nou, butonul „View records" și avertismentul de dublă numărare.
- `view_tax_register_form_doubtful`: notă explicativă deasupra liniilor registrului de evidență fiscală.

**Acțiuni Automate / Acțiuni Server**

- Nu definește.

#### 5. Conexiuni

- [l10n_ro_doubtful_receivables](../l10n_ro_doubtful_receivables/index.md): sursa dosarelor de creanțe incerte (model `l10n.ro.doubtful.receivable`, sumele deductibil/nedeductibil, temeiul fiscal, contul de cheltuială din companie).
- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): calculul D101, registrul de evidență fiscală și regulile `l10n.ro.tax.adjustment`.
