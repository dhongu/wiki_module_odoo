# Sale Pallet Website (localizat la `deltatech_sale_pallet_website/index.md`)

- **Nume Tehnic:** `deltatech_sale_pallet_website`
- **Versiune:** `19.0.1.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_pallet_website`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_pallet_website`
- **Ultima Ingestie:** `2026-11-10`

#### 1. Sumar

Produsele vândute în vrac (cărămizi, plăci) se livrează pe paleți pe care clientul îi plătește. Modulul `deltatech_sale_pallet` adaugă liniile de palet pe comenzile din back-office; acest modul aduce aceeași logică în magazinul online: paleții sunt afișați pe pagina de produs și adăugați automat în coș.

#### 2. Funcționalități Cheie

- **Prețul paletului pe pagina de produs:** pentru produsele cu cantitate minimă de palet, apare un rând de tipul „When buying 10 units, the price is ...", unde prețul este cantitatea minimă de palet la prețul de vânzare plus prețul produsului-palet.
- **Linii de palet în coș:** la fiecare adăugare sau modificare de cantitate, liniile de palet se recalculează: o linie per produs-palet, cu numărul de paleți întregi necesari tuturor liniilor din coș care folosesc acel palet. O cantitate sub un palet întreg nu adaugă palet. Când ultimul produs care necesită palet este scos din coș, linia de palet dispare și ea.
- **Prețul livrării include paleții:** liniile de palet sunt actualizate înainte de recalcularea prețului de livrare și a cantității din coș, deci ambele țin cont de paleți.
- **Configurare:** pe fișa produsului, tab-ul *Inventar*, secțiunea **Palletizing** (din `deltatech_sale_pallet`): **Pallet Product** (produsul-palet, vândut la propriul preț) și **Pallet Qty Min** (cantitatea care umple un palet). Produsele fără aceste setări se vând normal în magazin. Flag-ul **Pallet** de pe categoriile de produse nu este folosit de magazin.

#### 3. Dependențe

- [deltatech_sale_pallet](../deltatech_sale_pallet/index.md)
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `sale.order`: suprascrie hook-ul `_verify_cart_after_update` (apelat de `website_sale` după `_cart_add` / `_cart_update_line_quantity`) și apelează `_update_cart_pallet_lines` înainte de `super()`, ca livrarea și cantitatea din coș să includă paleții.

**Vizualizări**

- `show_pallet_price` (`views/templates.xml`): extinde `website_sale.product` și afișează prețul pentru cantitatea minimă de palet.

#### 5. Conexiuni

- [deltatech_sale_pallet](../deltatech_sale_pallet/index.md): modulul de bază pentru logica de paletizare pe comenzile de vânzare, extins de acest modul pentru magazinul online.
- `website_sale`: platforma eCommerce Odoo ale cărei pagini de produs și coș de cumpărături sunt extinse pentru afișarea și recalcularea paleților.
