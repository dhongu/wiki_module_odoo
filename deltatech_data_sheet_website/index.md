# Product Data Sheet Website (localizat la `deltatech_data_sheet_website/index.md`)

- **Nume Tehnic:** `deltatech_data_sheet_website`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_data_sheet_website
- **Cale Locală:** `odoo-addons/deltatech/deltatech_data_sheet_website`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul extinde magazinul online pentru a pune la dispoziția vizitatorilor fișele tehnice și fișele cu date de securitate ale produselor. Când un produs are asociată o astfel de fișă (gestionată prin modulul de bază), pe pagina publică a produsului apar automat butoane de descărcare, fără configurare suplimentară. Astfel, informația tehnică necesară deciziei de cumpărare este direct accesibilă clientului.

#### 2. Funcționalități Cheie

- Buton „Show Data Sheet” pe pagina de produs din website, afișat doar dacă șablonul de produs are o fișă tehnică atașată.
- Buton „Show Safety Data Sheet” pe pagina de produs, afișat doar dacă șablonul de produs are o fișă cu date de securitate atașată.
- Butoanele trimit direct la document, care se poate deschide sau descărca în browser; produsele fără documente nu afișează butoane.
- Fișele se atașează din **Inventar > Produse > Produse** (sau **Vânzări > Produse**), prin câmpurile oferite de `deltatech_data_sheet`; pe site, butoanele apar în pagina de detaliu a produsului (`/shop`), sub descrierea produsului.

#### 3. Dependențe

- `website_sale`
- [deltatech_data_sheet](../deltatech_data_sheet/index.md)

#### 4. Componente Cheie

**Vizualizări**

- `product_data_sheet`: șablon de website care moștenește `website_sale.product` și injectează butoanele de fișă tehnică și fișă de securitate pe pagina produsului.

#### 5. Conexiuni

- [deltatech_data_sheet](../deltatech_data_sheet/index.md): modulul de bază care definește fișele tehnice și fișele cu date de securitate ale produselor; acest modul doar le expune în magazinul online.
