# Brand Field (localizat la `deltatech_brand_field/index.md`)

- **Nume Tehnic:** `deltatech_brand_field`
- **Versiune:** `19.0.0.1.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_brand_field
- **Cale Locală:** `odoo-addons/bitshop/deltatech_brand_field`
- **Ultima Ingestie:** `2026-11-04`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care spune celorlalte module în ce câmp al produsului se află marca. Mai multe module (feed-uri de produse, SEO pentru website, Google Tag) au nevoie de marca produsului, dar aceasta poate sta în câmpuri diferite, în funcție de ce e instalat: un Many2one către un model de mărci din alt modul sau un simplu câmp text. În Setări se alege o singură dată numele tehnic al câmpului, iar toate modulele integrate citesc marca din el, prin `brand_name` / `get_brand_name()`.

#### 2. Funcționalități Cheie

- **O singură setare pentru toate modulele integrate**, în loc de un câmp de marcă pentru fiecare modul. Se completează în **Website → Configurare → Setări**, secțiunea „Shop - Products", la **Brand Field** (parametrul de sistem `product.brand_field`), cu numele tehnic al câmpului de produs care ține marca (de exemplu `product_brand_id` din `deltatech_product_brand`).
- Funcționează cu câmpuri Many2one (se folosește numele mărcii) și cu câmpuri Char/Text.
- **Rezervă pe atributul cu rolul *Brand***: dacă în câmpul configurat marca lipsește sau e goală pe produs, se folosește valoarea atributului de produs cu rolul *Brand* (din `deltatech_product_attribute_role`), astfel încât și marca ținută ca atribut (Barcode Lookup, importuri) ajunge în feed-uri și în marcajul SEO. Se setează la **Vânzări → Configurare → Produse → Atribute**, câmpul **Rol**; doar un atribut poate avea rolul. Pe șablonul de produs marca se cunoaște dacă linia de atribut are o singură valoare, iar pe variantă e valoarea variantei pentru atribut.
- Produsele fără marcă întorc o valoare goală; o marcă goală (Char/Text sau Many2one) dă șir gol, iar feed-urile de produse nu mai răspund cu eroare HTTP 500.
- Modulele `deltatech_feed`, `deltatech_website_seo` și `terrabit_google_tag` îl instalează singure; lângă conectorii marketplace eMAG sau Shopify se instalează separat (fără el, conectorul eMAG trimite numele companiei ca marcă).
- După schimbarea setării se apasă **Refresh Feeds** pe feed, ca acesta să nu fie servit din cache.
- Limitări: modulul nu adaugă un model de mărci sau ecrane de administrare; `brand_name` e calculat și nestocat, deci nu poate fi folosit în căutări, filtre sau grupări. Numele câmpului din Setări nu e validat: un nume greșit dă marcă goală peste tot, cu excepția produselor cu atribut de marcă. Căsuța „Module Brand Field" trebuie lăsată bifată: debifarea și salvarea deschide fereastra de dezinstalare a modulului.

#### 3. Dependențe

- `website_sale_stock`
- [deltatech_product_attribute_role](../deltatech_product_attribute_role/index.md)

#### 4. Componente Cheie

*Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`, completate din `readme/CONFIGURE.md`, `readme/USAGE.md` și `readme/HISTORY.md`; analiza detaliată a componentelor nu este cerută de readme. Mai jos sunt doar reperele confirmate în cod.*

**Modele**

- `product.template` (extins): câmpul calculat `brand_name` și metoda `get_brand_name(brand_field=None)`, care citește marca din câmpul configurat, cu rezervă pe atributul cu rolul *Brand*.
- `product.product` (extins): `get_brand_name`, delegat către șablonul de produs.
- `product.attribute` (extins): adaugă valoarea „Brand" în câmpul de selecție `attribute_role`.
- `res.config.settings` (extins): câmpul `brand_field` (parametrul `product.brand_field`) și `module_deltatech_brand_field`.

**Vizualizări**

- `res_config_settings_view_form`: moștenește formularul de setări Website și adaugă câmpul „Brand Field” după setarea de disponibilitate a produselor.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_feed](../deltatech_feed/index.md): depinde de acest modul și folosește marca produsului în feed-urile de produse.
- [deltatech_product_attribute_role](../deltatech_product_attribute_role/index.md): oferă rolul de atribut din care se citește marca atunci când câmpul configurat e gol.
- `deltatech_product_brand`: exemplu de modul care adaugă câmpul Many2one `product_brand_id` indicat în setare.
