# Romania - Stock Custody (localizat la `l10n_ro_stock_custody/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_custody`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_custody
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_custody`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează bunurile primite sau date în custodie, adică mărfuri care circulă între companie și un terț fără transfer de proprietate. Evidența se ține în afara bilanțului, conform OMFP 1802/2014, pe contul **8033 — Valori materiale primite în păstrare sau custodie**, astfel încât aceste bunuri nu distorsionează stocul propriu valorizat și nici rezultatul financiar al companiei.

#### 2. Funcționalități Cheie

- **Custodie primită** — la validarea recepției, modulul setează automat proprietarul (terțul) pe liniile de mișcare (consignație nativă Odoo), astfel încât bunurile nu intră în valorizarea proprie, și generează automat nota extracontabilă **Dr 8033 = Cr 8039**.
- **Stornare la retur** — butonul **Reverse Custody Entry** de pe transferul de stoc stornează automat nota de custodie (Dr 8039 = Cr 8033) la returul bunurilor către terț.
- **Custodie dată** — marcarea transferurilor de ieșire cu bunuri proprii date în custodie la terți; modulul generează automat nota **Dr 357 = Cr 371** (mărfuri aflate la terți / stoc propriu), cu stornare simetrică la retur.
- **Raport Goods in Custody** — listează toate stocurile ținute pe seama terților (quant-uri cu proprietar setat), accesibil din meniul Inventar → Raportare.
- **Proces-verbal predare-primire custodie** — raport PDF imprimabil de pe transferul de stoc, cu lista produselor, cantităților și valorilor, pentru custodie primită sau dată.
- **Conturi configurabile** — conturile de custodie primită (implicit 8033/8039), conturile de custodie dată (implicit 357/371) și jurnalul utilizat se configurează în Contabilitate → Setări, cu fallback automat după codul contului dacă nu sunt setate explicit.

> **Notă de corecție (semnalată la ingestie):** `readme/DESCRIPTION.md` afirmă că tratamentul contabil al „custodiei date" (contul 357) *nu face parte din scope-ul modulului* și că aceasta ar fi doar un marcaj de evidență. Analiza codului (`models/stock_picking.py`, `models/res_company.py`, view-ul de setări) arată însă că modulul **implementează efectiv** contabilizarea on-balance Dr 357 = Cr 371 (cu stornare Dr 371 = Cr 357), inclusiv câmpuri de configurare dedicate (`l10n_ro_custody_given_account_id`, `l10n_ro_custody_stock_account_id`). Secțiunile de mai sus reflectă comportamentul real din cod; DESCRIPTION.md pare neactualizat față de implementare.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): adaugă câmpurile `l10n_ro_custody_type` (Received/Given in custody) și `l10n_ro_custody_move_id` (referință la nota extracontabilă generată); la `button_validate()` generează automat nota de custodie corespunzătoare tipului, și expune acțiunea `action_l10n_ro_reverse_custody()` pentru stornare.
- `res.company` (extins): câmpuri de configurare a conturilor de custodie primită (`l10n_ro_custody_account_id` / `l10n_ro_custody_counterpart_account_id`, implicit 8033/8039) și custodie dată (`l10n_ro_custody_given_account_id` / `l10n_ro_custody_stock_account_id`, implicit 357/371), plus jurnalul dedicat (`l10n_ro_custody_journal_id`); metodele `_l10n_ro_get_custody_account()` și `_l10n_ro_get_custody_balance_account()` caută automat conturile după cod dacă nu sunt setate explicit.
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
- `l10n_ro`: planul de conturi românesc, sursa conturilor off-balance 8033/8039 și a conturilor 357/371 folosite de modul.
