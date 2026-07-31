# eCommerce Portal (localizat la `deltatech_website_sale_portal/index.md`)

- **Nume Tehnic:** `deltatech_website_sale_portal`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_sale_portal`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_sale_portal`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul îmbunătățește portalul de client din eCommerce (Website Sale), adăugând clienților posibilitatea de a-și căuta și identifica rapid ofertele și comenzile proprii după referința comenzii clientului (`client_order_ref`), pe lângă căutarea standard după numele documentului. Este util companiilor B2B ale căror clienți urmăresc comenzile plasate în Odoo folosind propriul cod de comandă intern.

#### 2. Funcționalități Cheie

- Adaugă în listele portalului de client ("Ofertele mele" / "Comenzile mele") o coloană suplimentară cu referința comenzii clientului (`client_order_ref`).
- Extinde bara de căutare a portalului cu opțiunea de sortare/căutare după "Order Name" și "Client Reference".
- Permite clientului să aleagă unde caută termenul introdus: doar în numele comenzii, doar în referința clientului sau în ambele câmpuri deodată.
- Filtrarea se aplică atât listei de oferte (quotations), cât și listei de comenzi confirmate (orders) din portal.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește sau extinde niciun model Python; toată logica se află într-un controller care extinde portalul de vânzări (`sale.controllers.portal.CustomerPortal`).

**Vizualizări**

- `portal_my_quotations` (extinde `sale.portal_my_quotations`): adaugă o coloană "Reference" cu `client_order_ref` în tabelul ofertelor din portal.
- `portal_my_orders` (extinde `sale.portal_my_orders`): adaugă o coloană "Reference" cu `client_order_ref` în tabelul comenzilor din portal.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, sarcini cron sau acțiuni server în acest modul. Logica de căutare este implementată în controllerul `CustomerPortal` (rutele `portal_my_quotes` și `portal_my_orders` sunt suprascrise pentru a injecta filtrul de căutare și opțiunile din bara de căutare).

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale relevante către alte module cu pagină wiki.
