# CRM + FSM Bridge (localizat la `deltatech_crm_fsm/index.md`)

- **Nume Tehnic:** `deltatech_crm_fsm`
- **Versiune:** `20.0.0.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_crm_fsm
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_crm_fsm`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Acest modul leagă oportunitățile din CRM de sarcinile din Project/FSM și permite crearea rapidă a unei sarcini direct dintr-o oportunitate. În multe fluxuri de vânzare este necesară o vizită pe teren înainte de ofertare (recunoaștere la fața locului, colectare de date, măsurători). Pornind de la oportunitate, utilizatorii pot crea o sarcină pentru echipa de teren și pot urmări ulterior toate sarcinile conectate la acea oportunitate.

#### 2. Funcționalități Cheie

- Adaugă un câmp „Oportunitate" pe sarcinile de proiect (`project.task.lead_id`).
- Pe formularul oportunității:
  - Buton inteligent „Tasks" cu numărul de sarcini asociate (calculat cu `search_count`); dacă există o singură sarcină, aceasta se deschide direct în formular.
  - Buton de antet „Create FSM Task" pentru a crea rapid o sarcină precompletată cu oportunitatea, partenerul și un nume contextual.
- Căutare și grupare după Oportunitate în vizualizările de sarcini; oportunitatea apare și ca coloană în liste.
- Securitate: butoanele și accesul la sarcini urmează drepturile din Project (de regulă grupul Project User).

#### 3. Dependențe

- `crm`
- `project`

#### 4. Componente Cheie

Secțiunile 'Sumar' și 'Funcționalități Cheie' au fost preluate din `readme/DESCRIPTION.md`, care acoperă pe scurt și componentele relevante (câmpul `project.task.lead_id`, butoanele de pe formularul oportunității și extinderile vizualizărilor de sarcini). Conform fluxului de ingestie, nu s-a efectuat o analiză suplimentară a codului pentru această secțiune.

#### 5. Conexiuni

- `crm`: oferă modelul `crm.lead` (oportunitatea) care devine sursa pentru crearea sarcinilor de teren.
- `project`: oferă modelul `project.task`, extins aici cu legătura către oportunitate și cu acțiunea de creare a sarcinii FSM.
