# AI Auto Translate for Odoo

- **Nume Tehnic:** `deltatech_auto_translate`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_auto_translate
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_auto_translate`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Traduce automat câmpurile traductibile (text simplu și HTML) cu framework-ul AI nativ din Odoo (modulul `ai`, Enterprise). Cererile merg către Odoo AI (credite IAP), care alege modelul. Traducerile sunt reținute în cache, deci nu se plătesc de două ori, iar corecțiile manuale ale utilizatorilor sunt respectate.

#### 2. Funcționalități Cheie

- **Joburi de traducere** (Setări → Auto Translate): definesc modelul, câmpurile traductibile, domeniul și, opțional, limbile țintă; fiecare job are propriul cursor de progres.
- **Acțiune programată** instalată **inactivă**, care rulează joburile în loturi, cu buget de timp; butonul **Run now** de pe job face același lucru la cerere.
- Textele unei rulări sunt grupate și trimise într-un singur set de cereri pe limbă.
- **Cache de traduceri** și validarea tagurilor HTML: o traducere cu taguri sau atribute diferite este respinsă.
- **Corecțiile manuale sunt păstrate**: la câmpurile simple se rețin hash-ul sursei și al traducerii scrise; la câmpurile HTML se retraduc doar propozițiile schimbate în limba sursă.
- Activare din *Setări → Integrări → Traducere automată*.
- Alte module pot apela `env["deltatech.translate.service"].translate_records(records, field_names)` și pot extinde `_system_prompt` pentru terminologia proprie.
- Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `ai`
- `base_setup`

#### 4. Componente Cheie

**Modele**

- `deltatech.translate.job`: jobul de traducere (model, câmpuri, domeniu, limbi, cursor de progres).
- `deltatech.translate.service`: serviciul care grupează textele, apelează AI-ul și validează rezultatul.
- `deltatech.translate.cache`: cache-ul traducerilor.
- `deltatech.translate.state`: starea (hash-urile sursei/traducerii) pentru respectarea corecțiilor manuale.
- `res.config.settings` (extins): activarea traducerii automate.

**Vizualizări**

- `deltatech_translate_job_view_list` / `deltatech_translate_job_view_form`: lista și formularul joburilor.
- `deltatech_translate_cache_view_list`: lista cache-ului de traduceri.
- `res_config_settings_view_form_auto_translate`: setările din Integrări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_auto_translate` (Auto Translate: run translation jobs): rulează joburile în loturi; livrată inactivă.

#### 5. Conexiuni

- `ai`: framework-ul AI Enterprise prin care se fac cererile (credite IAP).
