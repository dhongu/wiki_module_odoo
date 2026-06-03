# Stock Inventory Product Display (localizat la `deltatech_stock_inventory_product_display/index.md`)

- **Nume Tehnic:** `deltatech_stock_inventory_product_display`
- **Versiune:** `19.0.0.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_inventory_product_display
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_inventory_product_display`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul adaugă un buton pe comenzile de vânzare și pe facturi, care permite vizualizarea rapidă a produselor incluse în linii. Apăsând butonul, utilizatorul vede într-o vizualizare kanban produsele din document împreună cu disponibilitatea lor în stoc (cantitatea în stoc minus cea rezervată), fără a părăsi fluxul de vânzare sau de facturare. Astfel, agenții de vânzări și operatorii pot verifica imediat dacă produsele comandate sunt disponibile, sprijinind o gestiune mai bună a stocului.

#### 2. Funcționalități Cheie

- Integrare cu comenzile de vânzare: adaugă un buton care afișează produsele din liniile comenzii într-o vizualizare kanban, indicând cantitățile disponibile (stoc minus rezervat).
- Integrare cu facturile: adaugă un buton care afișează produsele din liniile facturii într-o vizualizare kanban, cu nivelurile curente de stoc.
- Filtrare pe depozit: informațiile sunt filtrate per depozit, pentru o gestiune mai bună a inventarului.
- Vizibilitate a stocului: oferă utilizatorului posibilitatea de a vedea disponibilitatea produselor în timp real, direct din fluxul de vânzări sau de facturare.

#### 3. Dependențe

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): adaugă acțiunea care deschide vizualizarea produselor din liniile comenzii cu disponibilitatea în stoc.
- `account.move` (extins): adaugă acțiunea care deschide vizualizarea produselor din liniile facturii cu nivelurile curente de stoc.

**Vizualizări**

- `sale_order_view.xml`: adaugă butonul de afișare a produselor pe formularul comenzii de vânzare.
- `account_move_view.xml`: adaugă butonul de afișare a produselor pe formularul facturii.

#### 5. Conexiuni

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): furnizează modelul și vizualizările de inventar pe care acest modul le reutilizează pentru afișarea produselor și a disponibilității în stoc.
