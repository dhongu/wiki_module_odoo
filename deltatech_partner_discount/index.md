# Partner Discount (localizat la `deltatech_partner_discount/index.md`)

- **Nume Tehnic:** `deltatech_partner_discount`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_partner_discount
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_discount`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaugă pe partener un câmp cu reducerea propusă și avertizează utilizatorul pe factură, printr-un banner, când partenerul are o reducere recomandată. Modificarea reducerii este rezervată unui grup restrâns de utilizatori.

#### 2. Funcționalități Cheie

- Câmpul *Proposed discount* (procent) pe formularul partenerului.
- Doar utilizatorii din grupul *Can modify partner discount* pot crea parteneri cu reducere sau modifica reducerea; regula se aplică și la import și RPC, nu doar în formular.
- Pe factură apare un banner „Recommended discount: X" cu reducerea propusă a partenerului comercial (compania).

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): câmpul `discount` și verificarea dreptului de modificare la `create`, `write` și `onchange`.
- `account.move` (extins): câmpul `partner_discount`, legat de reducerea partenerului comercial.

**Vizualizări**

- `view_partner_form_discount`: câmpul de reducere pe partener.
- `invoice_form_discount_propose`: bannerul cu reducerea recomandată pe factură.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Grupul `group_partner_discount` este definit în `security/groups.xml`.

#### 5. Conexiuni

- Nu are legături cu alte module din wiki.
