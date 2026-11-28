# Bank Statement Import Extension (localizat la `deltatech_account_bank_statement_import/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import`
- **Versiune:** `20.0.1.3.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_account_bank_statement_import
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul extinde importul extraselor bancare cu fișiere XLSX și recunoaște automat partenerul tranzacției. Este și baza comună a importurilor de fișiere de decontare ale procesatorilor de plăți (EuPlatesc.ro, Stripe, PayPal): recunoaște formatul după antetul coloanelor, găsește clientul și construiește extrasul unei plăți către bancă, cu comisioanele de procesare.

#### 2. Funcționalități Cheie

- Import de extrase bancare din fișiere XLSX (și recunoaștere a fișierelor CSV de decontare după antet).
- Detectarea automată a partenerului după numele partenerului sau după referința comenzii de vânzare (se asociază partenerul comercial al comenzii).
- Pentru fișierele de decontare: clientul se găsește din comanda din magazin sau din plata online.
- Comisioanele de procesare pot fi agregate (o linie per decontare), pe tranzacție sau omise, iar linia plății către bancă se poate adăuga, astfel încât extrasul să se echilibreze.
- O singură monedă per fișier și protecție împotriva importării repetate a acelorași tranzacții.
- Opțiunile de comision și de plată apar pe jurnalul bancar după instalarea unui format de decontare.

#### 3. Dependențe

- `account_bank_statement_import_csv`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): potrivirea după antet și detectarea partenerului (`_statement_sheet_matching_header`, `_statement_partner_from_order_ref`, `_statement_partner_from_payment_transaction`), recunoașterea fișierelor de decontare, construirea extrasului (`_settlement_statement_vals`) și opțiunile `settlement_fee_mode` și `settlement_add_transfer_line`.
- `base_import.import` (extins): parsarea datelor importate (`_parse_import_data`).

**Vizualizări**

- `views/account_journal_views.xml`: opțiunile de decontare (comisioane, linia plății) pe formularul jurnalului.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): format de decontare EuPlatesc.ro construit peste acest modul.
- [deltatech_account_bank_statement_import_stripe](../deltatech_account_bank_statement_import_stripe/index.md): format de decontare Stripe.
- [deltatech_account_bank_statement_import_paypal](../deltatech_account_bank_statement_import_paypal/index.md): format de decontare PayPal.
