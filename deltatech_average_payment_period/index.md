# Average Payment Period (localizat la `deltatech_average_payment_period/index.md`)

- **Nume Tehnic:** `deltatech_average_payment_period`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_average_payment_period
- **Cale Locală:** odoo-addons/deltatech/deltatech_average_payment_period
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Modulul măsoară cât durează în realitate până când clienții plătesc și până când firma își plătește furnizorii, oferind echipei financiare un indicator concret al eficienței încasărilor și plăților. Pentru fiecare linie de jurnal reconciliată se înregistrează data efectivă a plății și numărul de zile scurse de la data facturii. Un raport pivot/grafic, **Average Payment Period**, permite analiza pe partener, jurnal sau perioadă și ajută la gestionarea cash-flow-ului.

#### 2. Funcționalități Cheie

- **Data plății** (`Payment Date`): se determină automat din linia de contrapartidă a reconcilierii și se stochează pe fiecare linie de jurnal.
- **Zile de plată** (`Payment Days`): diferența în zile dintre data facturii și data plății, ponderată cu suma liniei, pentru medii corecte pe date grupate.
- **Zile de plată simple** (`Plain payment days`): variantă limitată la facturi client (`out_invoice`) și facturi furnizor (`in_invoice`), fără note de credit, pentru indicatori mai curați.
- Raport pivot și grafic **Average Payment Period** (**Contabilitate → Raportare → Average Payment Period**), grupat implicit pe partener, cu măsurile Balance, Payment Days și Plain payment days; se poate filtra după dată (lună, trimestru, an), partener și referință și regrupa pe dată sau jurnal.
- Media pe grupuri este ponderată, `sum(sumă × zile) / sum(sumă)`, nu o medie aritmetică simplă, ca sumele mici să nu distorsioneze rezultatul.
- Valorile se actualizează singure la reconciliere și la dereconciliere, fără acțiuni manuale; raportul ia în calcul doar notele postate, cu linii complet reconciliate, din jurnale de vânzări și achiziții.
- Raportul are regulă multi-company: utilizatorii văd doar liniile companiilor active (19.0.1.0.4).

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move.line` (extins): câmpurile stocate `payment_date`, `payment_days` și `payment_days_simple`, calculate la reconciliere.
- `account.average.payment.report` (view SQL, `_auto = False`): raportul de analiză, cu `weight`, `amount`, `balance` și `company_id`; `_read_group()` calculează media ponderată a zilelor de plată.

**Vizualizări**

- `view_move_line_form`: câmpurile Payment Date și Payment Days pe formularul liniei de jurnal, după data scadenței.
- `view_account_average_payment_report_pivot`: pivotul raportului, pe partener.
- `view_account_average_payment_report_search`: căutare după partener, referință și dată, grupări după partener și dată.
- `action_account_average_payment_report`: acțiunea pivot/grafic din meniul Raportare.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; calculul rulează la reconciliere. Regula `account_average_payment_report_company_rule` limitează raportul la companiile utilizatorului.

#### 5. Conexiuni

- `account`: facturile, plățile și reconcilierile din contabilitatea nativă sunt sursa calculului.
