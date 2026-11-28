# Mail Client

- **Nume Tehnic:** `deltatech_mail_client`
- **Versiune:** `20.0.1.31.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_mail_client
- **Cale Locală:** `odoo-addons/bitshop/deltatech_mail_client`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Mail Client este un client de e-mail generic pentru Odoo, conectat la orice server IMAP (sau, pentru Gmail și Microsoft 365, prin autentificare OAuth2). Fiecare utilizator își salvează căsuța poștală și o citește, o organizează și trimite mesaje din aplicația proprie **Mail Client**, fără să părăsească Odoo. Mesajele rămân pe serverul de e-mail și sunt citite direct de acolo; în Odoo se copiază doar mesajele atașate explicit unei înregistrări (contact, comandă, factură etc.), ca notă internă în discuția acesteia. Modulul este în stadiul Alpha și acoperă etapele 1–6a din roadmap (citire, mutare, trimitere, atașare, securitate, audit și căsuțe partajate).

#### 2. Funcționalități Cheie

- **Cont de e-mail personal**: configurat în **Mail Client → Configuration → Mail Accounts** (server IMAP, utilizator, parolă stocată criptat; opțional SMTP pentru trimitere, cu **Test Connection**).
- **Gmail și Microsoft 365 prin OAuth2**: câmpul **Sign in with** înlocuiește parola; administratorul configurează o singură dată aplicația Google/Microsoft în **Settings → General Settings → Emails**.
- **Citire și organizare**: foldere, listă de mesaje (30 pe pagină), panou de citire, marcare citit/necitit, stea, mutare între foldere (inclusiv prin tragere sau click dreapta), selecție multiplă, Arhivează / Spam / Șterge cu un click; proprietarul creează, redenumește și șterge foldere și golește coșul.
- **Scriere, răspuns, redirecționare**: editor HTML, semnătură per căsuță, atașamente (max. 25 MB), ciorne salvate automat pe server, sugestii de destinatari din contacte, copie în Sent.
- **Căutare pe server**: cu operatori (`from:`, `to:`, `subject:`, `is:unread`, `has:attachment`, `after:`, `before:`), în folderul curent sau în toate folderele.
- **Atașare la înregistrare**: mesajul devine notă internă în discuția unui contact, a unei comenzi de vânzare/achiziție, a unei facturi, a unui transfer, a unui lead sau a unei sarcini, împreună cu atașamentele și fișierul `.eml`; același mesaj nu se atașează de două ori aceleiași înregistrări.
- **Securitate**: rezultatele SPF, DKIM și DMARC scrise de serverul de e-mail, avertismente pentru expeditor falsificat, HTML curățat și afișat într-un cadru izolat (fără scripturi, fără imagini la distanță, cu **Show images** la cerere).
- **Jurnal de acces**: **Mail Access Log** (doar citire) arată cine a deschis, trimis sau atașat ce mesaj.
- **Căsuțe partajate**: proprietarul adaugă membri cu acces **Read** sau **Full**; un selector comută între căsuța personală și cele partajate.
- **Notificări de e-mail nou**: contoare de necitite, plic în bara de sus și o acțiune programată la 5 minute, activabilă de fiecare utilizator.
- **Aspect**: culorile ecranului urmează compania sau o temă aleasă în **Settings → Mail Client Colors**.
- Sesiunea IMAP rămâne deschisă 2 minute (parametrul de sistem `deltatech_mail_client.imap_session_seconds`).

Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mail`
- `bus`
- `html_editor`
- `google_gmail`
- `microsoft_outlook`
- Pachet Python: `cryptography`

#### 4. Componente Cheie

**Modele**

- `mail.client.account`: căsuța poștală (IMAP/SMTP, OAuth2 prin mixin-urile Gmail și Outlook, partajare, stare verificare).
- `mail.client.member`: membrii unei căsuțe partajate și nivelul lor de acces.
- `mail.client.link`: legăturile private dintre mesaje și înregistrările Odoo.
- `mail.client.audit`: jurnalul de acces, doar citire.
- `mail.client.watch`: abonarea utilizatorilor la notificări de e-mail nou.
- `res.company`, `res.config.settings`: tema de culori a aplicației.

**Vizualizări**

- `mail_client_action`: acțiunea client (aplicația Mailbox).
- `mail_client_account_view_form` / `_list` / `_search`: configurarea conturilor.
- `mail_client_audit_view_list` / `_search`: jurnalul de acces.
- `res_config_settings_view_form`: culorile aplicației.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_mail_client_check`: verifică la 5 minute căsuțele urmărite și notifică utilizatorii de mesaje noi.

#### 5. Conexiuni

- `mail`: mesajele atașate apar ca note interne în discuția înregistrărilor.
- `sale`, `purchase`, `account`, `stock`, `crm`, `project`: tipuri de înregistrări la care se pot atașa mesaje, când aplicațiile sunt instalate.
