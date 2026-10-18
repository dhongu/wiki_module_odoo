# Romania - Balanță analitică pe parteneri

- **Nume Tehnic:** `l10n_ro_partner_trial_balance`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_trial_balance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_trial_balance`
- **Ultima Ingestie:** `2026-10-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă **balanța analitică pe parteneri**: balanța de verificare românească, cu 4 sau 5 coloane, detaliată pe cont și pe partener, pentru conturile de terți (furnizori, clienți, avansuri, debitori și creditori diverși). Este documentul cerut periodic de bănci la analiza de credit și se adresează contabililor care îl predau băncilor sau auditorilor.

#### 2. Funcționalități Cheie

- **Două variante, în selectorul balanței de verificare** (Contabilitate → Raportare → Registre → Balanța de verificare, butonul **Raport:**): *Balanță analitică pe parteneri (4 coloane)* — sold inițial, rulaj, total sume, sold final — și *(5 coloane)*, care adaugă sumele precedente de la începutul anului.
- **Partenerul pe rând:** sub fiecare cont apare câte un rând pe partener, cu soldul inițial și soldul final pe o singură coloană (Debit sau Credit); codul fiscal e afișat lângă nume.
- **Sold desfășurat pe cont:** pe rândul contului, soldurile debitoare și cele creditoare ale partenerilor se adună separat, deci un furnizor plătit în avans nu compensează datoria față de ceilalți. Soldul net al contului = Sold final Debit − Sold final Credit; rulajele coincid cu balanța de verificare sintetică.
- **Conturi alese din filtrul standard „Cont”, fără nicio setare** (fără prefixe configurabile): intrările comerciale Creanțe / Datorii (401, 403, 404, 4111, 461, 4621, 4622, 4551) sunt bifate implicit, la fel și două intrări noi pentru conturile RO de terți pe care filtrul standard nu le poate selecta: **Avansuri (409, 419)** și **Alte conturi de terți** (405, 408, 413, 418, 4118, 451, 453, 455, 456). Conturile necomerciale rămân nebifate.
- **Salariile nu ajung la bancă:** la instalare (și din planul de conturi RO la companiile noi), conturile 421, 425 și 463 sunt marcate **necomerciale**, deci ies din filtrul implicit, atât în balanță, cât și în Partner Ledger și în rapoartele de scadențe. Pentru alte conturi de personal cu tipul Creanțe / Datorii, bifa se pune manual în Plan de conturi.
- **Avansurile și în Partner Ledger:** aceleași două intrări apar, nebifate implicit, în filtrul **Cont** din Fișa partenerului (Partner Ledger), astfel încât soldul unui partener să se poată reconcilia cu balanța pe parteneri.
- **Rândul „Fără partener":** liniile contabile fără partener (frecvent pe 408, 418, 461, 462) apar pe un rând separat, cu sumele debitoare și creditoare brute, fără compensare. Pe 401 și 4111 rândul ar trebui să lipsească.
- **Filtre și export standard:** filtrul pe parteneri, perioada, compania, exportul XLSX / PDF și drill-down-ul până la notele contabile vin din rapoartele Enterprise.

Fluxul pas-cu-pas, cu capturi de ecran, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md)

Indirect (prin `l10n_ro_reports_fix`): `account_reports` (framework Enterprise de rapoarte) și `l10n_ro_reports` (balanța de verificare românească cu 4 și 5 coloane).

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.trial.balance.5.column.report.handler` (abstract): handler al raportului cu 5 coloane, extinde handlerul balanței românești; desface liniile pe parteneri, calculează soldul net pe partener, soldul desfășurat pe cont, rândul „Fără partener" și adaugă codul fiscal.
- `l10n.ro.partner.trial.balance.4.column.report.handler` (abstract): varianta cu 4 coloane, moștenește handlerul cu 5 coloane.
- `account.report` (extins): câmpul `l10n_ro_filter_partner_accounts` (Optional / Enabled by Default) care adaugă în filtrul „Cont” intrările **Avansuri (409, 419)** și **Alte conturi de terți** și completează domeniul filtrului de tip de cont cu conturile corespunzătoare (după prefix, pe companiile raportului).
- `account.chart.template` (extins): pentru planul `ro` marchează `non_trade` conturile 421, 4211, 4212, 425 și 463.

**Vizualizări**

- Rapoartele `l10n_ro_partner_trial_balance_4_column` / `_5_column` (`account.report`, în `data/partner_trial_balance.xml`), sub raportul rădăcină `account_reports.trial_balance_report`, cu filtru pe parteneri și intrările RO ale filtrului „Cont” bifate implicit.
- `account_reports.partner_ledger_report` (extins prin date): activează opțional aceleași intrări în filtrul „Cont” din Partner Ledger.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): la instalare, bifează „Necomercial” pe conturile 421, 425, 463 (tip Creanțe / Datorii) ale companiilor cu planul RO deja încărcat. Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md): oferă corecțiile de sold din balanța românească, pe care balanța pe parteneri le folosește.
- `l10n_ro_reports`: balanța de verificare românească cu 4 și 5 coloane, al cărei handler este extins.
- `account_reports`: Partner Ledger (`account.report` extins) primește intrările Avansuri și Alte conturi de terți.
