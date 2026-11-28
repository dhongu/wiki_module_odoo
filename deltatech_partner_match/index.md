# Partner Match (localizat la `deltatech_partner_match/index.md`)

- **Nume Tehnic:** `deltatech_partner_match`
- **Versiune:** `20.0.1.3.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_partner_match
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_match`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care concentrează într-un singur loc regulile după care se decide dacă două înregistrări de parteneri sunt același partener, astfel încât modulele care caută un partener existent (import marketplace, căutare de dubluri, import de balanță) să îl recunoască la fel. Nu adaugă câmpuri, date, meniuri, acțiuni planificate sau reguli de acces și nu schimbă singur niciun comportament: oferă doar funcții pe care le apelează alte module.

#### 2. Funcționalități Cheie

- Normalizare nume: litere mici, fără diacritice, punctuație și forme juridice (o singură listă pentru România și UE: SRL, SA, PFA, II, GmbH, Ltd, SARL, KFT...), cuvinte sortate; „S.C. Popescu Ion S.R.L." și „ion popescu srl" dau aceeași cheie.
- Normalizare CUI/TVA: fără prefixul de țară și fără zerourile de la început; verifică cifra de control a CUI/CNP românesc sau a unui cod de TVA UE (`python-stdnum`).
- Normalizare telefon: E.164 (`+40722123456`), cu aceeași regulă ca `phone_sanitized` din Odoo; fără biblioteca `phonenumbers` merg formatele românești și prefixul internațional; pentru comparații în masă, ultimele nouă cifre.
- Normalizare e-mail prin `email_normalize` din Odoo.
- Potrivire nume: `name_similarity` (0-1) compară cuvânt cu cuvânt, deci un nume de familie comun nu face două persoane asemănătoare; `token_sort_ratio` și `similar_pairs` (0-100) compară nume întregi în masă (`rapidfuzz` dacă e instalat, altfel `difflib`).
- `res.partner._find_similar_partners(values, domain, keys, limit)` returnează partenerii care au același CUI, e-mail sau telefon (niciodată doar numele), cu scor și cheile comune; localitățile omonime din județe diferite nu contează. Reutilizarea o decide modulul apelant.
- `phonenumbers`, `rapidfuzz` și `unidecode` sunt opționale.
- Utilizare (pentru dezvoltatori): se adaugă modulul în `depends` și se importă `odoo.addons.deltatech_partner_match.tools.partner_match`.

Exemplele de utilizare pe fluxuri reale sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): metoda `_find_similar_partners`.
- `tools/partner_match.py` (Python simplu): `normalize_name`, `normalize_vat`, `check_vat`, `normalize_phone`, `phone_key`, `name_similarity`, `token_sort_ratio`, `similar_pairs`.

**Vizualizări**

- Nu are vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): depinde de modul pentru recunoașterea partenerilor la importul comenzilor.
- [deltatech_ai_pdf_base](../deltatech_ai_pdf_base/index.md): depinde de modul pentru potrivirea partenerilor.
