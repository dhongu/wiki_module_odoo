# Conector Marketplace Odoo către Odoo (localizat la `deltatech_marketplace_odoo/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_odoo`
- **Versiune:** `20.0.0.3.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_odoo
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_odoo`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un conector Odoo-către-Odoo peste cadrul Marketplace al suitei. Permite unei companii să preia dintr-un alt Odoo datele de bază (catalogul de produse, categoriile, atributele, partenerii, lista de prețuri) și, în varianta B2B, să trimită comenzile de achiziție confirmate către Odoo-ul furnizorului, unde devin comenzi de vânzare. Astfel se elimină introducerea manuală a datelor între cele două sisteme.

#### 2. Funcționalități Cheie

- Import șabloane de produs, variante, atribute cu valori, categorii și parteneri din Odoo-ul de la distanță; legăturile lipsă (categoria produsului, compania părinte a clientului) se creează din mers.
- Import în joburi de fundal, de pe cardurile din fila **Objects** a backend-ului (meniul ⋮ → **Import** sau **Import All**); în varianta B2B se adaugă și o linie de furnizor cu prețul din Odoo-ul de la distanță.
- Import listă de prețuri, cu regulile ei legate de produsele, șabloanele, categoriile sau lista de bază locale; cardul **Price List** se adaugă manual în fila **Objects**.
- Conectare prin XML-RPC: în fila **Credentials** se completează **Location**, tipul de acces *User and password*, utilizatorul API, parola și, pentru B2B, **Access Token** (tokenul de securitate al backend-ului din Odoo-ul de la distanță); **Test connection** mută backend-ul în starea **Confirmed**.
- Setări specifice (doar pentru provider-ul Odoo): baza de date, versiunea Odoo de la distanță, **Odoo Integration B2B**, furnizorul și clientul; **Import basic data** citește partenerul utilizatorului API și lista lui de prețuri.
- Flux B2B: la confirmarea unei comenzi de achiziție către furnizorul backend-ului, un job creează și confirmă comanda de vânzare corespunzătoare în Odoo-ul de la distanță (conectorul trebuie instalat și acolo); mesajele din comandă se trimit printr-un job separat, iar schimbările de stare doar dacă este activ **Active On Write** pe cardul **Purchase Order**.
- Joburile apar la butonul **Jobs** al backend-ului, iar erorile în **Marketplace > Logs**.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, componentele nu au fost analizate în cod (readme-ul acoperă funcționalitatea).

**Modele**

- `marketplace.backend` (extins): adaugă provider-ul `odoo` și câmpurile de conexiune.
- Modelele de legătură ale cadrului (`marketplace.product.template`, `marketplace.product`, `marketplace.product.attribute`, `marketplace.product.category`, `marketplace.public.category`, `marketplace.customer`, `marketplace.product.pricelist`, `marketplace.sale.order`, `marketplace.purchase.order` ș.a.) sunt extinse cu logica de import/export Odoo.
- `purchase.order` și `sale.order` (extinse): legătura cu comenzile din Odoo-ul de la distanță.

**Vizualizări**

- `views/backend_views.xml`: câmpurile conectorului în formularul backend-ului.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește sarcini `ir.cron` proprii; importurile și trimiterile rulează ca joburi de fundal.

#### 5. Conexiuni

- Nu există conexiuni suplimentare față de dependențele din secțiunea 3 (verificat în manifest; \`deltatech_marketplace_website\` nu mai este dependență pe 20.0).
