# Picking Validation Restrict Entry Exit (localizat la `deltatech_picking_restrict_entry_exit/index.md`)

- **Nume Tehnic:** `deltatech_picking_restrict_entry_exit`
- **Versiune:** `20.0.0.0.15`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_picking_restrict_entry_exit
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_restrict_entry_exit`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul împiedică depozitul să valideze recepții și livrări care nu corespund comenzilor: produse care nu provin dintr-o comandă de achiziție sau de vânzare, ori cantități mai mari decât cererea. Astfel se mută efectiv doar ce a fost aprobat în comenzi.

#### 2. Funcționalități Cheie

- La **Validare**, fiecare linie cu cantitate a unei recepții trebuie să provină dintr-o linie de comandă de achiziție, iar cea a unei livrări dintr-o linie de comandă de vânzare. Verificarea la recepții se aplică dacă este instalat `purchase_stock`, cea la livrări dacă este instalat `sale_stock`.
- O linie a cărei **Cantitate** efectuată depășește **Cererea** blochează validarea; aceeași verificare rulează la salvarea transferului după modificarea cantității unei linii.
- Liniile adăugate manual nu pot fi salvate cu cantitate efectuată pe recepții și livrări; pe celelalte transferuri, cantitatea unei astfel de linii nu poate depăși cererea.
- Cazuri scutite: retururile și backorder-urile nu sunt verificate la validare, nici transferurile interne între două locații ale aceluiași depozit.
- Grupul **Picking create permission** scutește membrii de verificările de la validare și le permite să adauge linii pe recepții și livrări. La instalare doar administratorul este în grup; ceilalți utilizatori sunt restricționați. Pentru a scuti un utilizator: modul dezvoltator, **Settings > Users & Companies > Groups**, se deschide grupul și se adaugă utilizatorul.
- Limitări: crearea unei recepții sau livrări fără comandă sursă nu este blocată, ci doar validarea ei; verificarea cantității la salvare se aplică tuturor utilizatorilor, inclusiv membrilor grupului, și retururilor/backorder-urilor.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, care nu cere analiză suplimentară a codului.

**Modele**

- `stock.picking` (extins): verificările la validare și la salvare descrise mai sus.

**Vizualizări**

- Modulul nu adaugă vizualizări; definește doar grupul de securitate `group_picking_restrict_entry_exit` („Picking create permission”).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

Nu există conexiuni funcționale cu alte module documentate în wiki.
