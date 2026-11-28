# Sale Order Search by Contact (importable, Odoo Online) (localizat la `deltatech_saleorder_search/index.md`)

- **Nume Tehnic:** `deltatech_saleorder_search`
- **Versiune:** `20.0.1.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_saleorder_search`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_saleorder_search`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ajută la găsirea comenzilor de vânzare atunci când despre client se știe doar o adresă de e-mail sau un număr de telefon. Nu necesită nicio configurare și poate fi folosit și pe Odoo Online.

#### 2. Funcționalități Cheie

- Căutare după e-mail: bara de căutare a ofertelor și comenzilor primește opțiunea „Search E-mail for: ...”, care returnează comenzile al căror client are un e-mail ce conține textul introdus. O parte comună, de exemplu domeniul `@example.com`, găsește comenzile tuturor clienților de pe acel domeniu.
- Căutare după telefon: opțiunea „Search Phone for: ...” face același lucru cu numărul de telefon; textul este potrivit așa cum e tastat, deci numărul se introduce în formatul în care e stocat pe contact (un fragment scurt, fără spații sau prefix, găsește cele mai multe variante).
- Funcționează în **Sales > Orders > Quotations** și **Orders**, precum și în orice altă listă de comenzi care folosește vizualizarea de căutare standard.
- Căutarea se face pe e-mailul și telefonul contactului setat ca „Customer” pe comandă, nu pe alte contacte ale aceleiași companii.
- Fără cod Python, doar o extensie de vizualizare de căutare: se poate importa pe Odoo Online (plan Custom) din **Apps > Import Module**, pe lângă Odoo.sh și on-premise.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

Secțiunea se bazează pe `readme/DESCRIPTION.md`; verificarea codului a confirmat doar elementele de mai jos.

**Modele**

- Nu definește și nu extinde modele Python.

**Vizualizări**

- `view_sales_order_filter`: extinde vizualizarea de căutare a comenzilor cu filtrele „E-mail” (`partner_id.email`) și „Phone” (`partner_id.phone`), cu potrivire parțială (`ilike`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- Nu au fost identificate module cu pagină wiki existentă legate funcțional de acest modul.
