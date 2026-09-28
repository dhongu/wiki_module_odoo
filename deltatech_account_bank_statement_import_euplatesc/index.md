# Euplatesc Settlement Bank Statements Import (localizat la `deltatech_account_bank_statement_import_euplatesc/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_euplatesc`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_euplatesc
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_euplatesc`
- **Ultima Ingestie:** `2026-09-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă direct în Odoo, ca extrase de cont, fișierele de decontare (settlement) Euplatesc.ro pentru comerțul electronic, eliminând procesarea manuală a fișierelor XLSX primite de la procesatorul de plăți cu cardul. Fiecare fișier de decontare devine automat un extras bancar cu linii detaliate pe tranzacție, gata de reconciliere cu comenzile web sau facturile aferente.

#### 2. Funcționalități Cheie

- **Import fișier original**: se încarcă exact fișierul de detaliere primit de la Euplatesc — se creează câte un extras pentru fiecare lot de decontare (foaie FPS).
- **Detectare prin semnătură pe SET de coloane**: fișierul este recunoscut dacă antetul conține coloanele obligatorii `MerchantID`, `InvoiceId`, `RRN`, `Suma`, `Moneda` — în orice ordine și în oricare dintre foile fișierului — nu mai printr-un prefix fix de patru coloane în ordine. Astfel poate fi importat din orice jurnal de tip bancă, alături de alte formate de extras, chiar dacă antetul e reordonat sau primește o coloană nouă.
- **Semnătură bazată doar pe coloane cu nume tehnice**: `Descriere` și `Nume client` sunt citite de parser, dar nu mai fac parte din semnătura de recunoaștere — anterior, fiind denumiri românești, un raport descărcat din interfața Euplatesc în engleză nu mai era recunoscut și cădea tăcut în asistentul generic de mapare a coloanelor.
- **O linie per plată cu cardul**: fiecare tranzacție devine o linie de extras cu referința comenzii web sau a facturii (InvoiceId), numele clientului și detaliile de decontare; rambursările (refund) sunt importate ca linii negative separate.
- **Comisioane configurabile**: comisioanele de procesare Euplatesc (Minim1RON + Diff1RON) pot fi importate ca o singură linie agregată per extras (implicit), ca o linie per tranzacție, sau pot fi omise.
- **Linie opțională de transfer bancar**: se poate adăuga automat o linie negativă cu suma netă transferată (configurabil per jurnal), astfel încât extrasul să se balanseze la zero, iar decontarea să poată fi reconciliată cu extrasul bancar real printr-un cont de transfer intern.
- **Identificare automată a partenerului**: numărul comenzii (`InvoiceId`) este căutat în `sale.order` (`client_order_ref` sau `name`), iar clientul găsit este setat direct pe liniile de plată și de refund; o potrivire ambiguă lasă linia neatribuită, pentru decizia operatorului.
- **Protecție la duplicate**: fiecare tranzacție este importată o singură dată (id unic de import per RRN); reimportarea aceluiași fișier este detectată.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

*Notă: conform priorității Readme, componentele tehnice nu au fost extrase din cod pentru această pagină; secțiunea de mai jos oferă doar un reper minim util pentru navigare tehnică.*

**Modele**

- `account.journal` (extindere): adaugă câmpurile de configurare `euplatesc_commission_mode` și `euplatesc_add_transfer_line`, plus logica de detecție/parsare a fișierelor de decontare Euplatesc. Detecția (`_read_euplatesc_file`) și parsarea (`_parse_euplatesc_file`) se bazează pe același set de coloane obligatorii (`EUPLATESC_REQUIRED_COLUMNS`), verificat prin helperul comun `_statement_sheet_matching_header()` din [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md), pentru ca cele două să nu diveargă. Identificarea partenerului folosește helperul comun `_statement_partner_from_order_ref()`.

**Vizualizări**

- `view_account_journal_form_euplatesc`: extinde formularul de jurnal contabil (`account.view_account_journal_form`) cu opțiunile de comision Euplatesc și de adăugare a liniei de transfer, vizibile doar pentru jurnalele de tip bancă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): furnizează helperele comune de detecție pe set de coloane (`_statement_sheet_matching_header`) și de identificare a partenerului după referința comenzii (`_statement_partner_from_order_ref`), folosite de acest modul.
- [deltatech_account_bank_statement_import_emag](../deltatech_account_bank_statement_import_emag/index.md): modul soră, din aceeași familie de import extrase pentru procesatori/marketplace-uri e-commerce, actualizat în aceeași schimbare la detecția pe set de coloane.
- [l10n_ro_account_bank_statement_import_xlsx](../l10n_ro_account_bank_statement_import_xlsx/index.md): modul înrudit funcțional pentru import extrase XLSX în context de localizare românească.
