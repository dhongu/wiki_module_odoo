# eCommerce Pager Guard

- **Nume Tehnic:** `deltatech_website_pager_guard`
- **Versiune:** `19.0.1.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_pager_guard`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_pager_guard`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Acest modul face ca magazinul online să răspundă cu eroare **404** atunci când cineva cere o pagină de listare care nu există sau o ordonare (`?order=`) invalidă. În mod nativ, componenta de paginare (`pager`) a Odoo limitează silențios un număr de pagină în afara intervalului la ultima pagină reală, în loc să refuze cererea — astfel, o adresă precum `/shop/page/999999` răspunde cu cod `200` și conținutul ultimei pagini valide. Un motor de căutare (crawler) interpretează acest răspuns ca pe o confirmare că pagina există, urmărește tiparul la infinit și nu se mai oprește niciodată. Pe un site în producție, acest comportament a generat 2.386 cereri pe zi doar pentru o singură adresă de tipul `/shop/category/…/page/3467514`, fiecare cerere presupunând o căutare completă de produse și randare QWeb. Modulul elimină această risipă de resurse și trimite motoarelor de căutare un semnal corect că spațiul de adrese al magazinului este finit.

#### 2. Funcționalități Cheie

- Returnează eroare **404 (Not Found)** pentru orice pagină de listare din magazin (`/shop/page/N`) situată dincolo de ultima pagină reală.
- Pagina `/shop` (fără parametru de pagină) și ultima pagină reală rămân neafectate — funcționează normal.
- Nu impune o limită fixă (hardcodată) de pagini: numărul total de pagini este determinat dinamic, după numărarea produselor, evitând astfel blocarea accesului la pagini reale pe cataloage mari (s-a observat un catalog real cu 2.578 de pagini valide).
- Verificarea are loc după randarea logicii de bază, dar înainte de randarea efectivă a șablonului QWeb (care este „lazy" în Odoo), deci nu se pierde performanță suplimentară — se evită tocmai partea costisitoare a cererii.
- Reduce sarcina serverului generată de crawlere care exploatează acest comportament pentru a genera cereri infinite către pagini inexistente.
- Un parametru `?order=` invalid în magazin (câmp necunoscut, câmp care nu poate fi sortat sau clauză malformată, ex. `?order=1034054500` trimis de crawlere) returnează acum **404**, în loc de eroare `500` cu traceback `ValueError: Invalid field`.
- Clauza de ordonare este validată înaintea oricărei căutări de produse, cu parserul propriu al ORM, deci fără acces la baza de date.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Modulul nu definește modele, vizualizări sau acțiuni automate proprii; întreaga funcționalitate este implementată printr-un singur controller care extinde `website_sale`:

- `controllers/main.py` — clasa `WebsiteSalePagerGuard(WebsiteSale)`:
  - `shop()` (rută moștenită prin `@route()` fără argumente): apelează `super().shop(...)`, citește `page_count` din contextul QWeb al paginatorului (`pager`) și ridică `werkzeug.exceptions.NotFound` dacă pagina cerută depășește numărul real de pagini.
  - `_get_search_order()`: dacă `?order=` este prezent și invalid, ridică `NotFound` înainte de căutarea produselor.
  - `_is_valid_shop_order()`: compilează clauza de ordonare cu `_order_to_sql` al `product.template` pe un `Query` de probă și returnează `False` la `ValueError`, `UserError` sau `AccessError`.

#### 5. Conexiuni

- `website_sale`: modulul de bază al magazinului online — controllerul `shop()` al acestuia este extins pentru a adăuga verificarea limitei de paginare.
- [deltatech_website_disable_fuzzy_search](../deltatech_website_disable_fuzzy_search/index.md): modul înrudit tematic, care extinde tot controllerele de căutare/listare din `website_sale` pentru a controla precizia rezultatelor afișate în magazin.
