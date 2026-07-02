# Romania - Data Contabilă Mișcări de Stoc (Posting Date) (localizat la `l10n_ro_stock_posting_date/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_posting_date`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_posting_date](https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_posting_date)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_posting_date`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o **dată contabilă (Posting Date)** pe operațiile de stoc — similar conceptului din SAP — pentru companiile din România, și o pune sub un control care împiedică datarea ce ar strica ordinea cronologică a valorizării. Astfel, echipa de contabilitate poate stabili exact în ce zi contabilă se înregistrează o recepție, o livrare sau un transfer, fără riscul de a rupe ordinea costurilor FIFO/CMP prin operații datate necorespunzător.

#### 2. Funcționalități Cheie

- Expune un câmp „Posting Date" (dată contabilă) pe operațiile de stoc (`stock.picking`), separat de data efectivă de validare.
- La validare, data contabilă aleasă este propagată către **toate** notele generate: valorizarea nativă Odoo, recepția fără factură (371 = 408), transferul valoric între gestiuni și storno-ul de retur — printr-un mecanism unic bazat pe contextul `force_period_date`.
- Control activabil per companie care blochează o dată contabilă atunci când:
  - este în **viitor**;
  - este înainte de **ultima mișcare valorizată** a aceluiași produs (ar desincroniza ordinea costurilor FIFO/CMP);
  - la **retur**, este înainte de mișcarea originală pe care o stornează (barieră absolută — un retur nu poate precede recepția/livrarea inversată);
  - cade într-o **perioadă contabilă blocată** (lock date fiscal/TVA/hard lock);
  - opțional, este mai devreme de **prima zi a lunii precedente**.
- Granularitatea verificării „ultimei postări" urmează granularitatea valorizării native Odoo 19: implicit pe `(produs, companie)`.
- Setări dedicate în Configurare Inventar/Contabilitate pentru activarea controlului și a restricției pe luna precedentă.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `stock.move` (extins): calculează dacă mișcarea intră sub controlul datei contabile (`_l10n_ro_posting_control_active`), rezolvă data contabilă efectivă (`_l10n_ro_resolve_posting_date`), validează cele cinci bariere cronologice (`_l10n_ro_check_posting_date`) și suprascrie `_action_done` pentru a procesa mișcările grupat pe dată contabilă via `force_period_date`.
- `stock.picking` (extins): adaugă câmpul `l10n_ro_posting_date` (dată contabilă a operației) și reaplică `date_done` cu data contabilă după ce nucleul îl suprascrie cu data curentă.
- `res.company` (extins): adaugă comutatoarele `l10n_ro_posting_date_control` (activează controlul) și `l10n_ro_posting_restrict_last_month` (restricționează la luna precedentă).
- `res.config.settings` (extins): expune cele două câmpuri de companie în ecranul de configurare.

**Vizualizări**

- `view_picking_form_l10n_ro_posting_date`: adaugă câmpul „Posting Date" pe formularul de transfer stoc (`stock.picking`), lângă `date_done`.
- `vpicktree_l10n_ro_posting_date`: adaugă coloana „Posting Date" (ascunsă implicit) în lista de transferuri.
- `res_config_settings_view_form_l10n_ro_posting_date`: adaugă secțiunea de setări pentru controlul datei contabile în Configurare, sub secțiunea de costuri suplimentare.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): respectă același context `force_period_date` pentru a propaga data contabilă și pe notele de gestiune RO (RNI, transfer valoric între gestiuni).
