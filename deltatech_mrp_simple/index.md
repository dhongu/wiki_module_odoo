# Simple MRP (localizat la `deltatech_mrp_simple/index.md`)

- **Nume Tehnic:** `deltatech_mrp_simple`
- **Versiune:** `20.0.1.1.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_mrp_simple
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_simple`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă o variantă simplificată de producție, pentru cazurile în care întocmirea unei liste de materiale (BOM) este inutil de complexă. Utilizatorul înregistrează direct, pe un singur document, componentele consumate și produsele obținute; modulul mișcă stocul și evaluează produsele obținute la costul componentelor. Poate crea și un produs final nou și o ofertă pentru client. Este util pentru ambalări, reambalări, asamblări ad-hoc sau transformări simple de stoc.

#### 2. Funcționalități Cheie

- Document de producție simplă în **Inventar > Operațiuni > Simple Production**, cu liniile de consum (*Consume*) și de produse obținute (*Receipt*); **Add lines** adaugă mai multe componente deodată, cu aceeași cantitate.
- La **Confirm** se generează două transferuri, de consum și de recepție, cu tipurile de operațiune alese pe document; fiecare se validează automat dacă opțiunea (*Validation consume*, *Validation receipt*) este bifată, altfel rămâne de validat manual. Ele se deschid din butoanele **Consume** și **Receipt**; un document se confirmă o singură dată.
- Costul componentelor consumate se repartizează pe produsele obținute proporțional cu valoarea lor standard (sau cu cantitatea, dacă niciunul nu are preț de cost); **Recompute prices** refă repartizarea, iar *Unit Price* se poate modifica manual. Recepția intră în evaluarea stocului la acest preț.
- Un produs obținut cu preț unitar 0 blochează confirmarea, cu excepția cazului în care parametrul de sistem `deltatech_mrp_simple.allow_zero_cost` este `1`.
- Pentru utilizatorii din grupul *Sale simple production*, opțiunea *Create product & sale* creează la confirmare produsul final (stocabil, nepublicat) sau îl actualizează pe cel ales, îl adaugă ca produs obținut și generează o ofertă pentru *Client*, cu termenele de plată și lista de prețuri ale acestuia. Costul produsului este costul componentelor, iar prețul de vânzare suma prețurilor de vânzare ale componentelor.
- Comanda de vânzare asociată afișează butonul **MRP Simple**, care deschide producția simplă.
- La instalare, doar administratorul este membru al grupului *Sale simple production*; alți utilizatori se adaugă din **Setări > Utilizatori și companii > Grupuri**.
- Limitare cunoscută: **Add lines** rămâne disponibil și după confirmare, deși liniile unui document confirmat nu mai modifică transferurile.

#### 3. Dependențe

- `stock_account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `mrp.simple`: documentul central de producție simplă; grupează componentele consumate și produsele obținute, calculează prețurile și gestionează transferurile asociate.
- `mrp.simple.line.in`: liniile cu produsele obținute (recepție).
- `mrp.simple.line.out`: liniile cu componentele consumate.
- `add.multi.mrp.lines`, `add.multi.mrp.lines.product`: asistentul de adăugare în masă a liniilor.
- `sale.order` (extins): legătura cu producția simplă și butonul **MRP Simple**.
- `stock.picking`, `stock.move` (extinse): integrare cu transferurile generate de producția simplă.

**Vizualizări**

- `view_mrp_simple_form`, `mrp_simple_list`: interfața principală a producției simple (formular și listă), cu acces la transferuri.
- `view_order_form_inherit_simple_mrp`: extensie a comenzii de vânzare.
- `multi_add_view_form`: wizardul de adăugare a mai multor linii.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_config_parameter.xml`: definește parametrul de sistem `deltatech_mrp_simple.allow_zero_cost`, care permite confirmarea cu cost zero al produsului obținut.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): alternativă bazată pe liste de materiale (BOM); producția simplă acoperă același scop de transformare a stocului, dar fără structură de fabricație.
- [deltatech_mrp_cost](../deltatech_mrp_cost/index.md): tratează costurile suplimentare în fluxul MRP clasic, complementar calculului de preț din producția simplă.
- [deltatech_mrp_simple_barcode](../deltatech_mrp_simple_barcode/index.md): extensie cu scanare de coduri de bare pentru liniile de consum.
