# Business Process Handover Document (localizat la `deltatech_business_process_handover_document/index.md`)

- **Nume Tehnic:** `deltatech_business_process_handover_document`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_business_process_handover_document
- **Cale Locală:** `odoo-addons/deltatech/deltatech_business_process_handover_document`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde [deltatech_business_process](../deltatech_business_process/index.md) pentru a genera un document formal de predare-primire (proces-verbal) în format PDF, direct dintr-un Proiect de Business. Documentul adună informațiile despre compania furnizoare și cea beneficiară, reprezentanții și testerii lor și lista dezvoltărilor din proiect, gata de semnat. Echipa de implementare poate astfel formaliza rapid și standardizat predarea unui proiect către client.

#### 2. Funcționalități Cheie

- **Date de predare pe proiect**: grupurile *Provider Information* (companie, reprezentant, testeri) și *Recipient Information* (companie, reprezentant, testeri) pe formularul Proiectului de Business; reprezentanții sunt persoane (nu companii), iar testerii sunt parteneri.
- **Dezvoltări colectate automat**: toate dezvoltările legate de proiect sunt incluse în document prin câmpul calculat *Developments*.
- **Filtrare după etapa de implementare** (nou în 19.0): câmpul *Handover Stage Filter* din grupul *Handover Options* limitează documentul la procesele aflate în etapa aleasă, cu testele și dezvoltările lor; lăsat gol, documentul include toate procesele și toate dezvoltările proiectului.
- **Bifă de predare pe Aria de Business**: *Handover Checked* marchează aria ca verificată și acceptată la predare.
- **Raport PDF**: *Handover Document* (QWeb, A4), din *Print ▸ Handover Document* pe Proiectul de Business; conține lista dezvoltărilor și blocuri de semnătură pentru ambele părți; disponibil în engleză și în română.
- **Flux**: se deschide Proiectul de Business din *Business Processes*, se completează informațiile furnizorului și beneficiarului, se verifică legarea dezvoltărilor, apoi se tipărește documentul.

#### 3. Dependențe

- [deltatech_business_process](../deltatech_business_process/index.md)

#### 4. Componente Cheie

**Modele**

- `business.project` (extindere): `provider_company`, `provider_representative`, `provider_testers`, `recipient_company`, `recipient_representative`, `recipient_testers`; `development_ids` (calculat, stocat); `handover_stage_id` (filtru de etapă), `handover_process_ids` (procesele incluse, după filtru) și `handover_development_ids` (dezvoltările incluse în document).
- `business.area` (extindere): bifa `handover_checked`.

**Vizualizări**

- `view_business_project_form_inherit` (`business_project_view.xml`): grupurile „Provider Information”, „Recipient Information” și „Handover Options” pe formularul proiectului.
- `business_area_view.xml`: bifa „Handover Checked” pe formularul Ariei de Business.

**Rapoarte**

- `action_report_verbal_process` (`verbal_process_report.xml`) și șablonul QWeb din `verbal_process_template.xml`: raportul „Handover Document”, atașat modelului `business.project`.
- `paperforat_a4_bp.xml`: formatul de hârtie A4 folosit de raport.

#### 5. Conexiuni

- [deltatech_business_process](../deltatech_business_process/index.md): modulul de bază care definește proiectele, procesele și dezvoltările pe care se generează documentul.
