# Product Labels (localizat la `deltatech_product_labels/index.md`)

- **Nume Tehnic:** `deltatech_product_labels`
- **Versiune:** `19.0.1.1.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_labels
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_labels`
- **Ultima Ingestie:** `2026-06-01`

#### 1. Sumar

Modulul permite tipărirea etichetelor pentru produse direct din mai multe puncte ale fluxului de lucru: din fișa produsului, din comenzile de vânzare și din livrările (pickings). Atunci când tipărirea pornește dintr-un produs și este selectată doar opțiunea de loturi, modulul tipărește automat etichetele pentru toate loturile aflate pe stoc. Astfel, echipele de depozit și de vânzări pot genera rapid etichetele necesare, cu posibilitatea de a personaliza aspectul acestora în funcție de nevoile companiei.

#### 2. Funcționalități Cheie

- Tipărire etichete pornind de la produse, comenzi de vânzare și livrări (pickings).
- Dacă este selectată doar opțiunea de lot, iar tipărirea pornește dintr-un produs, se tipăresc etichetele pentru toate loturile aflate pe stoc.
- În mod implicit, suprascrie butonul standard de tipărire a etichetelor din produse. Pentru a reveni la funcția standard de tipărire, parametrul de sistem `terrabit_labels.override_print_button` trebuie setat la `False`.
- Se pot crea aspecte (layout-uri) personalizate prin definirea unui raport pe modelul `product.product.label`.

#### 3. Dependențe

- `product`
- `sale`
- `stock`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`, secțiunile pentru Modele, Vizualizări și Acțiuni Automate / Acțiuni Server nu au fost detaliate prin analiza codului. Documentul DESCRIPTION.md menționează însă explicit:

**Modele**

- `product.product.label`: model pe care se pot defini rapoarte pentru a crea aspecte (layout-uri) personalizate de etichete.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte pagini wiki existente.
