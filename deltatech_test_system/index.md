# Indicator Sistem de Test (localizat la `deltatech_test_system/index.md`)

- **Nume Tehnic:** `deltatech_test_system`
- **Versiune:** `20.0.0.0.11`
- **Cale:** `https://github.com/dhongu/deltatech/tree/20.0/deltatech_test_system`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_test_system`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul ajută la marcarea clară a unei baze de date Odoo ca bază de test sau de producție. Baza de date poate fi neutralizată din Setări, iar în partea de sus a interfeței apare un banner permanent care arată că lucrezi într-o bază de test, ca să nu fie confundată cu producția.

#### 2. Funcționalități Cheie

- Neutralizarea bazei de date din Setări.
- Banner permanent în partea de sus a interfeței pentru bazele de test.
- Starea de neutralizare este vizibilă și în lista de module.

#### 3. Dependențe

- `web`
- `base_setup`

#### 4. Componente Cheie

> Notă: DESCRIPTION.md nu detaliază componentele tehnice; ele au fost sintetizate din cod.

**Modele**

- `res.config.settings` (extins): opțiunea `database_is_neutralized` (parametrul `database.is_neutralized`) și interogările de neutralizare ale modulelor instalate.
- `ir.module.module` (extins): câmp calculat `database_is_neutralized`, citit din același parametru.

**Vizualizări**

- `res_config_settings_view_form`: opțiunea de stare a sistemului în Setări; moștenește `base_setup.res_config_settings_view_form`.
- `module_view_kanban` / `module_form`: ajustări ale vizualizărilor de module.
- `notification_banner` (`views/templates.xml`): bannerul din `web.layout`.

**Acțiuni Automate / Acțiuni Server**

- `data/neutralize.sql`: script de neutralizare. Nu sunt definite sarcini `ir.cron` sau reguli `base.automation`.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module documentate.
