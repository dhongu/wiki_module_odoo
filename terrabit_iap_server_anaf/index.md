# IAP Server - Service ANAF (localizat la `terrabit_iap_server_anaf/index.md`)

- **Nume Tehnic:** `terrabit_iap_server_anaf`
- **Versiune:** `19.0.1.7.2`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_iap_server_anaf
- **Cale Locală:** `odoo-addons/terrabit/terrabit_iap_server_anaf`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă pe serverul IAP al Terrabit serviciul „ANAF Token”. Serverul obține de la ANAF, în numele clienților, token-urile de acces necesare pentru e-Factura, le reînnoiește automat înainte să expire și le trimite instanței Odoo a clientului. Astfel clientul nu mai trebuie să reautorizeze manual conexiunea cu ANAF (cu certificat digital) la fiecare expirare. Este partea de server a modulului client [terrabit_iap_anaf](../terrabit_iap_anaf/index.md).

*Notă: `readme/DESCRIPTION.md` este gol (conține doar „Features:”), deci pagina este sintetizată din manifest, cod și `HISTORY.md`.*

#### 2. Funcționalități Cheie

- **Serviciul „ANAF Token”** (cod `anaf_token`, 100 de credite inițiale), configurat pe serviciul IAP cu Client ID și Client Secret ale aplicației înregistrate la ANAF; formularul afișează și URL-ul de callback ce trebuie declarat la ANAF.
- **Autorizare OAuth cu ANAF** prin link-ul `/iap_anaf/authorize/<account_token>`:
  - pagină de confirmare înainte de start, cu firma (nume + CUI) și serverul Odoo către care va fi trimis token-ul; fluxul pornește doar prin `POST` cu CSRF;
  - parametru `state` (nonce de 16 caractere hex, valabil 15 minute, consumat la prima utilizare) verificat la callback înainte de schimbul codului;
  - opțiunea „Close Previous ANAF Session” închide întâi sesiunea veche de pe `logincert.anaf.ro`, util când clientul primește eroarea „Your session is finished”.
- **Reînnoire automată zilnică** a token-urilor care expiră în mai puțin de 30 de zile; refresh token-ul ANAF se rotește la fiecare apel, deci noul token este salvat și trimis clientului; un eșec pe un cont nu le oprește pe celelalte (commit per cont).
- **Detectarea token-urilor moarte**: când ANAF răspunde că refresh token-ul a expirat sau e invalid, contul este blocat pentru refresh și este necesară reautorizarea cu certificat; ultima eroare și data ultimei încercări se văd pe cont.
- **Trimiterea token-ului către client** (`/iap/anaf_token_response`), cu reluare automată dacă push-ul a eșuat; butonul „Send Token” refuză token-urile moștenite din 18.0, iar „Force Send Token” (cu confirmare) suprascrie token-ul clientului cu cel al serverului.
- **Preluarea token-ului de la client** („Adopt Client Token”) pentru clienții migrați din 18.0: serverul preia copia vie de pe client, devine autoritativ și oprește cronul local de refresh de pe client, astfel încât un singur capăt să rotească token-ul.
- Buton „Refresh Token” pentru reînnoire manuală pe un cont.
- Acțiune de raportare a token-urilor active (`action_anaf_report_live_tokens`) cu datele de expirare și partenerul.
- Refresh token-ul se consideră valabil 365 de zile (în versiunile anterioare era presupus incorect 3 ani; migrarea 19.0.1.4.0 corectează datele).
- **Securitate la trimitere** (19.0.1.4.8): push-ul token-ului, „Adopt Client Token” și cererea de oprire a cronului de refresh de pe client trimit secretul de callback al clientului, dacă acesta și l-a înregistrat; clienții încă pe 18.0 sunt apelați ca înainte. Serverul se instalează înaintea clienților.
- **Token păstrat chiar dacă livrarea eșuează** (19.0.1.4.7): un cont fără `Base URL` sau orice altă eroare de livrare nu mai anulează perechea nouă de token-uri (deja rotită de ANAF); push-ul rămâne marcat ca netrimis și cronul îl reia.
- **Protecție pentru token-urile moștenite din 18.0** (19.0.1.4.6): eligibilitatea pentru push se bazează pe câmpul „Token Obtained On”, scris doar când serverul a obținut efectiv token-ul (autorizare, refresh sau adopție reușită); „Last Refresh Attempt” înregistrează în continuare toate încercările. Bug-urile ANAFSERVER-001/002 din `bugs.md` sunt astfel rezolvate.
- După ce token-ul obținut de server ajunge la client, serverul cere clientului să oprească cronul `l10n_ro_edi` de refresh (`/iap/anaf_disable_local_refresh`); dacă push-ul eșuează, cronul clientului rămâne activ (19.0.1.4.5, valabil și la reluarea din cron).
- Parametrul OAuth `state` este un nonce alfanumeric scurt de 16 caractere hex (19.0.1.4.4), în același timp unic, legat de sesiune și cont, cu expirare.

#### 3. Dependențe

- `iap`
- [terrabit_iap_server](../terrabit_iap_server/index.md)
- `l10n_ro_edi`

#### 4. Componente Cheie

**Modele**

- `iap.server.service` (extins): adaugă valoarea `anaf_token` în `service_code`, plus Client ID, Client Secret, URL callback calculat și opțiunea de închidere a sesiunii ANAF.
- `iap.server.account` (extins): câmpuri pentru access/refresh token, date de expirare, stare push, data și eroarea ultimei reînnoiri, blocare refresh; câmpul „Token Obtained On” (`anaf_token_obtained_date`); metode de refresh, push, adopție și protecții împotriva suprascrierii token-ului viu al clientului.

**Controllere**

- `/iap_anaf/authorize/<account_token>` (și ruta veche `authorize_old`): pagină de confirmare și pornirea fluxului OAuth.
- `/iap_anaf/callback/<service_id>` (`auth="public"`): validează `state`, schimbă codul pe token-uri și le salvează pe cont.

**Vizualizări**

- `view_iap_server_service_form`: grupul „ANAF” (credențiale, callback, opțiune sesiune) pe serviciul IAP.
- `view_iap_server_account_form`: butoanele Send Token, Refresh Token, Adopt Client Token, Force Send Token și pagina „ANAF Token” cu stadiul reînnoirii.
- `anaf_authorize_confirm`, `anaf_authorize_logout_first`, `anaf_authorize_result`: șabloane QWeb pentru confirmare, închiderea sesiunii anterioare și rezultatul autorizării.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_anaf_refresh_tokens` („IAP ANAF: Refresh Access Tokens”): rulează zilnic; reînnoiește token-urile care expiră curând și reia push-urile nereușite.

#### 5. Conexiuni

- [terrabit_iap_anaf](../terrabit_iap_anaf/index.md): modulul client care deschide link-ul de autorizare și primește token-ul trimis de server.
- [terrabit_iap_server](../terrabit_iap_server/index.md): serverul IAP de bază (conturi și servicii) extins aici.
- `l10n_ro_edi`: e-Factura; pe clienți, cronul său de refresh este oprit după ce serverul preia token-ul.
