# IAP Services for Odoo Online (localizat la `deltatech_iap_online/index.md`)

- **Nume Tehnic:** `deltatech_iap_online`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_iap_online
- **Cale Locală:** `odoo-addons/deltatech/deltatech_iap_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Baza serviciilor Terrabit pentru **Odoo Online**. Modulele de servicii (doar date, fără Python, importate ca arhivă zip) trimit cererile către un server Terrabit, care face munca grea și scrie răspunsul înapoi în baza de date. Acest modul conține ce au în comun toate aceste servicii: activarea, creditele, urmărirea cererilor și consumul. Fiecare modul de serviciu adaugă doar propriile câmpuri, butoane și modul de scriere a răspunsului. Starea de dezvoltare este Alpha.

#### 2. Funcționalități Cheie

- **Un cont pe serviciu**: *Setări > Terrabit Credits > Services and Credits* listează serviciile instalate și creditele rămase (în mod dezvoltator și la *Setări > Technical > Terrabit Services*).
- **Activare dintr-un clic**: butonul **Activate** înregistrează baza de date la serverul Terrabit. Tokenul contului revine automat, împreună cu creditele de probă. Nu se copiază nimic manual. După activare apar **Activate Again**, **Refresh Credits** și **Buy Credits**.
- **Cumpărare și verificare credite**: **Buy Credits** deschide, într-o filă nouă, pagina de credite a contului pe serverul Terrabit. **Refresh Credits** cere soldul, care se actualizează și cu fiecare răspuns.
- **Consum de credite**: *Settings > Terrabit Credits > Credit Usage* listează fiecare răspuns taxat, cu creditele consumate și cele rămase după el, cu total, grafic și pivot pe serviciu și lună. Filtrul **Charged** e implicit; 1 credit = 1 EUR. Activările, reîmprospătările și cererile refuzate nu costă și nu apar. Butonul **Credit Usage** de pe serviciu deschide consumul acelui serviciu. Cererile răspunse înainte de versiunea 19.0.1.1.0 nu au cost.
- **Cereri urmăribile**: *Terrabit Services > Requests* arată fiecare cerere, starea și eroarea (filtre **Errors** și **Waiting**; erorile sunt roșii, cele în așteptare albastre). O cerere fără răspuns după 10 minute este retrimisă o singură dată.
- **Răspunsuri sigure**: răspunsul vine pe o automatizare *On webhook*, cu URL secret, care acceptă doar o cerere aflată în așteptare, identificată prin token.
- **Secrete rezervate administratorilor**: tokenul contului și URL-ul de callback sunt citite doar de administratori. Ceilalți utilizatori pot crea cereri, dar nu le pot citi. Doar administratorii activează un serviciu.
- **Ce pleacă din baza de date**: datele de intrare ale cererii, tokenul, adresa și UUID-ul bazei de date (pentru răspuns) și, la activare, numele și CUI-ul companiei.
- **Pentru dezvoltatori**: un modul de serviciu creează o înregistrare `x_iap_online_service` (`x_code`, `x_server`) și, opțional, o acțiune server *apply* (`x_apply_action_id`) care primește răspunsul în cheia de context `iap_answer`. Documentele lui creează `x_iap_online_request` cu `x_kind = 'request'`.

Fluxul pas cu pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_automation`

#### 4. Componente Cheie

**Modele**

Modele create din date (`ir.model`, prefix `x_`, fără cod Python, deci importabile pe Odoo Online):

- `x_iap_online_service`: serviciul Terrabit instalat, cu cod, URL server, token, sold de credite, acțiune de trimitere și acțiune de aplicare a răspunsului.
- `x_iap_online_request`: cererea trimisă serverului, cu tip, stare, intrare, rezultat, eroare, documentul sursă (model și ID), tokenul, URL-ul de callback, UUID-ul bazei, costul și soldul după cerere.

**Vizualizări**

- `views/x_iap_online_views.xml`: listă și formular pentru servicii (cu butonul Credit Usage), listă și formular numai-citire pentru cereri, listă/grafic/pivot pentru consumul de credite, meniul *Terrabit Credits*.

**Acțiuni Automate / Acțiuni Server**

- `action_iap_online_activate`, `action_iap_online_balance`, `action_iap_online_buy`: butoanele Activate, Refresh Credits și Buy Credits.
- `automation_iap_online_request_create` (acțiune `action_iap_online_prepare`): pregătește cererea nou creată și o trimite serverului.
- `automation_iap_online_callback` (*On webhook*, acțiune `action_iap_online_callback`): primește răspunsul, actualizează cererea, soldul și costul și apelează acțiunea *apply* a serviciului.
- `automation_iap_online_retry` (acțiune `action_iap_online_retry`): retrimite o singură dată cererea fără răspuns după 10 minute.

#### 5. Conexiuni

- `l10n_ro_anaf_partner_online`: exemplu de modul de serviciu care creează înregistrarea serviciului (necesită instalare împreună cu acest modul).
