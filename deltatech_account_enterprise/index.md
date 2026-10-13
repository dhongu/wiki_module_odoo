# Customer Follow-up Enhancements (localizat la `deltatech_account_enterprise/index.md`)

- **Nume Tehnic:** `deltatech_account_enterprise`
- **Versiune:** `20.0.0.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_account_enterprise
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_enterprise`
- **Ultima Ingestie:** `2026-10-13`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îmbunătățește urmărirea clienților (Customer Follow-up) din Odoo Enterprise, astfel încât
responsabilul de încasări să vadă exact ce mai are de încasat. Raportul nativ arăta documentele parțial
decontate cu suma lor inițială; modulul păstrează rapoartele native (urmărire, extras de client, creanțe
pe scadențe, exporturi, fereastra de trimitere), dar afișează separat valoarea inițială, partea stinsă și
restul la data aleasă, grupate pe restante și nescadente. Opțional, trimite clienților un memento prin
email și SMS cu o zi înainte de scadența facturilor. Nu alocă plăți și nu modifică înregistrări contabile.

#### 2. Funcționalități Cheie

- **Linii grupate pe status**: pozițiile deschise sunt grupate în **Overdue** (Depășit) și **Due**
  (nescadent) față de data raportului, nu față de data curentă.
- **Sume rămase la dată**: coloanele **Valoare inițială**, **Stins / aplicat** și **Rest**, calculate din
  reconcilierile parțiale datate; notele de credit și plățile nealocate își păstrează semnul, iar un sold
  net zero nu ascunde documentele deschise.
- **Subtotaluri pe status**: fiecare grup are subtotaluri proprii, calculate pe toate pozițiile, nu doar pe
  pagina încărcată; PDF și XLSX au aceleași cifre ca ecranul.
- **Scurtături pe fișa partenerului**: butoanele **Urmărire** (sold semnat al pozițiilor eligibile, fără
  cele marcate No Reminder), **Fișa partener**, **Creanțe pe scadențe** și **Poziții deschise actuale**,
  toate pe partenerul comercial și contactele lui, în firma activă.
- **Poziții deschise actuale**: lista nativă de elemente de jurnal cu restul curent diferit de zero și
  totalul coloanei Rest (actual); este o listă operațională de azi, nu un raport istoric.
- **Reamintire înainte de scadență** (din 20.0.0.1.2): opțiune în **Setări → Facturare**, afișată sub
  **Automatic Invoice Reminders**, nebifată implicit. Bifarea creează pe firma curentă un nivel de
  urmărire de **1 zi before** (întârziere -1) cu email și SMS; SMS-ul listează facturile neplătite ajunse
  la nivel (număr, scadență, rest de plată). Nivelul pleacă prin cron-ul zilnic al reamintirilor
  automate cât timp **Automatic Invoice Reminders** e activă; debifarea șterge nivelul. Dacă firma are
  deja un nivel „before”, configurarea ei se păstrează. Configurarea șabloanelor e descrisă în fișa
  consultant.

#### 3. Dependențe

- `account`
- `account_accountant`
- `account_reports`
- `account_followup`

#### 4. Componente Cheie

**Modele**

- `account.followup.report.handler` (extins): interogarea pozițiilor deschise la data raportului cu rest
  semnat din `account_partial_reconcile`, coloanele Valoare inițială / Stins-aplicat / Rest, gruparea
  Overdue / Due și subtotalurile; face flush ORM înainte de interogările SQL directe.
- `res.partner` (extins): câmpurile **Follow-up Balance** și **Open Receivables**, acțiunile spre
  rapoartele native și lista Poziții deschise actuale; `_get_followup_before_due_text()` produce lista
  de facturi din SMS-ul de memento.
- `res.company` (extins): `_create_followup_before_due_level()` / `_get_followup_before_due_level()`.
- `res.config.settings` (extins): `followup_before_due` — Boolean simplu, citit în `get_values()` din
  nivelurile firmei, ca bifa să nu se piardă între salvare și aplicare.

**Vizualizări**

- `res_partner_view_form`, `res_partner_followup_button`: butoanele de pe fișa partenerului.
- `res_config_settings_view_form`: opțiunea **Reminder Before Due Date** sub **Automatic Invoice
  Reminders**.

**Date**

- `email_template_followup_before_due`, `sms_template_followup_before_due` (`noupdate`): șabloanele
  memento-ului înainte de scadență.

#### 5. Conexiuni

Nu au fost identificate conexiuni verificate către alte module documentate în wiki.
