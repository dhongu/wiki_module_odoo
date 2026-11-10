# Barcode Picking (localizat la `deltatech_barcode_picking/index.md`)

- **Nume Tehnic:** `deltatech_barcode_picking`
- **Versiune:** `19.0.2.2.11`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_barcode_picking
- **Cale Locală:** `odoo-addons/bitshop/deltatech_barcode_picking`
- **Ultima Ingestie:** `2026-11-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite operatorilor de depozit să adauge produse pe recepții și livrări direct prin scanarea codului de bare, fără să mai completeze manual liniile. Scanarea recunoaște codul de bare al produsului și etichetele combinate „cod produs + separator + nume lot", accelerând pregătirea comenzilor și reducând erorile de introducere manuală.

#### 2. Funcționalități Cheie

- Adaugă produse pe recepții și livrări prin scanarea codului de bare, cu orice cititor care funcționează ca tastatură (scrie codul și trimite Enter). Cursorul trebuie ținut în afara câmpurilor text. Fiecare scanare adaugă **o unitate**.
- Citește etichete combinate produs + lot, cu separatorii `-` sau `/` (ex. `5940000000024/LOT26`); codul se desparte la ultimul separator și cantitatea se pune pe acel lot. Dacă numele loturilor conțin `-`, se folosește `/` ca separator. Se poate scana și doar numele lotului, dacă este unic.
- Lotul scanat trebuie să existe deja. Pentru loturi pe recepții se bifează **Use Existing ones** (grupul **Lots/Serial Numbers**) la tipul de operațiune Recepții, în **Inventar → Configurare → Tipuri de operațiuni**, ca loturile scanate să apară în **Detailed Operations**.
- Pe recepție în ciornă, fiecare scanare crește **Demand**; pe recepția pregătită (Ready) cantitatea poate depăși cererea (recepție în plus), iar un produs scanat fără mișcare se adaugă ca mișcare nouă.
- Pe livrare pregătită, cererea rezervată este limită: o scanare peste ea este refuzată cu „Your reserved quantity has already been reached". Pentru a număra marfa scanând, se setează **Quantity** la 0 pe linie și se salvează (eliberează rezervarea), apoi se scanează fiecare unitate; nu se apasă **Check Availability** înainte de scanare.
- Cod necunoscut: transferul rămâne neschimbat, cu mesajul „There is no product with barcode …". Un transfer **Done** sau **Cancelled** nu poate fi scanat (mesaj **Invalid Operation**), indiferent de context.
- **Scanarea în ajustările de inventar nu este disponibilă în această versiune** (codul există, dar este dezactivat).
- Câmpurile **Allowed to add products by scanning** și **Request Effective Date**, adăugate pe tipul de operațiune, nu au efect în această versiune.
- Limitări cunoscute: o scanare în plus nu se anulează prin scanare (se corectează manual); pe o recepție din comandă de achiziție (Ready, cantitate = cerere) scanarea se adaugă peste cantitate, deci cantitatea se setează întâi la 0; un cod produs + lot cu lot inexistent adaugă unitatea **fără lot**, fără avertisment; la prima scanare a unui produs încă absent din transfer apare mesajul „Lotul este deja prezent in lista", deși linia se adaugă. Fluxul pas cu pas rămâne în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock`
- `barcodes`
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking.type` (extins): adaugă câmpurile `product_barcode_scanner`, `request_effective_date` și `force_current_date` (folosit la migrare); primele două nu au efect în această versiune.
- `stock.picking` (extins, moștenește și `barcodes.barcode_events_mixin`): implementează `on_barcode_scanned()` (interpretează codul scanat — produs, lot/serie sau combinație produs-lot) și `_add_product()` (alege mișcarea potrivită: cea care deține deja lotul scanat și mai are loc, altfel prima mișcare cu loc în cerere, altfel ultima; creează sau actualizează `stock.move` și `stock.move.line`); `_barcode_check_scannable()` refuză pe server transferurile Done/Cancelled. Adaugă și `request_effective_date`, `forced_effective_date`, `force_current_date`.
- `stock.move` (extins): leagă liniile de mișcare create prin scanare de transferul mișcării lor (`_barcode_link_move_lines_to_picking`).
- `stock.inventory` (în `models/stock_inventory.py`): cod de scanare pentru ajustări de inventar (`on_barcode_scanned`, `_add_product`), dar importul modelului este comentat în `models/__init__.py`, deci **nu este încărcat**.

**Vizualizări**

- `view_picking_barcode_inherit_form`: adaugă câmpul `_barcode_scanned` (widget `barcode_handler`) pe formularul de transfer, pentru captarea scanărilor; poartă și liniile de mișcare ale fiecărei mișcări (`move_ids.move_line_ids`, coloană ascunsă), ca linia de lot scanată să se salveze.
- `view_stock_move_line_detailed_operation_tree`: forțează salvarea câmpului `product_id` în lista de operațiuni detaliate, necesar pentru scanarea cu lot.
- `view_picking_type_form`: expune pe tipul de operațiune câmpurile `product_barcode_scanner` și `request_effective_date`.
- `views/stock_inventory_view.xml`: nu definește nicio vizualizare activă (formularul de inventar este comentat).

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_barcode_sale](../deltatech_barcode_sale/index.md): aplică același principiu de accelerare a introducerii datelor prin scanare de coduri de bare, dar pe comenzile de vânzare (`sale.order`) în loc de transferurile de stoc.
- [deltatech_stock_barcode](../deltatech_stock_barcode/index.md): extinde separat aplicația Stock Barcode din Odoo Enterprise pentru transferuri și inventar; face parte din același ecosistem de scanare a codurilor de bare în depozit, dar nu este o dependență directă a acestui modul.
