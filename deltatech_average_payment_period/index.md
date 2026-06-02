# Deltatech Average Payment Period (localizat la `deltatech_average_payment_period/index.md`)

- **Nume Tehnic:** `deltatech_average_payment_period`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_average_payment_period`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_average_payment_period`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul calculează durata medie de încasare și de plată a companiei, adică perioada medie scursă între data facturii și data efectivă a decontării. Această informație ajută echipa financiară să înțeleagă cât de repede își încasează banii de la clienți și cât de repede își plătește furnizorii, oferind un indicator util pentru gestionarea cash-flow-ului.

#### 2. Funcționalități Cheie

- Calculează durata medie a contabilității de casă (perioada medie de plată/încasare).
- Zile de plată ("Payment Days"): diferența dintre data facturii și data plății, ponderată cu suma decontată.
- Zile de plată simple ("Payment days simple"): diferența dintre data facturii și data plății, doar pentru facturile de furnizor și client, fără notele de credit.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`, care nu solicită explicit analiza codului pentru Componente Cheie. Această secțiune este, prin urmare, omisă.

#### 5. Conexiuni

- `account`: modulul standard de contabilitate al Odoo, sursa facturilor și a plăților pe baza cărora se calculează perioadele medii.
