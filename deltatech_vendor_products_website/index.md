# Vendor Products Website (localizat la `deltatech_vendor_products_website/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_website`
- **Versiune:** `19.0.1.4.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_vendor/tree/19.0/deltatech_vendor_products_website`
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_website`
- **Ultima Ingestie:** `2026-10-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul leagă catalogul produselor furnizorilor de magazinul online. Un flux de furnizor poate fi marcat pentru căutare online: când un client caută un cod în `/shop` și nu îl găsește în catalogul propriu, sub grilă apare blocul „Available from our suppliers", cu produsele găsite la furnizor. La click pe un card, produsul este creat în Odoo, publicat pe website și deschis în magazin, gata de comandat. Astfel oferta magazinului poate fi extinsă cu produsele furnizorilor, fără gestionare manuală articol cu articol.

#### 2. Funcționalități Cheie

- Opțiunea **Online Search** pe fluxul de furnizor (*Achiziții → Produse → Vendor Feed*, grupul Connection), vizibilă doar când tipul conexiunii nu este `none`. Doar fluxurile cu această opțiune activă sunt interogate din magazin.
- **Căutare online în `/shop`** (19.0.1.3.0, interacțiune Odoo 19): când rezultatele magazinului încap pe o singură pagină, furnizorii sunt interogați după afișarea paginii (un furnizor lent nu întârzie magazinul), iar produsele găsite apar sub grilă într-un bloc „Available from our suppliers". Mesajul standard „fără rezultate" este ascuns când furnizorii găsesc produse.
- Cardul afișează imaginea, numele, **codul** și **prețul** furnizorului, plus disponibilitatea: „Available at the supplier" (stoc la furnizor) sau „On order". Prețul pornește de la prețul de listă al furnizorului, cu regulile de preț ale fluxului, convertit în moneda website-ului și afișat cu sau fără taxe, ca restul magazinului (taxa de vânzare implicită a companiei).
- Reguli de afișare: se arată doar produsele furnizorului fără produs Odoo asociat (celelalte sunt găsite de căutarea standard) și doar cele cu preț la furnizor, ca să nu poată fi comandate la 0. Căutările sub 3 caractere nu se trimit, iar o căutare repetată în sesiune refolosește ultimul rezultat. Se afișează cel mult 24 de carduri.
- Rută `/vendor_product/<id>`: creează produsul de magazin din produsul furnizorului (dacă nu există deja) și redirecționează către pagina lui din `/shop`. Produsele create sunt publicate și permit comanda chiar fără stoc (**Sell when Out-of-Stock**). Redirecționarea nu mai poartă înregistrarea în query string.
- Securitate: ruta acceptă doar ID-uri returnate clientului în aceeași sesiune (ultimele 200) sau utilizatori interni de vânzări; orice alt ID întoarce 404. Pentru produse deja legate, ruta nu forțează republicarea, deci produsele despublicate rămân despublicate.
- Rută JSON-RPC `/vendor_product/online_results` (cardurile pentru blocul din `/shop`). Rutele vechi `/vendor_product/online_search` și `/vendor_product/online_source` au fost eliminate în 19.0.1.4.0, fiindcă ocoleau filtrele (un apel scris de mână putea publica un produs la preț 0).
- Limită de căutări (19.0.1.4.0, în locul gărzii de CPU): cel mult 10 căutări la furnizor pe minut pentru o sesiune (`vendor_product_online_search_session_limit`) și 60 pentru o adresă IP (`vendor_product_online_search_ip_limit`); 0 dezactivează limita. O căutare repetată în sesiune nu se numără. Peste limită blocul nu apare, iar jurnalul arată „Online search … skipped, too many searches".
- Multi-companie: sunt interogate doar fluxurile companiei website-ului, iar blocul apare doar dacă acea companie are un flux cu căutare online.
- Configurare recomandată: **Based on** = **List Price** în grupul Price al fluxului, pentru ca actualizarea ulterioară a prețului de listă să nu schimbe prețul față de cel afișat; setarea website-ului **Display Product Prices** (Tax Excluded / Tax Included) influențează prețul din card.
- Căutările online salvează produsele găsite în *Vendor Product Catalog*; doar rândul deschis de client primește produs Odoo asociat. Comanda către furnizor se face din reaprovizionare sau automat cu rutele *Buy* și *Replenish on Order (MTO)*.
- Extensibilitate: câmpurile salvate din căutarea online provin din hook-ul `_online_search_fields()`, pe care un conector îl poate completa (conectorul Kramp adaugă codul de bare).
- Fluxul pas-cu-pas, cu capturi de ecran, este în [Fișa Consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- `website_sale`

Nu are dependențe Python externe (`psutil` a fost eliminat în 19.0.1.4.0).

#### 4. Componente Cheie

**Modele**

- `vendor.feed` (extins): adaugă câmpul `online_search`, metoda `online_get_values(search)` (punct de extensie, implementat de conectori), `_online_search_fields()` și `get_products(search)`, care combină produsele existente cu cele aduse online.
- `vendor.product` (extins): `_prepare_values()` adaugă `website_published` și `allow_out_of_stock_order`, deci produsele create sunt publicate și comandabile.
- `website` (extins): `_vendor_online_search_enabled()` întoarce dacă există vreun flux cu căutare online, caz în care `/shop` cere rezultatele de la furnizori.

**Vizualizări**

- `view_vendor_feed_form`: adaugă opțiunea `online_search` în grupul de conexiune al formularului fluxului.
- `products` (șablon, moștenește `website_sale.products`): adaugă înaintea paginatorului containerul `o_vendor_online_search` (cu mesajul „Searching the supplier catalogs..."), afișat când există o căutare cu o singură pagină de rezultate, și marchează mesajul „fără rezultate" pentru a putea fi ascuns.
- `online_results` (șablon): blocul „Available from our suppliers" cu cardurile produselor (imagine, nume, cod, preț, disponibilitate).
- Interacțiunea JS `VendorOnlineSearch` (`static/src/interactions/vendor_online_search.esm.js`): apelează `/vendor_product/online_results` după afișarea paginii și inserează cardurile; erorile furnizorului nu afectează pagina.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Migrarea `19.0.1.2.0` șterge tabela veche `vendor_product_search`.

#### 5. Conexiuni

- [deltatech_vendor_products](../deltatech_vendor_products/index.md): modulul de bază cu produsele și fluxurile furnizorilor; acest modul îi adaugă expunerea în magazinul online.
- [deltatech_vendor_products_kramp](../deltatech_vendor_products_kramp/index.md): conector care folosește `_online_search_fields()` pentru a adăuga codul de bare (conform istoricului modulului).
- `website_sale`: infrastructura de magazin online (coș, comenzi, pagini de produs).
