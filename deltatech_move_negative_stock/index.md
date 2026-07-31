# Realimentare Stoc Negativ (localizat la `deltatech_move_negative_stock/index.md`)

- **Nume Tehnic:** `deltatech_move_negative_stock`
- **Versiune:** `19.0.1.1.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_move_negative_stock`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_move_negative_stock`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul oferă un mod simplu și rapid de a identifica și corecta stocurile negative dintr-o locație, completând automat o operațiune de transfer cu cantitățile necesare pentru a le aduce înapoi la cel puțin zero, preluate dintr-o altă locație sursă. În plus, permite desemnarea unui responsabil (manager) pentru fiecare locație internă, care primește zilnic, prin e-mail, un raport automat cu produsele aflate pe stoc negativ în acea locație.

#### 2. Funcționalități Cheie

- Identificare automată a cantităților negative: butonul dedicat **Get negative products** (Obține produse negative) de pe formularul de transfer identifică toate produsele cu cantitate negativă în locația de destinație a transferului curent.
- Completare automată a transferului: adaugă rapid linii în transferul curent pentru toate produsele identificate cu stoc negativ, cu exact cantitățile necesare pentru a aduce inventarul destinației la cel puțin zero.
- Monitorizarea sănătății stocului: gândit pentru gestionarii de inventar care trebuie să mențină evidențe de stoc curate, fără valori negative, în mai multe locații.
- Notificare zilnică: fiecărei locații interne i se poate atribui un Manager; o acțiune programată zilnică trimite prin e-mail managerului lista produselor cu stoc negativ din acea locație, agregată pe sub-locațiile ei. Locațiile fără manager sunt omise.

#### 3. Dependențe

- `stock`
- `mail`

#### 4. Componente Cheie

**Modele**

- `stock.location` (extins): adaugă câmpul `user_id` (Manager) — utilizatorul notificat de acțiunea programată zilnică atunci când locația respectivă are stoc negativ; metoda `get_negative_products()` agregă pe produs cantitățile negative din locație și sub-locațiile ei, iar `send_mail_negative_stock()` trimite e-mailul șablonului de notificare către manager (dacă există manager și există produse cu stoc negativ).
- `stock.picking` (extins): metoda `get_negative_products()` caută loturile (`stock.quant`) cu cantitate negativă din locația de destinație a transferului (doar în stare `draft`) și creează liniile de mișcare (`stock.move`) necesare pentru a compensa cantitatea negativă, preluând stocul din locația sursă a transferului.

**Vizualizări**

- `view_picking_form` (extinde `stock.view_picking_form`): adaugă butonul **Get negative products** în antetul formularului de transfer, vizibil doar cât timp transferul este în starea `draft`.
- `view_location_form` (extinde `stock.view_location_form`): adaugă câmpul `user_id` (Manager) în formularul locației de stoc, vizibil doar pentru locațiile de tip intern (`usage = internal`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_negative_stock` ("Send negative stock"): rulează zilnic, parcurge toate locațiile interne (`stock.location`) și apelează `send_mail_negative_stock()` pe fiecare, trimițând notificarea prin e-mail managerilor locațiilor care au stoc negativ.

#### 5. Conexiuni

- [deltatech_stock_negative](../deltatech_stock_negative/index.md): abordare complementară — acel modul *previne* apariția stocului negativ la nivel de locație/companie, în timp ce `deltatech_move_negative_stock` oferă instrumentul pentru a *corecta* stocul deja negativ printr-un transfer de realimentare.
