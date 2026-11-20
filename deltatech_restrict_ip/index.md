# IP Login Restriction (localizat la `deltatech_restrict_ip/index.md`)

- **Nume Tehnic:** `deltatech_restrict_ip`
- **Versiune:** `19.0.1.3.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_restrict_ip
- **Cale Locală:** `odoo-addons/bitshop/deltatech_restrict_ip`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul adaugă un strat de securitate pentru Odoo, permițând restricționarea autentificării în funcție de adresa IP, precum și blocarea adreselor IP, a subrețelelor și a roboților nedoriți la nivelul întregii instanțe. Astfel, accesul la sistemul ERP poate fi controlat și monitorizat pe baza locației utilizatorului. Din perspectivă de business, funcționalitatea protejează datele sensibile ale companiei și limitează accesul la locațiile autorizate (birouri, conexiuni VPN securizate), reducând suprafața de atac și sprijinind conformitatea cu cerințele de securitate a datelor.

#### 2. Funcționalități Cheie

- **Securitate sporită:** previne accesul neautorizat în Odoo restricționând autentificarea la o listă de adrese IP de încredere. Fiecare adresă se potrivește exact; intervalele, măștile (`/24`) și wildcard-urile nu sunt suportate la autentificare.
- **Restricție per utilizator:** pe fișa utilizatorului, în fila **Access Restricted** (*Settings > Users & Companies > Users*):
    - cât timp **Restrict IPs** e debifat, fiecare autentificare reușită dintr-un IP nou adaugă automat un rând în listă; utilizatorul se poate autentifica de oriunde, cu excepția IP-urilor marcate **Banned**;
    - cu **Restrict IPs** bifat, autentificarea e permisă doar din IP-urile din listă; la o listă goală, prima autentificare reușește de oriunde și IP-ul ei devine singurul permis.
- **Refuz discret:** o autentificare dintr-un IP nepermis sau banat primește mesajul standard „Wrong login/password”, chiar dacă parola e corectă. Verificarea se face doar la autentificare (sesiunile deja deschise rămân active) și acoperă și integrările XML-RPC / JSON-RPC cu parolă sau cheie API; cheile API trimise în antetul `Authorization: Bearer` nu sunt acoperite, deci IP-ul serverului de integrare trebuie adăugat în listă.
- **Evidență a locațiilor:** *Settings > Users & Companies > User Log* afișează IP-ul fiecărei autentificări; lista completă de IP-uri rămâne pe fila **Access Restricted** a utilizatorului (curățarea zilnică standard păstrează în jurnal doar ultima autentificare).
- **Muncă la distanță securizată:** accesul remote sigur prin autorizarea unor IP-uri VPN specifice.
- **Blocare IP, subrețele și roboți la nivel de instanță:** se configurează prin directive `# restrict-ip:` în robots.txt (*Website > Configuration > Settings*, secțiunea **Tracking & SEO**, **Edit robots.txt**, cu modul dezvoltator activ); se aplică imediat după salvare, pe întreaga instanță (website, backend și pagina de login), nu doar pe website-ul public:
    - `blocked_ip` și `blocked_subnet` (CIDR): primesc **403 Forbidden**;
    - `bad_bot`: User-Agent-urile care conțin unul dintre cuvinte primesc **403 Forbidden**;
    - `allowed_bot` și `bot_peak_rate_limit`: roboții permiți sunt limitați (implicit 5 cereri/minut) între 04:00 și 17:00 UTC;
    - `rate_limit` (implicit 200): cereri pe minut per IP pentru vizitatorii neautentificați; peste limită primesc **429 Too many requests**; limitele se numără separat în fiecare worker Odoo.
- **Atenție la configurare:** de la prima linie `# restrict-ip:` din robots.txt, listele de roboți implicite nu se mai folosesc, deci `allowed_bot` și `bad_bot` trebuie scrise explicit. Directivele sunt publicate în `/robots.txt`, citibil de oricine, deci IP-urile și roboții blocați sunt publici; nu se trec niciodată IP-ul biroului, al VPN-ului sau al proxy-ului.
- **Prerechizit:** în spatele unui reverse proxy (nginx, Odoo.sh, CDN), serverul trebuie pornit cu `proxy_mode = True`, altfel toți utilizatorii par să vină de la același IP; se verifică în **User Log**, coloana **IP Address**.
- **Versiunea 19.0:** verificarea pe fiecare cerere este optimizată, deci restricționarea nu mai costă timp de răspuns pe instanțele aglomerate.

#### 3. Dependențe

- `base`
- `website`

#### 4. Componente Cheie

**Modele**

- `res.users.ip`: adresa IP asociată unui utilizator, cu marcajul **Banned**.
- `res.users` (extins): bifa **Restrict IPs**, lista de IP-uri și verificarea IP-ului la autentificare (`_check_credentials`).
- `res.users.log` (extins): jurnalul de autentificări afișează adresa IP.
- `ir.http` (extins): `_dispatch` aplică blocarea IP/subrețea, filtrarea roboților și limitarea cererilor, pe baza directivelor din robots.txt (configurație păstrată în cache per website).

**Vizualizări**

- `view_users_form`: fila **Access Restricted** pe formularul utilizatorului.
- `view_res_users_log_tree` / `view_res_users_log_form` și acțiunea `action_res_users_log`: jurnalul de autentificări cu coloana **IP Address**.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- `website`: directivele de blocare se citesc din câmpul `robots_txt` al website-ului (dependență directă).
- `res.users.log`: jurnalul standard de autentificări, extins cu adresa IP.
