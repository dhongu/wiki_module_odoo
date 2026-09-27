# Deltatech Sale Order Stage (localizat la `deltatech_sale_stage/index.md`)

- **Nume Tehnic:** `deltatech_sale_stage`
- **Versiune:** `20.0.1.2.6`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_sale_stage`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_stage`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Acest modul ajută echipa de vânzări să țină sub control fiecare comandă prin introducerea unui sistem de faze (etape) personalizabile pentru comenzile de vânzare. În loc să se bazeze doar pe statusurile standard din Odoo (Ciornă, Confirmat, Finalizat), echipa își poate defini propriile faze interne — precum *Confirmat*, *Pregătit*, *Expediat*, *Livrat* — și poate urmări exact în ce etapă a procesului de onorare se află fiecare comandă. Fazele avansează automat pe măsură ce comanda parcurge fluxul standard (trimitere ofertă, confirmare, facturare, anulare) și pe măsură ce livrările sunt validate sau își schimbă statusul de curierat, oferind vizibilitate completă echipelor de back-office.

#### 2. Funcționalități Cheie

- **Vizibilitate completă pentru back-office:** fiecare comandă de vânzare afișează faza curentă sub forma unui badge colorat, ușor de identificat dintr-o privire.
- **Configurare flexibilă a fazelor:** se pot defini oricâte faze sunt necesare, fiecare cu nume, culoare și secvență. Fazele se gestionează din Vânzări → Configurare → Faze comenzi de vânzare.
- **Progresie automată a fazelor:** fazele avansează automat odată cu fluxul standard Odoo — ofertă trimisă → *Trimis*, comandă confirmată → *Confirmat*, comandă facturată → *Facturat*, comandă anulată → *Anulat*.
- **Actualizare a fazei în funcție de livrare:** la validarea unei expedieri sau la schimbarea statusului de livrare (preluat de curier, în tranzit, preavizat/AWB generat, livrat clientului, refuzat), faza comenzii de vânzare asociate se actualizează automat, fără intervenție manuală.
- **Declanșare de acțiuni automate:** fiecărei faze i se poate atașa o acțiune de server opțională, care rulează automat când comanda intră în acea fază (notificări, actualizări de înregistrări, integrări).
- **Impunerea fluxului de comandă:** dacă pe o comandă ciornă se setează manual o fază marcată ca *Confirmat*, comanda este confirmată automat; dacă se setează o fază marcată ca *Anulat*, comanda este anulată — păstrând datele consecvente.
- **Căutare și grupare după fază:** comenzile de vânzare pot fi filtrate și grupate după fază direct din vizualizarea listă.
- **Faza implicită pe tipul de operațiune de depozit:** fiecărui tip de operațiune (ex. comenzi de livrare) i se poate atribui o fază implicită, aplicată automat la validarea livrării de acel tip.

#### 3. Dependențe

- `sale_stock`
- [deltatech_widget_many2one_badge](../deltatech_widget_many2one_badge/index.md)

#### 4. Componente Cheie

**Modele**

- `sale.order.phase`: definește fazele personalizabile ale comenzii de vânzare — nume, culoare, secvență, marcaje booleene (`send_email`, `confirmed`, `pre_advice`, `shipped`, `delivered`, `refused`, `invoiced`, `paid`, `canceled`) și o acțiune de server opțională (`action_id`).
- `sale.order` (extins): câmp `phase_id` (urmărit în chatter, `tracking=True`); avansează automat faza la trimiterea ofertei, confirmare și anulare (`action_quotation_sent`, `action_confirm`, `_action_cancel`); metoda `set_phase()` caută faza următoare potrivită pe baza marcajului cerut (și ține cont dacă există o tranzacție de plată reușită, favorizând fazele `paid`); `write()` declanșează acțiunea de server a noii faze și, dacă faza e marcată `confirmed`/`canceled`, forțează confirmarea/anularea comenzii.
- `account.move` (extins): la validarea unei facturi (`_post`), setează faza `invoiced` pe comenzile de vânzare complet facturate (verificare făcută explicit în modul, deoarece `sale.order._get_invoice_status` nu mai există în core-ul 20.0).
- `stock.picking.type` (extins): câmp `phase_id` — faza implicită asociată tipului de operațiune de depozit.
- `stock.picking` (extins): la validarea livrării (`_action_done`) preia faza implicită a tipului de operațiune; la schimbarea câmpului `delivery_state` (furnizat de `deltatech_delivery_status`) mapează statusurile de curierat pe faze: `in_transit`/`in_warehouse`/`in_delivery` → `shipped`, `pre_advice` → `pre_advice`, `delivered` → `delivered`, `refused` → `refused`.

**Vizualizări**

- `view_order_list` / `view_quotation_list` (extind `sale.view_order_tree` / `sale.view_quotation_tree`): badge-ul colorat al fazei (`widget="many2one_badge"`) în listele de comenzi și oferte.
- `view_order_form` (extinde `sale.view_order_form`): câmpul `phase_id` afișat ca badge pe formularul comenzii.
- `view_sales_order_filter` (extinde `sale.view_sales_order_filter`): filtru de căutare pe fază și grupare `group_by_phase`.
- `view_sale_order_phase_form` / `view_sale_order_phase_list`: formular și listă pentru gestionarea fazelor (`action_sale_order_phase`, meniu `menu_sale_order_phase` sub Vânzări → Configurare).
- `view_picking_type_form` (extinde `stock.view_picking_type_form`): câmpul `phase_id` (faza implicită) pe tipul de operațiune de depozit.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau `base.automation` definite de modul. Fiecare înregistrare `sale.order.phase` poate referi opțional o `ir.actions.server` (`action_id`), rulată automat de `sale.order.write()` când comanda intră în acea fază.

#### 5. Conexiuni

- [deltatech_marketplace_sale_stage](../deltatech_marketplace_sale_stage/index.md): depinde de acest modul, extinzând sistemul de faze pentru comenzile provenite din marketplace.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează statusurile de curierat (`delivery_state`) care declanșează schimbările automate de fază (preluat, AWB generat, livrat, refuzat).
