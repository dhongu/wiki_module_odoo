# Partner Match

- **Nume Tehnic:** `deltatech_partner_match`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_partner_match
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_match`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care ține într-un singur loc regulile după care două fișe de partener sunt considerate „același partener”. Modulele care caută un partener existent (importul clienților din marketplace, căutarea de dubluri, importul balanței) recunosc astfel același partener în același fel, oricum ar fi scrise numele, codul fiscal, telefonul sau emailul. Modulul nu adaugă câmpuri, date, meniuri, acțiuni programate sau reguli de acces și nu schimbă nimic singur: oferă doar funcții pe care le apelează alte module, iar decizia (refolosire, semnalare ca posibil duplicat) rămâne la modulul apelant.

#### 2. Funcționalități Cheie

- **Normalizarea numelui**: litere mici, fără diacritice, punctuație și forme juridice (o singură listă pentru România și UE: SRL, SA, PFA, II, GmbH, Ltd, SARL, KFT etc.), cu cuvintele sortate. „S.C. Popescu Ion S.R.L.” și „ion popescu srl” dau aceeași cheie. Formele „SAS”, „AG”, „BV”, „NV”, „RA” nu se elimină, fiind și nume de familie sau inițiale.
- **Normalizarea CUI / TVA**: doar litere și cifre, fără prefixul de țară și fără zerourile din față („RO 012.345” = „12345”); verificarea cifrei de control pentru CUI și CNP românesc și pentru codurile de TVA din UE (`python-stdnum`). Un cod din afara UE nu se poate verifica și nu e considerat greșit.
- **Normalizarea telefonului**: format E.164 (`+40722123456`), după aceeași regulă ca `phone_sanitized` din Odoo; fără biblioteca `phonenumbers` se folosesc formatele românești și prefixele internaționale. Pentru comparația în masă se folosesc ultimele 9 cifre; numerele cu sub 7 cifre sau cu o singură cifră repetată nu se compară.
- **Normalizarea emailului**: `email_normalize` din Odoo.
- **Asemănarea numelor**: `name_similarity` (0–1) asociază fiecare cuvânt cu cel mai apropiat cuvânt din celălalt nume, deci un nume de familie comun nu face două persoane asemănătoare („Ana Popescu” / „Ion Popescu” = 0,67). `token_sort_ratio` și `similar_pairs` (0–100) compară nume întregi, în masă, cu `rapidfuzz` sau, în lipsă, `difflib` pe blocuri limitate.
- **Căutarea candidaților**: `res.partner._find_similar_partners` selectează partenerii care au același CUI, email sau telefon (niciodată după nume singur) și îi întoarce cu scor și motivele potrivirii. Scorul combină numele (0,6), strada (0,25) și localitatea (0,15); strada și localitatea contează doar dacă sunt completate pe ambele părți.
- **Regula județului**: dacă județele diferă și în ambele există o localitate cu acel nume („Satu Nou” în Bacău și în Iași), strada și localitatea nu mai contează. Un județ necunoscut sau care nu se potrivește cu localitatea se ignoră; fără `base_address_extended`, județul nu scade niciodată scorul.
- **Biblioteci opționale** (`phonenumbers`, `rapidfuzz`, `unidecode`): rezultatele pe cheile exacte rămân aceleași fără ele; diferă doar telefoanele altor țări și viteza comparației în masă.
- **Utilizare de către dezvoltatori**: se adaugă modulul în `depends` și se importă `odoo.addons.deltatech_partner_match.tools.partner_match` (`normalize_name`, `normalize_vat`, `check_vat`, `normalize_phone`, `phone_key`, `name_similarity`). Fluxul pas-cu-pas, regulile cu exemple, mesajele frecvente și verificările rămân în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`

Biblioteci Python opționale: `python-stdnum`, `phonenumbers`, `rapidfuzz`, `unidecode`.

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): adaugă metodele `_find_similar_partners` (interfața publică) și ajutoarele `_partner_match_*` (chei, condiții de căutare, scor, motive, regula județului). Nu adaugă câmpuri.

**Vizualizări**

Modulul nu definește vizualizări sau meniuri.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește acțiuni programate, reguli de automatizare sau acțiuni server.

Logica de normalizare și potrivire stă în `tools/partner_match.py` (Python simplu, fără ORM).

#### 5. Conexiuni

- [deltatech_partner_merge](../deltatech_partner_merge/index.md): căutarea de dubluri folosește normalizarea numelui, CUI-ului, telefonului, emailului și străzii și `similar_pairs`; efectul se vede în coloanele Scor și Motive.
- [deltatech_marketplace](../deltatech_marketplace/index.md): la importul clienților apelează `_find_similar_partners` pe email și telefon și decide refolosirea contactului sau marcarea „Posibil duplicat al”.
- [deltatech_ai_trial_balance_import](../deltatech_ai_trial_balance_import/index.md): potrivește partenerii din balanța PDF după CUI normalizat și nume.
- [deltatech_ai_pdf_base](../deltatech_ai_pdf_base/index.md): verifică cifra de control a CUI / CNP / TVA UE citite din PDF (și, prin el, [deltatech_ai_purchase_pdf](../deltatech_ai_purchase_pdf/index.md)).
