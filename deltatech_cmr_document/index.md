# CMR Document (localizat la `deltatech_cmr_document/index.md`)

- **Nume Tehnic:** `deltatech_cmr_document`
- **Versiune:** `19.0.1.3.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_cmr_document
- **Cale Locală:** `odoo-addons/bitshop/deltatech_cmr_document`
- **Ultima Ingestie:** `2026-11-10`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul tipărește scrisoarea de transport internațional CMR (casetele 1–24 din formularul-model IRU) direct dintr-un transfer de stoc, în cele trei exemplare originale cerute de Convenția CMR. Expeditorul, destinatarul și locurile de preluare și de livrare se citesc din transfer, deci documentul iese corect și la recepții, retururi sau transferuri fără comandă de vânzare. Greutatea brută, volumul, mărfurile periculoase (ADR) și datele transportatorului se completează automat, iar formularul urmează limba adresei de livrare.

#### 2. Funcționalități Cheie

- **Părți și locuri din transfer**: expeditorul, destinatarul, locul de preluare și locul de livrare vin din transferul însuși; la o recepție, expeditorul și destinatarul sunt inversați.
- **Trei exemplare** (art. 5): pentru expeditor, destinatar și transportator, denumite și colorate lângă titlu (roșu, albastru, verde), plus un al patrulea exemplar opțional, cu scop administrativ (setarea **Fourth CMR Copy**, dezactivată implicit).
- **Mențiunea art. 6 (1) k** (transportul este supus Convenției) tipărită pe fiecare exemplar.
- **Tab CMR pe transfer**: transportator succesiv, numere de înmatriculare camion și remorcă, delegat (șofer), documente anexate, instrucțiunile expeditorului, plata transportului, ramburs, rezervele transportatorului și acordurile speciale, fiecare tipărit în caseta sa. Tab-ul apare doar pe tipurile de operațiune la care CMR este activat.
- **Firma de transport**: pe contact (tab **Sales & Purchase**, grupul **CMR Transport**) se rețin numerele uzuale și delegatul; la alegerea firmei pe transfer se copiază, fără a suprascrie ce era deja completat. Firma se leagă de metoda de livrare prin câmpul **Transport Company**.
- **Număr CMR** dintr-o secvență, atribuit la prima tipărire.
- **Greutate brută și tabel de mărfuri**: cantități convertite în unitatea de măsură a produsului, colete numărate o singură dată pe transfer, rând de tară și rând de total. Peste 7 linii, după fiecare exemplar se tipărește o **listă de încărcare**.
- **Cod HS** și greutate/volum preluate din produs (tab **Inventory**, grupul **Logistics**).
- **Mărfuri periculoase (ADR)**: număr UN, denumire oficială de transport, clasă, grup de ambalare și cod de tunel pe produs, tipărite în caseta 9 în ordinea ADR 5.4.1.1.1.
- **Zece limbi**: formularul urmează limba adresei de livrare (engleză, română, germană, franceză, italiană, spaniolă, olandeză, poloneză, maghiară, bulgară), cu eticheta în engleză sub fiecare casetă pe formularele neenglezești (setarea **English Labels on the CMR**, activă implicit).
- **Unde apare**: raportul este oferit în meniul **Print** doar pe tipurile de operațiune la care este bifat **CMR Document** (implicit livrările); se poate tipări și din listă, pentru mai multe transferuri deodată.
- **Limitări cunoscute**: doar etichetele fixe urmează limba adresei; caseta 20 (cheltuieli) se completează manual; descrierea ADR nu include numărul și felul coletelor (se adaugă în instrucțiunile expeditorului) și nu se calculează pragul de 1000 de puncte din ADR 1.1.3.6.

#### 3. Dependențe

- `base`
- `stock`
- `delivery`
- `stock_delivery`

#### 4. Componente Cheie

Secțiunile Sumar și Funcționalități Cheie sunt acoperite de `readme/DESCRIPTION.md` și `readme/USAGE.md`; mai jos sunt doar extinderile principale, verificate în `models/` și `views/`.

**Modele**

- `stock.picking` (extins): câmpurile CMR (`cmr_number`, `cmr_truck_plate`, `cmr_trailer_plate`, `cmr_successive_carrier_id`, `cmr_documents`, `cmr_sender_instructions`, `cmr_carriage_payment`, `cmr_cod_amount`, `cmr_carrier_reservations`, `cmr_special_agreements`), delegatul (`delegate_id`), firma de transport (`carrier_partner_id`) și părțile/datele calculate pentru casetele 1–4. Câmpurile Many2one către `res.partner` au `index=True`, pentru a evita scanări secvențiale la ștergerea sau unificarea partenerilor pe baze mari.
- `stock.picking.type` (extins): bifa `cmr_document`, care activează CMR pe tipul de operațiune.
- `product.template` (extins): câmpurile ADR (`cmr_un_number`, `cmr_shipping_name`, `cmr_adr_class`, `cmr_packing_group`, `cmr_tunnel_code`) și `l10n_ro_net_weight`.
- `res.partner` (extins): numerele uzuale ale firmei de transport și delegatul (`cmr_delegate_id`).
- `delivery.carrier` (extins): firma de transport asociată metodei de livrare (`partner_id`).
- `res.company` / `res.config.settings` (extinse): setările `cmr_fourth_copy` și `cmr_english_labels`.
- `ir.actions.report` (extins): atribuie numărul CMR la randarea raportului.

**Vizualizări**

- `report_cmr_document` / `report_cmr_document_main`: șabloanele QWeb ale formularului CMR (casetele 1–24, exemplarele).
- `report_cmr_loading_list`: lista de încărcare tipărită după fiecare exemplar, la peste 7 linii.
- `action_report_picking_slip`: acțiunea de raport „CMR Document”, din meniul Print.
- `paperformat_a4_cmr`: formatul de hârtie A4 dedicat.
- `res_config_settings_view_form_cmr`: setările din Inventory, secțiunea Shipping.
- `view_picking_add_delegate_form`, `view_picking_add_carrier_partner_form`, `view_picking_type_form_cmr`, `view_partner_form_cmr`, `product_template_form_view_adr`, `view_delivery_carrier_add_partner_form`: câmpurile suplimentare pe livrare, tipul de operațiune, contact, produs și metoda de livrare (`views/additional_fields.xml`).

**Acțiuni Automate / Acțiuni Server**

- `sequence_cmr` (`ir.sequence`, „CMR Consignment Note”): secvența numărului CMR, folosită la prima tipărire. Modulul nu definește acțiuni `ir.cron` sau `base.automation`.

#### 5. Conexiuni

- `stock`: transferul de stoc (`stock.picking`) este documentul-sursă din care se generează CMR-ul.
- `delivery`: metoda de livrare indică firma de transport și transportatorul folosit pe document.
- `stock_delivery`: formularul de livrare cu transportator, în care se adaugă firma de transport.
