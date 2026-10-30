# MRP BoM Alternative Components (localizat la `deltatech_mrp_bom_alternative/index.md`)

- **Nume Tehnic:** `deltatech_mrp_bom_alternative`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_bom_alternative
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_bom_alternative`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite definirea de componente alternative pe liniile listei de materiale și folosirea lor în comenzile de producție atunci când componenta originală lipsește din stoc, fie manual, fie automat, în ordinea aleasă de tehnolog. Producția nu mai rămâne blocată din cauza unei singure componente lipsă, iar fiecare înlocuire rămâne documentată și trasabilă.

#### 2. Funcționalități Cheie

- **Alternative pe linia listei de materiale**, fiecare cu propria cantitate și unitate de măsură (de exemplu 1 kg de rășină înlocuit cu 1.200 g din altă rășină). Se definesc din butonul de schimb (alternative) de pe linia componentei și pot fi revăzute în **Manufacturing > Products > BoM Alternatives**.
- **Prioritate și perioadă de valabilitate** pentru fiecare alternativă, plus o notă; ordinea rândurilor este ordinea de preferință, utilă pentru înlocuiri temporare sau componente scoase din uz la o dată dată.
- **Politică de substituire pe linie:** *Manual* (alternativa se alege pe comandă) sau *Automatic* (lipsa se acoperă singură din alternativele aflate în stoc).
- **Substituire automată** la confirmarea comenzii și, opțional, la fiecare **Check Availability**; se folosește întâi stocul componentei originale.
- **Substituire parțială:** o componentă poate fi împărțită între originală și una sau mai multe alternative; dezactivată, o alternativă se folosește doar dacă acoperă singură toată lipsa. Ambele setări (*Partial Substitution*, *Substitute on Availability Check*, bifate implicit) sunt pe companie, în **Manufacturing > Configuration > Settings**, secțiunea *Operations*.
- **Buton Substitute** pe componentele comenzii de producție, cu fereastră care arată stocul liber și previzionat al originalei și al fiecărei alternative, plus cantitatea convertită.
- **Fără avertizări false de consum:** consumul așteptat urmează substituirea, deci *Produce All* nu cere confirmarea unui consum diferit de rețetă.
- **Trasabilitate:** mișcarea de stoc păstrează componenta înlocuită, regula folosită și tipul substituirii; raportul *Component Substitutions* arată ce s-a consumat în locul a ce. Alternativele se creează doar de **Manufacturing / Administrator**; modulul nu generează note contabile proprii.

Fluxul pas-cu-pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.bom.line.alternative`: alternativă a unei linii de listă de materiale (produs, cantitate, unitate, prioritate, valabilitate, notă).
- `mrp.bom.line` (extins): câmpul `alternative_policy` (Manual/Automatic) și legătura către alternative.
- `mrp.production` (extins): aplică substituirea automată la `action_confirm` și `action_assign` și ajustează verificarea consumului.
- `stock.move` (extins): `bom_line_alternative_id`, `original_product_id`, `substitution_reason`; logica de înlocuire a mișcării.
- `res.company` / `res.config.settings` (extinse): `mrp_alternative_partial`, `mrp_alternative_on_assign`.
- `mrp.bom.alternative.substitute` (wizard): substituirea manuală a unei componente de pe comandă.

**Vizualizări**

- `mrp_bom_line_alternative_view_list` / `_view_search` / `mrp_bom_line_alternative_action`: lista alternativelor, meniul BoM Alternatives.
- `mrp_bom_form_view` și `mrp_bom_line_view_form_alternative`: coloana de politică și fereastra de alternative pe lista de materiale.
- `mrp_production_form_view`: butonul Substitute pe componentele comenzii.
- `mrp_bom_alternative_substitute_view_form`: fereastra Substitute Component.
- `stock_move_view_list_substitution`, `stock_move_view_search_substitution`, `stock_move_action_substitution`: raportul Component Substitutions (în Manufacturing > Reporting).
- `res_config_settings_view_form`: cele două setări pe companie.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server; substituirea automată rulează la confirmarea comenzii și la verificarea disponibilității.

#### 5. Conexiuni

- `mrp`: modulul extinde listele de materiale, comenzile de producție și mișcările de stoc ale acestuia.
