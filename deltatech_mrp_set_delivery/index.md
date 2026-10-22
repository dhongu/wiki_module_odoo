# Deltatech restrict incomplete set deliveries (localizat la `deltatech_mrp_set_delivery/index.md`)

- **Nume Tehnic:** `deltatech_mrp_set_delivery`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_set_delivery
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_set_delivery`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul previne livrarea unui set incomplet: când un produs vândut ca set (listă de materiale de tip **Kit**) este marcat ca restricționat, livrarea nu poate fi validată decât dacă toate componentele sunt prezente în același transfer, în proporțiile din lista de materiale.

#### 2. Funcționalități Cheie

- **Activare per listă de materiale**: opțiunea **Restrict Incomplete Delivery** apare doar pe listele de tip Kit (**Manufacturing > Products > Bills of Materials**); kiturile fără ea se livrează ca în Odoo standard.
- **Toate componentele în transfer**: dacă lipsește o componentă, validarea se oprește cu un mesaj care numește produsul, transferul și setul.
- **Cantități în proporție**: cantitatea efectuată a fiecărei componente trebuie să respecte raportul din lista de materiale față de prima componentă, comparat cu rotunjirea unității de măsură; o diferență oprește validarea și numește componenta.
- **Livrări parțiale permise**: se pot livra mai puține seturi decât cele comandate (ex. 1 din 2), cât timp componentele rămân în proporție.
- **Doar livrări din vânzări**: verificarea se aplică liniilor de transfer generate dintr-o linie de comandă de vânzare; celelalte transferuri nu sunt afectate.
- **Mesaj de blocare clar**: la validarea mai multor transferuri odată, erorile tuturor sunt afișate într-un singur mesaj („Set delivery restriction”) și niciun transfer nu este validat.

#### 3. Dependențe

- `sale_mrp`

#### 4. Componente Cheie

**Modele**

- `mrp.bom` (extins): câmpul boolean `restrict_incomplete_delivery`.
- `stock.picking` (extins): `button_validate` apelează `check_complete_set` pentru fiecare transfer și ridică `UserError` cu erorile adunate.

**Vizualizări**

- `mrp_bom_form_view`: moștenește formularul listei de materiale și adaugă opțiunea după câmpul `type`, vizibilă doar pentru tipul Kit.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `mrp`: modulul extinde listele de materiale de tip Kit (phantom).
- `stock`: validarea transferurilor de livrare.
