# AI - Conversation Summary (Rezumatul AI al conversației)

- **Nume Tehnic:** `deltatech_ai_thread_summary`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_ai_thread_summary
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_ai_thread_summary`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un agent AI din Odoo 19 Enterprise ține la zi un **rezumat al conversației** unei înregistrări (e-mailurile, mesajele și notele interne din chatter), astfel încât un coleg care preia o oportunitate, un tichet sau un proiect să afle unde s-a ajuns fără să citească tot istoricul. Modulul conține motorul; punțile pentru CRM, Helpdesk și Proiect adaugă rezumatul pe înregistrările aplicațiilor respective. Mesajele sunt trimise furnizorului modelului de limbaj al agentului ales.

#### 2. Funcționalități Cheie

- **Rezumat structurat**: stare, context (ce vrea clientul, produse, cantități, sume, date), decizii, întrebări deschise și pași următori (cine și până când). Se scrie în limba companiei înregistrării și apare într-un panou *Rezumat AI* în capul chatterului.
- **Actualizare incrementală**: modelul primește rezumatul curent și doar mesajele de după el, deci costul nu crește la fiecare actualizare; un istoric foarte lung se rezumă în mai mulți pași la prima rulare.
- **Text curățat**: citatele și semnăturile e-mailurilor sunt omise, un mesaj lung își păstrează începutul, atașamentele apar doar prin nume, iar schimbările de etapă sau de responsabil devin o linie. Notele interne sunt marcate, ca modelul să știe că clientul nu le-a văzut.
- **Manual sau automat**: butonul *Actualizează rezumatul* adaugă mesajele noi, *Refă* rescrie rezumatul din tot istoricul. Cu actualizarea automată (opțională, în setări), rezumatul urmează un mesaj nou după câteva minute (mesajele dintr-o rafală se grupează); o actualizare eșuată afișează eroarea și se reîncearcă la următorul mesaj.
- **Modelul și regulile companiei**: se folosește modelul și promptul de sistem ale unui agent AI ales în *Setări > AI*, blocul *Rezumatele conversațiilor* (implicit agentul *Conversation Summary*, creat de modul; un model mic, de tip GPT-4.1 Mini, ajunge). Din agent contează doar modelul și promptul de sistem. Cheia furnizorului se pune în *Setări > AI* (pentru Claude, cu `deltatech_ai_anthropic`).
- **Doar intern**: rezumatul este vizibil exclusiv utilizatorilor interni.
- Punțile `deltatech_ai_thread_summary_crm`, `_helpdesk` și `_project` se instalează automat odată cu aplicația corespunzătoare; pe proiect, rezumatul include și rezumatele sarcinilor.

Fluxul pas-cu-pas, aspectele GDPR (ce date pleacă la furnizor) și capturile sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `mail`
- `ai_app` (Odoo Enterprise)
- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md)

#### 4. Componente Cheie

**Modele**

- `ai.thread.summary.mixin` (abstract, moștenește `mail.thread`): câmpurile `ai_summary`, `ai_summary_data`, `ai_summary_message_id`, `ai_summary_date`, `ai_summary_pending`, `ai_summary_error`; logica de colectare a mesajelor, împărțire în bucăți, interogare a modelului și randare. Modelele de aplicație o moștenesc prin punți.
- `res.config.settings` (extins): `ai_summary_agent_id` (agentul rezumatelor) și `ai_summary_auto_update` (actualizare automată).
- `ai.agent` (date): agentul *Conversation Summary*, ales implicit prin parametrul `deltatech_ai_thread_summary.agent_id`.

**Vizualizări**

- `res_config_settings_view_form`: blocul *Rezumatele conversațiilor* în *Setări > AI*.
- `ai_thread_summary_content` (template QWeb): conținutul panoului *Rezumat AI* din chatter (rezumat, dată, etichete de stare, butoanele *Actualizează rezumatul* și *Refă*).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ai_thread_summary` (*AI: update the conversation summaries*): rulează orar `_cron_ai_summary_update()`; actualizează rezumatele marcate ca în așteptare (la ~10 minute după un mesaj nou), doar cu actualizarea automată pornită.

#### 5. Conexiuni

- [deltatech_ai_thread_summary_crm](../deltatech_ai_thread_summary_crm/index.md): puntea pentru lead-uri și oportunități.
- [deltatech_ai_thread_summary_helpdesk](../deltatech_ai_thread_summary_helpdesk/index.md): puntea pentru tichete.
- [deltatech_ai_thread_summary_project](../deltatech_ai_thread_summary_project/index.md): puntea pentru proiecte și sarcini.
- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md): afișează panoul rezumatului în capul chatterului.
- `deltatech_ai_anthropic`: permite folosirea modelelor Claude pentru rezumate.
