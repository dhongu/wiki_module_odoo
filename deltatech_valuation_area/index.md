# Deltatech Stock Valuation Area (localizat la `deltatech_valuation_area/index.md`)

- **Nume Tehnic:** `deltatech_valuation_area`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_valuation_area](https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_valuation_area)
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_valuation_area`
- **Ultima Ingestie:** `2026-07-31`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul introduce conceptul de **arie de evaluare a stocului** (inspirat din "Valuation Area" din SAP), permițând companiilor să organizeze evaluarea contabilă a stocului nu doar la nivel global, ci și pe depozite sau locații distincte. Practic, aria de evaluare determină automat pe ce jurnal contabil se înregistrează mișcările de stoc, oferind flexibilitate companiilor cu mai multe depozite sau gestiuni care trebuie ținute separat din punct de vedere contabil.

#### 2. Funcționalități Cheie

- Activare per companie a funcționalității de arii de evaluare (`use_valuation_area`)
- Definire arii de evaluare cu cod scurt, nume și jurnal contabil dedicat
- Asociere a ariei de evaluare la nivel de companie, depozit sau locație, cu prioritate configurabilă
- Propagare automată a ariei de evaluare pe liniile contabile (`account.move.line`) generate din mișcările de stoc
- Validare a caracterului obligatoriu al ariei de evaluare pentru produsele stocabile (dacă funcționalitatea e activată pe companie), prin metodă extensibilă
- Editare manuală a ariei pe linia contabilă, pentru corecții excepționale
- Constrângere: transferurile interne între locații cu arii de evaluare diferite nu sunt permise (sursa și destinația trebuie să aparțină aceleiași arii)

**Notă privind metoda de evaluare:** modulul este proiectat pentru metoda **AVCO (cost mediu ponderat)**; nu este compatibil cu produse configurate pe metoda **FIFO**, întrucât agregarea liniilor contabile per produs și arie pierde informația despre straturile individuale de cost necesare pentru FIFO.

#### 3. Dependențe

- `stock`
- `account`
- `stock_account`

#### 4. Componente Cheie

**Modele**

- `valuation.area`: modelul principal — cod, nume, companie și jurnal contabil de stoc asociat ariei.
- `res.company` (extins): câmpurile `use_valuation_area` (activare funcționalitate) și `valuation_area_id` (arie implicită la nivel de companie).
- `stock.warehouse` (extins): câmpul `valuation_area_id` (arie asociată depozitului).
- `stock.location` (extins): câmpul `valuation_area_id` (arie asociată locației, cu prioritate maximă în determinarea ariei).
- `stock.move` (extins): metoda `_get_valuation_area()` care determină aria pornind de la locația destinație, locația sursă, depozit sau, în lipsă, compania.
- `account.move.line` (extins): câmpul stocat `valuation_area_id` (calculat automat din mișcarea de stoc care a generat linia) și metoda de validare `_is_valuation_area_required`.

Logica de determinare a ariei, la generarea liniilor contabile dintr-o mișcare de stoc, urmează ordinea de prioritate: locația destinație (dacă e internă) → locația sursă (dacă e internă) → depozitul mișcării → compania (fallback implicit). Propagarea se face prin extinderea metodei `_prepare_account_move_line`, care injectează automat `valuation_area_id` pe fiecare linie contabilă generată din mișcările de stoc.

**Vizualizări**

- `action_valuation_area` / `valuation.area.tree` / `valuation.area.form`: listă și formular pentru configurarea ariilor de evaluare (cod, nume, companie, jurnal de stoc).
- `menu_valuation_area`: intrare de meniu sub **Inventar > Configurare** pentru ariile de evaluare.
- `res.config.settings.view.form.inherit.website` (moștenește `stock_account.res_config_settings_view_form`): activare `use_valuation_area` și selecție a ariei implicite din setările de Inventar.
- `view_location_form_valuation_area` (moștenește `stock.view_location_form`): câmp `valuation_area_id` pe formularul locației de stoc.
- `view_warehouse_form_valuation_area` / `view_warehouse_tree_valuation_area` (moștenesc vizualizările depozitului `stock.view_warehouse` / `stock.view_warehouse_tree`): câmp `valuation_area_id` pe depozit.
- `view_move_form` (moștenește `account.view_move_form`): coloană `valuation_area_id` (ascunsă implicit, opțională) pe liniile facturii/notei contabile.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; propagarea ariei de evaluare se face sincron, prin suprascrierea metodelor Python (`_prepare_account_move_line`, `_get_valuation_area`) la generarea liniilor contabile din mișcările de stoc.

#### 5. Conexiuni

- `stock_account`: modulul de evaluare standard Odoo pe care se bazează, extinzând ecranul de setări și logica de generare a liniilor contabile din mișcările de stoc.
- `stock`: furnizează modelele `stock.warehouse`, `stock.location` și `stock.move`, extinse pentru a purta/determina aria de evaluare.
- `account`: furnizează modelul `account.move.line`, pe care se stochează aria de evaluare determinată.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): consumă ariile de evaluare definite aici pentru a calcula evaluarea stocului pe arie și cont.
- [deltatech_obyc](../deltatech_obyc/index.md): folosește aria de evaluare ca dimensiune în matricea de reguli de determinare a conturilor.
