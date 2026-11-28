# Queue Job Cron Jobrunner (localizat la `queue_job_cron_jobrunner/index.md`)

- **Nume Tehnic:** `queue_job_cron_jobrunner`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/queue/tree/20.0/queue_job_cron_jobrunner
- **Cale Locală:** `odoo-addons/queue/queue_job_cron_jobrunner`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul oferă un executor simplu pentru joburile `queue.job`, bazat pe cron-urile Odoo (`ir.cron`). Este util în mediile în care runner-ul obișnuit al `queue_job` nu poate rula, de exemplu pe Odoo.sh. Joburile sunt procesate pe thread-urile CronWorker, nu pe HttpWorker, deoarece Odoo.sh adoarme HttpWorker-ii când nu există trafic, iar aceștia trebuie păstrați pentru utilizatori. Modulul nu se folosește împreună cu runner-ul standard al `queue_job`.

#### 2. Funcționalități Cheie

- Procesează joburile din coadă prin cron-ul „Queue Job Runner”, fără un proces dedicat de runner.
- Cron-ul este declanșat la crearea unui job sau la reprogramarea lui, prin trigger-e `ir.cron`.
- Suportă capacitatea canalelor și prioritățile joburilor.
- Gestionează oprirea CronWorker-ului la depășirea timpului CPU și confirmă tranzacția după trecerea jobului în starea „started”.
- `RetryableJobError(seconds=N)` amână jobul cu N secunde. Fără `seconds` se aplică pattern-ul de reîncercare al funcției jobului. Dacă niciunul nu e setat, întârzierea rămâne de 5 secunde.
- Execuție în paralel: se duplică înregistrarea cron `queue_job_cron` de câte ori e nevoie, cu respectarea numărului de CronWorker-i disponibili (`--max-cron-threads`).
- Recomandare: pornirea Odoo cu `--limit-time-real-cron=0`, pentru ca timeout-ul CronWorker-ului să nu oprească brusc procesarea (pe Odoo.sh e setat implicit).
- Pe formularul cron-ului apare câmpul `queue_job_runner`, vizibil doar pentru cron-urile modelului `queue.job`.

#### 3. Dependențe

- [queue_job](../queue_job/index.md)

#### 4. Componente Cheie

**Modele**

- `queue.job` (extins): metode pentru achiziția și procesarea unui job (`_acquire_one_job`, `_process`), runner-ul `_job_runner` și gestionarea trigger-elor cron la `create` și `write`.
- `ir.cron` (extins): adaugă câmpul `queue_job_runner`, care marchează cron-urile ce rulează runner-ul.

**Vizualizări**

- `ir_cron_view_form`: moștenește `base.ir_cron_view_form` și adaugă câmpul `queue_job_runner` după `priority`.

**Acțiuni Automate / Acțiuni Server**

- `queue_job_cron` (`ir.cron`, „Queue Job Runner”): rulează `model._job_runner()` zilnic, ca plasă de siguranță. În practică este pornit de trigger-ele create la apariția joburilor.

#### 5. Conexiuni

- [queue_job](../queue_job/index.md): modulul de bază al cozii de joburi, al cărui runner standard este înlocuit de acesta.
