# Purchase XLS Import / Export (localizat la `deltatech_purchase_xls/index.md`)

- **Nume Tehnic:** `deltatech_purchase_xls`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_xls
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_xls`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă liniile unei cereri de ofertă dintr-un fișier Excel și exportă în Excel liniile comenzilor de achiziție, astfel încât listele lungi de la furnizori să nu mai fie tastate manual.

#### 2. Funcționalități Cheie

- **Import linii din Excel**: pe o comandă în starea *RFQ*, meniul Acțiuni oferă **Import Purchase Line**; wizardul citește prima foaie a unui `.xlsx` și adaugă câte o linie pe rând. Opțiuni: *Fields* (coloanele, implicit `product_code,default_code,product_name,quantity,price,uom_name`), *Header row*, *Search by internal code*, *Create missing product* (produs stocabil cu preț de la furnizor) și *Is amount* (prețul e valoarea liniei).
- Produsele se găsesc după codul furnizorului, apoi, opțional, după referința internă; un cod ambiguu sau o unitate de măsură diferită oprește importul; fără coloană de preț se folosește lista de prețuri a furnizorului.
- **Export linii**: din meniul Print, **Export Purchase Lines** produce `purchase_order.xlsx` (Code, Internal Code, Name, Qty, Price, Unit of Measure).
- Butonul inteligent **Order lines** deschide liniile comenzii; importul standard de înregistrări de acolo actualizează liniile existente, potrivite după produs.
- Limitări: rândurile fără cod de furnizor sau cu preț nenumeric sunt ignorate fără mesaj; wizardul adaugă mereu linii noi; importul din lista de linii eșuează dacă același produs apare pe mai multe linii. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `import.purchase.line`: wizardul de import al liniilor din Excel.
- `export.purchase.line`: wizardul de export în Excel.
- `purchase.order`: buton inteligent pentru liniile comenzii (`show_order_lines`).
- `purchase.order.line`: import standard adaptat (`load`, `_parse_import_data`).

**Vizualizări**

- `purchase_order_form`: acțiunile de import/export și butonul Order lines.
- `purchase_order_line_tree`: lista liniilor comenzii pentru import.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki.
