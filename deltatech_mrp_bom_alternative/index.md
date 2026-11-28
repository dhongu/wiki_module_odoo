# MRP BoM Alternative Components (localizat la `deltatech_mrp_bom_alternative/index.md`)

- **Nume Tehnic:** `deltatech_mrp_bom_alternative`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp_bom_alternative
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_bom_alternative`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Permite definirea de componente alternative pe liniile unei liste de materiale și folosirea lor în ordinele de fabricație atunci când componenta originală lipsește, manual sau automat, în ordinea aleasă de utilizator. Producția nu se oprește pentru un material lipsă, iar înlocuirile rămân trasabile.

#### 2. Funcționalități Cheie

- Alternative pe linia de BoM, fiecare cu cantitate și unitate proprie (1 kg de rășină = 1.200 g din altă rășină).
- Prioritate și perioadă de valabilitate pe fiecare alternativă, pentru înlocuiri temporare sau componente scoase din uz la o dată dată.
- Substituire automatică: linia de BoM setată pe *Automatic* acoperă lipsa din alternativele în stoc, la confirmare și la fiecare verificare a disponibilității.
- Substituire parțială: o componentă poate fi împărțită între produsul original (stocul lui se consumă primul) și una sau mai multe alternative; opțional doar alternative care acoperă întreaga lipsă.
- Buton de substituire pe componentele ordinului de fabricație, cu stocul liber și previzionat al originalului și al fiecărei alternative și cantitatea convertită.
- Fără avertismente false de consum: consumul așteptat urmează substituirea, deci *Produce All* nu cere confirmarea.
- Trasabilitate: fiecare mișcare substituită păstrează componenta înlocuită; raportul *Manufacturing > Reporting > Component Substitutions* arată ce s-a consumat în loc de ce.
- Configurare în *Manufacturing > Configuration > Settings*, secțiunea *Operations*: *Partial Substitution* și *Substitute on Availability Check* (ambele active implicit); alternativele pot fi revăzute în *Manufacturing > Products > BoM Alternatives*.

Pașii detaliați sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.bom.line.alternative`: alternativa unei linii de BoM (produs, cantitate, unitate, secvență, valabilitate de la/până la, notă).
- `mrp.bom.line` (extins): modul de substituire (manual/automat) și alternativele liniei.
- `mrp.production` și `stock.move` (extinse): logica de substituire și păstrarea componentei înlocuite.
- `mrp.bom.alternative.substitute` (wizard): dialogul de substituire manuală.
- `res.company` / `res.config.settings` (extinse): opțiunile de substituire parțială și de verificare la disponibilitate.

**Vizualizări**

- `mrp_bom_line_alternative_view_list` / `_search`, `mrp_bom_line_view_form_alternative`, `mrp_bom_form_view`: alternativele în BoM și în meniul dedicat.
- `mrp_production_form_view`, `mrp_bom_alternative_substitute_view_form`: butonul și dialogul de substituire pe ordinul de fabricație.
- `stock_move_view_list_substitution` / `_search_substitution`: raportul substituirilor.
- `res_config_settings_view_form`: setările.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; substituirea automatică rulează la confirmarea ordinului și la verificarea disponibilității.

#### 5. Conexiuni

- [deltatech_mrp_bom](../deltatech_mrp_bom/index.md): extensii ale listelor de materiale din aceeași suită (fără dependență în manifest).
