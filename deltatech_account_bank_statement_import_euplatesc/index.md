# Euplatesc Settlement Bank Statements Import (localizat la `deltatech_account_bank_statement_import_euplatesc/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_euplatesc`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_euplatesc
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_euplatesc`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă direct în Odoo, ca extrase de cont, fișierele de decontare (settlement) Euplatesc.ro pentru comerțul electronic, eliminând procesarea manuală a fișierelor XLSX primite de la procesatorul de plăți cu cardul. Fiecare fișier de decontare devine automat un extras bancar cu linii detaliate pe tranzacție, gata de reconciliere cu comenzile web sau facturile aferente.

#### 2. Funcționalități Cheie

- **Import fișier original**: se încarcă exact fișierul de detaliere primit de la Euplatesc — se creează câte un extras pentru fiecare lot de decontare (foaia FPS).
- **Detectare prin semnătură**: fișierul este recunoscut după antetul specific de coloane Euplatesc (MerchantID / InvoiceId / ... / RRN), astfel poate fi importat din orice jurnal de tip bancă, alături de alte formate de extras.
- **O linie per plată cu cardul**: fiecare tranzacție devine o linie de extras cu referința comenzii web sau a facturii (InvoiceId), numele clientului și detaliile de decontare; rambursările (refund) sunt importate ca linii negative separate.
- **Comisioane configurabile**: comisioanele de procesare Euplatesc (Minim1RON + Diff1RON) pot fi importate ca o singură linie agregată per extras (implicit), ca o linie per tranzacție, sau pot fi omise.
- **Linie opțională de transfer bancar**: se poate adăuga automat o linie negativă cu suma netă transferată (configurabil per jurnal), astfel încât extrasul să se balanseze la zero, iar decontarea să poată fi reconciliată cu extrasul bancar real printr-un cont de transfer intern.
- **Protecție la duplicate**: fiecare tranzacție este importată o singură dată (id unic de import per RRN); reimportarea aceluiași fișier este detectată.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

*Notă: conform priorității Readme, componentele tehnice nu au fost extrase din cod pentru această pagină; secțiunea de mai jos oferă doar un reper minim util pentru navigare tehnică.*

**Modele**

- `account.journal` (extindere): adaugă câmpurile de configurare `euplatesc_commission_mode` și `euplatesc_add_transfer_line`, plus logica de parsare/import a fișierelor de decontare Euplatesc (detecție semnătură, generare linii de extras, deduplicare pe RRN).

**Vizualizări**

- `view_account_journal_form_euplatesc`: extinde formularul de jurnal contabil (`account.view_account_journal_form`) cu opțiunile de comision Euplatesc și de adăugare a liniei de transfer, vizibile doar pentru jurnalele de tip bancă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): face parte din aceeași familie de module de import extrase bancare pentru procesatori de plăți e-commerce.
- [l10n_ro_account_bank_statement_import_xlsx](../l10n_ro_account_bank_statement_import_xlsx/index.md): modul înrudit funcțional pentru import extrase XLSX în context de localizare românească.
