# Product Labels (localizat la `deltatech_product_labels/index.md`)

- **Nume Tehnic:** `deltatech_product_labels`
- **Versiune:** `19.0.1.3.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_labels
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_labels`
- **Ultima Ingestie:** `2026-10-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite tipărirea etichetelor de produs și de lot dintr-un singur asistent, deschis din produse, comenzi de vânzare, transferuri, loturi și linii de stoc. Machetele implicite includ denumirea, referința internă, codul de bare, lotul și prețul cu TVA, pe formate gata făcute pentru imprimanta de birou (coală A4) și pentru imprimantele termice. Echipele de depozit și de vânzări pot eticheta rapid marfa la recepție și pe raft, iar companiile își pot adăuga propriile machete.

#### 2. Funcționalități Cheie

- Tipărire etichete din produse, comenzi de vânzare, transferuri, loturi și linii de stoc (quants).
- Machete implicite, fiecare cu formatul ei de hârtie: coală A4 cu 3x8 etichete (70x37 mm), 100x50 mm și 40x25 mm (o etichetă pe pagină, pentru imprimante termice) și machetă continuă, fără format de hârtie.
- Machetele implicite A4 3x8, 100x50 și 40x25 tipăresc prețul cu TVA, cu moneda și unitatea de măsură, alături de denumire, referință internă, cod de bare și lot. Fără preț, nu se tipărește blocul de preț. Fără listă de prețuri, se folosește moneda produsului.
- Asistentul propune macheta tipărită ultima dată de utilizator; prima dată, coala A4 3x8.
- Dacă este selectată doar opțiunea de lot, iar tipărirea pornește dintr-un produs, se tipăresc etichetele pentru toate loturile aflate pe stoc.
- Din transferuri de tip recepție, opțiunea „Generează loturile automat” completează numele loturilor înainte de tipărire.
- Machetele ZPL (raport de tip text) au buton **Previzualizare**: ZPL-ul este trimis la serviciul extern Labelary (`api.labelary.com`) și returnat ca PDF. Dimensiunea etichetei se setează pe raport (lățime, înălțime, rezoluție imprimantă) sau se citește din numele lui, de exemplu „Labels 40x30 ZPL (300 DPI)”.
- În mod implicit, suprascrie butonul standard de tipărire a etichetelor din produse. Pentru a reveni la funcția standard, parametrul de sistem `terrabit_labels.override_print_button` trebuie setat la `False`.
- Se pot crea machete personalizate prin definirea unui raport pe modelul `product.product.label`.

#### 3. Dependențe

- `product`
- `sale`
- `stock`

#### 4. Componente Cheie

DESCRIPTION.md acoperă funcționalitățile; fluxul detaliat este în fișa consultant. Componentele tehnice din cod:

**Modele**

- `product.product.label` (wizard): asistentul „Etichete produs”; pe el se definesc rapoartele cu machete personalizate.
- `product.product.label.line` (wizard): linia asistentului, cu produs, număr de etichete și lot.
- `product.template` / `product.product` (extinse): `action_open_label_layout` deschide asistentul modulului în loc de cel standard, cât timp `terrabit_labels.override_print_button` nu este `False`.
- `ir.actions.report` (extins): dimensiunea etichetei și previzualizarea pentru machetele ZPL.

**Vizualizări**

- `product_product_label_view_form`: formularul asistentului „Etichete produs”.
- `act_report_xml_view_zpl_label`: câmpurile de dimensiune și rezoluție pe rapoartele de tip text.
- `action_action_product_template_label`, `action_action_product_product_label`, `action_action_sale_order_product_label`, `action_action_stock_picking_product_label`, `action_action_stock_lot_product_label`, `action_action_stock_quant_product_label`: acțiunile care deschid asistentul din produs, variantă, comandă, transfer, lot și linie de stoc.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron` sau reguli `base.automation`. Modulul înregistrează formatele de hârtie (`paperformat_label_a4_3x8`, `paperformat_label_100x50`, `paperformat_label_40x25`) și patru rapoarte de etichete (A4 3x8, 100x50, 40x25, continuu).

#### 5. Conexiuni

- [deltatech_price_change_label](../deltatech_price_change_label/index.md): etichete din modificările de preț; calculul prețului cu taxe (`price_incl`) a fost mutat din acel modul în `deltatech_product_labels`.
- Labelary (`api.labelary.com`, serviciu extern): transformă ZPL în PDF pentru **Previzualizare**.
