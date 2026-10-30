# AI - Conversation Summary for Project

- **Nume Tehnic:** `deltatech_ai_thread_summary_project`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_thread_summary_project
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_thread_summary_project`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Extinde modulul [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md) la proiecte și sarcini: în partea de sus a chatter-ului fiecărui proiect și fiecărei sarcini apare panoul **AI Summary**, cu sumarul conversației generat de agentul AI. Sumarul proiectului strânge și sumarele sarcinilor sale, astfel încât imaginea de ansamblu se vede fără a citi fiecare sarcină în parte.

#### 2. Funcționalități Cheie

- **Sarcină:** sumarul mesajelor sarcinii, îmbogățit cu proiectul, responsabilii, starea, termenul limită și etichetele.
- **Proiect:** sumarul mesajelor proiectului **și** ale sarcinilor sale. Modelul primește sumarele (status și pașii următori) ale sarcinilor actualizate de la ultimul sumar al proiectului (cel mult 30, cele mai recente primele), numărul de sarcini deschise, datele planificate și statusul ultimei actualizări de proiect.
- Când sumarul unei sarcini se schimbă, sumarul proiectului ei este marcat ca depășit; actualizarea automată rezumă întâi sarcinile, apoi proiectele.
- **Utilizare:** panoul **AI Summary** se deschide din chatter; butonul **Update Summary** apelează modelul (deschiderea documentului doar citește sumarul stocat), iar când apar mesaje noi panoul afișează *New messages since the last summary*. Un eșec al actualizării automate este afișat în panou și reîncercat la următorul mesaj.
- Butonul **Rebuild** rescrie sumarul din toate mesajele (de ex. după schimbarea instrucțiunilor sau a modelului agentului); la proiect citește toate sarcinile sumarizate (cele mai recente 30), nu doar pe cele schimbate.
- Panoul este vizibil utilizatorilor interni (`base.group_user`).
- Modulul are `auto_install`: se instalează singur când sunt prezente `project` și modulul de bază. Stadiu de dezvoltare: Beta.

#### 3. Dependențe

- `project`
- [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md)

#### 4. Componente Cheie

**Modele**

- `project.task` (extins): adaugă mixin-ul `ai.thread.summary.mixin`; completează informațiile trimise modelului (proiect, responsabili, stare, termen, etichete); după fiecare actualizare marchează proiectul ca având sumar în așteptare.
- `project.project` (extins): adaugă același mixin cu `_ai_summary_sequence = 20` (după sarcini); adaugă în context datele planificate, statusul ultimei actualizări, numărul de sarcini și sumarele sarcinilor schimbate; schimbarea sumarelor sarcinilor declanșează actualizarea proiectului.

**Vizualizări**

- Fără vizualizări XML proprii: panoul apare în chatter prin `chatter.quick.info`.

**Acțiuni Automate / Acțiuni Server**

- `chatter_quick_info_project_task_ai_summary` și `chatter_quick_info_project_project_ai_summary` (`data/chatter_quick_info_data.xml`, `noupdate`): înregistrează panoul „AI Summary" (secvența 5, metoda `_chatter_quick_info_ai_summary`) pe sarcini și proiecte. Nu există cron propriu; folosește actualizarea automată a modulului de bază.

#### 5. Conexiuni

- [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md): modulul de bază care furnizează mixin-ul, agentul și actualizarea automată.
- [deltatech_ai_thread_summary_crm](../deltatech_ai_thread_summary_crm/index.md): aceeași extensie pentru piste CRM.
- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md): mecanismul de panouri din chatter în care apare sumarul (dependență a modulului de bază).
