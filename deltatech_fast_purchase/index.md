# Fast Purchase (localizat la `deltatech_fast_purchase/index.md`)

- **Nume Tehnic:** `deltatech_fast_purchase`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_fast_purchase
- **Cale Locală:** `odoo-addons/deltatech/deltatech_fast_purchase`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul comprimă într-un singur clic confirmarea comenzii de achiziție, recepția și facturarea. Este util când marfa intră în gestiune odată cu cumpărarea și nu se justifică parcurgerea separată a fiecărei etape.

#### 2. Funcționalități Cheie

- Buton „Confirm, Receipt and Bill" pe comanda de achiziție, care parcurge într-un pas confirmarea, recepția și facturarea.
- Buton „Receipt and Bill" pentru comenzile deja confirmate.
- Buton „Receipt Notice" pe comanda de achiziție, care generează recepția pe bază de aviz.
- Buton „Invoice" pe recepție, pentru introducerea directă a facturii.

#### 3. Dependențe

- `base`
- `purchase_stock`
- `stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): acțiunile `action_button_confirm_to_invoice` și `action_button_confirm_notice`, plus `receipt_to_stock` pentru recepția automată.
- `stock.picking` (extins): `action_view_invoice`, care deschide factura de pe recepție.
- `account.move` (extins): fără logică activă.

**Vizualizări**

- `purchase_order_form`: adaugă în antetul comenzii butoanele „Confirm, Receipt and Bill", „Receipt and Bill" și „Receipt Notice".
- `view_picking_form`: adaugă butonul „Invoice" pe recepție.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [deltatech_fast_sale](../deltatech_fast_sale/index.md): modul analog pentru vânzări (confirmare, livrare, facturare într-un pas).
