# Raport PRN (localizat la `deltatech_report_prn/index.md`)

- **Nume Tehnic:** `deltatech_report_prn`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_report_prn`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_prn`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul adaugă în Odoo un nou tip de raport, în format text brut PRN, destinat tipăririi directe la imprimante de etichete și imprimante matriciale. Spre deosebire de rapoartele PDF, conținutul generat este text neformatat care conține sintaxa nativă a imprimantei (de exemplu limbajul ZPL pentru imprimante de etichete Zebra), astfel încât fișierul descărcat poate fi trimis direct la imprimantă fără conversii intermediare.

#### 2. Funcționalități Cheie

- Permite tipărirea de fișiere cu extensia `.prn`, care conțin sintaxa pentru imprimante de etichete Zebra.
- Adaugă un tip de raport nou (`qweb-prn`) ce poate fi atribuit oricărui raport Odoo pentru a produce ieșire text în loc de PDF.
- Generează un fișier descărcabil cu extensia `.prn`, numit automat conform regulii de denumire a raportului.
- Handler-ul JS de generare a URL-ului raportului (`buildPrnUrl`) este exportat, astfel încât un modul companion (de exemplu, integrarea cu **Zebra Browser Print**) îl poate intercepta cu o secvență de handler mai mică pentru a tipări direct din browser, cu fallback automat pe descărcarea clasică `.prn` implementată aici. Fluxul legacy de descărcare rămâne neschimbat, iar acest modul rămâne liber de orice cod proprietar sau dependență de Browser Print — funcționalitatea completă de tipărire prin Zebra Browser Print (SDK, comutator de activare și logica de tipărire) trăiește într-un modul companion separat.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `ir.actions.report` (extins): adaugă valoarea `qweb-prn` în lista tipurilor de raport și metoda de randare `_render_qweb_prn`, care produce conținut text (`text`) pe baza șablonului QWeb al raportului.

**Controllere**

- `ReportController` (extins din controller-ul `web`): tratează rutele `/report/prn/...` și descărcarea raportului. Pentru tipul `qweb-prn` setează convertorul și extensia pe `prn`, determină numele fișierului din regula `print_report_name` a raportului și returnează răspunsul cu antetul de descărcare.

**Active (assets)**

- `web.assets_backend`: include `static/src/js/action_manager.esm.js`, care înregistrează handler-ul `prn_handler` în registrul `ir.actions.report handlers`. Acesta expune funcția `buildPrnUrl(action)` (folosită și de module companion) și, pentru tipul `qweb-prn`, declanșează descărcarea fișierului `.prn` prin ruta `/report/download`, cu excepția cazului în care raportul este tipărit via IoT (`action.device_id`).

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki. Modulul oferă o capabilitate generică (tip de raport PRN) ce poate fi folosită de orice modul care definește rapoarte de etichete sau de imprimante matriciale, inclusiv de un eventual modul companion de tipărire prin Zebra Browser Print (menționat în HISTORY.md, dar neidentificat încă ca modul separat documentat în wiki).
