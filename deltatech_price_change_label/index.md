# Etichete modificare prețuri (Price Change Labels)

- **Nume Tehnic:** `deltatech_price_change_label`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_price_change_label
- **Cale Locală:** odoo-addons/deltatech/deltatech_price_change_label
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă pe documentul de modificare de preț un buton de tipărire a etichetelor, astfel încât etichetele de raft ale tuturor produselor cu preț nou se pot tipări odată.

#### 2. Funcționalități Cheie

- **Buton Print Labels** pe documentul de modificare de preț: deschide wizardul de etichete din `deltatech_product_labels` cu câte o linie pentru fiecare produs din document.
- **Layout „Shelf label with price”:** nume produs, preț cu taxe, cod și unitate de măsură; este propus implicit din document, dar se poate alege orice alt layout.
- **Instalare automată** când sunt instalate ambele module, `deltatech_price_change` și `deltatech_product_labels`.

#### 3. Dependențe

- [deltatech_price_change](../deltatech_price_change/index.md)
- [deltatech_product_labels](../deltatech_product_labels/index.md)

#### 4. Componente Cheie

**Modele**

- `product.price.change` (extins): acțiunea butonului de etichete.
- `product.product.label` (extins): wizard-ul de etichete preia liniile din document.

**Vizualizări**

- `view_change_price_form`: adaugă butonul Print Labels pe documentul de modificare de preț.
- `report_shelf_label`: raportul pentru layoutul „Shelf label with price”.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_price_change](../deltatech_price_change/index.md): documentul din care se tipăresc etichetele.
- [deltatech_product_labels](../deltatech_product_labels/index.md): wizardul și layouturile de etichete.
