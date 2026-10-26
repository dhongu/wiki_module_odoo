# Romania - Depunere electronică a declarațiilor ANAF (FR-53) (localizat la `l10n_ro_anaf_submission/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_submission`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_submission
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_submission`
- **Ultima Ingestie:** `2026-10-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă infrastructura comună pentru depunerea electronică a declarațiilor fiscale ANAF generate în Odoo (D112, D300, D394, D406 etc.), conform cerinței FR-53. El nu generează declarațiile — acestea sunt produse de modulele dedicate (`l10n_ro_anaf_d112`, `l10n_ro_anaf_d300`, ...) — ci adaugă stratul de urmărire a depunerii și a recipisei. O înregistrare de depunere păstrează fișierul depus, amprenta SHA-256, ID-ul solicitării ANAF, starea, eventualele erori, recipisa și pista de audit (cine și când a depus), iar declarațiile rectificative păstrează legătura cu depunerea inițială.

#### 2. Funcționalități Cheie

- **Registrul depunerilor** — meniu **Contabilitate → Raportare → Declarații ANAF → Depuneri electronice**. Starea urmărește ciclul de viață: Ciornă, Depusă, În prelucrare, Acceptată (recipisă primită), Respinsă, Eroare. O depunere se creează manual sau din butonul „Create ANAF submission" din raportul declarației.
- **Depunere manuală (SPV / e-guvernare)** — fluxul disponibil azi, funcțional complet: contabilul depune fișierul în SPV cu certificatul calificat, introduce ID-ul solicitării în Odoo (fără el, depunerea manuală este refuzată) și apasă **Depune**; sistemul verifică starea și păstrează recipisa (butonul **Marchează acceptată** apare după atașarea recipisei).
- **Depunere prin Terrabit Agent (Terrabit Connect)** — conector complet implementat: **Depune** pune fișierul într-o coadă de job-uri (`deltatech.tc.job`); agentul local Terrabit, cu certificatul calificat pe stația contabilului, îl semnează și îl urcă direct la ANAF (SPVWS2), iar ID-ul solicitării, starea și recipisa se sincronizează înapoi în Odoo.
- **Depunere certSIGN Cloud (API)** — conector de semnare PAdES + upload automat direct; interfața și configurarea există, însă conectorul propriu-zis este un *stub* care necesită API-ul comercial certSIGN și se activează când acesta devine disponibil.
- **Verificarea stării** — butonul **Verifică stare** interoghează endpoint-ul public ANAF de stare prin ID solicitare (nu necesită certificat); un cron dezactivat implicit (la 6 ore) verifică automat depunerile aflate în lucru.
- **Urmărirea depunerii și a recipisei** — păstrarea fișierului depus, a amprentei SHA-256 (calculată automat), a ID-ului solicitării ANAF, a stării, a erorilor și a recipisei.
- **Pistă de audit** — înregistrarea utilizatorului (**Depus de**) și a momentului depunerii (**Data depunerii**), plus mesajele din chatter.
- **Declarații rectificative** — butonul **Creează rectificativă** generează o depunere legată de original; butonul inteligent **Rectificative** numără corecțiile.
- **Configurare** — în **Setări → Contabilitate**, blocul „Depunere electronică declarații ANAF": metoda de depunere implicită (Manual, Agent Terrabit sau certSIGN Cloud) și URL-ul de stare ANAF (precompletat).
- Dacă este instalat modulul complementar `l10n_ro_anaf_duk`, fiecare depunere are în plus butonul **Validare DUK** și un status unificat.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_agent](../l10n_ro_anaf_agent/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.submission`: înregistrarea depunerii (cu `mail.thread` și `mail.activity.mixin`), cu acțiunile de depunere, verificare a stării, marcare acceptată, resetare la ciornă și creare/listare a rectificativelor.
- `l10n_ro_anaf.report.handler.mixin` (extins): adaugă `l10n_ro_anaf_create_submission`, folosită de butonul „Create ANAF submission" din rapoartele declarațiilor.
- `deltatech.tc.job` (extins, `models/l10n_ro_anaf_agent_job.py`): legătura cu coada de job-uri a agentului Terrabit.
- `res.company` și `res.config.settings` (extinse): metoda de depunere implicită și URL-ul de stare.

**Vizualizări**

- `views/l10n_ro_anaf_submission_views.xml`: lista și formularul depunerilor electronice.
- `views/res_config_settings_views.xml` (`res_config_settings_view_form_submission`): blocul de setări pentru depunerea electronică.
- `views/menus.xml`: meniul Depuneri electronice.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_poll_anaf_submission` („ANAF: check status of pending submissions"): rulează `_cron_poll_pending()` la 6 ore pentru depunerile aflate în lucru; instalat dezactivat.

#### 5. Conexiuni

- [l10n_ro_anaf_d112](../l10n_ro_anaf_d112/index.md): modul dedicat care generează declarația D112 depusă prin acest strat de infrastructură.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): modul dedicat care generează declarația D300 depusă prin acest strat de infrastructură.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): declarația D394, depusă prin același strat.
- `l10n_ro_anaf_duk`: modul complementar care adaugă validarea DUK pe depuneri.
