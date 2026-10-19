# Vendor Products Kramp (localizat la `deltatech_vendor_products_kramp/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_kramp`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_vendor/tree/19.0/deltatech_vendor_products_kramp`
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_kramp`
- **Ultima Ingestie:** `2026-10-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează catalogul de produse al furnizorului la Kramp, distribuitorul de piese de schimb agricole, prin API-ul webshop-ului Kramp. Cu butonul *Încarcă preț* de pe feed, toate produsele Kramp din catalog primesc prețul net și brut al clientului, stocul, termenul de livrare și codul de bare, fără introducere manuală.

#### 2. Funcționalități Cheie

- Căutare online (prin ruta JSON-RPC `/vendor_product/online_search` a modulului website; în Odoo 19 căutarea nu are încă interfață pe /shop): un cod sau un termen este căutat la Kramp (inclusiv după cod EAN), iar articolele găsite sunt adăugate în catalogul furnizorului cu denumirea Kramp, imaginea, prețul net (de achiziție) și prețul brut (de listă). Fără credențiale căutarea returnează doar denumiri și imagini, fără prețuri.
- Actualizare prețuri: butonul „Load Price API" de pe feed-ul furnizorului sau de pe produsele furnizorului citește prețurile net și brut curente de la Kramp, în loturi de 25 de produse per cerere, pentru toate produsele feed-ului; codurile se potrivesc indiferent de majuscule.
- Disponibilitate: Kramp nu publică stocul, deci conectorul îl deduce din planurile de livrare. Cantitatea livrată în maximum 10 zile devine cantitatea disponibilă (cel mult 999), iar zilele până la prima livrare devin termenul de achiziție.
- Cod de bare: preluat din EAN-ul Kramp la căutare și la actualizarea prețurilor; un cod de bare pe care Kramp nu îl are este păstrat.
- Configurare feed (*Achiziții > Produse > Vendor Feed*): tip conexiune **Kramp**, furnizor, moneda prețurilor Kramp (RON pentru Kramp România), utilizator și parolă ale contului de webshop, *Kramp Locale* (implicit `ro_RO`; Kramp returnează prețuri doar în locale-ul propriului magazin, altfel actualizarea prețurilor se oprește cu eroare) și bifa *Online Search*.
- Autentificare eficientă: token-ul este reținut până la expirare și reînnoit fără retrimiterea parolei; fiecare cerere are timeout.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md)

#### 4. Componente Cheie

**Modele**

- `vendor.feed` (extins): adaugă tipul de conexiune `kramp`, câmpurile `kramp_locale`, `token_temp`, `token_expires_in`, `token_refresh` și metodele `load_price_api`, `online_get_values`, `get_token`, plus logica de disponibilitate și valorile articolelor.
- `vendor.product` (extins): suportă actualizarea prețurilor, a stocului și a codului de bare din Kramp.
- `KrampWebshopClient` (clasă Python, `models/kramp_webshop.py`): client pentru login (`auth.kramp.com`), reînnoirea token-ului și interogări GraphQL pe `www.kramp.com/graphql/webshop` (căutare, articole, planuri de livrare).

**Vizualizări**

- `view_vendor_feed_form`: extinde formularul feed-ului cu câmpurile Kramp (locale, credențiale, căutare online).

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): dependența directă; conectorul Kramp răspunde la căutarea online a acestui modul și adaugă codul de bare prin `_online_search_fields()`.
- [deltatech_vendor_products](../deltatech_vendor_products/index.md): modulul de bază al suitei de produse furnizor (modelele `vendor.feed` și `vendor.product`).
