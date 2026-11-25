# Health and Safety (EHS) (localizat la `deltatech_ehs/index.md`)

- **Nume Tehnic:** `deltatech_ehs`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_ehs
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ehs`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Evidența securității și sănătății în muncă (SSM) în Odoo, lângă angajați, pentru companiile care o țin azi pe hârtie sau în tabele ori care se pregătesc pentru certificarea ISO 45001. Modulul acoperă incidentele și evenimentele la limită, evaluarea riscurilor, instruirile de securitate cu scadențe și registrul echipamentelor de protecție. Formularele legale specifice unei țări (fișe de instruire, registre de accidente) nu sunt incluse.

#### 2. Funcționalități Cheie

- **Incidente și evenimente la limită:** orice angajat raportează un accident de muncă, un eveniment la limită, un eveniment periculos sau o boală profesională (dată, loc, persoane implicate, prim ajutor acordat). Utilizatorul simplu vede doar propriile raportări (date de sănătate); managerul SSM vede tot.
- **Investigare și acțiuni corective:** managerul SSM apasă **Investighează**, înregistrează vătămarea, zilele pierdute și cauza rădăcină, apoi **Deschide neconformitate**. Incidentul se închide doar după închiderea neconformității, cu acțiunile verificate.
- **Evaluarea riscurilor:** pe loc de muncă sau funcție, fiecare pericol e cotat pe o matrice (probabilitate și gravitate), înainte și după măsurile de control, apoi evaluarea se aprobă. Matricea e configurabilă (scale, niveluri de risc, grilă); este inclusă o matrice 5×5, iar grila se poate completa din scoruri sau edita celulă cu celulă.
- **Instruiri de securitate:** tipuri de instruire cu recurență în luni, sesiuni cu instructor și participanți; la **Marchează ca efectuată** fiecare participant primește următoarea scadență. Evidența instruirilor pe angajat marchează cu roșu cele restante.
- **Echipamente de protecție:** registru al echipamentelor predate fiecărui angajat, cu data înlocuirii; cele scadente sunt marcate cu roșu. Perioadele se adaptează în tipurile de echipament.
- **Fișa angajatului:** butoane către incidentele, instruirile și echipamentele angajatului.
- **Drepturi:** nivel „Health and Safety (EHS)” pe utilizator (*Utilizator* pentru raportare, *Manager SSM* pentru restul); managerul SSM este și auditor intern în modulul de calitate, pentru a deschide neconformități, iar închiderea lor rămâne la responsabilul de calitate.

#### 3. Dependențe

- `hr`
- [deltatech_qms](../deltatech_qms/index.md)

#### 4. Componente Cheie

**Modele**

- `ehs.incident`: incident SSM, cu stări (nou, investigație, închis) și legătură către neconformitate.
- `ehs.risk.matrix`, `ehs.risk.scale`, `ehs.risk.level`, `ehs.risk.cell`: matricea de risc configurabilă.
- `ehs.risk.assessment`, `ehs.risk.line`: evaluarea riscurilor și pericolele cotate.
- `ehs.training.type`, `ehs.training`, `ehs.training.participant`: tipuri de instruire, sesiuni și participanți cu scadență.
- `ehs.ppe.type`, `ehs.ppe.issue`: tipuri de echipament de protecție și predările către angajați.
- `hr.employee` (extins): butoane și contoare SSM.
- `qms.nonconformity` (extins): câmpul `incident_id`, legătura inversă către incident.

**Vizualizări**

- `ehs_incident_view_form`, `ehs_incident_view_list`, `ehs_incident_view_search`, `ehs_incident_view_pivot`: incidente.
- `ehs_risk_assessment_view_form`, `ehs_risk_matrix_view_form`: evaluări de risc și matricea.
- `ehs_training_view_form`, `ehs_training_view_calendar`, `ehs_training_participant_view_list`: sesiuni, calendar și evidența instruirilor.
- `ehs_ppe_issue_view_list`, `ehs_ppe_type_view_list`: registrul echipamentelor.
- `hr_employee_view_form_ehs`, `qms_nonconformity_view_form_ehs`: extinderi ale formularelor angajatului și neconformității.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni cron sau server; datele includ secvențe, matricea 5×5 și tipurile implicite.

#### 5. Conexiuni

- [deltatech_qms](../deltatech_qms/index.md): furnizează neconformitățile și acțiunile corective/preventive prin care se închide un incident.
