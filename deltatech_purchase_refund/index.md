# Refund Purchase (localizat la `deltatech_purchase_refund/index.md`)

- **Nume Tehnic:** `deltatech_purchase_refund`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_purchase_refund
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_refund`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul emite note de credit de la furnizor pentru cantități negative din comenzile de achiziție. Când o comandă are cantități de facturat negative, factura se deschide direct ca notă de credit, nu ca factură obișnuită.

#### 2. Funcționalități Cheie

- Detectează cantitățile negative de facturat pe comanda de achiziție.
- Deschide factura ca notă de credit furnizor (`in_refund`) în loc de factură normală.
- Înregistrează cantități pozitive pe linia notei de credit, cu soldul recalculat în moneda companiei.
- Permite alegerea comenzii de achiziție de origine direct în formularul notei de credit.

#### 3. Dependențe

- `base`
- `account`
- `purchase_stock`
- `stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order`: `action_view_invoice` alege tipul documentului după cantități.
- `purchase.order.line`: pregătirea liniei contabile calculează cantitatea și soldul.

**Vizualizări**

- `view_move_form`: câmpul `purchase_id` pe nota de credit furnizor în ciornă.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_purchase_price](../deltatech_purchase_price/index.md): alt modul Terrabit pe fluxul de achiziții (legătură doar tematică).
