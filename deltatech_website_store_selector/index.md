# eCommerce Store Selector

- **Nume Tehnic:** `deltatech_website_store_selector`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_store_selector
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_store_selector`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite vizitatorului magazinului online să-și aleagă **magazinul propriu**, ca la marile lanțuri de bricolaj. Stocul afișat, depozitul comenzii și livrarea urmează magazinul ales, astfel încât site-ul funcționează pentru magazinul respectiv. Alegerea este ținută într-un cookie timp de un an.

#### 2. Funcționalități Cheie

- **Buton de magazin** în antet (toate variantele de antet, desktop și mobil): arată magazinul ales și deschide lista magazinelor, cu căutare, adresă, telefon și, când poziția vizitatorului e cunoscută din GeoIP și magazinele sunt geolocalizate, distanța (cele mai apropiate primele).
- **Stocul urmează magazinul**: disponibilitatea de pe pagina produsului, banda „stoc epuizat”, butonul rapid de adăugare, limita de cantitate la adăugarea în coș și avertizările din coș se calculează pe stocul liber al magazinului ales.
- **Pagina produsului** arată disponibilitatea variantei în magazin (în stoc, stoc limitat, disponibil la comandă, indisponibil) și permite verificarea celorlalte magazine.
- **Casetele din magazin** (listă de produse) arată disponibilitatea fiecărui produs în magazin, calculată o singură dată pentru toată pagina.
- **Comanda urmează magazinul**: coșul se creează pe magazinul ales, depozitul comenzii este magazinul, iar livrarea pleacă de acolo. Schimbarea magazinului mută coșul și avertizează dacă noul magazin nu poate onora comanda integral.
- Cu **Click & Collect** (`website_sale_collect`) se instalează automat modulul [deltatech_website_store_selector_collect](../deltatech_website_store_selector_collect/index.md).
- Configurare: câte un depozit per magazin (cu adresa și telefonul pe partenerul depozitului); în *Website > Configurare > Setări > Shop - Inventory* se completează **Store Selector** cu depozitele alese de vizitator (apare doar dacă există mai multe depozite). Pe produsele vândute per magazin se debifează *Sell when Out-of-Stock*. Fără magazine în setare, site-ul păstrează comportamentul standard.
- Construit să nu încarce site-ul: fără interogări suplimentare pe pagini, stocul tuturor magazinelor se calculează doar la deschiderea listei, fără apeluri către servicii externe de geolocalizare. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `website_sale_stock`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse`: extins cu datele magazinului (adresă, telefon, geolocalizare).
- `website`: stochează magazinele selectabile și calculează magazinul vizitatorului.
- `sale.order`: coșul este creat pe depozitul magazinului ales.
- `product.template` / `product.product`: disponibilitate calculată pe stocul liber al magazinului.
- `res.config.settings`: setarea **Store Selector**.

**Vizualizări**

- `views/templates.xml`: butonul din antet, lista magazinelor, blocul de magazin din pagina produsului și avertizările din coș.
- `views/res_config_settings_views.xml`: setarea magazinelor selectabile.
- `views/sale_order_views.xml`: magazinul pe comanda de vânzare.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_website_store_selector_collect](../deltatech_website_store_selector_collect/index.md): legătura cu Click & Collect, instalată automat.
- `website_sale_collect`: metoda *Pick up in store* poate folosi aceleași depozite.
