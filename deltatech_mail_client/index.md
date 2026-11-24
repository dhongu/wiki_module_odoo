# Mail Client (localizat la `deltatech_mail_client/index.md`)

- **Nume Tehnic:** `deltatech_mail_client`
- **Versiune:** `19.0.1.31.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_mail_client
- **Cale Locală:** odoo-addons/bitshop/deltatech_mail_client
- **Ultima Ingestie:** `2026-11-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Mail Client este un client de e-mail generic pentru Odoo, conectat la orice server IMAP și SMTP. Fiecare utilizator își salvează propria căsuță (parola e stocată criptat) și își citește, mută și trimite e-mailurile direct din Odoo, din aplicația proprie **Mail Client**; căsuțele pot fi și partajate între utilizatori, cu drept de citire sau complet. Mesajele rămân pe serverul de e-mail și sunt citite direct de acolo; se copiază în Odoo doar cele atașate unei înregistrări. Modulul acoperă citirea, mutarea, trimiterea, atașarea, securitatea, auditul și căsuțele partajate, plus notificări de mail nou, căutare (într-un dosar sau în toate), selecție multiplă, ciorne automate, sugestii de destinatari, editor HTML și semnătură per căsuță; stadiul de dezvoltare rămâne Alpha.

#### 2. Funcționalități Cheie

- **Cont de e-mail per utilizator** (**Mail Client → Configuration → Mail Accounts**): server IMAP (implicit port 993, SSL/TLS), utilizator și parolă criptată, grup SMTP opțional (adresă expeditor, server, port, securitate; fără credențiale SMTP se folosesc cele IMAP), buton **Test Connection** care raportează numărul de foldere găsite. Serverele cu adrese private sunt refuzate, cu excepția celor permise printr-un parametru de sistem; certificatul TLS este verificat.
- **Autentificare OAuth2 pentru Gmail și Microsoft 365** (**Sign in with**): Google și Microsoft nu mai acceptă parola contului pe IMAP/SMTP, deci căsuța se conectează cu contul însuși (**Connect with Google / Microsoft**, **Disconnect** retrage accesul); contul autentificat trebuie să fie cel din **Username**, iar accesul se reînnoiește singur. La Google trebuie bifată permisiunea Gmail. Administratorul configurează o singură dată aplicația la Google/Microsoft (ID și secret) în **Settings → General Settings → Emails**, dacă abonamentul Odoo nu oferă serviciul de autentificare; varianta Microsoft nu a fost încă încercată cu un cont real.
- **Căsuțe partajate**: proprietarul bifează **Shared Mailbox** și adaugă membri cu acces *Read* (citește și marchează ca citit) sau *Full* (și stea, mutare, scriere, trimitere, atașare). Doar proprietarul vede datele de conectare și poate schimba membrii; un selector deasupra folderelor comută între căsuța personală și cele partajate, iar mesajele se trimit de la adresa căsuței partajate. Administratorii văd toate căsuțele din **All Mailboxes**.
- **Citire**: foldere în stânga (cu pictograme după rolul lor: inbox, sent, drafts, archive, spam, trash), mesaje de la cele mai noi, 30 pe pagină, grupate pe zile, necitite îngroșate; marcare citit/necitit și stea, sincronizate pe server.
- **Randare HTML în siguranță**: mesajele sunt curățate și afișate într-un cadru izolat, fără scripturi și fără imagini externe (expeditorul ar vedea prin ele că mesajul a fost deschis); culorile, fonturile și aspectul mesajului se păstrează. Butonul **Show images** afișează imaginile (doar `https`) numai pentru mesajul curent și se înregistrează în jurnalul de acces. Anexele apar ca fișe cu pictogramă, nume și mărime, cu previzualizare (imagini, PDF) sau descărcare.
- **Mutare, arhivare, spam, ștergere**: mutare într-un folder ales (IMAP `MOVE` sau, dacă serverul nu îl are, `COPY` + `\Deleted` + `UID EXPUNGE`); butoanele **Archive**, **Spam**, **Delete** duc mesajul în folderul cu rolul respectiv (Delete merge în coșul de gunoi, recuperabil; dacă folderul lipsește, proprietarul e întrebat dacă îl creează). Steaua și starea citit se păstrează.
- **Tragere și meniu clic dreapta**: un mesaj (sau selecția) se mută tragându-l peste un folder din coloana din stânga (necesită drept de scriere; pe ecran tactil se folosește **Move to...**). Clic dreapta pe un rând deschide meniul: citit/necitit, stea, **Move to...**, arhivare, spam, coș; acționează pe rândul respectiv sau pe toată selecția, fără a deschide mesajul. Membrii cu drept doar de citire văd doar citit/necitit.
- **Foldere uzuale și restul**: coloana arată întâi folderele uzuale (inbox, sent, drafts, archive, spam, trash), apoi grupul **Other folders**; peste cinci foldere în grup, acesta e pliat (alegerea se ține per căsuță, în browser), cu totalul necitit pe linia lui, și se deschide singur la tragerea unui mesaj.
- **Gestionarea folderelor** (doar proprietarul): creare, redenumire, ștergere (doar folder gol și fără subfoldere), golirea coșului sau a spamului cu confirmare; folderele de sistem nu se redenumesc și nu se șterg. Golirea este singura modalitate de ștergere definitivă din modul și se înregistrează în jurnal.
- **Selecție multiplă**: casete de bifat, Shift+click pentru interval, Ctrl/Cmd+click pentru adăugare; bara de acțiuni marchează citit/necitit, pune stea, arhivează, trimite la spam, șterge sau mută mesajele paginii curente (în căutarea în toate folderele, selecția multiplă nu e disponibilă).
- **Căutare și filtre**, direct pe serverul de e-mail: cuvinte în subiect, expeditor și destinatari (între ghilimele pentru expresii) și operatorii `from:`, `to:`, `subject:`, `is:unread/read/starred/unstarred`, `has:attachment`, `after:`, `before:`; butoanele **Unread**, **Starred**, **With attachment** adaugă operatorul automat. Implicit se caută în folderul deschis (**This folder**); **All folders** caută în toate folderele căsuței (fără coș și spam, decât cu **Include Trash and Spam**; cel mult 40 de foldere și 500 de potriviri per folder, cu avertizare de rezultat parțial), fiecare mesaj arătând folderul ca etichetă. Căutarea în textul mesajelor și selecția peste mai multe pagini nu sunt încă disponibile.
- **Mail nou: contoare și notificări**: insignă cu numărul de necitite lângă fiecare folder, total în titlul tab-ului, iar clopoțelul de sub foldere pornește notificările (implicit oprite) pentru utilizator și căsuță. O acțiune programată rulează la 5 minute, verifică doar inbox-ul și anunță pe orice ecran Odoo expeditorul și subiectul ultimului mesaj; prima verificare doar reține starea. Un plic în bara de sus arată totalul necitit pentru căsuțele cu notificări active (valoare de până la 5 minute vechime).
- **Starea verificării**: grupul **New-mail check** din căsuță arată câți utilizatori o urmăresc, ultima verificare, numărul de necitite și eroarea serverului dacă ultima verificare a eșuat (ex. parolă schimbată); lista are coloane similare, rând roșu la eșec și filtrul **Check Failed**. Câmpurile goale nu indică o defecțiune dacă nimeni nu urmărește căsuța.
- **Redactare**: mesaj nou, răspuns, răspuns tuturor, redirecționare (Ctrl+Enter trimite), cu anexe (maximum 25 MB) și cel mult 100 de destinatari; trimitere prin SMTP-ul căsuței, cu copie în folderul Sent (se poate dezactiva cu **Keep a Copy in Sent**) și marcarea originalului ca răspuns. Textul se scrie într-un editor HTML cu bară de formatare la selecție (titlu, mărime, bold, italic, subliniere, culoare, listă, link); mesajul pleacă cu formatare și cu versiune text simplu; imaginile nu se pot pune în text.
- **Semnătură per căsuță**: grupul **Signature** din **Mail Account**; mesajul nou, răspunsul și redirecționarea încep cu semnătura după linia `--` (deasupra citatului la răspuns). Dacă căsuța nu are semnătură se folosește cea din preferințele utilizatorului (sau, dacă firma folosește `deltatech_mail_signature`, cea generată pentru fiecare utilizator din șablonul companiei); într-o căsuță partajată semnătura căsuței se aplică tuturor membrilor, iar doar proprietarul o schimbă. Semnătura poate conține imagini (logo, banner — `/image` sau dialogul media), trimise în interiorul mesajului: cel mult 5 imagini de câte 300 KB, PNG, JPEG sau GIF, verificate la salvare. În textul mesajului propriu-zis imaginile rămân indisponibile.
- **Ciorne automate și sugestii de destinatari**: textul se salvează la 5 secunde după ultima modificare în folderul Drafts de pe server (nimic în Odoo, deci ciorna se vede și de pe telefon), o ciornă per mesaj; la părăsirea ecranului sau schimbarea mesajului ciorna se păstrează, iar din Drafts se continuă cu **Continue writing**. Serverele fără folder Drafts dau avertisment și nu salvează. În **To**, **Cc**, **Bcc** apar, după două caractere, până la 8 contacte cu e-mail, căutate după nume sau adresă; câmpul rămâne text liber.
- **Atașare la documente de business**: butonul **Attach to...** postează mesajul ca notă internă în discuția unui contact, comandă de vânzare/achiziție, factură, transfer, lead sau task (doar pentru aplicațiile instalate), cu textul curățat, anexele și `.eml`-ul original; se execută cu drepturile utilizatorului, iar același mesaj nu se atașează de două ori la aceeași înregistrare. Panoul de citire arată unde e atașat mesajul, contactele cu adresa expeditorului și atașările anterioare pentru același expeditor; legăturile sunt private, iar cele făcute într-o căsuță partajată sunt vizibile tuturor membrilor ei.
- **Verificare expeditor și avertismente**: un rezumat în cuvinte simple deasupra verificărilor tehnice — **Verified sender**, **Partly verified**, **Sender not verified** sau **Sender not checked**, plus **Outside the company** când domeniul expeditorului nu e al firmei (domeniul căsuței, e-mailul și site-ul companiilor), cu motivele sub **Why?**. Dedesubt, rezultatele SPF, DKIM, DMARC scrise de serverul de e-mail (Odoo nu verifică nimic singur) și avertizări informative: expeditor neverificat, Reply-To pe alt domeniu, nume afișat cu altă adresă, domeniu cu caractere speciale sau care imită un contact, link cu text diferit de destinație. Nimic nu se blochează.
- **Jurnal de acces** (**Mail Access Log**): cine a deschis, trimis sau atașat ce mesaj și când, plus acțiunile pe foldere; append-only (nici administratorii nu pot modifica sau șterge), fără conținutul mesajelor, cu indicarea căsuței vizate. Utilizatorii își văd liniile proprii (proprietarul căsuței le vede și pe ale membrilor), administratorii pe toate.
- **Teme de culori** (**Settings → Mail Client Colors**, per companie): culorile companiei (implicit), Odoo neutru, verde închis sau personalizat (valori `#rrggbb`); respectă modul luminos/întunecat.
- **Viteză**: conexiunea la serverul de e-mail rămâne autentificată două minute după ultimul clic; timpul se schimbă cu parametrul de sistem `deltatech_mail_client.imap_session_seconds` (secunde; `0` = autentificare la fiecare acțiune).
- **Plan viitor** (`ROADMAP.md`): creare de lead/task/tichet din mesaj, căutare în textul mesajelor și selecție peste mai multe pagini, IDLE (push în loc de verificarea la 5 minute), migrare de la `agroamat_mail` (etapa 7). Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `mail`
- `bus`
- `html_editor`
- `google_gmail`
- `microsoft_outlook`
- Dependență Python externă: `cryptography`

#### 4. Componente Cheie

**Modele**

- `mail.client.account` (moștenește `google.gmail.mixin` și `microsoft.outlook.mixin` pentru OAuth2): contul IMAP/SMTP al utilizatorului (personal sau partajat), cu parole criptate, semnătura căsuței și operațiile pe server (test, listare foldere, citire, căutare, mutare, trimitere, ciorne, verificare mail nou).
- `mail.client.member`: membrii unei căsuțe partajate și nivelul lor de acces (citire sau complet).
- `mail.client.link`: legătura privată dintre un mesaj de pe server și o înregistrare Odoo la care a fost atașat.
- `mail.client.audit`: jurnalul de acces append-only (deschidere, trimitere, atașare, operații pe foldere).
- `mail.client.watch`: abonarea unui utilizator la notificările de mail nou pentru o căsuță (câte o linie unică per căsuță și utilizator).
- `res.company` / `res.config.settings` (extinse): tema de culori a ecranului Mail Client, per companie.

**Vizualizări**

- `mail_client_account_view_form` / `mail_client_account_view_list` / `mail_client_account_view_search`: formularul, lista și căutarea conturilor de e-mail (**Mail Account**, plus **All Mailboxes** pentru administratori).
- `mail_client_action` (acțiune client, meniul **Mail Client → Mailbox**): ecranul OWL cu foldere, listă de mesaje și panou de citire (`static/src/js/mail_client.esm.js`), plus serviciul de notificări și plicul din bara de sus (`mail_client_systray.esm.js`).
- `mail_client_audit_view_list` / `mail_client_audit_view_search`: lista și căutarea în **Mail Access Log**.
- `res_config_settings_view_form`: secțiunea de culori din Setări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_mail_client_check` („Mail Client: check for new mail”): rulează la fiecare 5 minute `model._cron_check_mail()`, verifică starea inbox-ului căsuțelor cu notificări active și anunță utilizatorii abonați când a sosit mail necitit.

#### 5. Conexiuni

- `agroamat_mail`: modul client din care este planificată migrarea setărilor căsuței, a drepturilor și a legăturilor la anexe (etapa 7, încă neimplementată).
- `deltatech_mail_signature`: opțional; generează semnătura fiecărui utilizator din șablonul companiei, folosită de Mail Client când căsuța nu are semnătură proprie.
- `sale`, `purchase`, `account`, `stock`, `crm`, `project`: opționale; înregistrările lor pot fi țintă pentru **Attach to...** dacă aplicațiile sunt instalate.
