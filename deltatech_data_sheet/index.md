# Product Data Sheet (localizat la `deltatech_data_sheet/index.md`)

- **Nume Tehnic:** `deltatech_data_sheet`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_data_sheet
- **Cale Locală:** odoo-addons/deltatech/deltatech_data_sheet
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Modulul permite atașarea fișelor tehnice și a fișelor de securitate (PDF) direct pe produs. Documentația tehnică rămâne astfel pe șablonul de produs, ușor de accesat de echipele de vânzări și de logistică, iar documentele publice pot fi partajate în siguranță cu clienții și portalurile.

#### 2. Funcționalități Cheie

- Grup nou **Data Sheet** pe formularul produsului, după grupul Description, cu două câmpuri de atașament PDF.
- **Data Sheet Attachment** — leagă un atașament PDF public (specificații tehnice, pagină de catalog).
- **Safety Data Sheet** — leagă un atașament PDF public pentru documentele de conformitate MSDS / SDS.
- Ambele câmpuri acceptă doar atașamente publice de tip PDF (`application/pdf`, `public = True`); la încărcarea unui fișier nou din câmp, atașamentul se creează public implicit.
- Câmpurile sunt stocate pe `product.template`, deci sunt comune tuturor variantelor produsului.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): `data_sheet_id` și `safety_data_sheet_id`, relații către `ir.attachment` cu domeniul PDF public.

**Vizualizări**

- `product_template_form_view`: grupul **Data Sheet** pe formularul produsului, după grupul `description`.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_data_sheet_website](../deltatech_data_sheet_website/index.md): depinde de acest modul în manifest și folosește fișele atașate pe produs în magazinul online.
