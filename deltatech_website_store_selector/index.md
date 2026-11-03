# eCommerce Store Selector (Alegerea magazinului pe website)

- **Nume Tehnic:** `deltatech_website_store_selector`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_store_selector
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_store_selector`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îi permite vizitatorului magazinului online să-și aleagă **magazinul fizic** preferat, ca pe site-urile marilor rețele de bricolaj. Din acel moment, site-ul lucrează pentru magazinul ales: stocul afișat este cel al magazinului, coșul și comanda se creează pe magazinul respectiv, iar livrarea pleacă de acolo. Fără magazine configurate, site-ul păstrează comportamentul standard Odoo.

#### 2. Funcționalități Cheie

- **Buton „Magazinul tău” în header** (toate variantele de header, desktop și mobil): arată magazinul ales și deschide lista magazinelor, cu căutare, adresă, telefon și, dacă poziția vizitatorului este cunoscută din GeoIP și magazinele sunt geolocalizate, distanța (cele mai apropiate primele). Lista nu apelează niciun serviciu extern de geolocalizare.
- **Stocul urmează magazinul**: disponibilitatea de pe pagina de produs, panglica „stoc epuizat”, butonul de adăugare rapidă, limita de cantitate la adăugarea în coș și avertizările din coș se calculează pe stocul liber al magazinului ales.
- **Pagina de produs**: afișează disponibilitatea variantei selectate în magazin (în stoc, stoc limitat, disponibil la comandă, indisponibil) și permite verificarea celorlalte magazine.
- **Cardurile din magazinul online** afișează disponibilitatea fiecărui produs în magazin, calculată dintr-o dată pentru toată pagina.
- **Comanda urmează magazinul**: coșul se creează pe magazinul ales, depozitul comenzii este magazinul, deci livrarea pleacă de acolo. Schimbarea magazinului mută coșul și avertizează vizitatorul dacă noul magazin nu poate livra tot conținutul.
- **Click & Collect** (`website_sale_collect`): puntea `deltatech_website_store_selector_collect` se instalează automat; magazinul devine locația de ridicare propusă la finalizarea comenzii, iar alegerea altui magazin de ridicare schimbă și magazinul vizitatorului.
- Alegerea este păstrată într-un cookie pentru un an (rezistă sesiunii și deconectării).
- **Fără impact asupra performanței**: nicio interogare suplimentară pe pagini (magazinul se citește din cookie), stocul tuturor magazinelor se calculează doar când se deschide lista, iar paginile publice din cache-ul de pagini Odoo rămân partajate (se păstrează în cache doar versiunea fără magazin, numele magazinului fiind pus în header la servire).
- **Configurare** (detalii în fișa consultantului):
  - câte un depozit pe magazin, în *Inventar > Configurare > Depozite*, cu adresa (și telefonul) pe partenerul depozitului;
  - în *Website > Configurare > Setări > Shop - Inventory*, câmpul **Store Selector** (vizibil când există mai multe depozite) primește magazinele selectabile;
  - pe produsele vândute per magazin se debifează *Sell when Out-of-Stock* și, opțional, se bifează *Show Available Quantity*;
  - pentru ridicare din magazin se adaugă aceleași depozite metodei de livrare *Pick up in store*.

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `website` (extins): câmpul `store_warehouse_ids` (magazinele selectabile, validate să aparțină companiei website-ului); citirea magazinului ales din cookie, scrierea cookie-ului, stocul disponibil și valorile comenzii calculate pe magazin.
- `sale.order` (extins): câmpul `website_store_id` (magazinul ales de client); depozitul comenzii și depozitul de verificare a stocului din coș urmează magazinul; mutarea coșului pe alt magazin cu verificarea disponibilității.
- `stock.warehouse` (extins): date de afișare a magazinului (adresă, telefon, coordonate, distanță Haversine).
- `product.template` / `product.product` (extinse): informațiile de disponibilitate per magazin pentru variantă și pentru lista de produse.
- `website.page` (extins): integrarea cu cache-ul de pagini, astfel încât doar versiunea fără magazin să fie cache-uită.
- `res.config.settings` (extins): `website_store_warehouse_ids`, setarea magazinelor selectabile.

**Vizualizări**

- `res_config_settings_view_form`: câmpul Store Selector în setările de inventar ale magazinului online.
- `view_order_form` (`sale.order`): afișează magazinul website pe comandă, lângă depozit.
- `header_store_link`: butonul magazinului în header (moștenește `website_sale.header_cart_link`).
- `product_store_availability`: blocul de disponibilitate în magazin pe pagina de produs.
- `products_item_store_stock`: disponibilitatea pe cardurile de produs.
- Front-end: dialogul de selecție (`store_selector_dialog.esm.js`) și interacțiunea `store_selector.esm.js`.

Rute (controller): `/shop/store/list` (lista magazinelor, cu stoc la cerere) și `/shop/store/set` (setarea magazinului ales).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_website_store_selector_collect](../deltatech_website_store_selector_collect/index.md): puntea cu Click & Collect (`website_sale_collect`), instalată automat.
