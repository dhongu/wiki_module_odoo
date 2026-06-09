# Deltatech Stock Barcode (localizat la `deltatech_stock_barcode/index.md`)

- **Nume Tehnic:** `deltatech_stock_barcode`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/terrabit-ro/bitshop_ent/tree/19.0/deltatech_stock_barcode
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_stock_barcode`
- **Ultima Ingestie:** `2026-06-09`

#### 1. Sumar

Acest modul extinde funcționalitatea Stock Barcode din Odoo Enterprise cu mai multe îmbunătățiri pentru transferuri (pickings) și gestiunea stocului. Operatorul de depozit poate, direct din interfața de scanare cu codul de bare, să gestioneze greutatea coletelor și numărul de pachete, să genereze și să tipărească etichetele de curier (AWB) și să vadă detaliile precise de amplasare a produselor în depozit. Scopul principal este accelerarea și simplificarea procesului de pregătire a livrărilor, oferind operatorilor toate informațiile necesare într-un singur loc.

#### 2. Funcționalități Cheie

- **Gestiunea greutății și a coletelor:** posibilitatea de a administra greutatea pachetelor și numărul de colete direct din interfața de scanare cu codul de bare.
- **Integrare cu curierul:** generarea și tipărirea etichetelor de curier (AWB) la salvarea detaliilor de greutate în cadrul fluxului de scanare.
- **Detalii de amplasare îmbunătățite:** integrarea informațiilor detaliate de locație (Raft, Rând, Poliță, Cutie) în vizualizările de scanare a codului de bare, pentru o mai bună vizibilitate a poziției articolelor.
- **Îmbunătățiri ale fluxului de lucru:** include un formular simplificat pentru capturarea detaliilor de livrare în timpul procesului de transfer.

#### 3. Dependențe

- `stock_barcode`
- [deltatech_delivery](../deltatech_delivery/index.md)
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)

#### 4. Componente Cheie

Componentele cheie sunt acoperite prin descrierea funcțională din secțiunile 1 și 2 (sursă: `readme/DESCRIPTION.md`). Modulul aduce contribuții pe interfața de scanare cu codul de bare (transferuri și inventar), un wizard pentru detaliile de livrare ale curierului și extensii de vizualizare pentru `stock.picking` și inventar.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): furnizează integrarea cu curierul, folosită la generarea și tipărirea etichetelor AWB din fluxul de scanare.
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): asigură funcționalitatea de inventar extinsă pe care se grefează vizualizările de scanare ale acestui modul.
