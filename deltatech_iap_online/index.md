# IAP Services for Odoo Online (localizat la `deltatech_iap_online/index.md`)

- **Nume Tehnic:** `deltatech_iap_online`
- **Versiune:** `20.0.1.2.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_iap_online
- **Cale Locală:** `odoo-addons/deltatech/deltatech_iap_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Baza serviciilor Terrabit pentru **Odoo Online**: modulele de servicii fără cod Python (importate ca arhivă zip) trimit cererile către un server Terrabit, care face munca grea și scrie răspunsul înapoi în baza de date. Acest modul conține ce au în comun toate serviciile: activarea, creditele, urmărirea cererilor și consumul de credite. Fiecare modul de serviciu adaugă doar câmpurile și butoanele proprii.

#### 2. Funcționalități Cheie

- **Un cont pentru fiecare serviciu**: *Setări > Credite Terrabit > Servicii și credite* listează serviciile instalate, cu creditele rămase (în modul dezvoltator și sub *Setări > Tehnic > Servicii Terrabit*).
- **Activare dintr-un clic**: butonul **Activează** înregistrează baza de date la serverul Terrabit; tokenul contului revine automat, împreună cu creditele de probă ale serviciului.
- **Cumpărare și verificare credite**: **Cumpără credite** deschide pagina de credite a contului de pe serverul Terrabit; **Actualizează creditele** cere creditele rămase, care se actualizează și cu fiecare răspuns.
- **Consum de credite**: *Setări > Credite Terrabit > Consum credite* listează fiecare răspuns taxat, cu creditele folosite și cele rămase după el, cu total, grafic și pivot pe serviciu și lună; 1 credit = 1 EUR. Cererile răspunse înainte de versiunea 20.0.1.1.0 nu au cost.
- **Cereri urmărite**: *Servicii Terrabit > Cereri* arată fiecare cerere, starea și eroarea; o cerere fără răspuns după 10 minute este retrimisă o singură dată.
- **Răspunsuri sigure**: răspunsul vine pe o automatizare *On webhook*, cu URL secret care acceptă doar o cerere încă în așteptare, identificată prin token.
- **Secrete rezervate administratorilor**: tokenul contului și URL-ul de callback sunt vizibile doar administratorilor; ceilalți utilizatori pot crea cereri, dar nu le pot citi, iar activarea e permisă doar administratorilor.
- **Ce pleacă din baza de date**: datele de intrare ale cererii, tokenul, adresa și UUID-ul bazei de date și, la activare, numele și codul fiscal al companiei.
- **Pentru dezvoltatori**: un modul de serviciu creează o înregistrare `x_iap_online_service` (`x_code`, `x_server`) și, opțional, o acțiune *apply* care primește răspunsul în cheia de context `iap_answer`; documentele creează `x_iap_online_request` cu `x_kind = 'request'`. O înregistrare creată cu `x_state = 'done'` nu se trimite, ci doar consemnează un cost raportat de server.
- Detaliile pas cu pas sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_automation`

#### 4. Componente Cheie

**Modele**

- `x_iap_online_service`: serviciul Terrabit (cod, server, token, credite rămase, acțiunile de trimitere și de aplicare a răspunsului); model Studio-style, creat din date.
- `x_iap_online_request`: cererea trimisă serverului, cu tip, stare, eroare, cost și credite rămase după ea.

**Vizualizări**

- `views/x_iap_online_views.xml`: listă și formular pentru servicii, listă și formular (doar citire) pentru cereri, listă, grafic și pivot pentru consumul de credite, plus meniurile *Credite Terrabit*.

**Acțiuni Automate / Acțiuni Server**

- `action_iap_online_activate`, `action_iap_online_balance`, `action_iap_online_buy`: butoanele **Activează**, **Actualizează creditele** și **Cumpără credite**.
- `automation_iap_online_callback`: automatizare *On webhook* care aplică răspunsul serverului.
- `automation_iap_online_request_create`: la crearea unei cereri, o pregătește și o trimite.
- `automation_iap_online_retry`: retrimite o cerere rămasă fără răspuns după 10 minute.

#### 5. Conexiuni

- `l10n_ro_anaf_partner_online`: exemplu de modul de serviciu care creează înregistrarea serviciului, folosit în fișa modulului.
