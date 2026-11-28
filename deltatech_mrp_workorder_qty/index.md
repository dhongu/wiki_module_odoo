# Work Order Processed Quantity

- **Nume Tehnic:** `deltatech_mrp_workorder_qty`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_mrp_workorder_qty
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_mrp_workorder_qty`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența cantității procesate pe fiecare operație (ordin de lucru) a unui ordin de fabricație, pe tranșe. Odoo standard folosește o singură cantitate de produs pentru toate operațiile; aici fiecare operație are propriul jurnal (de exemplu 10 bucăți tăiate în prima zi, 10 vopsite și alte 10 tăiate a doua zi), fără mișcări de stoc pe tranșă.

#### 2. Funcționalități Cheie

- Înregistrarea cantității pe operație din formularul ordinului de lucru (butonul **Register Quantity**) sau din meniul operației din **Shop Floor**.
- Fiecare înregistrare e logată cu dată, utilizator și notă; valorile negative corectează greșelile; tab-ul *Processed Quantity* listează tranșele.
- O operație nu poate depăși cantitatea procesată de operațiile de care depinde și nici cantitatea ordinului de fabricație. Pe rutări liniare operațiile sunt înlănțuite automat; pe rutări neliniare se activează *Work Order Dependencies* și dependențele pe BoM.
- Coloane opționale **Processed Quantity** și **Remaining to Process** în lista ordinelor de lucru.
- Cardul operației din Shop Floor afișează cantitatea procesată și cea disponibilă sub cea planificată.
- **Continuous Production** (pe BoM, tab *Miscellaneous*): operația următoare pornește imediat ce prima tranșă e înregistrată pe cea anterioară; *Mark as done* e refuzat cât timp o operație anterioară e deschisă, iar după închiderea lor loghează cantitatea rămasă.
- Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mrp_workorder`

#### 4. Componente Cheie

**Modele**

- `mrp.workorder.qty.log`: jurnalul tranșelor procesate (dată, utilizator, cantitate, notă).
- `mrp.workorder.qty.wizard`: dialogul de înregistrare a cantității.
- `mrp.workorder` (extins): cantitate procesată, rest de procesat, limitări față de operațiile anterioare.

**Vizualizări**

- `views/mrp_workorder_views.xml`: formularul și lista ordinului de lucru.
- `wizard/mrp_workorder_qty_wizard_views.xml`: dialogul de înregistrare.
- Șabloane OWL pentru Shop Floor (`mrp_menu_dialog.xml`, `mrp_display_record.xml`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `mrp`: ordinele de fabricație și BoM-urile pe care se aplică limitele.
