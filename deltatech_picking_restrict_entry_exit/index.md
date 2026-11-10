# Picking Validation Restrict Entry Exit (localizat la `deltatech_picking_restrict_entry_exit/index.md`)

- **Nume Tehnic:** `deltatech_picking_restrict_entry_exit`
- **Versiune:** `19.0.0.0.15`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_restrict_entry_exit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_restrict_entry_exit`
- **Ultima Ingestie:** `2026-11-10`

#### 1. Sumar

Recepțiile și livrările trebuie să corespundă cu ce s-a comandat. Modulul împiedică utilizatorii din depozit să valideze o recepție sau o livrare care conține produse nelegate de o comandă de achiziție, respectiv de vânzare, sau cantități mai mari decât cererea (Demand), prevenind astfel mișcări de stoc fără document justificativ.

#### 2. Funcționalități Cheie

- **Recepții și livrări legate de o comandă**: la **Validate**, fiecare linie cu cantitate a unei recepții trebuie să provină dintr-o linie de comandă de achiziție, iar fiecare linie a unei livrări dintr-o linie de comandă de vânzare. Verificarea pentru recepții se aplică dacă este instalat Purchase (`purchase_stock`), cea pentru livrări dacă este instalat Sales (`sale_stock`).
- **Nicio cantitate peste cerere**: la **Validate**, o linie a cărei **Quantity** efectuată depășește **Demand** blochează validarea. Aceeași verificare rulează și la salvarea transferului după modificarea cantității unei linii.
- **Fără linii adăugate manual**: pe o recepție sau o livrare nu se poate salva o linie nouă cu cantitate efectuată; pe celelalte transferuri, o astfel de linie nu poate avea cantitate efectuată mai mare decât cererea.
- **Cazuri scutite**: retururile și back-order-urile nu sunt verificate la validare, nici transferurile interne între două locații ale aceluiași depozit.
- **Grupul „Picking create permission"** (`group_picking_restrict_entry_exit`): membrii sunt scutiți de verificările de la validare și pot adăuga linii pe recepții și livrări. La instalare în grup se află doar utilizatorii root și administrator; toți ceilalți sunt restricționați. Pentru a scuti alt utilizator, în modul dezvoltator: **Settings > Users & Companies > Groups** → **Picking create permission** → se adaugă utilizatorul.
- **Limitări**: crearea unei recepții sau livrări fără comandă-sursă nu este blocată, ci doar validarea ei; verificarea cantității efectuate la salvare se aplică tuturor utilizatorilor, inclusiv membrilor grupului de scutire, și retururilor/back-order-urilor.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md` (actualizat în 19.0.0.0.15 după cod); mai jos, o verificare punctuală a codului.

**Modele**

- `stock.picking` (extindere): suprascrie `button_validate` (blochează validarea transferurilor de intrare/ieșire cu linii fără linie de comandă de vânzare/achiziție sau cu cantitate efectuată peste cerere) și `write` (aplică verificări la salvarea comenzilor `move_ids` trimise de formular — linii noi sau modificate — prin `_check_restrict_move_commands`). Verificarea din `create()` este dezactivată (comentată) în cod.

**Securitate**

- `group_picking_restrict_entry_exit` („Picking create permission"): grup `res.groups` ai cărui membri sunt scutiți de restricțiile de la validare; conține implicit `base.user_root` și `base.user_admin` (înregistrare `noupdate`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [deltatech_picking_restrict](../deltatech_picking_restrict/index.md): modul înrudit, care restricționează validarea transferurilor pe tip de operațiune (grup, cantități, produse noi); nu există dependență între cele două (ambele depind doar de `stock`).
- `purchase_stock` / `sale_stock`: dacă sunt instalate, activează verificarea legăturii cu linia de comandă (câmpurile `purchase_line_id` / `sale_line_id` de pe `stock.move`); modulul nu depinde de ele.
