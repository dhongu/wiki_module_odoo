# Conector Marketplace WooCommerce (localizat la `deltatech_marketplace_woocommerce/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_woocommerce`
- **Versiune:** `20.0.0.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_woocommerce
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_woocommerce`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un magazin WooCommerce ținut lângă Odoo fără conector înseamnă același catalog, aceiași clienți și aceleași comenzi în două locuri: produsul adăugat în Odoo se recreează în WordPress, comanda de pe site se reintroduce, iar stocul se desincronizează. Conectorul aduce produsele, clienții și comenzile din WooCommerce în Odoo și trimite stocul înapoi, dintr-un singur backend. Fiind construit pe cadrul `deltatech_marketplace`, comun cu Shopify, eMAG și ceilalți conectori, nu cere învățarea unui al doilea sistem.

#### 2. Funcționalități Cheie

- Import produse din WooCommerce, inclusiv variante, categorii, atribute și imagini (dacă „Ignore Images” nu e bifat); produsele sunt doar import, iar prețul vine de pe variații.
- **Map Products** leagă produsele deja existente în ambele sisteme, după referința internă egală cu SKU-ul, fără import (codul de bare nu se caută).
- Import clienți cu adrese de facturare și livrare.
- Import comenzi cu client, adrese, linii, linie de transport, metodă de plată și taxe; filtrare după status (**Import Orders With Status**) și după fereastra „Sale Order Days”; statusul se mapează pe o fază de vânzare, creată la prima apariție. Transportatorii, metodele de plată și fazele se creează automat la prima referință.
- Export de stoc (`stock_quantity` și `stock_status`) prin cron-ul comun de export, dezactivat implicit; necesită „Can send stock” pe backend. Nu există export de preț.
- Mai multe magazine WooCommerce, fiecare ca backend separat, cu credențiale proprii (Consumer key/secret; HTTPS recomandat).
- Test de conexiune prin apelul real `system_status`; badge de sănătate pe card, cu legături la jurnale și la joburile eșuate.
- Importurile rulează ca joburi în coadă; **Only Missing** și **Items Per Page** controlează volumul. Un import recurent nu are cron dedicat, iar anulările/rambursările din WooCommerce după import nu ajung în Odoo; cupoanele nu se importă ca înregistrări separate.
- Nu necesită bibliotecă Python externă (folosește `requests`); funcționează pe On-Premise și Odoo.sh, nu pe Odoo Online.
- Flux pas-cu-pas, cu capturi, în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` și `readme/USAGE.md`; analiza detaliată a codului este omisă conform fluxului de ingestie. Maparea câmpurilor de produs, din `readme/USAGE.md`:

| Câmp | Câmp Odoo | Câmp WooCommerce | Direcție |
|------|-----------|------------------|----------|
| ID produs | `external_id` (legătură) | `id` | WooCommerce → Odoo |
| Denumire | `name` | `name` | WooCommerce → Odoo |
| SKU | `default_code`, `external_code` | `sku` | WooCommerce → Odoo |
| Descriere site | `website_description` | `description` | WooCommerce → Odoo |
| Greutate | `weight` | `weight` | WooCommerce → Odoo |
| Preț | `list_price` | `price`, de pe variație | WooCommerce → Odoo |
| Atribute și valori de variantă | `marketplace.product.attribute`, `attribute_line_ids`, `odoo_attribute_values` | `attributes[]` | WooCommerce → Odoo |
| Imagini | `image_1920`, `product.image` | `images[]` | WooCommerce → Odoo |
| Cantitate în stoc | `odoo_stock` (legătură) | `stock_quantity` | Odoo → WooCommerce |
| Stare stoc | derivată din `odoo_stock` | `stock_status` | Odoo → WooCommerce |

#### 5. Conexiuni

- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): conector analog, pentru Shopify.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector analog, pentru eMAG.
- [deltatech_marketplace_magento](../deltatech_marketplace_magento/index.md): conector analog, pentru Magento.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): conector analog, pentru PrestaShop.
