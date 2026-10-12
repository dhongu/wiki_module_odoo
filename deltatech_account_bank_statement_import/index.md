# Bank Statements Import Extension (localizat la `deltatech_account_bank_statement_import/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import`
- **Versiune:** `19.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Acest modul extinde funcționalitatea de import al extraselor de cont bancar pentru a accepta fișiere XLSX, pe lângă formatele acceptate în mod standard. În plus, ajută la identificarea automată a partenerului asociat fiecărei tranzacții, reducând munca manuală de reconciliere și potrivire a încasărilor cu partenerii corecți. Este și baza comună a importurilor de fișiere de decontare (procesatori de carduri, curieri, marketplace-uri): recunoaște fișierul după antet (XLSX sau CSV), găsește clientul din comanda din magazin sau din plata online și construiește extrasul unei plăți către bancă, cu comisioanele de procesare, linia de plată către bancă, o singură monedă per fișier și protecție împotriva importării de două ori a acelorași tranzacții.

#### 2. Funcționalități Cheie

- Import al extraselor de cont bancar din fișiere XLSX.
- Detectare automată a partenerului după numele partenerului (caută un partener cu nume corespunzător).
- Detectare automată a partenerului după referința comenzii de vânzare (caută o comandă de vânzare care corespunde referinței plății și asociază partenerul comercial al acelei comenzi) — helper comun `_statement_partner_from_order_ref()`; dacă referința se potrivește cu mai multe comenzi, linia rămâne neatribuită și cere intervenția operatorului la reconciliere.
- Detectare a partenerului după plata online Odoo: `_statement_partner_from_payment_transaction()` caută tranzacția de plată după identificatorul procesatorului sau după referința plății și preia clientul ei.
- Recunoașterea fișierului de decontare după antet: `statement_header_key()` normalizează numele coloanelor (fără diacritice, literă mică, fără spații), iar `_statement_sheet_matching_header()` (XLSX, toate foile) și `_statement_csv_matching_header()` (CSV) verifică antetul ca **set** de coloane obligatorii, nu ca prefix ordonat — fișierele de la procesatori/curieri/marketplace nu poartă niciun marcaj al emitentului, iar un prefix ordonat ceda tăcut la prima coloană adăugată sau reordonată.
- Constructor comun de extras de decontare (`_settlement_statement_vals`, `_settlement_parse_result`): rânduri de plată cu sumă brută și comision, comisioane ca o linie per plată, o linie per tranzacție sau omise, linia netă de plată către bancă, o singură monedă per fișier. Preluat din importul EuPlatesc.ro și folosit și de importurile Stripe și PayPal.
- Un fișier de decontare recunoscut de un modul de procesator sare peste wizardul de mapare a coloanelor CSV/XLSX (`_settlement_file_is_recognized()`).
- Opțiuni pe jurnalul bancar, vizibile doar când e instalat un format de decontare (Stripe, PayPal): **Settlement Files: Fees** (o linie agregată per decontare / o linie per tranzacție / fără comisioane) și **Settlement Files: Add Payout Line** (adaugă linia negativă cu suma netă plătită, astfel încât extrasul să se echilibreze la zero; nu e necesară pentru fișierele care listează retragerile, ca PayPal).
- Utilitare de parsare comune: `parse_statement_amount()` și `parse_statement_date()`.

#### 3. Dependențe

- `account_bank_statement_import_csv`

#### 4. Componente Cheie

Documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice; sunt menționate doar elementele structurante.

**Modele**

- `account.journal` (extins, `models/account_bank_statement_import.py` și `models/settlement.py`): helperele de recunoaștere a antetului și de atribuire a partenerului, câmpurile `settlement_fee_mode`, `settlement_add_transfer_line`, `settlement_import_available` și constructorul extrasului de decontare.
- `base_import.import` (extins): detectarea partenerului după nume la importul XLSX.

**Vizualizări**

- `view_account_journal_form_settlement`: adaugă pe fila contului bancar al jurnalului opțiunile de decontare, vizibile doar când `settlement_import_available`.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): conectorul de decontare Euplatesc; folosește helperele de antet, atribuirea partenerului și constructorul comun de extras.
- [deltatech_account_bank_statement_import_emag](../deltatech_account_bank_statement_import_emag/index.md): conectorul de decontare eMAG; folosește helperele de antet și `_statement_partner_from_order_ref()`.
- `deltatech_account_bank_statement_import_stripe`: import de decontări Stripe, pe constructorul comun (opțiunile de comisioane și linie de plată).
- `deltatech_account_bank_statement_import_paypal`: import de decontări PayPal, pe constructorul comun.
