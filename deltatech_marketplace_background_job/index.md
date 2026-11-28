# Marketplace Jobs on Background Jobs (localizat la `deltatech_marketplace_background_job/index.md`)

- **Nume Tehnic:** `deltatech_marketplace_background_job`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_marketplace_background_job
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_marketplace_background_job`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Rulează sincronizările marketplace-urilor pe motorul Terrabit *Background Jobs*, fără `queue_job`. Conectorii de marketplace nu depind de un motor de joburi, iar acest modul-punte îi leagă de *Background Jobs*. Joburile pornesc în câteva secunde pe workerii HTTP, inclusiv pe odoo.sh, unde runner-ul `queue_job` nu poate rula.

#### 2. Funcționalități Cheie

- Copiază funcțiile de job declarate de conectori (canal, model de reîncercare) în *Running Processes > Configuration > Job Functions* și creează canalele backend-urilor, fără limită; capacitatea se setează în *Channels* pentru canalele care trebuie plafonate.
- Scrie eșecul unui job de marketplace în jurnalul marketplace-ului și închide intrarea când o reîncercare reușește; se reîncearcă doar erorile temporare (rate limit, timeout).
- Oferă backend-urilor contoarele și listele *Failed jobs* și *Jobs*, plus butonul *Run jobs*.
- Permite managerului de marketplace să citească joburile tuturor utilizatorilor; reîncearcă doar joburile pornite de el (pentru reîncercare/anulare generală se acordă grupul *Background Jobs Manager*).
- Se instalează automat când în *Marketplace > Configuration > Settings*, secțiunea **Job engine**, este ales *Background Jobs*. Trecerea la `queue_job` cere oprirea cron-urilor și golirea cozii, apoi schimbarea opțiunii.

#### 3. Dependențe

- [deltatech_marketplace](../deltatech_marketplace/index.md)
- [deltatech_background_job](../deltatech_background_job/index.md)

#### 4. Componente Cheie

Modulul nu are ecrane proprii; detaliile tehnice sunt acoperite de Readme.

#### 5. Conexiuni

- [deltatech_marketplace_queue_job](../deltatech_marketplace_queue_job/index.md): puntea alternativă, pentru `queue_job`.
- [queue_job](../queue_job/index.md): motorul OCA ales în varianta alternativă.
