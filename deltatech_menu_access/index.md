# Deltatech Menu Access (Acces pe aplicații)

- **Nume Tehnic:** `deltatech_menu_access`
- **Versiune:** `19.0.3.0.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/deltatech_menu_access
- **Cale Locală:** `odoo-addons/terrabit/deltatech_menu_access`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul ascunde aplicațiile de pe ecranul principal, din bara de sus și din paleta de comenzi, fie pentru un singur utilizator, fie prin grupuri de acces, **fără a modifica meniurile standard**. Scopul este reducerea aglomerării vizuale: fiecare utilizator vede doar aplicațiile de care are nevoie. Atenție: nu este o restricție de securitate. O aplicație ascunsă poate fi deschisă de cine îi cunoaște adresa, iar drepturile de citire/scriere rămân cele ale grupurilor standard.

#### 2. Funcționalități Cheie

- **Ascundere pe utilizator:** pe fișa utilizatorului, tabul **Aplicații ascunse** (Hidden Apps) listează aplicațiile pe care acel utilizator nu trebuie să le vadă.
- **Ascundere prin grupuri de acces:** un grup legat de o aplicație (câmpul **Aplicație** din formularul grupului) face aplicația vizibilă doar membrilor săi. Dacă o aplicație are unul sau mai multe grupuri de acces, utilizatorii din niciunul dintre ele nu o văd. Grupurile standard se aplică în continuare: un grup de acces singur nu afișează o aplicație la care utilizatorul nu are drepturi.
- Cele două metode se cumulează.
- **Acțiunea „Create Menu Access Groups”** (pe lista de Utilizatori, doar administratori) creează câte un grup `Access <Aplicație>` pentru fiecare aplicație și îl leagă de aceasta. Grupul nou pornește cu utilizatorii care văd deja aplicația, deci rularea nu ascunde nimic; refolosește ID-urile externe, deci rularea repetată nu creează duplicate.
- **Aplicații protejate:** Administration, Discuss și Business Process nu sunt ascunse niciodată prin grupuri de acces, pentru a evita blocarea accesului în bază.
- Meniurile sunt cache-uite per utilizator; cache-ul se invalidează la schimbarea aplicațiilor ascunse, a grupurilor unui utilizator, a membrilor unui grup sau a aplicației legate.
- **Upgrade de la 19.0.2.x:** migrarea leagă grupurile de acces de aplicații, scoate grupurile de pe meniurile rădăcină și reface grupurile standard din definițiile `menuitem`. Un meniu la care grupurile standard ar face un membru curent să piardă aplicația rămâne fără grupuri (vizibil ca înainte) și e consemnat în log.
- Unificat cu `mdtrade_menu_visibility` (MD Trade Concept SRL), tichet 9618.

#### 3. Dependențe

- `web`

#### 4. Componente Cheie

**Modele**

- `ir.ui.menu` (extins): ascunderea la încărcarea meniurilor prin `_load_menus_blacklist()` (ecran principal, bară, paletă de comenzi) și `get_user_roots()` (șabloane website, scurtături PWA); verificare administrator pentru operațiile de administrare.
- `res.groups` (extins): câmpul `dma_menu_id` leagă grupul de o aplicație (doar meniuri rădăcină); invalidează cache-ul la create/unlink.
- `res.users` (extins): câmpul `dma_hidden_app_ids` (aplicații ascunse per utilizator, doar rădăcini) și metoda `action_create_menu_access_groups()`.

**Vizualizări**

- `view_users_form_dma_hidden_apps`: tabul „Aplicații ascunse” în formularul utilizatorului.
- `view_groups_form_dma_menu`: câmpul Aplicație în formularul grupului.
- `view_groups_search_dma_menu`: filtrare grupuri după aplicația legată.

**Acțiuni Automate / Acțiuni Server**

- `ir_actions_server_create_menu_access_groups`: „Create Menu Access Groups”, acțiune server legată de `res.users`, restricționată la grupul Settings (`base.group_system`).

#### 5. Conexiuni

- `mdtrade_menu_visibility`: modul client MD Trade, ale cărui funcții (ascundere per utilizator) au fost unificate aici.
