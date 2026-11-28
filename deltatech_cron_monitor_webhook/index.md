# Cron Monitor Webhook (localizat la `deltatech_cron_monitor_webhook/index.md`)

- **Nume Tehnic:** `deltatech_cron_monitor_webhook`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_cron_monitor_webhook
- **Cale Locală:** `odoo-addons/deltatech/deltatech_cron_monitor_webhook`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă o soluție simplă și sigură pentru a declanșa sarcinile programate (cron) din Odoo prin webhook-uri, folosind un token de acces global. Execuția sarcinilor poate fi astfel controlată din platforme externe de monitorizare și programare (ex. cron-job.org, healthchecks.io, EasyCron), independent de planificatorul intern al Odoo.

#### 2. Funcționalități Cheie

- Activare webhook per sarcină cron, din tab-ul „Webhook Configuration" al acțiunii programate (*Settings > Technical > Automation > Scheduled Actions*), cu un „Webhook Code" unic, care formează URL-ul endpoint-ului; „Webhook URL" generat conține deja token-ul.
- Token global, setat în *Settings > General Settings* (secțiunea „Cron Monitor"), cu buton „Generate Token" care creează un UUID; același token protejează toate webhook-urile active, fără semnături HMAC.
- Trei metode de autentificare, la alegere: parametrul `?token=...` în URL (recomandat), antetul `X-Access-Token` sau cheia `token` în corpul JSON (doar POST).
- Endpoint-uri: declanșare `/cron/webhook/<webhook_code>` (POST/GET), stare `/cron/webhook/<webhook_code>/status` (GET) și verificare `/cron/healthcheck` (GET).
- Răspuns JSON: la succes (HTTP 200) `status`, `job_name`, `execution_time`, `timestamp`; la eroare (HTTP 401, 404, 500) `status: error` și `message` (ex. token sau cod invalid).

#### 3. Dependențe

- `base`
- `mail`
- `web`

#### 4. Componente Cheie

**Modele**

- `ir.cron` (extindere): câmpurile pentru webhook (activare, cod, URL calculat).
- `res.config.settings` (extindere): token-ul global și acțiunea de generare.

**Vizualizări**

- `ir_cron_view_form_inherit_monitoring`: tab-ul „Webhook Configuration" pe acțiunea programată.
- `res_config_settings_view_form`: secțiunea de setări pentru token.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron` proprii; modulul declanșează cron-uri existente.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
