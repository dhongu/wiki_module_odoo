# Deltatech Delivery IOT (localizat la `deltatech_delivery_iot/index.md`)

- **Nume Tehnic:** `deltatech_delivery_iot`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_delivery_iot
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_iot`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul permite restricționarea imprimantelor IoT folosite la tipărirea automată a etichetelor de expediere, astfel încât fiecare utilizator să vadă și să folosească doar imprimantele care i-au fost atribuite explicit. Este util în depozite cu mai multe stații de ambalare, fiecare echipată cu propria imprimantă IoT, pentru a evita ca etichetele unui operator să iasă la imprimanta altui operator.

#### 2. Funcționalități Cheie

- Atribuirea unuia sau mai multor utilizatori fiecărei imprimante IoT (`iot.device`), direct din formularul dispozitivului.
- Filtrarea automată a imprimantelor propuse la tipărirea etichetelor de expediere, păstrând doar imprimantele atribuite utilizatorului curent (dacă cel puțin o imprimantă din raport are utilizatori asignați).
- Filtrarea listei de imprimante afișate în dialogul de selecție a imprimantei (introdus în Odoo 19 pentru tipărirea IoT), astfel încât un utilizator să nu poată alege imprimanta altui utilizator.
- Respectarea alegerii explicite a utilizatorului atunci când imprimanta este selectată manual (`data['device_id']`), fără suprascriere de către filtrul automat.

#### 3. Dependențe

- `delivery_iot`

#### 4. Componente Cheie

**Modele**

- `iot.device` (extindere): adaugă câmpul `user_ids` (Many2many către `res.users`, exclude utilizatorii partajați/portal) pentru a atribui imprimanta unuia sau mai multor utilizatori interni.
- `ir.actions.report` (extindere): adaugă logica de filtrare a imprimantelor IoT pe baza utilizatorului curent, atât la generarea directă a raportului (`report_action`), cât și în dialogul de selecție a imprimantei (`get_action_wizard`); include și un hook `_get_report_from_name` care poate sări peste raportul de etichete de expediere via contextul `skip_report_shipping_labels`.

**Vizualizări**

- `iot_device_view_form`: extinde formularul standard al dispozitivului IoT (`iot.iot_device_view_form`), adăugând câmpul `user_ids` ca tag-uri many2many lângă identificatorul dispozitivului.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server; logica de filtrare rulează sincron la apelarea acțiunilor de tipărire.

#### 5. Conexiuni

- `delivery_iot`: modulul de bază care oferă tipărirea automată prin imprimante IoT; acest modul îi adaugă restricția pe utilizator.
- `iot`: furnizează modelul `iot.device` și dialogul de selecție a imprimantei (`select.printers.wizard`) extinse de acest modul.
- `stock`: fluxul de expediere (`stock.picking`) declanșează tipărirea etichetelor filtrate de acest modul.
