# Replenish Negative Stock (localizat la `deltatech_move_negative_stock/index.md`)

- **Nume Tehnic:** `deltatech_move_negative_stock`
- **Versiune:** `19.0.1.1.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_move_negative_stock
- **Cale Locală:** `odoo-addons/deltatech/deltatech_move_negative_stock`
- **Ultima Ingestie:** `2026-11-09`

#### 1. Sumar

Acest modul oferă un mod simplu și rapid de a identifica și corecta stocurile negative dintr-o locație, completând automat o operațiune de transfer cu cantitățile necesare pentru a le aduce înapoi la cel puțin zero, preluate dintr-o altă locație sursă. În plus, permite desemnarea unui responsabil (manager) pentru fiecare locație internă, care primește zilnic, prin e-mail, un raport automat cu produsele aflate pe stoc negativ în acea locație.

#### 2. Funcționalități Cheie

- **Realimentare dintr-un click:** butonul **Get negative products** de pe un transfer intern în starea Draft adaugă o linie pentru fiecare produs cu stoc negativ în locația de destinație, cu cantitatea care îl aduce înapoi la zero, luată din locația sursă a transferului. Se aplică locației de destinație propriu-zise, nu și sub-locațiilor ei.
- **Transfer editabil:** liniile se pot modifica, șterge sau completa manual înainte de validare, ca la orice transfer; fiecare apăsare a butonului adaugă liniile din nou, deci se apasă o singură dată pe transfer.
- **Flux:** se creează un transfer intern cu locația de realimentat ca **Destination Location** și locația din care se iau marfa ca **Source Location**; opțional, un tip de operațiune intern (*Inventar > Configurare > Tipuri de operațiuni*) cu locațiile implicite deja setate (de ex. stoc depozit → showroom).
- **E-mail zilnic cu stoc negativ:** fiecărei locații interne i se poate atribui un **Manager** (*Inventar > Configurare > Locații*); acesta primește o dată pe zi, cu subiectul „Negative stock for location …”, lista produselor negative (referință, nume, cantitate negativă, unitate de măsură), cu cantitățile însumate pe produs pentru locație și toate sub-locațiile ei. Locațiile fără manager sunt omise.
- **Frecvență:** acțiunea programată **Send negative stock** rulează zilnic; frecvența se schimbă din acțiunile programate (*Setări > Tehnic*, mod dezvoltator).

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
