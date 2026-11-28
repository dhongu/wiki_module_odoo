# PRN Report (localizat la `deltatech_report_prn/index.md`)

- **Nume Tehnic:** `deltatech_report_prn`
- **Versiune:** `20.0.1.1.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_report_prn
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_prn`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite tipărirea fișierelor cu extensia `.prn`, adică text brut cu sintaxa nativă a imprimantelor de etichete Zebra. Un raport Odoo poate produce astfel ieșire text în loc de PDF, iar fișierul descărcat se trimite direct la imprimantă, fără conversii intermediare.

#### 2. Funcționalități Cheie

- Tip de raport nou (`qweb-prn`), atribuibil oricărui raport Odoo, care generează text neformatat în loc de PDF.
- Fișier descărcabil cu extensia `.prn`, numit automat după regula de denumire a raportului.
- Funcția JS `buildPrnUrl` este exportată, astfel încât un modul companion (de exemplu integrarea cu **Zebra Browser Print**) o poate intercepta pentru a tipări direct din browser, cu revenire automată la descărcarea `.prn`. Modulul rămâne fără cod proprietar sau dependență de Browser Print; tipărirea prin Browser Print stă într-un modul companion separat.
- Fluxul pas-cu-pas de configurare este în fișa consultantului.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `ir.actions.report` (extins): adaugă tipul `qweb-prn` și metoda `_render_qweb_prn`, care produce conținut text pe baza șablonului QWeb al raportului.

**Controllere**

- `ReportController` (extins din `web`): pentru `qweb-prn` setează extensia `prn`, determină numele fișierului din `print_report_name` și returnează răspunsul cu antet de descărcare.

**Active (assets)**

- `web.assets_backend`: `static/src/js/action_manager.esm.js` înregistrează handlerul `prn_handler`, care pentru `qweb-prn` declanșează descărcarea prin `/report/download`, cu excepția tipăririi prin IoT (`action.device_id`).

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki. Capabilitatea este generică și poate fi folosită de orice modul cu rapoarte de etichete sau pentru imprimante matriciale.
