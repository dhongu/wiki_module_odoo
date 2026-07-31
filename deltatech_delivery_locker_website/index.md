# Delivery in locker - website (localizat la `deltatech_delivery_locker_website/index.md`)

- **Nume Tehnic:** `deltatech_delivery_locker_website`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_locker_website
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_locker_website`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul extinde funcționalitatea de livrare în locker (punct de ridicare) pentru interfața de website și eCommerce. Rolul său principal este să facă legătura între gestiunea de bază a lockerelor și fluxul de comandă online (`website_sale`), astfel încât metodele de livrare să fie filtrate corect în pagina de checkout, în funcție de compatibilitatea produselor din coș. În acest fel, clientul care plasează o comandă online vede doar opțiunile de livrare relevante și are o experiență fluidă atunci când alege un punct de ridicare.

#### 2. Funcționalități Cheie

- **Filtrare inteligentă a metodelor de livrare**: filtrează automat metodele de livrare disponibile în pagina de checkout în funcție de compatibilitatea produselor. Dacă un produs din coș este marcat ca nepotrivit pentru livrarea în locker (`for_locker = False`), curierii care au activată opțiunea „Use Locker” sunt ascunși.
- **Context de checkout**: furnizează pagina de checkout cu informații suplimentare privind compatibilitatea coșului curent pentru livrarea în locker.
- **Integrare eCommerce**: asigură puntea între gestiunea de bază a lockerelor și fluxul Odoo `website_sale`, pentru o experiență coerentă la selectarea punctelor de ridicare.
- **Dependențe optimizate**: este conceput să funcționeze împreună cu `website_sale`, păstrând în același timp modulul de bază [deltatech_delivery_locker](../deltatech_delivery_locker/index.md) independent de componentele de eCommerce.

#### 3. Dependențe

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md)
- `deltatech_website_city`
- `website_sale`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, această secțiune nu este detaliată la nivel de cod (modele, vizualizări, acțiuni automate), descrierea funcțională acoperind scopul modulului. Vezi secțiunile 1 și 2.

#### 5. Conexiuni

- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): modulul de bază pentru gestiunea livrării în locker, pe care acest modul îl extinde pentru website/eCommerce.
- `deltatech_website_city`: componenta de website pentru selecția localității, utilizată în fluxul de checkout.
- `website_sale`: fluxul standard Odoo de eCommerce în care sunt filtrate metodele de livrare.
