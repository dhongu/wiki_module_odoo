# eCommerce Store Selector - Click & Collect

- **Nume Tehnic:** `deltatech_website_store_selector_collect`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_store_selector_collect
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_store_selector_collect`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face legătura dintre alegerea magazinului pe website și ridicarea din magazin (Click & Collect) din Odoo. Magazinul ales de client rămâne același de la pagina de produs până la predarea comenzii: este propus automat ca punct de ridicare la checkout, iar stocul afișat și verificat este al acestui magazin. Se instalează automat când sunt prezente ambele module de care depinde.

#### 2. Funcționalități Cheie

- Magazinul ales pe website este punctul de ridicare propus la checkout pentru metoda „Ridicare de la sediu”, chiar dacă metoda deservește mai multe magazine.
- Alegerea altui punct de ridicare pe harta de la checkout face din acel magazin magazinul clientului (header, stoc afișat, depozitul comenzii).
- Schimbarea magazinului din header mută ridicarea comenzii pe noul magazin sau o golește, dacă metoda de ridicare nu deservește acel magazin.
- Stocul afișat și verificat este cel al magazinului ales, nu cel mai bun stoc dintre toate magazinele de ridicare; se evită și calculul stocului pentru fiecare magazin pe paginile de produs.
- Listarea punctelor de ridicare (harta de la checkout) nu mai lasă pe liniile coșului avertizările magazinelor fără stoc: decide doar magazinul ales.
- Pagina de produs afișează blocul „Magazinul tău” în locul blocului Click & Collect, care ignoră magazinul vizitatorului; punctul de ridicare se alege astfel la checkout.
- Configurare: pe metoda de ridicare se lasă în fila **Magazine** aceleași magazine ca în „Alegerea magazinului”, iar furnizorul „Plata la fața locului” trebuie să fie activ și publicat (detalii în fișa consultant).

#### 3. Dependențe

- [deltatech_website_store_selector](../deltatech_website_store_selector/index.md)
- `website_sale_collect`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): mută comanda pe magazinul de ridicare (depozit, magazin website, cookie), propune magazinul clientului ca punct implicit de ridicare, reacționează la schimbarea magazinului din header și calculează stocul liber doar pentru magazinul ales.
- `delivery.carrier` (extins): la listarea punctelor de ridicare păstrează neschimbate avertizările liniilor coșului.
- `product.template` (extins): ascunde blocul Click & Collect de pe pagina de produs când website-ul folosește alegerea magazinului.
- `website` (extins): cantitatea disponibilă (inclusiv maximul pentru ridicare) este stocul magazinului ales.

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [deltatech_website_store_selector](../deltatech_website_store_selector/index.md): modulul de bază care oferă alegerea magazinului pe website.
- `website_sale_collect`: ridicarea din magazin standard Odoo, ale cărei comportamente sunt ajustate aici.
