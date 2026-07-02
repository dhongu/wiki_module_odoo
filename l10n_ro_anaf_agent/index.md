# Romania - Agent ANAF (punte cloud) (localizat la `l10n_ro_anaf_agent/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_agent`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_agent
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_agent`
- **Ultima Ingestie:** `2026-06-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul reprezintă fundația pentru modelul **cloud** de comunicare cu ANAF: oferă un registru de agenți locali, o coadă de joburi și un API pe care **Agentul Terrabit** îl apelează. Când Odoo rulează în cloud, nu poate ajunge la stația de lucru a contabilului (unde se află tokenul cu certificat digital). De aceea **agentul inițiază toate conexiunile** outbound către Odoo, autentificându-se cu o cheie API, iar Odoo nu se conectează niciodată direct la agent. Este un modul de infrastructură pe care se sprijină celelalte module de comunicare cu ANAF.

#### 2. Funcționalități Cheie

- Registru de agenți locali înregistrați (`l10n.ro.anaf.agent`): companie, cheie API, ultima vizualizare (`last_seen`) și subiectul certificatului digital.
- Coadă de joburi (`l10n.ro.anaf.agent.job`) cu tipurile `sync_messages` / `download` / `submit` și stările `pending → claimed → done/error`, cu hook `_process_result` extins de modulele consumatoare (mesaje, depunere).
- Controllere apelate de agent, cu autentificare pe antetul `X-Agent-Key`:
  - `POST /anaf_agent/poll` — preia joburile în stare pending.
  - `POST /anaf_agent/result` — întoarce rezultatul unui job.
  - `POST /anaf_agent/messages` — push direct de mesaje SPV (sincronizare periodică).
  - `POST /anaf_agent/heartbeat` — semnal de viață plus subiectul certificatului.
- Model cloud sigur în care agentul inițiază conexiunile (mTLS la ANAF din stația locală), eliminând nevoia ca tokenul cu certificat să fie disponibil în cloud.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

Conform prioritizării Readme, analiza codului pentru această secțiune a fost omisă (există `readme/DESCRIPTION.md`, iar acesta nu solicită explicit detalierea componentelor tehnice).

#### 5. Conexiuni

- `l10n_ro_anaf_messages`: depinde de acest modul pentru a crea joburi de sincronizare a mesajelor SPV și a prelucra rezultatele.
- `l10n_ro_anaf_submission`: depinde de acest modul pentru a crea joburi de depunere și a prelucra rezultatele.
