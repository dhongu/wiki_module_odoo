# Creanțe și Datorii Extinse România (FR-29) (localizat la `l10n_ro_receivables_enhanced/index.md`)

- **Nume Tehnic:** `l10n_ro_receivables_enhanced`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_receivables_enhanced
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_receivables_enhanced`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul extinde gestionarea creanțelor și datoriilor pentru localizarea românească, oferind instrumente pentru compensarea soldurilor client-furnizor și pentru calculul penalităților de întârziere. Compensarea se realizează între un partener care este simultan client și furnizor, cu generarea unui proces-verbal de compensare, iar penalitățile sunt calculate conform Legii 72/2013 privind combaterea întârzierii la plată.

## 2. Funcționalități Cheie

- **Compensare client-furnizor:** Stabilește soldurile reciproce dintre un partener care este în același timp client și furnizor și generează compensarea valorică.
- **Proces-verbal de compensare (PV):** Tipărește un raport PDF cu procesul-verbal de compensare pentru documentarea operațiunii.
- **Penalități de întârziere (Legea 72/2013):** Wizard pentru calculul automat al penalităților pe facturile restante, cu linii detaliate per document.
- **Extensii pe partener:** Adaugă informații și acțiuni relevante de reconciliere creanțe/datorii pe fișa partenerului.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `l10n.ro.partner.compensation`: Gestionează operațiunea de compensare a soldurilor reciproce client-furnizor.
- `l10n.ro.penalty.wizard` / `l10n.ro.penalty.wizard.line`: Wizard pentru calculul penalităților de întârziere conform Legii 72/2013.
- `res.partner`: Extins cu informații și acțiuni de reconciliere creanțe/datorii.

### Vizualizări / Date

- `views/l10n_ro_compensation_views.xml`: Interfața pentru gestionarea compensărilor.
- `views/res_partner_views.xml`: Extinderi pe formularul partenerului.
- `wizard/l10n_ro_penalty_wizard_views.xml`: Vizualizarea wizardului de penalități.
- `report/report_compensation.xml`: Șablonul PDF pentru procesul-verbal de compensare.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate acțiuni automate (`ir.cron`) în `__manifest__.py`.*

## 5. Conexiuni

- [l10n_ro_partner_ledger_currency](../l10n_ro_partner_ledger_currency/index.md): fișa partenerului în valută, complementară urmăririi creanțelor.
- `account`: liniile contabile (creanțe 411 / datorii 401) și reconcilierea.
