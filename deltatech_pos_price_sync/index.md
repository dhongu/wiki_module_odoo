# POS Price Sync (localizat la `deltatech_pos_price_sync/index.md`)

- **Nume Tehnic:** `deltatech_pos_price_sync`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_price_sync
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_price_sync`
- **Ultima Ingestie:** `2026-11-18`

#### 1. Sumar

Modul nou în 19.0. Trimite instant modificările de preț ale produselor către sesiunile de Punct de Vânzare (POS) deja deschise, astfel încât casierii să vadă mereu prețul corect, fără să închidă și să redeschidă sesiunea. O sesiune deschisă nu recitește prețurile, deci casierul ar continua să vândă la prețul vechi, chiar și după reîncărcarea paginii.

#### 2. Funcționalități Cheie

- Detectează modificările câmpurilor `list_price`/`standard_price` (preț de vânzare și cost) pe produsele disponibile în POS.
- Trimite o notificare live prin bus către toate sesiunile POS deschise, reutilizând același model de canal ca `deltatech_pos_stock`.
- Interfața POS integrează prețul proaspăt direct în modelul din memorie, fără reîncărcare de pagină.
- Rezolvă situația „am schimbat prețul, dar casierul îl vede pe cel vechi chiar și după F5": o sesiune rămasă deschisă nu mai rulează sincronizarea bazată pe `write_date` la reîncărcare.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): suprascrie `write()` pentru a detecta schimbările de `list_price`/`standard_price` pe produsele `available_in_pos` și declanșează `_notify_pos_price_change()`, care caută sesiunile POS cu starea `opened` din companiile relevante și trimite pe bus evenimentul `PRICE_SYNCHRONISATION` cu datele produsului reîncărcate.

**Frontend (assets POS)**

- `pos_price_synchronisation.esm.js`: patch pe `PosStore` — ascultă evenimentul `PRICE_SYNCHRONISATION` în `processServerData()` și, la primirea lui, injectează direct datele noi de produs în modelele POS din memorie (`connectNewData`), fără RPC suplimentar sau reîncărcare.

**Vizualizări**

- Niciuna (`data: []` în manifest).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

Modulul este o completare mică peste `point_of_sale` standard și rulează alături de restul suitei POS Terrabit și de modulele românești de conformitate fiscală, fără suprapuneri:

- [deltatech_pos_stock](../deltatech_pos_stock/index.md): afișează stocul disponibil în POS, pe același canal live prin bus (pattern comun, nu dependență de manifest).
- [deltatech_pos](../deltatech_pos/index.md): tipărește bonuri fiscale și gestionează numerarul pe casa de marcat certificată.
- [deltatech_pos_base](../deltatech_pos_base/index.md): setările casei de marcat și codurile ECR.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): model comun de document fiscal, convertor de format ECR și expeditor Terrabit Connect.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): corectează totalul POS pentru poziții fiscale cu taxă inclusă.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): urmărirea bonurilor AMEF, reconcilierea raportului Z și blocarea sesiunii.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): raportează bonurile fiscale POS în declarația D394 (op. 2).
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): factură de retur și linie de casă dedicate pentru fiecare retur POS.
