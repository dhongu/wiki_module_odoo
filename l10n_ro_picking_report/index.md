# Romania - Terrabit - Picking Reports (localizat la `l10n_ro_picking_report/index.md`)

- **Nume Tehnic:** `l10n_ro_picking_report`
- **Versiune:** `19.0.2.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_picking_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_picking_report`
- **Ultima Ingestie:** `2026-10-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă rapoarte specifice gestiunii de stoc din România pentru documentele de mișcare a mărfurilor: recepție (NIR), livrare (aviz de însoțire) și transfer intern (bon de consum, notă de transfer). Pe lângă tipărirea acestor documente conforme cu practicile locale, modulul propagă referința din comanda de achiziție în NIR și în factură și oferă opțiuni de configurare pentru afișarea taxelor pe recepție și a conturilor bancare pe rapoarte. Valoarea de afaceri constă în obținerea, direct din Odoo, a documentelor de gestiune uzuale folosite în România, fără prelucrări manuale suplimentare.

**Redenumire (12.10.2026, versiunea 2.0.0).** Modulul se numea anterior `l10n_ro_stock_picking_report`; numele tehnic respectiv este deja ocupat pe Odoo Apps de OCA (seria 14.0), de aceea a fost schimbat în `l10n_ro_picking_report`. Bazele de date care au instalat modulul vechi sunt migrate automat (vezi secțiunea 4, `pre_init_hook`), fără pierderea câmpurilor, a view-urilor, a rapoartelor sau a setărilor.

#### 2. Funcționalități Cheie

- Rapoarte pentru recepție (NIR — cu taxe, fără taxe și cu preț de vânzare), livrare (aviz simplu și aviz cu preț) și transfer intern (bon de consum, notă de transfer).
- Referința furnizorului din comanda de achiziție este copiată ca document sursă pe NIR și pe factură.
- Opțiune pe companie (`taxes_on_reception`, implicit activă) pentru tipărirea taxelor pe recepție și opțiune (`banks_on_pickings`) pentru tipărirea conturilor bancare pe rapoarte — fără ecran de setări livrat (vizualizarea de setări e dezactivată în manifest), se ajustează direct pe companie.
- Livrările marcate ca aviz se tipăresc cu titlul „Aviz de însoțire a mărfii" (14-3-6A); livrările obișnuite rămân „Livrare".
- Pe livrările fără comandă de vânzare (aviz, custodie, consignație), raportul cu preț preia prețul din lista de prețuri a partenerului sau, în lipsa acesteia, prețul de listă al produsului.
- NIR-ul cu preț de vânzare afișează prețul înghețat la validarea recepției (din lista de prețuri a locației, dacă există), plus marja și valoarea la preț de vânzare.
- Pe transfer se completează delegatul și mijlocul de transport (preluat implicit de pe partener); aceste câmpuri ajung și pe factură.
- Rapoarte cumulative (Inventar → Raportare → Picking cumulative Report) care adună într-un singur document toate mișcările dintr-un interval, pe tip de operațiune.
- Toate coloanele de cantitate/preț/valoare se exprimă în unitatea de pe document, indiferent dacă recepția e în unitate de referință sau în unitate de ambalare (cutii, baxuri) — cu condiția ca `stock.propagate_uom` să fie `1`.
- Fluxul operațional pas cu pas (alegerea documentului din meniul Tipăriți, configurare, verificări) este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `stock`
- `l10n_ro_report_common`
- `purchase_stock`
- `sale_stock`
- `l10n_ro_stock`
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md)
- `delivery`

Modul exclus reciproc (`excludes`): `l10n_ro_stock_picking_comment_template`.

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): câmpurile `delegate_id` (delegat) și `mean_transp` (mijloc de transport), transmise în factură; numele fișierului tipărit; atașarea semnăturii.
- `stock.move` (extins): `l10n_ro_sale_price` — prețul de vânzare înghețat la validarea recepției (înainte de crearea înregistrărilor de stoc, ca NIR-ul și eventuala notă de magazin să folosească același preț).
- `stock.location` (extins): `store_pricelist_id` (lista de prețuri a locației), `user_id` (gestionar), `is_store` (calculat).
- `purchase.order` (extins): propagă referința comenzii în transfer prin `_prepare_picking`.
- `res.company` / `res.config.settings` (extinse): `taxes_on_reception`, `banks_on_pickings`.
- `res.partner` (extins): `mean_transp` implicit.
- `stock.picking.cumulative` (model tranzitoriu): wizardul/raportul cumulativ (interval, tip de operațiune); acces pentru grupul `stock.group_stock_user`.
- Modele abstracte de raport `report.abstract_report.delivery_report` și `report.abstract_report.reception_report`, din care derivă rapoartele `report.l10n_ro_picking_report.*`.

**Vizualizări**

- `view_picking_form` (`stock_view.xml`): delegat și mijloc de transport pe transfer.
- `view_location_form` (`stock_location_view.xml`): lista de prețuri și gestionarul pe locație.
- `stock_picking_cumulative_view.xml`: formularul și acțiunea raportului cumulativ.
- Șabloane QWeb în `report_picking.xml`: `report_delivery`, `report_delivery_price`, `report_consume_voucher`, `report_internal_transfer`, `report_reception`, `report_reception_no_tax`, `report_reception_sale_price`, `report_c_internal_transfer`, `report_c_recep_sale_price` și părțile comune (`report_title`, `report_address`, `report_totals`, `report_delivery_info`, semnături).

**Acțiuni Automate / Acțiuni Server**

- `pre_init_hook` (`hooks.py`): migrare automată de la numele vechi. Dacă `l10n_ro_stock_picking_report` este instalat, înainte de încărcarea noului modul mută pe noul nume `ir_model_data`, constrângerile (`ir_model_constraint`), relațiile (`ir_model_relation`) și cheile view-urilor, redirecționează dependențele altor module spre noul nume (pașii din `merge_module` al upgrade-util, fără dependență externă), apoi șterge modulul vechi din lista de module. Nu există `ir.cron` sau acțiuni server.
- Rapoartele (`ir.actions.report`) sunt definite în `views/l10n_ro_picking_report.xml`: `action_report_delivery`, `action_report_delivery_price`, `action_report_consume_voucher`, `action_report_reception`, `action_report_reception_no_tax`, `action_report_reception_sale_price`, `action_report_internal_transfer`, `action_report_c_internal_transfer`, `action_report_c_recep_sale_price`.

**Atenție la moștenire:** modulele care moștenesc șabloanele sau rapoartele acestui modul trebuie să folosească prefixul `l10n_ro_picking_report.` (nu `l10n_ro_stock_picking_report.`) în `inherit_id`, `report_name` și referințele `env.ref`.

#### 5. Conexiuni

Module care depind de acesta:

- [l10n_ro_stock_picking_batch_report](../l10n_ro_stock_picking_batch_report/index.md): extensie pentru loturi de transferuri (picking batch), care folosește rapoartele acestui modul.
- [l10n_ro_etransport_batch_enhancement](../l10n_ro_etransport_batch_enhancement/index.md): depinde indirect, prin `l10n_ro_stock_picking_batch_report`.
- [l10n_ro_stock_picking_report_product_expiry](../l10n_ro_stock_picking_report_product_expiry/index.md): extensie a rapoartelor de picking pentru produse cu dată de expirare (`product_expiry`).
- [terrabit_base](../terrabit_base/index.md): metapachet de bază Terrabit, care îl instalează prin dependențe.

Alte legături:

- `l10n_ro_stock`: gestiunea de stoc localizată pe care se bazează rapoartele de picking (indicatorul de aviz).
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): primește delegatul și mijlocul de transport pe factură (câmpuri adăugate de acest modul).
- `l10n_ro_report_common`: elementele comune de layout ale rapoartelor localizării.
- `l10n_ro_stock_picking_comment_template`: modul exclus reciproc (`excludes`), care oferă o abordare alternativă pentru comentariile pe rapoartele de picking.
- `l10n_ro_stock_account` (suita `l10n-romania-oca`): singura sursă care valorizează mișcările interne (`move.value`) — dacă e instalat, bonul de consum și nota de transfer arată prețul și valoarea reale în loc de 0,00; incompatibil cu pachetul CMP de mai jos.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md) / [l10n_ro_stock_pack_cmp](../l10n_ro_stock_pack_cmp/index.md) (suita `l10n_ro_ent`): valorizează transferurile pe cont propriu, cu notă contabilă separată, dar nu scriu `move.value` — bonul de consum și nota de transfer rămân 0,00 chiar dacă nota contabilă corectă există în altă parte.
- [deltatech_cmr_document](../deltatech_cmr_document/index.md): documentul CMR pentru transportul internațional, complementar rapoartelor de livrare ale acestui modul.
