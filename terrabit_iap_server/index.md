# IAP Server (localizat la `terrabit_iap_server/index.md`)

- **Nume Tehnic:** `terrabit_iap_server`
- **Versiune:** `19.0.0.5.5`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server`
- **Ultima Ingestie:** `2026-11-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Transformă o instanță Odoo Terrabit într-un server IAP (In-App Purchase): clienții Odoo își înregistrează conturile, primesc credite și le consumă pentru servicii cu plată (de exemplu ANAF, SMS, AI). Serverul ține evidența soldului și a tranzacțiilor, rezervă creditele la autorizare și le consumă la confirmare, astfel încât serviciile să poată fi taxate pe bază de credite, fără riscul de a depăși soldul. Creditele au termen de valabilitate, iar serviciile pot partaja un singur portofel de credite per bază de date a clientului. Este baza pe care se construiesc sub-modulele `terrabit_iap_server_*`.

#### 2. Funcționalități Cheie

Notă: `readme/DESCRIPTION.md` este gol (doar „Features:"), deci pagina este sintetizată din manifest, cod și `readme/HISTORY.md` / `ROADMAP.md`. Modulul nu are `readme/FISA_CONSULTANT.md`. Conținutul reflectă `origin/19.0` (checkout-ul local 19.0 este în urmă).

- Înregistrarea conturilor clienților (`/iap/register`) pe baza token-ului de cont, a serviciului și a UUID-ului bazei clientului; legarea contului de partenerul companiei, cu toleranță la modul de scriere a CUI-ului.
- Flux de consum în doi pași: autorizare (`/iap/1/authorize`) care rezervă creditele, apoi captură (`/iap/1/capture`) sau anulare (`/iap/1/cancel`). Autorizările pending expiră după `ttl` (ore), iar un cron orar le anulează.
- Protecție la suprasolicitare: soldul disponibil exclude rezervările pending neexpirate; sumele nepozitive, nefinite (`NaN`, `inf`) sau peste sold sunt refuzate; autorizarea și captura sunt serializate prin blocare de rând pe cont (sau portofel).
- **Valabilitatea creditelor (19.0.0.3.0):** fiecare alimentare primește o ultimă zi de utilizare („Credits Valid Until"): creditele cumpărate și ajustările pozitive 12 luni, creditele gratuite de la prima înregistrare 60 de zile. Termenele se setează per serviciu (luni / zile; 0 = fără expirare). Consumul se scade întâi din creditele care expiră primele.
- Expirarea creditelor: un cron zilnic înregistrează restul neutilizat al unei alimentări expirate ca linie de tip `Expired`, scăzută din sold; o alimentare expiră o singură dată. La autorizare, alimentările expirate sunt scoase din sold înainte de verificare, deci creditele expirate nu pot fi cheltuite între rulările cronului.
- Contul și portofelul afișează „Next Credits Expiry" și „Credits Expiring"; răspunsurile către clienți (`/iap/register`, `/iap/services-token`, `/iap/1/get-accounts-information`) le trimit ca `next_expiry_date` și `next_expiry_credit`. Migrarea numără valabilitatea alimentărilor vechi de la data actualizării.
- **Portofel de credite per bază de date (19.0.0.3.0):** un serviciu marcat „Shared Credits" nu ține sold pe conturi; conturile aceleiași baze folosesc un singur „Credit Wallet" (meniu nou) cu sold, rezervări, alimentări și expirare comune. Token-urile rămân per serviciu; creditele și istoricul se mută în portofel la legare.
- Portofelul aparține perechii (`db_uuid`, Base URL), deoarece `db_uuid` vine din cereri anonime și nu e secret. Contul se leagă doar pe o cale de încredere (înregistrarea Odoo Online, migrarea), niciodată din `/iap/register`. Un alt host cu același `db_uuid` primește portofel propriu, fără a doua perioadă de probă. Portofelul fără conturi refuză modificarea manuală a creditelor.
- O singură probă per bază de date pentru serviciile cu credite partajate: primul cont înregistrat acordă credite gratuite din parametrul de sistem `terrabit_iap_server.wallet_trial_credits` (implicit 5); serviciile fără credite partajate păstrează „Initial Credits" proprii, acordate o singură dată per pereche db_uuid + serviciu.
- Tipuri de tranzacții („Type"): `Usage`, `Purchase`, `Free Credits`, `Adjustment`, `Expired`. `add_credits`, creditele inițiale și modificarea manuală a câmpului „Credits" înregistrează o linie captată de tipul respectiv; scrierea creditelor unui cont legat de portofel se face pe portofel, ca ajustare.
- Pagini web publice pentru credite (`/iap/1/credit`) și cont (`/iap/<serviciu>/account`), cu hook gol pentru achiziția de credite; ruta `/iap/1/request-link-my-account` oferă butonului „Buy Credits" al clienților Odoo 19 linkul paginii de credite.
- Alertă de sold scăzut: opțiunea „Warn me", prag și e-mail per cont; interogări de sold prin `/iap/1/balance` și `/iap/update-warning-odoo`.
- Portal client (`/my/iap`): cardul „Services & Credits" din `/my`, lista conturilor IAP ale companiei utilizatorului (sold disponibil, credite rezervate, ultima utilizare, insignă de sold scăzut) și istoricul unui cont (`/my/iap/<id>`) cu filtre pe perioadă și tip, totaluri și 50 de linii pe pagină. „Buy Credits" folosește hash-ul token-ului, care nu poate autoriza o cheltuială.
- Securitate: utilizatorii de portal nu au drepturi pe modelele IAP (paginile citesc cu `sudo` doar conturile companiei utilizatorului, altfel 404); tranzacțiile sunt vizibile doar administratorilor; `base_url` acceptat doar http/https către adrese publice (excepție de dezvoltare: `terrabit_iap_server.allow_private_base_url = 1`); „Callback Secret" trimis de client la înregistrare, necesar apoi pentru schimbarea Base URL, cu buton „Reset Callback Secret" pentru suport; erorile rutelor JSON-RPC ajung la client ca erori (`InsufficientCreditError`, `AccessError`).
- Meniuri sub aplicația IAP: „IAP Service", „Registered Accounts", „Transactions", „Credit Wallets".

#### 3. Dependențe

- `iap`
- [terrabit_iap](../terrabit_iap/index.md)
- `website`
- `portal`
- Dependență Python externă: `json2html`

#### 4. Componente Cheie

**Modele**

- `iap.server.service`: serviciul oferit (nume, cod serviciu, unitate de măsură, credite inițiale, „Shared Credits", valabilitatea creditelor cumpărate în luni și a celor gratuite în zile); folosește mixin-uri de website și imagine.
- `iap.server.account`: contul unui client pentru un serviciu (token, token hash-uit, partener, bază URL, db_uuid, credite, sold și sold disponibil, setări de avertizare, secret de callback, legătura către portofel).
- `iap.server.wallet`: portofelul de credite per (`db_uuid`, Base URL); conturi, tranzacții, credite, sold, sold disponibil, indicator de probă acordată, următoarea expirare; metode de blocare și expirare a creditelor.
- `iap.server.transaction`: tranzacția de credit (token, serviciu, cont, portofel, credit, stare pending/captured/cancelled, ttl, dată de expirare); tip (`kind`), credite expirate, descriere; metodele `capture`, `cancel`.

**Vizualizări**

- `view_iap_server_service_form` / `_tree`: administrarea serviciilor.
- `view_iap_server_account_form` / `_tree`: conturile înregistrate.
- `view_iap_server_transaction_form` / `_tree`: istoricul tranzacțiilor.
- `view_iap_server_wallet_form` / `_tree`: portofelele de credite (acțiunea „Credit Wallets").
- `iap_templates.xml`: paginile web publice de credite și cont; asset-uri frontend (`key_modal.esm.js`, `widget_services_recap.esm.js`).
- `iap_portal_templates.xml`: portalul clientului (servicii și credite, istoric cont, card în `/my`); controller `controllers/portal.py`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_cancel_expired_transactions` („IAP Server: cancel expired authorizations"): rulează din oră în oră și anulează autorizările pending expirate.
- `ir_cron_expire_credits` („IAP Server: expire the unused credits past their validity"): rulează zilnic și înregistrează liniile `Expired` pentru creditele nefolosite peste termen.

#### 5. Conexiuni

- [terrabit_iap](../terrabit_iap/index.md): dependență în manifest, partea comună a mecanismului IAP Terrabit.
- [terrabit_iap_server_sale](../terrabit_iap_server_sale/index.md): depinde de acest server în manifest.
- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): depinde de acest server în manifest.
- [terrabit_iap_server_anaf](../terrabit_iap_server_anaf/index.md): depinde de acest server în manifest.
- [terrabit_iap_server_ai](../terrabit_iap_server_ai/index.md): depinde de acest server în manifest.
- [terrabit_iap_server_sms](../terrabit_iap_server_sms/index.md): depinde de acest server în manifest.
- [terrabit_iap_server_line_counter](../terrabit_iap_server_line_counter/index.md): depinde de acest server în manifest.
- [terrabit_iap_server_params](../terrabit_iap_server_params/index.md): depinde de acest server în manifest.
- [terrabit_iap_server_online](../terrabit_iap_server_online/index.md): depinde de acest server în manifest; leagă conturile de portofel pe calea de încredere a înregistrării Odoo Online.
