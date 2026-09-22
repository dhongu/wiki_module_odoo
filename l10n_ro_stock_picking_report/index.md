# Romania - Terrabit - Picking Reports (localizat la `l10n_ro_stock_picking_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_picking_report`
- **Versiune:** `19.0.1.3.6`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_picking_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_picking_report`
- **Ultima Ingestie:** `2026-09-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă rapoarte specifice gestiunii de stoc din România pentru documentele de mișcare a mărfurilor: recepție (NIR), livrare (aviz de însoțire) și transfer intern (bon de consum). Pe lângă tipărirea acestor documente conforme cu practicile locale, modulul propagă referința din comanda de achiziție în NIR și în factură și oferă opțiuni de configurare pentru afișarea taxelor pe recepție și a conturilor bancare pe rapoarte. Valoarea de afaceri constă în obținerea, direct din Odoo, a documentelor de gestiune uzuale folosite în România, fără prelucrări manuale suplimentare.

#### 2. Funcționalități Cheie

- Rapoarte pentru recepție (NIR — cu taxe, fără taxe și cu preț de vânzare), livrare (aviz simplu și aviz cu preț) și transfer intern (bon de consum, notă de transfer).
- Referința furnizorului din comanda de achiziție este copiată ca document sursă pe NIR și pe factură.
- Opțiune pe companie (`taxes_on_reception`, implicit activă) pentru tipărirea taxelor pe recepție și opțiune (`banks_on_pickings`) pentru tipărirea conturilor bancare pe rapoarte — fără ecran de setări livrat, se ajustează direct pe companie.
- Livrările marcate ca aviz se tipăresc cu titlul „Aviz de însoțire a mărfii" (14-3-6A); livrările obișnuite rămân „Livrare".
- Pe livrările fără comandă de vânzare (aviz, custodie, consignație), raportul cu preț preia prețul din lista de prețuri a partenerului sau, în lipsa acesteia, prețul de listă al produsului.
- NIR-ul cu preț de vânzare afișează prețul înghețat la validarea recepției (din lista de prețuri a locației, dacă există), plus marja și valoarea la preț de vânzare.
- Rapoarte cumulative (Inventar → Raportare → Picking cumulative Report) care adună într-un singur document toate mișcările dintr-un interval, pe tip de operațiune.
- Toate coloanele de cantitate/preț/valoare se exprimă în unitatea de pe document, indiferent dacă recepția e în unitate de referință sau în unitate de ambalare (cutii, baxuri) — cu condiția ca `stock.propagate_uom` să fie `1`.

#### 3. Dependențe

- `base`
- `stock`
- `l10n_ro_report_common`
- `purchase_stock`
- `sale_stock`
- `l10n_ro_stock`
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md)
- `delivery`

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar `readme/FISA_CONSULTANT.md` detaliază fluxul operațional; conform fluxului de ingestie, analiza suplimentară a codului pentru componentele tehnice nu a fost efectuată.

#### 5. Conexiuni

- `l10n_ro_stock`: gestiunea de stoc localizată pe care se bazează rapoartele de picking (indicatorul de aviz).
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): primește delegatul și mijlocul de transport pe factură (câmpuri adăugate de acest modul).
- `l10n_ro_report_common`: elementele comune de layout ale rapoartelor localizării.
- `l10n_ro_stock_picking_comment_template`: modul exclus reciproc (`excludes`), care oferă o abordare alternativă pentru comentariile pe rapoartele de picking.
- `l10n_ro_stock_account` (suita `l10n-romania-oca`): singura sursă care valorizează mișcările interne (`move.value`) — dacă e instalat, bonul de consum și nota de transfer arată prețul și valoarea reale în loc de 0,00; incompatibil cu pachetul CMP de mai jos.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md) / [l10n_ro_stock_pack_cmp](../l10n_ro_stock_pack_cmp/index.md) (suita `l10n_ro_ent`): valorizează transferurile pe cont propriu, cu notă contabilă separată, dar nu scriu `move.value` — bonul de consum și nota de transfer rămân 0,00 chiar dacă nota contabilă corectă există în altă parte.
- [deltatech_cmr_document](../deltatech_cmr_document/index.md): documentul CMR pentru transportul internațional, complementar rapoartelor de livrare ale acestui modul.
