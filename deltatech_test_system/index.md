# Test System Indicator (localizat la `deltatech_test_system/index.md`)

- **Nume Tehnic:** `deltatech_test_system`
- **Versiune:** `19.0.0.0.12`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_test_system
- **Cale Locală:** `odoo-addons/deltatech/deltatech_test_system`
- **Ultima Ingestie:** `2026-11-20`

#### 1. Sumar

O copie de test a unei baze de date se confundă ușor cu producția. Modulul marchează o bază de date ca fiind de test sau de producție, afișează un banner pe cele de test și ascunde butoanele de instalare și dezinstalare din ecranul Aplicații pe cele de producție. Astfel, utilizatorii și administratorii știu imediat în ce mediu lucrează și evită modificări accidentale pe baza reală.

#### 2. Funcționalități Cheie

- **Test sau producție:** setarea **Database Is Neutralized**, în secțiunea de companii din setările generale, marchează o bază de date de test. Textul de sub ea indică „It is a test system” sau „It is a productive system”.
- **Neutralizare la salvare:** salvarea cu bifa nou activată rulează scriptul `data/neutralize.sql` al fiecărui modul instalat care îl are. O nouă salvare nu repetă operația, iar debifarea nu anulează ce au modificat scripturile.
- **Banner de test:** la fiecare salvare a setărilor, bannerul de neutralizare al clientului web (`web.neutralize_banner`) se activează sau se dezactivează conform bifei.
- **Ecran Aplicații mai sigur:** pe o bază care nu este neutralizată (producție), cardurile și formularul modulelor ascund butoanele de instalare și dezinstalare, iar fiecare card arată „Is installed” sau „Is not installed”.
- **Bare de notificare:** când parametrul de sistem `database_notification_banner` conține un text, utilizatorii interni îl văd într-o bară galbenă; `database_news_notification` face același lucru într-o bară albastru deschis. Parametrii nu au ecran de setări; se completează ca parametri de sistem.
- Modulul nu are grupuri de securitate proprii.

#### 3. Dependențe

- `web`
- `base_setup`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extins): câmpul `database_is_neutralized` (parametrul `database.is_neutralized`) și `neutralize_database()`, care rulează scripturile `neutralize.sql` ale modulelor instalate la prima bifare; `set_values()` activează sau dezactivează bannerul `web.neutralize_banner`.
- `ir.module.module` (extins): câmpul calculat `database_is_neutralized`, citit din parametrul `database.is_neutralized`, folosit pentru a ascunde butoanele de instalare/dezinstalare.

**Vizualizări**

- `res_config_settings_view_form`: setarea „Database Is Neutralized” în secțiunea de companii din Setări (moștenește `base_setup.res_config_settings_view_form`).
- `module_view_kanban` / `module_form`: ascund butoanele de instalare și dezinstalare pe bazele de producție și afișează starea „Is installed” / „Is not installed” pe carduri.
- `notification_banner` (`views/templates.xml`, extinde `web.layout`): barele de notificare galbenă și albastră pentru utilizatorii interni.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`. Scripturile de neutralizare rulează doar la salvarea setărilor.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale către alte module documentate în wiki.
