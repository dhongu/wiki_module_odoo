# Deltatech Cron Monitor Webhook (localizat la `deltatech_cron_monitor_webhook/index.md`)

- **Nume Tehnic:** `deltatech_cron_monitor_webhook`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_cron_monitor_webhook
- **Cale Locală:** `odoo-addons/deltatech/deltatech_cron_monitor_webhook`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul oferă o soluție simplă și sigură pentru a declanșa sarcinile programate (cron) din Odoo prin webhook-uri, folosind un token de acces global. Astfel, execuția sarcinilor poate fi controlată din platforme externe de monitorizare și programare (ex. cron-job.org, healthchecks.io, EasyCron), independent de planificatorul intern al Odoo.

#### 2. Funcționalități Cheie

- Activare webhook per sarcină cron: fiecare acțiune programată poate fi configurată să permită declanșarea externă.
- Cod unic de webhook: se definește un cod unic pentru fiecare cron, folosit pentru a construi URL-ul dedicat de endpoint.
- Securitate prin token global: protecție printr-un token de acces global (Bearer sau parametru), fără semnături HMAC complexe.
- Endpoint-uri dedicate:
  - Declanșare: `/cron/webhook/<webhook_code>` (POST/GET)
  - Stare: `/cron/webhook/<webhook_code>/status` (GET)
- Configurare simplă: un singur token global gestionează accesul pentru toate webhook-urile activate, simplificând integrarea cu servicii externe.

#### 3. Dependențe

- `base`
- `mail`
- `web`

#### 4. Componente Cheie

Documentația pentru acest modul a fost generată pe baza fișierului `readme/DESCRIPTION.md`. Conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune a fost omisă deoarece nu este solicitată explicit în Readme.

#### 5. Conexiuni

Nu au fost identificate conexiuni către alte module cu pagină wiki existentă.
