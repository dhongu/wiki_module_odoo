# Delivery in locker - website (localizat la `deltatech_delivery_locker_website/index.md`)

- **Nume Tehnic:** `deltatech_delivery_locker_website`
- **Versiune:** `19.0.0.0.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_locker_website
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_locker_website`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde funcționalitatea de livrare în locker (punct de ridicare) pentru interfața de website și eCommerce. Rolul său principal este să facă legătura între gestiunea de bază a lockerelor și fluxul de comandă online (`website_sale`), astfel încât metodele de livrare să fie filtrate corect în pagina de checkout, în funcție de compatibilitatea produselor din coș. În acest fel, clientul care plasează o comandă online vede doar opțiunile de livrare relevante și are o experiență fluidă atunci când alege un punct de ridicare.

#### 2. Funcționalități Cheie

- **Filtrare inteligentă a metodelor de livrare**: filtrează automat metodele de livrare disponibile în pagina de checkout în funcție de compatibilitatea produselor. Dacă un produs stocabil din coș este marcat ca nepotrivit pentru livrarea în locker (`for_locker = False`), curierii care au activată opțiunea „Use Locker” sunt ascunși.
- **Context de checkout**: furnizează pagina de checkout cu informații suplimentare privind compatibilitatea coșului curent pentru livrarea în locker (`for_locker` în valorile paginii).
- **Badge vizual „Locker”**: afișează (opțional, prin funcționalități de personalizare website) un badge pe cardul de produs și pe pagina de produs pentru articolele care pot fi livrate în locker.
- **Integrare eCommerce**: asigură puntea între gestiunea de bază a lockerelor și fluxul Odoo `website_sale`, pentru o experiență coerentă la selectarea punctelor de ridicare.
- **Dependențe optimizate**: este conceput să funcționeze împreună cu `website_sale`, păstrând în același timp modulul de bază [deltatech_delivery_locker](../deltatech_delivery_locker/index.md) independent de componentele de eCommerce.

#### 3. Dependențe

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md)
- [deltatech_website_city](../deltatech_website_city/index.md)
- `website_sale`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, secțiunile de Sumar și Funcționalități Cheie provin din readme; suplimentar, câmpurile HISTORY.md și codul sursă indică următoarele componente tehnice relevante.

**Modele**

- `sale.order` (extindere): adaugă metoda `_get_delivery_methods()`, care exclude din lista de curieri disponibili pe cei cu `use_locker` activat dacă în comandă există cel puțin un produs stocabil marcat `for_locker = False`. Câmpul `locker` este definit ca derivat (calculat, cu invers) în [deltatech_delivery_locker](../deltatech_delivery_locker/index.md) și nu mai este redefinit aici.

**Controlere**

- `WebsiteSaleLocker` (extinde `website_sale.WebsiteSale`): suprascrie `shop_checkout` (elimină parametrul `express` la apelul standard) și `_prepare_checkout_page_values`, adăugând în valorile paginii de checkout indicatorul `for_locker`, calculat pe baza compatibilității tuturor produselor stocabile din comandă.

**Vizualizări**

- `products_item_locker_badge_on_card` (moștenește `website_sale.products_item`, inactiv implicit, activabil din personalizarea temei): afișează un badge „Locker” pe cardul de produs din listare, pentru produsele cu `for_locker = True`.
- `product_locker_badge_on_pdp` (moștenește `website_sale.product`, inactiv implicit, activabil din personalizarea temei): afișează același badge pe pagina de detaliu a produsului.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): modulul de bază pentru gestiunea livrării în locker, pe care acest modul îl extinde pentru website/eCommerce.
- [deltatech_website_city](../deltatech_website_city/index.md): componenta de website pentru selecția localității, utilizată în fluxul de checkout.
- `website_sale`: fluxul standard Odoo de eCommerce în care sunt filtrate metodele de livrare și în care se afișează badge-urile de produs.
