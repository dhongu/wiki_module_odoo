# PayPal Settlements (localizat la `deltatech_account_bank_statement_import_paypal/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_paypal`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_paypal
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_paypal`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul importă direct în Odoo, ca extras de cont, raportul de activitate (Activity download) generat de PayPal. Fiecare plată, rambursare, conversie valutară și retragere către bancă devine o linie de extras, legată de client, iar comisioanele PayPal sunt importate separat, fără nicio editare a fișierului. Modulul citește doar fișierul încărcat și nu se conectează la PayPal.

#### 2. Funcționalități Cheie

- **Fișier în forma descărcată**: se încarcă raportul *Activity download* (CSV, tranzacții care afectează soldul, antet în engleză) exact așa cum îl produce PayPal.
- **Recunoaștere automată**: fișierul este identificat după setul de coloane, în orice ordine, deci se importă din jurnal ca orice alt format de extras, fără asistentul de mapare a coloanelor.
- **O monedă per jurnal**: PayPal ține un sold pe fiecare monedă. Se importă doar rândurile în moneda jurnalului; o plată în altă monedă ajunge prin conversia ei, la suma efectiv creditată, netă de comision (comisionul rămâne pe rândul în moneda străină). Pentru un al doilea jurnal în altă monedă se încarcă același fișier și acolo.
- **Doar ce mișcă soldul**: autorizările, blocările și alte rânduri informative (*Memo*) sunt omise.
- **Client identificat după plată**: clientul se ia din plata online Odoo care poartă id-ul tranzacției PayPal sau referința plății (*Invoice Number*), ori din comanda de vânzare cu acea referință; dacă nu există exact o potrivire, linia rămâne neatribuită, pentru operator.
- **Comisioane configurabile**: comisioanele PayPal, inclusiv cele returnate la rambursări, se importă ca o linie agregată, câte o linie per tranzacție sau deloc (opțiunea *Settlement Files: Fees* din jurnal). Opțiunea *Add Payout Line* nu are efect, retragerile către bancă fiind linii ale fișierului.
- **Date în ambele ordini**: sunt citite atât datele zi-lună (Europa), cât și lună-zi (SUA); dacă toate zilele sunt ≤ 12, fișierul e citit zi-lună.
- **Fără duplicate**: fiecare tranzacție se importă o singură dată, deci perioadele suprapuse pot fi importate fără risc.
- **Configurare**: pentru fiecare monedă se creează în *Contabilitate > Configurare > Jurnale* un jurnal de tip Bank (ex. *PayPal EUR*), cu cont propriu pentru soldul PayPal (în planul românesc, un subcont 461 de tip Bank and Cash, în moneda jurnalului), iar *Bank Feeds* se setează pe *Import*.
- **Reconciliere**: liniile de plată cu facturile clienților, linia de comision cu contul de comisioane (627), retragerile cu transferul PayPal din extrasul bancar real, printr-un cont de transfer intern (581). Conversia fără jurnal PayPal în moneda plății este chiar plata clientului, netă de comision (diferența de comision la 627, diferențele de curs la 665/765); dacă există jurnal și în moneda plății, conversiile din cele două jurnale se reconciliază între ele prin 581, niciodată cu factura, ca plata să nu fie numărată de două ori.
- **Observații contabile**: extrasul nu înlocuiește factura de comision PayPal; comisioanele returnate la rambursări reduc cheltuiala, iar sumele reținute de PayPal rămân creanțe, nu cheltuieli.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

#### 4. Componente Cheie

*Notă: conform priorității Readme, componentele tehnice nu au fost extrase detaliat din cod; secțiunea oferă doar un reper minim.*

**Modele**

- `account.journal` (extindere): înregistrează formatul „PayPal”, îl detectează după setul de coloane obligatorii (`PAYPAL_REQUIRED_COLUMNS`) prin helperul comun din [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md) și parsează fișierul (`_parse_paypal_file`), folosind modul de comision al jurnalului. `account_bank_statement_import_csv` e în dependențe pentru ordinea MRO: importul PayPal trebuie să ruleze înaintea interceptorului CSV/XLSX.

**Vizualizări**

- Nu definește vizualizări proprii; opțiunile de comision sunt cele din formularul jurnalului, furnizate de modulul comun.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md): constructorul comun de extrase de decontare (parsare sume/date, mod comisioane, identificare partener).
- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): modul soră pentru decontările Euplatesc.
- [deltatech_account_bank_statement_import_emag](../deltatech_account_bank_statement_import_emag/index.md): modul soră pentru decontările eMAG.
- [deltatech_account_bank_statement_import_gls](../deltatech_account_bank_statement_import_gls/index.md): modul soră pentru decontările GLS.
