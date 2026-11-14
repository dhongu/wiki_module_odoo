# FAN Courier AWB for Odoo Online (localizat la `deltatech_delivery_fc_online/index.md`)

- **Nume Tehnic:** `deltatech_delivery_fc_online`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_fc_online
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_fc_online`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite generarea AWB-ului FAN Courier, tipărirea etichetei, anularea și urmărirea coletului direct din livrare, inclusiv în Odoo Online. Nu conține cod Python și se importă ca arhivă zip, împreună cu `deltatech_delivery_online` și [deltatech_iap_online](../deltatech_iap_online/index.md). Apelurile către FAN Courier sunt făcute de serverul Terrabit, iar expedierile se facturează în continuare direct de FAN Courier, pe contractul clientului.

#### 2. Funcționalități Cheie

- **Serviciul FAN Courier**, gata de activat, cu setările FAN: tip serviciu (Standard), plătitor, dimensiunea etichetei (A4, A5, A6), livrare sâmbăta, ePOD, deschidere colet, SMS către destinatar. Se activează din *Setări > Tehnic > Servicii Terrabit > Servicii* (mod dezvoltator), prin butonul **Activate**.
- **Metodă de livrare FAN Courier**, deja legată de serviciu și de pagina de urmărire FAN Courier (preț fix 0, de stabilit în *Inventar > Configurare > Livrare > Metode de livrare*).
- **Contul de curier propriu**: AWB-urile se creează pe contul selfAWB al clientului (utilizator, parolă, ID client), trimis o singură dată către serverul Terrabit prin butonul **Courier Account** din serviciu (doar administratori). Parola se golește după trimitere, iar câmpul *Courier Account Accepted On* arată când a fost acceptat contul. Se recomandă un utilizator API separat.
- **AWB din livrare**: butonul **AWB** pe transferul cu metoda FAN Courier scrie AWB-ul în referința de urmărire și atașează eticheta; butonul **Tracking** deschide pagina FAN Courier a AWB-ului.
- **Refuzul FAN Courier** (localitate necunoscută, date lipsă) se postează în chatter cu câmpul și mesajul FAN Courier și nu se taxează; după corectarea adresei se apasă din nou **AWB**.
- **Credite**: 0,001 credite Terrabit per AWB nou; primul credit (1000 AWB-uri) este gratuit.

Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `deltatech_delivery_online`

Modulul exclude `deltatech_delivery_fc` (varianta clasică, nu rulează împreună cu aceasta).

#### 4. Componente Cheie

**Modele**

- Fără modele Python proprii. Datele creează un serviciu `x_iap_online_service` (cod `fan_courier_online`, server `https://terrabit.odoo.com`, acțiune de aplicare `deltatech_delivery_online.action_awb_apply`), un produs serviciu `FAN Courier` și o metodă `delivery.carrier` de tip preț fix legată de serviciu.

**Vizualizări**

- Fără vizualizări proprii; se folosesc cele din `deltatech_delivery_online`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): serviciile Terrabit, creditele și contul de curier, necesare funcționării modulului.
- [deltatech_delivery_fc](../deltatech_delivery_fc/index.md): varianta FAN Courier pentru Odoo clasic (incompatibilă, se exclud reciproc).
- `deltatech_delivery_online`: modulul de bază pentru livrare prin serviciile Terrabit (fără pagină wiki încă).
