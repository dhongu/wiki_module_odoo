# Deltatech Sales Missions (localizat la `deltatech_sale_missions/index.md`)

- **Nume Tehnic:** `deltatech_sale_missions`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_missions
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_missions`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În fiecare luni, fiecare agent de vânzări primește o listă scurtă de **misiuni de recuperare**: clienții în scădere și cei inactivi din portofoliul lui, cu cei mai mulți bani în joc primii și cu termen vineri. O misiune se lucrează până când clientul cumpără din nou, promite că revine sau este pierdut, iar fiecare pas este consemnat. Astfel, recuperarea clienților nu mai depinde de memoria agentului, iar directorul de vânzări vede cine a sunat, ce a răspuns clientul și cât s-a recuperat.

#### 2. Funcționalități Cheie

- **Valul săptămânal**, unul pe companie și săptămână: cotă per agent (implicit 4, ajustabilă per agent), o treime rezervată clienților în scădere, trepte A / B / C după banii în joc. Nu intră clienții cu misiune deschisă, cei aflați în pauză după închidere, cei pierduți din cauze pe care firma nu le poate remedia, cei fără telefon și email sau cu restanțe mari. Clienții inactivi fără agent sunt listați separat, pentru director.
- **Construit pe segmentele de clienți**: valul citește rândurile nocturne din *Customer Segment* (`deltatech_customer_segment`), recalculate chiar înainte, și recomandarea din *Customer Analysis* (`deltatech_customer_analysis`) — o singură definiție a „în scădere" și „inactiv" pentru segmente, tablou de bord și misiuni.
- **O misiune, un ecran**: butoanele *Am sunat*, *Trimite email*, *Am vizitat*, *A cumpărat*, *Am vorbit, revine*, *Amână*, *Pierdut*. Formularul arată ce să-i spui clientului la telefon (fiecare argument cu cifra lui), ce a cumpărat pe categorii și produse, încercările anterioare și un link WhatsApp.
- **Închiderea explică mereu**: „pierdut" cere motiv și ce a spus clientul; „am vorbit, revine" cere motiv și ziua revenirii, iar misiunea se redeschide singură în acea zi; „amână" cere ziua de revenire.
- **Recuperare automată**: o factură postată sau o comandă confirmată închide misiunea ca recuperată și se numără vânzările fără taxe din fereastra de recuperare (implicit 30 de zile). Un cron zilnic prinde facturile importate. O eroare în misiuni nu blochează niciodată o factură sau o comandă.
- **Emailuri ca scrisori personale**: șapte șabloane oferite ca fișe, cu previzualizare randată pe clientul real; cele cu părți de completat nu pot fi trimise ca atare. Nimic nu pleacă fără agent. Șablonul „Invitație în showroom" este arhivat implicit.
- **Pentru directorul de vânzări**: misiuni ale echipei, misiuni întârziate escaladate o singură dată, jurnalul cine a deschis/sunat/scris, motivele pentru care clienții nu mai cumpără și tabloul *Misiuni pe agent* (atinși, văzuți, timp de răspuns, clienți reveniți, sumă recuperată, când lucrează).
- **Roluri ale portofoliului de clienți**: *Clienții proprii* lucrează doar misiunile proprii; *Toți clienții* le vede pe toate și generează valul. Cifrele unei misiuni sunt scrise doar de generare și de recuperare.
- **Căi de meniu**: *Vânzări > Portofoliu clienți > Misiuni vânzări* (Misiunile mele, Misiuni echipă, Misiuni întârziate, Misiuni pe agent, De ce nu mai cumpără, Jurnal misiuni, Valuri săptămânale); *Setări misiuni* (Agenți, Motive de pierdere, Șabloane email, Generează valul acum). Parametrii per companie (cotă, termen, escaladare, pauză după închidere, fereastră de recuperare, istoric minim, filtre de contact, prag restanțe, trepte) sunt în *Portofoliu clienți > Setări*, grupul *Misiuni vânzări*. Rolurile se acordă la *Setări > Utilizatori > Portofoliu clienți*.
- Nu adaugă câmpuri pe modelele standard: cotele per agent, fișele șabloanelor de email și setările per companie au înregistrări proprii.

#### 3. Dependențe

- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md)
- `mail`

(`deltatech_customer_segment` intră tranzitiv prin `deltatech_customer_analysis`.)

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.mission`: misiunea de recuperare (cu `mail.thread` și `mail.activity.mixin`), cu stări, termen, cifre de recuperare.
- `deltatech.sale.mission.wave`: valul săptămânal, cu generarea și lista motivelor pentru care un client nu a primit misiune.
- `deltatech.sale.mission.event`: jurnalul de evenimente (deschis, sunat, scris etc.).
- `deltatech.sale.mission.agent`: cota și excepțiile per agent.
- `deltatech.sale.mission.reason`: motivele de pierdere / revenire.
- `deltatech.sale.mission.template`: șabloanele de email ca fișe.
- `deltatech.sale.mission.dashboard`: sursa tabloului *Misiuni pe agent*.
- `deltatech.sale.mission.close.wizard`, `deltatech.sale.mission.email.wizard`: asistenții de închidere și de trimitere email.
- Extinderi: `deltatech.customer.segment.config` (setările misiunilor per companie), `account.move` și `sale.order` (recuperare la postare / confirmare).

**Vizualizări**

- `view_mission_kanban`, `view_mission_kanban_team`, `view_mission_list`, `view_mission_form`, `view_mission_search`, `view_mission_graph`, `view_mission_pivot`: interfețele misiunilor.
- `view_mission_wave_list`, `view_mission_wave_form`: valurile săptămânale.
- `view_mission_event_list`, `view_mission_event_search`, `view_mission_event_pivot`: jurnalul.
- `view_mission_close_wizard_form`, `view_mission_email_wizard_form`: asistenții.
- `view_customer_segment_config_form`: setările misiunilor.
- Tablou OWL de bord și `open_logger` în `static/src/`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_mission_generate_weekly`: generează valul săptămânal (luni dimineața).
- `ir_cron_mission_sync_purchases`: zilnic, închide misiunile ale căror clienți au cumpărat (facturi importate).
- `ir_cron_mission_wake_postponed`: zilnic, redeschide misiunile cu ziua de revenire sosită.
- `ir_cron_mission_escalate_late`: zilnic, escaladează o singură dată misiunile întârziate către director.

#### 5. Conexiuni

- [deltatech_customer_segment](../deltatech_customer_segment/index.md): segmentele de clienți (F1) din care valul citește rândurile nocturne.
- [deltatech_customer_analysis](../deltatech_customer_analysis/index.md): analiza clienților (F2), recomandările și tabloul de bord.
