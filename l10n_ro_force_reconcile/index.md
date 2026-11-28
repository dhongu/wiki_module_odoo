# Romania - Reconciliere forțată între conturi diferite (localizat la `l10n_ro_force_reconcile/index.md`)

- **Nume Tehnic:** `l10n_ro_force_reconcile`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_force_reconcile
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_force_reconcile`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Wizard pentru reconcilierea a două înregistrări contabile din conturi diferite. Odoo standard permite reconcilierea doar între linii din același cont; modulul elimină această restricție printr-un document intermediar de compensare, cu câte o linie pe fiecare cont, și acoperă cazurile tipice din contabilitatea românească (avans furnizor ↔ factură, avans client ↔ factură, compensare client-furnizor).

#### 2. Funcționalități Cheie

- Cazuri de utilizare: avans furnizor ↔ factură furnizor (409 ↔ 401), avans client ↔ factură client (419 ↔ 411), compensare client-furnizor pe același partener (411 ↔ 401), decontare avans angajat ↔ furnizor (542 ↔ 401).
- Wizard lansat din lista de elemente de jurnal, prin acțiunea „Reconciliere forțată (conturi diferite)", disponibilă pentru grupul Contabilitate / Manager, la selectarea a exact 2 linii postate, nereconciliate complet, din aceeași companie, pe conturi care permit reconcilierea.
- Afișează conturile, soldurile reziduale și suma propusă de compensare (minimul celor două reziduuri); suma, jurnalul (implicit primul jurnal de tip Diverse), data și eticheta (COMPENSARE) pot fi modificate.
- Creează și postează automat o notă contabilă de compensare cu două linii (câte una pe fiecare cont) și reconciliază liniile originale cu liniile corespondente din notă.
- Suportă reconcilierea parțială (suma compensată mai mică decât rezidualul liniei). Fluxul detaliat pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.force.reconcile` (wizard, `wizard/account_force_reconcile.py`): preia cele două linii selectate, calculează reziduurile și suma compensată, creează și postează nota de compensare și reconciliază liniile.

**Vizualizări**

- `wizard/account_force_reconcile_views.xml`: formularul wizardului de reconciliere forțată.

**Acțiuni Automate / Acțiuni Server**

- `action_server_force_reconcile` (`data/server_actions.xml`): acțiune server „Reconciliere forțată" disponibilă pe elementele de jurnal selectate, care deschide wizardul (restricționată la grupul Contabilitate / Manager). Nu sunt definite `ir.cron`.

#### 5. Conexiuni

- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): reevaluarea valutară a soldurilor, folosită în același context de închidere a conturilor de terți.
- [l10n_ro_expense_currency](../l10n_ro_expense_currency/index.md): cheltuieli în valută, ale căror avansuri se pot compensa cu acest wizard.
