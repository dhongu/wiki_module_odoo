# Romania - Terrabit Connect (punte cloud) (localizat la `l10n_ro_anaf_agent/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_agent`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_agent
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_agent`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este stratul ANAF peste **Terrabit Connect** (`deltatech_tc`), fundația comună de comunicare cloud↔stație pentru toate integrările Terrabit. Când Odoo rulează în cloud, nu poate ajunge la stația contabilului, unde se află tokenul cu certificat calificat necesar autentificării la SPV. De aceea **stația inițiază toate conexiunile** outbound către Odoo, autentificându-se cu o cheie API; Odoo nu se conectează niciodată la stație. Modulul adaugă peste registrul generic de stații și coada de joburi din `deltatech_tc` specificul ANAF: subiectul certificatului digital, tipurile de job pentru sincronizare/descărcare/depunere și meniurile de administrare din Contabilitate → Configurare.

#### 2. Funcționalități Cheie

- **Înrolarea stației** (**Contabilitate → Configurare → Stație ANAF**): se creează o înregistrare cu nume și companie, iar cheia API se generează automat. Butonul **Descarcă config** oferă fișierul `agent.conf`, pre-completat cu adresa instanței și cheia API, care se pune în dosarul de configurare al aplicației Terrabit Connect (`~/.terrabit-anaf-agent/`) sau se importă din setările ei. La pornire aplicația trimite un heartbeat, iar în Odoo se completează **Last Seen** și subiectul certificatului.
- **Fișa stației**: cheia API (mascată, vizibilă doar administratorilor de sistem), `cert_subject` (subiectul certificatului calificat de pe token, raportat la heartbeat), butonul-statistică **Joburi** și acțiunile **Cere sincronizare mesaje** (job de sincronizare SPV pe ultimele 30 de zile), **Regenerează cheia** (invalidează cheia veche; stația trebuie reconfigurată), **Descarcă config** și **Ping**. O stație sănătoasă are **Last Seen** recent (minute, nu zile).
- **Coada de joburi** (**Contabilitate → Configurare → Joburi TC** sau butonul **Joburi** de pe stație): tipurile ANAF `sync_messages` / `download` / `submit`; ciclul de viață este În așteptare → Preluat → Finalizat sau Eroare, cu rezultatul sau eroarea atașată. Prelucrarea rezultatelor este delegată prin hook-ul `_process_result`, suprascris în `l10n_ro_anaf_messages` (mesaje SPV) și `l10n_ro_anaf_submission` (depuneri).
- `POST /anaf_agent/messages` — endpoint dedicat de push direct de mesaje SPV (sincronizare periodică, fără trecere prin coada de joburi); autentificare pe antetul `X-Station-Key` (cu fallback legacy pe `X-Agent-Key`).
- Heartbeat, poll, result și config sunt servite de endpoint-urile generice `/tc/*` din `deltatech_tc` — acest modul nu le mai duplică.
- Meniurile sunt vizibile doar utilizatorilor cu rol de manager contabil (`account.group_account_manager`).

#### 3. Dependențe

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [deltatech_tc](../deltatech_tc/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.tc.station` (extins): adaugă `cert_subject` (subiectul certificatului, doar citire), actualizat la heartbeat, și acțiunile de punere în coadă `action_enqueue_sync_messages` (implicit 30 de zile) și `action_enqueue_submit`.
- `deltatech.tc.job` (extins): adaugă tipurile de job ANAF în câmpul `job_type`.

**Vizualizări**

- `view_tc_station_form_anaf` / `view_tc_station_list_anaf`: extind formularul și lista stațiilor din `deltatech_tc` cu certificatul și acțiunile ANAF.
- `menu_l10n_ro_anaf_agent` („ANAF Station”) și `menu_l10n_ro_anaf_agent_job` („Joburi TC”): meniuri sub Contabilitate → Configurare, care deschid acțiunile `deltatech_tc.action_deltatech_tc_station` și `deltatech_tc.action_deltatech_tc_job`.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; sincronizările se pornesc din butonul **Cere sincronizare mesaje** sau prin push-ul stației la `/anaf_agent/messages`.

#### 5. Conexiuni

- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md): folosește joburile `sync_messages` create de acest modul pentru a sincroniza și prelucra mesajele SPV.
- [l10n_ro_anaf_submission](../l10n_ro_anaf_submission/index.md): folosește joburile `submit` create de acest modul pentru a depune declarații la SPV.
