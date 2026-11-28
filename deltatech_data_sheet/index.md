# Product Data Sheet (localizat la `deltatech_data_sheet/index.md`)

- **Nume Tehnic:** `deltatech_data_sheet`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_data_sheet
- **Cale Locală:** `odoo-addons/deltatech/deltatech_data_sheet`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite atașarea fișelor tehnice și a fișelor de securitate (PDF) direct pe produs. Documentația rămâne pe șablonul de produs, la îndemâna echipelor de vânzări și logistică, și poate fi partajată în siguranță cu clienții.

#### 2. Funcționalități Cheie

- Grup „Data Sheet" pe formularul produsului, după grupul Descriere, cu două câmpuri de atașament PDF.
- „Data Sheet Attachment": leagă un atașament PDF public (specificații tehnice, pagină de catalog).
- „Safety Data Sheet": leagă un atașament PDF public pentru documente MSDS / SDS.
- Ambele câmpuri acceptă doar atașamente publice de tip PDF (`application/pdf`, `public = True`), pentru partajare sigură cu clienții și portalul.
- Câmpurile sunt stocate pe `product.template`, deci sunt comune tuturor variantelor produsului.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea este omisă deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită analiza codului.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în acest wiki.
