# Deltatech Line Counter (localizat la `deltatech_line_counter/index.md`)

- **Nume Tehnic:** `deltatech_line_counter`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_line_counter](https://github.com/dhongu/deltatech/tree/19.0/deltatech_line_counter)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_line_counter`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă un wizard simplu în meniul de Administrare care numără liniile de cod ale modulelor Odoo instalate, alese de utilizator. Este util pentru a estima rapid dimensiunea și complexitatea unui modul (de exemplu, la evaluări tehnice, oferte de dezvoltare sau audit de cod), fără a fi nevoie de instrumente externe.

#### 2. Funcționalități Cheie

- Selectarea unuia sau mai multor module instalate (widget many2many_tags) pentru numărare.
- Numărarea liniilor ne-goale din fișiere `.py`, `.xml`, `.js`, `.css` și `.scss`.
- Excluderea automată a directorului `tests` din calcul.
- Afișarea rezultatului într-un tabel HTML, cu total pe fiecare modul și un total general.
- Acces din meniul Setări → Tehnic/Administrare (`base.menu_administration`).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `line.counter.wizard` (model tranzitoriu): reține modulele selectate (`module_ids`, m2m către `ir.module.module`, filtrate pe `state = installed`) și rezultatul numărătorii (`result`, câmp HTML); metoda `action_count_lines()` parcurge directorul fiecărui modul cu `os.walk`, numără liniile ne-goale din fișierele relevante și construiește tabelul HTML de rezultat.

**Vizualizări**

- `view_line_counter_wizard_form`: formularul wizard-ului, cu selecția modulelor, butonul „Count Lines” și afișarea rezultatului (vizibil doar după calcul).

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul; există doar acțiunea de fereastră `action_line_counter_wizard` și meniul `menu_line_counter_wizard` (Setări → Administrare) care deschid wizard-ul.

#### 5. Conexiuni

Nu au fost identificate module conexe funcțional (dincolo de dependența `base`); modulul este un utilitar independent pentru dezvoltatori/consultanți.
