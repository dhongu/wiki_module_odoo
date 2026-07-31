# eCommerce Country (localizat la `deltatech_website_country/index.md`)

- **Nume Tehnic:** `deltatech_website_country`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_country`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_country`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul oferă extensii legate de țară pentru platforma de eCommerce a Odoo. Se asigură că formularul de adresă de la finalizarea comenzii (checkout) are întotdeauna o țară pre-selectată implicit, pe baza țării companiei asociate site-ului web, îmbunătățind astfel experiența de completare a adresei pentru clienți.

#### 2. Funcționalități Cheie

- **Logică frontend specifică pe țară:** îmbunătățește formularul de adresă de la checkout cu o selecție mai bună a țării și a județului/statului.
- **Integrare cu datele de bază despre țări:** formularele de adresă se adaptează la formatul țării alese, folosind datele native Odoo despre țări.
- **Validare optimizată a adresei:** oferă o bază pentru validări de adresă mai avansate (precum maparea oraș/cod poștal) atunci când este folosit împreună cu alte extensii Deltatech pentru website.
- **Fundație pentru alte module regionale:** acționează ca dependință standard pentru alte module de website specifice României sau altor regiuni, care necesită o gestionare rafinată a țărilor.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

Modulul nu definește sau extinde modele Odoo — logica este implementată exclusiv la nivel de controller.

**Controllere / Frontend**

- `WebsiteSale` (extinde `website_sale.controllers.main.WebsiteSale`): suprascrie `_prepare_address_form_values()` astfel încât, dacă nu există deja o țară determinată pentru formularul de adresă, se folosește implicit țara companiei site-ului web (`request.website.company_id.country_id`).

#### 5. Conexiuni

- [deltatech_website_city](../deltatech_website_city/index.md): extensie complementară a formularului de adresă de la checkout, cu selecție structurată a orașului și mapare oraș/cod poștal — exact scenariul de „validare avansată a adresei" menționat ca fiind acoperit împreună cu acest modul.
- [deltatech_website_vat_validation](../deltatech_website_vat_validation/index.md): extensie a aceluiași formular de adresă de checkout, pentru validarea CUI/VAT.
- [deltatech_website_phone_validation](../deltatech_website_phone_validation/index.md): extensie a formularului de adresă de checkout, pentru validarea numărului de telefon.
