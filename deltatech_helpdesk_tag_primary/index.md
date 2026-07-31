# Helpdesk Tag Primary & Team Filter (localizat la `deltatech_helpdesk_tag_primary/index.md`)

- **Nume Tehnic:** `deltatech_helpdesk_tag_primary`
- **Versiune:** `19.0.0.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_helpdesk_tag_primary
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_helpdesk_tag_primary`
- **Ultima Ingestie:** `2026-06-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce o organizare pe două niveluri a etichetelor (tag-urilor) folosite la clasificarea tichetelor din Helpdesk. Pe lângă eticheta standard, fiecare etichetă poate fi marcată ca subordonată unei etichete principale și poate fi asociată unei anumite echipe Helpdesk. Astfel, atunci când se completează un tichet, lista de etichete disponibilă devine mai scurtă și mai relevantă: utilizatorul vede întâi doar etichetele principale potrivite pentru echipa tichetului, iar apoi un câmp suplimentar de etichete secundare, dependente de selecția făcută. Rezultatul este o taxonomie mai curată a tichetelor și o selecție mai rapidă și mai corectă pentru agenții de suport.

#### 2. Funcționalități Cheie

- Adaugă pe eticheta de Helpdesk două câmpuri noi: echipa Helpdesk și eticheta principală.
- În câmpul standard de etichete al tichetului afișează doar etichetele care nu au o etichetă principală setată și care aparțin echipei tichetului sau nu au echipă asociată.
- După completarea etichetelor standard, afișează un câmp pentru etichete secundare, unde pot fi adăugate doar etichetele care au ca etichetă principală una dintre etichetele alese în câmpul standard.

#### 3. Dependențe

- `helpdesk`

#### 4. Componente Cheie

**Modele**

- `helpdesk.tag` (extins): adaugă câmpurile `Primary Tag` (marchează eticheta drept sub-etichetă a unei alte etichete) și `Helpdesk Team` (limitează eticheta la o anumită echipă Helpdesk). Un tag nu se poate referi la el însuși ca etichetă principală.
- `helpdesk.ticket` (extins): adaugă câmpul `Secondary Tags`, disponibil doar după selectarea unor etichete principale, în care pot fi alese doar etichete al căror `Primary Tag` este una dintre etichetele principale deja selectate.

**Vizualizări**

- `views/helpdesk_tag_views.xml`: extinde lista/formularul de etichete Helpdesk pentru a expune coloanele `Primary Tag` și `Helpdesk Team`.
- `views/helpdesk_ticket_views.xml`: extinde formularul și kanban-ul tichetului pentru a aplica filtrarea pe câmpul standard de etichete și pentru a afișa câmpul `Secondary Tags`.

#### 5. Conexiuni

- `helpdesk`: modulul de bază Helpdesk din Odoo, ale cărui modele `helpdesk.tag` și `helpdesk.ticket` sunt extinse de acest modul.
