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
- **Doar conturile de terți:** conturile se aleg prin prefixe configurabile pe companie (Contabilitate → Configurare → Setări → Balanță analitică pe parteneri → Conturi detaliate pe partener). Implicit: 401, 403, 404, 405, 408, 409, 411, 413, 418, 419, 451, 453, 455, 456, 461, 462. Un prefix include toate conturile care încep cu el; tipul contului nu contează, deci conturile de salarii și taxe nu intră decât dacă sunt adăugate explicit (se recomandă evitarea conturilor de personal).
- **Rândul „Fără partener":** liniile contabile fără partener (frecvent pe 408, 418, 461, 462) apar pe un rând separat, cu sumele debitoare și creditoare brute, fără compensare. Pe 401 și 4111 rândul ar trebui să lipsească.
- **Filtre și export:** filtrul pe parteneri, perioada, compania, exportul XLSX / PDF și drill-down-ul până la notele contabile vin din rapoartele Enterprise.
- Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md)

Indirect (prin `l10n_ro_reports_fix`): `account_reports` (framework Enterprise de rapoarte) și `l10n_ro_reports` (balanța de verificare românească cu 4 și 5 coloane).

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.trial.balance.5.column.report.handler` (abstract): handler al raportului cu 5 coloane, extinde handlerul balanței românești; limitează conturile la prefixele companiei, desface liniile pe parteneri, calculează soldul net pe partener, soldul desfășurat pe cont, rândul „Fără partener" și adaugă codul fiscal.
- `l10n.ro.partner.trial.balance.4.column.report.handler` (abstract): varianta cu 4 coloane, moștenește handlerul cu 5 coloane.
- `res.company` (extins): câmpul `l10n_ro_partner_tb_account_prefixes` (prefixe de cont separate prin virgulă).
- `res.config.settings` (extins): câmp related către prefixele de pe companie.

**Vizualizări**

- `res_config_settings_view_form`: bloc „Balanță analitică pe parteneri" în Setări contabilitate, cu lista conturilor detaliate pe partener.
- Rapoartele `l10n_ro_partner_trial_balance_4_column` / `_5_column` (`account.report`, în `data/partner_trial_balance.xml`), sub raportul rădăcină `account_reports.trial_balance_report`, cu filtru pe parteneri.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_reports_fix](../l10n_ro_reports_fix/index.md): oferă corecțiile de sold din balanța românească, pe care balanța pe parteneri le folosește.
- `l10n_ro_reports`: balanța de verificare românească cu 4 și 5 coloane, al cărei handler este extins.
