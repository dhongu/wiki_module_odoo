# Mail Client (localizat la `deltatech_mail_client/index.md`)

- **Nume Tehnic:** `deltatech_mail_client`
- **Versiune:** `19.0.1.18.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_mail_client
- **Cale Locală:** `odoo-addons/bitshop/deltatech_mail_client`
- **Ultima Ingestie:** `2026-11-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Mail Client este un client de e-mail generic pentru Odoo, conectat la orice server IMAP și SMTP. Fiecare utilizator își salvează propria căsuță (parola e stocată criptat) și își citește, mută și trimite e-mailurile direct din Odoo, din **Discuss → Mail Client**; căsuțele pot fi și partajate între utilizatori, cu drept de citire sau complet. Mesajele rămân pe serverul de e-mail și sunt citite direct de acolo; se copiază în Odoo doar cele atașate unei înregistrări. Modulul acoperă citirea, mutarea, trimiterea, atașarea, securitatea, auditul și căsuțele partajate, plus notificări de mail nou, căutare (într-un dosar sau în toate), selecție multiplă, ciorne automate, sugestii de destinatari, editor HTML și semnătură per căsuță; stadiul de dezvoltare rămâne Alpha.

#### 2. Funcționalități Cheie

- **Cont de e-mail per utilizator** (**Discuss → Mail Account**): server IMAP (implicit port 993, SSL/TLS), utilizator și parolă criptată (pentru Gmail sau Microsoft 365 se folosește o parolă de aplicație), grup SMTP opțional (adresă expeditor, server, port, securitate; fără credențiale SMTP se folosesc cele IMAP), buton **Test Connection** care raportează numărul de foldere găsite. Serverele cu adrese private sunt refuzate, cu excepția celor permise printr-un parametru de sistem; certificatul TLS este verificat.
- **Căsuțe partajate**: proprietarul bifează **Shared Mailbox** și adaugă membri cu acces *Read* (citește și marchează ca citit) sau *Full* (și stea, mutare, scriere, trimitere, atașare). Doar proprietarul vede datele de conectare și poate schimba membrii; un selector deasupra folderelor comută între căsuța personală și cele partajate, iar mesajele se trimit de la adresa căsuței partajate. Administratorii văd toate căsuțele din **All Mailboxes**.
- **Citire**: foldere în stânga (cu pictograme după rolul lor: inbox, sent, drafts, archive, spam, trash), mesaje de la cele mai noi, 30 pe pagină, grupate pe zile, necitite îngroșate; marcare citit/necitit și stea, sincronizate pe server.
- **Randare HTML în siguranță**: mesajele sunt curățate și afișate într-un cadru izolat, fără scripturi și fără imagini externe; anexele sunt listate după nume.
- **Mutare, arhivare, spam, ștergere**: mutare într-un folder ales (IMAP `MOVE` sau, dacă serverul nu îl are, `COPY` + `\Deleted` + `UID EXPUNGE`); butoanele **Archive**, **Spam**, **Delete** duc mesajul în folderul cu rolul respectiv (Delete merge în coșul de gunoi, recuperabil; dacă folderul lipsește, proprietarul e întrebat dacă îl creează). Steaua și starea citit se păstrează.
- **Gestionarea folderelor** (doar proprietarul): creare, redenumire, ștergere (doar folder gol și fără subfoldere), golirea coșului sau a spamului cu confirmare; folderele de sistem nu se redenumesc și nu se șterg. Golirea este singura modalitate de ștergere definitivă din modul și se înregistrează în jurnal.
- **Selecție multiplă**: casete de bifat, Shift+click pentru interval, Ctrl/Cmd+click pentru adăugare; bara de acțiuni marchează citit/necitit, pune stea, arhivează, trimite la spam, șterge sau mută mesajele paginii curente (în căutarea în toate folderele, selecția multiplă nu e disponibilă).
- **Căutare și filtre**, direct pe serverul de e-mail: cuvinte în subiect, expeditor și destinatari (între ghilimele pentru expresii) și operatorii `from:`, `to:`, `subject:`, `is:unread/read/starred/unstarred`, `has:attachment`, `after:`, `before:`; butoanele **Unread**, **Starred**, **With attachment** adaugă operatorul automat. Implicit se caută în folderul deschis (**This folder**); **All folders** caută în toate folderele căsuței (fără coș și spam, decât cu **Include Trash and Spam**; cel mult 40 de foldere și 500 de potriviri per folder, cu avertizare de rezultat parțial), fiecare mesaj arătând folderul ca etichetă. Căutarea în textul mesajelor și selecția peste mai multe pagini nu sunt încă disponibile.
- **Mail nou: contoare și notificări**: insignă cu numărul de necitite lângă fiecare folder, total în titlul tab-ului, iar clopoțelul de sub foldere pornește notificările (implicit oprite) pentru utilizator și căsuță. O acțiune programată rulează la 5 minute, verifică doar inbox-ul și anunță pe orice ecran Odoo expeditorul și subiectul ultimului mesaj; prima verificare doar reține starea. Un plic în bara de sus arată totalul necitit pentru căsuțele cu notificări active (valoare de până la 5 minute vechime).
- **Starea verificării**: grupul **New-mail check** din căsuță arată câți utilizatori o urmăresc, ultima verificare, numărul de necitite și eroarea serverului dacă ultima verificare a eșuat (ex. parolă schimbată); lista are coloane similare, rând roșu la eșec și filtrul **Check Failed**. Câmpurile goale nu indică o defecțiune dacă nimeni nu urmărește căsuța.
- **Redactare**: mesaj nou, răspuns, răspuns tuturor, redirecționare (Ctrl+Enter trimite), cu anexe (maximum 25 MB) și cel mult 100 de destinatari; trimitere prin SMTP-ul căsuței, cu copie în folderul Sent (se poate dezactiva cu **Keep a Copy in Sent**) și marcarea originalului ca răspuns. Textul se scrie într-un editor HTML cu bară de formatare la selecție (titlu, mărime, bold, italic, subliniere, culoare, listă, link); mesajul pleacă cu formatare și cu versiune text simplu; imaginile nu se pot pune în text.
- **Semnătură per căsuță**: grupul **Signature** din **Mail Account**; mesajul nou, răspunsul și redirecționarea încep cu semnătura după linia `--` (deasupra citatului la răspuns). Dacă căsuța nu are semnătură se folosește cea din preferințele utilizatorului; într-o căsuță partajată semnătura căsuței se aplică tuturor membrilor, iar doar proprietarul o schimbă. Imaginile din semnătură merg doar ca link `https`.
- **Ciorne automate și sugestii de destinatari**: textul se salvează la 5 secunde după ultima modificare în folderul Drafts de pe server (nimic în Odoo, deci ciorna se vede și de pe telefon), o ciornă per mesaj; la părăsirea ecranului sau schimbarea mesajului ciorna se păstrează, iar din Drafts se continuă cu **Continue writing**. Serverele fără folder Drafts dau avertisment și nu salvează. În **To**, **Cc**, **Bcc** apar, după două caractere, până la 8 contacte cu e-mail, căutate după nume sau adresă; câmpul rămâne text liber.
- **Atașare la documente de business**: butonul **Attach to...** postează mesajul ca notă internă în discuția unui contact, comandă de vânzare/achiziție, factură, transfer, lead sau task (doar pentru aplicațiile instalate), cu textul curățat, anexele și `.eml`-ul original; se execută cu drepturile utilizatorului, iar același mesaj nu se atașează de două ori la aceeași înregistrare. Panoul de citire arată unde e atașat mesajul, contactele cu adresa expeditorului și atașările anterioare pentru același expeditor; legăturile sunt private, iar cele făcute într-o căsuță partajată sunt vizibile tuturor membrilor ei.
- **Verificare expeditor și avertismente**: rezultatele SPF, DKIM, DMARC scrise de serverul de e-mail (Odoo nu verifică nimic singur) și avertizări informative: expeditor neverificat, Reply-To pe alt domeniu, nume afișat cu altă adresă, domeniu cu caractere speciale sau care imită un contact, link cu text diferit de destinație. Nimic nu se blochează.
- **Jurnal de acces** (**Mail Access Log**): cine a deschis, trimis sau atașat ce mesaj și când, plus acțiunile pe foldere; append-only (nici administratorii nu pot modifica sau șterge), fără conținutul mesajelor, cu indicarea căsuței vizate. Utilizatorii își văd liniile proprii (proprietarul căsuței le vede și pe ale membrilor), administratorii pe toate.
- **Teme de culori** (**Settings → Mail Client Colors**, per companie): culorile companiei (implicit), Odoo neutru, verde închis sau personalizat (valori `#rrggbb`); respectă modul luminos/întunecat.
- **Plan viitor** (`ROADMAP.md`): creare de lead/task/tichet din mesaj, căutare în textul mesajelor, OAuth2 pentru Gmail și Microsoft 365, migrare de la `agroamat_mail` (etapa 7). Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `mail`
- `bus`
- `html_editor`
- Dependență Python externă: `cryptography`

#### 4. Componente Cheie

**Modele**

- `mail.client.account`: contul IMAP/SMTP al utilizatorului (personal sau partajat), cu parole criptate, semnătura căsuței și operațiile pe server (test, listare foldere, citire, căutare, mutare, trimitere, ciorne, verificare mail nou).
- `mail.client.member`: membrii unei căsuțe partajate și nivelul lor de acces (citire sau complet).
- `mail.client.link`: legătura privată dintre un mesaj de pe server și o înregistrare Odoo la care a fost atașat.
- `mail.client.audit`: jurnalul de acces append-only (deschidere, trimitere, atașare, operații pe foldere).
- `mail.client.watch`: abonarea unui utilizator la notificările de mail nou pentru o căsuță (câte o linie unică per căsuță și utilizator).
- `res.company` / `res.config.settings` (extinse): tema de culori a ecranului Mail Client, per companie.

**Vizualizări**

- `mail_client_account_view_form` / `mail_client_account_view_list` / `mail_client_account_view_search`: formularul, lista și căutarea conturilor de e-mail (**Mail Account**, plus **All Mailboxes** pentru administratori).
- `mail_client_action` (acțiune client, meniul **Mail Client**): ecranul OWL cu foldere, listă de mesaje și panou de citire (`static/src/js/mail_client.esm.js`), plus serviciul de notificări și plicul din bara de sus (`mail_client_systray.esm.js`).
- `mail_client_audit_view_list` / `mail_client_audit_view_search`: lista și căutarea în **Mail Access Log**.
- `res_config_settings_view_form`: secțiunea de culori din Setări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_mail_client_check` („Mail Client: check for new mail”): rulează la fiecare 5 minute `model._cron_check_mail()`, verifică starea inbox-ului căsuțelor cu notificări active și anunță utilizatorii abonați când a sosit mail necitit.

#### 5. Conexiuni

- `agroamat_mail`: modul client din care este planificată migrarea setărilor căsuței, a drepturilor și a legăturilor la anexe (etapa 7, încă neimplementată).
- `sale`, `purchase`, `account`, `stock`, `crm`, `project`: opționale; înregistrările lor pot fi țintă pentru **Attach to...** dacă aplicațiile sunt instalate.
