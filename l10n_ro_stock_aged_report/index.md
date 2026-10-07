# Romania - Stock Aged Report (localizat la `l10n_ro_stock_aged_report/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_aged_report`
- **Fost nume tehnic:** `l10n_ro_stock_age_report` (redenumit pe 07.10.2026)
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_aged_report
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_aged_report`
- **Ultima Ingestie:** `2026-10-07`

#### 1. Sumar

Modulul oferă un raport de vechime a stocului (Stock Aged Report) pentru localizarea românească. Urmărește ultima dată de intrare și ultima dată de ieșire pe fiecare quant de stoc, astfel încât marfa care stagnează în depozit să poată fi identificată și evaluată contabil, pe intervale de vechime configurabile.

**Redenumire.** Modulul s-a numit anterior `l10n_ro_stock_age_report`. Numele tehnic vechi este ocupat pe Odoo Apps de alt publicator (modulul provine din `NextERP-Romania/addons_extern`), așa că modulul a fost redenumit pe 07.10.2026 în `l10n_ro_stock_aged_report` (dhongu/l10n-romania#608 pe 19.0, #609 pe 18.0). Cine caută după `l10n_ro_stock_age_report` ajunge la această pagină. Modelele (`l10n.ro.stock.age.report`), câmpurile și funcționalitatea au rămas neschimbate.

#### 2. Funcționalități Cheie

- **Data ultimei intrări / ieșiri pe quant:** câmpurile `l10n_ro_last_in_date` și `l10n_ro_last_out_date` pe `stock.quant` se actualizează automat când cantitatea crește, respectiv scade.
- **Wizard de raport:** din **Inventar → Raportare → Raport vechime stoc** se alege depozitul (sau locațiile), data de referință și intervalul de vechime (15, 30, 90, 180, 365 de zile).
- **Defalcare pe intervale:** cantitatea și valoarea stocului sunt împărțite pe tranșe de vechime (de ex. [1] 0-15 zile, [2] 15-30 zile etc.).
- **Cont contabil:** fiecare linie arată contul de evaluare a stocului; se folosește contul de pe produs dacă există câmpul OCA `l10n_ro_property_stock_valuation_account_id` (citit defensiv), altfel contul de pe categoria produsului.
- **Analiză:** rezultatul se deschide în vizualizare pivot și listă.
- **Date istorice la instalare:** `post_init_hook` completează datele goale pe quant-urile existente din ultimele mișcări de stoc efectuate.
- **Migrare automată de la numele vechi:** la instalare, `pre_init_hook` preia înregistrările modulului vechi `l10n_ro_stock_age_report`, dacă este instalat, prin aceiași pași ca `merge_module` din upgrade-util (fără dependență externă). Câmpurile, vizualizările, acțiunile și meniurile sunt mutate pe noul nume, dependențele altor module sunt redirecționate, iar modulul vechi este scos din lista de module. Datele de intrare/ieșire deja calculate pe quant-uri se păstrează.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

- `stock.quant` (extins): `l10n_ro_last_in_date`, `l10n_ro_last_out_date`, actualizate în `create` / `write` după variația cantității.
- `l10n.ro.stock.age.report`: wizardul (companie, depozit, locații, dată de referință, interval); `do_compute_report` generează liniile, `button_show_sheet` deschide analiza.
- `l10n.ro.stock.age.report.location`: locațiile incluse în raport.
- `l10n.ro.stock.age.report.line`: liniile raportului (interval, produs, cont, cantitate, valoare, data ultimei ieșiri).
- `pre_init_hook`: preia înregistrările modulului vechi `l10n_ro_stock_age_report` (vezi mai sus).
- `post_init_hook`: completează retroactiv datele de intrare/ieșire pe quant-uri.

#### 5. Conexiuni

- [l10n_ro_stock_provision](../l10n_ro_stock_provision/index.md): folosește opțional `l10n_ro_last_in_date` (detectat la runtime) pentru pragul de slow-moving la provizioanele de depreciere a stocurilor.
- `terrabit_datus` (proiect client datus): depinde de acest modul.
