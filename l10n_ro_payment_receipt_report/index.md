# Romania - Payment Receipt Report (localizat la `l10n_ro_payment_receipt_report/index.md`)

- **Nume Tehnic:** `l10n_ro_payment_receipt_report`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_payment_receipt_report
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_payment_receipt_report`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă rapoartele de casă cerute în practica românească: chitanța și dispozițiile de plată și de încasare, tipărite direct din plăți și din liniile de extras.

#### 2. Funcționalități Cheie

- Raportul „Chitanță” tipărit din plata clientului.
- Raportul „Dispoziție de plată / încasare” tipărit din operațiunile de extras (liniile extrasului de cont).
- Suma în litere, generată cu biblioteca `num2words`.
- Format de hârtie dedicat.

#### 3. Dependențe

- [l10n_ro_payment_to_statement](../l10n_ro_payment_to_statement/index.md)

Dependență externă Python: `num2words>=0.5.8`.

#### 4. Componente Cheie

**Modele**

- `account.bank.statement.line`: extins pentru datele necesare raportului.

**Vizualizări**

- `l10n_ro_action_report_payment_receipt`: acțiunea de raport pentru chitanță.
- `action_report_bank_statement_line_payment`: acțiunea de raport pentru dispoziție.
- `report_payment_receipt_document`, `report_bank_statement_line_payment_document`: șabloanele QWeb.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_payment_to_statement](../l10n_ro_payment_to_statement/index.md): furnizează legătura plată - linie de extras pe care se bazează rapoartele.
