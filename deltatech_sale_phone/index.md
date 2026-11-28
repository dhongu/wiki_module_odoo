# Sale Phone (localizat la `deltatech_sale_phone/index.md`)

- **Nume Tehnic:** `deltatech_sale_phone`
- **Versiune:** `20.0.1.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_phone`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_phone`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul afișează numărul de telefon al partenerului direct pe comenzile de vânzare și pe facturi, fără navigare către fișa contactului. Echipele de vânzări și de facturare au datele de contact la îndemână în documentul la care lucrează.

#### 2. Funcționalități Cheie

- Telefonul partenerului pe formularul comenzii de vânzare.
- Telefonul partenerului pe formularul facturii.
- Valoarea este preluată automat din fișa partenerului și afișată cu widgetul de telefon.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `sale.order`: câmpul calculat `partner_phone`.
- `account.move`: câmpul calculat `partner_phone`.

**Vizualizări**

- `sale_order_view_form`: telefonul după partener, pe comandă.
- `view_move_form`: telefonul pe factură.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, cron sau acțiuni server.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module cu pagină wiki.
