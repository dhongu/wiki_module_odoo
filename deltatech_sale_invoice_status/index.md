# Sale Invoice Status (localizat la `deltatech_sale_invoice_status/index.md`)

- **Nume Tehnic:** `deltatech_sale_invoice_status`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_invoice_status
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_invoice_status`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul ține starea de facturare a comenzii de vânzare legată de livrare. Când o comandă conține și produse, și servicii, iar marfa nu a fost livrată, comanda nu apare ca „De facturat". Astfel serviciile nu sunt facturate înaintea livrării mărfii.

#### 2. Funcționalități Cheie

- Starea de facturare a comenzii depinde de livrare pentru produsele consumabile.
- Dacă linii de produse și de servicii sunt prezente și nu s-a livrat nimic, starea de facturare devine „Nu" (nimic de facturat).
- Dacă există doar servicii, starea rămâne „De facturat".

#### 3. Dependențe

- `sale`
- `delivery`

#### 4. Componente Cheie

**Modele**

- `sale.order.line`: metoda `_can_be_invoiced_alone` este suprascrisă pentru regula de mai sus.

**Vizualizări**

- Modulul nu adaugă vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- Niciuna documentată suplimentar față de dependențe.
