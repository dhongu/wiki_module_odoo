# Rating partener în comenzi de vânzare și facturi (localizat la `deltatech_partner_rating_sale/index.md`)

- **Nume Tehnic:** `deltatech_partner_rating_sale`
- **Versiune:** `19.0.0.0.2`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_partner_rating_sale`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_partner_rating_sale`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul afișează un indicator vizual al ratingului partenerului direct în fluxul de vânzări și facturare, ajutând echipele de vânzări să ia decizii informate pe baza istoricului și a gradului de încredere al clientului. Din perspectivă de business, accesul imediat la ratingul clientului în procesul de ofertare și facturare reduce riscul financiar și îmbunătățește calitatea interacțiunilor comerciale.

#### 2. Funcționalități Cheie

- Decizii de vânzare mai bune: vizualizarea instantanee a ratingului partenerului pe oferte, comenzi de vânzare și facturi, pentru negociere și evaluare a riscului.
- Management îmbunătățit al creditului: folosirea ratingului pentru identificarea clienților cu risc ridicat înainte de finalizarea comenzilor mari sau a termenelor de plată.
- Livrare informată: vizibilitate asupra ratingului clientului pe livrări (pickings), pentru ca echipele de depozit și logistică să prioritizeze sau să ajusteze procesarea.
- Strategii comerciale țintite: adaptarea tacticilor de vânzare și a condițiilor în funcție de ratingul și performanța fiecărui partener.
- Vizibilitate centralizată a partenerilor: o imagine consecventă și accesibilă asupra fiabilității clienților în toate funcțiile integrate de vânzări și contabilitate.

#### 3. Dependențe

- `sale`
- `stock`
- `account`
- [deltatech_partner_rating](../deltatech_partner_rating/index.md)

#### 4. Componente Cheie

Modulul extinde modelele existente de vânzări, facturare și logistică pentru a expune ratingul partenerului preluat din modulul de bază `deltatech_partner_rating`.

**Modele**

- `sale.order`: extins pentru a afișa ratingul partenerului pe oferte și comenzi de vânzare.
- `account.move`: extins pentru a afișa ratingul partenerului pe facturi.
- `stock.picking`: extins pentru a afișa ratingul partenerului pe livrări.

**Vizualizări**

- `views/sale_order_view.xml`: adaugă indicatorul de rating în formularul de comandă de vânzare/ofertă.
- `views/account_move_view.xml`: adaugă indicatorul de rating în formularul de factură.
- `views/stock_picking_view.xml`: adaugă indicatorul de rating în formularul de livrare.

#### 5. Conexiuni

- [deltatech_partner_rating](../deltatech_partner_rating/index.md): modulul de bază care definește și calculează ratingul partenerului, valoare reutilizată aici în fluxul de vânzări, facturare și livrare.
