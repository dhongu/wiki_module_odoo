# Livrare / Recepție din Factură (localizat la `deltatech_stock_delivery/index.md`)

- **Nume Tehnic:** `deltatech_stock_delivery`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_delivery
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_delivery`
- **Ultima Ingestie:** `2026-10-26`

#### 1. Sumar

Acest modul îmbunătățește integrarea dintre Contabilitatea Odoo și Inventar, oferind acces rapid la operațiunile de depozit asociate, direct din factură. Adaugă un buton de „Livrare" sau „Recepție" în formularul de factură, în funcție de tipul documentului (factură client sau factură furnizor), permițând utilizatorilor să vizualizeze imediat transferurile de stoc legate de comenzile de vânzare/cumpărare ale facturii respective. Astfel, contabilii și gestionarii de depozit pot verifica mai ușor livrările fizice față de documentele financiare, îmbunătățind trasabilitatea și reducând timpul pierdut la căutarea documentelor conexe.

#### 2. Funcționalități Cheie

- Adaugă un buton „Livrare" (Delivery) sau „Recepție" (Reception) în vizualizarea facturii, în funcție de tipul acesteia (factură client/notă de credit client sau factură furnizor/notă de credit furnizor).
- Permite utilizatorilor să vizualizeze rapid transferurile de stoc finalizate (livrări sau recepții) asociate facturii curente, identificate prin liniile de comandă de vânzare/cumpărare legate de liniile facturii. Dacă există un singur transfer, se deschide direct formularul acestuia; dacă sunt mai multe, o listă filtrată.
- Dacă factura nu are niciun transfer finalizat asociat, afișează eroarea „This invoice has no deliveries".
- Fluidizează fluxul de lucru pentru contabili și gestionarii de depozit care trebuie să verifice expedierile fizice față de documentele financiare.
- Îmbunătățește trasabilitatea și reduce timpul petrecut căutând documentele legate.

#### 3. Dependențe

- `account`
- `stock`
- `purchase`
- `sale`
- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins, `models/account_invoice.py`): metoda `invoice_print_delivery` colectează transferurile finalizate legate de liniile facturii (prin `sale_line_ids` și `purchase_line_id`) și întoarce acțiunea de afișare a lor.

**Vizualizări**

- `views/account_invoice_view.xml` (`invoice_form`): Extinde formularul de factură (`account.view_move_form`) cu butoane de tip stat în caseta de butoane, „Delivery" pentru facturile client și „Reception" pentru cele furnizor.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate.*

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): leagă facturile de transferurile de stoc (facturare livrări).
- [deltatech_invoice_picking_automatically](../deltatech_invoice_picking_automatically/index.md): automatizează crearea facturilor din transferuri de stoc.
- [deltatech_invoice_receipt](../deltatech_invoice_receipt/index.md): creează recepția pornind de la factură.
- [deltatech_account](../deltatech_account/index.md): adaugă grupul de butoane în factură (dependență opțională, comentată în manifest).
