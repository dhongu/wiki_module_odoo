# Deltatech Test System (localizat la `deltatech_test_system/index.md`)

- **Nume Tehnic:** `deltatech_test_system`
- **Versiune:** `19.0.0.0.7`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_test_system`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_test_system`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul ajută la marcarea clară a unei baze de date Odoo ca fiind de test sau de producție. Atunci când o bază de date este folosită pentru testare, modulul permite „neutralizarea” ei din setări și afișează permanent, în partea de sus a interfeței, un banner vizibil. Astfel, utilizatorii și administratorii știu imediat că lucrează într-un mediu de test și evită confuzia cu baza de date reală de producție.

#### 2. Funcționalități Cheie

- Setarea stării sistemului: test sau producție.
- Neutralizarea bazei de date direct din setări.
- Afișarea unui banner permanent în partea de sus a interfeței pentru a indica faptul că baza de date este una de test.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

> Notă: Fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, dar nu detaliază componentele tehnice. Acestea au fost sintetizate din `__manifest__.py` și din structura modulului pentru completitudine.

**Modele**

- `res.config.settings`: extins pentru a expune opțiunea de setare a stării sistemului (test/producție) și de neutralizare a bazei de date.
- `ir.module.module`: extins în contextul gestionării stării sistemului de test.

**Vizualizări**

- `res_config_settings_view.xml`: adaugă în Setări opțiunile pentru marcarea stării sistemului și neutralizarea bazei de date.
- `ir_module_module_view.xml`: ajustări de vizualizare aferente modulelor.
- `templates.xml`: definește bannerul permanent afișat în partea de sus a interfeței pentru bazele de date de test.

**Acțiuni Automate / Acțiuni Server**

- Modulul include fișierul de date `data/neutralize.sql`, folosit la neutralizarea bazei de date. Nu sunt definite sarcini `ir.cron` sau reguli `base.automation`.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module documentate în wiki.
