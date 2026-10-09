# eCommerce Delivery Address (localizat la `deltatech_website_delivery_address/index.md`)

- **Nume Tehnic:** `deltatech_website_delivery_address`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_delivery_address
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_delivery_address`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite administratorului să stabilească pentru fiecare utilizator de website o adresă de livrare implicită. Atunci când clientul se autentifică și începe o comandă online, adresa respectivă este preselectată automat, ceea ce accelerează comenzile și reduce erorile de selecție.

#### 2. Funcționalități Cheie

- Câmp nou „Delivery Address" pe fișa utilizatorului, configurabil de administrator.
- Adresa configurată este setată automat ca adresă de livrare pe comanda de vânzare (coș) creată din website.
- Configurare: **Setări > Utilizatori și companii > Utilizatori**, se deschide utilizatorul, câmpul apare sub semnătură.
- Fără configurare, comportamentul standard al checkout-ului din website rămâne neschimbat.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `res.users` (extins): adaugă câmpul `delivery_address_id` (Many2one către `res.partner`).
- `website` (extins): suprascrie `_prepare_sale_order_values`; dacă utilizatorul curent are `delivery_address_id`, îl folosește ca `partner_shipping_id` al comenzii.

**Vizualizări**

- `view_users_form_forum`: moștenește `base.view_users_form` și afișează `delivery_address_id` după câmpul `signature`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `website_sale`: fluxul standard de creare a coșului, în care este injectată adresa.
