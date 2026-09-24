# Marketplace Base Connector (localizat la `deltatech_marketplace/index.md`)

- **Nume Tehnic:** `deltatech_marketplace`
- **Versiune:** `19.0.1.27.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_marketplace
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Marketplace Base Connector este modulul de bază al familiei de module marketplace din Odoo, conceput pentru a facilita integrarea între Odoo și diverse platforme de marketplace online (eMAG, Shopify, WooCommerce, PrestaShop, Magento, Trendyol, alt Odoo etc.). Singur, modulul nu vorbește cu niciun magazin — asta o fac conectorii dedicați fiecărei platforme —, dar oferă tot ce e comun pe orice canal: backend-ul (magazinul conectat, cu acces, companie și reguli), obiectele sincronizate (produse, clienți, categorii, stoc) cu regulile lor de import/export, asocierile (legăturile) dintre înregistrările Odoo și cele din magazin, exportul de stoc și preț cu acțiunile programate aferente, coada de joburi în fundal și jurnalul centralizat al operațiunilor. Este fundația unui ecosistem complet de management al marketplace-urilor, cu control centralizat asupra prezenței online pe mai multe platforme.

#### 2. Funcționalități Cheie

- Backend de magazin conectat, cu date de acces, companie, echipă de vânzări, listă de prețuri și reguli de stoc.
- Obiecte sincronizate (produse, șablon de produs, clienți, categorii, stoc), fiecare cu regula lui de import (creează/actualizează, doar unul din cele două, sau niciunul) și de export (automat la scriere sau doar manual).
- Asocieri (legături) Odoo ↔ magazin, pe șablon și pe variantă, cu stocul și prețul din Odoo comparate cu cele din magazin și filtre pentru diferențe (stoc/preț nesincronizat).
- Export de stoc și de preț, cu acțiuni programate dedicate — livrate **dezactivate** la instalare, activate abia după verificarea importului.
- Mapare TVA cotă din magazin → taxă de vânzare Odoo, completată de conector la importul datelor de bază: e o tabelă de referință, **nu decide TVA-ul comenzilor** — acesta vine din taxele de vânzare ale produsului și din poziția fiscală a comenzii.
- Categorie implicită — doar o categorie de rezervă pentru produsele **noi** create fără categorie din magazin; nu leagă categoriile magazinului de ea și nu oprește schimbarea categoriei produselor existente.
- Produs pentru comision (*Fee Product*) — în ciuda etichetei, nu e comisionul platformei: e produsul cu care conectorul WooCommerce adaugă pe comanda clientului taxele/suprataxele din magazin (venit facturat clientului). Comisionul platformei vine pe factura de furnizor a platformei.
- Asistent de sincronizare la cerere pe produs (export/import, tot/stoc/preț), pentru un produs urgent între două rulări.
- Jurnal centralizat al operațiunilor de marketplace (stoc, preț, import, export, webhook, limitare), cu stare de sănătate per backend (Neconfirmat / Erori / Avertismente / În regulă) și curățare automată după un număr configurabil de zile.
- Coadă de joburi (`queue_job`), cu canale proprii per backend și reîncercare automată a joburilor eșuate.

#### 3. Dependențe

- `sale`
- `product`
- `account`
- `stock`
- `queue_job`
- `base_address_extended`

#### 4. Componente Cheie

Conform fluxului de ingestie, această secțiune este sintetizată din `readme/DESCRIPTION.md`. Modulul este construit cu o arhitectură modulară, structurată în:

- Configurări de date (`data`)
- Modele pentru logica de business de bază și pentru jurnalele centralizate de marketplace (`models`)
- Vizualizări pentru interfața cu utilizatorul (`views`)
- Controllere pentru interacțiunile web (`controller`)
- Wizard-uri pentru procese ghidate (`wizard`)
- Definiții de securitate (`security`)
- Servicii JavaScript pentru funcționalitatea de frontend (`static`)
- Suport pentru internaționalizare (`i18n`)

#### 5. Conexiuni

Modulul servește ca fundație pentru un ecosistem complet de management al marketplace-urilor. Următorii conectori de platformă din suita `bitshop_marketplace` au pagină wiki proprie:

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): conector pentru platforma eMAG.
- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): conector pentru platforma Shopify.
- [deltatech_marketplace_woocommerce](../deltatech_marketplace_woocommerce/index.md): conector pentru platforma WooCommerce.
- [deltatech_marketplace_prestashop](../deltatech_marketplace_prestashop/index.md): conector pentru platforma PrestaShop.
- [deltatech_marketplace_magento](../deltatech_marketplace_magento/index.md): conector pentru platforma Magento.
- [deltatech_marketplace_trendyol](../deltatech_marketplace_trendyol/index.md): conector pentru platforma Trendyol.
- [deltatech_marketplace_merchantpro](../deltatech_marketplace_merchantpro/index.md): conector pentru platforma MerchantPro.
- [deltatech_marketplace_opencart](../deltatech_marketplace_opencart/index.md): conector pentru platforma OpenCart.
- [deltatech_marketplace_doraly](../deltatech_marketplace_doraly/index.md): conector pentru platforma Doraly.
- [deltatech_marketplace_odoo](../deltatech_marketplace_odoo/index.md): conector pentru sincronizare Odoo-la-Odoo.
