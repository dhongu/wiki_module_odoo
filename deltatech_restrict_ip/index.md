# Deltatech Restrict IP Login (localizat la `deltatech_restrict_ip/index.md`)

- **Nume Tehnic:** `deltatech_restrict_ip`
- **Versiune:** `20.0.1.3.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_restrict_ip
- **Cale Locală:** `odoo-addons/bitshop/deltatech_restrict_ip`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul adaugă un strat de securitate pentru Odoo, permițând restricționarea autentificării în funcție de adresa IP. Accesul la ERP poate fi controlat și monitorizat pe baza locației utilizatorului, limitat la birouri sau conexiuni VPN autorizate, ceea ce reduce suprafața de atac și sprijină conformitatea cu cerințele de securitate a datelor. În plus, poate bloca IP-uri, subrețele și boți nedoriți la nivelul întregii instanțe.

#### 2. Funcționalități Cheie

- **Restricție de login per utilizator**: în **Settings > Users & Companies > Users**, fila **Access Restricted**. Cât timp **Restrict IPs** e debifat, fiecare IP nou de login se adaugă automat în listă (se pot marca **Banned**). Cu opțiunea bifată, utilizatorul se poate autentifica doar de la IP-urile din listă; cu lista goală, primul login reușește și IP-ul lui este memorat.
- IP-urile se potrivesc exact; intervalele, măștile (`/24`) și wildcard-urile nu sunt suportate la login.
- Un login refuzat primește mesajul standard „Wrong login/password", chiar cu parolă corectă. Verificarea se face doar la autentificare (sesiunile deschise rămân active) și acoperă și integrările XML-RPC/JSON-RPC cu parolă sau cheie API; cheile trimise în antetul `Authorization: Bearer` nu sunt acoperite.
- Recomandare: în spatele unui reverse proxy se pornește serverul cu `proxy_mode = True`, iar IP-urile reale se verifică în **Settings > Users & Companies > User Log**.
- **Blocare la nivel de instanță** prin directive `# restrict-ip:` în robots.txt (**Website > Configuration > Settings > Tracking & SEO > Edit robots.txt**): `blocked_ip`, `blocked_subnet` (CIDR) dau 403; `bad_bot` blochează User-Agent-uri; `allowed_bot` cu `bot_peak_rate_limit` limitează boții permiși; `rate_limit` limitează cererile pe minut per IP pentru vizitatorii neautentificați (429). Blocarea acoperă site-ul, backend-ul și pagina de login.
- Directivele devin active la salvare, dar sunt publice în `/robots.txt`. Imediat ce există o directivă `# restrict-ip:`, listele de boți implicite nu mai sunt folosite.
- Fluxul detaliat, cu capturi, este în fișa consultantului.

#### 3. Dependențe

- `base`
- `website`

#### 4. Componente Cheie

Secțiune omisă conform prioritizării Readme (`readme/DESCRIPTION.md` prezent și nu solicită explicit detalierea componentelor tehnice). Din manifest: vizualizări în `views/res_users_log_view.xml` și `views/res_user_view.xml`, plus drepturile din `security/ir.access.csv`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki.
