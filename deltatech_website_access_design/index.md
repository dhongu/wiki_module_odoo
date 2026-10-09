# Website web designer access (localizat la `deltatech_website_access_design/index.md`)

- **Nume Tehnic:** `deltatech_website_access_design`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_website_access_design
- **Cale Locală:** `odoo-addons/deltatech/deltatech_website_access_design`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă acces restrâns pentru un web designer: utilizatorii care lucrează doar pe site nu mai văd meniurile de Contacte, Vânzări și Facturare (clienți și furnizori), acestea rămânând vizibile numai pentru un grup dedicat de acces intern. Astfel, designerul poate lucra pe website fără a avea acces la datele comerciale și contabile ale companiei.

#### 2. Funcționalități Cheie

- Grup nou „Access Partners, Sale, Invoice”, în care sunt adăugați implicit utilizatorii root și administrator.
- Meniurile Contacte, Vânzări, Clienți (Facturare) și Furnizori (Facturare) devin vizibile doar pentru membrii acestui grup.
- Utilizatorii interni care trebuie să păstreze accesul la aceste meniuri se adaugă manual în grup.
- Modulul modifică doar vizibilitatea meniurilor; nu introduce reguli de acces (ACL) noi pe modele.

#### 3. Dependențe

- `website`
- `contacts`
- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele Python.

**Vizualizări**

- `contacts.menu_contacts`, `sale.sale_menu_root`, `account.menu_finance_receivables`, `account.menu_finance_payables`: meniuri existente, cu `group_ids` înlocuit cu grupul `group_user_internal`.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau server. Grupul `group_user_internal` este definit în `data/data.xml` (`noupdate="1"`).

#### 5. Conexiuni

- Nu există legături funcționale cu alte pagini wiki. A fost instalat standalone pentru Ridacon (helpdesk #9538), fără a fi dependență a unui modul de client.
