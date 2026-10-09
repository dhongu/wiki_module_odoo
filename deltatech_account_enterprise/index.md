# Deltatech Account Enterprise (localizat la `deltatech_account_enterprise/index.md`)

- **Nume Tehnic:** `deltatech_account_enterprise`
- **Versiune:** `19.0.0.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_enterprise
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_enterprise`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde rapoartele native de urmărire a clienților din Odoo Enterprise, astfel încât cifrele să reflecte ce mai are de încasat firma la data aleasă în raport. Facturile și notele de credit parțial decontate nu mai apar cu suma inițială, ci cu trei valori separate: **Valoare inițială**, **Stins / aplicat** și **Rest**. Pozițiile sunt grupate în **Restante** și **Scadente**, cu subtotaluri, iar persoanele responsabile cu încasările văd rapid ce sume sunt restante și ce sume urmează să devină scadente. Modulul păstrează rapoartele, exporturile și fereastra de trimitere native și nu modifică nicio înregistrare contabilă și nu alocă plăți automat.

#### 2. Funcționalități Cheie

- **Linii de urmărire grupate**: pozițiile deschise sunt grupate în **Restante (Overdue)** și **Scadente (Due)**, la data raportului.
- **Sold rămas semnat la data raportului**: Valoare inițială − Stins / aplicat = Rest. Notele de credit și plățile nealocate își păstrează semnul; un net zero nu reconciliază documentele deschise. Facturile complet decontate și plățile nu apar în urmărire, dar rămân vizibile în extrasul de client.
- **Subtotaluri pe status**: Restante / Scadente au subtotaluri proprii pentru Valoare inițială, Stins / aplicat și Rest, iar totalul acoperă toate pozițiile eligibile, nu doar pagina încărcată. Previzualizarea și tipărirea exclud la fel pozițiile marcate **Fără urmărire**; PDF și XLSX au aceleași cifre ca ecranul.
- **Butoane pe fișa partenerului**: **Urmărire** (soldul semnat al pozițiilor eligibile, nu doar partea restantă), **Fișa partener** (extras de client nativ, istoric, fără total pe buton) și **Creanțe pe scadențe** (raportul nativ de vechime, inclusiv intervalul nescadent și pozițiile excluse din urmărire). Sunt vizibile pentru grupurile Facturare și Contabilitate (doar citire); se folosește partenerul comercial și compania curentă, iar regulile de acces rămân active.
- **Poziții deschise actuale**: link în tabul **Facturare**, secțiunea de urmăriri facturi, care deschide lista nativă de elemente de jurnal cu rest nenul, coloana **Rest (actual)** cu total, iar Debit / Credit / Sold ca coloane opționale. Este o listă operațională la zi; o reconcilire cu dată viitoare o poate face să difere de un raport la o dată anterioară.
- **Flux de email nativ**: butoanele **Trimite** și wizardul `account.report.send` rămân cele native; modulul nu trimite mesaje singur și nu schimbă automatizarea memento-urilor.
- **Memento înainte de scadență**: opțiune în **Setări / Facturare / Facturi clienți**, debifată implicit. Bifată, creează pentru compania curentă un nivel de urmărire **Before due date**, la **-1 zi**, **automat**, cu **email** și **SMS** (SMS-ul listează fiecare factură neachitată ajunsă la nivel, cu număr, scadență și sumă), fără atașarea facturilor. Debifată, nivelul se șterge. Poate fi modificat din **Contabilitate / Configurare / Niveluri de urmărire**; SMS-ul consumă credite IAP și folosește telefonul adresei de facturare.

Fluxul detaliat pas cu pas, cu capturi, este în [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `account_accountant`
- `account_reports`
- `account_followup`

#### 4. Componente Cheie

Descrierea din `readme/DESCRIPTION.md` e la nivel funcțional; extensiile tehnice de mai jos sunt verificate în cod.

**Modele**

- `account.followup.report.handler` (extins): filtrează pozițiile cu `no_followup`, reordonează și redenumește coloanele (Original Amount, Remaining, Remaining in Currency), adaugă coloana Settled / Applied, calculează restul la data raportului din reconcilierile parțiale datate, construiește liniile grupate Restante / Scadente cu subtotaluri pe toate paginile și face `flush_model` înainte de interogările directe.
- `res.partner` (extins): câmpurile calculate `followup_open_amount` (Follow-up Balance, sold semnat din raportul de urmărire) și `aged_open_amount` (Open Receivables, din Aged Receivable), pe partenerul comercial și compania curentă; acțiunile `open_partner_ledger`, `open_customer_statement`, `open_follow_up_report`, `open_aged_receivable` (resetează scopul la compania activă și contactele partenerului comercial) și `action_open_partner_followup_journal_items` (Poziții deschise actuale: linii postate de creanță, cu rest nenul, până la data de azi).
- `res.partner` (memento): `_get_followup_before_due_invoices` selectează facturile de client neachitate ajunse la primul nivel, iar `_get_followup_before_due_text` le formatează pentru SMS.
- `res.company` (extins): `_get_followup_before_due_level` și `_create_followup_before_due_level` (nivel -1 zi, automat, email + SMS, cu traduceri pe limbile instalate); nu se creează nimic dacă există deja un nivel cu zile negative.
- `res.config.settings` (extins): câmpul `followup_before_due`; la salvare creează sau șterge nivelul.

**Vizualizări**

- `res_partner_view_form`: butoanele statistice „Customer Statement” și „Receivables by Maturity” (cu `aged_open_amount`) în `button_box`.
- `res_partner_followup_button`: înlocuiește totalul butonului „Follow-up” din `account_followup` cu `followup_open_amount`.
- `res_partner_open_items_link`: redenumește linkul din tabul Facturare în „Current Open Items”.
- `view_open_move_line_list`: listă derivată din `account.view_move_line_tree_grouped_partner`, cu „Remaining (Current)” vizibil și însumat; Debit, Credit și Balance opționale, ascunse implicit.
- `res_config_settings_view_form`: opțiunea „Reminder Before Due Date” și butonul „Follow-up Levels”.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server. Date: coloana `followup_report_applied` (Settled / Applied) pe raportul `account_reports.followup_report`; șabloanele `email_template_followup_before_due` și `sms_template_followup_before_due` (`noupdate`).

#### 5. Conexiuni

Nu au fost identificate conexiuni verificate către alte module documentate în wiki.
