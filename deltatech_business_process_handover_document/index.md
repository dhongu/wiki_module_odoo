# Business process handover document (localizat la `deltatech_business_process_handover_document/index.md`)

- **Nume Tehnic:** `deltatech_business_process_handover_document`
- **Versiune:** `19.0.0.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_business_process_handover_document`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_business_process_handover_document`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul generează documentul de predare-primire (proces verbal de predare) pentru un proces de business, direct dintr-un Proiect de Business. Acesta adună informațiile despre compania furnizoare și cea beneficiară, reprezentanții acestora, testerii implicați și lista dezvoltărilor realizate în cadrul proiectului, producând un document PDF pregătit pentru semnare. Astfel, echipa de implementare poate formaliza rapid și standardizat predarea unui proiect către client, fără a redacta manual documentul.

#### 2. Funcționalități Cheie

- Generează documentul de predare-primire pentru un proces de business direct dintr-un Proiect de Business.
- Capturează companiile furnizoare/beneficiare, reprezentanții acestora, testerii și lista dezvoltărilor proiectului.
- Disponibil în limba engleză și română.
- Produce un PDF (QWeb) folosind formatul de hârtie A4.
- Accesibil din Proiectul de Business prin meniul Print: „Handover Document".

#### 3. Dependențe

- [deltatech_business_process](../deltatech_business_process/index.md)

#### 4. Componente Cheie

Conform fișierului `readme/Description.md`, raportul este expus prin acțiunea de raport `deltatech_business_process_handover_document.action_report_verbal_process`, accesibilă din meniul Print al Proiectului de Business.

Mod de utilizare:

1. Se deschide un Proiect de Business.
2. Se completează informațiile despre Furnizor/Beneficiar și Testeri.
3. Se verifică faptul că dezvoltările sunt asociate proiectului.
4. Se apasă Print > Handover Document pentru a genera PDF-ul.

#### 5. Conexiuni

- [deltatech_business_process](../deltatech_business_process/index.md): modulul de bază care definește proiectele și procesele de business pe care se generează documentul de predare-primire.
