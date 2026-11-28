# Chart of Accounts Sync

- **Nume Tehnic:** `deltatech_chart_of_accounts`
- **Versiune:** `20.0.0.1.12`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_chart_of_accounts
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chart_of_accounts`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aliniază soldurile conturilor din Odoo cu cele dintr-un alt sistem contabil: balanța de verificare a programului anterior la momentul trecerii pe Odoo sau un sistem paralel păstrat o perioadă. Odoo calculează propriile solduri la o dată, utilizatorul introduce sau importă soldurile externe alături de ele, iar în contabilitate se postează doar diferențele, sub formă de note contabile legate de sincronizare. Modulul postează doar în jurnalul ales; nu importă el însuși planul de conturi.

#### 2. Funcționalități Cheie

- **Soldul Odoo lângă cel extern:** pentru o dată, fiecare cont (sau un singur cont) primește o linie cu debitul, creditul și soldul din Odoo și cu debitul și creditul extern; liniile care diferă sunt evidențiate, iar totalurile arată dacă sincronizarea este echilibrată.
- **Pe partener, când contează:** cu opțiunea **Partner Detail**, conturile de creanțe și datorii se compară pe partener, cu scadență și referință, astfel încât soldurile inițiale ale clienților și furnizorilor să poată fi reconciliate ulterior.
- **Valori externe dintr-un fișier:** valorile externe se introduc manual sau se importă din CSV/Excel; o balanță SAGA cu parteneri este asociată partener cu partener, deci o a doua importare actualizează liniile, nu le dublează.
- **Se postează doar diferența:** modul *Opening balances only* postează diferența netă, cu linii pozitive, față de un cont de capitaluri; modul *Match debit/credit totals* aliniază și totalurile de debit și credit și scrie stornările ca note storno, dacă firma folosește contabilitatea storno.
- **Ciornă, postat, resetare:** notele contabile rămân legate de sincronizare; **Reset to draft** le anulează și le șterge și regenerează liniile, ca o valoare greșită să poată fi corectată și postată din nou (cu confirmare dacă există reconcilieri).
- **Acces:** meniul *Contabilitate > Configurare > Conturi > Sincronizare Plan de Conturi*, rezervat managerilor de contabilitate; datele sunt restricționate pe companie.
- Fluxul pas cu pas, cu capturi de ecran, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `account`

#### 4. Componente Cheie

**Modele**

- `sync.chart.of.accounts`: sesiunea de sincronizare (nume, dată, jurnal, cont de capitaluri, mod de postare); generează liniile de comparație, gestionează stările ciornă/postat și păstrează legătura cu notele contabile generate.
- `import.chart.of.accounts`: linia de sincronizare, cu valorile Odoo alături de cele externe (debit/credit extern); postează diferențele, inclusiv note storno.
- `sync.chart.of.accounts.cancel.wizard` (tranzitoriu): confirmarea anulării/resetării când există reconcilieri.
- `account.move` (extins): marchează nota ca storno când sincronizarea o cere (context `storno`).

**Vizualizări**

- `view_sync_chart_of_accounts_form` / `view_sync_chart_of_accounts_list`: sesiunea de sincronizare, cu butoanele de generare linii, afișare, postare diferență și revenire la ciornă.
- `view_import_chart_of_accounts_list` / `view_import_chart_of_accounts_search`: liniile de sincronizare, în care se introduc valorile externe.
- `view_sync_chart_of_accounts_cancel_wizard_form`: dialogul de confirmare a resetării.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește `ir.cron`, `base.automation` sau acțiuni server. Acțiunile ferestră `action_sync_chart_of_accounts` și `action_import_chart_of_accounts` deschid sesiunile, respectiv liniile.

#### 5. Conexiuni

- `account`: planul de conturi și notele contabile pe care le extinde.
- `l10n_ro`: contabilitatea storno din localizarea românească, folosită la postarea stornărilor.
