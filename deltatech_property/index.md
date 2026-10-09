# Property Management (Administrare proprietăți)

- **Nume Tehnic:** `deltatech_property`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_property
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_property`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă un sistem de administrare a proprietăților imobiliare ale companiei: terenuri, clădiri și încăperile din clădiri. Fiecare proprietate are fișă proprie cu adresă, proprietar, mod și dată de achiziție, valori și suprafețe, iar clădirile pot fi detaliate pe camere, caracteristici și istoric. Fiind construit peste echipamentele din Mentenanță, proprietățile pot fi urmărite și întreținute cu aceleași instrumente ca restul echipamentelor.

#### 2. Funcționalități Cheie

- Evidența terenurilor (intravilan/extravilan, tarla, parcelă, sector cadastral, carte funciară, UTR, categorie) și a clădirilor (teren asociat, categorie, destinație, dată PIF, structură acoperiș, locuri de parcare, nr. de ocupanți, dotare cu mobilier).
- Date comune: adresă, proprietar și responsabil, regiune, număr de activ, cod de clasificare, mod/dată/document de achiziție, coordonate GPS, preț, valoare la achiziție, imagine, număr de documente atașate, discuții și activități (chatter).
- Camere pe clădire: nivel, înălțime, perimetru, suprafață, tip pardoseală, destinație, stare tehnică, închiriere (chiriaș), ultima mentenanță.
- Suprafețe calculate automat la nivel de clădire: suprafața pe fiecare destinație de cameră (birouri, bucătării, garaje etc.) este suma camerelor de acea destinație; suprafața totală curățată (administrativă + industrială + externă) și suprafața de derating (internă + externă). Suprafețele administrativă și industrială curățate și derating-ul intern se introduc manual.
- Caracteristicile clădirii și istoric (`building.history`), valoare de piață la închiriere, reevaluare (dată și valoare), medii lunare de utilități vară/iarnă, data verificării.
- Nomenclatoare configurabile: moduri de achiziție, destinații de clădire (ierarhice), regiuni, destinații de cameră; categoriile de teren/clădire.
- Tipuri noi de adresă pe parteneri: „Land” și „Building”, cu avatar dedicat.
- Meniu de aplicație „Property”: Property, Information (camere), Reports, Configurations.
- Securitate: drepturi doar pentru utilizatori interni; camerele, caracteristicile și istoricul urmează clădirea (reguli pe companie și pe echipamentele urmărite de utilizator, ca în Mentenanță).

#### 3. Dependențe

- `mail`
- `maintenance`

#### 4. Componente Cheie

**Modele**

- `property.property` (abstract): bază comună, extinde `maintenance.equipment` prin `_inherits`, cu adresă, proprietar, achiziție, valori, chatter.
- `property.land`: teren, cu date cadastrale.
- `property.building`: clădire, cu suprafețe calculate, camere, caracteristici și istoric.
- `property.room`: cameră dintr-o clădire; `room.usage`: destinații de cameră.
- `property.features`, `building.history`: caracteristicile și istoricul clădirii.
- `property.nomenclature` și derivate (`property.acquisition`, `property.land.categ`, `property.building.categ`, `property.building.purpose`, `property.region`, `property.room.usage`): nomenclatoare.
- `res.partner` (extins): tipuri de adresă „Land”/„Building”.

**Vizualizări**

- `view_property_land_kanban` / `_list` / `_form` / `_filter`: terenuri.
- `view_property_building_kanban` / `_list` / `_form` / `_filter`: clădiri.
- `view_property_room_list` / `_form` / `_filter`: camere.
- `view_property_nomenclature_list` / `_form`: nomenclatoare de configurare.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni automate sau cron-uri.

#### 5. Conexiuni

- `maintenance`: proprietățile sunt echipamente de mentenanță, deci moștenesc echipe, cereri și reguli de acces.
