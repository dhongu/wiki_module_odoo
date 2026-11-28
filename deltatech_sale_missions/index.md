# Misiuni de vânzări (Sales Missions)

- **Nume Tehnic:** `deltatech_sale_missions`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sale_missions
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_missions`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În fiecare luni, fiecare agent de vânzări primește o listă scurtă de **misiuni de recâștigare**: clienții din portofoliul lui care scad sau au devenit inactivi, cei cu cei mai mulți bani în joc primii, cu termen vineri. O misiune se lucrează până când clientul cumpără din nou, revine mai târziu sau este pierdut, iar fiecare pas este consemnat. Modulul este bazat pe modulul de misiuni de vânzări al MD Trade Concept SRL.

#### 2. Funcționalități Cheie

- **Valul săptămânal**, unul pe companie și săptămână: cotă per agent (implicit 4, ajustabilă per agent), o treime rezervată clienților în scădere, niveluri A / B / C după banii în joc. Nu intră clienții cu misiune deschisă, cei în pauza de după închidere, cei pierduți din cauze pe care firma nu le poate remedia, cei fără telefon și e-mail sau cu restanțe mari; clienții inactivi fără agent sunt listați separat pentru director.
- **Construit pe segmentele de clienți:** valul citește rândurile nocturne din *Customer Segment* (`deltatech_customer_segment`), recalculate chiar înainte, și recomandarea din *Customer Analysis* (`deltatech_customer_analysis`): o singură definiție a clientului în scădere și inactiv.
- **O misiune, un ecran:** *Am sunat*, *Trimite e-mail*, *Am vizitat*, *A cumpărat*, *Am vorbit, revine*, *Amână*, *Pierdut*. Formularul spune ce să zici la telefon (fiecare sfat cu cifra lui), ce a cumpărat clientul pe categorii și produse, încercările anterioare și un link WhatsApp.
- **Închiderea explică mereu:** *Pierdut* cere motiv și ce a spus clientul; *Am vorbit, revine* cere motiv și ziua revenirii, iar misiunea se redeschide singură în acea zi.
- **Recuperare automată:** o factură postată sau o comandă confirmată închide misiunea ca recuperată și se numără vânzările fără taxe din fereastra de recuperare (30 de zile implicit); un cron zilnic prinde facturile importate. O eroare în misiuni nu blochează niciodată o factură sau o comandă.
- **E-mailuri ca scrisori personale:** șapte șabloane oferite ca fișe, cu previzualizare randată pe clientul real; cele cu părți de completat nu pot fi trimise ca atare, iar nimic nu pleacă fără agent.
- **Pentru directorul de vânzări:** misiuni echipă, misiuni întârziate escaladate o singură dată, jurnalul cine a deschis/sunat/scris, motivele pentru care clienții nu mai cumpără și tabloul *Misiuni pe agent* (atinse, văzute, timp de răspuns, clienți reveniți, sumă recuperată, când lucrează).
- **Roluri ale portofoliului de clienți:** *Clienți proprii* lucrează doar misiunile proprii; *Toți clienții* le vede pe toate și generează valul.
- **Meniuri:** *Vânzări > Portofoliu clienți > Misiuni de vânzări* (*Misiunile mele*, *Misiuni echipă*, *Misiuni întârziate*, *Misiuni pe agent*, *De ce nu mai cumpără*, *Jurnal*, *Valuri săptămânale*), iar setările din *Setări misiuni* (agenți, motive de pierdere, șabloane de e-mail, *Generează valul acum*).
- Nu adaugă câmpuri pe modele standard. Modul cu plată pe Odoo Apps (200 EUR, licență OPL-1, stadiu Beta). Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md)
- `mail`

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.mission`: misiunea unui client (cu `mail.thread` și activități).
- `deltatech.sale.mission.wave`: valul săptămânal al unei companii.
- `deltatech.sale.mission.event`: jurnalul pașilor.
- `deltatech.sale.mission.agent`: cotă și excepții per agent.
- `deltatech.sale.mission.reason`: motive de pierdere / revenire.
- `deltatech.sale.mission.template`: șabloanele fișelor de e-mail.
- `deltatech.sale.mission.dashboard`: raportul *Misiuni pe agent*.
- `deltatech.sale.mission.close.wizard` / `deltatech.sale.mission.email.wizard`: închiderea și trimiterea e-mailului.
- `sale.order`, `account.move` (extinse): recuperarea automată a misiunii; `deltatech.customer.segment.config` (extins): setările valului pe companie.

**Vizualizări**

- `mission_views.xml`: kanban, listă și formular al misiunii.
- `mission_wave_views.xml`, `mission_event_views.xml`, `mission_config_views.xml`, `mission_wizard_views.xml`, `mission_dashboard_views.xml`, `menus.xml`.
- Active JS: tabloul de bord și `open_logger` (jurnalizarea deschiderii misiunii).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_mission_generate_weekly`: generează valul săptămânal, în fiecare luni dimineață.
- `ir_cron_mission_sync_purchases`: zilnic, recuperează misiunile pentru facturile importate.

#### 5. Conexiuni

- [deltatech_customer_segment](../deltatech_customer_segment/index.md): sursa rândurilor nocturne de segmente citite de val.
- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md): recomandarea și definiția clientului în scădere / inactiv.
