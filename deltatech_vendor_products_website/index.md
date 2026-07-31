# Vendor Products Website (localizat la `deltatech_vendor_products_website/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_website`
- **Versiune:** `19.0.1.1.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_vendor_products_website
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vendor_products_website`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul extinde funcționalitatea de gestionare a produselor furnizorilor către magazinul online (website). Permite căutarea produselor în cataloagele furnizorilor și importul automat al acestora în lista principală de produse din Odoo, afișarea produselor furnizorilor direct în site și posibilitatea ca vizitatorii să adauge aceste produse în coș și să plaseze comenzi pentru ele. Astfel, oferta de produse disponibile în magazinul online poate fi extinsă cu produsele furnizorilor fără a fi nevoie de o gestionare manuală separată a fiecărui articol.

#### 2. Funcționalități Cheie

- Căutarea produselor în cataloagele furnizorilor și importul automat al acestora în lista principală de produse din Odoo.
- Afișarea produselor furnizorilor în magazinul online (website).
- Adăugarea produselor furnizorilor în coș și plasarea de comenzi pentru acestea.

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- `website_sale`

Dependență externă Python: `psutil`.

#### 4. Componente Cheie

Conform fluxului de ingestie, componentele tehnice nu sunt detaliate deoarece secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`, iar acesta nu solicită explicit analiza codului.

#### 5. Conexiuni

- [deltatech_vendor_products](../deltatech_vendor_products/index.md): modulul de bază care gestionează produsele furnizorilor; acest modul îi adaugă expunerea în magazinul online.
- `website_sale`: oferă infrastructura de magazin online (coș, comenzi, pagini de produs) pe care se afișează produsele furnizorilor.
