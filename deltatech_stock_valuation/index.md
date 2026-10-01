# Product Valuation (localizat la `deltatech_stock_valuation/index.md`)

- **Nume Tehnic:** `deltatech_stock_valuation`
- **Versiune:** `20.0.0.0.11`
- **Cale:** [https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_stock_valuation](https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_stock_valuation)
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_stock_valuation`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează și urmărește evaluarea stocului de produse pe arie de evaluare și cont contabil, după modelul SAP Material Valuation (MBEW & MBEWH). Spre deosebire de mecanismul standard Odoo, care se bazează pe mișcările de stoc, evaluarea este derivată direct din notele contabile postate (`account.move.line`), ceea ce o ține consistentă cu balanța contabilă — util în contexte cu ajustări contabile manuale sau cerințe de raportare pe centre de cost/depozite. Modulul nu înlocuiește evaluarea standard din `stock_account`, ci adaugă un strat suplimentar de raportare și nu generează el însuși note contabile.

#### 2. Funcționalități Cheie

- Cost mediu ponderat (AVCO) calculat per produs, arie de evaluare și cont contabil, direct din notele contabile.
- Istoric lunar al evaluărilor (`product.valuation.history`): cantitate inițială, intrări, ieșiri, finală și valorile aferente.
- Conturi contabile dedicate: se bifează **Stock Valuation** (`is_for_stock_valuation`) pe contul de stoc; la salvarea setărilor, conturile de stoc ale categoriilor de produse sunt marcate automat.
- Aria de evaluare este obligatorie pe orice linie contabilă cu produs stocabil (regulă din `deltatech_valuation_area`) și se completează automat cu aria companiei.
- La postarea, de-postarea, schimbarea datei sau ștergerea unei note, istoricul și evaluarea curentă se recalculează țintit pentru combinațiile afectate.
- Convenție de cantitate semnată pe notele de tip `entry`: pozitivă pe debit (intrare), negativă pe credit (ieșire); la notele manuale de stoc cantitatea se introduce cu semn.
- Opțiunea **Use Valuation Area Price** pe categoria de produs (doar AVCO): ieșirile din locații interne se valorizează la prețul din **Product Valuation** al ariei și contului, nu la costul standard; fără evaluare sau cu preț zero se folosește costul mediu, cu avertisment în log.
- Odoo 20: valoarea mișcărilor de ieșire este negativă. Setarea **Keep move value on retroactive recompute** (bifată implicit, vine din `deltatech_valuation_area`) păstrează prețul unitar al ieșirilor valorizate la prețul ariei după o corecție retroactivă (dată schimbată, cantitate editată, intrare revalorizată); debifată, recalcularea standard le rescrie la costul mediu global, fără a corecta notele contabile deja postate.
- Configurare **Valuation Area Level** per companie (singurul nivel suportat de recalcularea completă este Company); setările se salvează per companie și necesită grupul de administrator de sistem.
- Recalculare completă în fundal din **Inventar → Configurare → Setări → Evaluare → Recompute All (Background)**, cu indicator de progres; alternativ, acțiunea server **Recompute All Stock Valuation** (administrator de sistem) și un cron dedicat, implicit inactiv. Necesară la prima instalare sau după import de date.
- Recomandare pentru companiile românești: instalarea împreună cu `deltatech_obyc`, astfel încât notele de stoc să se posteze la validarea recepției/livrării, nu doar la facturare. Categoriile trebuie să aibă metoda **AVCO** și **Inventory Valuation** = Perpetual (at invoicing).
- Detaliile pas cu pas (configurare, utilizare, erori frecvente) sunt în [Fișa consultantului](FISA_CONSULTANT.md).

> **Limitare:** Modulul suportă exclusiv metoda de evaluare **AVCO**. Nu este compatibil cu produsele FIFO — FIFO necesită straturi individuale de cost, informație pierdută prin agregarea contabilă folosită aici; opțiunea **Use Valuation Area Price** este refuzată pe categoriile FIFO.

#### 3. Dependențe

- `stock_account`
- [deltatech_valuation_area](../deltatech_valuation_area/index.md)

#### 4. Componente Cheie

**Modele**

- `product.valuation`: evaluarea curentă a unui produs pe arie de evaluare, cont și companie (preț, cantitate, valoare).
- `product.valuation.history` (extinde `product.valuation`): istoricul lunar al evaluărilor, unic pe combinația produs/arie/cont/companie/lună; conține și logica recalculării în pași (în fundal).
- `account.account` (extins): câmpul `is_for_stock_valuation`.
- `account.move` (extins): recalcul țintit al evaluării la postarea/anularea/modificarea notelor.
- `account.move.line` (extins): punct de extensie pentru cerința ariei de evaluare.
- `product.category` (extins): câmpul `use_valuation_area_price`, cu constrângere față de metoda FIFO.
- `product.product` / `product.template` (extinse): relația `product_valuation_ids` și recalcul manual per produs.
- `res.company` (extins): `valuation_area_level`, `valuation_lot_level` și `set_stock_valuation_at_company_level()`.
- `res.config.settings` (extins): setările de evaluare și urmărirea progresului recalculării.
- `stock.move` (extins): `_get_valuation_area_price()` și suprascrierea `_set_value()` pentru valorizarea ieșirilor la prețul ariei, inclusiv păstrarea valorii la recalculări retroactive.
- `stock.move.line` (extins): suprascrie `write` pentru corecțiile de cantitate pe mișcări efectuate.

**Vizualizări**

- `product_valuation_view_tree` / `product_valuation_view_form` / `product_valuation_view_pivot`: interfețele pentru `product.valuation`.
- `product_valuation_history_view_tree` / `product_valuation_history_view_form` / `product_valuation_history_view_pivot`: interfețele pentru istoricul lunar.
- `product_valuation_action` / `product_valuation_history_action`: acțiunile de fereastră, cu meniuri dedicate.
- `product_template_form_view`: evaluările produsului pe formularul de articol.
- `view_account_form`: bifa `is_for_stock_valuation` pe contul contabil.
- `res_config_settings_view_form`: secțiunea de evaluare din setările Inventarului și progresul recalculării.
- `product_category_form_view_inherit`: opțiunea `use_valuation_area_price` pe categoria de produs.

**Acțiuni Automate / Acțiuni Server**

- `action_product_valuation_history_recompute`: acțiune server (administrator de sistem) care recalculează integral istoricul și evaluarea curentă.
- `product_valuation_recompute_amount_action` / `product_valuation_history_recompute_amount_action` / `product_template_recompute_amount_action`: acțiuni server de recalcul la nivel de listă/formular.
- `ir_cron_auto_refresh_valuation`: cron „Auto Refresh Stock Valuation” (implicit inactiv, la 2 minute) care rulează `_auto_refresh_step()` pentru avansarea reîmprospătării în fundal.

#### 5. Conexiuni

- `stock_account`: evaluarea standard Odoo, față de care modulul adaugă un strat de raportare sincronizat cu contabilitatea.
- [deltatech_valuation_area](../deltatech_valuation_area/index.md): definește ariile de evaluare și setarea de păstrare a valorii mișcărilor.
- [deltatech_obyc](../deltatech_obyc/index.md): determină conturile de stoc și postează notele la validarea recepției/livrării (recomandat în România).
- [deltatech_valuation_report](../deltatech_valuation_report/index.md): raport de verificare care compară evaluarea calculată aici cu soldul conturilor de stoc.
