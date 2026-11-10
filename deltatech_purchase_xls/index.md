# Purchase XLS Import / Export (localizat la `deltatech_purchase_xls/index.md`)

- **Nume Tehnic:** `deltatech_purchase_xls`
- **Versiune:** `19.0.1.0.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_xls`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_xls`
- **Ultima Ingestie:** `2026-11-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă liniile unei cereri de ofertă (RFQ) dintr-un fișier Excel și exportă liniile comenzilor de achiziție în Excel, astfel încât listele lungi de articole de la furnizor să nu mai fie introduse manual.

#### 2. Funcționalități Cheie

- **Import linii din Excel:** pe o comandă în starea RFQ, din meniul Acțiuni (roata dințată) se alege **Import Purchase Line**. Wizardul citește prima foaie dintr-un fișier `.xlsx` și adaugă o linie de comandă pentru fiecare rând. Opțiuni:
  - **Fields**: coloanele fișierului, în ordine; implicit `product_code,default_code,product_name,quantity,price,uom_name`, adică formatul produs de export;
  - **Header row**: ignoră primul rând;
  - **Search by internal code**: dacă codul furnizorului nu e găsit, se caută și ca referință internă;
  - **Create missing product**: un produs negăsit este creat ca produs stocabil, cu preț de furnizor pentru furnizorul comenzii; altfel importul se oprește cu un mesaj;
  - **Is amount**: coloana de preț conține valoarea liniei, iar prețul unitar se calculează ca valoare împărțită la cantitate.
- **Regăsirea produselor:** după codul furnizorului din prețurile de furnizor ale furnizorului comenzii (pentru compania comenzii sau fără companie), apoi după referința internă. Un cod de furnizor care corespunde mai multor produse oprește importul. Dacă fișierul nu are coloană de preț, prețul vine din lista de prețuri a furnizorului. O unitate de măsură diferită de cea a produsului oprește importul.
- **Export linii în Excel:** pe una sau mai multe comenzi, din meniul Print se alege **Export Purchase Lines**; rezultă `purchase_order.xlsx` cu coloanele *Code* (codul furnizorului), *Internal Code*, *Name* (denumirea produsului la furnizor, când există), *Qty*, *Price* și *Unit of Measure*.
- **Lista liniilor comenzii:** butonul inteligent **Order lines** de pe comandă deschide lista liniilor. Importul cu funcția standard **Import records** actualizează liniile existente, potrivite după produs (în ordine, când același produs apare pe mai multe linii); rândurile cu produs care nu e pe comandă sunt ignorate. Dacă comanda nu are încă linii, rândurile devin linii noi ale ei.
- **Limitări:** în wizardul de import, un rând fără cod de furnizor și fără cod intern, sau cu un preț care nu e număr, este sărit fără mesaj; wizardul adaugă mereu linii noi, nu actualizează liniile existente.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `import.purchase.line`: wizard de import al liniilor din Excel.
- `export.purchase.line`: wizard de export al liniilor în Excel.
- `purchase.order` / `purchase.order.line` (extinse): deschiderea listei de linii și logica de import standard (`load`) pentru potrivirea liniilor existente.

**Vizualizări**

- `view_import_purchase_line_form`, `view_export_purchase_line_form`: formularele wizardurilor.
- `purchase_order_form`: butonul **Order lines** și acțiunile pe comandă.
- `purchase_order_line_tree`: lista liniilor comenzii.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; doar acțiunile de fereastră `action_import_purchase_line` și `action_working_days_export`.

#### 5. Conexiuni

Nu au fost identificate legături funcționale suplimentare către alte module cu pagină wiki.
