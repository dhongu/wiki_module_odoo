# Product Labels (localizat la `deltatech_product_labels/index.md`)

- **Nume Tehnic:** `deltatech_product_labels`
- **Versiune:** `20.0.1.3.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_product_labels
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_labels`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite tipărirea etichetelor de produs din mai multe puncte ale fluxului: produse, comenzi de vânzare, livrări/recepții, loturi și stocuri. Echipele de depozit și de vânzări obțin rapid etichetele necesare, cu aspecte (layout-uri) predefinite sau personalizate.

#### 2. Funcționalități Cheie

- Tipărire etichete din produse, comenzi de vânzare, transferuri (pickings), loturi și cantități în stoc (quants).
- Aspecte implicite cu denumirea produsului, referința internă, codul de bare, lotul și prețul cu TVA (cu monedă și unitate de măsură), pentru rafturi de magazin, depozite sau produse, fiecare cu formatul propriu de hârtie: coală A4 cu 3x8 etichete (70x37 mm), 100x50 mm și 40x25 mm (o etichetă pe pagină, pentru imprimante termice) și etichete continue, fără format de hârtie.
- Asistentul propune aspectul tipărit ultima dată de utilizator; prima dată, coala A4 3x8.
- Dacă este selectată doar opțiunea de lot și tipărirea pornește dintr-un produs, se tipăresc etichetele pentru toate loturile aflate pe stoc.
- Implicit suprascrie butonul de tipărire a etichetelor din produse; pentru revenirea la funcția standard, parametrul de sistem `terrabit_labels.override_print_button` se setează la `False`.
- Aspecte personalizate se creează prin definirea unui raport pe modelul `product.product.label`.
- Aspectele ZPL (raport de tip text) au butonul *Previzualizare*: ZPL-ul este trimis serviciului Labelary (`api.labelary.com`) și întors ca PDF. Dimensiunea etichetei se setează pe raport (lățime, înălțime, rezoluția imprimantei) sau se citește din denumire, de exemplu „Labels 40x30 ZPL (300 DPI)”.

#### 3. Dependențe

- `product`
- `sale`
- `stock`

#### 4. Componente Cheie

**Modele**

- `product.product.label` și `product.product.label.line`: asistentul de tipărire și liniile sale.
- `ir.actions.report` (extins): dimensiunile etichetei ZPL (`zpl_label_width`, `zpl_label_height`, `zpl_dpmm`) pentru previzualizare.
- `product.template` / `product.product` (extinse): `action_open_label_layout`, care deschide asistentul de etichete.

**Vizualizări**

- `views/report_product_labels.xml`: rapoartele de etichete implicite.
- `views/terrabit_product_label_print_view.xml`: formularul asistentului de tipărire.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte pagini wiki de module.
