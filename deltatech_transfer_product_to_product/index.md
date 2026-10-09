# Transfer Product to Product (localizat la `deltatech_transfer_product_to_product/index.md`)

- **Nume Tehnic:** `deltatech_transfer_product_to_product`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_transfer_product_to_product
- **Cale Locală:** `odoo-addons/deltatech/deltatech_transfer_product_to_product`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul permite înlocuirea rapidă în stoc a unui produs cu altul (de exemplu un articol introdus greșit în gestiune sau un produs echivalent), fără a face manual ajustări de inventar. Utilizatorul alege cele două produse, locația și cantitatea, iar sistemul scoate din stoc cantitatea de produs sursă și introduce aceeași cantitate din produsul destinație. Modulul are statut de dezvoltare Beta.

#### 2. Funcționalități Cheie

- Meniu nou **Inventar → Operațiuni → Ajustări → Transfer Product to Product** (sub `stock.menu_stock_adjustments`), care deschide un wizard.
- Wizard-ul cere: produs sursă („From Product"), produs destinație („To Product"), locația de stoc („Adjustment Location"), cantitatea (implicit 1), locația de ajustare/inventar („Adjusting Location") și tipul de operațiune intern.
- La alegerea produsului sursă, locația de ajustare se completează automat cu locația de inventar a produsului; la alegerea locației de stoc, tipul de operațiune intern se alege automat din depozitul căruia îi aparține locația (eroare dacă depozitul nu are tip intern).
- Avertizare vizuală în wizard: mesaj verde dacă cele două produse au același cost standard, mesaj roșu cu costurile celor două produse dacă diferă (atenție la impactul asupra valorii stocului).
- La confirmare se creează, se confirmă și se validează automat două transferuri interne: unul care scoate produsul sursă din stoc către locația de ajustare și unul care introduce produsul destinație din locația de ajustare în stoc.
- Limitări cunoscute (din `readme/bugs.md`, deschise): confirmarea de backorder pentru transferul sursă este ignorată (al doilea transfer se poate valida singur), iar la tipuri de operațiune cu rezervare manuală validarea eșuează cu cantitate zero.

#### 3. Dependențe

- `product`
- `stock`

#### 4. Componente Cheie

**Modele**

- `transfer.product.to.product` (TransientModel): wizard-ul de transfer; conține câmpurile alese de utilizator, onchange-urile pentru preț/locații/tip operațiune și metoda `action_confirm` care creează și validează cele două transferuri interne.

**Vizualizări**

- `view_transfer_wizard`: formularul wizard-ului, cu alertele de preț și butoanele Confirm / Cancel.
- `action_invoice_stock_adjustment_wizard`: acțiunea (fereastră nouă) care deschide wizard-ul.
- `menu_transfer_product_to_product`: intrarea de meniu din Inventar → Ajustări.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `stock`: transferurile create sunt `stock.picking` / `stock.move` interne obișnuite, vizibile în Inventar.
