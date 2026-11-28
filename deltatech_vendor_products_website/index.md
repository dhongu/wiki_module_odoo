# Vendor Products Website (localizat la `deltatech_vendor_products_website/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products_website`
- **Versiune:** `20.0.1.4.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_vendor/tree/20.0/deltatech_vendor_products_website
- **Cale Locală:** `odoo-addons/bitshop_vendor/deltatech_vendor_products_website`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde gestionarea produselor furnizorilor către magazinul online. Permite căutarea produselor în cataloagele furnizorilor, importul lor automat în lista de produse din Odoo, afișarea lor pe website și comandarea lor de către vizitatori prin fluxul standard de eCommerce, fără gestionare manuală separată a fiecărui articol.

#### 2. Funcționalități Cheie

- **Căutare online în shop:** pe fluxul de furnizor se bifează **Online Search** (grupul *Connection*, vizibil doar când fluxul are tip de conexiune). Când o căutare în shop nu găsește produsul, blocul **Available from our suppliers** afișează articolele găsite la furnizor, cu imagine, nume, cod, preț și disponibilitate („Available at the supplier” sau „On order”).
- Blocul apare doar când rezultatele shop-ului încap pe o pagină (se caută un cod, nu un cuvânt general) și se încarcă după afișarea paginii, deci un furnizor lent nu încetinește shop-ul. Produsele fără preț la furnizor nu se afișează.
- **Creare produs la click:** la click pe un card, produsul se creează din rândul catalogului (dacă nu există), se publică, se poate comanda și fără stoc, apoi urmează fluxul standard de coș și comandă.
- Fiecare căutare salvează produsele găsite în *Purchase > Products > Vendor Product Catalog*; doar rândul deschis de client primește produs Odoo.
- **Preț:** pornește de la prețul de listă al furnizorului, cu regulile fluxului (**Discount**, **Surcharge**, **Extra Fee**; recomandat *Based on* = **List Price**), convertit în moneda website-ului și afișat cu sau fără taxe, după setarea *Display Product Prices*.
- **Limite de căutare** (parametri de sistem): `vendor_product_online_search_session_limit` (implicit 10/minut pe sesiune) și `vendor_product_online_search_ip_limit` (implicit 60/minut pe IP); 0 dezactivează limita. Într-o bază multi-companie se caută doar în fluxurile companiei website-ului.
- Pașii detaliați sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_vendor_products](../deltatech_vendor_products/index.md)
- `website_sale`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, completate din CONFIGURE.md și USAGE.md; componentele sunt listate pe scurt din cod.

**Modele**

- `vendor.feed` (extins): adaugă câmpul `online_search`.
- `vendor.product` (extins): creare și publicare produs din rândul de catalog.
- `website` (extins): logica de căutare online a furnizorilor.

**Vizualizări**

- `views/vendor_info_view.xml`: bifa Online Search pe fluxul de furnizor.
- `views/templates.xml`: blocul „Available from our suppliers” în shop; încărcarea se face prin interacțiuni JS din `web.assets_frontend`.
- Controller: ruta `/vendor_product/online_results` (jsonrpc, public) întoarce rezultatele de la furnizor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_vendor_products](../deltatech_vendor_products/index.md): catalogul de produse furnizor pe care acest modul îl expune în shop.
- [deltatech_vendor_products_kramp](../deltatech_vendor_products_kramp/index.md): conector Kramp care folosește căutarea online.
- [deltatech_vendor_products_granit](../deltatech_vendor_products_granit/index.md): conector Granit care folosește căutarea online.
- `website_sale`: infrastructura de shop (coș, comenzi, pagina de produs).
