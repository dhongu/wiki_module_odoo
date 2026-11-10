# Picking Services (localizat la `deltatech_picking_services/index.md`)

- **Nume Tehnic:** `deltatech_picking_services`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_picking_services
- **Cale Locală:** `odoo-addons/deltatech/deltatech_picking_services`
- **Ultima Ingestie:** `2026-11-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe transferurile de stoc (`stock.picking`) o pagină dedicată liniilor de servicii, în care pot fi înregistrate produse de tip serviciu (de exemplu transport, manipulare, paletizare sau ambalare) separat de liniile de mișcare de stoc. Echipele de logistică notează astfel pe același document serviciile aferente recepției sau livrării, cu cantitate, preț unitar și subtotal, fără a le amesteca cu produsele stocabile. Liniile sunt doar evidență operațională: nu generează mișcări de stoc, note contabile sau facturi.

#### 2. Funcționalități Cheie

- Pagină nouă **Services** pe formularul transferului, după pagina operațiilor, care conține doar produse de tip serviciu.
- Fiecare linie are serviciul, descrierea (ascunsă implicit, o afișează selectorul de coloane), cantitatea (implicit 1), unitatea de măsură, prețul unitar și subtotalul (preț unitar × cantitate); totalul se afișează sub coloana Subtotal. Descrierea și unitatea se propun din produs; ordinea liniilor se schimbă prin tragere.
- Liniile de servicii se copiază la duplicarea transferului și se șterg odată cu el.
- Liniile preiau compania transferului și sunt vizibile doar utilizatorilor cu acces la acea companie (regulă multi-company).
- Facturarea sau decontarea serviciilor rămâne manuală, prin fluxurile standard de vânzare sau achiziție. Fluxul pas cu pas este în fișa consultant.

> Notă: în Odoo Apps modulul apare sub numele „Picking Services" (anterior „Picking Service Lines"); numele tehnic nu s-a schimbat. Starea de dezvoltare din manifest: Beta.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Sumar și Funcționalități Cheie provin din `readme/DESCRIPTION.md`, completat cu fișa consultant și istoricul; mai jos, o verificare punctuală a codului.

**Modele**

- `picking.service.line` (nou): linia de serviciu, cu produs (domeniu `type = service`), unitate de măsură, cantitate, descriere, preț unitar, subtotal calculat, transferul (`ondelete="cascade"`) și compania (stocată, din transfer).
- `stock.picking` (extins): câmpul `picking_service_lines` (One2many, `copy=True`).

**Vizualizări**

- `view_picking_form_services`: moștenește `stock.view_picking_form` și adaugă pagina „Services" cu lista editabilă a serviciilor (cu total pe subtotal).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul adaugă regula `picking_service_line_rule` (`ir.rule`, multi-company) și drepturile de acces din `security/ir.model.access.csv`.

#### 5. Conexiuni

- `stock`: transferul pe care se adaugă pagina Services (dependență directă).
- `product`: produsele de tip serviciu alese pe linii.
