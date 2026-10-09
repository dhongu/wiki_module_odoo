# Deltatech Warranty

- **Nume Tehnic:** `deltatech_warranty`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_warranty
- **Cale Locală:** `odoo-addons/deltatech/deltatech_warranty`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite setarea unei perioade de garanție (în luni) pe produse și tipărirea automată a unei pagini de garanție împreună cu oferta de preț sau comanda de vânzare. Astfel, clientul primește în același document informațiile despre garanția produselor comandate.

#### 2. Funcționalități Cheie

- Câmp „Garanție (luni)" pe fișa produsului, în grupul de informații generale.
- Pagină suplimentară de garanție în raportul de ofertă/comandă de vânzare (după pagina principală, pe o foaie nouă), cu tabel Produs / Garanție (luni).
- Pagina de garanție apare doar dacă cel puțin un produs din comandă are garanție setată; liniile de secțiune/notă și produsele fără garanție sunt omise.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): adaugă câmpul `warranty_months` (Integer, „Warranty (months)").

**Vizualizări**

- `product_template_form_view`: adaugă `warranty_months` în `group_general` din formularul produsului.
- `sale_order_warranty_data`: șablon QWeb moștenit din `sale.report_saleorder_document`, care adaugă pagina de garanție.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu are conexiuni funcționale cu alte module cu pagină wiki.
