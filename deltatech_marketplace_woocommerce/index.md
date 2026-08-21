# Conector Marketplace WooCommerce (localizat la `deltatech_marketplace_woocommerce/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_woocommerce`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_woocommerce
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_woocommerce`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul conectează Odoo cu magazine online WooCommerce, sincronizând bidirecțional produse, comenzi, clienți, transportatori și metode de plată, astfel încât o afacere care vinde și pe un site WooCommerce să gestioneze tot din Odoo, fără introducere manuală de date și fără riscul de suprevânzare din cauza stocurilor neactualizate.

#### 2. Funcționalități Cheie

- Sincronizare bidirecțională: produse și stoc din Odoo către WooCommerce, comenzi și clienți din WooCommerce către Odoo, cu actualizări în timp real sau programate.
- Gestiune produse: creare/actualizare produse în WooCommerce din Odoo, mapare categorii, atribute și variante, sincronizare imagini și niveluri de stoc.
- Gestiune comenzi: import automat al comenzilor WooCommerce, sincronizare stare comandă, gestionare etape și stări, modificări/anulări, istoric complet.
- Integrare clienți: sincronizare date client, adrese, grupuri/etichete, istoric de achiziții, profiluri unificate.
- Integrare plăți: mapare metode de plată WooCommerce către Odoo, sincronizare stare plată, suport pentru diverse gateway-uri, procesare rambursări.
- Livrare și transport: mapare metode de livrare, partajare informații de tracking, sincronizare costuri de transport, suport multi-curier.
- Integrare website: suport pentru mai multe magazine WooCommerce, prețuri și stoc specifice per site, reguli de sincronizare personalizabile.
- Raportare unificată a vânzărilor pe toate canalele și informații privind performanța WooCommerce direct în Odoo.
- Implementare tehnică pe bază de REST API WooCommerce, procesare pe joburi în fundal, mapare inteligentă a datelor, logare erori/sincronizări și webhook-uri pentru evenimente în timp real.

*Sursă: `readme/DESCRIPTION.md`.*

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)

#### 4. Componente Cheie

*(secțiune omisă conform fluxului de ingestie: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar Componentele Cheie nu sunt cerute explicit de readme)*

#### 5. Conexiuni

- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): conector marketplace analog, pentru magazine Shopify, construit pe același nucleu `deltatech_marketplace`.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector marketplace analog, pentru eMAG.
- [deltatech_marketplace_magento](../deltatech_marketplace_magento/index.md): conector marketplace analog, pentru Magento.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): conector marketplace analog, pentru PrestaShop.
