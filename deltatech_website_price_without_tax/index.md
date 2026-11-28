# Price Without Tax on Website (localizat la `deltatech_website_price_without_tax/index.md`)

- **Nume Tehnic:** `deltatech_website_price_without_tax`
- **Versiune:** `20.0.1.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_price_without_tax
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_price_without_tax`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un magazin care vinde atât consumatorilor, cât și firmelor afișează de obicei prețurile cu TVA, în timp ce un cumpărător firmă vrea prețul net. Modulul adaugă pe pagina de produs a site-ului o linie cu prețul fără TVA, utilă mai ales în scenarii B2B.

#### 2. Funcționalități Cheie

- **Linia de preț net:** blocul de preț al produsului primește o linie discretă *Preț fără TVA:* cu suma în moneda site-ului; linia este ascunsă când suma este zero.
- **Urmărește modul de afișare:** dacă prețurile sunt afișate fără taxe, linia repetă prețul afișat; altfel taxele produsului sunt scoase din prețul afișat, ca și cum toate ar fi incluse în el. Setarea listei de prețuri o suprascrie pe cea a site-ului.
- **Doar afișare:** prețurile din coș, comenzi și facturi nu sunt modificate.
- **Vizualizare opțională:** linia este o vizualizare opțională (*Product Price without tax*), activă după instalare, care poate fi dezactivată pentru un singur site.
- **Observații:** orice vizitator vede linia; eticheta este scrisă în română în șablon și nu are traducere. Suma provine din `list_price`, nu din `price`, deci produsele de test trebuie să aibă reducere prin listă de prețuri pentru a vedea diferența. Pașii cu capturi sunt în fișa consultant.

#### 3. Dependențe

- `website`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.template`: suprascrie `_get_combination_info` și adaugă `list_price_without_tax` în datele de preț ale combinației.

**Vizualizări**

- `product_price_without_tax`: șablon care moștenește `website_sale.product_price` și adaugă linia *Preț fără TVA* (vizualizare opțională, `customize_show`).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- `website_sale`: modulul standard de eCommerce al cărui bloc de preț este extins cu valoarea fără taxe.
