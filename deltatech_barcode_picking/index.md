# Barcode Picking (localizat la `deltatech_barcode_picking/index.md`)

- **Nume Tehnic:** `deltatech_barcode_picking`
- **Versiune:** `20.0.2.2.14`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_barcode_picking`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_barcode_picking`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite operatorilor de depozit să adauge produse pe recepții și livrări prin scanarea codului de bare, fără a completa manual liniile transferului. Se pot scana și etichete compuse, care conțin codul produsului și numele lotului, iar cantitatea se înregistrează pe lotul respectiv. Rezultatul este o introducere mai rapidă a datelor și mai puține erori la recepție și la pregătirea comenzilor.

#### 2. Funcționalități Cheie

- Adăugarea de produse pe recepții și livrări prin scanare, cu orice cititor care funcționează ca tastatură (tastează codul și trimite Enter). Cursorul trebuie ținut în afara câmpurilor text. Fiecare scanare adaugă **o unitate**.
- Citirea etichetelor compuse produs + lot, separate prin `-` sau `/` (de exemplu `5940000000024/LOT26`); codul se desparte la ultimul separator. Dacă numele loturilor conțin cratimă, se folosește `/`.
- Lotul scanat trebuie să existe deja; pentru produsele urmărite pe lot, un lot inexistent este refuzat cu eroare. Pe recepții se bifează **Use Existing ones** (grupul **Lots/Serial Numbers**) la tipul de operațiune.
- Pe o recepție în stare Draft, prima scanare adaugă linia, iar următoarele cresc **Demand**; pe un transfer **Ready**, scanarea se adaugă peste cantitatea existentă (se recomandă setarea cantității la 0 înainte).
- La livrări, cererea este o limită: o scanare peste cantitatea rezervată este refuzată. Pentru numărarea prin scanare, **Quantity** se setează la 0 și se salvează. Cu `deltatech_stock_reservation_lock`, pe tipurile cu **Protect Reservations** se scanează față de cantitatea rezervată.
- Cod necunoscut: transferul rămâne neschimbat (**There is no product with barcode …**); un transfer **Done** sau **Cancelled** nu poate fi scanat (**Invalid Operation**).
- Fiecare scanare creează în **Detailed Operations** o linie de 1,00; un lot scanat de mai multe ori apare pe mai multe linii.
- Limitări: scanarea în ajustările de inventar nu este disponibilă în această versiune; casetele **Allowed to add products by scanning** și **Request Effective Date** nu au efect; o scanare în plus nu poate fi anulată prin scanare, ci prin corectarea manuală a cantității.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock`
- [deltatech_barcode_handler](../deltatech_barcode_handler/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): implementează `on_barcode_scanned()` și `_add_product()` pentru adăugarea produselor și loturilor prin scanare, cu verificări de scanabilitate și de cantitate disponibilă.
- `stock.picking.type` (extins): adaugă opțiunile legate de scanare la tipul de operațiune.
- `stock.move` (extins): leagă liniile de operațiuni detaliate de transfer în fluxul de scanare.

**Vizualizări**

- `view_picking_barcode_inherit_form`: adaugă câmpul de captare a scanărilor pe formularul transferului.
- `view_stock_move_line_detailed_operation_tree`: forțează salvarea produsului în lista de operațiuni detaliate, necesar pentru scanarea cu lot.
- `view_picking_type_form`: expune opțiunile de scanare pe tipul de operațiune.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_barcode_sale](../deltatech_barcode_sale/index.md): același principiu de scanare, aplicat pe comenzile de vânzare.
- [deltatech_stock_reservation_lock](../deltatech_stock_reservation_lock/index.md): pe tipurile de operațiune cu **Protect Reservations**, scanarea la livrare se face față de cantitatea rezervată.
- [deltatech_stock_barcode](../deltatech_stock_barcode/index.md): extinde separat aplicația Stock Barcode din Enterprise; același ecosistem de scanare în depozit, fără dependență directă.
