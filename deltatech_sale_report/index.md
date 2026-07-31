# Sale Report Additional Info (localizat la `deltatech_sale_report/index.md`)

- **Nume Tehnic:** `deltatech_sale_report`
- **Versiune:** `19.0.0.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_report](https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_report)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_report`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul îmbogățește raportul de vânzări din Odoo (`sale.report`) cu adresa de email a partenerului, astfel încât informația să fie disponibilă direct în analizele și pivotările standard de vânzări, fără a mai fi nevoie de căutări suplimentare în fișele de contact.

#### 2. Funcționalități Cheie

- Adaugă câmpul email al partenerului (`partner_email`) în raportul de vânzări (`sale.report`).

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.report`: extins cu câmpul `partner_email` (email-ul partenerului), populat prin suprascrierea `_select_additional_fields()` și inclus în agregare prin `_group_by_sale()`.

**Vizualizări**

Modulul nu adaugă vizualizări proprii; câmpul nou este disponibil pentru a fi expus manual în vizualizările existente ale raportului de vânzări (pivot/gantt/grafic) care se bazează pe modelul `sale.report`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- `sale`: modulul extinde direct raportul standard de vânzări din acest modul.

---

**Notă corecție ingestie:** `readme/DESCRIPTION.md` menționează schimbarea drept `(17.0.0.0.0)`, referință la o versiune veche a modulului; `__manifest__.py` indică versiunea reală `19.0.0.0.0` pentru codul curent, corectată mai sus.
