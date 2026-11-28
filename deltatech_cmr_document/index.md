# CMR Document

- **Nume Tehnic:** `deltatech_cmr_document`
- **Versiune:** `20.0.1.3.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_cmr_document
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cmr_document`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul tipărește scrisoarea de transport internațional CMR (casetele 1-24 din formularul model IRU) direct dintr-un transfer de stoc, în cele trei exemplare cerute de Convenția CMR. Convenția reglementează transportul rutier internațional între statele contractante, printre care toate statele UE; formularul se tipărește în engleză și în alte nouă limbi europene. Părțile, locurile, greutatea brută și volumul se preiau din transfer și din produse, deci documentul nu se mai completează manual.

#### 2. Funcționalități Cheie

- **Părți și locuri din transfer:** expeditorul, destinatarul, locul de preluare și locul de livrare vin din transfer, deci recepțiile, returnările și transferurile fără comandă de vânzare se tipăresc corect; la recepție, expeditorul și destinatarul se inversează.
- **Trei exemplare** (art. 5): pentru expeditor, destinatar și transportator, denumite și colorate lângă titlu (roșu, albastru, verde), plus un al patrulea exemplar opțional, cu scop administrativ.
- **Mențiunea art. 6 (1) k** (transportul este supus Convenției) tipărită pe fiecare exemplar.
- **Fila CMR pe transfer:** transportator succesiv, numere de înmatriculare camion/remorcă, șofer, documente anexate, instrucțiunile expeditorului, plata transportului, rambursul, rezervele și convențiile speciale; datele uzuale ale firmei de transport se copiază pe transfer la alegerea ei. Transportatorul și firma de transport se aleg în fila *Additional Info* și devin doar citire după finalizare.
- **Număr CMR** dintr-o secvență proprie fiecărei companii (`CMR/AAAA/NNNNN`), atribuit la prima tipărire.
- **Greutate brută** cu tara ambalajelor, cantități convertite în unitatea de măsură a produsului, colete numărate o singură dată pe transfer, rând de total. Peste 7 linii se tipărește o **listă de încărcare** după fiecare exemplar.
- **Mărfuri periculoase (ADR):** număr ONU, denumire oficială, clasă, grup de ambalare și cod de tunel pe produs, tipărite în caseta 9 în ordinea ADR 5.4.1.1.1; greutatea, volumul și codul HS (casetele 10-12) vin din fișa produsului.
- **Nouă limbi:** formularul urmează limba adresei de livrare (engleză, română, germană, franceză, italiană, spaniolă, olandeză, poloneză, maghiară, bulgară), cu eticheta engleză sub fiecare casetă pe formularele neenglezești (opțiune în setări).
- **Unde apare:** raportul este oferit în meniul *Print* doar pe tipurile de operațiune la care este bifat **CMR Document** (implicit livrările); setări de companie în *Inventory > Settings > Shipping* (al patrulea exemplar, etichete în engleză).
- Fluxul complet, cu capturi și limitările cunoscute, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `stock`
- `delivery`
- `stock_delivery`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): câmpurile fila CMR (șofer/delegat, numere de înmatriculare, documente anexate, instrucțiuni, plata transportului, rezerve) și numărul CMR.
- `stock.picking.type` (extins): bifa **CMR Document** care decide unde apare raportul.
- `product.template` (extins): câmpurile ADR (număr ONU, denumire, clasă, grup de ambalare, cod de tunel).
- `delivery.carrier` și `res.partner` (extinse): firma de transport și datele ei uzuale (plăcuțe, șofer).
- `res.company` și `res.config.settings` (extinse): secvența CMR pe companie și setările exemplarului al patrulea și ale etichetelor în engleză.
- `ir.actions.report` (extins): afișarea condiționată a raportului în meniul *Print*.

**Vizualizări**

- `view_picking_add_delegate_form`, `view_picking_add_carrier_partner_form`: fila CMR și firma de transport pe transfer.
- `view_picking_type_form_cmr`: bifa CMR pe tipul de operațiune.
- `product_template_form_view_adr`, `product_template_form_view_net_weight_fallback`: câmpurile ADR și greutatea pe produs.
- `view_delivery_carrier_add_partner_form`, `view_partner_form_cmr`: firma de transport pe metoda de livrare și datele CMR pe partener.
- `res_config_settings_view_form_cmr`: setările CMR din Inventory.
- Rapoarte QWeb: `report_cmr_document`, `report_cmr_document_main`, `report_cmr_loading_list`, plus formatul de hârtie dedicat; `action_report_picking_slip` pentru bonul de livrare.

**Acțiuni Automate / Acțiuni Server**

Nu definește `ir.cron` sau acțiuni server; `ir_sequence.xml` creează secvența CMR (câte una pe companie).

#### 5. Conexiuni

- `delivery`: metoda de livrare și transportatorul propus pe document.
- `stock`: transferul de stoc (`stock.picking`) este documentul din care se tipărește CMR-ul.
