# Side Panel (Panou lateral)

- **Nume Tehnic:** `deltatech_web_side_panel`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_web_side_panel
- **Cale Locală:** `odoo-addons/deltatech/deltatech_web_side_panel`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul tehnic care adaugă un panou în dreapta listelor și al vizualizărilor kanban, în care se afișează formularul înregistrării selectate, fără ca utilizatorul să părăsească ecranul. Utilizatorul parcurge rapid înregistrările și vede detaliile fiecăreia, iar modulele care folosesc panoul decid prin XML ce se afișează în el.

#### 2. Funcționalități Cheie

- **Selectare dintr-un click:** un click pe un card sau pe un rând afișează înregistrarea în panou și o evidențiază, în loc să deschidă formularul complet. Un dublu click pe card sau pe rând deschide formularul complet (din 19.0.1.2.0); butoanele, linkurile și câmpurile din card sau rând își păstrează comportamentul.
- **Navigare în panou:** butoane pentru înregistrarea anterioară/următoare, deschiderea formularului complet, reîmprospătare și închidere.
- **Formular configurabil:** panoul încorporează un formular în modul doar-citire; modulul care îl folosește definește antetul, câmpurile, notebook-ul și butoanele prin XML, iar widgeturile obișnuite funcționează.
- **Kanban și listă, același comportament:** vizualizările `side_panel_kanban` și `side_panel_list` partajează același panou.
- **Redimensionabil:** mânerul de pe marginea stângă se trage cu mouse-ul sau se folosesc săgețile stânga/dreapta; lățimea este între 300 px și 70% din zona de conținut, dublu click pe mâner readuce lățimea implicită, iar lățimea aleasă se reține în browser. Formularul urmărește lățimea panoului.
- **Ecrane mici:** sub breakpoint-ul extra-large panoul este oprit și click-ul deschide formularul ca de obicei.
- **Activare (pentru dezvoltatori):** `js_class="side_panel_kanban"` pe `<kanban>` sau `js_class="side_panel_list"` pe `<list>`; formularul panoului se indică prin cheia de context `side_panel_view_ref` a acțiunii (fără ea se folosește formularul implicit al modelului); `disable_side_panel: True` în context oprește panoul pentru acțiunea respectivă.
- **Exemplu demo:** acțiunea *Contacts with side panel (demo)* (`deltatech_web_side_panel.action_demo_partners`).

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește modele Python; este implementat doar în partea de client (JavaScript/OWL).

**Vizualizări**

- `side_panel_kanban`: vizualizare kanban cu panou lateral (înregistrată în registrul `views`).
- `side_panel_list`: vizualizare listă cu panou lateral (înregistrată în registrul `views`).
- `SidePanel` (`static/src/side_panel/side_panel.esm.js`): componenta OWL a panoului, cu redimensionare și memorarea lățimii.
- `demo/demo_views.xml`: exemplu de utilizare pe contacte.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Modul de infrastructură, fără legături funcționale cu alte module din wiki; este destinat folosirii de către alte module prin `js_class` și `side_panel_view_ref`.
