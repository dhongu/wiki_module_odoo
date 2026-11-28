# Panou lateral

- **Nume Tehnic:** `deltatech_web_side_panel`
- **Versiune:** `20.0.1.3.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_web_side_panel
- **Cale Locală:** odoo-addons/deltatech/deltatech_web_side_panel
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care adaugă, în dreapta unei vederi kanban sau listă, un panou cu formularul înregistrării selectate, ca operatorul să citească detaliile fără să părăsească ecranul.

#### 2. Funcționalități Cheie

- Un clic selectează: cardul sau rândul este evidențiat, iar înregistrarea apare în panou; dublu clic deschide formularul complet. Panoul are butoane pentru înregistrarea anterioară/următoare, deschidere formular, reîmprospătare și închidere.
- Formularul este definit de modul în XML (antet, câmpuri, notebook, butoane), în mod doar citire, cu widgeturile obișnuite.
- Kanban și listă se comportă identic (`side_panel_kanban`, `side_panel_list`).
- Panoul se redimensionează prin tragerea mânerului de pe marginea stângă (sau cu săgețile stânga/dreapta; dublu clic restaurează lățimea implicită); lățimea se reține în browser.
- Sub pragul ecranelor extra-large, clicul deschide formularul ca până acum.
- Configurare pentru dezvoltator: `js_class="side_panel_kanban"` pe `<kanban>` sau `js_class="side_panel_list"` pe `<list>`; formularul panoului se indică prin `side_panel_view_ref` în contextul acțiunii; `disable_side_panel: True` oprește panoul.
- Poate rula și pe Odoo Online (plan Custom), prin *Apps > Import Module*, deoarece nu conține cod Python. Exemplu demo: acțiunea *Contacts with side panel (demo)*.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- Niciunul (modul fără cod Python).

**Vizualizări**

- `side_panel_kanban` și `side_panel_list`: clase JS pentru kanban și listă, cu același panou.
- `demo/demo_views.xml`: exemplu pe contacte (`action_demo_partners`).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- Niciuna verificată în cod; se instalează ca dependență a modulelor care folosesc panoul.
