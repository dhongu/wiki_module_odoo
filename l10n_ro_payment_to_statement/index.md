# Romania - Payment to Statement (localizat la `l10n_ro_payment_to_statement/index.md`)

- **Nume Tehnic:** `l10n_ro_payment_to_statement`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_payment_to_statement
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_payment_to_statement`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul leagă plățile clienților și furnizorilor de extrasele de cont și de registrul de casă, generând automat linia de extras pentru fiecare plată validată. În plus, permite folosirea secvențelor proprii pe jurnale, conform cerințelor contabilității românești.

#### 2. Funcționalități Cheie

- Adăugarea plăților în extrasele de cont: din meniul de plăți sau din „Înregistrează plata” de pe factură, după validare se creează linia de extras pe extrasul selectat.
- Secvențe atașate jurnalului, în locul numerotării standard Odoo:
  - secvență de jurnal (pentru jurnalele de vânzări, factura; pentru casă/bancă, celelalte înregistrări);
  - secvență de extras (casă/bancă);
  - secvență de încasare de la client (doar casă);
  - secvențe de intrare și ieșire de numerar, folosite la restituirile furnizor, respectiv client (doar casă).
- Opțiune de extras automat pe jurnal și câmpuri noi pe formularul jurnalului și al plății.
- Panou jurnal (dashboard) adaptat.

#### 3. Dependențe

- `account`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `account.journal`: secvențele românești și opțiunea `l10n_ro_auto_statement`.
- `account.payment`: legătura către extras (`l10n_ro_statement_id`) și linia de extras.
- `account.bank.statement` / `account.bank.statement.line`: creare linii din plăți; indicator `is_l10n_ro_payment_disposal`.
- `account.move`: numerotare după secvențele jurnalului.

**Vizualizări**

- `view_account_journal_form`: configurarea secvențelor.
- `view_account_payment_form`: extras pe plată.
- `account_journal_dashboard_kanban_view`: panoul jurnalelor.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_payment_receipt_report](../l10n_ro_payment_receipt_report/index.md): tipărește chitanțe și dispoziții de plată/încasare pe baza acestui modul.
