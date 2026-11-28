# Courier AWB for Odoo Online

- **Nume Tehnic:** `deltatech_delivery_online`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_online
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

AWB, etichetă, anulare și urmărire direct din livrare, pentru curierii serviciului Terrabit, inclusiv pe Odoo Online: modulul nu are cod Python și se importă ca zip, iar munca o face serverul Terrabit. Fiecare curier este un modul mic separat (primul: FAN Courier), iar butoanele și câmpurile sunt aceleași pentru toți. Modulul este ascuns în Odoo Apps și are stadiul Alpha.

#### 2. Funcționalități Cheie

- Buton **AWB** lângă referința de urmărire: AWB imediat, eticheta PDF atașată livrării și postată în chatter; fără răspuns de la serviciu, AWB-ul intră în coadă și livrarea se actualizează după câteva secunde.
- Acțiuni pe selecție de livrări: *Generate AWB*, *Print AWB Label*, *Refresh AWB Status*, *Cancel AWB*; opțional AWB la validarea livrării (*AWB on Validation*).
- Un singur AWB per livrare: o livrare retrimisă primește același AWB, netaxat din nou.
- Urmărire: la fiecare 30 de minute se reîmprospătează starea AWB-urilor nelivrate de pe livrările validate în ultimele 30 de zile ale unui serviciu activ, cu ultimul eveniment al curierului; filtrul *AWB Not Delivered*.
- Pe livrare: colete, ramburs, valoare declarată; greutatea este cea de expediere, expeditorul adresa depozitului, destinatarul partenerul.
- Contul de curier rămâne la Terrabit: administratorul îl trimite o dată din butonul *Courier Account* al serviciului; parola se golește din baza de date după trimitere, iar contul e citibil doar de administratori. Tokenul serviciului este citit de utilizatorii de stoc (compromis asumat pentru răspunsul imediat).
- Credite: doar AWB-ul nou se taxează; eticheta, anularea și urmărirea sunt gratuite; creditele se văd și se cumpără din *Settings > Technical > Terrabit Services*.
- Refuzul curierului (localitate necunoscută, date lipsă) apare ca avertisment și în chatter, fără AWB scris.
- Nu pe Odoo Online: prețul live în comandă/coș; se folosește preț fix sau reguli pe metoda de livrare. Flux pas cu pas: vezi fișa consultant.

#### 3. Dependențe

- `base_automation`
- `deltatech_iap_online`
- `stock_delivery`

#### 4. Componente Cheie

**Modele**

- `x_iap_online_service` (câmpuri `x_delivery_*` adăugate): setările de curier ale serviciului (tip serviciu, plătitor, format etichetă, sâmbătă, ePOD, colet deschis, SMS, AWB la validare).
- `x_iap_online_courier_account`: contul de curier trimis o dată serverului Terrabit.
- `delivery.carrier` (câmp `x_iap_online_service_id`) și `stock.picking` (câmpuri `x_awb_*`, ex. `x_awb_parcels`, `x_awb_cod`): extinse prin câmpuri personalizate.

**Vizualizări**

- `view_x_iap_online_service_form`, `view_x_iap_online_courier_account_form`: setările curierului și dialogul contului.
- `view_delivery_carrier_form`: câmpul Terrabit Courier Service pe metoda de livrare.
- `view_picking_form`, `view_picking_tree`, `view_picking_search`: butonul AWB, câmpurile și filtrul pe livrare; widget JS `awb_button_widget`.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_awb_status`: reîmprospătează statusul AWB-urilor (la 30 de minute).
- Acțiuni server pe selecție: generare AWB, tipărire etichetă, reîmprospătare status, anulare AWB.

#### 5. Conexiuni

- [deltatech_delivery_fc_online](../deltatech_delivery_fc_online/index.md): modulul de curier FAN Courier.
- [deltatech_delivery_sd_online](../deltatech_delivery_sd_online/index.md): modulul de curier Sameday.
- `deltatech_iap_online`: serviciile Terrabit, creditele și tokenul.
