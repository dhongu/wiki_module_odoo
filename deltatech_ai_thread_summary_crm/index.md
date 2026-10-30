# AI - Conversation Summary for CRM (localizat la `deltatech_ai_thread_summary_crm/index.md`)

- **Nume Tehnic:** `deltatech_ai_thread_summary_crm`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_thread_summary_crm
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_thread_summary_crm`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Modulul aduce rezumatul AI al conversației, oferit de [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md), și pe lead-urile și oportunitățile din CRM. Rezumatul apare într-un panou „AI Summary” în partea de sus a chatterului, lângă conversația pe care o rezumă. Astfel, un coleg care preia o oportunitate vede rapid unde se află discuția și ce are de făcut mai departe, fără să citească tot istoricul de mesaje.

#### 2. Funcționalități Cheie

- Panou **AI Summary** în chatterul lead-urilor și oportunităților, vizibil pentru toți utilizatorii interni (grupul `base.group_user`), pe prima poziție din chatter (secvența 5).
- Pe lângă emailuri, mesaje și note, modelul AI primește și contextul comercial al oportunității: clientul, vânzătorul, etapa, venitul așteptat, probabilitatea, data estimată de închidere, etichetele și motivul pierderii. Rezumatul spune astfel unde se află oportunitatea și ce trebuie făcut pentru a fi câștigată.
- Contextul distinge tipul înregistrării (lead sau oportunitate); probabilitatea se transmite doar pentru oportunități, iar motivul pierderii doar pentru înregistrările arhivate (pierdute).
- Operare (preluată din baza comună, vezi [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md)):
  - **Update Summary** actualizează rezumatul (status, context, decizii, întrebări deschise, pași următori, cu data rezumatului); la deschiderea documentului se citește doar rezumatul stocat, doar butoanele apelează modelul.
  - Panoul semnalează „New messages since the last summary” când au apărut mesaje noi; actualizarea poate fi și automată, iar o actualizare automată eșuată se afișează în panou și se reîncearcă la următorul mesaj.
  - **Rebuild** rescrie rezumatul din toate mesajele, util după schimbarea instrucțiunilor sau a modelului agentului.
- Se instalează automat (`auto_install`) când sunt prezente `crm` și modulul de bază.

#### 3. Dependențe

- `crm`
- [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md)

#### 4. Componente Cheie

**Modele**

- `crm.lead`: extins cu mixin-ul `ai.thread.summary.mixin`; suprascrie `_ai_summary_record_info` pentru a adăuga tipul, venitul așteptat, probabilitatea, data estimată de închidere, etichetele și motivul pierderii în contextul trimis modelului AI.

**Vizualizări**

- Modulul nu definește vizualizări proprii; panoul apare în chatter prin înregistrarea `chatter.quick.info` de mai jos.

**Acțiuni Automate / Acțiuni Server**

- `chatter_quick_info_crm_lead_ai_summary` (`chatter.quick.info`, date `noupdate`): înregistrează panoul „AI Summary” pe `crm.lead`, apelând metoda `_chatter_quick_info_ai_summary`. Nu există cron-uri sau acțiuni server proprii.

#### 5. Conexiuni

- [deltatech_ai_thread_summary](../deltatech_ai_thread_summary/index.md): modulul de bază care oferă mixin-ul, panoul și apelurile către modelul AI; același rezumat este disponibil și pe alte documente (tichete, proiecte, sarcini) prin module similare.
