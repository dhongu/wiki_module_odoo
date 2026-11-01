# Stock Count Zero (localizat la `deltatech_stock_count_zero/index.md`)

- **Nume Tehnic:** `deltatech_stock_count_zero`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_count_zero
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_count_zero`
- **Ultima Ingestie:** `2026-11-01`

#### 1. Sumar

Acest modul adaugă o opțiune care permite stabilirea automată a cantității inventariate la zero atunci când se solicită o numărare a stocului. Este util în timpul inventarierii fizice, unde produsele care nu sunt găsite trebuie marcate explicit cu cantitate zero, simplificând astfel procesul de ajustare a stocului prin reducerea introducerii manuale a datelor pentru articolele lipsă.

#### 2. Funcționalități Cheie

- Adaugă bifa „Set Count to Zero” (Setează numărarea la zero) în asistentul de solicitare a inventarului.
- Setează automat cantitatea la 0.0 pentru liniile de inventar selectate atunci când bifa este activată, apoi aplică ajustarea.
- Simplifică procesul de ajustare a stocului prin reducerea introducerii manuale a datelor pentru articolele lipsă.
- Doar liniile selectate sunt aduse la zero: pentru produsele urmărite pe lot/serie, celelalte loturi ale produsului din aceeași locație nu sunt modificate.
- Opțiunea este disponibilă doar administratorilor de inventar (grupul `stock.group_stock_manager`), ca și „Set to 0” standard; ceilalți utilizatori primesc o eroare de acces dacă încearcă să o folosească.
- Dacă o linie selectată s-a mișcat după numărare (cantitate depășită), se deschide fereastra standard de conflict, în care se alege ce cantitate se păstrează.
- Flux de utilizare: Inventar > Operațiuni > Inventar fizic, se selectează liniile de inventar și se apasă „Request Count” (Solicită numărare); în asistentul afișat se bifează „Set Count to Zero”, iar la confirmare sistemul setează cantitatea inventariată la zero și aplică ajustarea.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Readme-ul nu cere explicit detalierea componentelor; mai jos sunt cele verificate în cod.

**Modele**

- `stock.request.count` (asistent tranzitoriu, extins): adaugă câmpul `set_count_zero` („Set Count to Zero”, vizibil doar grupului `stock.group_stock_manager`) și suprascrie `action_request_count`, care pentru liniile selectate scrie cantitatea inventariată 0.0 și apelează `action_apply_inventory`; dacă rezultatul e o fereastră de conflict, o returnează. Fără bifă, se rulează fluxul standard.

**Vizualizări**

- `stock_inventory_request_count_form_view`: extinde formularul standard al asistentului de numărare, afișând `set_count_zero` după `show_expected_quantity`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
