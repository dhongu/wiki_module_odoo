# Deltatech Stock Count Zero (localizat la `deltatech_stock_count_zero/index.md`)

- **Nume Tehnic:** `deltatech_stock_count_zero`
- **Versiune:** `19.0.0.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_count_zero
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_count_zero`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul adaugă o opțiune care permite stabilirea automată a cantității inventariate la zero atunci când se solicită o numărare a stocului. Este util în timpul inventarierii fizice, unde produsele care nu sunt găsite trebuie marcate explicit cu cantitate zero, simplificând astfel procesul de ajustare a stocului prin reducerea introducerii manuale a datelor pentru articolele lipsă.

#### 2. Funcționalități Cheie

- Adaugă bifa „Set Count to Zero" (Setează numărarea la zero) în asistentul de solicitare a inventarului.
- Setează automat cantitatea la 0.0 pentru liniile de inventar selectate atunci când bifa este activată.
- Simplifică procesul de ajustare a stocului prin reducerea introducerii manuale a datelor pentru articolele lipsă.
- Flux de utilizare: Inventar > Operațiuni > Inventar fizic, se selectează liniile de inventar și se apasă butonul „Request Count" (Solicită numărare); în asistentul afișat se bifează „Set Count to Zero", iar la confirmare sistemul setează cantitatea inventariată la zero și aplică ajustarea.

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile pentru Componente Cheie au fost acoperite de fișierul `readme/DESCRIPTION.md`, care descrie funcționalitatea principală a modulului (extinderea asistentului de solicitare a numărării de inventar din modulul `stock` și fișierul de vizualizare `views/stock_request_count_views.xml`). Analiza suplimentară a codului a fost omisă în conformitate cu regula de prioritizare a Readme-ului.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
