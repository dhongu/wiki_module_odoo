# OBYC - Landed Cost Class 6 Routing (localizat la `deltatech_obyc_landed_cost/index.md`)

- **Nume Tehnic:** `deltatech_obyc_landed_cost`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech_stock_valuation/tree/19.0/deltatech_obyc_landed_cost
- **Cale Locală:** `odoo-addons/deltatech_stock_valuation/deltatech_obyc_landed_cost`
- **Ultima Ingestie:** `2026-11-11`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul completează costurile adiționale (landed costs) pentru companiile care folosesc determinarea de conturi OBYC. Contul de stoc al costului adițional vine din regula OBYC `landed_cost`, iar la nivel de companie se poate activa, opțional, rutarea creditului în contul de cheltuieli (clasa 6) printr-un cont intermediar tehnic. În plus, costul adițional creat dintr-o factură de la furnizor este completat automat cu recepțiile și conturile potrivite.

#### 2. Funcționalități Cheie

- Contul de stoc al notei contabile a costului adițional se ia din regula OBYC `landed_cost` (nu mai depinde de un cont pe locație); regula trebuie să aibă completat contul de evaluare.
- Pe companie, în *Inventar → Configurare → Setări*, blocul **Evaluare**, se alege **metoda pentru creditul clasei 6**: *Standard* (comportamentul nativ Odoo: Dr stoc / Cr clasa 6) sau *Prin cont intermediar* (Dr stoc / Cr intermediar și Dr intermediar / Cr clasa 6, același efect net, într-o singură notă cu două perechi echilibrate).
- Contul intermediar este un cont tehnic ales de companie; nu poate fi din clasa 6 (validare la salvare) și se anulează la zero pe fiecare cost adițional.
- Nu se rutează niciodată: clasa 609, conturile din afara clasei 6 și debitul unui cost negativ.
- La crearea costului adițional dintr-o factură de la furnizor (butonul **Creați costuri adiționale**), se preiau recepțiile finalizate ale comenzilor de achiziție din factură care nu sunt deja acoperite de un alt cost adițional validat, iar fiecare linie de cost primește contul liniei corespunzătoare din factură (asociere una-la-una, deci două linii cu același produs își păstrează conturile).
- Fluxul complet pas-cu-pas este în fișa consultantului: configurarea (metoda, contul intermediar, regula OBYC), comanda de achiziție, recepția și nota ei, factura furnizorului de marfă, factura transportatorului cu butonul de costuri adiționale, costul adițional (recepția se adaugă în Transferuri dacă factura n-are comandă de achiziție), nota standard și nota prin cont intermediar.

#### 3. Dependențe

- [deltatech_obyc](../deltatech_obyc/index.md)
- `stock_landed_costs`
- `purchase_stock`
- `account`

#### 4. Componente Cheie

Conform fluxului de ingestie, Sumarul și Funcționalitățile provin din `readme/DESCRIPTION.md`, `USAGE.md` și fișa consultantului; modelele de mai jos sunt un reper tehnic scurt.

**Modele**

- `res.company` (extindere): câmpurile `landed_cost_method` (standard / prin cont intermediar) și `landed_cost_intermediary_account_id`, cu constrângere ca contul să nu fie din clasa 6.
- `res.config.settings` (extindere): expune cele două câmpuri în Setările Inventar.
- `stock.valuation.adjustment.lines` (extindere): `_create_account_move_line` împarte creditul clasei 6 (fără 609) în două perechi prin contul intermediar.
- `account.move` (extindere): `button_create_landed_costs` completează recepțiile și conturile costului adițional creat din factură.

**Vizualizări**

- `res_config_settings_view_form`: moștenește formularul de setări din `stock_account` și adaugă metoda și contul intermediar.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_obyc](../deltatech_obyc/index.md): furnizează regula OBYC `landed_cost` din care provine contul de stoc.
- [l10n_ro_stock_account_landed_cost_account](../l10n_ro_stock_account_landed_cost_account/index.md): modulul pe care îl înlocuiește pentru companiile care folosesc `deltatech_obyc` în loc de `l10n_ro_stock_account`.
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): stratul de evaluare care reconstruiește mișcările cantitativ-valorice din notele contabile generate.
