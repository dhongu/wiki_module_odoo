# Average Payment Period (localizat la `deltatech_average_payment_period/index.md`)

- **Nume Tehnic:** `deltatech_average_payment_period`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_average_payment_period
- **Cale Locală:** `odoo-addons/deltatech/deltatech_average_payment_period`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul măsoară cât de repede plătesc clienții și furnizorii, adică perioada scursă între data facturii și data efectivă a decontării. Pentru fiecare înregistrare contabilă reconciliată se reține data plății și se calculează numărul de zile, iar un raport agregat din meniul de rapoarte contabile permite analiza pe partener, jurnal sau perioadă. Echipa financiară obține un indicator concret pentru gestionarea cash-flow-ului.

#### 2. Funcționalități Cheie

- **Payment Date**: dedusă automat din linia de partener cu care s-a făcut reconcilierea și stocată pe fiecare `account.move.line`.
- **Payment Days**: diferența în zile dintre data facturii și data plății, ponderată cu suma liniei.
- **Plain Payment Days**: variantă simplă, limitată la facturi de client (`out_invoice`) și de furnizor (`in_invoice`), fără note de credit.
- Raportul **Average Payment Period** (**Contabilitate > Raportare > Average Payment Period**) este pivot și grafic, grupat implicit pe partener, cu filtre pe dată (lună, trimestru, an), partener, jurnal și cont; arată **Balance**, **Payment Days** și **Plain payment days**.
- Media la gruparea rândurilor este ponderată: `sum(sumă × zile) / sum(sumă)`, pentru a evita distorsiunile din sume mici.
- Calculul pornește de la `full_reconcile_id` al liniei și de la data liniei de contrapartidă; valorile se actualizează automat la reconciliere și dereconciliere, fără acțiuni manuale.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move.line`: câmpurile Payment Date, Payment Days și Plain Payment Days.
- `account.average.payment.report`: raportul de analiză (pivot și grafic).

**Vizualizări**

- `views/account_view.xml` și `report/account_average_payment_view.xml`: câmpurile pe linia contabilă și vizualizările raportului.

#### 5. Conexiuni

- `account`: sursa facturilor și plăților pe baza cărora se calculează perioadele medii.
