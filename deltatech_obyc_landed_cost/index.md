# OBYC - Landed Cost Class 6 Routing

- **Nume Tehnic:** `deltatech_obyc_landed_cost`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/20.0/deltatech_obyc_landed_cost
- **Cale Locală:** odoo-addons/deltatech_stock_valuation/deltatech_obyc_landed_cost
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Completează modulul OBYC cu tratarea costurilor de achiziție suplimentare (landed costs). Contul de stoc al unui landed cost vine din regula OBYC `landed_cost`, iar modulul adaugă, per companie, posibilitatea de a trece creditul de clasa 6 printr-un cont intermediar tehnic și precompletează landed cost-ul creat dintr-o factură de furnizor.

#### 2. Funcționalități Cheie

- Setare per companie, în *Inventar → Configurare → Setări*, blocul **Valuation**: **Landed Cost Class 6 Method** cu valorile *Standard* (credit direct în clasa 6, comportamentul nativ Odoo) sau *Through intermediary account*.
- Cu metoda prin cont intermediar, nota contabilă devine Dr stoc / Cr intermediar și Dr intermediar / Cr 624, în loc de Dr stoc / Cr 624.
- Contul intermediar este un cont tehnic stabilit de politica contabilă a companiei, nu un cont de clasa 6 (validat prin constrângere).
- Butonul **Create Landed Costs** de pe factura de furnizor (cu o linie de produs marcat ca landed cost) creează landed cost-ul: recepțiile comenzilor de achiziție de pe factură, neacoperite încă de alt landed cost, sunt precompletate, iar contul fiecărei linii de cost se ia din linia facturii.
- Nu se redirecționează niciodată clasa 609, conturile din afara clasei 6 și debitul unui cost negativ.
- Regula OBYC **Landed Costs** (`landed_cost`) trebuie să aibă completat **Valuation Account**.
- Fluxul pas cu pas, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- [deltatech_obyc](../deltatech_obyc/index.md)
- `stock_landed_costs`
- `purchase_stock`
- `account`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): câmpurile `landed_cost_method` și `landed_cost_intermediary_account_id`, cu verificarea contului intermediar.
- `res.config.settings` (extins): expune cele două setări în Setări Inventar.
- `account.move` (extins): `button_create_landed_costs` pentru crearea landed cost-ului din factura de furnizor.
- `stock.valuation.adjustment.lines` (extins): `_create_account_move_line` și `_route_class6_through_intermediary` pentru rutarea creditului de clasa 6.

**Vizualizări**

- `res_config_settings_view_form`: blocul de setări pentru metoda de landed cost și contul intermediar.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): suita de valorizare a stocului în care se încadrează modulul.
