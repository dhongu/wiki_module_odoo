# Terrabit Helpdesk AI Reply (localizat la `terrabit_helpdesk_ai_reply/index.md`)

- **Nume Tehnic:** `terrabit_helpdesk_ai_reply`
- **Versiune:** `19.0.1.18.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_helpdesk_ai_reply
- **Cale Locală:** `odoo-addons/terrabit/terrabit_helpdesk_ai_reply`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă un agent AI (Tibi) care se ocupă de partea dinspre client a ciclului de viață al unui tichet de helpdesk: confirmă primirea tichetului, trimite mementouri când clientul nu răspunde și închide tichetul când clientul confirmă rezolvarea. Agentul nu încearcă soluții tehnice — rezolvarea rămâne la consultanții umani; rolul lui este strict de dispecerat. Folosește motorul AI standard din Odoo 19 și furnizorul LLM deja configurat în baza de date, fără integrări externe proprii.

#### 2. Funcționalități Cheie

- **Primul răspuns la tichet nou:** confirmă primirea, rezumă ce a înțeles, cere datele de diagnostic lipsă (pași de reproducere, eroare/traceback, capturi) și anunță preluarea de către un consultant. Poate fi restrâns la o echipă prin `filter_domain` pe automatizarea `automation_ai_reply`.
- **Mementou la clientul care tace:** pe etapele marcate „Așteptăm clientul”, un cron zilnic trimite un mementou după `ai_reminder_day` zile de tăcere (repetat la același interval, până răspunde clientul).
- **Retrogradarea priorității:** tichetele cu prioritate mare, fără răspuns după `ai_priority_downgrade_day` zile, trec la prioritate medie, cu notă internă explicativă.
- **Fără schimbare automată de etapă la răspunsul clientului:** AI-ul nu răspunde imediat și nu mută tichetul; trecerea în lucru rămâne în sarcina utilizatorului intern (comportamentul din `deltatech_helpdesk` este suprimat).
- **Intervenție întârziată:** dacă nimeni din echipă nu reacționează în `ai_intervene_after_hours` ore (implicit 24) de la ultimul mesaj real, AI-ul clasifică răspunsul clientului: la confirmare de rezolvare postează mesajul de încheiere și **închide tichetul** (cu notă internă), altfel trimite o scurtă confirmare de primire, fără conținut tehnic și fără schimbare de etapă. Activitatea unui consultant (răspuns sau notă internă) resetează fereastra; tichetele din etapele de tip „Așteptăm clientul” sunt excluse.
- **Plafon de mesaje consecutive:** după `ai_max_consecutive_messages` (implicit 3) mesaje AI la rând, fără mesaj uman între ele, agentul tace până intervine un om.
- **Praguri per echipă:** setate în configurarea echipei de helpdesk; valoarea `0` dezactivează funcția respectivă pentru echipă.
- **Fără răspuns AI pe tichet:** bifa `ai_mute` oprește complet agentul pe tichet; se bifează automat la tichetele deschise de colegi din backend (notificări către client).
- **Înlocuirea confirmării standard:** la instalare, hook-ul scoate șablonul standard de confirmare din etapele care îl folosesc, ca să nu primească clientul două e-mailuri (la dezinstalare nu se restaurează).
- **Închiderea tichetelor fără activitate:** se reutilizează mecanismul nativ Odoo (închidere automată a tichetelor inactive); se configurează `auto_close_day` mai mare decât pragul de retrogradare și se activează o dată cronul nativ.
- **Ancorare în documentație (RAG):** se pot adăuga Surse pe agentul Tibi (articole Knowledge, documentație, tichete rezolvate) pentru răspunsuri mai fundamentate.
- **Cerință:** un furnizor LLM configurat în Setări / AI (cheie proprie OpenAI/Google sau conector IAP); fără el agentul raportează „No API key set”.

#### 3. Dependențe

- `helpdesk`
- `ai`
- `base_automation`
- `deltatech_helpdesk`

#### 4. Componente Cheie

**Modele**

- `helpdesk.ticket` (extins): câmpul `ai_mute` și metodele AI (compunere și postare mesaj agent, clasificare răspuns client, retrogradare prioritate, număr de mesaje AI consecutive); suprimă mutarea automată în etapa „în lucru” la mesajul clientului.
- `helpdesk.team` (extins): pragurile `ai_reminder_day`, `ai_priority_downgrade_day`, `ai_intervene_after_hours`, `ai_max_consecutive_messages` și metodele apelate de cron.
- `helpdesk.stage` (extins): bifa `is_customer_waiting` („Așteptăm clientul”).

**Vizualizări**

- `helpdesk_stage_view_form_inherit_ai_reply`: bifa „Așteptăm clientul” pe etapă.
- `helpdesk_team_view_form_inherit_ai_reply`: pragurile AI în configurarea echipei.
- `helpdesk_ticket_view_form_ai_mute`: câmpul `ai_mute` pe formularul tichetului, după echipă.

**Acțiuni Automate / Acțiuni Server**

- `automation_ai_reply` (`base.automation`, la creare tichet) cu `action_ai_reply`: generează și trimite primul răspuns prin agentul Tibi (`ai_agent_support`).
- `ir_cron_ai_send_reminders` (zilnic): mementouri pe tichetele care așteaptă clientul.
- `ir_cron_ai_downgrade_priority` (zilnic): retrogradarea priorității tichetelor fără răspuns.
- `ir_cron_ai_intervene_on_pending_replies` (orar): intervenția AI pe răspunsurile clientului rămase fără reacție.

#### 5. Conexiuni

- `helpdesk`: modulul de bază extins (tichete, etape, echipe); cronul nativ de închidere automată `helpdesk.ir_cron_auto_close_ticket` este reutilizat pentru tichetele tăcute.
- `deltatech_helpdesk`: modulul intern a cărui mutare automată în etapa „în lucru” este suprimată aici.
