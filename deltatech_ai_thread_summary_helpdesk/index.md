# AI - Conversation Summary for Helpdesk (localizat la `deltatech_ai_thread_summary_helpdesk/index.md`)

- **Nume Tehnic:** `deltatech_ai_thread_summary_helpdesk`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_thread_summary_helpdesk
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_thread_summary_helpdesk`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Adaugă rezumatul AI al conversației la tichetele de suport (Helpdesk), într-un panou „AI Summary” în partea de sus a chatterului. Pe lângă emailuri, mesaje și note, modelul primește clientul, echipa, utilizatorul alocat, etapa, prioritatea, etichetele și termenul SLA. Colegul care preia tichetul vede imediat ce a raportat clientul, ce s-a încercat și ce se așteaptă în continuare.

#### 2. Funcționalități Cheie

- Panou „AI Summary” în chatterul tichetului, vizibil pentru toți utilizatorii interni, afișat în capul chatterului (secvența 5).
- Rezumatul conține statusul, contextul, deciziile, întrebările deschise și pașii următori, cu data rezumatului.
- Contextul trimis modelului include: tichetul (referința), echipa, prioritatea, etichetele și termenul SLA, în plus față de client, utilizatorul alocat și etapă (furnizate de modulul de bază).
- Deschiderea tichetului doar citește rezumatul stocat; doar butoanele apelează modelul.
- Butonul **Update Summary** actualizează rezumatul; când sosesc mesaje noi, panoul afișează „New messages since the last summary”. Actualizarea automată este posibilă, iar o actualizare automată eșuată este afișată în panou și reîncercată la următorul mesaj.
- Butonul **Rebuild** rescrie rezumatul din toate mesajele (de exemplu după schimbarea instrucțiunilor sau a modelului agentului).
- Se instalează automat (`auto_install`) când sunt prezente `helpdesk` și modulul de bază.

#### 3. Dependențe

- `helpdesk`
- [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md)

#### 4. Componente Cheie

**Modele**

- `helpdesk.ticket` (extins): moștenește `ai.thread.summary.mixin` și suprascrie `_ai_summary_record_info`, adăugând în contextul trimis modelului tichetul, echipa, prioritatea, etichetele și termenul SLA.

**Vizualizări**

- Modulul nu definește vizualizări; panoul din chatter vine din modulul de bază, prin înregistrarea de mai jos.

**Acțiuni Automate / Acțiuni Server**

- `chatter_quick_info_helpdesk_ticket_ai_summary` (`chatter.quick.info`, `noupdate`): înregistrează panoul „AI Summary” pe `helpdesk.ticket`, metoda `_chatter_quick_info_ai_summary`, grup `base.group_user`. Nu există cron-uri sau acțiuni server proprii.

#### 5. Conexiuni

- [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md): modulul de bază care oferă mixinul, panoul și butoanele de actualizare.
- [deltatech_ai_thread_summary_crm](../deltatech_ai_thread_summary_crm/index.md): extensia soră pentru piste/oportunități, construită pe același mixin.
