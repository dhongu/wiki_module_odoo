# Stock Inventory Product Display (localizat la `deltatech_stock_inventory_product_display/index.md`)

- **Nume Tehnic:** `deltatech_stock_inventory_product_display`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_inventory_product_display
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_inventory_product_display`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaugă un buton pe comenzile de vânzare și pe facturi, care permite vizualizarea rapidă a produselor din linii. Utilizatorul vede, într-o vizualizare kanban, produsele documentului împreună cu disponibilitatea lor în stoc, fără a părăsi fluxul de vânzare sau de facturare. Astfel, agenții de vânzări și operatorii pot verifica imediat dacă produsele comandate sunt disponibile.

#### 2. Funcționalități Cheie

- Integrare cu comenzile de vânzare: buton care afișează produsele din liniile comenzii într-un kanban, cu cantitățile disponibile (stoc minus rezervat).
- Integrare cu facturile: buton care afișează produsele din liniile facturii într-un kanban, cu nivelurile curente de stoc.
- Filtrare pe depozit: informațiile sunt afișate per depozit, pentru o gestiune mai bună a inventarului.
- Vizibilitate a stocului: disponibilitatea produselor în timp real, direct din fluxul de vânzări sau de facturare.

#### 3. Dependențe

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): acțiunea care deschide vizualizarea produselor din liniile comenzii, cu disponibilitatea în stoc.
- `account.move` (extins): acțiunea care deschide vizualizarea produselor din liniile facturii, cu nivelurile curente de stoc.

**Vizualizări**

- `sale_order_view.xml`: butonul de afișare a produselor pe formularul comenzii de vânzare.
- `account_move_view.xml`: butonul de afișare a produselor pe formularul facturii.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md): furnizează modelul și vizualizările de inventar pe care acest modul le reutilizează pentru afișarea produselor și a disponibilității în stoc.
