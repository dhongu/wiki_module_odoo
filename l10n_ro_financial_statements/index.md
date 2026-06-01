# Romania - Situații Financiare Anuale ANAF (FR-31) (localizat la `l10n_ro_financial_statements/index.md`)

- **Nume Tehnic:** `l10n_ro_financial_statements`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_financial_statements
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_financial_statements`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Extinde modulul `l10n_ro_reports` (Enterprise) cu un buton de export XML ANAF direct în rapoartele standard Formular 10 (Bilanț) și Formular 20 (Cont de Profit și Pierdere). Generează XML-ul ANAF prin același mecanism ca exportul D300/SAF-T și validează că bilanțul este echilibrat înainte de export, integrându-se nativ în frameworkul Enterprise de rapoarte.

## 2. Funcționalități Cheie

- **Buton „Export XML ANAF"** în headerul rapoartelor „Cod 10 - Bilanț" și „Cod 20 - Cont de Profit și Pierdere".
- **Formularul 10 (Bilanț):** XML cu rândurile 01–51 extrase din raportul Enterprise prin pattern `| NN`.
- **Formularul 20 (CPP):** XML cu rândurile 01–68 extrase din raportul Enterprise.
- **Validare bilanț echilibrat:** blocare export dacă Total Activ (rd.04+11+12) ≠ Total Pasiv (rd.15+18+19+20+51), cu toleranță 1 RON.
- **Implementat ca `account.report.custom.handler`** — integrat nativ în frameworkul Enterprise de rapoarte.

## 3. Dependențe

- `l10n_ro_reports`
- `account`

## 4. Componente Cheie

### Modele

- `account.report.custom.handler` (handlere dedicate F10 și F20): extind rapoartele Enterprise cu butonul de export XML ANAF și validarea bilanțului echilibrat.

### Vizualizări / Date

- `data/l10n_ro_fs_report_setup.xml`: configurarea rapoartelor F10/F20 și legarea handlerelor de export.

### Acțiuni Automate / Acțiuni Server

- Acțiunea de export XML ANAF, declanșată din butonul din headerul rapoartelor F10/F20.

## 5. Conexiuni

- `[[l10n_ro_financial_notes]]`
- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_account_chart]]`
