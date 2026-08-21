# Terrabit Connect - Base (localizat la `deltatech_tc/index.md`)

- **Nume Tehnic:** `deltatech_tc`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_tc
- **Cale Locală:** `odoo-addons/deltatech/deltatech_tc`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul este fundația tehnică pentru **Terrabit Connect** — agentul nativ, ușor, care rulează pe un calculator (stație de lucru) și face legătura între Odoo și hardware-ul sau serviciile locale pe care norul nu le poate accesa direct: tokenul ANAF (PKCS#11 / mTLS către SPV), imprimantele fiscale (Datecs), imprimantele de etichete (Zebra ZPL) și validarea declarațiilor (DUKIntegrator). Acest modul de bază nu comunică el însuși cu niciun echipament — oferă doar stratul de conexiune și protocolul de job-uri, plus un singur tip de job generic (apel HTTP către rețeaua locală a clientului) pe care celelalte module de funcționalitate (feature modules) îl folosesc.

#### 2. Funcționalități Cheie

- Registru de stații (`deltatech.tc.station`) — o înregistrare per stație de lucru care rulează Terrabit Connect, fiecare cu o cheie API unică, un timestamp de tip „ultima activitate" (last-seen) și metadate raportate (versiune TC, sistem de operare, funcționalități activate).
- Coadă de job-uri către exterior (`deltatech.tc.job`) — Odoo pune în coadă job-uri `pending`; stația le preia, le execută local și raportează rezultatul (`done` / `error`).
- Endpoint-uri REST autentificate prin antetul `X-Station-Key`: `/tc/heartbeat`, `/tc/poll`, `/tc/result`, `/tc/config/<id>`.
- Tip de job `http_request` — Odoo cere stației să apeleze un echipament accesibil doar în rețeaua locală (o linie de sortare, un cântar, un PLC, un server de etichete) și să raporteze răspunsul înapoi. Se pune în coadă cu `_tc_enqueue_http()`, iar răspunsul se citește cu `response_dict()` / `response_json()`.
- Model de conectare de tip cloud, fără porturi de intrare — stația inițiază mereu conexiunea către Odoo; Odoo nu se conectează niciodată înapoi către stație. Același agent funcționează atât pentru instalări on-premise, cât și în cloud, fără a deschide niciun port pe partea clientului.
- Notificare de tip browser (prin `bus`) către managerii Terrabit Connect atunci când agentul trimite un heartbeat manual.
- Arhitectură extensibilă — modulele de funcționalitate își adaugă propriile tipuri de job (`selection_add` pe `job_type`) și transformă rezultatul stației în înregistrări de business prin suprascrierea hook-ului `_process_result`, păstrând registrul, coada și stratul de transport centralizate într-un singur loc.
- Securitatea apelurilor `http_request` este configurată **în agent, pe stația de lucru**, niciodată din Odoo: lista de host-uri permise (allow-list) nu există în baza de date, iar callback-urile sunt restricționate la metode al căror nume începe cu `_tc_`.

#### 3. Dependențe

- `base`
- `bus` — folosit pentru `bus.bus._sendone()` (notificările către manageri).

#### 4. Componente Cheie

Această secțiune nu este detaliată din analiza codului: documentația se bazează pe `readme/DESCRIPTION.md`, care nu solicită explicit analiza componentelor tehnice. Pentru context tehnic minimal (fără a înlocui secțiunea de mai sus):

- `deltatech.tc.station`: registrul stațiilor Terrabit Connect (cheie API, ultima activitate, versiune TC, sistem de operare, funcționalități raportate).
- `deltatech.tc.job`: coada de job-uri către exterior, cu stările `pending` / `claimed` / `done` / `error`, tipul de job generic `http_request` (`_tc_enqueue_http()`) și hook-ul `_process_result` extensibil.
- Controller REST (`controllers/main.py`): endpoint-urile `/tc/heartbeat`, `/tc/poll`, `/tc/result`, `/tc/config/<id>`, autentificate cu antetul `X-Station-Key`.

#### 5. Conexiuni

- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md): modul de funcționalitate care depinde direct de acest modul de bază — folosește registrul de stații și coada de job-uri Terrabit Connect pentru a transmite mesaje către ANAF prin agentul local.
