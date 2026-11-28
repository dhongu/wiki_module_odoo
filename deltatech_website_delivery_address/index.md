# eCommerce Delivery Address (localizat la `deltatech_website_delivery_address/index.md`)

- **Nume Tehnic:** `deltatech_website_delivery_address`
- **Versiune:** `20.0.1.0.2`
- **Cale:** [https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_delivery_address](https://github.com/dhongu/deltatech/tree/20.0/deltatech_website_delivery_address)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_delivery_address`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite stabilirea unei adrese de livrare implicite pentru fiecare utilizator de website. La finalizarea comenzii, adresa preferată este preselectată, ceea ce accelerează comenzile și reduce erorile de selecție.

#### 2. Funcționalități Cheie

- Administratorul poate seta o adresă de livrare implicită pentru utilizatori specifici ai website-ului.
- Adresa preferată este preselectată automat în procesul de checkout.
- Se integrează cu fluxul standard de checkout al website-ului Odoo.
- Utilizare: **Settings > Users & Companies > Users**, se deschide profilul utilizatorului de website și se completează adresa de livrare implicită; la următorul checkout al clientului, adresa este selectată implicit.

#### 3. Dependențe

- `website_sale`

#### 4. Componente Cheie

**Modele**

- `res.users` (extins): câmpul `delivery_address_id` (adresa de livrare implicită, `res.partner`).
- `website` (extins): `_prepare_sale_order_values` folosește adresa implicită la crearea comenzii.

**Vizualizări**

- `views/res_users_view.xml`: secțiunea pentru adresa de livrare implicită pe formularul utilizatorului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `website_sale`: fluxul de checkout în care adresa este preselectată.
