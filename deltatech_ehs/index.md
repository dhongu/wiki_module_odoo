# Health and Safety (EHS) (localizat la `deltatech_ehs/index.md`)

- **Nume Tehnic:** `deltatech_ehs`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_ehs
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ehs`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ține evidența securității și sănătății în muncă direct lângă angajați, pentru companiile care o țin azi pe hârtie sau în foi de calcul ori se pregătesc pentru certificarea ISO 45001. Acoperă incidentele și evenimentele la limită, evaluarea riscurilor pe o matrice configurabilă, instruirile cu scadențe și evidența echipamentului de protecție. Formularele legale specifice unei țări (fișe de instruire, registre de accidente) nu sunt incluse.

#### 2. Funcționalități Cheie

- **Incidente și evenimente la limită**: orice angajat raportează un accident de muncă, un eveniment la limită, un eveniment periculos sau o boală profesională, cu locul, persoanele implicate și primul ajutor acordat. Un utilizator simplu vede doar propriile raportări (vătămările sunt date de sănătate). Responsabilul EHS investighează, înregistrează vătămarea, zilele pierdute și cauza rădăcină și deschide o neconformitate când sunt necesare acțiuni corective; un incident cu neconformitate se închide doar după închiderea acesteia, cu acțiunile verificate.
- **Evaluarea riscurilor**: pe loc de muncă sau funcție, fiecare pericol este cotat pe o matrice de risc (probabilitate și gravitate), înainte și după măsurile de control, apoi evaluarea se aprobă. Matricea este configurabilă (scări, niveluri de risc, grilă); una de 5×5 este inclusă.
- **Instruire SSM**: tipuri de instruire cu recurență în luni, sesiuni cu instructor și participanți (la *Mark as done* fiecare participant primește următoarea scadență), evidența instruirilor per angajat, cu cele restante marcate roșu.
- **Echipament de protecție**: registru al echipamentului predat fiecărui angajat, cu data înlocuirii și lista articolelor scadente.
- **Fișa angajatului**: butoane către incidentele, instruirile și echipamentul angajatului.
- **Drepturi**: nivelul *Health and Safety (EHS)* din utilizator: *User* (raportează incidente) sau *EHS manager* (restul; este și auditor intern în `deltatech_qms`). Perioadele de recurență se ajustează în *Configuration > Training types* și *Equipment types*.
- Fluxul detaliat, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `hr`
- `deltatech_qms` (Quality Management ISO 9001; furnizează neconformitățile și acțiunile corective/preventive)

#### 4. Componente Cheie

**Modele**

- `ehs.incident`: incident / eveniment la limită, cu investigație, vătămare, zile pierdute, cauză rădăcină și legătură cu neconformitatea.
- `ehs.risk.assessment` / `ehs.risk.line`: evaluarea riscurilor și pericolele cotate.
- `ehs.risk.matrix`, `ehs.risk.scale`, `ehs.risk.level`, `ehs.risk.cell`: matricea de risc configurabilă.
- `ehs.training.type`, `ehs.training`, `ehs.training.participant`: tipuri, sesiuni și participanți la instruire.
- `ehs.ppe.type`, `ehs.ppe.issue`: tipuri de echipament și predările către angajați.
- `hr.employee`, `qms.nonconformity`: extinse cu butoane/legături către EHS.

**Vizualizări**

- `views/ehs_incident_views.xml`, `ehs_risk_views.xml`, `ehs_training_views.xml`, `ehs_ppe_views.xml`: formularele și listele fiecărei zone.
- `views/hr_employee_views.xml`, `views/qms_nonconformity_views.xml`: butoanele de pe angajat și legătura inversă de pe neconformitate.
- `views/ehs_menus.xml`: aplicația *Health and Safety*.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; datele implicite (secvențe, matricea 5×5, tipurile de incident/instruire/echipament) vin din `data/`.

#### 5. Conexiuni

- `deltatech_qms`: neconformitățile și acțiunile corective ale incidentelor se urmăresc acolo.
