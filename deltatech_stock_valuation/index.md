# Product Valuation (localizat la `deltatech_stock_valuation/index.md`)

- **Nume Tehnic:** `deltatech_stock_valuation`
- **Versiune:** `19.0.0.0.7`
- **Cale:** [https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_stock_valuation](https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_stock_valuation)
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_stock_valuation`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează și urmărește evaluarea stocului de produse pe arie de evaluare și cont contabil, după modelul SAP Material Valuation (MBEW & MBEWH). Spre deosebire de mecanismul standard Odoo, care se bazează pe mișcările de stoc, evaluarea este derivată direct din notele contabile (`account.move.line`), garantând astfel consistență permanentă cu balanța contabilă — util în contexte cu ajustări contabile manuale sau cerințe de raportare pe centre de cost/depozite.

#### 2. Funcționalități Cheie

- Cost mediu ponderat (AVCO) calculat per produs, arie de evaluare și cont contabil
- Evaluare determinată din note contabile, nu din mișcările de stoc
- Istoric lunar al evaluărilor (`product.valuation.history`) pentru urmărirea evoluției în timp
- Conturi contabile dedicate — se marchează conturile utilizate la evaluarea stocului (`is_for_stock_valuation`)
- Validare inteligentă — aria de evaluare devine obligatorie pe liniile contabile doar pentru conturile marcate pentru evaluare stoc
- Configurare nivel arie de evaluare per companie (ex. nivel companie, depozit, locație)
- Recalculare manuală/în fundal a evaluărilor din interfața de configurare (proces în 7 pași, doar pentru administratori de sistem), plus un cron dedicat de reîmprospătare automată
- Opțiune per categorie de produs (`use_valuation_area_price`) pentru ca ieșirile de stoc să folosească prețul calculat din `product.valuation` în locul prețului standard/CMP global

> **Notă Odoo 19:** Modelul `stock.valuation.layer` a fost eliminat în Odoo 19; evaluarea standard se bazează acum pe `stock.move`. Modulul rămâne independent de această schimbare, deoarece folosește `account.move.line` ca sursă de adevăr.

> **Limitare:** Modulul suportă exclusiv metoda de evaluare **AVCO** (cost mediu ponderat). Nu este compatibil cu produsele configurate cu metoda **FIFO** — folosirea acesteia produce rezultate incorecte, deoarece FIFO necesită urmărirea straturilor individuale de cost, informație pierdută prin agregarea contabilă folosită de acest modul.

#### 3. Dependențe

- `stock_account`
- [deltatech_valuation_area](../deltatech_valuation_area/index.md)

#### 4. Componente Cheie

**Modele**

- `product.valuation`: evaluarea curentă a unui produs pe arie de evaluare, cont și companie (preț, cantitate, valoare).
- `product.valuation.history` (extinde `product.valuation`): istoricul lunar al evaluărilor (cantitate/valoare inițială, intrări, ieșiri, finală), unic pe combinația produs/arie/cont/companie/lună.
- `account.account` (extins): câmp nou `is_for_stock_valuation` pentru a marca conturile ce participă la evaluare.
- `account.move` (extins): metode `_get_valuation_keys` / `_recompute_valuation_keys` / `_recompute_valuation` pentru recalcul țintit al evaluării la postarea/anularea notelor de stoc.
- `account.move.line` (extins): punct de extensie pentru cerința ariei de evaluare pe conturile marcate.
- `product.category` (extins): câmp `use_valuation_area_price`, cu constrângere care blochează combinația cu metoda de cost FIFO.
- `product.product` / `product.template` (extinse): relația `product_valuation_ids` și metoda `recompute_valuation_amount()` pentru recalcul manual per produs.
- `res.company` (extins): câmpurile `valuation_area_level` (companie/depozit/locație) și `valuation_lot_level`, plus `set_stock_valuation_at_company_level()`.
- `res.config.settings` (extins): câmpuri și logică pentru urmărirea progresului recalculării în fundal (pași 1-7).
- `stock.move` (extins): `_get_valuation_area_price()` și suprascrierea `_set_value()` pentru a valoriza ieșirile de stoc la prețul din `product.valuation` când categoria are `use_valuation_area_price` activ.

**Vizualizări**

- `product_valuation_view_tree` / `product_valuation_view_form` / `product_valuation_view_pivot`: interfețele principale pentru `product.valuation`.
- `product_valuation_history_view_tree` / `product_valuation_history_view_form` / `product_valuation_history_view_pivot`: interfețele pentru istoricul lunar `product.valuation.history`.
- `product_valuation_action` / `product_valuation_history_action`: acțiuni de fereastră asociate, cu meniuri dedicate (`product_valuation_menu`, `product_valuation_history_menu`).
- `product_template_form_view`: adaugă evaluările produsului pe formularul de articol.
- `view_account_form`: adaugă bifa `is_for_stock_valuation` pe formularul contului contabil.
- `res_config_settings_view_form`: secțiunea de configurare a nivelului ariei de evaluare și a progresului recalculării.
- `product_category_form_view_inherit`: adaugă opțiunea `use_valuation_area_price` pe formularul categoriei de produs.

**Acțiuni Automate / Acțiuni Server**

- `action_product_valuation_history_recompute`: acțiune server care recalculează integral `product.valuation.history` și `product.valuation` (`recompute_all_amount()`), disponibilă manual din configurare.
- `product_valuation_recompute_amount_action` / `product_valuation_history_recompute_amount_action` / `product_template_recompute_amount_action`: acțiuni server suplimentare de recalcul, expuse la nivel de listă/formular.
- `ir_cron_auto_refresh_valuation`: cron (implicit inactiv, interval 2 minute) care rulează `model._auto_refresh_step()` pentru a avansa procesul de reîmprospătare în fundal (7 pași) al istoricului și evaluării curente.

#### 5. Conexiuni

- `stock_account`: mecanismul standard Odoo de evaluare a stocului, față de care acest modul adaugă un strat suplimentar de raportare sincronizat cu contabilitatea.
- [deltatech_valuation_area](../deltatech_valuation_area/index.md): definește ariile de evaluare (`valuation.area`) și liniile de notă contabile pe care se bazează calculul din acest modul.
- [deltatech_obyc](../deltatech_obyc/index.md): determină conturile de stoc pe care se generează notele contabile reconstruite de acest modul.
- [deltatech_valuation_report](../deltatech_valuation_report/index.md): raport de verificare care compară evaluarea calculată aici cu soldul conturilor de stoc.
