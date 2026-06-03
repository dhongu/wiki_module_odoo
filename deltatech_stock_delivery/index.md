# Livrare / Recepție din Factură (localizat la `deltatech_stock_delivery/index.md`)

- **Nume Tehnic:** `deltatech_stock_delivery`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_delivery`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_delivery`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul îmbunătățește integrarea dintre Contabilitatea Odoo și Inventar, oferind acces rapid la operațiunile de depozit asociate, direct din factură. Adaugă un buton de „Livrare" sau „Recepție" în formularul de factură, în funcție de tipul documentului (factură client sau factură furnizor), permițând utilizatorilor să vizualizeze imediat transferurile de stoc legate de comenzile de vânzare/cumpărare ale facturii respective. Astfel, contabilii și gestionarii de depozit pot verifica mai ușor livrările fizice față de documentele financiare, îmbunătățind trasabilitatea și reducând timpul pierdut la căutarea documentelor conexe.

#### 2. Funcționalități Cheie

- Adaugă un buton „Livrare" (Delivery) sau „Recepție" (Reception) în vizualizarea facturii, în funcție de tipul acesteia (factură client sau factură furnizor).
- Permite utilizatorilor să vizualizeze rapid toate transferurile de stoc (livrări sau recepții) asociate facturii curente.
- Fluidizează fluxul de lucru pentru contabili și gestionarii de depozit care trebuie să verifice expedierile fizice față de documentele financiare.
- Îmbunătățește trasabilitatea și reduce timpul petrecut căutând documentele legate.

#### 3. Dependențe

- `account`
- `stock`
- `purchase`
- `sale`

#### 4. Componente Cheie

**Vizualizări**

- `views/account_invoice_view.xml`: Extinde formularul de factură (`account.move`) pentru a adăuga butonul de acces rapid către livrările/recepțiile asociate.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): leagă facturile de transferurile de stoc (facturare livrări).
- [deltatech_invoice_picking_automatically](../deltatech_invoice_picking_automatically/index.md): automatizează crearea facturilor din transferuri de stoc.
- [deltatech_invoice_receipt](../deltatech_invoice_receipt/index.md): creează recepția pornind de la factură.
- [deltatech_account](../deltatech_account/index.md): adaugă grupul de butoane în factură (dependență opțională, comentată în manifest).
