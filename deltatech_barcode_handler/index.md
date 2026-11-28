# Barcode Handler Widget

- **Nume Tehnic:** `deltatech_barcode_handler`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_barcode_handler
- **Cale Locală:** `odoo-addons/bitshop/deltatech_barcode_handler`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care oferă widgetul de formular `deltatech_barcode_handler`, în locul widgetului `barcode_handler` eliminat din modulul `barcodes` în Odoo 20. Este partajat de modulele de coduri de bare, astfel încât clientul web să se încarce corect când sunt instalate împreună.

#### 2. Funcționalități Cheie

- Un câmp afișat cu `widget="deltatech_barcode_handler"` (de regulă câmpul invizibil `_barcode_scanned`) primește fiecare cod de bare citit de scanner pe formular, iar onchange-ul său face restul.
- Folosit de *Barcode Picking* (`deltatech_barcode_picking`) și *Barcode Sale* (`deltatech_barcode_sale`); fiecare își înregistra propria copie a widgetului, iar clientul web nu se încărca dacă ambele erau instalate.
- Nu are meniuri și nu necesită configurare; scanarea se vede în fișa consultantului, pe formularul unei oferte.

#### 3. Dependențe

- `barcodes`

#### 4. Componente Cheie

**Modele**

- Fără modele.

**Vizualizări**

- Widgetul JS `deltatech_barcode_handler` (`static/src/js/barcode_handler_field.esm.js`), plus teste unitare în `web.assets_unit_tests`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_barcode_picking](../deltatech_barcode_picking/index.md): folosește widgetul pentru scanare la transferuri.
- [deltatech_barcode_sale](../deltatech_barcode_sale/index.md): folosește widgetul pentru scanare la vânzări.
