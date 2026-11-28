# Romania - Stock Picking Reports

- **Nume Tehnic:** `l10n_ro_picking_report`
- **Versiune:** `20.0.2.0.4`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_picking_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_picking_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă documentele de stoc cerute în România, tipărite din transferurile de stoc: recepția (NIR), avizul de însoțire a mărfii, bonul de consum și nota de transfer intern. Documentele au formatul românesc, cu datele firmei, gestionarul, delegatul și semnăturile, iar prețurile sunt preluate din comenzi sau din listele de prețuri.

#### 2. Funcționalități Cheie

- Rapoarte pentru recepție, livrare și transfer intern, tipărite din meniul **Tipăriți** al transferului: recepție (NIR), recepție fără TVA, recepție cu preț de vânzare, livrare, livrare cu preț, bon de consum, transfer intern.
- Rapoarte cumulative pe perioadă, pentru recepție cu preț de vânzare și pentru transfer intern, generate printr-un wizard.
- Livrările marcate ca aviz (`l10n_ro_notice`) se tipăresc cu titlul „Aviz de însoțire a mărfii" (14-3-6A); livrările obișnuite rămân „Livrare".
- Pe livrările fără comandă de vânzare (aviz, custodie, consignație), raportul „Delivery with price" preia prețul din lista de prețuri a partenerului sau prețul de listă al produsului.
- Referința din comanda de achiziție este copiată în NIR și în factură.
- Opțiuni în setările României: tipărirea taxelor pe recepție și tipărirea băncilor pe rapoarte.
- Pe documente: delegat și mijloc de transport, gestionar pe locație, listă de prețuri a magazinului pentru prețul de vânzare, cantități în unitatea de ambalare de pe document.
- Fluxul pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `stock`
- [l10n_ro_report_common](../l10n_ro_report_common/index.md)
- `purchase_stock`
- `sale_stock`
- [l10n_ro_stock](../l10n_ro_stock/index.md)
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md)
- `delivery`

#### 4. Componente Cheie

Descrierea din Readme nu detaliază componentele tehnice; lista de mai jos provine din analiza codului.

**Modele**

- `stock.picking` (extins): delegat (`delegate_id`) și mijloc de transport (`mean_transp`).
- `stock.location` (extins): lista de prețuri a magazinului, gestionarul și indicatorul de locație de tip magazin.
- `res.company` / `res.config.settings` (extinse): opțiunile de tipărire a taxelor pe recepție și a băncilor pe documentele de stoc.
- `res.partner` (extins): mijlocul de transport al delegatului.
- `stock.move` (extins): prețul de vânzare folosit în rapoarte.

**Vizualizări**

- `views/l10n_ro_picking_report.xml`: acțiunile de raport (livrare, livrare cu preț, bon de consum, recepție, recepție fără TVA, recepție cu preț de vânzare, transfer intern, variantele cumulative).
- `views/report_picking.xml`: șabloanele QWeb ale documentelor.
- `view_picking_form`, `view_location_form`, `res_config_settings_view_form_reception_taxes`: câmpurile adăugate pe transfer, locație și setări.
- `report/stock_picking_cumulative_view.xml`: wizardul rapoartelor cumulative.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate; `pre_init_hook` pregătește datele la instalare.

#### 5. Conexiuni

- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): modul înrudit pentru rapoartele de transfer.
- [l10n_ro_picking_report_online](../l10n_ro_picking_report_online/index.md): varianta fără Python, pentru Odoo Online; nu se instalează împreună (manifestul o exclude).
- `l10n_ro_stock_picking_comment_template`: exclus prin manifest.
