# Conector Marketplace WooCommerce (localizat la `deltatech_marketplace_woocommerce/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_woocommerce`
- **Versiune:** `19.0.0.0.16`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_woocommerce
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_woocommerce`
- **Ultima Ingestie:** `2026-08-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul conectează Odoo cu magazine online WooCommerce, sincronizând produse, comenzi și clienți din WooCommerce către Odoo și trimițând stocul Odoo înapoi spre magazin, astfel încât o afacere care vinde și pe un site WooCommerce să gestioneze catalogul, comenzile și stocul dintr-un singur backend Odoo, fără introducere manuală de date în două locuri.

#### 2. Funcționalități Cheie

- Sincronizare bidirecțională: produse, clienți și comenzi din WooCommerce către Odoo; stocul Odoo se exportă înapoi spre WooCommerce printr-un cron dedicat, dezactivat implicit.
- Gestiune produse: import produse din WooCommerce, inclusiv variante, mapare categorii, atribute și valori de atribut, sincronizare imagini (dacă „Ignore Images" nu e bifat).
- Gestiune comenzi: import automat al comenzilor WooCommerce, filtrabil după status (`Any`/`pending`/`processing`/`on-hold`/`completed`/`cancelled`/`refunded`/`failed`/`trash`) și după fereastra „Sale Order Days", cu mapare status → fază de vânzare Odoo creată automat la prima întâlnire a unui status nou.
- Integrare clienți: sincronizare date client, adrese de facturare/livrare, istoric de achiziții consolidat ca și contacte Odoo.
- Integrare plăți: mapare metodă de plată WooCommerce către achizitor de plată Odoo, creată automat la prima referință dintr-o comandă.
- Livrare și transport: mapare transportator (creat automat dacă nu există), linie de transport pe comanda importată.
- Suport pentru mai multe magazine WooCommerce, fiecare ca backend separat cu propriile credențiale și setări.
- Test de conexiune care validează efectiv credențialele printr-un apel real către magazin (`system_status`), nu doar completarea câmpurilor.
- Implementare tehnică pe bază de REST API WooCommerce (`wc/v3`), fără bibliotecă Python externă (folosește `requests`), autentificare HTTP Basic Auth (Consumer key/secret) peste HTTPS, procesare pe joburi în fundal (queue jobs) și suport generic de webhook moștenit din framework-ul comun.
- **Nu** exportă prețuri către WooCommerce: lista de prețuri e doar destinația prețului importat din magazin. **Nu** are un cron dedicat de import recurent (comenzi/produse/clienți noi se aduc prin repetarea manuală a acțiunii Import sau printr-o acțiune programată proprie). **Nu** urmărește anulările/rambursările făcute în WooCommerce după import.

*Sursă: `readme/DESCRIPTION.md` și `readme/USAGE.md` (corectate: exportul de preț inexistent a fost eliminat din documentație, exportul de stoc e descris corect ca fiind pe cron dedicat dezactivat implicit, iar testul de conexiune validează efectiv credențialele prin apel real la magazin — vezi și fișa consultant).*

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
