# Terrabit Helpdesk Connector (localizat la `terrabit_helpdesk_connector/index.md`)

- **Nume Tehnic:** `terrabit_helpdesk_connector`
- **Versiune:** `19.0.0.3.10`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_helpdesk_connector
- **Cale Locală:** `odoo-addons/terrabit/terrabit_helpdesk_connector`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce tichetele de suport Terrabit direct în Odoo-ul clientului, fără email și fără portal
separat: utilizatorul deschide un tichet, urmărește statusul real (nou, în lucru, așteaptă
răspunsul clientului, închis), vede cine din Terrabit se ocupă de el și poartă discuția din chatter,
la fel ca pe orice document Odoo. Colegii din aceeași firmă văd și tichetele celorlalți, ca să nu se
deschidă de două ori aceeași problemă. Dacă serverul Terrabit e temporar indisponibil, tichetul sau
răspunsul nu se pierd — rămân într-o coadă locală și pleacă automat la revenire.

#### 2. Funcționalități Cheie

- Deschiderea unui tichet nou direct din formularul standard Odoo (subiect, urgență pe 4 niveluri,
  descriere, fișiere atașate prin drag&drop sau lipite cu Ctrl+V), fără wizard separat. Tichetul
  nou e o **ciornă**: Odoo îl salvează pe parcurs, dar pleacă la Terrabit doar la butonul
  **Trimite la Terrabit** — altfel salvarea automată trimitea tichete incomplete.
- Ecranul **Tichetele mele** (`Terrabit Support → Tichetele mele`): kanban/listă grupate pe status,
  în ordinea firească a fluxului (Ciornă, De trimis, Nou, În lucru, De răspuns, Închis), cu urgență,
  consultant atribuit și dată de deschidere.
- Tichetele cu răspuns nou necitit ies în evidență: în kanban bară colorată pe card și eticheta
  „Răspuns nou”, în listă rândul îngroșat și colorat — doar la autor, dispare când citește discuția.
- Autorul tichetului e anunțat în Odoo, la clopoțel (doar inbox, fără email), când vine un
  răspuns nou de la Terrabit — nu pentru propriile mesaje și nici pentru istoricul adus la prima
  sincronizare.
- Ecranul **Tichete echipă** (`Terrabit Support → Tichete echipă`): toate tichetele companiei, indiferent
  cine le-a deschis (inclusiv cele venite direct la Terrabit prin telefon/email), grupabile după
  status, urgență, autor sau consultant.
- Discuție bidirecțională prin chatter: răspunsurile publice ale consultanților Terrabit apar local,
  iar răspunsurile clientului pleacă automat spre Terrabit; notele interne scrise cu „Scrie notă” nu
  ies niciodată din baza clientului, iar notele interne ale consultanților nu ajung la client.
- Coadă de retrimitere automată (cronul de sincronizare, la 15 minute, plus la fiecare notificare de la Terrabit) pentru tichete și răspunsuri neplecate din cauza
  indisponibilității serverului Terrabit, cu deduplicare (nu se creează tichete duble) și buton
  **Actualizează acum** pentru sincronizare imediată.
- Sincronizare automată a stadiului, consultantului atribuit și discuției, plus curățarea locală a
  tichetelor retrase la Terrabit.
- Sincronizare incrementală: fiecare rulare aduce doar tichetele și mesajele modificate de la
  ultima sincronizare; o dată pe zi rulează una completă, care prinde și ce a dispărut (tichet mutat
  pe altă companie, mesaj retras). Un tichet care apare prima oară (creat direct la Terrabit,
  mutat pe companie, dezarhivat) vine cu toată discuția. Cu un server mai vechi, sincronizarea
  rămâne completă.
- Meniuri **Tichete echipă**, **Tichete în așteptare** și **Tichete închise** (consultare, doar citire).
- Status **În așteptare**: clientul își parchează singur tichetul (**Pune în așteptare** / **Reia**).
- Urgență pe 4 niveluri: 0★ Normal, 1★ Urgent, 2★ Critic, 3★ Blocant, cu explicație lângă stele.
- Aviz în Odoo pentru tichetele care așteaptă răspunsul clientului de peste 24 h (autor sau persoană
  desemnată pe cont).
- Tichetul nou legat arată textul sursă separat, needitabil.
- Discuția (chatterul) stă mereu sub tichet, pe toată lățimea, și pe ecranele late.
- Buton **Trimite la Terrabit** în fereastra de eroare Odoo („Ups!”): deschide o ciornă cu mesajul real
  al erorii, pagina și traceback-ul completate.
- Bara de status cu timp pe tichet (Nou → În lucru → De răspuns → Închis), ca bara de stadii de la
  Terrabit; timpul statusului curent crește în direct. Orele pontate rămân doar la Terrabit.
- Duplicarea sau butonul **Tichet nou legat** (pe tichetele închise) creează o ciornă nouă, „Continuare
  la #cod”, cu trimitere la tichetul original.
- Clientul își poate închide singur tichetul (buton **Închide tichetul**, cu confirmare), dacă echipa
  Terrabit are bifa **Closure by Customers**; un tichet închis nu se redeschide.
- Reconcilierea zilnică cere doar id-urile mesajelor și aduce întregi numai pe cele lipsă; mesajele
  retrase se șterg pe lista de id-uri, inclusiv la discuțiile de peste 500 de mesaje.
- Actualizare imediată: Terrabit anunță baza clientului printr-o notificare semnată, fără date
  (`/terrabit_helpdesk/notify`), conectorul sincronizează în fundal și reîncarcă singur lista, kanbanul
  și tichetul deschis, în câteva secunde (sincronizarea pornește imediat, pe un fir separat; o singură
  sincronizare odată). Cronul de 15 minute rămâne pentru bazele pe care Terrabit nu le poate contacta.
- Panou deasupra listei și a kanbanului, în stilul tabloului din Helpdesk: tichetele mele (deschise,
  cu răspuns nou, netrimise) și sincronizarea (ultima, următoarea; o încercare eșuată apare cu roșu,
  cu motivul la trecerea mouse-ului). „Sync Now” există și pe formularul tichetului.
- Trecere automată pe endpointul de staging (`terrabit-staging.odoo.com`) când baza e neutralizată,
  ca testele să nu ajungă în helpdesk-ul de producție. Verificarea se face la instalare și înainte
  de fiecare sincronizare, deci și o copie restaurată a producției trece singură pe staging; un
  endpoint local pus intenționat rămâne neatins.
- Gestionare inteligentă a fișierelor mari: cele sub 2 MB se copiază la Terrabit, cele peste rămân în
  baza clientului și se trimite doar un link cu token de acces.
- Auto-înregistrare pe serverul Terrabit, fără cod de activare manual: la instalare se creează
  contul IAP pentru serviciul `terrabit_helpdesk`, iar un cron zilnic reia înregistrarea dacă
  serverul e temporar indisponibil.
- Tichetul pleacă la Terrabit pe contul propriei companii (cu mai multe companii active); un cont
  comun, fără companie, este doar rezerva.
- **Chat de suport** (`Terrabit Support → Chat`): discuție liberă cu Terrabit din Discuss, în canalul
  „Terrabit Support” al companiei; mesajele ajung la Terrabit, răspunsurile consultanților apar în
  același canal, cu notificarea obișnuită din Discuss. Chatul e oprit implicit și se activează din
  contul IAP Terrabit Helpdesk (bifa *Support chat*); meniul apare doar dacă e activat. Canalul e
  restricționat la companiile contului de suport (un canal al unui cont fără companie rămâne
  vizibil tuturor). Un mesaj scris cât Terrabit nu răspunde pleacă la următoarea sincronizare, fără
  dublare, iar discuțiile de peste 500 de mesaje se aduc pe pagini, cu reluare de la ultima pagină
  aplicată.
- Fără duplicate la răspunsuri: conectorul trimite o cheie stabilă de cerere (`request_key`, bază de
  date + mesaj local) atât la trimiterea imediată, cât și la reîncercarea din coadă; sincronizarea
  pornită de o notificare așteaptă salvarea răspunsului înainte să-l copieze. Un răspuns corectat la
  Terrabit se corectează și în discuție, cu tot cu fișiere. Necesită `terrabit_iap_server_helpdesk`
  19.0.0.3.1 sau mai nou.
- Pe tichet apar numărul de memento-uri trimise de Terrabit pe e-mail de la ultimul răspuns
  (*Reminders*, *Last reminder*, și coloană opțională în listă), care revine la zero după răspunsul
  clientului; necesită server 19.0.0.3.0 sau mai nou, altfel câmpurile rămân goale.
- Butonul **Sync Now** funcționează pentru orice utilizator intern, nu doar pentru administratori.

#### 3. Dependențe

- [terrabit_iap](../terrabit_iap/index.md)
- `iap`
- `mail`

#### 4. Componente Cheie

**Modele**

- `terrabit.helpdesk.ticket`: oglinda locală, doar-citire pentru client (cu excepția câmpurilor
  completate la deschidere), a tichetului de pe Terrabit — status proiectat pe 4 stări stabile
  (pending/new/in_progress/awaiting/closed), urgență, consultant atribuit, fișiere, coadă de
  trimitere cu `request_key` pentru deduplicare și releu automat al mesajelor din chatter.
- `iap.account` (extins): găzduiește logica de comunicare cu serverul Terrabit
  (`_terrabit_helpdesk_submit_ticket`, `_terrabit_helpdesk_fetch_tickets`,
  `_terrabit_helpdesk_fetch_messages`, `_terrabit_helpdesk_post_message`), protecția endpointului pe
  bazele neutralizate, cron-urile de înregistrare/sincronizare și câmpurile chatului de suport
  (`terrabit_chat_enabled`, `terrabit_chat_channel_id`).
- `discuss.channel` (extins): canalul „Terrabit Support” al chatului de suport, restricționat pe companiile contului de suport (regulă multi-companie).
- `mail.message` (extins): câmpul `terrabit_remote_id`, ancora de deduplicare pentru mesajele
  oglindite din discuția cu Terrabit.

**Vizualizări**

- `view_terrabit_helpdesk_ticket_kanban` / `view_terrabit_helpdesk_ticket_list`: listele „Tichetele
  mele” și „Tichete echipă”, grupate implicit pe status, cu buton „Sync Now” în antet și panoul cu
  tichetele mele și starea sincronizării deasupra listei.
- `view_terrabit_helpdesk_ticket_form`: formularul de tichet, cu zona de fișiere
  (`terrabit_attachment_dropzone`), avertisment când tichetul n-a plecat încă la Terrabit și chatter
  pentru discuție.
- `view_terrabit_helpdesk_ticket_search`: filtre pe status și pe „Mine”, grupări după status,
  urgență, autor și consultant.
- Meniu rădăcină `Terrabit Support`, cu submeniurile `My Tickets`, `Team Tickets` („Tichete echipă”),
  `Tickets On Hold` („Tichete în așteptare”), `Closed Tickets` („Tichete închise”) și `Chat`
  (`menu_terrabit_support_chat`, vizibil doar grupului *Terrabit support chat available*).
- `iap_account_view_form_terrabit_support_chat`: extinde contul IAP Terrabit Helpdesk cu bifa *Support chat* și canalul asociat.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_register_terrabit_helpdesk`: rulează zilnic, reia înregistrarea automată a contului IAP pe
  serverul Terrabit (fără cod de activare manual).
- `ir_cron_sync_terrabit_helpdesk_tickets`: rulează la 15 minute — trimite tichetele și mesajele din
  coada locală, aduce tichetele și discuțiile de la Terrabit, curăță tichetele retrase.
- `ir_cron_remind_awaiting_reply`: rulează din oră în oră — aviz în Odoo pentru tichetele în
  „De răspuns” de peste 24 de ore, o singură dată pe așteptare.
- `ir_actions_server_sync_terrabit_helpdesk_tickets` ("Sync Now"): acțiune server declanșată din
  butonul din antetul listei/kanbanului, pentru sincronizare imediată la cerere.
- `ir_actions_server_open_terrabit_chat` („Chat with Terrabit”): deschide canalul de chat de suport
  (`_terrabit_chat_open`); legată de modelul tichetelor, nu de `iap.account`, fiindcă utilizatorul
  intern nu are drept de scriere pe contul IAP.

#### 5. Conexiuni

- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): partea de server,
  instalată doar pe helpdesk-ul Terrabit — primește tichetele trimise de acest conector și îi
  întoarce statusul, consultantul atribuit și mesajele publice.
- [terrabit_helpdesk_link](../terrabit_helpdesk_link/index.md): modulul mai vechi, doar un link spre
  portalul de suport; conectorul îl înlocuiește, iar la clienții care îl au pe amândouă, linkul se
  poate dezinstala.
- [terrabit_iap](../terrabit_iap/index.md): furnizează contul de conectare (IAP) și înregistrarea
  automată pe serverul Terrabit, folosite de acest modul pentru autentificare.
