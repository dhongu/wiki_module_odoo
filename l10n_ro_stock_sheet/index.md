# Romania - Fișă de Magazie și Balanță Stocuri (localizat la `l10n_ro_stock_sheet/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_sheet`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_sheet`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_sheet`
- **Ultima Ingestie:** `2026-06-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce în Odoo 19 două rapoarte clasice de stoc cerute în România — **fișa de magazie** (formularul 14-3-8) și **balanța analitică a stocurilor** — implementate ca rapoarte native Enterprise (`account.report`), în același stil cu celelalte rapoarte din suita `l10n_ro_ent`. Rolul lor este să arate, pentru o perioadă aleasă, situația cantitativă și valorică a articolelor (stoc inițial, intrări, ieșiri, stoc final) și, în plus, să compare valoarea analitică a stocului cu soldul contabil al conturilor de stoc, semnalând diferențele. Valorizarea se citește direct de pe mișcările de stoc (`stock.move`), fără tabelul `stock.valuation.layer` eliminat în versiunea 19, ceea ce face raportul potrivit pentru deployment-urile pe valorizare nativă (cost standard sau CMP).

#### 2. Funcționalități Cheie

- Raport unic cu **trei niveluri** de detaliere: cont de stoc (clasa 3), produs și document (fișa de magazie desfășurată 14-3-8), cu drill-down de la sintetic la documentul individual.
- **Balanță analitică pe articol**: stoc inițial, intrări, ieșiri și stoc final, în cantitate și valoare, încadrate pe perioadă după data mișcării.
- **Fișa de magazie (14-3-8)**: desfășurare document-cu-document a fiecărei mișcări, cu stoc curent cumulat și linie de stoc inițial.
- **Reconciliere analitic ↔ sintetic**: coloanele „Sold sintetic" (din notele contabile) și „Diferență" arată unde valoarea analitică a stocului nu coincide cu soldul contului contabil — instrument de control, fără a genera note de ajustare.
- Tratarea corectă a intrărilor/ieșirilor: doar mișcările care traversează granița gestiunilor interne (recepții, livrări); transferurile intern↔intern sunt ignorate.
- Suport atât pentru valorizare **automată** (`real_time`), cât și **periodică** — contul de stoc se determină per mișcare (din nota contabilă a mișcării, cu fallback pe contul categoriei produsului).
- Acțiunea **„Înregistrări contabile"** pe liniile de cont și de produs deschide exact liniile `account.move.line` din care e calculat soldul sintetic, pentru audit.
- Filtre de **perioadă**, **multi-company**, pe **gestiuni/locații** și pe **produse**, plus export nativ **PDF / XLSX**.
- Acces din meniul **Inventar → Raportare → Fișă magazie / Balanță stocuri (RO)** și buton **Fișă de magazie** pe fișa produsului, care deschide raportul pre-filtrat pe produsul respectiv.

#### 3. Dependențe

- `account_reports`
- `stock_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.sheet.report.handler` (moștenește `account.report.custom.handler`): motorul raportului — construiește cele trei niveluri (cont de stoc / produs / document), citește cantitățile și valorile din `stock.move`, soldul sintetic din `account.move.line` și calculează coloanele de reconciliere și acțiunile de drill-down.
- `product.template` (extins): adaugă butonul / acțiunea care deschide raportul pre-filtrat pe produsul respectiv.
- `res.company` (extins): suport pentru contextul de companie folosit la determinarea conturilor și a soldurilor sintetice.

**Vizualizări**

- `l10n_ro_stock_sheet_report` (`account.report`): definiția raportului — coloanele cantitative/valorice (inițial, intrări, ieșiri, final), coloanele „Sold sintetic" și „Diferență", linia rădăcină și expresiile aferente.
- `action_l10n_ro_stock_sheet` (`ir.actions.client`): acțiunea client care afișează raportul.
- `menu_l10n_ro_stock_sheet` (`menuitem`): intrarea de meniu în Inventar → Raportare.
- `product_views.xml`: extinderea fișei produsului cu butonul „Fișă de magazie".
- `static/src/stock_sheet_filters.xml`: șablonul de filtre suplimentare (gestiuni/locații, produse) injectat în bara raportului.

#### 5. Conexiuni

- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): postează nota de corecție CMP perpetuu vs. periodic; raportul de față doar semnalează diferențele, regularizarea recurentă se face acolo.
- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md): postează nota coeficient K (diferențe de preț, conturi 348/378), complementar reconcilierii din acest raport.
- `l10n_ro_stock_account`: alternativa OCA pentru valorizare FIFO pe loturi; acest modul este varianta pentru valorizarea nativă Odoo 19, fără dependența de stack-ul OCA.
