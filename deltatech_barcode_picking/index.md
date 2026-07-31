# Barcode Picking (localizat la `deltatech_barcode_picking/index.md`)

- **Nume Tehnic:** `deltatech_barcode_picking`
- **Versiune:** `19.0.2.2.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_barcode_picking
- **Cale Locală:** `odoo-addons/bitshop/deltatech_barcode_picking`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul permite operatorilor de depozit să adauge produse pe un transfer de stoc (picking) direct prin scanarea codului de bare, fără să mai completeze manual liniile de operare. Scanarea recunoaște atât codul de bare al produsului, cât și cel al lotului/seriei, inclusiv formatul combinat "cod produs + separator + cod lot" (separatori acceptați: `-`, `/`, spațiu), accelerând semnificativ pregătirea comenzilor și reducând erorile de introducere manuală a datelor.

#### 2. Funcționalități Cheie

- Adăugarea produselor pe un transfer de stoc (picking) prin scanarea codului de bare.
- Recunoașterea codurilor de bare combinate produs+lot, folosind separatorii `-`, `/` sau spațiu; pentru a scana coduri cu lot pe picking este necesar ca tipul de operațiune să aibă activată opțiunea "Afișează detalii operațiune".
- Adăugarea produselor și în inventarul de stoc (`stock.inventory`) prin scanarea codului de bare al produsului sau al lotului/seriei (funcționalitate deja implementată în cod, nu doar planificată — vezi corecția de mai jos).
- Configurare per tip de operațiune (`stock.picking.type`) a permisiunii de scanare cu barcode-ul, printr-un câmp dedicat.

> **Corecție față de `readme/DESCRIPTION.md`:** descrierea originală menționează ca "todo" adăugarea produselor în inventar prin scanare, însă modelul `stock.inventory` din `models/stock_inventory.py` implementează deja complet această funcționalitate (`on_barcode_scanned`, `_add_product`). Nota "todo" este depășită și a fost corectată aici.

#### 3. Dependențe

- `stock`
- `barcodes`
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)

#### 4. Componente Cheie

**Modele**

- `stock.picking.type` (extins): adaugă câmpurile `product_barcode_scanner` (permite scanarea de coduri de bare pe acest tip de operațiune, activat implicit), `request_effective_date` și `force_current_date` (folosit la migrare).
- `stock.picking` (extins, moștenește și `barcodes.barcode_events_mixin`): adaugă câmpurile `request_effective_date`, `forced_effective_date`, `force_current_date`; implementează `on_barcode_scanned()` (interpretează codul scanat — produs, lot/serie sau combinație produs-lot — și verifică starea transferului) și `_add_product()` (creează sau actualizează liniile de mișcare `stock.move`/`stock.move.line` corespunzătoare cantității scanate).
- `stock.inventory` (extins, moștenește și `barcodes.barcode_events_mixin`): implementează `on_barcode_scanned()` și `_add_product()` pentru a adăuga/actualiza liniile de inventar (`stock.inventory.line`) direct din scanare.

**Vizualizări**

- `view_picking_barcode_inherit_form`: adaugă câmpul `_barcode_scanned` (widget `barcode_handler`) pe formularul de transfer (`stock.picking`), pentru a capta evenimentele de scanare.
- `view_stock_move_line_detailed_operation_tree`: forțează salvarea (`force_save`) câmpului `product_id` în lista de operațiuni detaliate, necesar pentru fluxul de scanare cu lot.
- `view_picking_type_form`: expune pe formularul tipului de operațiune (`stock.picking.type`) câmpurile `product_barcode_scanner` și `request_effective_date`.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_barcode_sale](../deltatech_barcode_sale/index.md): aplică același principiu de accelerare a introducerii datelor prin scanare de coduri de bare, dar pe comenzile de vânzare (`sale.order`) în loc de transferurile de stoc.
- [deltatech_stock_barcode](../deltatech_stock_barcode/index.md): extinde separat aplicația Stock Barcode din Odoo Enterprise pentru transferuri și inventar; face parte din același ecosistem de scanare a codurilor de bare în depozit, dar nu este o dependență directă a acestui modul.
