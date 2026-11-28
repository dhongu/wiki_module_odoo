# Delivery in locker - website (localizat la `deltatech_delivery_locker_website/index.md`)

- **Nume Tehnic:** `deltatech_delivery_locker_website`
- **Versiune:** `20.0.0.0.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_locker_website
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_locker_website`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul aduce livrarea în locker (punct de ridicare) în magazinul online. Leagă gestiunea de bază a lockerelor de fluxul de comandă `website_sale`, astfel încât metodele de livrare din checkout să fie filtrate după compatibilitatea produselor din coș. Clientul vede doar opțiunile relevante și alege fluid punctul de ridicare.

#### 2. Funcționalități Cheie

- **Filtrare a metodelor de livrare:** dacă un produs stocabil din coș este marcat nepotrivit pentru locker (`for_locker = False`), metodele cu **Use Locker** sunt ascunse în checkout.
- **Alegerea lockerului:** pentru o metodă cu locker, clientul apasă **Select a location**, alege punctul din listă sau de pe hartă (**Choose this location**), iar lockerul devine adresa de livrare a comenzii; pe comandă apar bannerul „Delivery to Locker" și câmpul **Locker**.
- **Context de checkout:** pagina de checkout primește indicatorul `for_locker` pentru coșul curent.
- **Insignă „Locker":** opțională, pe cardul și pe pagina produsului pentru articolele livrabile în locker; se activează din vizualizările tehnice (inactivă implicit).
- **Locker unic până la AWB:** selecția din magazin, adresa de livrare și AWB-ul citesc aceeași valoare, deci coletul pleacă la lockerul ales de client.
- **Dependențe separate:** modulul de bază [deltatech_delivery_locker](../deltatech_delivery_locker/index.md) rămâne independent de eCommerce. Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md)
- [deltatech_website_city](../deltatech_website_city/index.md)
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extindere): `_get_delivery_methods()` exclude metodele cu `use_locker` dacă în comandă există un produs stocabil cu `for_locker = False`.

**Controlere**

- `WebsiteSaleLocker` (extinde `website_sale.WebsiteSale`): adaugă în valorile paginii de checkout indicatorul `for_locker`, calculat pe produsele stocabile din comandă.

**Vizualizări**

- `views/templates.xml`: insigna „Locker" pe cardul de produs și pe pagina produsului (`products_item_locker_badge_on_card`, `product_locker_badge_on_pdp`), inactive implicit.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): modulul de bază al livrării în locker, extins pentru website.
- [deltatech_website_city](../deltatech_website_city/index.md): selecția localității în checkout.
- `website_sale`: fluxul standard eCommerce în care se filtrează metodele de livrare și se afișează insignele.
