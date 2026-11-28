# Helpdesk AI Reply (localizat la `terrabit_helpdesk_ai_reply/index.md`)

- **Nume Tehnic:** `terrabit_helpdesk_ai_reply`
- **Versiune:** `20.0.1.20.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_helpdesk_ai_reply
- **Cale Locală:** `odoo-addons/terrabit/terrabit_helpdesk_ai_reply`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Dispecer AI pentru partea de către client a ciclului de viață al unui tichet de helpdesk, construit pe un singur agent `ai.agent` (Tibi) și pe furnizorul LLM deja configurat în Odoo. Agentul nu încearcă soluții tehnice, care rămân în sarcina consultanților: confirmă primirea tichetului, trimite mementouri, scade prioritatea tichetelor rămase fără răspuns și închide tichetul când clientul confirmă rezolvarea.

#### 2. Funcționalități Cheie

- **Tichet nou**: răspuns de preluare care confirmă primirea, rezumă cererea, cere date lipsă (pași de reproducere, eroare, capturi) și anunță preluarea de către un consultant. Instalarea șterge șablonul standard de confirmare de pe etapele care îl folosesc, ca să nu primească clientul două emailuri.
- **Așteptăm clientul**: memento după `ai_reminder_day` zile de tăcere (repetat), iar tichetele cu prioritate High rămase fără răspuns `ai_priority_downgrade_day` zile coboară la Medium, cu notă internă. Etapa se marchează cu „Așteptăm clientul”.
- **Răspuns de la client**: nimic imediat și fără schimbare de etapă; dacă echipa nu reacționează în `ai_intervene_after_hours` ore (implicit 24, măsurat de la ultima activitate reală), AI-ul clasifică răspunsul: închide tichetul la confirmarea rezolvării (cu notă internă) sau trimite o confirmare scurtă de primire, fără conținut tehnic.
- Limită de mesaje AI consecutive (`ai_max_consecutive_messages`, implicit 3), după care agentul tace până intervine un om; `0` înseamnă fără limită.
- Prag pe echipă setat în Setări; `0` dezactivează funcția respectivă.
- Închiderea tichetelor tăcute folosește mecanismul nativ „Close inactive tickets automatically” (cronul nativ trebuie activat o dată).
- Necesită un furnizor LLM configurat (cheie proprie sau conector IAP). Se pot adăuga surse (RAG) agentului pentru ancorarea răspunsurilor, opțional cu restricție la surse.
- Primul răspuns se poate restrânge la o echipă prin `filter_domain` al automatizării `automation_ai_reply`.
- Suprascrie mutarea automată în „în lucru” din `deltatech_helpdesk`: Tibi nu schimbă niciodată etapa unui tichet deschis.
- Nu are fișă de consultant.

#### 3. Dependențe

- `helpdesk`
- `ai`
- `base_automation`
- `deltatech_helpdesk`

#### 4. Componente Cheie

**Modele**

- `helpdesk.team` (extins): pragurile `ai_reminder_day`, `ai_priority_downgrade_day`, `ai_intervene_after_hours`, `ai_max_consecutive_messages`.
- `helpdesk.stage` (extins): `is_customer_waiting` („Așteptăm clientul”).
- `helpdesk.ticket` (extins): `ai_mute` și logica de răspuns, mementouri, clasificare și închidere.

**Vizualizări**

- `helpdesk_team_views`, `helpdesk_stage_views`, `helpdesk_ticket_views`: câmpurile AI pe echipă, etapă și tichet.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_send_reminders`: memento AI pe tichete fără răspuns de la client (zilnic).
- `ir_cron_ai_downgrade_priority`: retrogradarea priorității tichetelor fără răspuns.
- `ir_cron_ai_intervene_on_pending_replies`: intervenția AI pe răspunsuri rămase fără reacție.
- `automation_ai_reply` (`base.automation`) și `action_ai_reply` (`ir.actions.server`): primul răspuns la tichet nou.
- `ai_agent_support`: agentul „Tibi”.
- `post_init_hook`: elimină șablonul standard de confirmare de pe etape.

#### 5. Conexiuni

- `deltatech_helpdesk`: modul intern Terrabit al cărui hook de mutare a etapei este suprascris.
- [terrabit_iap](../terrabit_iap/index.md): prin `terrabit_iap_ai`, apelurile AI pot fi direcționate prin serverul IAP Terrabit.
