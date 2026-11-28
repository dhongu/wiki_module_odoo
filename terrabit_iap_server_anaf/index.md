# IAP Server - Service ANAF (localizat la `terrabit_iap_server_anaf/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_anaf`
- **Versiune:** `20.0.1.7.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_iap_server_anaf
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_anaf`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Partea de server a serviciului de token ANAF SPV: serverul Terrabit IAP obține tokenul OAuth ANAF cu certificatul digital al clientului, îl păstrează valid și îl trimite în baza de date a clientului. Rulează doar pe serverul Terrabit IAP.

#### 2. Funcționalități Cheie

- **Pagină de autorizare** (`/iap_anaf/authorize/<account_token>`): arată cărei firme (cu CUI) și cărui server Odoo îi va fi atașat tokenul; fluxul OAuth pornește doar după confirmare, cu un `state` de unică folosință valabil 15 minute. Paginile sunt în română.
- **Închiderea sesiunii ANAF anterioare** (opțional): opțiunea **Close Previous ANAF Session** deschide întâi logout-ul ANAF într-o filă nouă, util când clienții ajung la „Your session is finished" fără solicitarea certificatului.
- **Configurare serviciu**: în meniul Settings > Technical > IAP (mod dezvoltator), serviciul **ANAF Token** cere Client ID și Client Secret ale aplicației OAuth înregistrate la ANAF (vizibile doar administratorilor) și afișează **Anaf Callback Url** de declarat la ANAF. O autorizare nouă costă 1 credit; reînnoirile sunt gratuite.
- **Reînnoire într-un singur loc**: jobul zilnic **IAP ANAF: Refresh Access Tokens** reînnoiește tokenurile care expiră în 30 de zile, reîncearcă trimiterile eșuate și cere bazei clientului să oprească propria reînnoire `l10n_ro_edi`.
- **Trimitere către client**: prin ruta `/iap/anaf_token_response` din `terrabit_iap_anaf` sau, pentru o bază Odoo Online (`l10n_ro_anaf_token_online`, fără Python), către automatizarea *On webhook* din linkul de autorizare, acceptată doar pe host-ul contului.
- **Urmărirea tokenului**: pe contul înregistrat, fila **ANAF Token** arată datele de expirare și grupul **Refresh Status**; butoanele **Send Token**, **Refresh Token** și **Force Send Token** (cu confirmare).
- **Reînnoire blocată**: când ANAF respinge tokenul de reîmprospătare, contul afișează avertisment, **Refresh Blocked** și eroarea; jobul nu mai reîncearcă.
- **Recuperare**: **Adopt Client Token** preia tokenul curent al bazei clientului, îl face token al serverului și cere clientului să oprească reînnoirea proprie.

Fluxul detaliat, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `iap`
- [terrabit_iap_server](../terrabit_iap_server/index.md)
- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): câmpurile serviciului ANAF Token (Client ID, Client Secret, callback, închiderea sesiunii).
- `iap.server.account` (extins): tokenurile, datele de expirare și starea reînnoirii pe contul clientului.

**Vizualizări**

- `views/iap_server_service_views.xml`: formularul serviciului ANAF Token.
- `views/iap_server_account_views.xml`: fila **ANAF Token** pe cont.
- `views/anaf_authorize_templates.xml`: paginile de confirmare, de închidere a sesiunii și de rezultat.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_anaf_refresh_tokens` (**IAP ANAF: Refresh Access Tokens**): rulează zilnic.

#### 5. Conexiuni

- [terrabit_iap_anaf](../terrabit_iap_anaf/index.md): clientul care primește tokenul pe ruta `/iap/anaf_token_response`.
- [terrabit_iap](../terrabit_iap/index.md): protocolul IAP comun client-server.
