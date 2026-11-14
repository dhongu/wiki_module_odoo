# Courier AWB for Odoo Online (localizat la `deltatech_delivery_online/index.md`)

- **Nume Tehnic:** `deltatech_delivery_online`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_online
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite generarea AWB-ului, tipărirea etichetei, anularea și urmărirea coletului direct din livrare, pentru curierii serviciului Terrabit, inclusiv pe Odoo Online. Nu conține cod Python și se importă ca arhivă zip, iar munca efectivă o face serverul Terrabit. Fiecare curier este un modul mic separat (primul: FAN Courier, `deltatech_delivery_fc_online`), iar butoanele și câmpurile sunt aceleași pentru toți.

#### 2. Funcționalități Cheie

- **Buton AWB** lângă referința de urmărire a livrării: AWB-ul se generează imediat, eticheta PDF se atașează livrării și se postează în chatter; dacă serviciul nu răspunde, AWB-ul intră la coadă, iar livrarea se actualizează după câteva secunde.
- **Acțiuni pe selecție de livrări:** *Generate AWB*, *Print AWB Label*, *Refresh AWB Status*, *Cancel AWB*; opțional, AWB-ul se creează la validarea livrării (*AWB on Validation*). *Generate AWB* pune la coadă un AWB per livrare și listează livrările omise.
- **Un singur AWB per livrare:** o livrare retrimisă primește același AWB, fără taxare repetată.
- **Urmărire:** la fiecare 30 de minute se reîmprospătează starea AWB-urilor nelivrate, pentru livrările validate în ultimele 30 de zile, ale unui serviciu activ (create, în tranzit, în depozit, în livrare, livrat), cu ultimul eveniment al curierului; primele sunt livrările verificate cel mai demult (*Last Courier Check*). Filtrul *AWB Not Delivered* și coloana opțională *AWB Status* ajută la listare.
- **Date per livrare** (tab *Additional Info*): număr de colete, ramburs, valoare declarată; greutatea e cea de expediere a livrării, expeditorul este adresa depozitului, destinatarul este partenerul.
- **Setări curier pe serviciu:** tip serviciu, cine plătește (expeditor/destinatar), format etichetă (A4/A5/A6), opțiuni (sâmbătă, ePOD, deschidere colet, SMS).
- **Contul de curier rămâne la Terrabit:** administratorul îl trimite o singură dată din butonul *Courier Account* al serviciului (utilizator, parolă, ID client); este verificat la curier și păstrat pe serverul Terrabit. Parola se golește din baza de date imediat după trimitere, iar contul e vizibil doar administratorilor. Data acceptării apare în *Courier Account Accepted On*.
- **Tokenul serviciului este citit de utilizatorii de stoc:** butonul AWB apelează serverul din browser pentru răspuns imediat; tokenul poate consuma credite, dar niciodată contul de curier (compromis asumat).
- **Refuzul curierului** (localitate necunoscută, date lipsă) apare ca avertisment cu câmpul și mesajul curierului și se postează în chatter; nu se scrie niciun AWB până la corectarea adresei.
- **Credite:** doar un AWB nou se taxează; eticheta, anularea și urmărirea sunt gratuite. Creditele se văd și se cumpără din *Settings > Technical > Terrabit Services*.
- **Nu funcționează pe Odoo Online:** prețul live în comandă sau coș (un tip nou de livrare cere Python); se folosește preț fix sau reguli de preț ale metodei de livrare.

#### 3. Dependențe

- `base_automation`
- [deltatech_iap_online](../deltatech_iap_online/index.md)
- `stock_delivery`

#### 4. Componente Cheie

**Modele**

Fără cod Python; modelele și câmpurile se declară prin date XML (importabile pe Odoo Online).

- `x_iap_online_courier_account`: cont de curier (trimis la serverul Terrabit), accesibil doar administratorilor.
- `delivery.carrier`: câmp adăugat `x_iap_online_service_id` (Terrabit Courier Service).
- `x_iap_online_service`: câmpuri adăugate `x_delivery_*` (serviciu, plătitor, format etichetă, sâmbătă, ePOD, deschidere colet, SMS, AWB automat).

**Vizualizări**

- `view_delivery_carrier_form`: câmpul serviciului de curier pe metoda de livrare.
- `view_x_iap_online_service_form`: setările de curier pe serviciu.
- `view_x_iap_online_courier_account_form`: dialogul de trimitere a contului de curier.
- Vizualizări pe `stock.picking` (buton AWB, câmpuri, filtru *AWB Not Delivered*), plus widgetul JS `awb_button_widget`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_awb_status`: „AWB: refresh the courier status”, la 30 de minute, pe `stock.picking`.
- Acțiuni server pentru generare, tipărire etichetă, anulare și reîmprospătare stare AWB (în `data/ir_actions_server_data.xml`).

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): serviciul Terrabit, tokenul și creditele pe care le folosește acest modul.
- `deltatech_delivery_fc_online`: modulul curierului FAN Courier, bazat pe acest modul.
