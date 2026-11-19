# Batch Reception Note (localizat la `deltatech_reception_note/index.md`)

- **Nume Tehnic:** `deltatech_reception_note`
- **Versiune:** `19.0.0.1.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_reception_note
- **Cale Locală:** odoo-addons/deltatech/deltatech_reception_note
- **Ultima Ingestie:** `2026-11-19`

#### 1. Sumar

Modulul permite recepția mărfii de la furnizor pe note de recepție care consumă cantitățile deschise din mai multe comenzi de achiziție deodată, în loc să se valideze recepția fiecărei comenzi separat. Este util când o singură livrare acoperă mai multe comenzi sau când o comandă sosește în mai multe livrări.

#### 2. Funcționalități Cheie

- **Tipuri de comenzi de achiziție:** fiecare comandă primește un *Type*: *Normal* (comanda obișnuită), *RFQ Only* (cerere care păstrează cantitățile încă așteptate de la furnizor; nu poate fi confirmată și are butonul *Set as sent*) și *Reception Note* (livrarea efectiv primită, cu *Delivery Note No* al furnizorului).
- **Create reception note:** pe o comandă *Normal*, *Actions > Create reception note* mută cantitățile deschise într-o comandă nouă *RFQ Only* în starea *RFQ Sent*, cu același furnizor, aceeași companie, monedă, poziție fiscală, termene de plată, prețuri și taxe, și cu cantitatea încă nerecepționată pe fiecare linie. Recepțiile *Ready* ale comenzii sursă se anulează, deci marfa se primește doar prin note de recepție.
- **Nota de recepție:** o comandă de tip *Reception Note* conține produsele și cantitățile livrate. La confirmare, cantitățile se scad din comenzile *RFQ Only* trimise ale aceluiași furnizor și ale aceleiași companii, cele mai vechi primele, în unitatea de măsură a produsului; recepția se creează prin confirmarea standard. O comandă *RFQ Only* complet consumată este marcată ca goală (*Empty*). O reconfirmare a unei note deja confirmate nu consumă a doua oară.
- **Ignore quantities:** dacă un produs sau o cantitate nu se găsește pe un RFQ Only trimis, confirmarea se oprește cu un mesaj care indică soluția; bifa *Ignore quantities* pe nota de recepție permite confirmarea oricum, iar cantitățile forțate sunt listate în chatter.
- **Meniuri și filtre:** Achiziții > Note de recepție are trei intrări: *Prepare reception note* (notele neconfirmate sau nefacturate), *To arrive* (transferuri de intrare în starea *Ready*) și *To invoice* (transferuri de intrare în starea *Done*). Listele de achiziții afișează *Type* și *Date sent* ca coloane opționale, iar căutarea are filtrele *Not empty* / *Empty* pentru comenzile *RFQ Only*.
- **Limitări:** modulul nu adaugă un document tipărit propriu — nota de recepție se tipărește cu rapoartele standard ale comenzii de achiziție; *To invoice* listează toate transferurile de intrare finalizate, facturate sau nu.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): adaugă câmpurile `reception_type` (Normal / RFQ Only / Reception Note), `delivery_note_no`, `is_empty`, `date_sent` și `ignore_quantities`. Conține logica de confirmare (`button_confirm`, care refuză comenzile `rfq_only` și consumă din RFQ-uri doar notele confirmate acum), de marcare ca trimis (`set_sent`), de reducere a cantităților din RFQ-uri cu conversie de unități de măsură (`reduce_from_rfq`) și de verificare a golirii comenzii (`check_if_empty`).
- `reception.note.create` (`models.TransientModel`): wizard care creează note de recepție pe baza comenzilor selectate, generând comenzi noi de tip `rfq_only` cu cantitățile rămase de recepționat și anulând recepțiile rezervate.

**Vizualizări**

- `purchase_order_form_discount`: adaugă pe formularul comenzii câmpurile de tip, dată trimitere, notă de livrare și *Ignore quantities*, și înlocuiește butoanele de confirmare în funcție de `reception_type`.
- `purchase_order_form_sent`: adaugă butonul „Set as sent" pentru comenzile de tip `rfq_only`.
- `purchase_order_draft_tree_type` / `purchase_order_view_tree_type` / `purchase_order_tree_type`: coloanele opționale *Type* și *Date sent* în listele de achiziții.
- `purchase_order_search_type`: filtrele „Not empty" / „Empty" pentru RFQ-uri.
- `view_reception_note_create_form`: formularul wizard-ului de creare a notei de recepție.

**Acțiuni Automate / Acțiuni Server**

- `prepare_reception_note_action`: acțiune de fereastră pentru pregătirea notelor de recepție (comenzi de tip `note`).
- `view_reception_assigned_action` / `view_receptions`: acțiuni pentru recepțiile de sosit (state `assigned`) și de facturat (state `done`).
- `action_reception_note_create`: acțiune contextuală (binding pe `purchase.order`, formular) care lansează wizard-ul de creare a notei de recepție.

#### 5. Conexiuni

- `purchase_stock`: dependența directă; confirmarea standard a comenzii de achiziție generează recepția pentru nota de recepție.
