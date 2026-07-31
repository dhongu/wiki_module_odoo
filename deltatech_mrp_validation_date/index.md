# MRP Validation Date (localizat la `deltatech_mrp_validation_date/index.md`)

- **Nume Tehnic:** `deltatech_mrp_validation_date`
- **Versiune:** `19.0.0.0.1`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_validation_date](https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_validation_date)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_validation_date`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul înregistrează data exactă la care o comandă de fabricație este validată (marcată ca „Efectuată"), oferind managerilor de producție un jurnal de audit sigur pentru momentul finalizării comenzilor.

#### 2. Funcționalități Cheie

- Adaugă un câmp **Dată Validare** pe formularul comenzii de fabricație, completat automat când operatorul apasă **Marchează ca Efectuată**.
- Câmpul este needitabil (read-only) — este setat de sistem și nu poate fi modificat manual, garantând integritatea datelor.
- Funcționează alături de câmpurile standard de planificare MRP (dată programată, dată finalizare) pentru a oferi o cronologie completă a producției.

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.production` (extins): adaugă câmpul `validation_date` (Date, needitabil) și suprascrie `button_mark_done()` pentru a seta automat data curentă la validarea comenzii.

**Vizualizări**

- `view_mrp_production_form_inherit`: extinde formularul standard al comenzii de fabricație (`mrp.mrp_production_form_view`), afișând câmpul `validation_date` înaintea câmpului responsabil (`user_id`).

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- `mrp`: modulul extinde direct formularul și modelul comenzii de fabricație din Manufacturing.
