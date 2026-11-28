# Services Equipment Base (localizat la `deltatech_service_equipment_base/index.md`)

- **Nume Tehnic:** `deltatech_service_equipment_base`
- **Versiune:** `19.0.1.2.13`
- **Cale:** https://github.com/dhongu/deltatech_service/tree/19.0/deltatech_service_equipment_base
- **Cale Locală:** `odoo-addons/deltatech_service/deltatech_service_equipment_base`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă baza pentru gestiunea echipamentelor în activitatea de service: locuri funcționale la
client, fișa echipamentelor, contoarele lor și citirile de contor, cu o valoare estimată calculată
prin regresie liniară din citirile reale. Nu face facturare pe baza citirilor și nici introducere
automată de citiri estimate la sfârșitul perioadei — acestea, ca și legătura echipamentelor cu
contractele de service, sunt aduse de `deltatech_service_equipment` și `deltatech_service_agreement`.
Valoarea de afaceri constă în registrul unic de echipamente și contoare pe care se construiește
facturarea pe consum a suitei de service.

#### 2. Funcționalități Cheie

- Gestiunea locurilor funcționale la client (sediu, punct de lucru), cu client, persoană de contact,
  adresă și tehnician responsabil.
- Gestiunea echipamentelor: tip, model, producător, serie, număr de inventar, tip de proprietate,
  stare (Activ, Defect, În reparație, Casat, Rezervat, Pierdut); alegerea *Locului funcțional*
  completează automat clientul, contactul și responsabilul.
- Legătura echipamentului cu un produs stocabil și cu numărul de serie/lot din stoc, cu
  trasabilitatea mișcărilor și locul de depozitare al seriei.
- Gestiunea contoarelor, fiecare pe o unitate de măsură proprie (un echipament nu poate avea două
  contoare cu aceeași unitate), plus contoare colector care adună mai multe contoare fără să fie ele
  însele citite.
- Gestiunea citirilor de contor, cu diferența calculată automat față de citirea anterioară (sau față
  de valoarea inițială, la prima citire), actualizată la editarea sau ștergerea citirilor. Mai multe
  citiri ale aceluiași contor în aceeași zi sunt înlănțuite în ordinea introducerii (fără diferențe
  negative), iar ștergerea unei citiri actualizează valoarea anterioară și diferența citirii
  următoare. Asistentul *Introducere citiri contoare* (`service.enter.reading`) propune data de azi,
  în fusul orar al utilizatorului.
- Contoarele colector însumează totalurile contoarelor lor, și atunci când un contor nu are încă
  citiri, și se actualizează la adăugarea, modificarea sau ștergerea unei citiri.
- Calculul estimării: butonul **Calculează estimarea** pe contor determină coeficienții unei drepte
  de regresie din citirile reale și afișează valoarea prognozată pentru data curentă; **Recalculează
  valorile** reface valoarea anterioară și diferența tuturor citirilor, în ordinea datelor — necesar
  după o citire introdusă cu dată în trecut, care altfel lasă consumul umflat.
- Tipuri de echipament cu șabloane de piese, verificări și măsurători (copiate automat la
  alegerea *Tipului*, doar în listele goale, deci ajustările făcute pe echipament nu se rescriu;
  butonul **Preia operațiunile din șablon**, cu confirmare, le înlocuiește deliberat); șabloanele de **contoare** de pe tip nu creează contoare
  în acest modul — sunt ignorate de `deltatech_service_equipment`, care le ia din categoria de
  echipament aleasă pe tip.
- Acces: utilizatorii de serviciu pot citi modelele, piesele, verificările și măsurătorile
  echipamentelor și pot bifa liniile de operațiuni din formularul echipamentului (din 19.0.1.2.12);
  doar grupul **Serviciu / Manager** configurează tipurile și poate alege *Tipul* echipamentului
  (încarcă aceleași șabloane), deci un utilizator obișnuit poate crea echipamente doar fără *Tip*.
- Lista derulantă de echipamente afișează seria într-o a doua coloană estompată; numele simplu
  (`referință / serie`) folosit pe facturi și rapoarte rămâne neschimbat.

Fluxul complet de configurare și utilizare, tabelele de erori frecvente și limitările cunoscute sunt
în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_service_base](../deltatech_service_base/index.md)
- `product`
- `stock`

#### 4. Componente Cheie

Secțiune omisă: fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu
solicită explicit analiza componentelor tehnice; conform fluxului de ingestie, analiza codului pentru
această secțiune este omisă. Din manifest și cod: modele principale `service.equipment`,
`service.location`, `service.meter`, `service.meter.reading`, tipuri, modele și șabloane de
piese/verificări/măsurători (`service.equipment.type`, `service.part.template` etc.) și asistentul
`service.enter.reading`.

#### 5. Conexiuni

- [deltatech_service_base](../deltatech_service_base/index.md): modulul de bază al suitei de
  service, pe care se construiește gestiunea echipamentelor (meniu, grupuri, cicluri și perioade).
- [deltatech_service_equipment](../deltatech_service_equipment/index.md): extinde acest modul —
  creează contoarele din șabloanele categoriei de echipament și leagă echipamentele de contractele
  de service și de facturare.
- [deltatech_service_maintenance](../deltatech_service_maintenance/index.md): se construiește pe
  registrul de echipamente din acest modul.
- [deltatech_service_agreement](../deltatech_service_agreement/index.md): contractele de service și
  facturarea lor pe consum; legătura cu echipamentele e făcută de `deltatech_service_equipment`.
- [deltatech_service_consumable](../deltatech_service_consumable/index.md): raportul de eficiență al
  consumabilelor folosește consumul pe perioadă al contoarelor definite aici.
