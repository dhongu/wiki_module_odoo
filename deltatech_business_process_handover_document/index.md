# Business process handover document (localizat la `deltatech_business_process_handover_document/index.md`)

- **Nume Tehnic:** `deltatech_business_process_handover_document`
- **Versiune:** `19.0.0.0.4`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_business_process_handover_document`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_business_process_handover_document`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul extinde `deltatech_business_process` pentru a genera un document formal de predare-primire (proces-verbal de predare-primire) în format PDF, direct dintr-un Proiect de Business. Acesta adună informațiile despre compania furnizoare și cea beneficiară, reprezentanții acestora, testerii implicați și lista dezvoltărilor realizate în cadrul proiectului, producând un document PDF pregătit pentru semnare. Astfel, echipa de implementare poate formaliza rapid și standardizat predarea unui proiect către client, fără a redacta manual documentul.

#### 2. Funcționalități Cheie

- Adaugă pe formularul Proiectului de Business detaliile companiei furnizoare și beneficiare (nume, reprezentant, testeri).
- Colectează automat toate dezvoltările asociate proiectului.
- Adaugă o bifă „Handover Checked" pe fiecare Arie de Business, pentru urmărirea validării la predare.
- Generează un raport PDF QWeb (format A4), accesibil din meniul Print al Proiectului de Business.
- Raportul este disponibil atât în limba engleză, cât și în română.

#### 3. Dependențe

- [deltatech_business_process](../deltatech_business_process/index.md)

#### 4. Componente Cheie

**Modele**

- `business.project` (extindere): adaugă informațiile despre compania furnizoare/beneficiară, reprezentanți, testeri și câmpul calculat cu dezvoltările proiectului, folosite la generarea raportului.
- `business.area` (extindere): adaugă bifa „Handover Checked" pentru marcarea ariei ca verificată/acceptată la predare.

**Vizualizări**

- `business_project_view.xml`: adaugă pe formularul Proiectului de Business grupurile „Provider Information" și „Recipient Information" (companie, reprezentant, testeri).
- `business_area_view.xml`: adaugă bifa „Handover Checked" pe formularul Ariei de Business.

**Rapoarte**

- `verbal_process_report.xml` / `verbal_process_template.xml`: acțiunea de raport și șablonul QWeb pentru documentul de predare-primire, accesibile din meniul Print al Proiectului de Business.
- `paperforat_a4_bp.xml`: definește formatul de hârtie A4 folosit de raport.

#### 5. Conexiuni

- [deltatech_business_process](../deltatech_business_process/index.md): modulul de bază care definește proiectele și procesele de business pe care se generează documentul de predare-primire.
