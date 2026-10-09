# Romania - Stocuri în custodie (localizat la `l10n_ro_stock_consignment/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_consignment`
- **Nume anterior:** `l10n_ro_stock_custody` (redenumit pe 23.09.2026: numele vechi e ocupat pe Odoo Apps de alt furnizor)
- **Versiune:** `19.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_consignment
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_consignment`
- **Ultima Ingestie:** 2026-10-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează bunurile primite sau date în custodie, adică mărfuri care circulă între companie și un terț fără transfer de proprietate. Evidența se ține în afara bilanțului, conform OMFP 1802/2014, pe contul **8033 — Valori materiale primite în păstrare sau custodie**, astfel încât aceste bunuri nu distorsionează stocul propriu valorizat și nici rezultatul financiar al companiei.

#### 2. Funcționalități Cheie

- **Custodie primită** — la validarea recepției, modulul setează automat proprietarul (terțul) pe liniile de mișcare (consignație nativă Odoo), astfel încât bunurile nu intră în valorizarea proprie, și generează automat nota extracontabilă **Dr 8033 = Cr 803999**.
- **Stornare la retur** — butonul **Reverse Custody Entry** de pe transferul de stoc stornează automat nota de custodie (Dr 803999 = Cr 8033) la returul bunurilor către terț.
- **Contrapartidă comună 803999** — nota de custodie primită folosește contrapartida tehnică comună 803999 din `l10n_ro_off_balance`, nu 8039 (care are funcțiune proprie în OMFP 1802/2014); câmpul „Cont contrapartidă” se completează doar pentru o contrapartidă proprie. La migrarea de la versiunile anterioare, soldul lui 8039 provenit din notele de custodie se mută pe 803999 printr-o notă de transfer **în ciornă** (jurnal EXTR), pe care contabilul o verifică și o postează.
- **Custodie dată** — marcarea transferurilor de ieșire cu bunuri proprii date în custodie la terți; modulul generează automat nota **Dr 357 = Cr 371** (mărfuri aflate la terți / stoc propriu), cu stornare simetrică la retur.
- **Raport Goods in Custody** — listează toate stocurile ținute pe seama terților (quant-uri cu proprietar setat), accesibil din meniul Inventar → Raportare.
- **Proces-verbal predare-primire custodie** — raport PDF imprimabil de pe transferul de stoc, cu lista produselor, cantităților și valorilor, pentru custodie primită sau dată.
- **Conturi configurabile** — conturile de custodie primită (implicit 8033 / contrapartida comună 803999), conturile de custodie dată (implicit 357/371) și jurnalul utilizat se configurează în Contabilitate → Setări. Fallback-uri: contul 8033 se caută automat după cod; contrapartida goală = 803999; jurnalul gol = **EXTR** (Evidență extrabilanțieră). Nota de custodie dată nu ajunge niciodată în EXTR, ci într-un jurnal general bilanțier.

> **Atenție la custodia dată** (din documentația modulului, verificată contabil): nota Dr 357 = Cr 371 se generează **în plus** față de mișcarea de stoc, deci destinația nu trebuie să aibă notă de valorizare proprie (altfel 371 e creditat de două ori) și nu trebuie să fie o locație de tip Client; 357 e corect doar pentru mărfuri (351 materii prime și materiale, 354 produse, 358 ambalaje); valoarea notei este cantitate × cost standard, iar la valoare 0 nu se generează notă; stornarea se calculează la costul de la data returului, deci soldul 357 / 8033 se verifică după retur.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): adaugă câmpurile `l10n_ro_custody_type` (Received/Given in custody) și `l10n_ro_custody_move_id` (referință la nota extracontabilă generată); la `button_validate()` generează automat nota de custodie corespunzătoare tipului, și expune acțiunea `action_l10n_ro_reverse_custody()` pentru stornare.
- `res.company` (extins): câmpuri de configurare a conturilor de custodie primită (`l10n_ro_custody_account_id` / `l10n_ro_custody_counterpart_account_id`, implicit 8033 / 803999) și custodie dată (`l10n_ro_custody_given_account_id` / `l10n_ro_custody_stock_account_id`, implicit 357/371), plus jurnalul dedicat (`l10n_ro_custody_journal_id`); metodele `_l10n_ro_get_custody_account()` și `_l10n_ro_get_custody_balance_account()` caută automat conturile după cod dacă nu sunt setate explicit.
- `stock.picking` — `_l10n_ro_custody_journal()`: jurnalul notei; primită = jurnalul de custodie sau EXTR, dată = jurnal general diferit de EXTR. Contrapartida și jurnalul EXTR vin din `res.company` prin metodele `_l10n_ro_get_off_balance_counterpart()` / `_l10n_ro_get_off_balance_journal()` ale `l10n_ro_off_balance`.
- `res.config.settings` (extins): câmpuri `related` către conturile/jurnalul de custodie de pe companie, editabile din Contabilitate → Setări.

**Vizualizări**

- `view_picking_form_custody`: extinde formularul de transfer de stoc cu câmpul **Custodie** (lângă *Dată programată*), câmpul readonly cu nota generată și butonul **Reverse Custody Entry**.
- `res_config_settings_view_form_custody`: adaugă în Contabilitate → Setări secțiunea „Romania - Stock Custody" cu cele două blocuri de conturi (off-balance pentru custodie primită, on-balance pentru custodie dată) și jurnalul.
- `action_l10n_ro_custody_quants` / `menu_l10n_ro_custody_quants`: acțiune și meniu „Goods in Custody" (Inventar → Raportare) care listează `stock.quant` cu `owner_id` setat.
- `action_report_l10n_ro_custody_pv`: raport QWeb-PDF „Proces-verbal predare-primire custodie", disponibil ca acțiune de imprimare pe `stock.picking`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul; logica de generare/stornare a notelor contabile rulează sincron la validarea transferului (`button_validate`) și la apăsarea butonului de stornare.

#### 5. Conexiuni

- `stock` / `stock_account`: mecanismul de consignație nativ (proprietar pe `stock.quant`/`stock.move.line`) folosit pentru a exclude bunurile primite în custodie din valorizarea proprie.
- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md): contrapartida tehnică comună 803999, jurnalul EXTR și nota de transfer folosită la migrare.
- `l10n_ro`: planul de conturi românesc, sursa contului off-balance 8033 și a conturilor 357/371 folosite de modul.
