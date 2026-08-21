# Comenzi de vânzare din Marketplace (localizat la `deltatech_marketplace_sale/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_sale`
- **Versiune:** `19.0.2.4.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_sale
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_sale`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul reprezintă punctul central pentru gestionarea comenzilor de vânzare provenite din diferiți conectori de marketplace, simplificând procesul de la comandă la încasare (order-to-cash) pentru retailerii care vând pe mai multe canale. Din perspectiva afacerii, elimină introducerea manuală a comenzilor și reduce erorile prin automatizarea importului și procesării vânzărilor din mai multe canale (de exemplu eMAG, Shopify, Magento etc.) direct în Odoo, oferind o imagine unificată asupra vânzărilor și menținând sincronizate statusurile comenzilor și nivelurile de stoc.

#### 2. Funcționalități Cheie

- Vizualizare unificată a vânzărilor: monitorizarea și gestionarea comenzilor de pe toate canalele de marketplace dintr-o singură interfață Odoo.
- Eficiență operațională: procesare mai rapidă a comenzilor și timpi de livrare îmbunătățiți pentru fulfillment-ul de marketplace.
- Consistența datelor: sincronizarea statusurilor comenzilor între Odoo și platformele de marketplace respective.
- Raportare financiară corectă: datele de vânzări integrate permit calculul precis al veniturilor și al indicatorilor de performanță pe marketplace.
- Fiabilitatea stocului: actualizările de inventar în timp real, declanșate de vânzările din marketplace, ajută la prevenirea rupturilor de stoc și a supravânzării.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- `sale_stock`
- `stock_delivery`

#### 4. Componente Cheie

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_marketplace_get_order` (cron „Marketplace: Get Orders"): rulează metoda `model.cron_import_orders()` pe modelul `marketplace.backend`, implicit la fiecare 1 oră, pentru a importa comenzile din marketplace în Odoo. Este livrat dezactivat (`active=False`) și trebuie activat manual la configurarea integrării.

#### 5. Conexiuni

- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): extinde gestionarea etapelor (stage) pentru comenzile de vânzare din marketplace.
- [deltatech_marketplace_sale_type](../deltatech_marketplace_sale_type/index.md): adaugă tipuri de comenzi de vânzare specifice fluxurilor de marketplace.
