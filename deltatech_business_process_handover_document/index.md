# Business Process Handover Document (localizat la `deltatech_business_process_handover_document/index.md`)

- **Nume Tehnic:** `deltatech_business_process_handover_document`
- **Versiune:** `20.0.0.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_business_process_handover_document
- **Cale Locală:** `odoo-addons/deltatech/deltatech_business_process_handover_document`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde [deltatech_business_process](../deltatech_business_process/index.md) pentru a genera un proces-verbal de predare-primire în format PDF, direct dintr-un Proiect de Business. Adună datele furnizorului și ale beneficiarului, reprezentanții și testerii lor și lista dezvoltărilor din proiect, într-un document pregătit pentru semnare. Echipa de implementare poate astfel formaliza rapid și standardizat predarea proiectului către client.

#### 2. Funcționalități Cheie

- Pe formularul Proiectului de Business apar grupurile **Provider Information** (companie, reprezentant, testeri furnizor) și **Recipient Information** (companie, reprezentant, testeri beneficiar).
- Toate dezvoltările legate de proiect sunt colectate automat, printr-un câmp calculat.
- Bifa **Handover Checked** pe fiecare Arie de Business marchează aria ca revizuită și acceptată la predare.
- Raportul PDF QWeb (format A4) se tipărește din **Print > Handover Document** pe proiect; conține lista dezvoltărilor și blocuri de semnătură pentru ambele părți.
- Raportul este disponibil în limbile engleză și română.

Fluxul complet este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_business_process](../deltatech_business_process/index.md)

#### 4. Componente Cheie

**Modele**

- `business.project` (extindere): informațiile despre compania furnizoare/beneficiară, reprezentanți, testeri și câmpul calculat cu dezvoltările proiectului, folosite la generarea raportului.
- `business.area` (extindere): bifa „Handover Checked” pentru marcarea ariei ca verificată/acceptată la predare.

**Vizualizări**

- `business_project_view.xml`: adaugă pe formularul proiectului grupurile „Provider Information” și „Recipient Information”.
- `business_area_view.xml`: adaugă bifa „Handover Checked” pe formularul ariei.

**Rapoarte**

- `verbal_process_report.xml` / `verbal_process_template.xml`: acțiunea de raport și șablonul QWeb pentru documentul de predare-primire.
- `paperforat_a4_bp.xml`: formatul de hârtie A4 folosit de raport.

#### 5. Conexiuni

- [deltatech_business_process](../deltatech_business_process/index.md): modulul de bază care definește proiectele și procesele pe care se generează documentul de predare-primire.
