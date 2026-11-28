# eCommerce Country (localizat la `deltatech_website_country/index.md`)

- **Nume Tehnic:** `deltatech_website_country`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_country
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_country`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă extensii legate de țară pentru magazinul online Odoo (eCommerce). Se asigură că formularul de adresă de la finalizarea comenzii (checkout) are întotdeauna o țară pre-selectată implicit, pe baza țării companiei asociate site-ului web, ceea ce reduce efortul clientului la completarea adresei.

#### 2. Funcționalități Cheie

- **Țară implicită la checkout:** dacă nu se poate determina nicio altă țară, formularul de adresă preselectează țara companiei site-ului web; formularul arată județele/statele, prefixul telefonic și câmpurile obligatorii ale acelei țări.
- **Adrese existente fără țară:** și pentru o adresă salvată care nu are țară se preselectează tot țara companiei, împreună cu lista de județe.
- **Datele de bază despre țări:** formularele de adresă se adaptează la formatul țării alese, folosind datele native Odoo.
- **Fundație pentru alte module regionale:** poate servi ca dependență pentru module de website specifice României sau altor regiuni, care au nevoie de o gestionare rafinată a țărilor.
- **Configurare:** nu e necesară nicio configurare în afara setărilor standard; țările și județele pieței țintă se verifică în **Website > Configuration > Countries**.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

Modulul nu definește sau extinde modele Odoo; logica este implementată exclusiv la nivel de controller.

**Controllere / Frontend**

- `WebsiteSale` (extinde controllerul `website_sale`): suprascrie `_get_default_country()` și `_prepare_address_form_values()`, astfel încât, în lipsa unei țări determinate, se folosește țara companiei site-ului web (`env.website.company_id.country_id`).

**Vizualizări**

Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- [deltatech_website_city](../deltatech_website_city/index.md): extensie complementară a formularului de adresă de la checkout, cu selecție structurată a orașului și mapare oraș/cod poștal.
- [deltatech_website_vat_validation](../deltatech_website_vat_validation/index.md): extensie a aceluiași formular de adresă, pentru validarea CUI/VAT.
- [deltatech_website_phone_validation](../deltatech_website_phone_validation/index.md): extensie a formularului de adresă, pentru validarea numărului de telefon.
