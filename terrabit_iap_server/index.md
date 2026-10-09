# IAP Server (localizat la `terrabit_iap_server/index.md`)

- **Nume Tehnic:** `terrabit_iap_server`
- **Versiune:** `19.0.0.1.5`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Transformă o instanță Odoo Terrabit într-un server IAP (In-App Purchase): clienții Odoo își înregistrează conturile, primesc credite și le consumă pentru servicii cu plată (de exemplu ANAF, SMS, AI). Serverul ține evidența soldului și a tranzacțiilor fiecărui cont, rezervă creditele la autorizare și le consumă la confirmare, astfel încât serviciile să poată fi taxate pe bază de credite, fără riscul de a depăși soldul. Este baza pe care se construiesc sub-modulele `terrabit_iap_server_*`.

#### 2. Funcționalități Cheie

Notă: `readme/DESCRIPTION.md` este gol (doar „Features:"), deci pagina este sintetizată din manifest, cod și `readme/HISTORY.md` / `ROADMAP.md`.

- Înregistrarea conturilor clienților (`/iap/register`) pe baza token-ului de cont, a serviciului și a UUID-ului bazei clientului; legarea contului de partenerul companiei, cu toleranță la modul de scriere a CUI-ului (RO16507426, ro 16507426, 16507426).
- Credite inițiale per serviciu, acordate o singură dată pentru fiecare pereche bază client (db_uuid) + serviciu.
- Flux de consum în doi pași: autorizare (`/iap/1/authorize`) care rezervă creditele, apoi captură (`/iap/1/capture`) sau anulare (`/iap/1/cancel`).
- Protecție la suprasolicitare: autorizarea verifică soldul disponibil (credite minus tranzacțiile captate și cele pending neexpirate); sumele nepozitive sau peste sold sunt refuzate; autorizarea și captura sunt serializate per cont (blocare de rând).
- Expirarea autorizărilor după `ttl` (ore); un cron orar anulează autorizările pending expirate.
- Interogări de sold și informații de cont: `/iap/1/balance`, `/iap/1/get-accounts-information`, `/iap/services-token`, `/iap/update-warning-odoo`.
- Pagini web publice pentru credite (`/iap/1/credit`) și cont (`/iap/<serviciu>/account`); pagina de credite are un hook gol pentru extinderea cu achiziția de credite (vezi `terrabit_iap_server_sale`).
- Alertă de sold scăzut: opțiunea „Warn me", prag și e-mail per cont.
- Securitate: `base_url` primit de la client este acceptat doar http/https către adrese publice (fără loopback, rețele private, link-local; excepție pentru dezvoltare prin parametrul `terrabit_iap_server.allow_private_base_url = 1`); apelul `/iap/get_info` nu urmează redirecturi.
- Meniuri sub aplicația IAP: „IAP Service", „Registered Accounts", „Transactions".

#### 3. Dependențe

- `iap`
- `terrabit_iap`
- `website`
- Dependență Python externă: `json2html`

#### 4. Componente Cheie

**Modele**

- `iap.server.service`: serviciul oferit (nume, cod serviciu, unitate de măsură, credite inițiale); folosește mixin-uri de website (SEO, multi-website, căutare) și imagine.
- `iap.server.account`: contul unui client pentru un serviciu (token, token hash-uit, partener, bază URL, db_uuid, credite, sold și sold disponibil, setări de avertizare, date de endpoint în JSON).
- `iap.server.transaction`: tranzacția de credit (token, serviciu, cont, credit, stare pending/captured/cancelled, ttl, dată de expirare); metodele `capture`, `cancel`.

**Vizualizări**

- `view_iap_server_service_form` / `_tree`: administrarea serviciilor.
- `view_iap_server_account_form` / `_tree`: conturile înregistrate.
- `view_iap_server_transaction_form` / `_tree`: istoricul tranzacțiilor.
- `iap_templates.xml`: paginile web publice de credite și cont; asset-uri frontend (`key_modal.esm.js`, `widget_services_recap.esm.js`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_cancel_expired_transactions` („IAP Server: cancel expired authorizations"): rulează din oră în oră și anulează autorizările pending expirate.

#### 5. Conexiuni

- [terrabit_iap_server_sale](../terrabit_iap_server_sale/index.md): achiziția de credite prin eCommerce, peste hook-ul paginii de credite.
- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): sub-modul de serviciu care depinde de acest server.
- `terrabit_iap_server_anaf`, [terrabit_iap_server_ai](../terrabit_iap_server_ai/index.md), `terrabit_iap_server_sms`, `terrabit_iap_server_line_counter`, `terrabit_iap_server_params`: alte servicii construite peste acest server (depind de el în manifest).
- `terrabit_iap`: partea de client/bază comună a mecanismului IAP Terrabit.
