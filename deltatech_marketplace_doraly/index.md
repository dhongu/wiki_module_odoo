# Conector Doraly (localizat la `deltatech_marketplace_doraly/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_doraly`
- **Versiune:** `19.0.0.0.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_doraly`
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_doraly`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul oferă un conector între Odoo și marketplace-ul Doraly, extinzând cadrul general de integrare cu marketplace-uri din suita Terrabit. Scopul său principal este să sincronizeze datele comerciale dintre magazinul Doraly și sistemul ERP Odoo: permite autentificarea către platforma Doraly, importul catalogului de produse, exportul parțial al produselor și importul comenzilor primite în marketplace. Astfel, comercianții care vând prin Doraly își pot gestiona produsele și comenzile direct din Odoo, fără introducere manuală a datelor.

#### 2. Funcționalități Cheie

- Logare (autentificare) către platforma Doraly: da
- Import produse din Doraly în Odoo: da
- Export produse din Odoo către Doraly: parțial
- Import comenzi din Doraly în Odoo: da
- Export comenzi din Odoo către Doraly: nu
- Generare AWB: nu
- Trimitere factură PDF: nu

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_website_short_description](../deltatech_website_short_description/index.md)
- `delivery`
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)

#### 4. Componente Cheie

Documentația din `readme/DESCRIPTION.md` acoperă scopul și funcționalitățile modulului, fără a detalia componentele tehnice. Conform fluxului de ingestie, analiza detaliată a modelelor, vizualizărilor și acțiunilor automate a fost omisă, întrucât nu este menționată explicit în Readme.

#### 5. Conexiuni

- [deltatech_marketplace](../deltatech_marketplace/index.md): cadrul de bază pentru conectarea Odoo la marketplace-uri (backend, adaptoare, binding-uri), pe care se construiește conectorul Doraly.
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md): gestionarea importului și sincronizării comenzilor de vânzare din marketplace.
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): cartografierea stadiilor comenzilor între Doraly și Odoo.
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md): gestionarea metodelor de livrare asociate marketplace-ului.
</content>
