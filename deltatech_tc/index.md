# Terrabit Connect - Base (localizat la `deltatech_tc/index.md`)

- **Nume Tehnic:** `deltatech_tc`
- **Versiune:** `20.0.1.5.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_tc`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_tc`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul este fundația pentru **Terrabit Connect** — agentul nativ, ușor, care rulează pe o stație de lucru (Windows, macOS, Linux; aplicație Tauri) și face legătura între Odoo și hardware-ul sau serviciile locale pe care cloudul nu le poate atinge direct: tokenul ANAF (PKCS#11 / mTLS către SPV), imprimantele fiscale (Datecs), imprimantele de etichete (Zebra ZPL) și validarea declarațiilor (DUKIntegrator). Oferă stratul de conexiune, protocolul de job-uri și două tipuri de job generice, de transport: apel HTTP în rețeaua clientului și interogări PostgreSQL read-only. Stația inițiază mereu conexiunea către Odoo, deci nu se deschide niciun port la client.

#### 2. Funcționalități Cheie

- **Registru de stații** (`deltatech.tc.station`): o înregistrare per stație, cu cheie API unică, ultima activitate și metadate raportate (versiune TC, sistem de operare, funcționalități, driver fiscal).
- **Coadă de job-uri** (`deltatech.tc.job`): Odoo pune în coadă job-uri `pending`; stația le preia, le execută local și raportează `done` / `error`. Job-urile pierdute după timeout se reiau doar dacă sunt sigure la reluare (`ping`, `http_request` GET/HEAD); restul rămân `Claimed` până la verificare manuală și **Retry** (doar manageri).
- **Endpoint-uri REST** autentificate cu antetul `X-Station-Key`: `/tc/heartbeat`, `/tc/poll`, `/tc/result`, `/tc/config/<id>`.
- **Job `http_request`**: Odoo cere stației să apeleze un dispozitiv din rețeaua locală (linie de sortare, cântar, PLC); se pune în coadă cu `_tc_enqueue_http()`, răspunsul se citește cu `response_dict()` / `response_json()`. Lista gazdelor permise (`TERRABIT_HTTP_ALLOW`) se setează doar pe stație, niciodată din Odoo.
- **Job `pg_query`**: pentru agentul *Terrabit Connect PostgreSQL* (serviciu Windows separat) — pagini dintr-o interogare read-only pe o bază din rețeaua clientului, cu SQL din modul sau interogare numită instalată pe stație; se pune în coadă cu `_tc_enqueue_pg_query()`, rândurile se citesc cu `pg_rows()`, paginile următoare se pun automat în coadă.
- **Callback-uri** doar către metode cu prefixul `_tc_`; modulele de funcționalitate adaugă tipuri de job (`selection_add` pe `job_type`) și extind hook-ul `_process_result`.
- **Administrare**: grupurile Utilizator (citire) și Manager (acces complet) din câmpul *Terrabit Connect* al utilizatorului; meniuri în *Setări > Terrabit Connect* (Stații, Job-uri); buton **Download config** (`station.conf`), **Ping**, **Regenerate key**; parametri de sistem `deltatech_tc.*` pentru timeout, număr de încercări și retenția job-urilor (curățare orară).
- **Stații simulate**: stația raportează driverul `simulated` și dispozitivele simulate; formularul afișează o panglică **Simulation**.
- **Copii ale bazei** (staging, neutralizare): fiecare stație primește cheie nouă, iar job-urile `Pending`/`Claimed` se închid în `Error`.
- Interfața agentului este în română și engleză (**Auto** urmează limba companiei stației). Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `bus`: folosit pentru `bus.bus._sendone()` (notificările către manageri).

#### 4. Componente Cheie

**Modele**

- `deltatech.tc.station`: registrul stațiilor Terrabit Connect.
- `deltatech.tc.job`: coada de job-uri, cu stările `pending` / `claimed` / `done` / `error`, tipurile `http_request` și `pg_query` și hook-ul extensibil `_process_result`.

**Vizualizări**

- `view_deltatech_tc_station_list` / `view_deltatech_tc_station_form`: lista și formularul stațiilor.
- `view_deltatech_tc_job_list` / `view_deltatech_tc_job_form` / `view_deltatech_tc_job_search`: job-urile, cu colorare pe stare.
- `menu_deltatech_tc_root`, `menu_deltatech_tc_station`, `menu_deltatech_tc_job`: meniurile din Setări.
- Controller REST `controllers/main.py`: endpoint-urile `/tc/*`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_deltatech_tc_gc_jobs` (*Terrabit Connect: queue cleanup*): rulează orar `_gc_jobs()` și șterge job-urile vechi după retenția configurată.
- `data/neutralize.sql`: la neutralizare regenerează cheile stațiilor și închide job-urile în așteptare.

#### 5. Conexiuni

- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md): stratul ANAF (mesaje SPV) peste registrul de stații și coada de job-uri.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): conectorul casei de marcat care folosește stația Terrabit Connect.
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md): casa de marcat fiscală, cu stația Terrabit Connect (mod simulare).
