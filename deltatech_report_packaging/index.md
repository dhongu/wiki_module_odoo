# Report Packaging (localizat la `deltatech_report_packaging/index.md`)

- **Nume Tehnic:** `deltatech_report_packaging`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_report_packaging
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_packaging`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul calculează automat cantitățile de materiale de ambalare (plastic, lemn, hârtie, PET, sticlă, metal, aluminiu) folosite pentru produsele facturate, pornind de la o configurare a materialelor pe fiecare produs. La confirmarea unei facturi, cantitățile sunt recalculate pe baza liniilor facturii, iar dintr-o listă de facturi se poate genera un raport agregat cu totalul materialelor de ambalare consumate.

#### 2. Funcționalități Cheie

- Configurarea materialelor de ambalare (tip material și cantitate) direct pe fișa produsului (filă Inventar).
- Recalcularea automată a materialelor de ambalare pe factură la postarea acesteia (`action_post`).
- Buton de reîmprospătare manuală a materialelor de ambalare pe factură, pentru cazul în care liniile facturii s-au modificat.
- Filă dedicată "Packaging materials" pe formularul facturii, cu lista materialelor și cantităților calculate.
- Wizard de raport (acționabil din lista de facturi) care agregă cantitățile de materiale de ambalare pentru facturile selectate.

#### 3. Dependențe

- `account`
- `product`

#### 4. Componente Cheie

**Modele**

- `product.template` (extindere): adaugă `packaging_material_ids`, materialele de ambalare configurate pentru un produs.
- `packaging.product.material`: linie de configurare material-cantitate legată de un `product.template`.
- `account.move` (extindere): adaugă `packaging_material_ids` și metoda `refresh_packaging_material()` care recalculează materialele din liniile facturii; suprascrie `action_post()` pentru a declanșa recalcularea automată la postare (doar pentru facturi, nu pentru înregistrări contabile de tip `entry`).
- `packaging.invoice.material`: linie cu cantitatea unui tip de material calculată pentru o factură.
- `packaging.report.material` (tranzitoriu, wizard): agregă materialele de ambalare pentru facturile selectate (`active_ids` din context) și le afișează în raport.
- `packaging.report.material.line` (tranzitoriu): liniile de rezultat ale raportului wizard.

**Vizualizări**

- `product_template_form_view`: extinde formularul produsului cu grupul "Packaging materials" în fila Inventar.
- `account_move_form_view`: extinde formularul facturii cu fila "Packaging materials" (ascunsă pentru mișcări contabile de tip `entry`) și butonul "Refresh".
- `invoice_packaging_material_form`: formular wizard cu două stări (`choose`/`get`) pentru raportul agregat de materiale.

**Acțiuni Automate / Acțiuni Server**

- `action_packaging_wizard`: acțiune de fereastră legată (`binding_model_id`) de lista de facturi (`account.move`), disponibilă ca acțiune contextuală în vizualizarea listă, care deschide wizard-ul de raport materiale de ambalare.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale suplimentare, în afara dependențelor directe (`account`, `product`).
