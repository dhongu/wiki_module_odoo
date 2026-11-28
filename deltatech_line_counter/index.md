# Module Line Counter (localizat la `deltatech_line_counter/index.md`)

- **Nume Tehnic:** `deltatech_line_counter`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_line_counter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_line_counter`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă un wizard în meniul de Administrare care numără liniile de cod ale modulelor Odoo instalate, alese de utilizator. Oferă o estimare rapidă a dimensiunii și complexității unui modul (evaluări tehnice, oferte de dezvoltare, audit), fără instrumente externe.

#### 2. Funcționalități Cheie

- Selectarea unuia sau mai multor module instalate pentru numărare.
- Numărarea liniilor ne-goale din fișierele `.py`, `.xml`, `.js`, `.css` și `.scss`; comentariile și docstring-urile sunt incluse în număr.
- Excluderea directorului `tests` din calcul; fișierele care nu pot fi citite ca UTF-8 sunt ignorate.
- Rezultat într-un tabel cu total pe modul și total general; valoarea este o estimare.
- Acces din meniul Administrare (**Line Counter**).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `line.counter.wizard` (tranzitoriu): reține modulele selectate și rezultatul numărătorii (câmp HTML); `action_count_lines()` parcurge directorul fiecărui modul și construiește tabelul.

**Vizualizări**

- `line.counter.wizard.form`: formularul wizard-ului, cu selecția modulelor, butonul **Count Lines** și rezultatul.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server`; doar acțiunea de fereastră și meniul `menu_line_counter_wizard` care deschid wizard-ul.

#### 5. Conexiuni

Nu au fost identificate module conexe; este un utilitar independent pentru dezvoltatori și consultanți.
