# Registru de casă RO (localizat la `l10n_ro_cash_register/index.md`)

- **Nume Tehnic:** `l10n_ro_cash_register`
- **Versiune:** `19.0.1.1.7`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_cash_register
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_cash_register`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul oferă un registru de casă zilnic pentru jurnalele de tip numerar și leagă operațiunile de încasare, plată și transfer direct de soldul casei. Pentru fiecare combinație de jurnal de casă și dată există un singur registru, cu sold inițial și sold final calculate automat din mișcările contabile postate. Modulul este soluția operațională pentru partea de registru de casă din localizarea românească, oferind casierilor și contabililor un instrument controlat pentru operarea numerarului și tipărirea registrului. Modulul nu acoperă importul extraselor bancare MT940 și nici reconcilierea bancară automată; acestea rămân module complementare separate.

#### 2. Funcționalități Cheie

- Model nou de registru de casă, organizat pe zi și pe jurnal de casă (un registru unic per combinație).
- Calcul automat de sold inițial și sold final din mișcările contabile postate pe contul de casă.
- Acces rapid la încasare, plată și operațiune de casă direct din formularul registrului.
- Wizard de operațiune casă (Cash In / Cash Out) care generează și postează automat nota contabilă cu contul de casă și contul corespondent.
- Generare automată a registrului de casă la postarea plăților pe jurnalul de tip numerar.
- Acțiune „Generate Missing Cash Register" pentru crearea registrelor lipsă pentru toate zilele cu mișcări.
- Raport PDF tipărit pentru registrul de casă (date companie, CIF/NRC, sold inițial, linii pe partener, total încasări/plăți, sold final).
- Deschiderea directă a registrului de casă din jurnalul cash pentru companiile din România.
- Cron pregătit pentru generarea registrelor lipsă, livrat inactiv.

#### 3. Dependențe

- `account`
- `l10n_ro_account_sequence`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de Componente Cheie (Modele, Vizualizări, Acțiuni Automate / Acțiuni Server) se omit deoarece documentația din readme acoperă scopul și funcționalitățile modulului fără a impune analiza suplimentară a codului. Pentru context tehnic, readme-ul menționează modelul principal `l10n.ro.cash.register`, un raport PDF dedicat și un `ir.cron` de generare a registrelor lipsă livrat inactiv.

#### 5. Conexiuni

- `l10n_ro_account_sequence`: furnizează secvențele localizate folosite la numerotarea registrului de casă.
- `account`: jurnale, plăți și note contabile pe care se bazează registrul.
- `l10n_ro_account_bank_statement_import_mt940_base`: bază pentru importul extraselor bancare MT940, complementar pe partea de bancă a aceluiași domeniu funcțional (FR-28).
- `l10n_ro_account_bank_statement_import_mt940_bcr` / `..._ing` și alte adaptoare de bancă: importul extraselor pentru diverse bănci, în afara acestui modul.
