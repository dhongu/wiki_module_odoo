# Services Base (localizat la `deltatech_service_base/index.md`)

- **Nume Tehnic:** `deltatech_service_base`
- **Versiune:** `19.0.2.0.6`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_base
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_base`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul reprezintă fundația suitei de servicii Deltatech. El nu acoperă singur un flux complet de business, ci pune la dispoziție structura comună pe care se construiesc celelalte module de servicii: aplicația „Service" cu meniurile sale, grupurile de securitate (utilizatori și manageri de service, respectiv roluri de garanție) și câteva date de referință folosite în mod repetat — cicluri de timp și intervale de date. Practic, este stratul de bază care asigură organizarea și drepturile de acces necesare modulelor de service mai avansate.

> Notă: fișierul `readme/DESCRIPTION.md` există, dar este gol (conține doar „Features:"). Prin urmare Sumarul și Funcționalitățile au fost sintetizate din `__manifest__.py` și din codul modulului. Nu există `readme/USAGE.md` sau `readme/FISA_CONSULTANT.md`.

#### 2. Funcționalități Cheie

- Creează aplicația „Service" în meniul principal, cu structura de meniuri aferentă (Master data, Service, Reports, Configuration).
- Definește grupurile de securitate pentru servicii (Client, User, Manager) și pentru garanție (User, Approval, Manager), organizate sub privilegiile „Service" și „Warranty".
- Pune la dispoziție noțiunea de „ciclu" de service (valoare + unitate de măsură: zi, săptămână, lună, an), utilizabilă pentru calcule de intervale recurente.
- Permite gestionarea intervalelor de date (data de început și de sfârșit), inclusiv generarea automată a celor 12 intervale lunare ale anului curent.

#### 3. Dependențe

- `product`
- `account`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` este gol și nu solicită explicit detalierea componentelor tehnice. Conform schemei wiki, analiza detaliată a codului pentru această secțiune este omisă.

#### 5. Conexiuni

Modulul este baza pe care se sprijină celelalte module din suita `deltatech_service`. Niciunul dintre aceste module conexe nu are încă pagină wiki, deci rămân ca text simplu: `deltatech_service`.
