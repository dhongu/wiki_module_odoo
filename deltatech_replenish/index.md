# Deltatech Replenish (localizat la `deltatech_replenish/index.md`)

- **Nume Tehnic:** `deltatech_replenish`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_replenish
- **Cale Locală:** `odoo-addons/deltatech/deltatech_replenish`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modul de compatibilitate, păstrat doar pentru bazele de date migrate de la Odoo 18.0, unde alegerea furnizorului în wizardul de reaprovizionare era oferită de Deltatech. Începând cu Odoo 19.0, această funcție face parte din modulul standard `purchase_stock`, deci modulul nu mai adaugă niciun model, vizualizare sau date proprii. Rămâne instalabil, fără conținut, ca baza de date să nu piardă intrarea modulului după upgrade.

#### 2. Funcționalități Cheie

Funcționalitățile de mai jos sunt oferite acum de Odoo standard (`purchase_stock`), nu de acest modul:

- Câmpul „Vendor” (furnizor) în wizardul de reaprovizionare a produsului.
- Selectarea unui furnizor anume din lista furnizorilor produsului.
- Furnizorul ales este folosit la crearea comenzii de achiziție rezultate din reaprovizionare.
- Termenul de livrare al furnizorului este luat în calcul la data programată.

Utilizare: din Inventar > Produse (sau orice vizualizare cu butonul „Replenish”), se apasă „Replenish”, se alege o rută care achiziționează produsul (apare câmpul „Vendor”), se selectează furnizorul și se continuă reaprovizionarea.

Notă tehnică: în standard, `product.replenish` moștenește `stock.replenish.mixin`, care furnizează câmpul `supplier_id` (`product.supplierinfo`) și îl transmite procurement-ului ca `supplierinfo_id`. Suprascrierea Deltatech a fost eliminată, pentru că ar fi afișat câmpul de două ori în formular.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- Niciunul: modulul nu definește și nu extinde modele.

**Vizualizări**

- Niciuna.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `stock`: wizardul de reaprovizionare (`product.replenish`) la care se referă funcția preluată de standard.
