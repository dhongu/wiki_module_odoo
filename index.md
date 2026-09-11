# Odoo Modules Wiki - Index (seria 18.0)

Acest fișier este catalogul central al modulelor documentate pe această ramură. Este menținut de asistentul LLM.

**Despre ramura `18.0`:** wiki-ul complet trăiește pe ramura `19.0`. Ramura `18.0` conține doar paginile efectiv verificate pe codul seriei 18.0 — restul modulelor rămân documentate exclusiv pe `19.0`, ca să nu existe pe această ramură pagini care descriu comportament de altă serie. Fiecare pagină de aici are un paragraf **Diferențe față de seria 19.0** în secțiunea Componente Cheie.

## Module

- [deltatech_marketplace_emag](deltatech_marketplace_emag/index.md): Conector eMAG Marketplace — oferte, comenzi, stoc, geografie românească, AWB și auto-pricing pe buy box; în această serie integrarea de curier eMAG este în interiorul modulului.
- [deltatech_marketplace_merchantpro](deltatech_marketplace_merchantpro/index.md): Conector MerchantPro — export produse și categorii, export stoc și preț, import comenzi prin webhook și job paginat.
- [deltatech_marketplace_prestashop](deltatech_marketplace_prestashop/index.md): Conector PrestaShop — catalog multilingv, clienți, comenzi și stoc (doar dinspre magazin), cu webhook de intrare și rută de facturi.
- [deltatech_marketplace_shopify](deltatech_marketplace_shopify/index.md): Conector Shopify — produse, clienți, comenzi, stoc și prețuri; în această serie comunicarea e exclusiv pe REST Admin API, fără stratul GraphQL.
- [deltatech_marketplace_trendyol](deltatech_marketplace_trendyol/index.md): Conector Trendyol — oferte identificate prin cod de bare, export asincron de preț și stoc prin API-ul batch, comenzi și AWB.
- [deltatech_marketplace_woocommerce](deltatech_marketplace_woocommerce/index.md): Conector WooCommerce — produse doar import, comenzi și clienți din magazin, export de stoc și push de status al comenzii.
