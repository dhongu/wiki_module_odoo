# Romania - Accounting Document Type

- **Nume Tehnic:** `l10n_ro_account_move_document_type`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_account_move_document_type
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_move_document_type`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe notele contabile **tipul documentului justificativ** (factură, notă de credit, declarație vamală de import – DVI, chitanță, extras de cont, stat de salarii, decont de cheltuieli sau notă contabilă simplă). Astfel, jurnalele și registrele românești pot arăta, pe fiecare rând, documentul care stă la baza înregistrării, în loc să afișeze „Notă contabilă” pentru tot ce nu este factură.

#### 2. Funcționalități Cheie

- Câmpul **Tip document** (`l10n_ro_document_type`) pe `account.move`, calculat automat și stocat; poate fi modificat manual.
- Facturile și bonurile iau tipul din felul documentului (factură, notă de credit, factură furnizor, bon de vânzare/cumpărare etc.).
- Rândurile de extras bancar sunt *Extras de cont*. O plată într-un jurnal de bancă este *Ordin de plată / Document de bancă* (nota ei se postează pe contul de plăți în curs, înainte de extras, uneori fără reconciliere cu el). În jurnalele de casă ambele sunt *Document de casă*.
- Orice altă notă este *Notă contabilă*, până când modulul care o creează stabilește alt tip (nota DVI din `l10n_ro_customs_dvi`, documentele de casă din `l10n_ro_account_sequence`).
- Pe o notă contabilă, contabilul poate schimba tipul din formular (lângă *Referință*), de exemplu *Import (DVI)* pentru TVA la import înregistrat manual. Câmpul nu apare pe facturi.
- În *Contabilitate > Contabilitate > Note contabile*, coloana **Tip document** este opțională în listă, iar notele se pot filtra și grupa după tip.
- Tipul se recalculează la schimbarea jurnalului, deci o alegere manuală trebuie refăcută după o astfel de schimbare.
- La instalare, tipul se completează direct în SQL (`pre_init_hook`) pentru notele existente, fără recalcul ORM pe baze mari.
- Jurnalul de TVA (cumpărări și vânzări) din `l10n_ro_account_vat_journal` îl folosește în coloana *Tip document*.
- Lista de tipuri este fixă (17 valori); un tip nou cere modificarea modulului. Modulul doar clasifică notele, nu generează și nu modifică înregistrări. Pasul cu pas, exemplul de TVA la import și verificările sunt în fișa consultant.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmpul `l10n_ro_document_type` (Selection, calculat din `move_type`, `journal_id.type`, `origin_payment_id`, `statement_line_id`; stocat, editabil, fără copiere) și metoda `_l10n_ro_get_document_type()`, pe care modulele specializate o suprascriu.

**Vizualizări**

- `view_move_form`: adaugă *Tip document* lângă *Referință*, vizibil doar pe note contabile (`move_type = entry`).
- `view_move_tree`: coloană opțională *Tip document* în lista notelor.
- `view_account_move_filter`: câmp de căutare și grupare după *Tip document*.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Are `pre_init_hook` care creează și completează coloana în SQL la instalare.

#### 5. Conexiuni

- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md): pune *Import (DVI)* pe nota generată din DVI.
- [l10n_ro_account_sequence](../l10n_ro_account_sequence/index.md): pune chitanță/dispoziție pe plățile prin casă.
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md): afișează tipul în coloana *Tip document* a jurnalului de TVA.
