# Notă de Recepție pe Bază de Cereri de Ofertă (localizat la `deltatech_reception_note/index.md`)

- **Nume Tehnic:** `deltatech_reception_note`
- **Versiune:** `19.0.0.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_reception_note`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_reception_note`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă un instrument specializat pentru gestionarea notelor de recepție în masă (batch) în cadrul modulelor de stoc și achiziții din Odoo. Este conceput pentru a simplifica procesul de recepție a mai multor articole sau de gestionare a documentației de recepție în volum mare, permițând gruparea mai multor cereri de ofertă (RFQ) într-o singură notă de recepție pentru o urmărire și o documentare mai ușoară între aprovizionare și operațiunile de depozit.

#### 2. Funcționalități Cheie

- **Procesarea recepției în masă (batch):** Adaugă un wizard dedicat pentru crearea și gestionarea notelor de recepție în volum, permițând gruparea mai multor comenzi de achiziție într-o singură notă de recepție.
- **Tipuri de comandă diferențiate:** Introduce un tip de comandă de achiziție (Normal, RFQ Only, Notă de recepție) care controlează fluxul de confirmare și de recepție.
- **Integrare cu fluxul de stoc:** Se integrează cu modulul `purchase_stock` pentru a asigura un flux de date consistent între aprovizionare și operațiunile de depozit.
- **Reducerea automată din RFQ:** La confirmarea unei note de recepție, cantitățile sunt scăzute automat din cererile de ofertă (RFQ) deschise ale aceluiași furnizor, cu validări de cantitate și opțiunea de a forța cantitățile mai mari (`Ignore quantities`).
- **Documentație îmbunătățită și meniuri dedicate:** Oferă vizualizări și meniuri specializate (pregătire notă de recepție, recepții de sosit, recepții de facturat) pentru informații de recepție sintetizate, utile pentru audit intern și verificarea furnizorilor.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): Adaugă câmpurile `reception_type` (Normal / RFQ Only / Reception Note), `delivery_note_no`, `is_empty`, `date_sent` și `ignore_quantities`. Conține logica de confirmare (`button_confirm`), de marcare ca trimis (`set_sent`), de reducere a cantităților din RFQ-uri (`reduce_from_rfq`) și de verificare a golirii comenzii (`check_if_empty`).
- `reception.note.create` (`models.TransientModel`): Wizard care creează note de recepție pe baza comenzilor selectate, generând comenzi noi de tip `rfq_only` cu cantitățile rămase de recepționat și anulând picking-urile rezervate.

**Vizualizări**

- `purchase_order_form_discount`: Adaugă pe formularul de comandă câmpurile de tip recepție și note de livrare și înlocuiește butoanele de confirmare în funcție de `reception_type`.
- `purchase_order_form_sent`: Adaugă butonul „Set as sent” pentru comenzile de tip `rfq_only`.
- `purchase_order_search_type`: Adaugă filtrele „Not empty” / „Empty” pentru RFQ-uri.
- `view_reception_note_create_form`: Formularul wizard-ului de confirmare a creării notei de recepție.

**Acțiuni Automate / Acțiuni Server**

- `prepare_reception_note_action`: Acțiune de fereastră pentru pregătirea notelor de recepție (comenzi de tip `note`).
- `view_reception_assigned_action` / `view_receptions`: Acțiuni pentru recepțiile de sosit (state `assigned`) și de facturat (state `done`).
- `action_reception_note_create`: Acțiune contextuală (binding pe `purchase.order`, formular) care lansează wizard-ul de creare a notei de recepție.

#### 5. Conexiuni

- [deltatech_fast_purchase](../deltatech_fast_purchase/index.md): extindere a fluxului de achiziție din aceeași suită deltatech.
- [deltatech_purchase_price](../deltatech_purchase_price/index.md): logică de prețuri pe comenzile de achiziție, complementară fluxului de recepție.
- [deltatech_stock_account](../deltatech_stock_account/index.md): contabilizarea mișcărilor de stoc rezultate din recepții.
