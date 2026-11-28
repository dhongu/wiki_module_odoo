# Romania - Corecție la instalarea SAF-T (localizat la `l10n_ro_saft_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_fix`
- **Versiune:** `20.0.1.2.4`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_fix](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_fix)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_fix`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul corectează codurile SAF-T `TaxCode` greșite pe taxele cu cotele de TVA de 21% și 11% și împiedică instalarea `l10n_ro_saft` să creeze taxe fără nume. De la 01.08.2025 (Legea 141/2025) cotele din România sunt 21%/11%, iar ANAF a alocat coduri noi pentru ele; versiunile mai vechi ale `l10n_ro_saft` scriau pe aceste taxe codurile cotelor de 19%/9%. Modulul rescrie codurile greșite pe taxele existente și protejează încărcarea datelor parțiale. Este o soluție temporară, de eliminat după ce toate bazele au codurile corecte.

#### 2. Funcționalități Cheie

- Corectează codurile SAF-T `TaxCode` ale taxelor de 21%/11%, atât în datele șablonului (instalări noi), cât și, printr-un `post_init_hook`, pe taxele care au deja scris codul greșit; corecția apare în jurnalul serverului.
- Pe Odoo 20.0, versiunile recente ale `l10n_ro_saft` au deja codurile corecte, deci modulul ajută doar bazele în care `l10n_ro_saft` a fost instalat cu o versiune care scria codurile de 19%/9%.
- Restrânge `account.chart.template._load_data()` astfel încât payload-urile parțiale de `account.tax` (doar `id`, `l10n_ro_saft_tax_type_id`, `l10n_ro_saft_tax_code`) să actualizeze doar taxe existente; eroarea „Missing required value for the field 'Nume taxa'" nu mai apare.
- Referințele de taxă lipsă pe companie sunt sărite, cu un avertisment în jurnal (pe 20.0 rândul apare doar la încărcări directe, deoarece nucleul sare deja aceste date).
- Dacă taxele sărite (ex. cele trei taxe „9% Art. 3") sunt totuși necesare pentru cota tranzitorie de 9%, se încarcă mai întâi din planul de conturi românesc, apoi se actualizează `l10n_ro_saft`.
- Nu necesită configurare; creările legitime (payload complet, cu `name`) trec neatinse către comportamentul standard.

#### 3. Dependențe

- `l10n_ro`

Notă intenționată: modulul **nu** declară `l10n_ro_saft` ca dependență, deliberat (ordinea de încărcare a modulelor, vezi Componente Cheie).

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extindere, `AbstractModel`): suprascrie `_load_data()` — pentru payload-uri `account.tax` fără câmpul `name`, actualizează doar taxele existente pe companie; restul trece către `super()`.

**Vizualizări**

*Modulul nu definește vizualizări.*

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): corectează la instalare codurile SAF-T greșite de pe taxele existente cu cota 21%/11%.

**Mecanism de ordonare a încărcării**

- Modulul depinde doar de `l10n_ro` (adâncime 11 față de `base`), iar `l10n_ro_saft` are adâncime 13; Odoo încarcă modulele în ordinea (fază, adâncime, nume), deci acest modul se instalează înaintea lui `l10n_ro_saft`. Adăugarea lui `l10n_ro_saft` în `depends` ar muta modulul după el și ar anula fix-ul.

#### 5. Conexiuni

- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): afectat indirect, întrucât depinde de `l10n_ro_saft`.
- `l10n_ro_saft`: modulul standard a cărui încărcare de taxe este corectată; nu are pagină wiki proprie.
