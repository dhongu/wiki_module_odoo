# Transport Change (localizat la `deltatech_transport_change/index.md`)

- **Nume Tehnic:** `deltatech_transport_change`
- **Versiune:** `19.0.0.1.9`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_transport_change
- **Cale Locală:** `odoo-addons/deltatech/deltatech_transport_change`
- **Ultima Ingestie:** `2026-11-05`

#### 1. Sumar

Datele de configurare introduse manual într-o bază de dezvoltare sau de test (etape, etichete, parametri, date de bază ale oricărui model) trebuie reintroduse în producție, cu riscul ca cele două baze să ajungă diferite. Acest modul tehnic exportă astfel de date în fișiere CSV într-un modul Odoo ținut în Git, astfel că modificarea ajunge în celelalte baze prin actualizarea acelui modul, similar cererilor de transport din SAP. Este nou în 19.0.

#### 2. Funcționalități Cheie

- **Configurații de export**: fiecare configurație numește un model, câmpurile de exportat și un domeniu opțional. **Generate File** pe formular, sau **Actions > Export CSV** pe mai multe configurații selectate, produce câte un fișier CSV per configurație. Prima coloană este întotdeauna External ID-ul (`id`) al înregistrării, deci importul actualizează aceleași înregistrări în loc să creeze duplicate.
- **Relații ca ID-uri externe**: câmpurile Many2one și Many2many se exportă într-o coloană `field/id` cu ID-urile externe ale înregistrărilor legate. Înregistrările fără ID extern primesc unul stabil de tip `__export__`.
- **Repository-uri Git**: un repository păstrează URL-ul Git, ramura, codul modulului (folderul modulului țintă din repository) și utilizatorul și token-ul HTTPS. Credențialele sunt vizibile doar administratorilor.
- **Commit și push**: la export, repository-ul este clonat într-un folder temporar, CSV-ul se scrie în `<modul>/data/<model>.csv`, fișierul se adaugă în lista `data` din `__manifest__.py` al modulului și versiunea modulului crește. Toate configurațiile unui repository intră într-un singur commit, trimis pe ramură.
- **Urmă în chatter**: fiecare configurație păstrează CSV-ul generat ca atașament în chatter, cu rezultatul push-ului. Un push respins e raportat ca eșec, iar **Last Export** se actualizează doar pentru configurațiile care au ajuns în repository.
- **Unde se configurează**: în modul developer, *Settings > Technical > Transport > Repositories* și *Settings > Technical > Transport > Configurations*. Au acces doar administratorii Settings. Pachetul Python `GitPython` trebuie instalat pe server.
- **Limitări**: formatul de export este doar CSV (nu și XML); funcționează doar HTTPS cu utilizator și token, iar tipul de credențial **SSH Key**, câmpul **SSH Private Key** și câmpul **Local Path** sunt stocate, dar nefolosite; o configurație nu poate fi exportată fără repository, nu există descărcare simplă a CSV-ului; `__manifest__.py` țintă este rescris din conținutul parsat, deci își pierde comentariile și formatarea.

#### 3. Dependențe

- `base`
- `mail`

Dependență externă Python: `GitPython`.

#### 4. Componente Cheie

Sumarul și Funcționalitățile Cheie provin din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului este omisă. Din structura modulului:

**Modele**

- `transport.config`: configurația de export (model, câmpuri, domeniu); moștenește `mail.thread` și `mail.activity.mixin`.
- `transport.repo`: repository-ul Git țintă (URL, ramură, codul modulului, credențiale).
- `models/transport_utils.py`: funcții ajutătoare pentru export.

**Vizualizări**

- `view_transport_config_tree` / `view_transport_config_form` (`views/transport_config_views.xml`): lista și formularul configurațiilor, meniul *Configurations*.
- `view_transport_repo_tree` / `view_transport_repo_form` (`views/transport_repo_views.xml`): lista și formularul repository-urilor, meniul *Repositories*.

**Acțiuni Automate / Acțiuni Server**

- `server_action_transport_config_export`: acțiunea server **Export CSV** din meniul *Actions* al listei de configurații.
- Nu sunt definite sarcini `ir.cron`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
