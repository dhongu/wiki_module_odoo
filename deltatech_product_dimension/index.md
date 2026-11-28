# Dimensiuni Produs (localizat la `deltatech_product_dimension/index.md`)

- **Nume Tehnic:** `deltatech_product_dimension`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_dimension
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_dimension`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Transportul, depozitarea și ofertele de livrare au nevoie să știe cât spațiu ocupă un produs. Modulul adaugă lungimea, lățimea și înălțimea pe fișa produsului și calculează automat volumul din ele.

#### 2. Funcționalități Cheie

- **Rândul Dimensiune**: pe fișa produsului apare un rând *Dimensiune* deasupra câmpului *Volum*, cu trei câmpuri (lungime, lățime, înălțime), scrise L x l x h și urmate de „cm”. Fiecare pornește de la 1 pe un produs nou.
- **Volum automat**: la modificarea oricărei valori, *Volum* se recalculează ca lungime × lățime × înălțime ÷ 1.000.000, adică metri cubi din centimetri.
- **Unitatea de volum**: rezultatul nu este convertit în unitatea de volum configurată în baza de date, rămâne în metri cubi.
- **Dimensiune zero**: dacă una dintre valori este zero, volumul nu se recalculează și își păstrează valoarea anterioară.
- **Nivel produs**: câmpurile aparțin șablonului de produs, deci toate variantele au aceleași dimensiuni.
- Volumul se recalculează doar la editarea în formular; importurile și scrierile prin API nu îl actualizează.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpurile `product_length`, `product_width`, `product_height` (implicit 1) și calculul volumului la modificarea lor.

**Vizualizări**

- `views/product_view.xml`: rândul *Dimensiune* pe fișa produsului.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `deltatech_product_extension`: câmpul text *Dimensiuni* din acel modul nu calculează volumul; pentru lungime, lățime și înălțime numerice se folosește acest modul.
