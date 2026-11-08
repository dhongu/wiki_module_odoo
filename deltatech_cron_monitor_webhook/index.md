# Cron Monitor Webhook (localizat la `deltatech_cron_monitor_webhook/index.md`)

- **Nume Tehnic:** `deltatech_cron_monitor_webhook`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_cron_monitor_webhook
- **Cale Locală:** `odoo-addons/deltatech/deltatech_cron_monitor_webhook`
- **Ultima Ingestie:** `2026-11-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă o soluție simplă și sigură pentru a declanșa sarcinile programate (cron) din Odoo prin webhook-uri, folosind un token de acces global. Astfel, execuția sarcinilor poate fi controlată din platforme externe de monitorizare și programare (ex. cron-job.org, healthchecks.io, EasyCron), independent de planificatorul intern al Odoo.

#### 2. Funcționalități Cheie

- Activare webhook per sarcină cron: în **Setări → Tehnic → Automatizare → Acțiuni programate**, pe tab-ul **Webhook Configuration**, se bifează **Enable Webhook**, se completează un **Webhook Code** unic (ex. `sync_partners`) și se copiază **Webhook URL**, care conține deja tokenul global.
- Securitate prin token global, fără semnături HMAC: un singur token gestionează accesul pentru toate webhook-urile activate. Se setează în **Setări → Setări generale** (căutare „Cron Monitor"), câmpul **Global Webhook Token**, cu butonul **Generate Token** (UUID).
- Autentificare, la alegere (una singură):
  - parametru în URL `?token=...` (recomandat);
  - antet HTTP `X-Access-Token`;
  - corp JSON cu cheia `token` (doar POST, `Content-Type: application/json`).
- Endpoint-uri dedicate:
  - Declanșare: `/cron/webhook/<webhook_code>` (POST/GET);
  - Stare: `/cron/webhook/<webhook_code>/status` (GET), care cere același token (HTTP 401 fără el), la fel ca declanșarea.
- Tokenul se verifică înaintea codului webhook-ului, deci un cod necunoscut nu se poate deosebi de un token greșit.
- Răspuns JSON: la succes (HTTP 200) `status: success`, `job_name`, `execution_time`, `timestamp`; la eroare `status: error` și `message` (HTTP 401 token invalid, 404 cod invalid sau dezactivat, 500 excepția apărută la rulare). Apelul GET al endpoint-ului de declanșare nu mai eșuează cu HTTP 500 (*read-only transaction*).
- Verificare: **Run now** în cron-job.org sau deschiderea URL-ului în browser.
- Endpoint public de sănătate `/cron/healthcheck` (GET), care răspunde `OK`, fără token.

#### 3. Dependențe

- `base`
- `mail`
- `web`

#### 4. Componente Cheie

**Modele**

- `ir.cron` (extins): adaugă `enable_webhook`, `webhook_code` (unic, constrângere `unique(webhook_code)`) și `webhook_url` (calculat din `web.base.url`, codul și tokenul global). Metodele `_log_execution`, `_send_alert`, `_healthcheck_ping` și `action_reset_statistics` sunt momentan goale (fără efect).
- `res.config.settings` (extins): câmpul `cron_webhook_token` (parametrul de sistem `deltatech_cron_monitor_webhook.global_token`) și acțiunea `action_generate_cron_webhook_token`.

**Controllere**

- `CronWebhookController`: rutele `/cron/webhook/<webhook_code>` (`trigger_cron`, rulează cron-ul prin `method_direct_trigger()` cu contextul `cron_trigger_type="webhook"`), `/cron/webhook/<webhook_code>/status` (`get_status`: `job_name`, `next_run`, `active`) și `/cron/healthcheck`; tokenul se compară cu `hmac.compare_digest`.

**Vizualizări**

- `ir_cron_view_form_inherit_monitoring`: extinde formularul acțiunii programate cu tab-ul de configurare a webhook-ului.
- `res_config_settings_view_form`: adaugă în setări câmpul tokenului global și butonul de generare.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește `ir.cron`, `base.automation` sau `ir.actions.server`; el permite declanșarea externă a cron-urilor existente.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
