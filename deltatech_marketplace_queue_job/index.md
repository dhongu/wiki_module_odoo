# Marketplace Jobs on queue_job (localizat la `deltatech_marketplace_queue_job/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_queue_job`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_queue_job
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_queue_job`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Rulează sincronizările marketplace-urilor pe `queue_job` (OCA). Conectorii de marketplace nu depind de un motor de joburi, iar acest modul-punte îi leagă de `queue_job`. Pentru odoo.sh, unde runner-ul `queue_job` nu poate rula, se folosește în schimb *Background Jobs* cu `deltatech_marketplace_background_job`.

#### 2. Funcționalități Cheie

- Copiază funcțiile de job declarate de conectori (canal, model de reîncercare) în *Job Queue > Queue > Job Functions* și creează canalele lipsă ale backend-urilor (părinții primii), plus `root.inbound` și `root.outbound`.
- Scrie eșecul unui job în jurnalul marketplace-ului și îl marchează *Resolved* când joburile repuse în coadă reușesc; se reîncearcă doar erorile temporare.
- Oferă backend-urilor contoarele și listele *Failed jobs* și *Jobs*, plus butonul *Run jobs* (pornește cron-ul `queue_job_cron_jobrunner`, dacă e activ).
- Cere un runner: `queue_job` încărcat în `server_wide_modules` cu un worker de joburi, sau `queue_job_cron_jobrunner`; fără runner joburile rămân *Pending*.
- Se instalează automat când în *Marketplace > Configuration > Settings*, secțiunea **Job engine**, este ales `queue_job`. Grupul *Job Queue Manager* se acordă celor care repun în coadă sau anulează joburi eșuate.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [queue_job](../queue_job/index.md)

#### 4. Componente Cheie

Modulul nu are ecrane proprii; detaliile tehnice sunt acoperite de Readme.

#### 5. Conexiuni

- [deltatech_marketplace_background_job](../deltatech_marketplace_background_job/index.md): puntea alternativă, pe *Background Jobs*.
- [deltatech_background_job](../deltatech_background_job/index.md): motorul recomandat pe odoo.sh.
