# Terrabit Helpdesk Link (localizat la `terrabit_helpdesk_link/index.md`)

- **Nume Tehnic:** `terrabit_helpdesk_link`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/terrabit-ro/terrabit/tree/19.0/terrabit_helpdesk_link
- **Cale Locală:** `odoo-addons/terrabit/terrabit_helpdesk_link`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modul utilitar minimal care adaugă în Odoo un element de meniu de nivel superior, „Terrabit Help", prin care orice utilizator intern poate deschide rapid portalul de suport Terrabit (`https://www.terrabit.ro/helpdesk`) într-o filă nouă a browserului. Rolul său este pur de comoditate: oferă un punct de acces vizibil și permanent către helpdesk-ul Terrabit, direct din interfața ERP, fără a adăuga modele sau logică de business.

#### 2. Funcționalități Cheie

- **Meniu de acces rapid la suport:** adaugă meniul de top „Terrabit Help" (cu pictogramă proprie), vizibil tuturor utilizatorilor interni.
- **Deschidere externă a portalului de helpdesk:** la accesarea meniului, deschide într-o filă nouă pagina de suport Terrabit printr-o acțiune de tip URL (`ir.actions.act_url`), fără a părăsi sesiunea Odoo.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

Întrucât `readme/DESCRIPTION.md` este gol, componentele de mai jos au fost identificate prin analiza codului (`views/menu_link.xml`). Modulul nu definește modele.

**Vizualizări**

- Modulul nu definește vizualizări (formulare/liste/kanban) — doar un element de meniu și o acțiune.

**Acțiuni Automate / Acțiuni Server**

- `helpdesk_link_action` (`ir.actions.act_url`): acțiune de tip URL care deschide `https://www.terrabit.ro/helpdesk` cu `target="new"` (filă nouă).
- `helpdesk_link_menu` (`menuitem`): meniul de top „Terrabit Help", legat de acțiunea de mai sus, restrâns la grupul `base.group_user` (utilizatori interni), cu `web_icon` propriu și `sequence` 1000.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki. Modulul este autonom (depinde doar de `base`).
