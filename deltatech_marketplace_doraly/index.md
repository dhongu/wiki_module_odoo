# Conector Doraly (localizat la `deltatech_marketplace_doraly/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_doraly`
- **Versiune:** `20.0.0.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_doraly
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_doraly`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un conector între Odoo și marketplace-ul Doraly, construit pe cadrul general de marketplace al suitei Terrabit. Permite autentificarea către platforma Doraly, importul catalogului de produse și al comenzilor primite, exportul parțial al produselor și trimiterea către Doraly a linkului PDF al facturii. Astfel, comercianții care vând prin Doraly își gestionează produsele și comenzile direct din Odoo, fără introducere manuală. Modulul este în stadiul Alpha.

#### 2. Funcționalități Cheie

- Logare: da. Se configurează în **Marketplace > Backends**, cu Provider **Doraly**; locația se completează cu `https://ylarod.ro/api/vendors`, iar accesul se face cu utilizator și parolă ale contului de vânzător, validat cu **Test connection**.
- Import produse: da. Se importă doar codul și numele (codul de vânzător devine referință internă, codul Doraly este codul extern), fără preț, stoc sau descriere.
- Export produse: parțial. Se trimite câte un produs pe apel; brandul nu este preluat din produs (se trimite o valoare fixă).
- Import comenzi: da. Fiecare comandă devine comandă de vânzare cu numărul Doraly, client potrivit după telefon sau e-mail, adrese, faza din starea Doraly, linie de transport pe transportatorul implicit și liniile de produs; prețul fără TVA se deduce din suma cu TVA, astfel încât totalul să coincidă.
- Export comenzi: nu. Generare AWB: nu.
- Trimitere factură PDF: da. La confirmarea facturii se trimite către Doraly linkul de portal al PDF-ului, construit din parametrul `web.base.url` (adresa publică a Odoo).
- Setare obligatorie pentru transport: **Default Carrier** (tab Orders and Products), deoarece Doraly trimite doar suma transportului, nu curierul.
- Limitări cunoscute (din USAGE): importul de categorii creează mereu aceeași categorie de test, erorile HTTP 429/5xx nu se reîncearcă automat, iar la importul produselor prețurile pot necesita corecție înainte de facturare.
- Fluxul pas-cu-pas, cu capturi, este în [Fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_website_short_description](../deltatech_website_short_description/index.md)
- `delivery`
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)

#### 4. Componente Cheie

Documentația din `readme/DESCRIPTION.md` acoperă scopul și funcționalitățile modulului, fără a detalia componentele tehnice. Conform fluxului de ingestie, analiza detaliată a modelelor, vizualizărilor și acțiunilor automate a fost omisă, întrucât nu este cerută explicit în Readme. Pentru maparea câmpurilor de produs, vezi `readme/USAGE.md` din modul (`models/binding_product.py`, `views/backend_views.xml`).

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază pe care se construiește conectorul Doraly.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): importul și sincronizarea comenzilor de vânzare din marketplace.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): maparea stadiilor comenzilor între Doraly și Odoo.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): maparea metodelor de livrare.
- [deltatech_website_short_description](../deltatech_website_short_description/index.md): descrierea scurtă a produsului, trimisă ca descriere la exportul de produse.
