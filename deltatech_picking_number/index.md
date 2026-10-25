# Picking Number (Număr oficial la cerere pentru transferuri)

- **Nume Tehnic:** `deltatech_picking_number`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_number
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_number`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul permite atribuirea unui al doilea număr, oficial, transferurilor de stoc doar atunci când utilizatorul decide. Tipul de operațiune poate avea o secvență suplimentară „la cerere”, iar butonul **Alocă număr** de pe transfer preia următorul număr din ea. Astfel, ciornele, transferurile anulate sau de test nu consumă numere din seria oficială, iar documentele numerotate rămân consecutive, fără goluri.

#### 2. Funcționalități Cheie

- **A doua secvență pe tipul de operațiune**: câmpul *Sequence on Request* (lângă secvența standard de referință) stabilește seria folosită pentru numerele alocate; se setează din *Inventar > Configurare > Tipuri de operațiuni*.
- **Număr la cerere**: butonul **Allocate number** de pe formularul transferului preia următorul număr din secvență și îl setează ca referință (nume) a transferului; numărul se păstrează și în câmpul *Request Number*.
- **Alocare o singură dată**: un transfer care are deja număr sau al cărui tip de operațiune nu are secvență la cerere rămâne neschimbat.
- **Mai multe transferuri deodată**: acțiunea lucrează pe un set de transferuri, fiecare primind numărul său.
- **Numerotare protejată**: un transfer cu număr alocat nu poate fi șters (apare mesaj de eroare); se anulează în schimb.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): câmpul `request_number`, metoda `action_get_number` și blocarea ștergerii (`unlink`) pentru transferurile numerotate.
- `stock.picking.type` (extins): câmpul `request_sequence_id` (many2one către `ir.sequence`).

**Vizualizări**

- `view_picking_form`: adaugă butonul „Allocate number” pe formularul transferului.
- `view_picking_type_form`: adaugă câmpul „Sequence on Request” după secvența standard.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `stock`: modelele `stock.picking` și `stock.picking.type` sunt extinse direct.
