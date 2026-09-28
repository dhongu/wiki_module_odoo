# Bank Statements Import Extension (localizat la `deltatech_account_bank_statement_import/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import`
- **Ultima Ingestie:** `2026-09-19`

#### 1. Sumar

Acest modul extinde funcționalitatea de import al extraselor de cont bancar pentru a accepta fișiere XLSX, pe lângă formatele acceptate în mod standard. În plus, ajută la identificarea automată a partenerului asociat fiecărei tranzacții, reducând munca manuală de reconciliere și potrivire a încasărilor cu partenerii corecți. De la versiunea 19.0.1.2.0 pune la dispoziție și un mecanism comun de recunoaștere a fișierelor de decontare (procesatori de carduri, curieri, marketplace-uri), folosit de conectoarele specializate ale suitei.

#### 2. Funcționalități Cheie

- Import al extraselor de cont bancar din fișiere XLSX.
- Detectare automată a partenerului după numele partenerului (caută un partener cu nume corespunzător).
- Detectare automată a partenerului după referința comenzii de vânzare (caută o comandă de vânzare care corespunde referinței plății și asociază partenerul comercial al acelei comenzi) — helper comun `_statement_partner_from_order_ref()`, folosit de conectoarele de decontare (ex. eMAG, Euplatesc); dacă referința se potrivește cu mai multe comenzi, linia rămâne neatribuită și cere intervenția operatorului la reconciliere.
- Helper comun `statement_header_key()`: normalizează un nume de coloană din antetul unui fișier (fără diacritice, literă mică, fără spații), astfel încât variații de scriere ale aceluiași antet să fie recunoscute ca identice.
- Helper comun `account.journal._statement_sheet_matching_header(raw_file, required_columns)`: identifică fișierul XLSX de decontare potrivit după antetul lui, verificat ca **set** de coloane obligatorii (nu ca prefix ordonat) și căutat în toate foile fișierului — necesar pentru că aceste fișiere de la procesatori/curieri/marketplace nu poartă niciun marcaj al emitentului, iar un prefix ordonat ceda tăcut la prima coloană adăugată sau reordonată de furnizor.

#### 3. Dependențe

- `account_bank_statement_import_csv`

#### 4. Componente Cheie

Această secțiune nu este detaliată: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni automate). Sunt menționate mai sus, la Funcționalități Cheie, cele două helpere noi introduse în `models/account_bank_statement_import.py` (`statement_header_key()` și `account.journal._statement_sheet_matching_header()`), fiind funcționalitate structurantă pentru restul suitei de conectoare.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): conectorul de decontare Euplatesc folosește `statement_header_key()` și `_statement_sheet_matching_header()` pentru a recunoaște fișierul de decontare, plus `_statement_partner_from_order_ref()` pentru atribuirea partenerului.
- [deltatech_account_bank_statement_import_emag](../deltatech_account_bank_statement_import_emag/index.md): conectorul de decontare eMAG folosește aceleași două helpere noi (`statement_header_key()`, `_statement_sheet_matching_header()`) și `_statement_partner_from_order_ref()`.
