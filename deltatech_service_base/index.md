# Services Base (localizat la `deltatech_service_base/index.md`)

- **Nume Tehnic:** `deltatech_service_base`
- **Versiune:** `20.0.2.0.6`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/20.0/deltatech_service_base
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_base`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Modulul reprezintă fundația suitei de servicii Deltatech. El nu acoperă singur un flux complet de business, ci pune la dispoziție structura comună pe care se construiesc celelalte module de servicii: aplicația „Service" cu meniurile sale, grupurile de securitate (utilizatori și manageri de service, respectiv roluri de garanție) și câteva date de referință folosite în mod repetat — cicluri de timp și intervale de date. Practic, este stratul de bază care asigură organizarea și drepturile de acces necesare modulelor de service mai avansate.

> Notă: fișierul `readme/DESCRIPTION.md` există, dar este gol (conține doar „Features:"). Prin urmare Sumarul și Funcționalitățile au fost sintetizate din `__manifest__.py` și din codul modulului. Nu există `readme/USAGE.md`, `readme/CONFIGURE.md` sau `readme/FISA_CONSULTANT.md`.

#### 2. Funcționalități Cheie

- Creează aplicația „Service" în meniul principal, cu structura de meniuri aferentă (Master data, Service, Reports, Configuration).
- Definește grupurile de securitate pentru servicii (Client, User, Manager) și pentru garanție (User, Approval, Manager), organizate sub privilegiile „Service" și „Warranty" (`res.groups.privilege`).
- Pune la dispoziție noțiunea de „ciclu" de service (valoare + unitate de măsură: zi, săptămână, lună, an), utilizabilă pentru calcule de intervale recurente (metoda `get_cycle()` returnează un `timedelta`/`relativedelta`).
- Permite gestionarea intervalelor de date (data de început și de sfârșit, cu unicitate pe nume + activ), inclusiv generarea automată, printr-o acțiune server, a celor 12 intervale lunare ale anului curent.

#### 3. Dependențe

- `product`
- `account`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` este gol și nu solicită explicit detalierea componentelor tehnice; secțiunea de mai jos e o sinteză minimală a codului, orientativă.

**Modele**

- `service.cycle`: definește un ciclu recurent (valoare + unitate de măsură — zi/săptămână/lună/an) folosit de modulele de servicii pentru calculul intervalelor.
- `service.date.range`: interval de date (început/sfârșit) cu constrângere de unicitate pe nume și câmp `active`; include acțiunea `generate_date_range()` care creează cele 12 intervale lunare ale anului curent.

**Vizualizări**

- `view_service_date_range_tree` / `view_service_date_range_form_view`: listă editabilă inline și formular pentru intervalele de date.
- `action_service_cycle`: acțiune fereastră (listă/formular) pentru ciclurile de service, expusă în meniul de Configurare.
- `action_service_data_range`: acțiune fereastră pentru intervalele de date, expusă în meniul de Configurare.

**Acțiuni Automate / Acțiuni Server**

- `action_generate_date_range`: acțiune server legată de modelul `service.date.range` care rulează `generate_date_range()`; disponibilă ca acțiune contextuală (`binding_model_id`) din listă.

#### 5. Conexiuni

Modulul este baza pe care se sprijină celelalte module din suita [deltatech_service](../deltatech_service/index.md). Niciunul dintre aceste module conexe nu are încă pagină wiki, deci rămân ca text simplu: [deltatech_service](../deltatech_service/index.md).
