# Helpdesk Tag Primary & Team Filter (localizat la `deltatech_helpdesk_tag_primary/index.md`)

- **Nume Tehnic:** `deltatech_helpdesk_tag_primary`
- **Versiune:** `20.0.0.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_helpdesk_tag_primary
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_helpdesk_tag_primary`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce o organizare pe două niveluri a etichetelor (tag-urilor) folosite la clasificarea tichetelor din Helpdesk. Pe lângă eticheta standard, fiecare etichetă poate fi marcată ca subordonată unei etichete principale și poate fi rezervată unei anumite echipe Helpdesk. La completarea unui tichet, lista de etichete devine mai scurtă și mai relevantă: agentul vede întâi doar etichetele principale potrivite echipei tichetului, apoi un câmp de etichete secundare, dependent de selecția făcută. Rezultatul este o taxonomie mai curată a tichetelor și o selecție mai rapidă și mai corectă pentru agenții de suport.

#### 2. Funcționalități Cheie

- Adaugă pe eticheta de Helpdesk două câmpuri: echipa Helpdesk și eticheta principală (o etichetă fără etichetă principală este principală; cu una, este sub-etichetă). Meniul **Helpdesk > Configurare > Etichete** este vizibil doar în modul dezvoltator.
- În câmpul standard de etichete al tichetului apar doar etichetele fără etichetă principală, ale echipei tichetului sau fără echipă.
- După completarea etichetelor standard apare câmpul **Etichete secundare**, cu sub-etichetele etichetelor principale alese, ale echipei tichetului sau fără echipă.
- La schimbarea echipei sau a etichetelor principale, etichetele secundare care nu se mai potrivesc sunt eliminate, inclusiv la modificări făcute în afara formularului (coloana Etichete din listă, automatizări, import); o etichetă secundară nepotrivită este refuzată. Etichetele principale rămân la mutarea tichetului pe altă echipă.
- Cardurile din kanban afișează etichetele secundare sub cele principale.

Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `helpdesk`

#### 4. Componente Cheie

**Modele**

- `helpdesk.tag` (extins): câmpurile `Primary Tag` (marchează eticheta drept sub-etichetă) și `Helpdesk Team` (limitează eticheta la o echipă). O etichetă nu poate fi propria etichetă principală.
- `helpdesk.ticket` (extins): câmpul `Secondary Tags`, cu validare (`_check_secondary_tags`) și curățarea automată a etichetelor secundare nepotrivite (`write`, `_onchange_drop_invalid_secondary_tags`).

**Vizualizări**

- `view_helpdesk_tag_tree_inherit_primary` / `view_helpdesk_tag_form_inherit_primary`: expun coloanele `Primary Tag` și `Helpdesk Team` pe etichetă.
- `view_helpdesk_ticket_form_inherit_tag_domain`: filtrarea câmpului de etichete și câmpul `Secondary Tags` pe formularul tichetului.
- `view_helpdesk_ticket_kanban_inherit_tag_domain`: etichetele secundare pe cardul kanban.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- `helpdesk`: modulul Helpdesk din Odoo Enterprise, ale cărui modele `helpdesk.tag` și `helpdesk.ticket` sunt extinse.
