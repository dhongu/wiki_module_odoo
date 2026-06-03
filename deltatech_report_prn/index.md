# Raport PRN (localizat la `deltatech_report_prn/index.md`)

- **Nume Tehnic:** `deltatech_report_prn`
- **Versiune:** `19.0.1.0.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_report_prn`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_report_prn`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul adaugă în Odoo un nou tip de raport, în format text brut PRN, destinat tipăririi directe la imprimante de etichete și imprimante matriciale. Spre deosebire de rapoartele PDF, conținutul generat este text neformatat care conține sintaxa nativă a imprimantei (de exemplu limbajul ZPL pentru imprimante de etichete Zebra), astfel încât fișierul descărcat poate fi trimis direct la imprimantă fără conversii intermediare.

#### 2. Funcționalități Cheie

- Permite tipărirea de fișiere cu extensia `.prn`, care conțin sintaxa pentru imprimante de etichete Zebra.
- Adaugă un tip de raport nou (`qweb-prn`) ce poate fi atribuit oricărui raport Odoo pentru a produce ieșire text în loc de PDF.
- Generează un fișier descărcabil cu extensia `.prn`, numit automat conform regulii de denumire a raportului.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `ir.actions.report` (extins): adaugă valoarea `qweb-prn` în lista tipurilor de raport și metoda de randare `_render_qweb_prn`, care produce conținut text (`text`) pe baza șablonului QWeb al raportului.

**Controllere**

- `ReportController` (extins din controller-ul `web`): tratează rutele `/report/prn/...` și descărcarea raportului. Pentru tipul `qweb-prn` setează convertorul și extensia pe `prn`, determină numele fișierului din regula `print_report_name` a raportului și returnează răspunsul cu antetul de descărcare.

**Active (assets)**

- `web.assets_backend`: include `static/src/js/action_manager.esm.js`, care declanșează descărcarea raportului PRN din interfața backend.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki. Modulul oferă o capabilitate generică (tip de raport PRN) ce poate fi folosită de orice modul care definește rapoarte de etichete sau de imprimante matriciale.
