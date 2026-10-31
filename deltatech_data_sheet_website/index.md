# Product Data Sheet Website (localizat la `deltatech_data_sheet_website/index.md`)

- **Nume Tehnic:** `deltatech_data_sheet_website`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_data_sheet_website
- **Cale Locală:** `odoo-addons/deltatech/deltatech_data_sheet_website`
- **Ultima Ingestie:** `2026-10-31`

#### 1. Sumar

Acest modul extinde magazinul online (website e-commerce) pentru a pune la dispoziția clienților fișele tehnice și fișele cu date de securitate ale produselor. Pe pagina publică a unui produs, vizitatorul primește butoane dedicate prin care poate deschide sau descărca documentația asociată produsului, fără a fi nevoie de asistență din partea vânzătorului. Butoanele apar automat, fără configurare suplimentară, doar pentru produsele care au documente atașate.

#### 2. Funcționalități Cheie

- Adaugă pe pagina de produs din website butonul „Show Data Sheet" (Afișare fișă tehnică), afișat doar dacă șablonul de produs are o fișă tehnică atașată.
- Adaugă pe pagina de produs din website butonul „Show Safety Data Sheet" (Afișare fișă cu date de securitate), afișat doar dacă șablonul de produs are o fișă cu date de securitate atașată.
- Butoanele trimit direct la document, iar vizitatorul îl poate deschide sau descărca în browser; produsele fără documente nu afișează niciun buton.
- Pregătirea datelor se face în backend: fișele se atașează șablonului de produs din **Inventar > Produse > Produse** (sau **Vânzări > Produse**), folosind câmpurile din modulul [deltatech_data_sheet](../deltatech_data_sheet/index.md).
- Pe site, butoanele se văd în secțiunea de documente de sub descrierea produsului, din pagina de detaliu accesată prin `/shop`.

#### 3. Dependențe

- `website_sale`
- [deltatech_data_sheet](../deltatech_data_sheet/index.md)

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul se concentrează pe extinderea interfeței publice a produsului prin butoanele de acces la fișele tehnice. Componenta cheie este șablonul de website definit în `views/templates.xml`, care injectează butoanele de afișare a fișelor pe pagina publică a produsului.

**Vizualizări**

- `product_data_sheet`: șablon moștenit din `website_sale.product`, care adaugă în blocul `product_documents` butoanele către `data_sheet_id` și `safety_data_sheet_id` (legături `/web/content/<id>`).

#### 5. Conexiuni

- [deltatech_data_sheet](../deltatech_data_sheet/index.md): modulul de bază care definește fișele tehnice și fișele cu date de securitate ale produselor; acest modul doar le expune în magazinul online.
