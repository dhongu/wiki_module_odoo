# MRP Validation Date (localizat la `deltatech_mrp_validation_date/index.md`)

- **Nume Tehnic:** `deltatech_mrp_validation_date`
- **Versiune:** `20.0.0.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp_validation_date
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_validation_date`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul înregistrează data la care o comandă de fabricație este validată (marcată ca „Efectuată"), oferind managerilor de producție un jurnal de audit al momentului finalizării comenzilor.

#### 2. Funcționalități Cheie

- Adaugă câmpul **Validation Date** pe formularul comenzii de fabricație, în antet lângă responsabil, completat automat cu data curentă când operatorul apasă **Mark as Done**.
- Câmpul este read-only: este setat de sistem și nu poate fi modificat manual.
- Funcționează alături de câmpurile standard de planificare MRP (dată programată, dată finalizare) pentru o cronologie completă a producției.
- Bug cunoscut (MRPDATE-001, P2, deschis): data se setează necondiționat după apelul părinte, deci și când `Mark as Done` deschide un asistent de pre-finalizare care este apoi anulat; `date.today` urmează data serverului, nu contextul utilizatorului.

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): adaugă câmpul `validation_date` (Date, read-only) și suprascrie `button_mark_done()` pentru a seta data curentă.

**Vizualizări**

- `view_mrp_production_form_inherit`: extinde formularul comenzii de fabricație (`mrp.mrp_production_form_view`), afișând `validation_date` înaintea câmpului responsabil (`user_id`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `mrp`: modulul extinde direct formularul și modelul comenzii de fabricație din Manufacturing.
