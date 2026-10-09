# Deltatech Payment Report (localizat la `deltatech_payment_report/index.md`)

- **Nume Tehnic:** `deltatech_payment_report`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_payment_report
- **Cale Locală:** `odoo-addons/deltatech/deltatech_payment_report`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă contabililor și managerilor financiari un raport de analiză a încasărilor de la clienți pe o perioadă aleasă. Raportul arată cum se distribuie încasările între jurnalele de bancă și de numerar și între jurnalele facturilor achitate, ajutând la urmărirea fluxului de numerar.

#### 2. Funcționalități Cheie

- Asistent de raportare cu **Data început**, **Data sfârșit** (implicit azi) și **Încasări** (jurnalele de plată). La deschidere sunt preselectate toate jurnalele de tip bancă și numerar.
- Meniu: **Facturare > Contabilitate > Acțiuni > Payment Report** (grupul Contabil / Manager contabilitate); se apasă **Show** pentru a genera raportul.
- Sunt incluse doar **încasările de la clienți** (inbound, tip partener client) aflate în starea **În curs de procesare** sau **Plătit**; ciorne, anulate și respinse sunt excluse (corecție din 19.0.1.0.3, când raportul ieșea gol).
- Analiză multidimensională în vizualizare **Pivot** (rânduri: jurnalul plății, coloane: jurnalul facturii, măsură: suma), plus vizualizări **Listă** și **Formular** pentru liniile raportului (dată, client, sumă, jurnal plată, jurnal factură, metodă de plată).
- Metoda de plată `card` este înregistrată pentru jurnalele de tip bancă (mod `unique`).
- Limitări cunoscute (`readme/bugs.md`): butonul de tipărire PDF (`print_pdf`) nu are raport asociat și generează o eroare (PAYREPORT-002, deschis); pentru plățile care achită mai multe facturi se reține jurnalul ultimei facturi.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.payment.report` (tranzitoriu): asistentul cu filtrele; `do_compute()` caută plățile și creează liniile, `button_show_report()` deschide rezultatul.
- `account.payment.report.line` (tranzitoriu): linia raportului (dată, client, sumă, monedă, jurnal plată, jurnal factură, metodă de plată).
- `account.payment.method` (extins): adaugă metoda `card` în informațiile metodelor de plată.

**Vizualizări**

- `view_account_payment_report_form`: formularul asistentului (Report Options).
- `view_account_payment_report_line_pivot`: pivot implicit, jurnal plată pe rânduri, jurnal factură pe coloane.
- `view_account_payment_report_line_list` / `view_account_payment_report_line_form`: listă și formular, doar citire.
- `view_account_payment_report_line_search`: căutare după jurnalul plății și al facturii.
- `menu_account_payment_report`: meniul de acces, sub `account.menu_finance_entries`.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- Nu există legături funcționale verificate cu alte module wiki; modulul depinde doar de `account`.
