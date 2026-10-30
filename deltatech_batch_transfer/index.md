# Batch Transfer Extension (localizat la `deltatech_batch_transfer/index.md`)

- **Nume Tehnic:** `deltatech_batch_transfer`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_batch_transfer
- **Cale Locală:** odoo-addons/deltatech/deltatech_batch_transfer
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde transferurile în lot (batch picking) din Odoo și oferă operatorilor de depozit mai mult control asupra loturilor cu transferuri „goale” sau procesate parțial. Evită comportamentul standard, în care la validarea lotului sunt validate și transferurile cu toate cantitățile zero, și adaugă un asistent „Prepare Batch” care grupează rapid recepțiile sau livrările din comenzile de achiziție/vânzare într-un singur lot. Câmpuri suplimentare, un tab cu liniile recepționate și un raport de livrări ajută la organizarea și trasabilitatea loturilor.

#### 2. Funcționalități Cheie

- **Gestionarea transferurilor goale la validare**: la apăsarea butonului **Validate** pe lot, transferurile fără nicio cantitate efectuată se tratează după parametrul de sistem `deltatech_batch_keep_pickings` (**Setări → Tehnic → Parametri → Parametri de sistem**):
  - *parametru absent* (implicit, recomandat) — transferurile goale sunt scoase din lot și se validează doar cele cu cantități; cele scoase pot fi adăugate manual într-un alt lot; dacă toate sunt goale, lotul rămâne gol;
  - *parametru `True`* — transferurile goale rămân în lot, dar nu sunt procesate, ca să fie tratate ulterior (nerecomandat în interfața barcode).
- **Asistentul Prepare Batch** (**Inventar → Managementul depozitului → Prepare batch**, sau acțiunea „Prepare batch” din lista comenzilor de vânzare, care precompletează clientul și modul *Sale*): se aleg **Partner**, **Responsible**, **Reference**, **Mode** (*Purchase* = recepții, *Sale* = livrări) și opțional **Set done qty**, cu o listă de produse/cantități (în modul Purchase) care limitează produsele incluse. La confirmare se creează un lot confirmat cu transferurile deschise ale partenerului, se rezervă stocul și se deschide lotul. Cu *Set done qty* liniile primesc cantitatea alocată și sunt marcate ca procesate; fără bifă rămân doar cantitățile cerute, rezervate. Cantitatea peste cea rezervată apare ca cantitate suplimentară.
- Buton **Add to batch** pe transferul care nu e încă în lot și nu e finalizat sau anulat; deschide dialogul standard Odoo.
- Câmpuri suplimentare pe lot: **Direction** (*Incoming* / *Outgoing*, doar citire), **Reference** și **Note**.
- Tab **Received** pe loturile de intrare, cu liniile de mișcare cu cantitate peste zero (cu aldine) față de cele cu cantitate zero (estompate).
- Raport PDF **Deliveries** (**Print → Deliveries** pe lot), cu documentele de livrare ale tuturor transferurilor din lot într-o singură acțiune.
- Fișa consultant detaliază fluxul pas cu pas; nu este refăcută aici.

#### 3. Dependențe

- `stock`
- `stock_picking_batch`
- `sale_stock`
- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking.batch` (extins): `direction`, `reference`, `note`, `received_move_line_ids`; `action_done()` și `action_cancel()` tratează transferurile goale.
- `stock.picking` (extins): `button_validate()` și `add_to_batch()`.
- `stock.prepare.batch` (wizard): `partner_id`, `mode`, `user_id`, `reference`, `set_done_qty`, `line_ids`; `attach_pickings()` creează lotul, iar `_allocate_line_quantities()` alocă cantitățile pe liniile de mișcare cu API-ul Odoo 19.
- `stock.prepare.batch.line` (wizard): produs, `quantity` și `additional_quantity` pentru fiecare linie cerută.

**Vizualizări**

- `stock_prepare_batch_form`: formularul asistentului Prepare Batch.
- `view_picking_form`: butonul Add to batch pe transfer.
- `batch_form_view_selected_lines` și `batch_view_move_line_tree`: tabul Received pe lot și lista liniilor de mișcare.

**Acțiuni Automate / Acțiuni Server**

- `action_prepare_batch`: meniul „Prepare batch”; `action_prepare_batch_sale_order`: aceeași acțiune, legată de lista comenzilor de vânzare.
- `delivery_batch_print`: raportul „Deliveries”, legat de loturile de transfer.
- Nu există cron-uri.

#### 5. Conexiuni

- `stock_picking_batch`: modulul standard de transfer în lot, extins de acest modul.
- `sale_stock` și `purchase_stock`: sursa transferurilor grupate de asistentul Prepare Batch.
