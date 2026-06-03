# Sale Phone (localizat la `deltatech_sale_phone/index.md`)

- **Nume Tehnic:** `deltatech_sale_phone`
- **Versiune:** `19.0.1.0.2`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_phone`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_phone`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul afișează numărul de telefon al partenerului direct pe comenzile de vânzare și pe facturi, fără a fi nevoie de navigare către fișa contactului. Astfel, echipa de vânzări și cea de facturare au la îndemână datele de contact ale clientului chiar în documentul la care lucrează, ceea ce ușurează comunicarea și verificarea rapidă a informațiilor.

#### 2. Funcționalități Cheie

- Adaugă numărul de telefon al partenerului pe formularul comenzii de vânzare.
- Adaugă numărul de telefon al partenerului pe formularul facturii.
- Numărul de telefon este preluat automat din fișa partenerului și afișat folosind widget-ul dedicat de telefon.

#### 3. Dependențe

- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): adaugă câmpul calculat `partner_phone`, preluat din telefonul partenerului asociat comenzii.
- `account.move` (extins): adaugă câmpul calculat `partner_phone`, preluat din telefonul partenerului asociat facturii.

**Vizualizări**

- `sale_order_view_form`: extinde formularul comenzii de vânzare (`sale.view_order_form`) pentru a afișa câmpul de telefon după partener.
- `view_move_form`: extinde formularul facturii (`account.view_move_form`) pentru a afișa câmpul de telefon după adresa de livrare.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate, sarcini cron sau acțiuni server în acest modul.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale relevante către alte module cu pagină wiki.
