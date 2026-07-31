# Fișa Partenerului în Valută (localizat la `l10n_ro_partner_ledger_currency/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_ledger_currency`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_ledger_currency
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_ledger_currency`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde raportul Partner Ledger (Fișa Partenerului) din Odoo Enterprise cu coloane în valuta originală a tranzacțiilor, conform OMFP 1802/2014 art. 39-49 privind evidența operațiunilor în valute externe. Pe lângă coloanele standard în RON, afișează Debit, Credit și Sold în valuta efectivă (EUR, USD etc.), util companiilor care confirmă solduri cu parteneri externi și reconciliază balanța în RON cu sumele comunicate în valută.

#### 2. Funcționalități Cheie

- Coloane Debit Valută și Credit Valută cu suma debitată/creditată în valuta originală a tranzacției.
- Coloană Sold Valută cu sold progresiv acumulat în valuta originală (running balance).
- Tranzacțiile în RON au coloanele valutare goale, pentru vizibilitate clară a operațiunilor cu valută efectivă.
- Păstrarea coloanelor standard Debit (RON), Credit (RON), Sold (RON).
- Vizibil automat doar pentru companiile cu țara România.
- Moștenește toate funcționalitățile Partner Ledger: sold inițial, export PDF/XLSX, filtre pe parteneri/jurnale, drill-down, reconciliere.

#### 3. Dependențe

- `account_reports`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- Extinde handlerul raportului Partner Ledger din `account_reports` pentru a calcula și afișa coloanele valutare per tranzacție.

**Vizualizări / Date**

- `data/l10n_ro_partner_currency_report.xml`: Definește raportul extins cu coloanele în valută.
- `security/ir.model.access.csv`: Drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate.*

#### 5. Conexiuni

- `[[l10n_ro_journal_reports]]`
