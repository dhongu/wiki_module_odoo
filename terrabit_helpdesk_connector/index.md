# Terrabit Helpdesk Connector (localizat la `terrabit_helpdesk_connector/index.md`)

- **Nume Tehnic:** `terrabit_helpdesk_connector`
- **Versiune:** `19.0.0.2.3`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_helpdesk_connector
- **Cale Locală:** `odoo-addons/terrabit/terrabit_helpdesk_connector`
- **Ultima Ingestie:** `2026-09-24`
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
- Ecranul **Ale echipei** (`Terrabit Support → Ale echipei`): toate tichetele companiei, indiferent
  cine le-a deschis (inclusiv cele venite direct la Terrabit prin telefon/email), grupabile după
  status, urgență, autor sau consultant.
- Discuție bidirecțională prin chatter: răspunsurile publice ale consultanților Terrabit apar local,
  iar răspunsurile clientului pleacă automat spre Terrabit; notele interne scrise cu „Scrie notă” nu
  ies niciodată din baza clientului, iar notele interne ale consultanților nu ajung la client.
- Coadă de retrimitere automată (cron la 15 minute) pentru tichete și răspunsuri neplecate din cauza
  indisponibilității serverului Terrabit, cu deduplicare (nu se creează tichete duble) și buton
  **Actualizează acum** pentru sincronizare imediată.
- Sincronizare automată a stadiului, consultantului atribuit și discuției, plus curățarea locală a
  tichetelor retrase la Terrabit.
- Trecere automată pe endpointul de staging (`terrabit-staging.odoo.com`) când baza e neutralizată,
  ca testele să nu ajungă în helpdesk-ul de producție. Verificarea se face la instalare și înainte
  de fiecare sincronizare, deci și o copie restaurată a producției trece singură pe staging; un
  endpoint local pus intenționat rămâne neatins.
- Gestionare inteligentă a fișierelor mari: cele sub 2 MB se copiază la Terrabit, cele peste rămân în
  baza clientului și se trimite doar un link cu token de acces.

#### 3. Dependențe

- `terrabit_iap`
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
  bazele neutralizate și cron-urile de înregistrare/sincronizare.
- `mail.message` (extins): câmpul `terrabit_remote_id`, ancora de deduplicare pentru mesajele
  oglindite din discuția cu Terrabit.

**Vizualizări**

- `view_terrabit_helpdesk_ticket_kanban` / `view_terrabit_helpdesk_ticket_list`: listele „Tichetele
  mele” și „Ale echipei”, grupate implicit pe status, cu buton „Sync Now” în antet.
- `view_terrabit_helpdesk_ticket_form`: formularul de tichet, cu zona de fișiere
  (`terrabit_attachment_dropzone`), avertisment când tichetul n-a plecat încă la Terrabit și chatter
  pentru discuție.
- `view_terrabit_helpdesk_ticket_search`: filtre pe status și pe „Mine”, grupări după status,
  urgență, autor și consultant.
- Meniu rădăcină `Terrabit Support`, cu submeniurile `My Tickets` și `Team Tickets`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_register_terrabit_helpdesk`: rulează zilnic, reia înregistrarea automată a contului IAP pe
  serverul Terrabit (fără cod de activare manual).
- `ir_cron_sync_terrabit_helpdesk_tickets`: rulează la 15 minute — trimite tichetele și mesajele din
  coada locală, aduce tichetele și discuțiile de la Terrabit, curăță tichetele retrase.
- `ir_actions_server_sync_terrabit_helpdesk_tickets` ("Sync Now"): acțiune server declanșată din
  butonul din antetul listei/kanbanului, pentru sincronizare imediată la cerere.

#### 5. Conexiuni

- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): partea de server,
  instalată doar pe helpdesk-ul Terrabit — primește tichetele trimise de acest conector și îi
  întoarce statusul, consultantul atribuit și mesajele publice.
- [terrabit_helpdesk_link](../terrabit_helpdesk_link/index.md): modulul mai vechi, doar un link spre
  portalul de suport; conectorul îl înlocuiește, iar la clienții care îl au pe amândouă, linkul se
  poate dezinstala.
- `terrabit_iap`: furnizează contul de conectare (IAP) și înregistrarea automată pe serverul
  Terrabit, folosite de acest modul pentru autentificare.
