# PRN Report (localizat la `deltatech_report_prn/index.md`)

- **Nume Tehnic:** `deltatech_report_prn`
- **Versiune:** `19.0.1.1.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_report_prn
- **Cale Locală:** odoo-addons/deltatech/deltatech_report_prn
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Imprimantele de etichete Zebra citesc comenzi text ZPL, nu PDF. Acest modul tehnic adaugă în Odoo un tip de raport *PRN*, astfel încât un șablon QWeb care produce text simplu poate fi tipărit dintr-o acțiune de raport ca fișier `.prn`, trimis apoi direct la imprimantă fără conversii intermediare. Modulul nu livrează rapoarte sau șabloane de etichete proprii; stația de lucru trebuie să trimită fișierul descărcat la imprimantă.

#### 2. Funcționalități Cheie

- **Tip de raport PRN:** acțiunile de raport de tip *PRN* (`qweb-prn`) randează șablonul ca text simplu, nu ca PDF; tipul se poate atribui oricărui raport Odoo.
- **Descărcare fișier:** acțiunea descarcă un fișier `.prn`, numit după raport sau, pentru o singură înregistrare, după expresia `print_report_name`.
- **Punct de extensie:** modulul exportă `buildPrnUrl`, astfel încât un modul companion poate intercepta acțiunea (cu o secvență de handler mai mică) și poate tipări în alt mod, cu revenire pe descărcarea `.prn`; modulul rămâne liber de cod proprietar și de dependența de Zebra Browser Print.
- **Dezinstalare:** la dezinstalare, rapoartele PRN revin la tipul implicit.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `ir.actions.report` (extins): adaugă valoarea `qweb-prn` în lista tipurilor de raport (la dezinstalare revine la valoarea implicită) și metoda de randare `_render_qweb_prn`, care produce conținut text pe baza șablonului QWeb al raportului.

**Controllere**

- `ReportController` (extins din controller-ul `web`): pentru convertorul `prn` randează ca text; la `report_download`, pentru tipul `qweb-prn` setează extensia `prn`, determină numele fișierului din `print_report_name` (pentru o singură înregistrare) și returnează răspunsul cu antetul de descărcare.

**Active (assets)**

- `web.assets_backend`: include `static/src/js/action_manager.esm.js`, care înregistrează handler-ul `prn_handler` în registrul `ir.actions.report handlers`. Acesta expune funcția `buildPrnUrl(action)` (folosită și de module companion) și, pentru tipul `qweb-prn`, declanșează descărcarea fișierului `.prn` prin ruta `/report/download`, cu excepția cazului în care raportul este tipărit via IoT (`action.device_id`). Pe stația de lucru, extensia `.prn` trebuie asociată unui script care trimite fișierul la imprimantă.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_report_prn_zebra_sdk](../deltatech_report_prn_zebra_sdk/index.md): modul companion „Zebra Label Printing", care depinde de acest modul și folosește `buildPrnUrl` pentru tipărire directă din browser prin Zebra Browser Print.
