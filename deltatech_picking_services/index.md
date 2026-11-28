# Picking Services (localizat la `deltatech_picking_services/index.md`)

- **Nume Tehnic:** `deltatech_picking_services`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_picking_services
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_services`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe transferurile de stoc un tab dedicat liniilor de servicii, separat de liniile de mișcare de stoc. Echipele de logistică pot înregistra pe același document servicii legate de transfer (manipulare, ambalare etc.), fără a le amesteca cu produsele stocabile.

#### 2. Funcționalități Cheie

- Tab nou **Services** pe formularul transferului, cu produse de tip serviciu.
- Fiecare linie are produs, descriere, cantitate, unitate de măsură, preț unitar și subtotal calculat (cu total pe coloană); liniile se pot reordona.
- Liniile se copiază odată cu transferul și sunt filtrate pe companie.
- Pașii de configurare și utilizare sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Sumarul provine din `readme/DESCRIPTION.md`; componentele au fost verificate punctual în cod.

**Modele**

- `stock.picking` (extins): câmpul `picking_service_lines`.
- `picking.service.line`: linie de serviciu a unui transfer (produs, cantitate, unitate de măsură, preț unitar, subtotal).

**Vizualizări**

- `view_picking_form_services`: tabul **Services** adăugat după tabul de operațiuni al transferului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

Nu există conexiuni funcționale cu alte module documentate în wiki.
