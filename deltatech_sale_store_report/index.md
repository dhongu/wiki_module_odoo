# Deltatech Sale from Store Z Report (localizat la `deltatech_sale_store_report/index.md`)

- **Nume Tehnic:** `deltatech_sale_store_report`
- **Versiune:** `19.0.1.1.0`
- **Cale:** [https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_store_report](https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_store_report)
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_store_report`
- **Ultima Ingestie:** `2026-07-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un raport zilnic al vânzărilor din magazin cu bon fiscal tipărit, gândit să fie
punctat cu raportul Z al casei de marcat (raportul fiscal de închidere zilnică). Pentru o zi sau
o perioadă și una sau mai multe case de marcat (jurnale de bonuri fiscale), raportul oferă atât o
verificare din interfață, cât și un raport PDF listat, cu toate totalurile necesare reconcilierii
zilnice sau lunare dintre Odoo și casele de marcat.

#### 2. Funcționalități Cheie

- Listarea documentelor (facturi, chitanțe, stornări) cu bon fiscal tipărit în intervalul selectat.
- Totaluri pe zile, pentru punctajul unei perioade întregi cu șirul de rapoarte Z zilnice.
- Totaluri pe cote de TVA, grupate exact cum le grupează fișierul trimis la casa de marcat (după
  prima taxă a fiecărei linii), pentru comparație cu grupele de TVA de pe raportul Z.
- Totaluri pe tip de plată (numerar, card, tichete de masă), grupate pe jurnalul de plată și codul
  ECR, pentru comparație cu totalurile pe tipuri de plată de pe raportul Z.
- Câmp de diferență (total bonuri − plăți asociate), evidențiat vizual când valoarea e nenulă,
  pentru a semnala rapid un bon neplatit integral sau o plată nelegată.
- Documentele sunt selectate după data facturii, deci raportul se potrivește cu raportul Z doar
  dacă bonurile fiscale sunt tipărite în aceeași zi cu data facturii.
- Raport PDF exportabil, cu aceleași secțiuni ca ecranul de rezultat (totaluri zilnice, bonuri,
  totaluri TVA, totaluri plăți).

#### 3. Dependențe

- [deltatech_sale_store](../deltatech_sale_store/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.store.z.report` (tranzitoriu): wizard-ul principal — parametrii raportului (interval de
  date, jurnale de bonuri fiscale, companie) și totalurile calculate (netaxat, TVA, total, plăți,
  diferență); metoda `do_compute()` interoghează facturile cu `receipt_print=True` și populează
  liniile de detaliu, iar `print_pdf()` generează raportul PDF.
- `sale.store.z.report.line` (tranzitoriu): o linie de detaliu per document (factură/bon/stornare)
  cu totalurile sale.
- `sale.store.z.report.day.line` (tranzitoriu): totaluri agregate pe zi (număr bonuri, netaxat,
  TVA, total).
- `sale.store.z.report.tax.line` (tranzitoriu): totaluri agregate pe cotă de TVA (bază, taxă,
  total), grupate după prima taxă a fiecărei linii de factură.
- `sale.store.z.report.payment.line` (tranzitoriu): totaluri agregate pe jurnal de plată și cod
  ECR.

**Vizualizări**

- `view_sale_store_z_report_form`: formularul de opțiuni al wizard-ului (interval de date, jurnale
  de bonuri fiscale).
- `view_sale_store_z_report_result_form`: formularul de rezultat, cu totalurile principale și patru
  file (Receipts, Daily Totals, Tax Totals, Payment Totals).
- Meniu `menu_sale_store_z_report`: acces din contabilitate (`account.menu_finance_entries`),
  restricționat la grupul `account.group_account_invoice`.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server` — modulul e declanșat manual, la
  cerere, din meniul de contabilitate.

#### 5. Conexiuni

- [deltatech_sale_store](../deltatech_sale_store/index.md): raportul citește direct câmpurile
  `fiscal_receipt` (jurnal) și `receipt_print` (factură) introduse de acest modul, pentru a
  identifica documentele cu bon fiscal tipărit.
- `account`: raportul se bazează pe `account.move` (facturi/bonuri/stornări), `account.journal` și
  `account.tax`, și se integrează în meniul de contabilitate.
