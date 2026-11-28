# Helpdesk Connector (localizat la `terrabit_helpdesk_connector/index.md`)

- **Nume Tehnic:** `terrabit_helpdesk_connector`
- **Versiune:** `20.0.0.3.5`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_helpdesk_connector
- **Cale Locală:** `odoo-addons/terrabit/terrabit_helpdesk_connector`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce tichetele de suport Terrabit direct în Odoo-ul clientului, fără email și fără portal separat. Baza de date se conectează la helpdesk-ul Terrabit printr-un cont IAP și păstrează o copie locală a tichetelor și a întregii discuții, sincronizată în ambele sensuri. Utilizatorul deschide un tichet, urmărește starea reală, vede cine din Terrabit se ocupă de el și poartă discuția din chatter. Dacă serverul Terrabit e temporar indisponibil, tichetul sau răspunsul rămân într-o coadă locală și pleacă singure la revenire.

#### 2. Funcționalități Cheie

- **Conexiune:** contul IAP al serviciului `terrabit_helpdesk` se creează la instalare, iar baza se înregistrează singură pe serverul Terrabit, fără cod de activare; o acțiune zilnică reia înregistrarea cât timp serverul nu răspunde.
- **Baze neutralizate:** pe o copie neutralizată (staging odoo.sh sau `odoo-bin neutralize`) conexiunea trece pe serverul de test Terrabit, iar tichetele locale se golesc, ca testele să nu deschidă sau să nu răspundă pe tichete reale.
- **Tichete:** meniul **Terrabit Support** cu *Tichetele mele*, *Ale echipei*, *În așteptare* și *Închise*, în listă și kanban, cu starea curentă, consultantul, urgența (Normal, Urgent, Critic, Blocant) și timpul petrecut în fiecare stare.
- Deschiderea unui tichet cu subiect, descriere și fișiere (drag and drop sau lipire de imagini); la nevoie tichetul așteaptă într-o coadă de trimitere, cu motivul scris pe el.
- Răspunsuri din chatter: mesajele și fișierele pleacă la Terrabit, iar răspunsurile echipei de suport revin în același fir.
- Punere în așteptare, reluare și închidere a tichetului, sau un tichet nou legat de unul închis.
- Sincronizare la 15 minute, instantanee când Terrabit notifică baza de date, sau la cerere cu **Sync Now**; panoul de deasupra listei arată ultima sincronizare și eventualele erori.
- Notificare când un tichet așteaptă răspunsul clientului de peste 24 de ore.
- **Chat de suport:** meniul **Terrabit Support > Chat** deschide canalul *Terrabit Support* din Discuss; este activat per cont IAP Terrabit Helpdesk și este dezactivat implicit.
- **Raportare erori:** dialogul de eroare Odoo primește butonul **Send to Terrabit**, care deschide un tichet precompletat cu pagina și detaliile tehnice.
- Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `iap`
- `mail`
- [terrabit_iap](../terrabit_iap/index.md)

#### 4. Componente Cheie

**Modele**

- `terrabit.helpdesk.ticket`: oglinda locală a tichetului de pe serverul Terrabit, cu stare, urgență, consultant, fișiere, coadă de trimitere și releu al mesajelor din chatter (`mail.thread`).
- `iap.account` (extins): logica de comunicare cu serverul Terrabit (trimitere tichete, aducere tichete și mesaje, postare mesaje), protecția endpointului pe baze neutralizate și înregistrarea contului.
- `mail.message` (extins): câmpul `terrabit_remote_id`, folosit la deduplicarea mesajelor oglindite.
- `discuss.channel` (extins): canalul de chat al suportului Terrabit.

**Vizualizări**

- `view_terrabit_helpdesk_ticket_list`, `view_terrabit_helpdesk_ticket_kanban`: listele de tichete, cu panou de sincronizare.
- `view_terrabit_helpdesk_ticket_form`: formularul tichetului, cu zona de fișiere și chatter.
- `view_terrabit_helpdesk_ticket_search`: filtre și grupări.
- `iap_account_view_form_terrabit_helpdesk`, `iap_account_view_form_terrabit_support_chat`: setările contului IAP, inclusiv activarea chatului.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_register_terrabit_helpdesk`: reia înregistrarea contului IAP pe serverul Terrabit.
- `ir_cron_sync_terrabit_helpdesk_tickets`: sincronizează tichetele și mesajele (trimite coada locală, aduce noutățile).
- `ir_cron_remind_awaiting_reply`: avertizează tichetele care așteaptă răspunsul clientului de peste 24 de ore.
- `ir_actions_server_sync_terrabit_helpdesk_tickets`: **Sync Now**, sincronizare la cerere.
- `ir_actions_server_open_terrabit_chat`: deschide canalul de chat al suportului.

#### 5. Conexiuni

- [terrabit_iap_server_helpdesk](../terrabit_iap_server_helpdesk/index.md): partea de server, instalată pe helpdesk-ul Terrabit, care primește tichetele și întoarce starea, consultantul și mesajele publice.
- [terrabit_iap](../terrabit_iap/index.md): furnizează contul IAP și înregistrarea automată pe serverul Terrabit.
