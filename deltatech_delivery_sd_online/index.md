# Sameday AWB for Odoo Online

- **Nume Tehnic:** `deltatech_delivery_sd_online`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_sd_online
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_sd_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

AWB, etichetă, anulare și urmărire Sameday direct din livrare, inclusiv pe Odoo Online: modulul nu are cod Python și se importă ca zip, cu `deltatech_delivery_online` și `deltatech_iap_online`; apelurile către Sameday le face serverul Terrabit. Este ascuns în Odoo Apps, în stadiul Alpha, și exclude `deltatech_delivery_sd`.

#### 2. Funcționalități Cheie

- Serviciul **Sameday**, gata de activat: livrare la domiciliu cu serviciul implicit al contului (de regulă Nextday 24H) sau alt serviciu după id/nume; etichetă A4 sau A6; colet deschis la livrare.
- Metoda de livrare **Sameday** legată de serviciu și de pagina de urmărire (preț fix 0, de stabilit).
- Contractul propriu Sameday: AWB-urile se creează pe contul API (utilizator și parolă, *Courier Client ID* rămâne gol), trimis o dată din *Courier Account* (doar administratori). Coletele pleacă din punctul de ridicare implicit al contului; județul și localitatea se potrivesc după nume cu lista Sameday.
- Ramburs încasat de Sameday și plătit conform contractului.
- Opțiuni în secțiunea **Courier**: *Courier Service Type* (gol sau id/nume, ex. `7` sau `24H`), *Shipping Paid By* (doar *Sender*), *Label Size* (A5 se tipărește ca A6), *Open Package at Delivery* (serviciul contului trebuie să aibă taxa OPCG); sâmbăta, ePOD și SMS nu sunt folosite.
- Refuzul Sameday se postează în chatter după *Courier:*, fără AWB și fără taxare. O livrare retrimisă după anulare primește referință nouă.
- Credite: 0,01 credite Terrabit per AWB (1 credit = 1 EUR); 5 credite de probă (500 AWB).
- Nu include: livrare la lockere easybox și Sameday Points, expedieri plătite de destinatar. Import oprit cât timp `deltatech_delivery_sd` e instalat. Flux: vezi fișa consultant.

#### 3. Dependențe

- [deltatech_delivery_online](../deltatech_delivery_online/index.md)

#### 4. Componente Cheie

**Modele**

- Fără cod Python. Datele creează serviciul `x_iap_online_service` Sameday (`iap_online_service_sameday`), produsul `product_sameday` și metoda de livrare `delivery_carrier_sameday`.

**Vizualizări**

- Nu adaugă vizualizări; folosește cele din `deltatech_delivery_online`.

**Acțiuni Automate / Acțiuni Server**

- Nu definește; urmărirea rulează prin cronul din `deltatech_delivery_online`.

#### 5. Conexiuni

- [deltatech_delivery_sd](../deltatech_delivery_sd/index.md): varianta clasică Sameday, incompatibilă cu acest modul (`excludes`).
- [deltatech_delivery_fc_online](../deltatech_delivery_fc_online/index.md): același mecanism, pentru FAN Courier.
- `deltatech_iap_online`: serviciile și creditele Terrabit.
