# Romania - Terrabit Connect (punte cloud) (localizat la `l10n_ro_anaf_agent/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_agent`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_agent
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_agent`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Stratul ANAF peste **Terrabit Connect** ([deltatech_tc](../deltatech_tc/index.md)), fundația comună de comunicare cloud↔stație pentru integrările Terrabit. Când Odoo rulează în cloud, nu poate ajunge la stația contabilului, unde se află tokenul cu certificat calificat necesar autentificării la SPV. De aceea **stația inițiază toate conexiunile** outbound către Odoo, autentificându-se cu o cheie API; Odoo nu se conectează niciodată la stație. Modulul adaugă peste registrul de stații și coada de joburi specificul ANAF.

#### 2. Funcționalități Cheie

- `cert_subject` pe `deltatech.tc.station` — subiectul certificatului calificat de pe token, raportat la heartbeat.
- Tipurile de job ANAF pe `deltatech.tc.job`: `sync_messages` / `download` / `submit`; prelucrarea rezultatelor se face prin hook-ul `_process_result`, suprascris în `l10n_ro_anaf_messages` (mesaje SPV) și `l10n_ro_anaf_submission` (depuneri).
- Meniuri sub *Contabilitate → Configurare*: **Stație ANAF** (registrul stațiilor, cu *Last Seen* și subiectul certificatului) și **Joburi TC** (coada de joburi: În așteptare → Preluat → Finalizat/Eroare); vizibile doar managerilor contabili.
- Pe fișa stației: cheia API (mascată), butonul-statistică **Joburi** și acțiunile **Cere sincronizare mesaje** (ultimele 30 de zile), **Regenerează cheia**, **Descarcă config** (fișierul `agent.conf` pre-completat) și **Ping**.
- `POST /anaf_agent/messages` — push direct de mesaje SPV (sincronizare periodică, fără job); autentificare prin antetul `X-Station-Key` (legacy `X-Agent-Key`).
- Heartbeat, poll, result și config sunt servite de endpoint-urile generice `/tc/*` din `deltatech_tc`.
- Înrolarea stației (pași detaliați) este în fișa consultant.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [deltatech_tc](../deltatech_tc/index.md)

#### 4. Componente Cheie

Conform prioritizării Readme, analiza codului pentru această secțiune a fost omisă (există `readme/DESCRIPTION.md`, iar acesta nu solicită explicit detalierea componentelor tehnice). Modelele extinse sunt `deltatech.tc.station` și `deltatech.tc.job`, iar endpointul propriu este `/anaf_agent/messages`.

#### 5. Conexiuni

- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md): folosește joburile `sync_messages` create de acest modul pentru a sincroniza și prelucra mesajele SPV.
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): folosește joburile `submit` create de acest modul pentru a depune declarații la SPV.
