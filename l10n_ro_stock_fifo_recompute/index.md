# Romania - FIFO Valuation Recompute

- **Nume Tehnic:** `l10n_ro_stock_fifo_recompute`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_fifo_recompute
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_fifo_recompute`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Recalculează în ordine cronologică evaluarea FIFO pe locație a mișcărilor de stoc și corectează valorile greșite din trecut (ieșiri pe stoc negativ necompensat, operații cu dată în urmă, bug-uri reparate între timp), postând nota contabilă de corecție. Astfel soldul conturilor de stoc revine la valoarea reală a stocului.

#### 2. Funcționalități Cheie

- Mișcările efectuate ale fiecărui produs FIFO se parcurg cronologic, cu o coadă FIFO pe fiecare locație; recepțiile și livrările fără aviz se ordonează după data facturii.
- Se recalculează ieșirile, transferurile interne și retururile de la clienți; valoarea intrărilor din facturi și costuri de achiziție rămâne cea înregistrată.
- Ieșirea pe stoc negativ se evaluează la prețul intrărilor care o acoperă în aceeași locație; dacă nu există o astfel de intrare, valoarea rămâne și nu se creează cantitate negativă nouă.
- Diferențele sub un prag ales la rulare (implicit 0,05 lei pe mișcare) sunt tratate ca rotunjiri și nu se corectează.
- **Rularea de probă** (butonul Calculează) nu modifică nimic: arată pe fiecare mișcare valoarea actuală, cea corectă și diferența, plus un control pe fiecare cont de stoc.
- **Aplică** corectează valorile mișcărilor și postează o singură notă de corecție, la data aleasă, în jurnalul de stoc: ieșire din exercițiul curent pe conturile notei originale; ieșire din exercițiu închis pe 1174 (OMFP 1802/2014); transfer între gestiuni 371 destinație = 371 sursă.
- Meniu: *Contabilitate → Contabilitate → Închidere → Recalculare FIFO*; în wizard se aleg produsele/categoriile, data corecției, sfârșitul ultimului exercițiu închis și contul de exerciții închise.
- Limitări: costul produselor fabricate, produsele pe loturi și liniile cu proprietar terț nu se recalculează; o rulare aplicată nu se poate anula (nota se stornează manual).
- Recomandare: întâi recalcularea FIFO, apoi verificarea stoc–contabilitate pentru diferențele rămase. Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `l10n_ro_stock_account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.fifo.recompute`: rularea de recalculare (selecție, parametri, stare, nota de corecție).
- `l10n.ro.fifo.recompute.line`: diferența pe o mișcare (valoare actuală, corectă, conturi).
- `l10n.ro.fifo.recompute.check`: controlul pe fiecare cont de stoc.

**Vizualizări**

- `view_l10n_ro_fifo_recompute_form` / `view_l10n_ro_fifo_recompute_list`: formularul și lista recalculărilor.
- `view_l10n_ro_fifo_recompute_line_list` / `view_l10n_ro_fifo_recompute_line_search`: lista și căutarea diferențelor.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_fifo_recompute`, `action_l10n_ro_fifo_recompute_line`: acțiuni de fereastră; secvența `seq_l10n_ro_fifo_recompute` numerotează rulările. Nu există cron-uri.

#### 5. Conexiuni

- `l10n_ro_stock_account`: motorul FIFO pe locație ale cărui valori le corectează.
- `l10n_ro_stock_account_check`: verificarea stoc–contabilitate, de rulat după recalculare.
