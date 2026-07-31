# eCommerce Pager Guard

- **Nume Tehnic:** `deltatech_website_pager_guard`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_pager_guard`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_pager_guard`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul face ca magazinul online să răspundă cu eroare **404** atunci când cineva cere o pagină de listare care nu există. În mod nativ, componenta de paginare (`pager`) a Odoo limitează silențios un număr de pagină în afara intervalului la ultima pagină reală, în loc să refuze cererea — astfel, o adresă precum `/shop/page/999999` răspunde cu cod `200` și conținutul ultimei pagini valide. Un motor de căutare (crawler) interpretează acest răspuns ca pe o confirmare că pagina există, urmărește tiparul la infinit și nu se mai oprește niciodată. Pe un site în producție, acest comportament a generat 2.386 cereri pe zi doar pentru o singură adresă de tipul `/shop/category/…/page/3467514`, fiecare cerere presupunând o căutare completă de produse și randare QWeb. Modulul elimină acest risipă de resurse și trimite motoarelor de căutare un semnal corect că spațiul de adrese al magazinului este finit.

#### 2. Funcționalități Cheie

- Returnează eroare **404 (Not Found)** pentru orice pagină de listare din magazin (`/shop/page/N`) situată dincolo de ultima pagină reală.
- Pagina `/shop` (fără parametru de pagină) și ultima pagină reală rămân neafectate — funcționează normal.
- Nu impune o limită fixă (hardcodată) de pagini: numărul total de pagini este determinat dinamic, după numărarea produselor, evitând astfel blocarea accesului la pagini reale pe cataloage mari (s-a observat un catalog real cu 2.578 de pagini valide).
- Verificarea are loc după randarea logicii de bază, dar înainte de randarea efectivă a șablonului QWeb (care este „lazy" în Odoo), deci nu se pierde performanță suplimentară — se evită tocmai partea costisitoare a cererii.
- Reduce sarcina serverului generată de crawlere care exploatează acest comportament pentru a genera cereri infinite către pagini inexistente.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile pentru componente nu sunt detaliate atunci când există un fișier `readme/DESCRIPTION.md`. Modulul nu definește modele, vizualizări sau acțiuni automate proprii; întreaga funcționalitate este implementată printr-un singur controller care extinde `website_sale`:

- `controllers/main.py` — clasa `WebsiteSalePagerGuard(WebsiteSale)` suprascrie metoda de rută `shop()`: apelează `super().shop(...)`, citește `page_count` din contextul QWeb al paginatorului (`pager`) și ridică `werkzeug.exceptions.NotFound` dacă pagina cerută depășește numărul real de pagini.

#### 5. Conexiuni

- `website_sale`: modulul de bază al magazinului online — controllerul `shop()` al acestuia este extins pentru a adăuga verificarea limitei de paginare.
- [deltatech_website_disable_fuzzy_search](../deltatech_website_disable_fuzzy_search/index.md): modul înrudit tematic, care extinde tot controllerele de căutare/listare din `website_sale` pentru a controla precizia rezultatelor afișate în magazin.
