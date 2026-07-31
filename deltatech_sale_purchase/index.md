# Sale Purchase (localizat la `deltatech_sale_purchase/index.md`)

- **Nume Tehnic:** `deltatech_sale_purchase`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_purchase`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_purchase`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul curăță automat comenzile de achiziție generate prin regulile de aprovizionare (procurement) atunci când oferta de vânzare care le-a declanșat este anulată. Astfel se evită liniile de achiziție „orfane" — comenzi de achiziție netrimise furnizorului, rămase în ciornă fără o comandă de vânzare corespunzătoare — și se păstrează sincronizarea între echipa de vânzări și cea de aprovizionare.

#### 2. Funcționalități Cheie

- La anularea unei oferte/comenzi de vânzare, elimină automat liniile de achiziție legate care se află încă în comenzi de achiziție în starea ciornă (draft).
- O comandă de achiziție deja confirmată (trimisă furnizorului) NU este atinsă — rămâne în sarcina cumpărătorului să decidă ce face cu ea.
- Previne acumularea de comenzi de achiziție ciornă fără corespondent activ în vânzări, menținând curat modulul de aprovizionare.

*Corecție față de `readme/DESCRIPTION.md`:* descrierea menționează și redimensionarea liniei de achiziție la scăderea cantității comandate în oferta de vânzare. În 19.0 acest comportament este acum tratat nativ de nucleul Odoo (nu mai există o suprascriere `_log_decrease_ordered_quantity` ca în versiunea 18.0) — testul `test_decrease_resizes_draft_purchase_line` din modul verifică explicit acest comportament al nucleului, ca gardă pentru cazul în care ar regresa. Modulul propriu-zis implementează astăzi doar comportamentul de anulare.

#### 3. Dependențe

- `sale_purchase`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): suprascrie `_action_cancel()` pentru a șterge liniile de achiziție generate (`order_line.move_ids.created_purchase_line_ids`) aflate încă în comenzi de achiziție ciornă, înainte de a continua fluxul standard de anulare.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`; logica rulează sincron, în cadrul metodei suprascrise `_action_cancel`.

#### 5. Conexiuni

- `sale_stock`: furnizează legătura dintre liniile de comandă de vânzare și mișcările de stoc (`move_ids`) din care se determină liniile de achiziție generate.
- `purchase_stock`: modulul standard care populează `created_purchase_line_ids` pe mișcările de stoc atunci când regulile de aprovizionare (MTO/Buy) generează o comandă de achiziție.
