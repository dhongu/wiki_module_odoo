# FAN Courier AWB for Odoo Online

- **Nume Tehnic:** `deltatech_delivery_fc_online`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_fc_online
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_fc_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

AWB, etichetă, anulare și urmărire FAN Courier direct din livrare, inclusiv pe Odoo Online: modulul nu are cod Python și se importă ca zip, împreună cu `deltatech_delivery_online` și `deltatech_iap_online`; apelurile către FAN Courier le face serverul Terrabit. Este ascuns în Odoo Apps, în stadiul Alpha, și exclude `deltatech_delivery_fc`.

#### 2. Funcționalități Cheie

- Serviciul **FAN Courier**, gata de activat, cu setările FAN: tip serviciu (Standard), plătitor, dimensiune etichetă (A4, A5, A6), livrare sâmbătă, ePOD, colet deschis, SMS către destinatar.
- Metoda de livrare **FAN Courier** deja legată de serviciu și de pagina de urmărire (preț fix 0, de stabilit).
- Contractul propriu FAN Courier: AWB-urile se creează pe contul selfAWB (utilizator, parolă, client ID), trimis o dată din butonul *Courier Account* (doar administratori); FAN facturează expedierile ca înainte.
- Refuzul FAN (localitate necunoscută, date lipsă) se postează pe livrare cu mesajul FAN și nu se taxează.
- Credite: 0,001 credite Terrabit per AWB nou; primul credit (1000 AWB) este gratuit.
- Pași: import zip, *Settings > Technical > Terrabit Services > Services* → **FAN Courier** → **Activate**, apoi cont de curier și preț pe metoda de livrare; restul fluxului e cel din `deltatech_delivery_online` (vezi fișa consultant).

#### 3. Dependențe

- [deltatech_delivery_online](../deltatech_delivery_online/index.md)

#### 4. Componente Cheie

**Modele**

- Fără cod Python. Datele creează înregistrarea `x_iap_online_service` pentru FAN Courier (`iap_online_service_fan_courier`), produsul de livrare `product_fan_courier` și metoda `delivery_carrier_fan_courier`.

**Vizualizări**

- Nu adaugă vizualizări; folosește cele din `deltatech_delivery_online`.

**Acțiuni Automate / Acțiuni Server**

- Nu definește; urmărirea rulează prin cronul din `deltatech_delivery_online`.

#### 5. Conexiuni

- [deltatech_delivery_fc](../deltatech_delivery_fc/index.md): varianta clasică FAN Courier, cu care acest modul nu poate fi folosit împreună (`excludes`).
- [deltatech_delivery_sd_online](../deltatech_delivery_sd_online/index.md): același mecanism, pentru Sameday.
- `deltatech_iap_online`: serviciile și creditele Terrabit.
