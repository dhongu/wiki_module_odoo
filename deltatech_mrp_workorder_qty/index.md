# Work Order Processed Quantity (localizat la `deltatech_mrp_workorder_qty/index.md`)

- **Nume Tehnic:** `deltatech_mrp_workorder_qty`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_mrp_workorder_qty`
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_mrp_workorder_qty`
- **Ultima Ingestie:** `2026-11-13`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul urmărește cantitatea procesată pe fiecare comandă de lucru a unui ordin de producție, pe tranșe. În Odoo standard, o singură cantitate de produs este comună tuturor operațiilor; aici fiecare operație își ține propriul jurnal (de exemplu 10 bucăți tăiate în prima zi, 10 vopsite și alte 10 tăiate a doua zi). Astfel se vede exact câte piese au trecut prin fiecare pas, fără mișcări de stoc pentru fiecare tranșă.

#### 2. Funcționalități Cheie

- Înregistrarea cantității procesate pe operație, din formularul comenzii de lucru (butonul **Register Quantity**) sau din meniul operației din **Shop Floor** (**Register Processed Quantity**).
- Fiecare înregistrare este logată cu dată, utilizator și notă; valorile negative corectează greșelile.
- Limitare: o operație nu poate depăși cantitatea procesată de operațiile de care depinde și nici cantitatea ordinului de producție. Pe trasee liniare operațiile se înlănțuie automat; pe trasee neliniare e nevoie de *Work Order Dependencies* și de dependența setată pe fiecare operație (fără dependență, limita nu se aplică).
- Coloane noi, opționale, în lista comenzilor de lucru: **Processed Quantity** și **Remaining to Process**.
- Fila **Processed Quantity** pe comanda de lucru listează toate înregistrările.
- Cardul operației din Shop Floor afișează cantitatea procesată sub cea planificată.
- Operația nu se marchează *Mark as Done* până nu este procesată întreaga cantitate.

#### 3. Dependențe

- `mrp_workorder` (Enterprise)

#### 4. Componente Cheie

**Modele**

- `mrp.workorder` (extins): câmpurile `qty_log_ids`, `qty_processed`, `qty_processed_remaining`, limita de cantitate și acțiunea de înregistrare.
- `mrp.workorder.qty.log`: jurnalul tranșelor (comandă de lucru, dată, utilizator, cantitate, notă).
- `mrp.workorder.qty.wizard` (tranzitoriu): dialogul de înregistrare a cantității.

**Vizualizări**

- `mrp_production_workorder_form_view_qty`: buton și filă pentru jurnal pe comanda de lucru.
- `mrp_production_workorder_tree_view_qty`: coloanele de cantitate procesată/rămasă.
- `mrp_workorder_qty_wizard_form`: dialogul de înregistrare.
- Șabloane OWL pentru Shop Floor (`mrp_menu_dialog.xml`, `mrp_display_record.xml`).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- Nicio conexiune funcțională cu alte module documentate: lucrează direct pe `mrp.workorder` (`mrp`) și pe Shop Floor (`mrp_workorder`, Enterprise).
