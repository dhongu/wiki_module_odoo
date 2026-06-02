# Product Data Sheet Website (localizat la `deltatech_data_sheet_website/index.md`)

- **Nume Tehnic:** `deltatech_data_sheet_website`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_data_sheet_website
- **Cale Locală:** `odoo-addons/deltatech/deltatech_data_sheet_website`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul extinde magazinul online (website e-commerce) pentru a pune la dispoziția clienților fișele tehnice și fișele cu date de securitate ale produselor. Pe pagina publică a unui produs, vizitatorul primește butoane dedicate prin care poate deschide și consulta documentația asociată produsului, fără a fi nevoie de asistență din partea vânzătorului. Astfel, informația tehnică relevantă pentru decizia de cumpărare devine direct accesibilă online.

#### 2. Funcționalități Cheie

- Adaugă pe pagina de produs din website butonul „Show Data Sheet" (Afișare fișă tehnică), care permite vizualizarea fișei tehnice asociate șablonului de produs.
- Adaugă pe pagina de produs din website butonul „Show Safety Data Sheet" (Afișare fișă cu date de securitate), care permite vizualizarea fișei cu date de securitate asociate șablonului de produs.

#### 3. Dependențe

- `website_sale`
- [deltatech_data_sheet](../deltatech_data_sheet/index.md)

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, modulul se concentrează pe extinderea interfeței publice a produsului prin butoanele de acces la fișele tehnice. Componenta cheie este șablonul de website definit în `views/templates.xml`, care injectează butoanele de afișare a fișelor pe pagina publică a produsului.

#### 5. Conexiuni

- [deltatech_data_sheet](../deltatech_data_sheet/index.md): modulul de bază care definește fișele tehnice și fișele cu date de securitate ale produselor; acest modul doar le expune în magazinul online.
