# Delivery IoT Printers per User (localizat la `deltatech_delivery_iot/index.md`)

- **Nume Tehnic:** `deltatech_delivery_iot`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_delivery_iot
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_iot`
- **Ultima Ingestie:** `2026-11-15`

#### 1. Sumar

Modulul atribuie imprimantele IoT utilizatorilor, astfel încât un operator din depozit tipărește etichetele de expediere la imprimanta de lângă propria stație, nu la imprimanta de care e legat raportul. Este util în depozite cu mai multe stații de ambalare, fiecare cu propria imprimantă IoT, pentru ca etichetele unui operator să nu iasă la imprimanta altuia.

#### 2. Funcționalități Cheie

- Câmpul **Users** pe formularul dispozitivului IoT (`iot.device`), pentru atribuirea imprimantei unuia sau mai multor utilizatori interni.
- **Regulă restrânsă de filtrare**: dacă cel puțin o imprimantă a raportului are utilizatori atribuiți, rămân doar imprimantele pe care apare utilizatorul curent, iar imprimantele fără utilizatori sunt excluse. Dacă nicio imprimantă a raportului nu are utilizatori, nu se filtrează nimic și se aplică comportamentul standard, deci o singură imprimantă atribuită unei persoane nu ia silențios tipărirea celorlalți.
- Filtrarea se aplică în ambele locuri în care Odoo 19 alege imprimanta: la acțiunea directă de tipărire și în dialogul de selecție a imprimantei (unde alegerea se face acum pe client), astfel încât un utilizator să nu poată alege imprimanta unui coleg.
- O imprimantă transmisă explicit de utilizator (`data['device_id']`) nu este niciodată suprascrisă de filtrul automat.

#### 3. Dependențe

- `delivery_iot`

#### 4. Componente Cheie

**Modele**

- `iot.device` (extins): adaugă `user_ids` (Many2many către `res.users`, doar utilizatori interni, nu partajați/portal).
- `ir.actions.report` (extins): filtrează imprimantele IoT după utilizatorul curent în `report_action` (tipărire directă) și în `get_action_wizard` (dialogul de selecție `select.printers.wizard`); logica comună stă în `_iot_devices_for_current_user`. Suprascrie și `_get_report_from_name`, care returnează un raport gol când contextul conține `skip_report_shipping_labels`.

**Vizualizări**

- `iot_device_view_form`: extinde formularul dispozitivului IoT (`iot.iot_device_view_form`) cu `user_ids` ca etichete many2many, după identificator.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server; filtrarea rulează sincron la apelarea acțiunilor de tipărire.

#### 5. Conexiuni

- `delivery_iot`: modulul de bază pentru tipărirea automată pe imprimante IoT; acest modul îi adaugă restricția pe utilizator.
- `iot`: furnizează modelul `iot.device` și dialogul de selecție a imprimantei, extinse aici.
- `stock`: fluxul de expediere (`stock.picking`) declanșează tipărirea etichetelor filtrate de acest modul.
