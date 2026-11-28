# Romania - Data contabilă a mișcărilor de stoc (localizat la `l10n_ro_stock_posting_date/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_posting_date`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_posting_date
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_posting_date`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o dată contabilă (Posting Date) pe operațiile de stoc, similar conceptului din SAP, și o pune sub un control care împiedică datarea ce ar strica ordinea cronologică a valorizării. Echipa de contabilitate poate stabili ziua contabilă a unei recepții, livrări sau a unui transfer, fără riscul de a rupe ordinea costurilor FIFO/CMP.

#### 2. Funcționalități Cheie

- Câmpul **Dată contabilă** pe operațiile de stoc (`stock.picking`), separat de data efectivă de validare.
- La validare, data contabilă se propagă către **toate** notele generate: valorizarea nativă Odoo, recepția fără factură (371 = 408), transferul valoric între gestiuni și storno-ul de retur, prin contextul `force_period_date`.
- Mișcarea de stoc (`stock.move.date`) se datează la data contabilă înainte de calculul valorii, astfel încât FIFO/CMP se calculează direct la acea dată. Data mișcării păstrează ora de pe transfer (sau ora curentă, dacă data contabilă e azi).
- Control activabil per companie, care blochează data contabilă dacă:
  - este în **viitor**;
  - este înainte de **ultima mișcare valorizată** a aceluiași produs;
  - la **retur**, este înainte de mișcarea originală stornată (barieră absolută);
  - cade într-o **perioadă contabilă blocată** (lock date fiscal/TVA/hard lock);
  - opțional, este mai devreme de **prima zi a lunii precedente**.
- Granularitatea verificării urmează valorizarea: implicit pe `(produs, companie)`.
- Se activează din Inventar → Configurare → Setări („Control dată contabilă stoc" și „Restricționează data contabilă la luna precedentă"). Exemplele pas cu pas sunt în fișa consultantului.

#### 3. Dependențe

- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `stock.move` (extins): stabilește dacă mișcarea intră sub control, rezolvă data contabilă efectivă, validează barierele cronologice și scrie data pe mișcare la trecerea în „Efectuat", înainte de calculul valorii.
- `stock.picking` (extins): câmpul `l10n_ro_posting_date` și reaplicarea `date_done` cu data contabilă.
- `res.company` (extins): `l10n_ro_posting_date_control` și `l10n_ro_posting_restrict_last_month`.
- `res.config.settings` (extins): expune cele două comutatoare în setări.

**Vizualizări**

- `view_picking_form_l10n_ro_posting_date`: câmpul „Dată contabilă" pe formularul de transfer.
- `vpicktree_l10n_ro_posting_date`: coloana „Dată contabilă" în lista de transferuri.
- `res_config_settings_view_form_l10n_ro_posting_date`: secțiunea de setări a controlului.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): respectă același context `force_period_date` pe notele de gestiune RO (RNI, transfer valoric între gestiuni).
- [l10n_ro_stock_pack_cmp](../l10n_ro_stock_pack_cmp/index.md): pachetul CMP îl include ca dependență.
- [l10n_ro_stock_pack_fifo](../l10n_ro_stock_pack_fifo/index.md): pachetul FIFO îl include ca dependență.
