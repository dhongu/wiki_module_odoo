# Services Base

- **Nume Tehnic:** `deltatech_service_base`
- **Versiune:** `19.0.2.0.10`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_base
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_base`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Modulul oferă modulelor de servicii un meniu comun, grupuri de acces, cicluri și intervale de date. Nu are o funcție de business proprie: este fundația suitei de servicii Deltatech, pe care se construiesc modulele mai avansate (contracte, echipamente etc.). Doar managerii de service pot modifica ciclurile și intervalele de date.

#### 2. Funcționalități Cheie

- **Cicluri:** un *Cycle* are o denumire, o valoare și o unitate de măsură (*Day*, *Week*, *Month* sau *Year*). Metoda `get_cycle()` întoarce intervalul de timp corespunzător, utilizabil pentru calcule de intervale recurente.
- **Intervale de date:** un *Date Range* are o denumire, o dată de început și una de sfârșit. Acțiunea *Generate Date Range* creează intervalele lunare ale anului curent, denumite de forma `2026/01`, sărind peste denumirile care există deja.
- **Meniu și grupuri:** modulul creează aplicația *Service* (cu structura Master data, Service, Reports, Configuration), cu *Cycle* și *Date Ranges* în *Configuration*, grupurile *Client*, *User* și *Manager* pentru service și trei grupuri *Warranty* (*User*, *Approval*, *Manager*).

#### 3. Dependențe

- `product`
- `account`

#### 4. Componente Cheie

**Modele**

- `service.cycle`: ciclu de service — denumire, valoare întreagă și unitate (zi, săptămână, lună, an); `get_cycle()` întoarce un `timedelta` sau `relativedelta`.
- `service.date.range`: interval de date cu denumire, dată de început și de sfârșit (obligatorii) și câmpul `active`; denumirea este unică (constrângere pe `name`, `active`); `generate_date_range()` creează cele 12 intervale lunare ale anului curent.

**Vizualizări**

- `view_service_date_range_tree` / `view_service_date_range_form_view`: listă și formular pentru intervalele de date.
- `action_service_cycle`: acțiunea pentru ciclurile de service (meniu în Configuration); `action_service_data_range`: acțiunea pentru intervalele de date.

**Acțiuni Automate / Acțiuni Server**

- `action_generate_date_range` (`ir.actions.server`, „Generate Date Range”): rulează `generate_date_range()` la cerere. Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele de servicii depind de acest modul.
- [deltatech_service_equipment_base](../deltatech_service_equipment_base/index.md): baza modulelor de echipamente depinde de acest modul.
- [deltatech_service](../deltatech_service/index.md): modulul principal al suitei de servicii.
