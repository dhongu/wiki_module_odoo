# Romania - Reconciliere forțată conturi diferite (localizat la `l10n_ro_force_reconcile/index.md`)

- **Nume Tehnic:** `l10n_ro_force_reconcile`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_force_reconcile
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_force_reconcile`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Wizard pentru reconcilierea a două înregistrări contabile din conturi diferite, ocolind restricția Odoo standard care permite reconcilierea doar între linii din același cont. Modulul creează un document intermediar de compensare cu câte o linie pe fiecare cont, util pentru cazuri românești precum avans furnizor ↔ factură (409 ↔ 401), avans client ↔ factură (419 ↔ 411) sau compensarea client-furnizor.

## 2. Funcționalități Cheie

- **Reconciliere între conturi diferite** prin wizard, pentru cazuri precum 409↔401, 419↔411, 411↔401 (compensare), 542↔401 (decont avans angajat).
- **Acțiune „Reconciliere forțată"** disponibilă din meniul de acțiuni la selectarea a exact 2 înregistrări contabile (doar pentru `group_account_manager`).
- **Afișarea conturilor, soldurilor reziduale și a sumei propuse** de compensare în wizard.
- **Generarea automată a notei contabile de compensare** cu două linii, postarea ei și reconcilierea liniilor originale cu liniile corespondente.

## 3. Dependențe

- `account`

## 4. Componente Cheie

### Modele

- `account.force.reconcile` (wizard): gestionează selecția celor două înregistrări, afișează soldurile și creează nota de compensare cu reconcilierea ulterioară.

### Vizualizări / Date

- `wizard/account_force_reconcile_views.xml`: interfața wizardului de reconciliere forțată.
- `data/server_actions.xml`: acțiunea „Reconciliere forțată" din meniul de acțiuni.

### Acțiuni Automate / Acțiuni Server

- Acțiune server „Reconciliere forțată": apare pe înregistrările contabile selectate și deschide wizardul (restricționată la `group_account_manager`).

## 5. Conexiuni

- `[[l10n_ro_currency_revaluation]]`
- `[[l10n_ro_expense_currency]]`
