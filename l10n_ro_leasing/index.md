# Romania - Împrumuturi și leasing (162/167/21x) (localizat la `l10n_ro_leasing/index.md`)

- **Nume Tehnic:** `l10n_ro_leasing`
- **Versiune:** `19.0.2.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_leasing
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_leasing`
- **Ultima Ingestie:** 2026-10-12
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența **creditelor bancare** și a contractelor de **leasing financiar și operațional**, conform OMFP 1802/2014. Calculează graficul de rambursare, generează automat notele contabile, angajează lunar dobânda, leagă tragerile și ratele de extrasul de cont și repartizează datoria pe termen scurt și termen lung, pentru bilanț. Contabilul are astfel o singură evidență pentru toate datoriile de finanțare, cu rapoarte gata de folosit pentru nota explicativă.

#### 2. Funcționalități Cheie

**Contracte și grafic de rambursare**

- Trei feluri de contract: credit bancar (`162` pe termen lung, `519` pe termen scurt), leasing financiar (`21x` / `167`) și leasing operațional (`612`).
- **Tipuri de contract** reutilizabile (conturi, jurnal, durată, metodă de calcul); la planul de conturi RO se creează automat patru tipuri: credit pe termen lung, credit pe termen scurt, leasing financiar, leasing operațional. Meniu: Contabilitate → Configurare → Contabilitate → Tipuri de împrumut / leasing.
- Meniul principal: Contabilitate → Contabilitate → Împrumuturi și leasing (fără Contabilitatea enterprise: Facturare → Contabilitate → …), cu filtre pe fel de contract și pe contractele active.
- Două metode de calcul: **rată constantă** (anuitate) și **principal constant**; convenții de zile 30/360, zile reale/360 sau zile reale/365.
- **Avans** (prima linie a graficului) și **valoare reziduală** (sumă sau procent), plătită într-o ultimă rată separată; dobânda curge pe tot soldul.
- **Cota de TVA pe fiecare rată**, după data scadenței (19% înainte de 01.08.2025, apoi 21%); regim scutit pentru leasingul de bunuri imobile; fără TVA la credit.
- Contracte în **valută**: notele se înregistrează în moneda contractului, iar soldurile `162`, `167`, `168`, `519` intră în reevaluarea valutară lunară.
- Stări contract: ciornă → activ → finalizat (sau anulat); editare manuală a graficului.

**Credit bancar**

- Tragerea și ratele se leagă de **linia de extras**: contrapartida se completează direct în nota extrasului, fără mișcare bancară dublă. Tragere: Dr `5121` + Dr `627` = Cr `16212`. Rată: Dr `16211` + Dr `16821` + Dr `627` = Cr `5121`. Anularea reconcilierii readuce rata în așteptare.
- **Dobânda angajată la sfârșit de lună**, pro-rata pe zile: Dr `666` = Cr `16821` / `51981`; la plată se angajează întâi dobânda zilelor rămase.
- Comisionul de acordare: direct pe cheltuieli sau eșalonat lunar prin `471`.

**Leasing**

- Leasing financiar: activare la costul total (avans + sumă finanțată) Dr `21x` = Cr `1672`; rata Dr `1671` + Dr `666` + Dr `4426` = Cr `4041` (furnizori de imobilizări; contractele vechi își păstrează contul anterior).
- Leasing operațional: rata Dr `612` + Dr `4426` = Cr `401`.
- Ratele se înregistrează individual, în batch sau printr-un cron opțional (implicit dezactivat).

**Pe toată durata contractului**

- **Reclasificare termen scurt / lung** la sfârșit de lună (`16212` → `16211`, `1672` → `1671`), prin notă de diferență, fără stornări.
- **Preluarea unui contract în derulare**, cu solduri de deschidere (inclusiv dobânda deja angajată), fără notă de tragere/activare.
- **Schimbarea dobânzii** (ROBOR/IRCC/EURIBOR + marjă) de la o dată: se regenerează doar ratele viitoare neînregistrate; istoricul rămâne pe contract.
- **Închidere anticipată** printr-un asistent (comision de rambursare anticipată, anulare rate rămase); anularea notei redeschide contractul.
- **Situația datoriilor pe scadențe** (sub 1 an, 1–5 ani, peste 5 ani, cu dobânda angajată și garanțiile) și **Analiză rate** în pivot/grafic.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.leasing.contract`: contractul (credit/leasing), graficul, generarea notelor, reclasificarea și starea.
- `l10n.ro.leasing.contract.line`: linia graficului (principal, dobândă, comision, TVA, total, sold).
- `l10n.ro.leasing.type`: tipul de contract cu valorile implicite (conturi, jurnal, durată, metodă); folosește mixinul `l10n.ro.leasing.accounts.mixin`.
- `l10n.ro.leasing.accrual`: dobânda angajată lunar.
- `l10n.ro.leasing.rate.change`: istoricul schimbărilor de dobândă.
- `l10n.ro.leasing.maturity.report` / `l10n.ro.leasing.maturity.line`: situația datoriilor pe scadențe.
- `l10n.ro.leasing.statement.match`: asistent de legare a tragerii/ratei de linia de extras.
- `l10n.ro.leasing.early.close`: asistent de închidere anticipată.
- Extinderi: `account.bank.statement.line`, `account.move`, `account.move.line`, `account.chart.template` (crearea tipurilor la planul de conturi RO).

**Vizualizări**

- `views/l10n_ro_leasing_contract_views.xml`: formular/listă contract, cu pagini pentru grafic, preluare și comisioane, contabilitate.
- `views/l10n_ro_leasing_type_views.xml`: tipurile de contract.
- `views/l10n_ro_leasing_line_views.xml`: analiza ratelor (pivot, grafic).
- `views/account_bank_statement_line_views.xml`: legătura cu linia de extras.
- `wizard/*_views.xml`: formulare pentru legare extras, închidere anticipată și situația pe scadențe.
- `views/menu.xml`: meniul „Împrumuturi și leasing”.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_cron.xml`: cron zilnic „Due Instalments and Month-end Entries” (`_cron_post_due_leasing_entries`), postează ratele scadente și notele de sfârșit de lună; implicit inactiv.
- `post_init_hook`: creează tipurile de contract implicite la instalare.

#### 5. Conexiuni

- [l10n_ro_currency_revaluation](../l10n_ro_currency_revaluation/index.md): reevaluarea valutară lunară preia soldurile contractelor în valută.
