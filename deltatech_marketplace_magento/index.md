# Conector Marketplace Magento (localizat la `deltatech_marketplace_magento/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_magento`
- **Versiune:** `19.0.0.0.15`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace_magento
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_magento`
- **Ultima Ingestie:** `2026-09-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Conectorul Magento Marketplace este o extensie Odoo dezvoltată de Terrabit care realizează o integrare fluidă între sistemul ERP Odoo și Magento, o platformă de e-commerce de nivel enterprise. Conectorul permite afacerilor să sincronizeze și să gestioneze magazinele online Magento direct din Odoo, oferind o soluție unificată pentru gestionarea produselor, datelor clienților, comenzilor și a stocurilor pe ambele platforme. Astfel, Magento devine canalul de vânzare online, iar Odoo rămâne sursa unică de adevăr pentru operațiunile de back-office.

#### 2. Funcționalități Cheie

- **Sincronizare completă a produselor**:
  - Import de produse configurabile (cu variante) din Magento în Odoo
  - Gestionarea șabloanelor de produs și a variantelor cu atributele lor
  - Sincronizarea categoriilor de produs și a categoriilor publice
  - Suport pentru seturi de atribute și atribute de produs
  - Procesare în loturi a importului de produse, cu paginare
- **Gestionarea stocurilor**:
  - Sincronizarea nivelurilor de stoc din Odoo către Magento, programată (cron) sau la scriere,
    în funcție de configurare
  - Export de stoc în bulk, prin API-ul de "inventory source-items" al Magento
- **Integrarea clienților**:
  - Import al clienților Magento în baza de contacte Odoo
  - Menținerea unor înregistrări de client consecvente între platforme
- **Gestionarea comenzilor**:
  - Import al comenzilor de vânzare din Magento în Odoo
  - Import de comenzi filtrat după status, nu doar după dată — statusurile disponibile pentru
    filtrare provin din cele deja sincronizate prin importul "Sale Stage", astfel încât statusurile
    custom ale magazinului funcționează la fel ca cele native Magento
  - Crearea automată de comenzi de vânzare Odoo pentru achizițiile din Magento
  - Sincronizarea actualizărilor de stare a comenzilor între sisteme
  - Suport pentru echipe de vânzări cu asociere de depozit
  - Sincronizarea etapelor de vânzare (stările comenzilor)
  - Suport pentru webhook-uri Magento pentru procesarea comenzilor aproape în timp real
- **Procesare livrare și plată**:
  - Integrare cu metodele de livrare Magento
  - Suport pentru mai mulți procesatori de plată
  - Sincronizarea informațiilor de livrare și de plată
- **Operațiuni automatizate**:
  - Procesare în fundal a sarcinilor cu gestionare a cozii de job-uri
  - Paginare și dimensiuni de lot configurabile pentru optimizarea performanței
  - Sarcini de sincronizare programate

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_marketplace_website](../deltatech_marketplace_website/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)
- [deltatech_marketplace_delivery](../deltatech_marketplace_delivery/index.md)
- [deltatech_marketplace_payment](../deltatech_marketplace_payment/index.md)
- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md)

#### 4. Componente Cheie

Documentația principală pentru acest modul provine din `readme/DESCRIPTION.md`, conform fluxului de ingestie; prin urmare analiza detaliată a codului pentru această secțiune este omisă. Implementarea tehnică descrisă în Readme se bazează pe API-ul REST Magento și pe un sistem de binding sofisticat:

**Modele**

- **Backend Adapter**: gestionează autentificarea pe API-ul REST (bazată pe token, obținut prin `POST /integration/admin/token`) și comunicarea cu Magento.
- **Modele de binding**: leagă entitățile Odoo de corespondentele lor din Magento — binding pentru șablon și variantă de produs, pentru atribut de produs și set de atribute, pentru categorii, pentru clienți, pentru comenzi de vânzare și pentru etape de vânzare.

Implementarea urmează modele de procesare asincronă cu cozi de job-uri pentru a gestiona eficient volume mari de date, cu paginare, procesare în fundal prin `with_delay()` și dimensiuni de lot configurabile prin setarea `items_per_page`.

**Mecanismul real de export stoc** (confirmat din `readme/USAGE.md` și `FISA_CONSULTANT.md`, corectat față de o versiune anterioară a paginii care menționa eronat metoda `update_stock`): stocul se exportă către Magento în bulk, printr-un singur apel `POST /inventory/source-items` per backend (`magento_stock_export`, pe `marketplace.product`), cu toate SKU-urile afectate, cantitatea și starea de stoc, întotdeauna pe sursa MSI `default` a Magento (fixă, neconfigurabilă — Multi-Source Inventory cu mai multe surse nu este suportat). Exportul este cablat prin lanțul comun al framework-ului (`_cron_export_stock` / `_cron_export_all_stock` pe `marketplace.backend`, `export_stock_for_items` / `stock_export` pe binder-ul item-ului), necesită bifa **Can Update Stock** activată pe backend și funcționează doar când **Stock Level** rămâne pe valoarea implicită `product` (Product Variant) — pe `template` (Product Template), binder-ul de șablon nu are `magento_stock_export`, iar exportul eșuează tăcut (doar log, fără eroare vizibilă). Fișierul propriu `models/backend_stock.py` al modulului (`magento_cron_export_stock` și altele similare) este cod mort, necablat la niciun cron. Prețul se exportă similar, în bulk, prin `POST /products/base-prices`, cu TVA inclus. Nu există import de stoc sau preț dinspre Magento către Odoo — ambele fluxuri sunt strict Odoo → Magento.

**Mapare câmpuri produs**

Documentată integral în `readme/USAGE.md` (secțiunea „Product field mapping"), derivată din `magento_job_import()`, `magento_extract_custom_attribute()`, `magento_stock_export()` și `magento_export_price()`. **Produsele sunt doar import**: `magento_write()` e un stub care doar scrie un avertisment în jurnal, deci nimic din produsul propriu-zis nu pleacă înapoi — singurele exporturi sunt stocul și prețul, ambele potrivite pe SKU. Prețul se citește doar pe produsul configurabil (șablon); importul de variantă lasă `list_price` neatins.

| Câmp | Câmp Odoo | Câmp Magento | Direcție |
|------|-----------|--------------|----------|
| ID produs | `external_id` (legătură) | `id` (`entity_id`) | Magento → Odoo |
| Denumire produs | `name` | `name` | Magento → Odoo |
| SKU | `default_code`, `external_code` (legătură) | `sku` | Magento → Odoo (și cheia pe care se potrivesc ambele exporturi) |
| Preț de vânzare | `list_price` (doar pe șablon) | `price` | Magento → Odoo |
| Preț exportat | `odoo_price` (legătură) | `/products/base-prices` `price` (cu TVA inclus), `store_id` | Odoo → Magento |
| Greutate | `weight` | `weight` | Magento → Odoo |
| Descriere site | `website_description` (împachetată într-un bloc `section`/`container`) | `custom_attributes` `description` | Magento → Odoo |
| Descriere scurtă | `website_short_description` | `custom_attributes` `short_description` | Magento → Odoo |
| Categorii eCommerce | `public_categ_ids` | `custom_attributes` `category_ids` | Magento → Odoo |
| Imagine principală | `main_image` | `custom_attributes` `image`, prefixat cu **Media URL** din backend | Magento → Odoo |
| Imagini suplimentare | înregistrări `product.image` | `media_gallery_entries[].file`, prefixat cu **Media URL** | Magento → Odoo |
| Atribute configurabile | `attribute_line_ids` | `extension_attributes.configurable_product_options` (`attribute_id`, `values[].value_index`) | Magento → Odoo |
| Valori de atribut | `external_attribute_values`, apoi `odoo_attribute_values` | setul de atribute al produsului (`attribute_set_id`) încrucișat cu `custom_attributes` — intrări `text`, `select` și `multiselect` | Magento → Odoo |
| Variante | legături `marketplace.product` | `extension_attributes.configurable_product_links` (produse de tip `simple`) | Magento → Odoo |
| Stoc | `odoo_stock` (legătură) | `/inventory/source-items` `quantity` și `status`, mereu pe sursa `default` | Odoo → Magento |

#### 5. Conexiuni

- [deltatech_marketplace_purchase](../deltatech_marketplace_purchase/index.md): extensie de aprovizionare a aceleiași suite marketplace; nu este dependență, dar completează fluxul de comenzi de cumpărare.
- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector frate pentru un alt marketplace (eMAG), bazat pe aceeași infrastructură marketplace.
- [deltatech_marketplace_extended](../deltatech_marketplace_extended/index.md): extinderi suplimentare ale funcționalității de bază marketplace.
