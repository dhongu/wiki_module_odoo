# Deltatech Stock Valuation Area (localizat la `deltatech_valuation_area/index.md`)

- **Nume Tehnic:** `deltatech_valuation_area`
- **Versiune:** `20.0.1.0.5`
- **Cale:** [https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_valuation_area](https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_valuation_area)
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_valuation_area`
- **Ultima Ingestie:** `2026-10-01`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul introduce conceptul de **arie de evaluare a stocului** (inspirat din "Valuation Area" din SAP), permițând companiilor să organizeze evaluarea contabilă a stocului nu doar la nivel global, ci și pe depozite sau locații distincte. Aria de evaluare se stabilește pe companie, depozit sau locație și se scrie automat pe liniile contabile generate din mișcările de stoc, oferind o bază unică pentru evaluarea și raportarea pe gestiune. Folosit singur, modulul doar etichetează liniile contabile; rapoartele valorice vin din modulele care îl consumă.

#### 2. Funcționalități Cheie

- Activare per companie a funcționalității de arii de evaluare (`use_valuation_area`), din **Inventar > Configurare > Setări** (secțiunea de evaluare a stocului), fără impact asupra celorlalte companii din bază
- Definire arii de evaluare cu cod scurt (afișat ca `[COD] Nume`), nume, companie și jurnal de stoc dedicat (jurnal de tip *Diverse*), din **Inventar > Configurare > Arii de evaluare** (scriere doar pentru managerul contabil)
- Asociere a ariei la nivel de companie (implicită), depozit sau locație
- Determinarea ariei la o mișcare de stoc, în ordinea: locația destinație internă (aria proprie sau a depozitului locației) → locația sursă internă → depozitul de aprovizionare al mișcării → compania; depozitul se deduce din locație, deci ajustările de inventar și transferurile manuale iau aria depozitului chiar dacă locația nu are arie proprie
- Propagare automată a ariei, a cantității semnate (pozitivă pe debit, negativă pe credit) și a UM pe liniile contabile generate din mișcările de stoc
- Arie obligatorie pe liniile cu produse stocabile (dacă funcționalitatea e activată pe companie), prin metodă extensibilă; editare manuală a ariei pe linia contabilă, pentru corecții excepționale
- Constrângere: transferurile interne între locații cu arii diferite sunt blocate la validarea mișcării (inclusiv pe liniile ei, ex. putaway pe o sublocație), indiferent dacă se generează sau nu notă contabilă; ruta prin locație de tranzit nu e o trecere validată între arii
- Setare specifică Odoo 20: **Păstrează valoarea mișcării la recalcularea retroactivă** (`valuation_keep_move_value`, implicit activă) — valoarea mișcărilor deja validate rămâne cea de la validare, coerentă cu notele contabile postate; dacă e dezactivată, recalcularea standard Odoo 20 rescrie valoarea ieșirilor ulterioare, iar notele postate nu se corectează, deci stocul și contabilitatea pot diverge
- Inversarea unei note de stoc (cu sau fără storno) anulează corect și cantitatea de pe linie (din 20.0.1.0.5)
- Coloane opționale pe notele contabile manuale: Produs, Cantitate, UM și Arie de evaluare; pe lista generală de elemente de jurnal: Cantitate și Arie de evaluare
- Fluxul detaliat pas-cu-pas, baza legală și reconcilierea pe arie sunt în [Fișa Consultant](FISA_CONSULTANT.md)

**Notă privind metoda de evaluare:** modulul este proiectat pentru metoda **AVCO (cost mediu ponderat)**; nu este compatibil cu produse configurate pe **FIFO**, întrucât agregarea liniilor contabile per produs și arie pierde informația despre straturile individuale de cost.

#### 3. Dependențe

- `stock`
- `account`
- `stock_account`

#### 4. Componente Cheie

**Modele**

- `valuation.area`: modelul principal — cod, nume, companie și jurnal de stoc asociat ariei.
- `res.company` (extins): `use_valuation_area` (activare), `valuation_area_id` (arie implicită) și `valuation_keep_move_value` (păstrarea valorii mișcării la recalcularea retroactivă).
- `res.config.settings` (extins): câmpuri related către cele de pe companie.
- `stock.warehouse` (extins): `valuation_area_id` (arie per depozit).
- `stock.location` (extins): `valuation_area_id` și metoda `_get_valuation_area()` (aria proprie, altfel cea a depozitului locației).
- `stock.move` (extins): `_get_valuation_area()` (determinarea ariei), `_check_internal_move_valuation_area()` (apelată din `_action_done`) și `_get_account_move_line_vals()` (injectează aria, cantitatea semnată și UM pe liniile contabile).
- `account.move.line` (extins): câmpul stocat `valuation_area_id` (calculat, editabil), constrângerea `_check_valuation_area`, metoda `_is_valuation_area_required` și inversarea cantității la reversul notelor de stoc.

**Vizualizări**

- `view_valuation_area_tree` / `view_valuation_area_form` / `action_valuation_area`: listă, formular și acțiune pentru ariile de evaluare.
- Meniu sub **Inventar > Configurare** pentru arii de evaluare (`menu_views.xml`).
- `res_config_settings_view_form` (moștenește `stock_account.res_config_settings_view_form`): activare, arie implicită și opțiunea de păstrare a valorii mișcării.
- `view_location_form_valuation_area` (moștenește `stock.view_location_form`): câmp pe locație.
- `view_warehouse_form_valuation_area` / `view_warehouse_tree_valuation_area` (moștenesc `stock.view_warehouse` / `stock.view_warehouse_tree`): câmp pe depozit.
- `view_move_form` (moștenește `account.view_move_form`): coloane opționale pe liniile notei contabile.
- `view_move_line_tree` (moștenește `account.view_move_line_tree`): coloane opționale Cantitate și Arie de evaluare.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; propagarea ariei se face sincron, prin suprascrierea metodelor Python la generarea liniilor contabile. Accesul este definit în `security/ir.access.csv` (manager contabil: CRUD; utilizatori interni: citire).

#### 5. Conexiuni

- `stock_account`: modulul de evaluare standard Odoo pe care se bazează.
- `stock`: furnizează `stock.warehouse`, `stock.location` și `stock.move`, extinse pentru a determina aria.
- `account`: furnizează `account.move.line`, pe care se stochează aria.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): consumă ariile definite aici pentru evaluarea stocului pe arie și cont.
- [deltatech_obyc](../deltatech_obyc/index.md): folosește aria ca dimensiune în regulile de determinare a conturilor și jurnalului.
