# Brand Field (localizat la `deltatech_brand_field/index.md`)

- **Nume Tehnic:** `deltatech_brand_field`
- **Versiune:** `20.0.0.0.11`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_brand_field`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_brand_field`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care spune celorlalte module în ce câmp al produsului se află marca. Mai multe module (feed-uri de produse, conectori de marketplace, SEO pentru website) au nevoie de marca produsului, dar aceasta poate fi stocată în câmpuri diferite, în funcție de ce este instalat. Numele tehnic al câmpului se alege o singură dată în Setări, iar toate modulele integrate citesc marca din el.

#### 2. Funcționalități Cheie

- O singură setare pentru toate modulele integrate, în loc de câte un câmp de marcă pe modul.
- Funcționează cu câmpuri Many2one (se folosește numele mărcii) și cu câmpuri Char.
- Produsele fără marcă returnează valoare goală.
- Setarea: **Website > Configuration > Settings**, blocul **Module Brand Field**, câmpul **Brand Field** (de exemplu `product_brand_id`). Valoarea nu este validată: un nume greșit dă marcă goală pe toate produsele, fără eroare. Debifarea casetei **Module Brand Field** urmată de salvare deschide fereastra de dezinstalare.
- Modulele integrate citesc marca fără setare proprie; după schimbarea câmpului se apasă **Refresh Feeds**, ca feed-ul să nu fie servit din cache. Fără acest modul, conectorul eMAG trimite numele companiei ca marcă.
- Modulul nu adaugă un model de mărci și nici ecrane de administrare. `brand_name` este calculat și nestocat, deci nu poate fi folosit în căutări, filtre sau grupări.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpul calculat `brand_name` și metoda `get_brand_name()`, care citește marca din câmpul configurat.
- `product.product` (extins): `get_brand_name()` delegă către șablonul de produs.
- `res.config.settings` (extins): setarea pentru câmpul de marcă și modulul asociat.

**Vizualizări**

- `res_config_settings_view_form`: blocul **Module Brand Field** din setările Website.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_feed](../deltatech_feed/index.md): citește marca produselor din câmpul configurat aici și instalează singur acest modul.
- [deltatech_product_brand](../deltatech_product_brand/index.md): adaugă câmpul de marcă pe produs (`product_brand_id`), folosit ca exemplu de câmp configurabil.
