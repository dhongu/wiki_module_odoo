# Delivery IoT Printers per User (localizat la `deltatech_delivery_iot/index.md`)

- **Nume Tehnic:** `deltatech_delivery_iot`
- **Versiune:** `20.0.0.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_delivery_iot
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_iot`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul atribuie imprimante IoT utilizatorilor, astfel încât fiecare operator din depozit să tipărească etichetele de expediere la imprimanta de lângă propria stație, nu la imprimanta de care este atașat raportul. Este util în depozite cu mai multe stații de ambalare, evitând ca etichetele unui operator să iasă la imprimanta altuia.

#### 2. Funcționalități Cheie

- Câmpul **Users** pe formularul dispozitivului IoT (`iot.device`), pentru a atribui imprimanta unuia sau mai multor utilizatori.
- Regulă deliberat îngustă: dacă cel puțin o imprimantă a raportului are utilizatori atribuiți, rămân doar imprimantele care îl listează pe utilizatorul curent, iar cele fără utilizatori sunt excluse. Dacă nicio imprimantă nu are utilizatori, nu se filtrează nimic și rămâne comportamentul standard — astfel o imprimantă atribuită unei singure persoane nu blochează tipărirea pentru ceilalți.
- Dialogul de selecție a imprimantei (deschis la tipărirea unui raport legat de imprimante) oferă doar imprimantele permise utilizatorului curent, iar prima sa imprimantă este preselectată când nu se aplică o alegere anterioară.
- Alegerea explicită a utilizatorului (`data['device_id']`) nu este suprascrisă de filtrul automat.

#### 3. Dependențe

- `delivery_iot`

#### 4. Componente Cheie

**Modele**

- `iot.device` (extindere): adaugă câmpul `user_ids` (Many2many către `res.users`, exclude utilizatorii partajați/portal).
- `ir.actions.report` (extindere): filtrarea imprimantelor IoT pe baza utilizatorului curent, la generarea directă a raportului și în dialogul de selecție a imprimantei; include un hook `_get_report_from_name` care poate sări peste raportul de etichete de expediere prin contextul `skip_report_shipping_labels`.

**Vizualizări**

- `iot_device_view_form`: extinde formularul dispozitivului IoT, adăugând `user_ids` ca tag-uri many2many.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- `delivery_iot`: modulul de bază care oferă tipărirea automată prin imprimante IoT; acest modul îi adaugă restricția pe utilizator.
- `iot`: furnizează modelul `iot.device` și dialogul de selecție a imprimantei extinse de acest modul.
- `stock`: fluxul de expediere (`stock.picking`) declanșează tipărirea etichetelor filtrate de acest modul.
