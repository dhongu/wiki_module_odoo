# Romania - Împrumuturi și leasing (162/167/21x) (localizat la `l10n_ro_leasing/index.md`)

- **Nume Tehnic:** `l10n_ro_leasing`
- **Versiune:** `20.0.2.1.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_leasing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_leasing`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența creditelor bancare și a contractelor de leasing financiar și operațional, conform OMFP 1802/2014. Pentru fiecare contract calculează graficul de rambursare, generează notele contabile, angajează lunar dobânda și împarte datoria pe termen scurt și termen lung, pentru bilanț. La credit, nota pleacă din extrasul de cont; la leasing, din factura ratei primită de la locator.

#### 2. Funcționalități Cheie

- Trei feluri de contract: credit bancar (`162` termen lung, `519` termen scurt), leasing financiar (`21x` / `167`) și leasing operațional (`612`), cu **tipuri de contract** reutilizabile (conturi, jurnal, durată, metodă). La planul de conturi RO se creează automat patru tipuri.
- Grafic de rambursare cu rată constantă (anuitate) sau principal constant, cu convenție de zile 30/360, zile reale/360 sau zile reale/365; avans, valoare reziduală (sumă sau procent) și editare manuală a graficului înainte de activare.
- TVA pe fiecare rată după data scadenței (19% înainte de 01.08.2025, apoi 21%), regim scutit la leasingul de bunuri imobile, fără TVA la credit; contracte în valută, cu soldurile `162`, `167`, `168`, `519` preluate de reevaluarea valutară lunară.
- Credit bancar: tragerea și ratele se leagă de linia extrasului de cont (fără mișcare bancară dublă), comisioane (acordare, eventual eșalonat prin `471`, și lunar) și dobândă angajată la sfârșit de lună (`666` = `16821` / `51981`).
- Leasing: nota de activare Dr `21x` = Cr `1672`; rata se leagă de factura de furnizor a locatorului (importată din e-Factura sau creată din grafic), cu taxe și grile de decont pentru D300, D394 și SAF-T; nota din contract rămâne disponibilă pentru contractele existente (individual, în lot sau prin acțiune programată).
- Reclasificare lunară termen scurt / termen lung prin notă de diferență, fără stornări.
- Preluarea unui contract aflat în derulare (fără notă de tragere/activare, cu solduri de deschidere) și schimbarea dobânzii (ROBOR, IRCC, EURIBOR + marjă) de la o dată, cu regenerarea ratelor viitoare.
- Închidere anticipată printr-un asistent (sau prin factura de închidere a locatorului la leasing financiar), cu anularea ratelor rămase.
- Situația datoriilor pe scadențe la orice dată (sub 1 an, 1–5 ani, peste 5 ani) și analiză rate în pivot și grafic.
- Fluxul pas cu pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.leasing.contract`: contractul de credit sau leasing, cu graficul de rate, starea și logica notelor contabile.
- `l10n.ro.leasing.contract.line`: linia graficului (avans, rată, valoare reziduală) cu principal, dobândă, comision, TVA și sold.
- `l10n.ro.leasing.type`: tipul de contract, cu conturile, jurnalul, durata și metoda implicite.
- `l10n.ro.leasing.accrual`: dobânda angajată lunar.
- `l10n.ro.leasing.rate.change`: istoricul schimbărilor de dobândă.
- `account.move`, `account.move.line`, `account.bank.statement.line`, `account.chart.template` (extinse): legătura ratelor cu facturile și extrasele și crearea tipurilor la planul de conturi RO.

**Vizualizări**

- `views/l10n_ro_leasing_contract_views.xml`: lista și formularul contractelor.
- `views/l10n_ro_leasing_type_views.xml` și `views/l10n_ro_leasing_line_views.xml`: tipurile de contract și analiza ratelor.
- `views/account_bank_statement_line_views.xml` și `views/account_move_views.xml`: legătura cu extrasul de cont și cu factura.
- Asistenți: potrivire cu extrasul (`l10n.ro.leasing.statement.match`), închidere anticipată (`l10n.ro.leasing.early.close`) și situația datoriilor pe scadențe (`l10n.ro.leasing.maturity.report`).

**Acțiuni Automate / Acțiuni Server**

- `cron_post_due_leasing_entries`: postează automat ratele scadente ale contractelor (pentru nota din contract).

#### 5. Conexiuni

- [l10n_ro_payment_instruments](../l10n_ro_payment_instruments/index.md): instrumente de plată românești folosite la achitarea ratelor.
- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): reevaluarea valutară lunară preia soldurile contractelor în valută.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md) și [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): TVA-ul ratelor de leasing intră în grilele de decont.
