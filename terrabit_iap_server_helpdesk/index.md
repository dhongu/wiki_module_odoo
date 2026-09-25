# IAP Server - Service Helpdesk (localizat la `terrabit_iap_server_helpdesk/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_helpdesk`
- **Versiune:** `19.0.0.1.15`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_helpdesk
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_helpdesk`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul e partea de server a conectorului de suport Terrabit și rulează doar pe helpdesk-ul
Terrabit, niciodată la clienți. El primește tichetele pe care clienții cu modulul
`terrabit_helpdesk_connector` le deschid din propriul Odoo, le leagă automat de firma clientului
(după codul fiscal al partenerului) și le atribuie echipei de helpdesk configurate. Pentru
consultant, un tichet venit astfel se tratează exact ca oricare altul: preluare, pontaj, răspuns,
schimbare de stadiu, închidere. Modulul se ocupă doar de rutarea inițială, de traducerea stadiului
intern într-un status simplu pentru client (Nou / În lucru / De răspuns / Închis) și de sincronizarea
mesajelor publice; nu trimite nimic din proprie inițiativă — conectorul clientului cere datele la
fiecare sincronizare. Fiecare client are pe cont și un sold de credite, dar alocarea acestora este
în prezent **manuală**, per client; consumul automat al creditelor din orele pontate pe tichete
este doar planificat, nu funcționează încă.

#### 2. Funcționalități Cheie

- Adaugă serviciul IAP `terrabit_helpdesk`, folosit de conectorul de suport instalat în Odoo-ul
  clienților, cu patru endpointuri JSON-RPC: creare tichet, listare tichete deschise, listare
  mesaje de corespondență și postare de răspuns.
- Fiecare client cu conector are un cont (`iap.server.account`) legat automat de compania lui,
  după codul fiscal al partenerului. Potrivirea e **tolerantă** la prefixul de țară, spații și
  majuscule („RO16507426" = „16507426"), dar se caută doar printre partenerii companie activi; fără
  potrivire se creează un partener nou. Dacă există mai mulți (dubluri vechi), contul ajunge pe cel
  cu cele mai multe conturi. Comportament din `terrabit_iap_server` 19.0.0.1.3; înainte potrivirea
  era exactă și crea dubluri tăcute.
- Fiecare stadiu al helpdesk-ului nostru primește un status vizibil clientului: **Nou**, **În
  lucru** sau **De răspuns**; „Închis" nu se mapează manual, ci se deduce din bifa **Pliat** a
  stadiului, ca să existe o singură sursă de adevăr. Pe un stadiu pliat, formularul ascunde câmpul și
  explică faptul că clientul vede tichetul **Închis**.
- La instalare, modulul propune singur o mapare inițială a stadiilor existente: cele cu „răspuns"
  / „raspuns" / „response" / „await" / „feedback" în nume devin **De răspuns**; primul stadiu
  deschis (cel cu secvența minimă) devine **Nou**; restul rămân **În lucru**. Un stadiu nou creat
  ulterior pornește mereu pe **În lucru** și trebuie mapat manual.
- Tichetele fiecărei firme se grupează sub un singur partener-companie (`partner_company_id`),
  calculat din contactul tichetului — acoperă și tichetele deschise direct la Terrabit (telefon,
  email, portal), nu doar cele venite prin conector.
- Clientul vede doar mesajele publice; notele interne ale consultanților nu ajung niciodată la
  client, filtrarea făcându-se pe subtip și pe `is_internal`, nu doar pe tipul mesajului.
- Cererile de creare tichet sunt idempotente printr-o cheie trimisă de conector
  (`terrabit_request_key`): dacă un timeout face clientul să retrimită aceeași cerere, serverul
  întoarce tichetul deja creat, nu unul nou.
- Sincronizare incrementală: cu parametrul `since`, listele de tichete și mesaje întorc doar ce
  s-a modificat de atunci (tichetele închise sau arhivate inclusiv, cu `active`), iar autorii doar
  pe cei ai mesajelor noi. Lista de tichete întoarce `server_time`, cursorul rulării următoare.
- La o modificare vizibilă clientului sau la un răspuns public, serverul anunță după commit baza
  clientului (`<base_url>/terrabit_helpdesk/notify`), cu o notificare semnată HMAC și fără date, pe un
  fir separat; un client care nu răspunde e ignorat.
- Închidere de către client (`/iap/terrabit_helpdesk/tickets/close`), după bifa **Closure by Customers**
  a echipei: prima etapă pliată + `closed_by_partner` (trece și de regula de pontaj), cu notă internă.
- Mesajele și autorii lor vin dintr-o singură căutare; avatarul unui autor pe care clientul îl are deja
  (`skip_avatars`) nu se mai retrimite.
- Pentru reconcilierea zilnică, `/tickets/messages` întoarce doar id-urile (`ids_only`, până la 20.000)
  sau doar mesajele cerute (`message_ids`).
- Atașamentele venite de la client se salvează local ca bytes; cele trimise către client
  (atașamente pe mesaje) pleacă ca link `access_token`, ca să nu depășească limita de timeout a
  apelurilor JSON-RPC.
- Urgența aleasă de client în conector se traduce 1:1 în prioritatea nativă a tichetului
  (`low`→0, `normal`→1, `urgent`→2, `blocking`→3), ca widgetul cu stele să arate identic de
  ambele părți.
- Creditele nu se acordă automat la înregistrarea contului — se alocă manual, per client, direct
  pe contul IAP; consumul lor automat din orele pontate pe tichete nu este implementat.
- Închiderea unui tichet pe helpdesk-ul Terrabit cere pontaj (regulă venită din alt modul, nu din
  acesta) — fără el tichetul nu ajunge în stadiul închis, iar clientul nu îl vede ca **Închis**.

#### 3. Dependențe

- `iap`
- `terrabit_iap_server`
- `helpdesk`
- `helpdesk_timesheet`

#### 4. Componente Cheie

**Modele**

- `iap.server.account` (extindere): conturile clienților — rezolvarea contactului care deschide
  tichetul, crearea și listarea tichetelor, listarea mesajelor de corespondență și postarea
  răspunsurilor clientului.
- `iap.server.service` (extindere): adaugă codul de serviciu `terrabit_helpdesk` și câmpul
  **Echipă implicită** (`helpdesk_team_id`) pentru tichetele venite prin conector.
- `helpdesk.ticket` (extindere): câmpurile `iap_account_id` (contul care a creat tichetul),
  `terrabit_request_key` (cheia de idempotență, cu index unic parțial) și
  `partner_company_id` (compania-ancoră, calculată din contact).
- `helpdesk.stage` (extindere): câmpul `connector_state` (Nou / În lucru / De răspuns) și logica
  de propunere automată a mapării la instalare.

**Vizualizări**

- `views/iap_server_service_views.xml`: câmpul **Echipă implicită** pe formularul serviciului IAP.
- `views/helpdesk_ticket_views.xml`: expune `iap_account_id` și `partner_company_id` pe tichet
  (vizibile în modul dezvoltator), plus gruparea după Companie Partener.
- `views/helpdesk_stage_views.xml`: câmpul **Status vizibil clientului** pe formularul stadiului.

**Date**

- `data/iap_server_service_data.xml`: creează serviciul IAP „Terrabit Helpdesk"
  (`service_code=terrabit_helpdesk`, `initial_credits=0`).

**Controller**

- `controllers/main.py`: endpointuri JSON-RPC, `auth="none"` — `/iap/terrabit_helpdesk/tickets`
  (creare), `/iap/terrabit_helpdesk/tickets/list`, `/iap/terrabit_helpdesk/tickets/messages`,
  `/iap/terrabit_helpdesk/tickets/message/post`; autentificarea se face prin `account_token`,
  rezolvat direct în cod, nu prin `ir.rule`.

#### 5. Conexiuni

- `terrabit_iap_server`: furnizează conturile înregistrate,
  serviciile și creditele IAP pe care se bazează acest modul.
- `helpdesk`: tichetele, echipele și stadiile extinse de modul.
- `helpdesk_timesheet`: pontajul pe tichete; e și dependență de instalare, pentru că una dintre
  vederile de căutare ale helpdesk-ului extinse aici conține un câmp definit doar acolo.
- [terrabit_helpdesk_connector](../terrabit_helpdesk_connector/index.md) *(instalat la client, nu la Terrabit)*: ecranele din Odoo-ul
  clientului care consumă endpointurile acestui modul.
