# Stock Removal Location by Priority (localizat la `deltatech_stock_removal_priority/index.md`)

- **Nume Tehnic:** `deltatech_stock_removal_priority`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_removal_priority
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_removal_priority`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul introduce o strategie de scoatere a stocului bazată pe prioritate. Gestionarii de depozit controlează ordinea în care se ridică marfa din zonele de stocare, pentru fluxuri logistice optime și o utilizare mai bună a spațiului. Funcționează împreună cu [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md): regulile de depozitare direcționează produsele la recepție, iar acest modul le folosește și pentru a stabili ordinea de scoatere la picking.

#### 2. Funcționalități Cheie

- Strategie de scoatere dedicată, **Priority**, adăugată în configurarea locațiilor; Odoo alege automat stocul din locațiile cu prioritatea cea mai mare.
- Prioritatea fiecărui quant derivă automat din regulile de depozitare (putaway), potrivite mai întâi după produs, apoi după categoria de produs.
- Prioritate implicită configurabilă prin parametrul de sistem `stock.removal_priority.default` (implicit 999), din `Setări > Tehnic > Parametri de sistem`.
- Recalculare automată a priorităților quanturilor afectate la crearea, modificarea sau ștergerea unei reguli de depozitare.
- Excluderea unor locații din colectarea stocului la picking.
- Utilizare: se configurează regulile de depozitare în `Inventar > Configurare > Locații` (secvență mai mică = prioritate mai mare), apoi se setează *Strategia de scoatere* pe **Priority** în `Inventar > Configurare > Categorii de produs`.
- Util în depozite mari, cu zone de picking preferate sau mai multe niveluri de stocare.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.quant` (extins): câmpul `removal_priority`, calculat din regulile de depozitare; ordinea de scoatere și domeniul de colectare.
- `stock.putaway.rule` (extins): invalidează prioritățile la create/write/unlink.
- `ir.config_parameter` (extins): recalculează prioritatea implicită când se schimbă parametrul.

**Vizualizări**

- Modulul nu adaugă vizualizări.

**Acțiuni Automate / Acțiuni Server**

- `removal_priority` (`product.removal`): înregistrarea de date a strategiei *Priority* (metoda `priority`).

#### 5. Conexiuni

- [deltatech_putaway_strategy](../deltatech_putaway_strategy/index.md): regulile de depozitare definite acolo determină prioritatea de scoatere calculată de acest modul.
