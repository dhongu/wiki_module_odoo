# Romania - Balanță analitică pe parteneri

- **Nume Tehnic:** `l10n_ro_partner_trial_balance`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_partner_trial_balance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_trial_balance`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Balanța de verificare românească cu 4 sau 5 coloane, detaliată pe cont și pe partener, pentru conturile de terți (furnizori, clienți, avansuri, debitori și creditori diverși). Este documentul cerut periodic de bănci la analiza de credit.

#### 2. Funcționalități Cheie

- Două variante în selectorul balanței de verificare (**Contabilitate → Raportare → Registre → Balanța de verificare**): **Balanță analitică pe parteneri (4 coloane)** și **(5 coloane)**, care adaugă sumele precedente de la începutul anului.
- Sub fiecare cont, câte un rând pe partener, cu codul fiscal lângă nume; soldurile inițial și final apar pe o singură coloană (Debit sau Credit).
- Sold desfășurat pe cont: soldurile debitoare și cele creditoare ale partenerilor se adună separat, deci un furnizor plătit în avans nu compensează datoria față de ceilalți. Reconcilierea cu balanța sintetică: rulajele coincid, iar soldul net = Sold final Debit − Sold final Credit.
- Filtrul standard **Cont**, cu două intrări noi: **Avansuri (409, 419)** și **Alte conturi de terți** (405, 408, 413, 418, 451–456); fără setări.
- La instalare, conturile 421, 425 și 463 se marchează **necomerciale** și ies din balanță, Partner Ledger și rapoartele de scadențe.
- Aceleași intrări apar, nebifate implicit, în filtrul **Cont** din Partner Ledger, pentru reconcilierea soldului partenerului cu balanța.
- Rândul „Fără partener” pentru liniile fără partener, cu solduri nete pe o singură coloană (ex. 462 cu 20 D / 70 C apare 0 D / 50 C).
- Filtrul pe parteneri, perioada, compania, exportul XLSX / PDF și drill-down-ul vin din rapoartele Enterprise.

#### 3. Dependențe

- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md)


#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.trial.balance.5.column.report.handler` și `l10n.ro.partner.trial.balance.4.column.report.handler`: handlerele de raport, extind balanța românească cu 5, respectiv 4 coloane.
- `account.report` (extins): filtrul de conturi de terți (`l10n_ro_filter_partner_accounts`).
- `account.chart.template` (extins): marchează conturile 421, 425, 463 ca necomerciale la încărcarea planului pe companiile noi.

**Vizualizări**

- Rapoartele `l10n_ro_partner_trial_balance_4_column` și 5 coloane (`account.report`, sub `account_reports.trial_balance_report`).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: bifează **Necomercial** pe conturile 421, 425, 463 din companiile cu planul RO. Nu are cron-uri.

#### 5. Conexiuni

- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md): corecțiile de sold din balanța românească, folosite de această balanță.
- `l10n_ro_reports`, `account_reports`: rapoartele Enterprise pe care se sprijină.
