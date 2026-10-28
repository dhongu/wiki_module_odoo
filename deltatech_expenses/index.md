# Expenses Deduction (localizat la `deltatech_expenses/index.md`)

- **Nume Tehnic:** `deltatech_expenses`
- **Versiune:** `19.0.3.7.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_expenses
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expenses`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează decontarea cheltuielilor efectuate de angajați pe baza avansurilor de trezorerie primite, un flux specific contabilității din România. Decontul de cheltuieli se introduce într-un document distinct, operat de contabil pe baza documentelor predate de angajat (angajatul nu lucrează în modul). Documentul generează automat chitanțele de achiziție aferente, iar la validare produce notele contabile de avans, de decontare din avans, de diurnă și de diferență, închizând soldul contului de avansuri de trezorerie (542). Se calculează automat diferența de restituit sau de încasat între avansul acordat și cheltuielile justificate, inclusiv TVA-ul deductibil.

> **Notă — nu depinde de `hr_expense`.** Nucleul `deltatech_expenses` este independent de modulul standard `hr_expense`. Preluarea cheltuielilor `hr.expense` într-un decont (wizardul „Preia cheltuieli HR") este în modulul-punte separat [deltatech_expenses_hr_expense](../deltatech_expenses_hr_expense/index.md) (auto-instalabil, activ doar dacă ambele module coexistă). Cele două acoperă procese distincte: `deltatech_expenses` tratează fluxul românesc *avans de trezorerie (542) → decont → diurnă → închidere 542* cu model central propriu (`deltatech.expenses.deduction`), iar `hr_expense` fluxul generic *angajatul/firma plătește → (eventual) rambursare*.

#### 2. Funcționalități Cheie

- Decont de cheltuieli într-un document distinct, cu număr `DEC/…`, care generează automat chitanțe de achiziție (`in_receipt`). Nu se creează înregistrări de plăți (`account.payment`): totul se face prin note contabile și chitanțe.
- Roluri (Setări → Utilizatori, secțiunea „Decont Cheltuieli"; fiecare rol îl include pe cel anterior): **Aprobator** (vede toate deconturile și apasă **Avans**, care aprobă și contabilizează acordarea avansului) și **Contabil** (introduce decontul și liniile, apasă **Validează** și **Invalidare**, poate șterge deconturi în Ciornă). Rolul „Angajat" există, dar nu face parte din fluxul recomandat. Administratorii primesc automat rolul de Contabil.
- Stări: Ciornă → Avans → Efectuat. Validarea generează chitanțele, notele de decontare din avans, nota de diurnă și nota de diferență; **Invalidare** șterge toate notele decontului (inclusiv avansul și chitanțele) și readuce documentul în Ciornă.
- **Suma liniei este mereu brută (TVA inclus)**, adică totalul de pe bon sau factură, indiferent cum e configurată taxa („inclusă în preț" sau „pe deasupra"); modulul extrage din ea baza și TVA-ul deductibil. Cu o taxă „pe deasupra" poate apărea o rotunjire de 1 ban față de bon. Tabelul de linii afișează coloanele de taxă.
- Linii de două tipuri: „Cheltuieli" (justificată cu bon/factură; generează chitanță de achiziție `Dr 6xx + Dr 4426 = Cr 401` și nota de decontare `Dr 401 = Cr 542`, reconciliate între ele) și „Plată furnizor" (angajatul achită direct o datorie a firmei; generează `Dr 401 = Cr 542`, reconciliată cu facturile furnizor deschise).
- **Plata directă la furnizor fără factură deschisă**: partea neacoperită de facturi deschise este un avans acordat furnizorului și se reclasifică automat `Dr 4092 = Cr 401` (reconciliat), astfel încât pe 401 nu rămâne sold debitor. Se folosește mereu 4092 (servicii); pentru bunuri (4091) sau imobilizări (4093) contabilul reclasifică manual, iar la primirea facturii compensează avansul (`Dr 401 = Cr 4092`).
- Calcul diurnă: sumă/zi (`diem`) × număr de zile (acceptă o zecimală, ex. 2,5 — pentru deplasări în străinătate diurna se acordă și pe fracțiuni de zi) = `total_diem`, cu notă proprie `Dr 625 = Cr 542`, datată cu data cheltuielii. Valoarea implicită de 42,50 lei/zi este doar un punct de pornire, **nu un plafon**: modulul contează integral diurna introdusă și nu verifică plafonul fiscal de neimpozitare. Partea peste plafon se preia manual în salarizare ca venit impozabil; verificarea automată o oferă modulul opțional `l10n_ro_expense_allowance`.
- Închiderea contului 542 prin **nota de diferență** (`Dr 5311 = Cr 542` când angajatul restituie, `Dr 542 = Cr 5311` când firma îi plătește diferența), **datată cu data decontului** (data cheltuielii), nu cu data avansului.
- **Mod de decontare** (`settlement_mode`, pe decont): **Numerar** (avansul se plătește din casă, `Dr 542 = Cr 5311`); **Virament (card personal)** (avansul se plătește dintr-un jurnal bancar prin contul de plăți în curs 5125 al jurnalului: `Dr 542 = Cr 5125`, apoi se potrivește cu extrasul `Dr 5125 = Cr 5121`; restituirea e `Dr 5125 = Cr 542`); **Card de firmă** (fără avans: fiecare chitanță se decontează `Dr 401 = Cr 5125` al jurnalului cardului, potrivit apoi cu extrasul cardului; din jurnalul de plată se achită doar diurna datorată angajatului). Retragerea de numerar cu cardul firmei este un decont separat, în modul Virament (`Dr 542 = Cr 5121`).
- **Jurnal card firmă**: pe decont (`card_journal_id`) și pe angajat (tabul „Setări", `expenses_card_journal_id`), din care se preia implicit la alegerea modului „Card de firmă". Jurnalele băncii/cardului au nevoie de conturi de plăți/încasări în curs 5125 pe metodele de plată.
- **Decont în valută**: moneda decontului este cea a jurnalului de plată (sau a jurnalului cardului, la „Card de firmă"); dacă e diferită de moneda companiei, avansul, liniile, diurna și diferența se introduc în valută, iar fiecare notă poartă suma în valută (`amount_currency`) și contravaloarea la cursul (BNR) de la data ei: avansul la data avansului, fiecare chitanță la data ei, diurna și diferența la data cheltuielii. La validare, 542 se închide în valută, iar soldul rămas în RON se contabilizează ca diferență de curs: `Dr 665 = Cr 542` (pierdere) sau `Dr 542 = Cr 765` (câștig). Cere jurnal de casă în valută (5314), jurnal de cheltuieli pe un 542 în valută, cursuri la zi și conturile de diferențe de curs din Setări contabilitate. La „Card de firmă" în valută, jurnalul de plată al diurnei trebuie să fie în aceeași valută sau în moneda companiei.
- Moneda liniei de decont este calculată din decont (`currency_id` de pe linie derivă din decont) și nu este un câmp independent: o monedă trimisă la creare/scriere (de ex. de o integrare) este ignorată, dar moneda decontului poate fi acum și valută, nu doar moneda companiei.
- Contul de cheltuială se vede în coloana „Cont cheltuieli implicit" (implicit primul cont 623; pentru deplasări se schimbă în 625).
- Taba **„Chitanțe"** pe decont afișează chitanțele de achiziție generate (tabul „Plăți" apare doar dacă există plăți); „Elemente jurnal" afișează toate liniile contabile.
- Tipărire: meniul ⚙ → Tipărire → „Tipărire decont cheltuieli" (justificativul semnat de titularul avansului).
- Meniu: Facturare → Furnizori → Decont Cheltuieli (cu Enterprise: Contabilitate → Furnizori → Decont Cheltuieli).
- Buton smart „Deconturi" pe fișa angajatului (`hr.employee`), cu numărul deconturilor și listă filtrată; vizibil doar grupurilor modulului.
- Partenerul contabil de pe note derivă din „Work Contact" (`work_contact_id`); dacă lipsește, notele se generează fără partener (înregistrări interne), iar validarea funcționează în ambele cazuri.

> **Configurare:** pe decont, „Jurnal avansuri (542)" (tabul „Alte informații") trebuie să aibă drept cont implicit 542; jurnalul de numerar (Casă) trebuie să aibă contul 5311; „Cont diurnă" (implicit primul 625) e în antet, „Jurnal diurnă" în „Alte informații". Alegerea cotei TVA se face pe linie: taxa se pune doar dacă documentul dă drept de deducere (factură sau bon fiscal ≤ 100 euro cu codul de TVA al firmei tipărit).

#### 3. Dependențe

- `l10n_ro`
- `account`
- `product`
- `hr`
- [deltatech_partner_generic](../deltatech_partner_generic/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.expenses.deduction`: decontul de cheltuieli (stări, avans, diurnă, `settlement_mode`, `card_journal_id`, moneda și diferențele de curs, notele contabile generate).
- `deltatech.expenses.deduction.line`: linia de decont (bon sau plată furnizor), cu moneda derivată din decont.
- `account.move`, `account.journal`, `account.payment`: extinderi pentru legătura cu decontul.
- `hr.employee`: butonul „Deconturi" și câmpul `expenses_card_journal_id` (Jurnal card firmă).

**Vizualizări**

- `views/deltatech_expenses_deduction_view.xml`: formular, listă, căutare și meniul „Decont Cheltuieli".
- `views/hr_employee_view.xml`, `views/account_journal_view.xml`: extinderi pe angajat și jurnal.
- `views/deltatech_expenses_deduction_report.xml`, `views/report_expenses.xml`: raportul tipărit al decontului.

**Acțiuni Automate / Acțiuni Server**

- Nu are `ir.cron` sau acțiuni server; `data/data.xml` conține datele implicite (secvența `DEC/…`).

#### 5. Conexiuni

- [deltatech_expenses_hr_expense](../deltatech_expenses_hr_expense/index.md): modul-punte care preia cheltuielile standard `hr.expense` ca linii de decont și previne dubla contabilizare la postare; nu este dependență a `deltatech_expenses`, ci invers.
- [deltatech_partner_generic](../deltatech_partner_generic/index.md): furnizează partenerul generic pentru liniile de decont fără furnizor explicit.
- [l10n_ro_expense_allowance](../l10n_ro_expense_allowance/index.md) (opțional): plafonul fiscal al diurnei și surplusul impozabil.
