# Terrabit Connect - Base (localizat la `deltatech_tc/index.md`)

- **Nume Tehnic:** `deltatech_tc`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_tc
- **Cale Locală:** `odoo-addons/deltatech/deltatech_tc`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul este fundația tehnică pentru **Terrabit Connect** — agentul nativ, ușor, care rulează pe un calculator (stație de lucru) și face legătura între Odoo și hardware-ul sau serviciile locale pe care norul nu le poate accesa direct: tokenul ANAF (PKCS#11 / mTLS către SPV), imprimantele fiscale (Datecs), imprimantele de etichete (Zebra ZPL) și validarea declarațiilor (DUKIntegrator). Agentul este o aplicație desktop Tauri (nucleu Rust, web view-ul sistemului de operare) pentru Windows, macOS și Linux, cu instalatoare și actualizări automate semnate publicate în `terrabit-connect-releases`. Acest modul de bază nu comunică el însuși cu niciun echipament — oferă doar stratul de conexiune și protocolul de job-uri, plus un singur tip de job generic (apel HTTP către rețeaua locală a clientului) pe care celelalte module de funcționalitate le folosesc.

#### 2. Funcționalități Cheie

- Registru de stații (`deltatech.tc.station`) — o înregistrare per stație de lucru, cu cheie API unică, timestamp „ultima activitate" (last seen) și metadate raportate (versiune TC, sistem de operare, funcționalități activate). Se creează din **Setări → Terrabit Connect → Stații**; cheia se generează automat și se poate regenera (**Regenerate key**) dacă a fost compromisă.
- Fișier `station.conf` descărcabil din formularul stației (**Download config**), cu `TERRABIT_ODOO_BASE` și `TERRABIT_STATION_KEY`; se importă în agent din **Setări → Importă config** și se aplică fără repornire. Doar managerii Terrabit Connect pot descărca fișierul.
- Grupuri de securitate: **User** (citire stații și job-uri) și **Manager** (acces complet, inclusiv Retry și descărcarea configurației).
- Coadă de job-uri către exterior (`deltatech.tc.job`) — Odoo pune în coadă job-uri `pending`; stația le revendică (`claimed`), le execută local și raportează rezultatul (`done` / `error`). Butonul **Ping** de pe stație pune în coadă un job de test.
- Endpoint-uri REST autentificate exclusiv prin antetul `X-Station-Key` (fallback-ul vechi `X-Agent-Key` a fost eliminat): `/tc/heartbeat`, `/tc/poll`, `/tc/result`, `/tc/config/<id>`. `/tc/poll` întoarce doar job-urile puse în coadă pentru stația apelantă (limita 1–50), iar `/tc/result` acceptă rezultat doar pentru un job în starea `claimed`.
- **Coadă robustă**: revendicarea job-urilor este atomică (`FOR UPDATE SKIP LOCKED`), deci două polluri simultane cu aceeași cheie nu mai pot executa de două ori același job. Un job revendicat fără rezultat după `deltatech_tc.claim_timeout_minutes` este considerat pierdut: cele „retry-safe" (`ping`, `http_request` cu `GET`/`HEAD`; extensibil prin `_tc_is_retry_safe()`) sunt oferite din nou până la `deltatech_tc.max_attempts`, apoi eșuează; celelalte rămân `claimed` (este posibil să fi rulat deja), iar rezultatul întârziat este încă acceptat. Câmpul `attempt_count` și filtrul **Claimed** ajută la diagnostic.
- Buton **Retry** (doar manageri) — repune în `pending` job-urile în eroare sau blocate, după verificarea manuală pe dispozitiv sau la ANAF.
- Cron zilnic de curățenie: job-urile `done` mai vechi de 30 de zile și cele în `error` mai vechi de 90 sunt șterse; job-urile `pending` neluate pot expira după `deltatech_tc.pending_ttl_hours` (implicit oprit).
- Parametri de sistem opționali: `deltatech_tc.claim_timeout_minutes` (15, `0` oprește recuperarea), `deltatech_tc.max_attempts` (3), `deltatech_tc.done_ttl_days` (30), `deltatech_tc.error_ttl_days` (90), `deltatech_tc.pending_ttl_hours` (0 = niciodată). Timeout-ul trebuie ținut peste durata celui mai lung job, altfel un job retry-safe încă în execuție poate rula de două ori.
- Tip de job `http_request` — Odoo cere stației să apeleze un echipament accesibil doar în rețeaua locală (linie de sortare, cântar, PLC, server de etichete) și să raporteze răspunsul. Se pune în coadă cu `_tc_enqueue_http()`; răspunsul se citește cu `response_dict()` / `response_json()`. Apelul este asincron: rulează la următorul poll, deci butoanele interactive trebuie să afișeze o stare de așteptare.
- Pe stația de lucru: heartbeat automat la pornire și apoi la 300 de secunde (interval fix); **polling-ul de job-uri este oprit implicit** și se activează cu `TERRABIT_POLL_JOBS=1` (interval `TERRABIT_POLL_SEC`, implicit 30, minim 5). Cât e oprit, job-urile rămân `pending`. Serverul limitează scrierea `last_seen` la una pe 60 de secunde.
- Model de conectare cloud, fără porturi de intrare — stația inițiază mereu conexiunea către Odoo; același agent servește instalări on-premise și cloud.
- Notificare de tip browser (prin `bus`) către managerii Terrabit Connect la heartbeat manual.
- Arhitectură extensibilă — modulele de funcționalitate adaugă tipuri de job (`selection_add` pe `job_type`) și transformă rezultatul în înregistrări de business prin hook-ul `_process_result`.
- Securitatea `http_request` se configurează **în agent**, nu din Odoo: lista de host-uri permise (`TERRABIT_HTTP_ALLOW`, intrări `host` sau `host:port`, implicit goală — până la completare orice job `http_request` întoarce eroare). Callback-urile sunt restricționate la metode al căror nume începe cu `_tc_`, verificat la punerea în coadă și la apel.

#### 3. Dependențe

- `base`
- `bus` — folosit pentru `bus.bus._sendone()` (notificările către manageri).

#### 4. Componente Cheie

- `deltatech.tc.station`: registrul stațiilor (cheie API, ultima activitate, versiune TC, sistem de operare, funcționalități raportate; acțiuni Ping, Download config, Regenerate key).
- `deltatech.tc.job`: coada de job-uri, cu stările `pending` / `claimed` / `done` / `error`, `attempt_count`, tipul generic `http_request` (`_tc_enqueue_http()`), hook-urile `_process_result` și `_tc_is_retry_safe()` și acțiunea Retry.
- Controller REST (`controllers/main.py`): `/tc/heartbeat`, `/tc/poll`, `/tc/result`, `/tc/config/<id>`, autentificate cu `X-Station-Key`.
- Cron zilnic de curățenie (`data/ir_cron.xml`) pentru job-urile terminate sau expirate.

#### 5. Conexiuni

- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md): modul de funcționalitate care depinde direct de acest modul — folosește registrul de stații și coada de job-uri pentru a comunica cu ANAF prin agentul local.
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md) și [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): depind indirect (prin `l10n_ro_anaf_agent`) pentru depunerea declarațiilor și validarea lor cu DUKIntegrator prin agent.
- [deltatech_print_queue](../deltatech_print_queue/index.md): coada de tipărire (suita bitshop): depinde de acest modul și adaugă joburile `print_zpl` / `print_pdf`, executate de stație pe imprimantele locale.
