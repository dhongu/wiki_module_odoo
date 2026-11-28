# IAP Server - Service Helpdesk (localizat la `terrabit_iap_server_helpdesk/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_helpdesk`
- **Versiune:** `20.0.0.3.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_server_helpdesk
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_helpdesk`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul este partea de server a conectorului de suport Terrabit și rulează doar pe helpdesk-ul Terrabit, niciodată la clienți. Primește tichetele pe care clienții cu [terrabit_helpdesk_connector](../terrabit_helpdesk_connector/index.md) le deschid din propriul Odoo, le leagă de firma clientului după codul fiscal și le atribuie echipei de helpdesk configurate. Pentru consultant, un astfel de tichet se tratează ca oricare altul (preluare, pontaj, răspuns, schimbare de stadiu, închidere), iar clientul primește la sincronizare un status simplificat și mesajele publice. Serverul nu trimite nimic din proprie inițiativă, în afară de o notificare fără date care anunță baza clientului că are noutăți.

#### 2. Funcționalități Cheie

- Serviciul IAP `terrabit_helpdesk`, folosit de conectorul instalat la clienți; fiecare client înregistrat primește un cont (`iap.server.account`) legat automat de compania lui, după CUI.
- Creditele nu se acordă automat la înregistrare; se alocă manual, per client, direct pe cont (consumul automat din orele pontate nu este implementat).
- Fiecare stadiu al helpdesk-ului primește un status vizibil clientului (Nou, În lucru, De răspuns, În așteptare); „Închis" se deduce din bifa **Pliat** a stadiului. La instalare se propune o mapare inițială după numele stadiilor, editabilă din fișa stadiului.
- Clientul vede doar mesajele publice; notele interne ale consultanților nu ajung la el. Cererile de creare tichet și de răspuns sunt idempotente (cheie `request_key`), deci o retrimitere după timeout nu creează dubluri.
- Sincronizare incrementală (parametrul `since`), reconcilierea mesajelor după id-uri, timpul petrecut pe fiecare status al clientului și urgența tradusă 1:1 în prioritatea nativă a tichetului.
- Punerea în așteptare și închiderea tichetului de către client (la echipele cu **Closure by Customers**), plus mementouri (subtipul „Ticket Reminder") care notifică Odoo-ul clientului.
- Chat de suport: fiecare client are un canal Discuss („Support · <client>”) cu membrii echipei de helpdesk; mesajele consultanților ajung în Odoo-ul clientului, cu paginare după `after_id`.
- Tichetele fiecărei firme se grupează sub un partener-companie (`partner_company_id`), inclusiv cele deschise direct la Terrabit.
- Pe 20.0: atașamentele se stochează în `raw`, iar conectorii 18/19 rămân compatibili (cheia din protocol rămâne `datas`, base64).
- Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `iap`
- [terrabit_iap_server](../terrabit_iap_server/index.md)
- `helpdesk`
- `helpdesk_timesheet`

#### 4. Componente Cheie

**Modele**

- `iap.server.account` (extins): contul clientului; rezolvă contactul care deschide tichetul, creează și listează tichete și mesaje, postează răspunsurile și ține canalul de chat (`support_channel_id`).
- `iap.server.service` (extins): codul de serviciu `terrabit_helpdesk` și câmpul **Echipă implicită** pentru tichetele venite prin conector.
- `helpdesk.ticket` (extins): `iap_account_id`, `terrabit_request_key` (cheie de idempotență) și `partner_company_id`.
- `helpdesk.stage` (extins): `connector_state` (statusul vizibil clientului) și propunerea automată a mapării.
- `helpdesk.team` (extins): căutarea primului stadiu deschis cu un anumit status.
- `discuss.channel` și `mail.message` (extinse): canalul de chat al clientului și deduplicarea mesajelor.

**Vizualizări**

- `view_iap_server_service_form`: **Echipă implicită** pe serviciul IAP.
- `helpdesk_ticket_view_form`, `helpdesk_tickets_view_search_company`, `helpdesk_tickets_view_tree_company`: contul IAP, compania partener și gruparea după ea.
- `helpdesk_stage_view_form_connector`: **Status vizibil clientului** pe formularul stadiului.

**Acțiuni Automate / Acțiuni Server**

- Endpointuri JSON-RPC (`auth="none"`, autentificare prin `account_token`): `/iap/terrabit_helpdesk/tickets` (creare), `/tickets/list`, `/tickets/messages`, `/tickets/hold`, `/tickets/close`, `/tickets/message/post`, `/chat/post`, `/chat/messages`.
- `iap_server_service_data`: creează serviciul „Terrabit Helpdesk” (`initial_credits=0`); `mt_ticket_reminder`: subtipul de mesaj „Ticket Reminder”.

#### 5. Conexiuni

- [terrabit_iap_server](../terrabit_iap_server/index.md): furnizează conturile, serviciile și creditele IAP.
- [terrabit_helpdesk_connector](../terrabit_helpdesk_connector/index.md) *(instalat la client, nu la Terrabit)*: consumă endpointurile acestui modul.
- `helpdesk_timesheet`: pontajul pe tichete; dependență de instalare, pentru că o vedere de căutare a helpdesk-ului conține un câmp definit doar acolo.
