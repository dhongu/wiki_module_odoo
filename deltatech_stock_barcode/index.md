# Deltatech Stock Barcode (localizat la `deltatech_stock_barcode/index.md`)

- **Nume Tehnic:** `deltatech_stock_barcode`
- **Versiune:** `19.0.0.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_stock_barcode
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_stock_barcode`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Acest modul extinde funcționalitatea Stock Barcode din Odoo Enterprise cu mai multe îmbunătățiri pentru transferuri (pickings) și gestiunea stocului. Operatorul de depozit poate, direct din interfața de scanare cu codul de bare, să gestioneze greutatea coletelor și numărul de pachete, să genereze și să tipărească etichetele de curier (AWB) și să vadă detaliile precise de amplasare a produselor în depozit. Scopul principal este accelerarea și simplificarea procesului de pregătire a livrărilor, oferind operatorilor toate informațiile necesare într-un singur loc.

#### 2. Funcționalități Cheie

- **Gestiunea greutății și a coletelor:** posibilitatea de a administra greutatea pachetelor și numărul de colete direct din interfața de scanare cu codul de bare.
- **Integrare cu curierul:** generarea și tipărirea etichetelor de curier (AWB) la salvarea detaliilor de greutate în cadrul fluxului de scanare.
- **Detalii de amplasare îmbunătățite:** integrarea informațiilor detaliate de locație (Raft, Rând, Poliță, Cutie) în vizualizările de scanare a codului de bare, pentru o mai bună vizibilitate a poziției articolelor.
- **Îmbunătățiri ale fluxului de lucru:** include un formular simplificat pentru capturarea detaliilor de livrare în timpul procesului de transfer.
- **Listă de prețuri configurabilă pentru scanare:** permite alegerea unei liste de prețuri specifice din setări, pentru calcularea prețului produsului la scanarea codului de bare, oferind mai multă flexibilitate în gestiunea stocului.
- **Inventar pe baze mari de date:** setarea opțională „Barcode Inventory: Only My Quants” (Inventar > Setări > Barcode, dezactivată implicit) face ca ecranul Inventar din aplicația Cod de bare să încarce doar cantitățile (quants) atribuite utilizatorului curent, ca în Odoo 18, nu și cele neatribuite cu data de inventar scadentă. Astfel ecranul se deschide rapid chiar și cu zeci de mii de quants; celelalte produse se adaugă prin scanare.
- **Amplasare fără raftul sursă:** la transferurile interne din aplicația de scanare, destinația propusă de strategia de amplasare nu mai este raftul de pe care pleacă marfa (relevant când e activă opțiunea `prefer_existing_stock_location`).

#### 3. Dependențe

- `stock_barcode`
- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`; componentele de mai jos completează informația cu elementele tehnice notabile identificate în cod (permise explicit, dat fiind că readme-ul nu acoperă în detaliu partea de modele/controller).

**Modele**

- `res.config.settings` (extindere): adaugă câmpul `barcode_pricelist_id`, ce permite configurarea listei de prețuri folosite la calculul prețului produsului în timpul scanării.
- `stock.location` (extindere): adaugă `max_products_leaf` în lista de câmpuri expuse către interfața Stock Barcode.
- `product.product` (extindere): adaugă `loc_rack`, `loc_row`, `loc_shelf`, `loc_case` în lista de câmpuri expuse către interfața Stock Barcode, pentru afișarea detaliilor de amplasare.
- `res.config.settings` (extindere): adaugă și `barcode_inventory_own_quants` (parametru `deltatech_stock_barcode.inventory_own_quants`).
- `stock.picking` (extindere): expune în interfața de scanare `carrier_tracking_ref`, `carrier_ready`, `carrier_ready_mobile`; metoda `barcode_get_putaway_dest` primește `location_id` (locația sursă a liniei noi) și o transmite, împreună cu sursa transferului, prin cheia de context `putaway_exclude_location_ids` din [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md).
- `stock.picking.type` (extindere): opțiunile `barcode_require_weight` și `barcode_require_putaway_dest` (obligă scanarea destinației determinate de regulile de amplasare).
- `stock.quant` (extindere): câmpurile calculate de amplasare și `list_price` (din lista de prețuri configurată); `_get_stock_barcode_data` este suprascrisă pentru ecranul Inventar când setarea „Only My Quants” este activă.

**Vizualizări**

- `res_config_settings_views.xml`: adaugă în setările de Inventar opțiunile de listă de prețuri pentru scanare și „Only My Quants”.
- `stock_picking_view.xml`: extensii pe formularul de transfer pentru greutate, colete și date de curier.
- `stock_inventory_view.xml`: integrează detaliile de amplasare (raft/rând/poliță/cutie) în vizualizările de inventar.
- `wizard/delivery_carrier_details_view.xml`: formular simplificat (wizard `delivery.carrier.details`) pentru capturarea greutății și generarea/tipărirea etichetei AWB direct din fluxul de scanare.

**Controller**

- `controllers/stock_barcode.py`: suprascrie ruta `/stock_barcode/get_specific_barcode_data` (declarată `type="jsonrpc"` din 19.0) și implementează fallback-ul de căutare după referința internă (`default_code`) pe baza payload-ului curent (`barcode`, `barcodes`, `barcodes_by_model`), folosind helper-ul standard `_get_records_fields_stock_barcode`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): furnizează integrarea cu curierul, folosită la generarea și tipărirea etichetelor AWB din fluxul de scanare.
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): asigură funcționalitatea de inventar extinsă pe care se grefează vizualizările de scanare ale acestui modul.
- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md): furnizează strategia de amplasare (raft/rând/poliță/cutie) ale cărei detalii sunt expuse acum și în interfața de scanare cu codul de bare.
