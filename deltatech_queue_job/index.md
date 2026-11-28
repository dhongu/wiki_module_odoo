# Queue Job Enhancements (localizat la `deltatech_queue_job/index.md`)

- **Nume Tehnic:** `deltatech_queue_job`
- **Versiune:** `20.0.1.4.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_queue_job`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_queue_job`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce îmbunătățiri funcționalității de coadă de joburi din Odoo, cu accent pe performanță, fiabilitate și flexibilitate. Joburile pot fi procesate în paralel de mai mulți lucrători fără blocaje, un job eșuat nu afectează restul lotului, iar procesarea poate fi declanșată de un serviciu extern la fiecare minut. Este gândit în special pentru Odoo.sh, unde acțiunea programată standard rulează cel mult la 5 minute și lucrătorii sunt opriți la depășirea timpului.

#### 2. Funcționalități Cheie

- **Concurență și blocare optimizate:** metoda `_acquire_specific_job` folosește `FOR NO KEY UPDATE SKIP LOCKED`, deci mai mulți lucrători (cron intern sau API extern) procesează coada simultan fără să se blocheze.
- **Procesare tranzacțională robustă:** fiecare job rulează într-un savepoint, deci la eșec se anulează doar modificările lui; erorile tipice de concurență (ex. serializare) duc la reprogramarea elegantă a jobului.
- **Runnere flexibile:**
  - runner intern prin cron (`_job_runner`), care respectă o limită configurabilă de lot și de timp;
  - endpoint extern `/api/v1/queue/process` (POST, JSON-RPC, cheie API), pentru servicii precum cron-job.org, cu procesare la fiecare minut;
  - endpoint `/api/v1/queue/stats`, care doar numără joburile pe stări (util pentru verificarea cheii);
  - procesare într-un fir de execuție separat, lansată din interfață, fără blocarea ei.
- **Declanșare automată:** la crearea unui job sau la schimbarea `eta` se creează un `ir.cron.trigger`, deci procesarea pornește imediat ce jobul devine eligibil.
- **Configurare centralizată:** în **Setări** (secțiunea Queue Job) se generează cheia API și se setează **Batch Size** (implicit 20) și **Max Seconds** (implicit 50).
- **Monitorizare:** în lista de joburi, butoanele **Cron Trigger**, **Process** și **Process Background** sunt mereu disponibile; notificări live confirmă declanșarea (verde: programat; galben: există deja o declanșare; roșu: cronul lipsește).
- **Curățare:** anularea duplicatelor eșuate și ștergerea joburilor terminale rămase fără dată.
- Răspunsul API este împachetat de două ori (`result` -> `result`) și are mereu HTTP 200, chiar și la cheie invalidă (eroarea apare în corp ca `"status": "error"`). Detaliile pas-cu-pas sunt în fișa consultant.

#### 3. Dependențe

- [queue_job](../queue_job/index.md)
- [queue_job_cron_jobrunner](../queue_job_cron_jobrunner/index.md)

#### 4. Componente Cheie

*Notă: componentele de mai jos sunt cele menționate în `readme/DESCRIPTION.md`.*

**Modele**

- `queue.job` (extins): `_acquire_specific_job`, `_job_runner`, `_api_job_runner`, `process_jobs`, `start_cron_trigger`, `action_process_api_thread`, `_remove_failed_duplicates`, `_gc_dateless_terminal_jobs`.
- `res.config.settings` (extins): cheia API, dimensiunea lotului și secundele maxime.

**Vizualizări**

- `views/queue_job_views.xml`: butoanele de procesare în lista și formularul jobului.
- `views/res_config_settings_views.xml`: blocul de setări al procesorului extern.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_config_parameter.xml`: valorile implicite pentru dimensiunea lotului și secundele maxime.
- Cronul cozii vine din `queue_job_cron_jobrunner`; declanșările `ir.cron.trigger` se creează automat la fiecare job nou.

#### 5. Conexiuni

- [queue_job](../queue_job/index.md): modulul OCA de bază peste care se aplică îmbunătățirile de concurență, tranzacționalitate și runner.
- [queue_job_cron_jobrunner](../queue_job_cron_jobrunner/index.md): runner-ul bazat pe cron pe care acest modul îl extinde.
