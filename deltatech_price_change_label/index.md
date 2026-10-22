# Etichete pentru modificarea de preț (Price Change Labels)

- **Nume Tehnic:** `deltatech_price_change_label`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_price_change_label
- **Cale Locală:** `odoo-addons/deltatech/deltatech_price_change_label`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul adaugă pe documentul de modificare de preț un buton pentru tipărirea etichetelor de raft. Cu un singur clic se deschide asistentul de etichete cu câte o linie pentru fiecare produs din document, astfel încât etichetele tuturor produselor cu preț nou se pot printa odată. Se instalează automat când sunt prezente ambele module de care depinde.

#### 2. Funcționalități Cheie

- Buton **Print Labels** pe documentul de modificare de preț (vizibil doar dacă documentul are linii).
- Asistentul de etichete se deschide cu o linie pentru fiecare produs din document, cantitate 1; la linii pe șablon sunt incluse toate variantele.
- Layout nou **Shelf label with price**: denumirea produsului, prețul cu taxe incluse, codul și unitatea de măsură; este propus implicit, dar se poate alege orice alt layout de etichetă.
- Prețul cu taxe incluse este calculat pe linia de etichetă din taxele de vânzare ale produsului.
- Dacă documentul are depozit, acesta este transmis în context asistentului de etichete.

#### 3. Dependențe

- [deltatech_price_change](../deltatech_price_change/index.md)
- [deltatech_product_labels](../deltatech_product_labels/index.md)

#### 4. Componente Cheie

**Modele**

- `product.price.change` (extins): metoda `action_print_labels` deschide asistentul de etichete cu layoutul implicit „Shelf label with price”.
- `product.product.label` (extins, tranzitoriu): `default_get` generează liniile de etichete din documentul de modificare de preț.
- `product.product.label.line` (extins, tranzitoriu): câmpul calculat `price_incl` (preț cu taxe incluse).

**Vizualizări**

- `view_change_price_form`: moștenește formularul documentului și adaugă butonul Print Labels.
- `report_shelf_label` / `shelf_label`: raportul QWeb PDF al etichetei de raft cu preț.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_product_labels](../deltatech_product_labels/index.md): oferă asistentul și layoutele de etichete extinse aici.
- [deltatech_price_change](../deltatech_price_change/index.md): documentul de modificare de preț din care se tipăresc etichetele.
