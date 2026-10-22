# Website Shop Header (localizat la `deltatech_website_shop_header/index.md`)

- **Nume Tehnic:** `deltatech_website_shop_header`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_shop_header
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_shop_header`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Adaugă un șablon de antet (header) pentru magazine online cu catalog mare, în care vizitatorul caută după cod și navighează pe categorii. Antetul pune în centru o casetă de căutare mare, afișează permanent contul, lista de dorințe, coșul și telefonul și oferă un buton evidențiat pentru toate categoriile. Șablonul nu este activ după instalare: se alege per website, deci instalarea nu schimbă nimic în site.

#### 2. Funcționalități Cheie

- **Bară de beneficii** deasupra antetului: mesaje scurte cu iconiță (livrare rapidă, retur, ramburs) și numărul de telefon; textele se editează direct în website.
- **O singură casetă de căutare**, mare, în mijlocul antetului, cu text indicativ propriu („Caută după cod, OEM sau denumire..."); antetul nu mai afișează a doua casetă de căutare.
- **Cont, listă de dorințe și coș**, cu contoare, plus **telefonul** mereu vizibil.
- **Meniul website-ului** sub acestea; elementul de meniu automat al categoriilor (din `deltatech_website_shop_snippets`, *Mega Menu Source*: *Shop categories (automatic)*) apare ca buton evidențiat cu iconiță de meniu, urmat de linkuri rapide (Produse noi, Reduceri, Lichidare de stoc).
- **Pe telefon**: antetul mobil standard al website-ului, cu caseta de căutare mereu vizibilă sub logo (fără a doua în panoul de meniu); în panou, elementele de meniu apar ca plăci pe două coloane, iar meniul de categorii ca acordeon dedesubt.
- Șablonul se activează per website, la fel ca șabloanele de antet standard.
- Stadiu de dezvoltare: Alpha.

#### 3. Dependențe

- `website_sale`
- `website_sale_wishlist`
- [deltatech_website_shop_snippets](../deltatech_website_shop_snippets/index.md)

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele Python.

**Vizualizări**

- `template_header_shop`: șablon de antet (moștenește `website.layout`, înlocuiește `nav`, `active="False"`) cu bara de beneficii, căutare, cont, wishlist, coș și meniu.
- `header_benefits_bar`: bara de beneficii de deasupra antetului.
- `template_header_mobile_search`: extinde `website.template_header_mobile` pentru căutarea vizibilă pe telefon.
- `static/src/scss/header.scss`: stilurile antetului (încărcate în `web.assets_frontend`).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_website_shop_snippets](../deltatech_website_shop_snippets/index.md): furnizează elementul de meniu automat de categorii, afișat ca buton în antet.
- `website_sale_wishlist`: sursa listei de dorințe și a contorului din antet.
