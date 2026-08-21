# Romania - Terrabit Connect (punte cloud) (localizat la `l10n_ro_anaf_agent/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_agent`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_agent
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_agent`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este stratul ANAF peste **Terrabit Connect** (`deltatech_tc`), fundația comună de comunicare cloud↔stație pentru toate integrările Terrabit. Când Odoo rulează în cloud, nu poate ajunge la stația contabilului, unde se află tokenul cu certificat calificat necesar autentificării la SPV. De aceea **stația inițiază toate conexiunile** outbound către Odoo, autentificându-se cu o cheie API; Odoo nu se conectează niciodată la stație. Modulul adaugă peste registrul generic de stații și coada de joburi din `deltatech_tc` specificul ANAF: subiectul certificatului digital, tipurile de job pentru sincronizare/descărcare/depunere și acțiunile de înrolare din meniul Contabilitate → ANAF.

#### 2. Funcționalități Cheie

- `cert_subject` pe `deltatech.tc.station` — subiectul certificatului calificat de pe token, raportat la fiecare heartbeat.
- Tipurile de job ANAF adăugate pe `deltatech.tc.job`: `sync_messages` / `download` / `submit`; prelucrarea rezultatelor per tip este delegată prin hook-ul `_process_result`, suprascris în `l10n_ro_anaf_messages` (mesaje SPV) și `l10n_ro_anaf_submission` (depuneri).
- Acțiuni de înrolare: „Cere sincronizare mesaje" pe fișa stației plus meniul „Terrabit Connect" sub Contabilitate → ANAF (aceleași stații și joburi ca în Setări → Terrabit Connect).
- `POST /anaf_agent/messages` — endpoint dedicat de push direct de mesaje SPV (sincronizare periodică, fără trecere prin coada de joburi); autentificare pe antetul `X-Station-Key` (cu fallback legacy pe `X-Agent-Key`).
- Heartbeat, poll, result și config sunt servite de endpoint-urile generice `/tc/*` din `deltatech_tc` — acest modul nu le mai duplică.

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [deltatech_tc](../deltatech_tc/index.md)

#### 4. Componente Cheie

Conform prioritizării Readme, analiza codului pentru această secțiune a fost omisă (există `readme/DESCRIPTION.md`, iar acesta nu solicită explicit detalierea componentelor tehnice).

#### 5. Conexiuni

- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md): folosește joburile `sync_messages` create de acest modul pentru a sincroniza și prelucra mesajele SPV.
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): folosește joburile `submit` create de acest modul pentru a depune declarații la SPV.
