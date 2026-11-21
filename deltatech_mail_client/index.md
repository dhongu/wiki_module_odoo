# Mail Client (localizat la `deltatech_mail_client/index.md`)

- **Nume Tehnic:** `deltatech_mail_client`
- **Versiune:** `19.0.1.7.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_mail_client
- **Cale Locală:** `odoo-addons/bitshop/deltatech_mail_client`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Mail Client este un client de e-mail generic pentru Odoo, conectat la orice server IMAP și SMTP. Fiecare utilizator își salvează propria căsuță (parola e stocată criptat) și își citește, mută și trimite e-mailurile direct din Odoo, din **Discuss → Mail Client**. Mesajele rămân pe serverul de e-mail și sunt citite direct de acolo; se copiază în Odoo doar cele atașate unei înregistrări. Modulul acoperă etapele 1–5 din plan (citire, mutare, trimitere, atașare, securitate și audit); stadiul de dezvoltare rămâne Alpha.

#### 2. Funcționalități Cheie

- **Cont de e-mail per utilizator** (**Discuss → Mail Account**): server IMAP (implicit port 993, SSL/TLS), utilizator și parolă criptată, grup SMTP opțional (adresă expeditor, server, port, securitate; fără credențiale SMTP se folosesc cele IMAP), buton **Test Connection** care raportează numărul de foldere găsite. Serverele cu adrese private sunt refuzate, cu excepția celor permise printr-un parametru de sistem; certificatul TLS este verificat.
- **Citire**: foldere în stânga (cu pictograme după flag-urile serverului), mesaje de la cele mai noi, 30 pe pagină, grupate pe zile, necitite îngroșate; marcare citit/necitit și stea, sincronizate pe server.
- **Randare HTML în siguranță**: mesajele sunt curățate și afișate într-un cadru izolat, fără scripturi și fără imagini externe; anexele sunt listate după nume.
- **Mutare între foldere**: într-un folder ales de utilizator, cu IMAP `MOVE` sau, dacă serverul nu îl are, `COPY` + `\Deleted` + `UID EXPUNGE`; steaua și starea citit se păstrează.
- **Redactare**: mesaj nou, răspuns, răspuns tuturor, redirecționare, cu anexe (maximum 25 MB) și cel mult 100 de destinatari; trimitere prin SMTP-ul căsuței, cu copie în folderul Sent (se poate dezactiva pe cont) și marcarea originalului ca răspuns. Nu există ciorne salvate, iar textul este simplu (plain text).
- **Atașare la documente de business**: butonul **Attach to...** postează mesajul ca notă internă în discuția unui contact, comandă de vânzare/achiziție, factură, transfer, lead sau task (doar pentru aplicațiile instalate), cu textul curățat, anexele și `.eml`-ul original; se execută cu drepturile utilizatorului, iar același mesaj nu se atașează de două ori la aceeași înregistrare. Panoul de citire arată unde e atașat mesajul, contactele cu adresa expeditorului și atașările anterioare pentru același expeditor.
- **Verificare expeditor și avertismente**: rezultatele SPF, DKIM, DMARC scrise de serverul de e-mail (Odoo nu verifică nimic singur) și avertizări informative: expeditor neverificat, Reply-To pe alt domeniu, nume afișat cu altă adresă, domeniu care imită un contact, link cu text diferit de destinație. Nimic nu se blochează.
- **Jurnal de acces** (**Mail Access Log**): cine a deschis, trimis sau atașat ce mesaj și când; append-only (nici administratorii nu pot modifica sau șterge), fără conținutul mesajelor. Utilizatorii își văd liniile proprii, administratorii pe toate.
- **Teme de culori** (**Settings → Mail Client Colors**, per companie): culorile companiei (implicit), Odoo neutru, verde închis sau personalizat (valori `#rrggbb`); respectă modul luminos/întunecat.
- **Plan viitor** (`ROADMAP.md`): etapa 6, căsuțe partajate și notificări; etapa 7, migrare de la `agroamat_mail`. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `mail`
- Dependență Python externă: `cryptography`

#### 4. Componente Cheie

**Modele**

- `mail.client.account`: contul IMAP/SMTP al utilizatorului, cu parole criptate și operațiile pe server (test, listare foldere, citire, mutare, trimitere).
- `mail.client.link`: legătura privată dintre un mesaj de pe server și o înregistrare Odoo la care a fost atașat.
- `mail.client.audit`: jurnalul de acces append-only (deschidere, trimitere, atașare).
- `res.company` / `res.config.settings` (extinse): tema de culori a ecranului Mail Client, per companie.

**Vizualizări**

- `mail_client_account_view_form` / `mail_client_account_view_list`: formularul și lista conturilor de e-mail.
- `mail_client_action` (acțiune client, meniul **Mail Client**): ecranul OWL cu foldere, listă de mesaje și panou de citire (`static/src/js/mail_client.esm.js`).
- `mail_client_audit_view_list` / `mail_client_audit_view_search`: lista și căutarea în **Mail Access Log**.
- `res_config_settings_view_form`: secțiunea de culori din Setări.

**Acțiuni Automate / Acțiuni Server**

- Niciuna (nu există cron-uri sau acțiuni server).

#### 5. Conexiuni

- `agroamat_mail`: modul client din care este planificată migrarea setărilor căsuței, a drepturilor și a legăturilor la anexe (etapa 7, încă neimplementată).
- `sale`, `purchase`, `account`, `stock`, `crm`, `project`: opționale; înregistrările lor pot fi țintă pentru **Attach to...** dacă aplicațiile sunt instalate.
