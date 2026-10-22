# Chart of Accounts (localizat la `deltatech_chart_of_accounts/index.md`)

- **Nume Tehnic:** `deltatech_chart_of_accounts`
- **Versiune:** `19.0.0.1.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_chart_of_accounts
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chart_of_accounts`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aliniază soldurile conturilor din Odoo cu cele ale altui sistem contabil: balanța de verificare a programului anterior la momentul trecerii în Odoo sau a unui sistem ținut în paralel o perioadă. Odoo calculează soldurile proprii la o dată, utilizatorul introduce sau importă soldurile externe alături de ele, iar modulul postează doar diferențele, sub formă de note contabile legate de sincronizare. Diferențele se văd pe ecran înainte de orice înregistrare, iar dacă o valoare a fost greșită, notele se anulează și se reiau. Modulul nu încarcă planul de conturi: conturile trebuie să existe deja în Odoo.

#### 2. Funcționalități Cheie

- **Solduri Odoo lângă cele externe:** pentru o dată, fiecare cont (sau un singur cont) primește o linie cu debitul, creditul și soldul din Odoo și cu debitul și creditul extern. Diferențele sunt evidențiate (roșu pentru diferențe, albastru pentru sume egale și nenule), iar totalurile și bifa **Echilibrat** arată dacă sincronizarea se închide. La prima generare, valorile externe pornesc de la cele din Odoo.
- **Detaliu pe partener:** conturile de creanțe și datorii se compară pe fiecare partener, cu scadență și referință, pentru ca soldurile inițiale ale clienților și furnizorilor să poată fi reconciliate ulterior.
- **Valori externe din fișier:** valorile se introduc manual sau se importă din CSV/Excel cu importul standard Odoo, câte o sincronizare pe cont de terți. Importul potrivește rândurile după partener: reimportul actualizează liniile existente în loc să le dubleze, iar două firme cu același nume opresc importul. Butonul **Șterge sumele externe** readuce valorile externe la 0 înaintea unui import nou.
- **Se postează doar diferența**, în două moduri:
  - **Doar solduri de deschidere** (recomandat la go-live): se postează diferența netă de sold, doar cu sume pozitive; conturile de tip rezultat curent nu se ajustează direct, iar contul de echilibrare primește o linie „Diferență” doar dacă nota nu se închide.
  - **Potrivește totalurile debit/credit** (pentru sisteme ținute în paralel): se aliniază separat rulajele de debit și de credit; când rulajul extern e mai mic, corecția se scrie ca notă storno separată (contabilitate în roșu).
- **Ciornă, Postat, resetare:** notele rămân legate de sincronizare (tab **Note contabile**). **Resetare la ciornă** le anulează și le șterge, apoi regenerează liniile. Dacă liniile notelor au fost deja reconciliate, un wizard de confirmare listează partenerii afectați, iar confirmarea desface acele reconcilieri.
- **Configurare:** sincronizarea cere data, jurnalul (tip Diverse), contul de echilibrare (propus: contul de tip rezultat curent), modul de postare și, opțional, un singur cont. Meniul și toate operațiunile sunt rezervate grupului Contabilitate: Administrator; accesul se face din Contabilitate > Configurare > Conturi > Sincronizare Plan de Conturi.
- **Alte reguli:** modulul nu generează linii de TVA (soldurile de TVA se preiau ca orice alt cont); jurnalul notelor trebuie să nu fie securizat, iar data sincronizării să nu fie într-o perioadă blocată.
- Fluxul pas-cu-pas, monografia contabilă, exemplul numeric, verificările și erorile frecvente sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `account`

#### 4. Componente Cheie

**Modele**

- `sync.chart.of.accounts`: sesiunea de sincronizare (nume, dată, companie, detaliu pe partener, cont opțional, jurnal, cont de echilibrare, mod de postare, stare ciornă/postat). Generează liniile, calculează `balance_odoo`, `balance_external` și `is_balanced`, postează diferențele și gestionează resetarea la ciornă; păstrează legătura cu notele generate (`move_ids`).
- `import.chart.of.accounts`: linia de sincronizare, cu valorile Odoo (debit, credit, sold) și cele externe (debit/credit extern, sold extern calculat), partener, referință, scadență. Suprascrie `load` pentru importul potrivit după partener și conține logica de postare pe cele două moduri (`balance_only`, `debit_credit`).
- `sync.chart.of.accounts.cancel.wizard` (tranzitoriu): confirmarea anulării notelor când acestea au linii reconciliate.
- `account.move.line` și `account.move` (extinse): logica de storno, folosită la modul de potrivire a totalurilor debit/credit.

**Vizualizări**

- `view_sync_chart_of_accounts_form` / `view_sync_chart_of_accounts_list`: formularul și lista sincronizării (butoane Generează liniile, Afișează, Șterge liniile, Șterge sumele externe, Postează diferența, Resetare la ciornă; tab Note contabile).
- `view_import_chart_of_accounts_list` / `view_import_chart_of_accounts_search`: lista editabilă a liniilor, cu panou lateral pe clase de conturi și evidențierea diferențelor.
- `view_sync_chart_of_accounts_cancel_wizard_form`: confirmarea resetării cu reconcilieri existente.
- `menu_sync_chart_of_accounts`: meniul Sincronizare Plan de Conturi, sub Contabilitate > Configurare > Conturi.

**Acțiuni Automate / Acțiuni Server**

- `action_sync_chart_of_accounts`: acțiunea de fereastră a meniului sincronizărilor.
- `action_import_chart_of_accounts`: acțiunea de fereastră a liniilor de sincronizare (deschisă cu **Afișează**).
- Nu există `ir.cron` sau reguli `base.automation`.

#### 5. Conexiuni

- `account`: conturile, jurnalele, notele contabile și reconcilierile pe care modulul le folosește.
- `l10n_ro`: planul de conturi RO (inclusiv contul 121000 de tip rezultat curent) și contabilitatea în roșu, activă implicit la firmele din România.
- `base_import`: importul valorilor externe din CSV/Excel.
