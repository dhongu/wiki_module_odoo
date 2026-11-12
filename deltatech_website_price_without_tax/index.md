# Price Without Tax on Website (localizat la `deltatech_website_price_without_tax/index.md`)

- **Nume Tehnic:** `deltatech_website_price_without_tax`
- **Versiune:** `19.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_price_without_tax
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_price_without_tax`
- **Ultima Ingestie:** `2026-11-06`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul afișează, pe pagina produsului din magazinul online Odoo, un rând suplimentar cu prețul fără TVA, sub prețul principal. Este util în special pentru site-urile cu clienți atât persoane fizice, cât și firme (B2B), unde prețul fără TVA este cel relevant pentru firme. Prețul net se calculează automat pentru varianta afișată, indiferent de modul în care este configurată taxa pe produs.

#### 2. Funcționalități Cheie

- Rândul **Preț fără TVA:** apare imediat după instalare pe pagina produsului, sub prețul principal, în moneda website-ului.
- Calcul după modul de afișare al website-ului (**Website → Configurare → Setări → Display Product Prices**): cu **Tax Excluded**, prețul afișat este deja net și rândul îl repetă; cu **Tax Included**, taxele produsului se scad din prețul afișat, ca și cum ar fi incluse în preț, oricum ar fi configurată taxa (de exemplu 121 lei cu TVA 21% → 100 lei).
- Valoarea se calculează la încărcarea paginii, pentru varianta afișată; la produsele cu variante de prețuri diferite, reîncărcarea paginii variantei confirmă rândul.
- Rândul este o vizualizare opțională (`customize_show`), activă după instalare. În Odoo 19 nu are comutator în panoul editorului de website: se oprește din **Setări → Tehnic → Interfață utilizator → Vizualizări** (modul dezvoltator), căutând „Product Price without tax” și debifând **Activ**; dacă website-ul are o copie proprie, se oprește copia acelui website.
- Prețul este doar afișat: comanda, factura și TVA-ul se calculează în continuare de Odoo; fără efect contabil.
- La upgrade din 18.0, scripturile de migrare 19.0.1.0.4 dezactivează temporar vizualizarea generică veche și o reactivează după încărcarea noii structuri; copiile specifice website-urilor rămân neatinse.

#### 3. Dependențe

- `website`
- `website_sale`

#### 4. Componente Cheie

Modulul are `readme/DESCRIPTION.md` minimal; componentele sunt descrise după cod.

**Modele**

- `product.template` (extins): `_get_combination_info` adaugă în informațiile de combinație cheia `list_price_without_tax`, calculată din prețul afișat, după modul de afișare al website-ului.

**Vizualizări**

- `product_price_without_tax`: șablon QWeb care moștenește `website_sale.product_price` și adaugă în containerul prețului rândul „Preț fără TVA:” (opțional, `customize_show`, prioritate 100).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate sau acțiuni server. Directorul `migrations/19.0.1.0.4` conține scripturile `pre-migration.py` și `end-migration.py`, folosite doar la upgrade.

#### 5. Conexiuni

- `website_sale`: modulul standard de eCommerce al cărui afișaj de preț este extins cu valoarea fără taxe.
