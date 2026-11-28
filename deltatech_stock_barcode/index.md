# Stock Barcode Enhanced (localizat la `deltatech_stock_barcode/index.md`)

- **Nume Tehnic:** `deltatech_stock_barcode`
- **Versiune:** `20.0.0.1.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_stock_barcode
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_stock_barcode`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde aplicația Stock Barcode din Odoo Enterprise cu îmbunătățiri pentru transferuri și inventar. Operatorul de depozit poate, direct din interfața de scanare, să gestioneze greutatea și numărul de colete, să genereze și să tipărească etichetele de curier (AWB) și să vadă detaliile de amplasare a produselor. Scopul este accelerarea pregătirii livrărilor și a inventarului, cu toate informațiile necesare într-un singur loc.

#### 2. Funcționalități Cheie

- **Greutate și colete:** numărul de colete și greutatea totală se introduc din scanare, într-un dialog simplificat cu butoane mari -1 / +1. Pe tipul de operație de livrare, **Require Weight on Barcode Scan** (secțiunea Final Validation) cere datele la validare; **Apply and Print** le salvează, trimite livrarea la curier (AWB) și continuă validarea, iar închiderea dialogului o anulează.
- **Integrare cu curierul:** butonul **Print AWB** din meniul de tipărire scoate eticheta de curier.
- **Detalii de amplasare:** Raft, Rând, Poliță și Cutie apar în vizualizările de scanare.
- **Destinație propusă la transferuri interne:** la scanarea unui produs fără linie, aplicația cere serverului destinația dată de regulile de putaway și capacitățile rafturilor (`deltatech_putaway_strategy`); raftul din care pleacă marfa nu este propus, iar o cantitate peste capacitatea maximă a raftului este refuzată. Cu **Require Scanning Putaway Destination** (**Inventar > Configurare > Tipuri de operații**, fila Barcode App), operatorul trebuie să scaneze exact raftul propus.
- **Listă de prețuri pentru scanare:** setarea **Barcode Pricelist** (**Inventar > Configurare > Setări**, blocul Barcode) stabilește prețul afișat pe cardul produsului scanat din ecranul principal.
- **Inventar pe baze mari:** setarea **Barcode Inventory: Only My Quants** încarcă pe ecranul de inventar doar quant-urile alocate utilizatorului curent (celelalte produse se adaugă prin scanare), ca ecranul să se deschidă rapid chiar cu zeci de mii de quant-uri.
- Căutarea la scanare folosește și referința internă (`default_code`) ca alternativă la codul de bare.

Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock_barcode`
- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md)

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extins): `barcode_pricelist_id` și opțiunea de inventar doar cu quant-urile proprii.
- `stock.picking` (extins): `action_get_weight`, `do_print_picking_awb`, `barcode_get_putaway_dest` (destinația propusă) și câmpurile expuse în interfața de scanare.
- `stock.picking.type` (extins): `_get_barcode_config`, configurația de scanare a destinației și a greutății.
- `stock.quant` (extins): `_compute_list_price`, `_barcode_inventory_own_quants`, `_get_barcode_inventory_quant_domain`, `_get_stock_barcode_data`.
- `stock.location`, `product.product` (extinse): câmpurile de amplasare (`max_products_leaf`, `loc_rack`, `loc_row`, `loc_shelf`, `loc_case`) expuse interfeței de scanare.
- `delivery.carrier.details` (extins): dialogul de greutate și colete.

**Vizualizări**

- `res_config_settings_view_form`: setările din blocul Barcode.
- `stock_barcode_view_picking_type_form`: opțiunile pe tipul de operație.
- `view_stock_quant_stock_barcode_tree` / `stock_quant_barcode` / `stock_quant_barcode_kanban_2`: vizualizările de inventar cu detaliile de amplasare.
- `wizard/delivery_carrier_details_view.xml`: formularul simplificat pentru greutate și AWB.

**Controller**

- `controllers/stock_barcode.py`: rutele `/stock_barcode/get_main_menu_data` și `/stock_barcode/get_specific_barcode_data` (`type="jsonrpc"`), cu fallback de căutare după referința internă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): integrarea cu curierul, folosită la AWB.
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): inventarul extins pe care se grefează vizualizările.
- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md): strategia de amplasare ale cărei destinații sunt propuse la scanare.
- `stock_barcode`: aplicația Enterprise extinsă.
