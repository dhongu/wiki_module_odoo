# Deltatech Contacts (localizat la `deltatech_contact/index.md`)

- **Nume Tehnic:** `deltatech_contact`
- **Versiune:** `19.0.1.4.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_contact`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_contact`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul extinde fișa de contact din Odoo cu informații personale suplimentare, utile mai ales pentru persoanele fizice: data nașterii, CNP-ul și numărul cărții de identitate. Pe lângă aceste câmpuri, modulul oferă o opțiune de afișare a numelui de contact: printr-un parametru de sistem, numele returnat poate conține doar denumirea contactului, fără numele companiei părinte. Astfel, echipele care lucrează cu date de persoane fizice au la dispoziție câmpurile necesare direct în interfața standard de contacte.

#### 2. Funcționalități Cheie

- Adaugă câmpuri suplimentare în fișa de contact: data nașterii, CNP și numărul cărții de identitate.
- Permite afișarea numelui de contact doar cu denumirea proprie (fără numele părintelui), atunci când parametrul de sistem `contact.get_name_only` este activat — funcția `_get_contact_name` returnează numai numele contactului.

#### 3. Dependențe

- `base`
- `contacts`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de Componente Cheie sunt acoperite de `readme/DESCRIPTION.md` și nu au fost extrase suplimentar din cod. Modulul extinde modelul `res.partner` (vizualizare `views/res_partner_view.xml`) pentru a expune noile câmpuri.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale documentate către alte module cu pagină wiki existentă.
