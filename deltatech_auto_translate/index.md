# Deltatech Auto Translate (localizat la `deltatech_auto_translate/index.md`)

- **Nume Tehnic:** `deltatech_auto_translate`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_auto_translate
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_auto_translate`
- **Ultima Ingestie:** `2026-10-01`

#### 1. Sumar

Modulul traduce automat câmpurile traductibile (text simplu și HTML) folosind cadrul AI nativ din Odoo (modulul `ai`, Enterprise). Este independent de furnizor: folosește modelul AI ales în *Setări → Integrări → Traducere automată* și cheia API a furnizorului respectiv din setările AI. Pentru traducere cu Claude se instalează `deltatech_ai_anthropic`, ale cărui modele apar apoi în listă. Valoarea de afaceri: conținut (produse, pagini, descrieri) tradus în mai multe limbi fără muncă manuală și fără costuri repetate.

#### 2. Funcționalități Cheie

- **Joburi de traducere** (Setări → Auto Translate → Translation jobs): definesc ce se traduce — un model, câmpurile traductibile, un domeniu de filtrare și, opțional, limbile țintă. Fiecare job are propriul cursor de progres.
- **Acțiune programată** instalată **inactivă** (rulează din oră în oră când este activată): procesează joburile în loturi, cu buget de timp. Butonul **Run now** de pe job face același lucru la cerere.
- **Grupare a textelor**: textele unei rulări sunt trimise într-un set de cereri pe limbă.
- **Cache de traduceri**: nimic nu se plătește de două ori.
- **Validarea etichetelor HTML**: o traducere cu etichete sau atribute diferite este respinsă.
- **Corecțiile manuale sunt respectate**: pentru câmpurile simple se rețin hash-urile sursei și ale traducerii scrise; pentru câmpurile HTML se retraduc doar propozițiile modificate în limba sursă.
- **API pentru alte module**: `env["deltatech.translate.service"].translate_records(records, field_names)`; metoda `_system_prompt` poate fi extinsă pentru terminologie proprie.
- Meniu de consultare a cache-ului (Auto Translate → Translation cache).

#### 3. Dependențe

- `ai`
- `base_setup`

#### 4. Componente Cheie

**Modele**

- `deltatech.translate.job`: jobul de traducere (model, câmpuri, domeniu, limbi țintă, progres).
- `deltatech.translate.service` (abstract): serviciul de traducere, cu `translate_records` și `_system_prompt`.
- `deltatech.translate.cache`: cache-ul traducerilor deja obținute.
- `deltatech.translate.state`: starea traducerilor automate pentru câmpurile simple (hash sursă/traducere).
- `res.config.settings` (extins): alegerea modelului AI pentru traducere.

**Vizualizări**

- `deltatech_translate_job_view_list` / `deltatech_translate_job_view_form`: listă și formular pentru joburi.
- `deltatech_translate_cache_view_list`: listă pentru cache.
- `res_config_settings_view_form_auto_translate`: secțiunea de setări cu modelul AI.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_auto_translate` (Auto Translate: run translation jobs): rulează joburile din oră în oră; instalată inactivă.

#### 5. Conexiuni

- [deltatech_ai_anthropic](../deltatech_ai_anthropic/index.md): oferă modelele Claude utilizabile pentru traducere.
