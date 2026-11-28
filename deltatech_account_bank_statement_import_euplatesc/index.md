# EuPlatesc.ro Settlements (localizat la `deltatech_account_bank_statement_import_euplatesc/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_euplatesc`
- **Versiune:** `20.0.1.2.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_account_bank_statement_import_euplatesc
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_euplatesc`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă fișierul de detaliere a decontărilor **EuPlatesc.ro** (platforma românească de plăți cu cardul, operată de EuroPayment Services S.R.L.) direct ca extras de cont bancar: o linie per plată cu cardul, legată de clientul comenzii, comisioanele de procesare și suma pe care EuPlatesc.ro o virează în bancă, fără nicio editare a fișierului. Modulul doar citește fișierul încărcat; nu se conectează la EuPlatesc.ro.

#### 2. Funcționalități Cheie

- **Fișierul așa cum vine**: se încarcă detalierea decontării (XLSX) exact cum a fost descărcată; fiecare foaie de decontare devine un extras separat, datat la ziua decontării.
- **Recunoaștere automată**: fișierul este identificat după coloanele tehnice (MerchantID, InvoiceId, RRN, Suma, Moneda), în orice ordine și pe orice foaie, deci și un raport descărcat din interfața în engleză se importă la fel, fără wizardul de mapare.
- **O linie per plată cu cardul**: referința comenzii (InvoiceId), numele clientului și descrierea; rambursările vin ca linii negative separate.
- **Clientul găsit după comandă**: InvoiceId este căutat în comenzile de vânzare (referința clientului sau numărul comenzii); dacă nu există exact o potrivire, linia rămâne pentru operator.
- **Comisioane la alegere**: comisioanele de procesare se importă ca o linie per extras (implicit), o linie per plată sau deloc (opțiunea **Euplatesc: Fees** pe jurnal).
- **Linie de transfer, o singură monedă, fără duplicate**: o linie negativă opțională cu suma netă virată echilibrează extrasul (**Euplatesc: Add Bank Transfer Line**); un fișier cu mai multe monede este refuzat (un jurnal per monedă); fiecare plată se importă o singură dată, reimportul fiind detectat.
- **Configurare**: jurnal de tip Bancă dedicat, cu cont propriu 5125 (sume în curs de decontare), **Bank Feeds = Import**. Linia de transfer se reconciliază cu plata EuPlatesc.ro din extrasul bancar real printr-un cont de viramente interne (581). Pașii detaliați sunt în fișa consultant.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

*Notă:* dependență externă Python: `openpyxl`. Extrasul unei decontări este construit de constructorul comun din *Bank Statements Import Extension* (comisioane, linie de transfer, verificarea monedei, ocolirea wizardului de mapare), partajat cu importurile Stripe și PayPal.

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, completat din `USAGE.md` și `CONFIGURE.md`. Componentele de mai jos reies din cod.

**Modele**

- `account.journal` (extins): câmpurile `euplatesc_commission_mode` (modul de import al comisioanelor) și `euplatesc_add_transfer_line` (linia de transfer bancar); recunoaște fișierul după coloanele obligatorii (`_read_euplatesc_file`, prin `_statement_sheet_matching_header`) și îl transformă în extrase (`_parse_euplatesc_file`), cu id unic de import per RRN.

**Vizualizări**

- `view_account_journal_form_euplatesc`: extinde formularul jurnalului cu opțiunile de comision și de linie de transfer, pentru jurnalele de tip Bancă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): oferă helperul comun de recunoaștere a fișierului și constructorul de extras.
- [deltatech_account_bank_statement_import_emag](../deltatech_account_bank_statement_import_emag/index.md): același tipar de import prin semnătură de antet, pentru decontările eMAG.
- [deltatech_account_bank_statement_import_gls](../deltatech_account_bank_statement_import_gls/index.md): același tipar, pentru borderourile de ramburs GLS.
- [deltatech_account_bank_statement_import_paypal](../deltatech_account_bank_statement_import_paypal/index.md): import de decontări prin același constructor comun.
- [l10n_ro_account_bank_statement_import_xlsx](../l10n_ro_account_bank_statement_import_xlsx/index.md): import generic de extrase XLSX, în context de localizare românească.
