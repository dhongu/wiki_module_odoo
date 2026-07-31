# Vendor Products Granit (localizat la `deltatech_vendor_products_granit/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_granit`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_vendor_products_granit
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vendor_products_granit`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă un conector specializat pentru importul și sincronizarea datelor despre produse din catalogul furnizorului Granit direct în Odoo, simplificând astfel aprovizionarea și gestiunea stocurilor. Din punct de vedere de business, automatizarea elimină introducerea manuală a datelor pentru produsele Granit, asigurând că în Odoo catalogul este mereu actualizat cu cele mai recente informații despre produse și prețuri.

#### 2. Funcționalități Cheie

- **Import automat de catalog:** construiește și actualizează rapid catalogul de produse folosind direct datele de la Granit.
- **Acuratețe mai bună a datelor:** elimină erorile de tastare și asigură reflectarea corectă în Odoo a specificațiilor și codurilor de produs.
- **Aprovizionare simplificată:** identifică și comandă ușor produsele Granit, având toate detaliile disponibile în ERP.
- **Vizibilitate mai bună a stocurilor:** menține informații exacte despre stoc și variante pentru toate produsele Granit, pentru o planificare mai eficientă.
- **Gestiune scalabilă a furnizorului:** administrează eficient un volum mare de produse Granit printr-un conector integrat și automatizat.

#### 3. Dependențe

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md)

#### 4. Componente Cheie

Documentația acestui modul se bazează pe fișierul `readme/DESCRIPTION.md`, care nu detaliază componente tehnice individuale. Modulul include directoarele `models/` și `wizard/` (specializări ale conectorului de produse furnizor pentru catalogul Granit), însă acestea nu sunt detaliate aici în absența unei mențiuni explicite în Readme.

#### 5. Conexiuni

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): modulul de bază al conectorului de produse furnizor (cu integrare website), pe care acest conector Granit îl extinde cu logica specifică furnizorului.
