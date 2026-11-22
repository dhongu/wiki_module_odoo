# Romania - Mesaje SPV ANAF (generale) (localizat la `l10n_ro_anaf_messages/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_messages`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_messages
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_messages`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul citește mesajele generale din Spațiul Privat Virtual (SPV) al ANAF — notificări și recipisele declarațiilor fiscale — separat de mesajele e-Factura (care rămân în modulul `l10n_ro_message_spv`). Folosește serviciul SPVWS2 al ANAF (`listaMesaje`, `descarcare`), care **nu este accesibil prin OAuth2 Bearer**: gateway-ul ANAF cere autentificare cu certificat client (mTLS), iar cheia privată stă pe tokenul fizic. De aceea apelul nu se face direct din Odoo, ci prin **Terrabit Connect** (Java + PKCS#11), care ține certificatul și proxează mTLS la ANAF. Sunt suportate două topologii: on-prem, unde Odoo apelează agentul local pe `localhost` (`URL Agent Terrabit`, implicit `http://127.0.0.1:8765`), autentificat cu un secret partajat (`X-Agent-Token`); și cloud, unde agentul rulează lângă tokenul fizic și împinge rezultatele înapoi în Odoo (push pe controller / jobul `sync_messages` din `l10n_ro_anaf_agent`), punctul unic de ingestie fiind același. Recipisele declarațiilor sosesc tot ca mesaje SPV, iar acest modul oferă canalul de preluare a lor, complementar modulului de depunere `l10n_ro_anaf_submission`.

#### 2. Funcționalități Cheie

- **Lista de mesaje** (**Contabilitate → Raportare → Declarații ANAF → Mesaje ANAF**): fiecare rând este un mesaj SPV, cu ID, CIF, tip, dată, detalii, ID solicitare (**Request ID**, prin care recipisa se corelează cu depunerea) și starea descărcării (Nedescărcat / Descărcat / Eroare).
- **Clasificare automată** a tipului: Recipisă, Decizie, Somație, Declarație, Notificare, Eroare, Altele; tipul brut primit de la ANAF se păstrează alături.
- **Sincronizare din browser**: butonul **Sincronizează SPV** din antetul listei cere agentului lista mesajelor din ultimele zile și creează doar mesajele noi (fără duplicate, poate fi rulat oricând).
- **Descărcarea documentului (PDF)** cu **Descarcă document** (formular) sau **Descarcă** (rând din listă), inițiată din browser — agentul rulează pe stația contabilului, deci funcționează și pe Odoo.sh. Documentul se atașează, starea devine Descărcat, iar **Deschide PDF** îl deschide; la eroare ANAF starea devine Eroare, cu textul erorii în formular.
- **Alerte de risc**: pentru mesajele de tip eroare se ridică o activitate „de verificat” către un manager de contabilitate al companiei, o singură dată per mesaj (cron implicit dezactivat).
- **Parametri pe companie** (**Setări → Contabilitate**, blocul **Mesaje SPV ANAF (Agent Terrabit)**): URL agent, token agent și numărul de zile interogate (1–60). Compania trebuie să aibă un CUI valid, înrolat în SPV, iar Terrabit Connect trebuie să fie pornit lângă tokenul fizic.
- Descărcarea automată server-side prin cron nu funcționează în modelul cloud: serverul Odoo nu poate ajunge la agentul de pe stația de lucru, deci sincronizarea și descărcarea se fac din browser.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.message`: mesajul SPV (cu `mail.thread.main.attachment` și `mail.activity.mixin`); câmpuri `message_type`, `tip_raw`, `request_id`, `state`, `error`, `attachment_id`, `risk_activity_done`; metode de sincronizare, descărcare și ingestie (`action_sync_spv`, `action_download`, `ingest_from_browser`, `store_downloaded_document`).
- `res.company` / `res.config.settings` (extinse): `l10n_ro_anaf_agent_url`, `l10n_ro_anaf_agent_token`, `l10n_ro_anaf_spv_days` și metodele de ingestie a mesajelor.
- `deltatech.tc.job` (extins): suprascrie `_process_result` pentru joburile `sync_messages` ale `l10n_ro_anaf_agent`, ingerând mesajele aduse de stație.
- `anaf_spv_client` (`make_spv_request`): clientul HTTP către agentul Terrabit Connect.

**Vizualizări**

- `view_l10n_ro_anaf_message_list` / `view_l10n_ro_anaf_message_form` / `view_l10n_ro_anaf_message_search`: lista, formularul și căutarea mesajelor SPV.
- `res_config_settings_view_form_anaf_messages`: blocul de setări al agentului.
- `menu_l10n_ro_anaf_message`: meniul **Mesaje ANAF**; regulă multi-companie `l10n_ro_anaf_message_comp_rule`; asset-urile OWL `spv_sync_action` pentru sincronizarea din browser.

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_anaf_message_sync` (acțiune server): sincronizarea mesajelor SPV, apelată din butonul **Sincronizează SPV**.
- `ir_cron_download_spv_messages` („ANAF SPV: download general messages”): zilnic, **dezactivat implicit**; metoda `_cron_download_spv_messages` doar loghează și nu descarcă nimic în modelul cloud.
- `ir_cron_anaf_risk_alerts` („ANAF SPV: risk alerts (error receipts)”): zilnic, **dezactivat implicit**; creează activități pentru mesajele de tip eroare.

#### 5. Conexiuni

- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md): furnizează transportul mTLS către ANAF (agent local pe `localhost` sau, în model cloud, jobul `sync_messages` al cărui rezultat este ingestat de acest modul).
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): modul de depunere a declarațiilor fiscale; recipisele declarațiilor depuse sosesc ca mesaje SPV preluate de acest modul, fiind complementare.
- `l10n_ro_message_spv`: gestionează mesajele SPV de tip e-Factura; acest modul tratează separat mesajele SPV generale (notificări și recipise de declarații).
