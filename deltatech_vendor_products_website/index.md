# Vendor Products Website (localizat la `deltatech_vendor_products_website/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_website`
- **Versiune:** `19.0.1.2.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_vendor/tree/19.0/deltatech_vendor_products_website`
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_website`
- **Ultima Ingestie:** `2026-10-19`

#### 1. Sumar

Modulul leagă catalogul produselor furnizorilor de magazinul online. Un flux de furnizor poate fi marcat pentru căutare online: la o căutare, produsele găsite la furnizor sunt aduse în lista de produse furnizor din Odoo, iar la accesarea unui produs, acesta este transformat într-un produs de magazin, publicat pe website și comandabil. Astfel oferta magazinului poate fi extinsă cu produsele furnizorilor fără gestionare manuală articol cu articol.

**Stare actuală (Odoo 19):** interfața de căutare online de pe pagina `/shop` nu mai există. În 19.0.1.2.0 a fost eliminat codul mort din versiunile vechi, iar căutarea online pe `/shop` urmează să revină ca interacțiune Odoo 19. În prezent modulul oferă doar fundamentul de server: rutele JSON-RPC și logica de import.

#### 2. Funcționalități Cheie

- Opțiunea **Online Search** pe fluxul de furnizor (`vendor.feed`), vizibilă în formular doar când tipul conexiunii nu este `none`. Doar fluxurile cu această opțiune activă sunt folosite de căutarea online.
- Rută JSON-RPC `/vendor_product/online_search` (parametri `source`, `search`): interoghează conectorul fluxului și întoarce produsele găsite (id, nume, cod, preț, imagine, produs asociat, URL și preț formatat în moneda website-ului). Include protecții: limită de încărcare CPU (parametrul de sistem `vendor_product_online_search_cpu`, implicit 20%) și ignorarea repetării aceleiași căutări în sesiune.
- Rută JSON-RPC `/vendor_product/online_source`: listează fluxurile cu căutare online activă (id, nume), pentru alegerea sursei.
- Rută `/vendor_product/<id>`: creează produsul de magazin din produsul furnizorului (dacă nu există deja) și redirecționează către pagina lui din `/shop`. Produsele create sunt publicate pe website și permit comanda chiar fără stoc.
- Securitate (19.0.1.1.6): ruta acceptă doar ID-uri returnate de `online_search` în aceeași sesiune (ultimele 200) sau utilizatori interni de vânzări; orice alt ID întoarce 404. Pentru produse deja legate, ruta nu mai forțează publicarea, deci produsele despublicate rămân despublicate.
- Corecție (19.0.1.2.1): `get_products` nu mai produce eroare când conectorul întoarce produse; rezultatele salvate sunt recitite după cod, cu invalidarea cache-ului ORM.
- Extensibilitate (19.0.1.2.1): câmpurile salvate din căutarea online provin din hook-ul `_online_search_fields()`, pe care un conector le poate completa (de exemplu, conectorul Kramp adaugă codul de bare).
- Curățare (19.0.1.2.0): eliminate modelul `vendor.product.search` (tabela se șterge la actualizare, inclusiv regula de acces fără grup care dădea drepturi complete oricărui utilizator), JS-ul vechi `online_search` și mixinurile website.

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- `website_sale`

Dependență externă Python: `psutil` (măsurarea încărcării CPU).

#### 4. Componente Cheie

**Modele**

- `vendor.feed` (extins): adaugă câmpul `online_search`, metoda `online_get_values(search)` (punct de extensie, implementat de conectori), `_online_search_fields()` și `get_products(search)`, care combină produsele deja existente cu cele aduse online.
- `vendor.product` (extins): `_prepare_values()` adaugă `website_published` și `allow_out_of_stock_order`, deci produsele create sunt publicate și comandabile.

**Vizualizări**

- `view_vendor_feed_form`: adaugă opțiunea `online_search` în grupul de conexiune al formularului fluxului de furnizor.
- `products` (șablon, moștenește `website_sale.products`): afișează grila de produse și adaugă un marcaj `online_search` când există o căutare cu o singură pagină de rezultate. Nu are încă interfață asociată în Odoo 19.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Migrarea `19.0.1.2.0` șterge tabela veche `vendor_product_search`.

#### 5. Conexiuni

- [deltatech_vendor_products](../deltatech_vendor_products/index.md): modulul de bază cu produsele și fluxurile furnizorilor; acest modul îi adaugă expunerea în magazinul online.
- [deltatech_vendor_products_kramp](../deltatech_vendor_products_kramp/index.md): conector care folosește `_online_search_fields()` pentru a adăuga codul de bare (conform istoricului modulului).
- `website_sale`: infrastructura de magazin online (coș, comenzi, pagini de produs).
