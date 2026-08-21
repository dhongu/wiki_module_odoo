# Terrabit Helpdesk Link (localizat la `terrabit_helpdesk_link/index.md`)

- **Nume Tehnic:** `terrabit_helpdesk_link`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_helpdesk_link
- **Cale Locală:** `odoo-addons/terrabit/terrabit_helpdesk_link`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modul utilitar minimal care adaugă în Odoo un element de meniu de nivel superior, „Terrabit Help", prin care orice utilizator intern poate deschide rapid formularul de asistență Terrabit direct din interfața ERP. Spre deosebire de un simplu link static, acțiunea precompletează formularul de pe site cu datele de identificare ale companiei (nume, CUI, telefon), numele și emailul utilizatorului curent, plus versiunea de Odoo și numele bazei de date — informații utile echipei de suport pentru a trata rapid solicitarea, fără ca utilizatorul să le introducă manual.

#### 2. Funcționalități Cheie

- **Meniu de acces rapid la suport:** adaugă meniul de top „Terrabit Help" (cu pictogramă proprie), vizibil tuturor utilizatorilor interni (`base.group_user`).
- **Formular de suport precompletat:** la accesarea meniului, deschide într-o filă nouă formularul de pe `https://www.terrabit.ro/helpdesk/asistenta-odoo-1`, cu parametri URL pentru numele și emailul utilizatorului, precum și o descriere pregătită automat ce conține numele companiei, CUI, telefon, versiunea Odoo și numele bazei de date.
- **Citire sigură a datelor companiei:** câmpurile `vat` și `phone` de pe companie (câmpuri `related` către `res.partner`) sunt citite prin `sudo()`, astfel încât și utilizatorii fără drept de scriere pe `res.company` pot folosi meniul fără `AccessError`.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

Întrucât `readme/DESCRIPTION.md` conține doar antetul „Features:" (fără conținut), componentele de mai jos au fost identificate prin analiza codului (`models/res_company.py`, `views/menu_link.xml`).

**Modele**

- `res.company` (extindere): adaugă metoda `action_terrabit_helpdesk()`, care construiește un URL către formularul de suport Terrabit cu parametrii `partner_name`, `partner_email` și `description` (nume companie, CUI, telefon, versiune Odoo, bază de date) și returnează o acțiune `ir.actions.act_url` cu `target="new"`.

**Vizualizări**

- Modulul nu definește vizualizări (formulare/liste/kanban) — doar un element de meniu și o acțiune de server.

**Acțiuni Automate / Acțiuni Server**

- `helpdesk_link_action` (`ir.actions.server`, model `res.company`, `state="code"`): rulează codul `action = env.company.action_terrabit_helpdesk()`, restrâns explicit la grupul `base.group_user` prin `group_ids`, pentru ca Odoo să valideze apartenența la grup în loc de dreptul de scriere pe `res.company`.
- `helpdesk_link_menu` (`menuitem`): meniul de top „Terrabit Help", legat de acțiunea de mai sus, restrâns la `base.group_user`, cu `web_icon` propriu și `sequence` 1000.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki. Modulul este autonom (depinde doar de `base`).
