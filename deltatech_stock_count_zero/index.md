# Stock Count Zero (localizat la `deltatech_stock_count_zero/index.md`)

- **Nume Tehnic:** `deltatech_stock_count_zero`
- **Versiune:** `20.0.0.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_count_zero
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_count_zero`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul adaugă o opțiune prin care cantitatea inventariată se setează automat la zero atunci când se cere o numărare de stoc. Este util la inventarierea fizică, unde produsele negăsite trebuie marcate explicit cu zero, reducând introducerea manuală pentru articolele lipsă.

#### 2. Funcționalități Cheie

- Bifa „Set Count to Zero” în asistentul de solicitare a numărării.
- Cantitatea se setează la 0.0 doar pe liniile selectate; la produsele urmărite pe lot/serie, celelalte loturi ale produsului din aceeași locație rămân neschimbate.
- Opțiunea este disponibilă doar administratorilor de inventar (la fel ca „Set to 0” standard).
- Dacă o linie selectată s-a mișcat de la numărare, se deschide fereastra standard de conflict, pentru a decide ce cantitate se păstrează.
- Flux: *Inventar > Operațiuni > Inventar fizic*, se selectează liniile, se apasă „Request Count”, se bifează „Set Count to Zero” și se confirmă; sistemul setează cantitatea inventariată la zero și aplică ajustarea.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.request.count` (asistent, extins): aplică setarea la zero pe liniile selectate.

**Vizualizări**

- `stock_inventory_request_count_form_view`: adaugă bifa „Set Count to Zero” în asistent.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
