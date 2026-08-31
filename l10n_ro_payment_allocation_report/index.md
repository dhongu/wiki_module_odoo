# Alocarea Plăților pe Facturi (RO)

- **Nume Tehnic:** `l10n_ro_payment_allocation_report`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payment_allocation_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payment_allocation_report`
- **Ultima Ingestie:** `2026-08-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul răspunde la o întrebare pe care contabilitatea o pune la fiecare verificare de sold: din ce se compune suma plătită printr-un ordin de plată? Cazul tipic este furnizorul care a emis o factură și un storno, iar prin bancă se achită doar diferența — din extras se vede o singură sumă, nu documentele care au produs-o. Rapoartele standard (*Partner Ledger*, *Aged Payable/Receivable*) listează plățile și facturile una lângă alta, dar niciodată **alocarea** dintre ele. Modulul adaugă două rapoarte native `account.report` care arată legătura în ambele sensuri: de la plată spre facturile pe care le stinge și de la factură spre documentele care au închis-o. Este exclusiv de citire — nu generează și nu modifică note contabile.

#### 2. Funcționalități Cheie

- **Alocarea plăților** (*Payment Allocation*) — grupare pe documentul care stinge: plata cu valoarea, suma alocată în perioadă și restul nealocat; sub ea, fiecare factură închisă cu suma alocată și restul neachitat; sub factură, **celelalte** alocări ale ei (note de credit, avansuri, plăți anterioare), fără de care suma nu se închide.
- **Stingerea facturilor** (*Invoice Settlement*) — aceleași alocări grupate invers, pornind de la factură.
- **Sursa de date este `account.partial.reconcile`, nu `account.payment`** — acoperă toate modurile de stingere folosite în practică: note contabile reconciliate din extrasul bancar, registru de casă, note de credit, compensări. În majoritatea instalărilor românești plățile de furnizor sunt note contabile, nu înregistrări `account.payment`, iar un raport construit pe `account.payment` le-ar rata aproape complet.
- **Până la patru secțiuni cu subtotaluri separate**, fiecare afișată doar dacă are conținut: *Plăți către furnizori* (401), *Încasări de la clienți* (4111), *Alte stingeri* (note de credit, compensări) și *Reconcilieri fără factură* (mecanica POS, stingeri între note contabile). Plățile și încasările stau separat pentru că au sens contrar în trezorerie — un subtotal comun nu s-ar putea confrunta cu rulajul unui extras. Încadrarea ca trezorerie se face după **tipul jurnalului** (bancă/casă), iar sensul după contul de terți.
- **Câte un total per flux** — *Total plăți către furnizori* (confruntabil cu rulajul creditor al trezoreriei), *Total încasări de la clienți* (cu cel debitor) și *Total stins (toate secțiunile de mai sus)*.
- Filtre native: perioadă (implicit luna curentă), jurnale (aplicate documentului de la primul nivel), parteneri, creanțe/datorii (`filter_account_type`), selector multi-companie, unfold all. Filtrele de comparație și de ciorne sunt dezactivate intenționat — alocările există numai între note postate, iar coloanele de comparație ar repeta aceleași valori.
- Meniurile declară explicit grupurile de acces la rapoartele contabile (`account.group_account_readonly` / `account.group_account_basic`). Raportul citește prin interogări directe, deci nu aplică reguli de acces la nivel de înregistrare pe notele contabile.
- Drill-down la orice document și export PDF/XLSX din bara de instrumente, moștenite din framework-ul de raportare Enterprise.
- Interfață tradusă integral în română (`i18n/ro.po`).

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.payment.allocation.report.handler` (`account.report.custom.handler`): motorul raportului. Citește reconcilierile parțiale din perioadă, stabilește pentru fiecare alocare care latură **stinge** și care este **stinsă**, grupează pe document și construiește ierarhia pe patru niveluri (secțiune → document de stingere → factură → celelalte alocări ale facturii). Pe nivelul al treilea, *Dată* și *Valoare document* sunt ale documentului, nu ale alocării.
- `l10n.ro.invoice.settlement.report.handler`: moștenește handlerul de mai sus și inversează rolurile (`_pa_group_by_settlement = False`), pentru raportul care pornește de la factură.

Determinarea rolurilor se face prin scor: o factură este întotdeauna ținta, o linie din jurnal de bancă sau de casă este întotdeauna plata, iar o nota de credit se clasează între cele două (stinge o factură, dar poate fi ea însăși stinsă de o plată). La egalitate — de pildă o compensare între două note contabile — documentul mai recent stinge pe cel mai vechi.

**Vizualizări**

Modulul nu definește vizualizări proprii; interfața este produsă de framework-ul `account.report`.

- `l10n_ro_payment_allocation_report` (`account.report`): definiția raportului direct, cu cele cinci coloane — Dată, Partener, Valoare document, Alocat, Sold restant.
- `l10n_ro_invoice_settlement_report` (`account.report`): definiția raportului invers, cu aceleași coloane.
- `action_l10n_ro_payment_allocation_report`, `action_l10n_ro_invoice_settlement_report` (`ir.actions.client`, tag `account_report`).
- Meniuri sub **Contabilitate → Raportare → Rapoarte parteneri**: *Alocarea plăților* și *Stingerea facturilor*.

**Acțiuni Automate / Acțiuni Server**

Niciuna — raportul se calculează la deschidere, nu are cron-uri și nu scrie nimic în bază.

#### 5. Conexiuni

- [l10n_ro_balance_confirmation](../l10n_ro_balance_confirmation/index.md): confirmarea soldurilor cu partenerii — raportul explică din ce se compune soldul confirmat.
- [l10n_ro_account_fisa_cont](../l10n_ro_account_fisa_cont/index.md): fișa de cont arată mișcările pe cont; alocarea plăților arată legătura dintre ele.
- [l10n_ro_registru_jurnal](../l10n_ro_registru_jurnal/index.md): alt raport nativ `account.report` din suită, construit pe același pattern (`account.report.custom.handler`).
- [l10n_ro_journal_reports](../l10n_ro_journal_reports/index.md): rapoarte de jurnal cu cont corespondent.
- [l10n_ro_payment_instruments](../l10n_ro_payment_instruments/index.md): cecuri și bilete la ordin — stingerile prin instrumente de plată apar în raport ca orice altă alocare.
- [l10n_ro_stock_sheet](../l10n_ro_stock_sheet/index.md): model de raport pe trei niveluri cu reconciliere, din aceeași familie de instrumente de verificare.
- `account_reports`: framework-ul Enterprise de raportare (dependență).
