# Sameday AWB for Odoo Online (localizat la `deltatech_delivery_sd_online/index.md`)

- **Nume Tehnic:** `deltatech_delivery_sd_online`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_sd_online
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_sd_online`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul permite crearea AWB-urilor Sameday, tipărirea etichetei, anularea și urmărirea coletului direct din livrare, inclusiv pe Odoo Online. Nu conține cod Python: se importă ca arhivă zip, împreună cu `deltatech_delivery_online` și `deltatech_iap_online`, iar apelurile către Sameday sunt făcute de serverul Terrabit. AWB-urile se emit în contractul propriu Sameday al clientului, iar Sameday facturează expedierile ca până acum.

#### 2. Funcționalități Cheie

- **Serviciul Sameday**, gata de activat: livrare la domiciliu cu serviciul implicit al contului Sameday (de regulă Nextday 24H) sau alt serviciu al contului, indicat prin id sau nume; etichetă A4 sau A6; deschiderea coletului la livrare.
- **Metodă de livrare Sameday** deja legată de serviciu și de pagina de urmărire Sameday (preț fix 0, de stabilit).
- **Contractul propriu Sameday**: contul API (utilizator și parolă) se trimite o singură dată serverului Terrabit, din butonul *Courier Account* al serviciului (doar administratori); parola se golește după acceptare. Coletele pleacă din punctul de ridicare implicit al contului; județul și localitatea se potrivesc cu lista Sameday după nume.
- **Flux pe livrare** (fila *Additional Info*): se completează *Parcels*, *Declared Value*, *Cash on Delivery*, apoi butonul **AWB**; referința AWB ajunge în *Tracking Reference*, starea devine *Created*, iar eticheta se atașează în chatter. Sunt disponibile *Tracking*, *Refresh AWB Status*, *Print AWB Label* și *Cancel AWB*; după anulare, o nouă trimitere primește o referință Sameday nouă.
- **Setări serviciu** (secțiunea *Courier*): tipul serviciului (gol = implicit), plătitor transport (doar expeditorul), dimensiune etichetă (A4/A6; A5 se tipărește ca A6), deschidere colet la livrare (necesită opțiunea OPCG pe serviciul contului). Opțiunile livrare sâmbăta, confirmare electronică și SMS destinatar nu sunt folosite de Sameday.
- **Ramburs** încasat de Sameday și virat conform contractului clientului.
- **Refuzul Sameday** (adresă necunoscută, date lipsă) este postat în livrare cu mesajul Sameday, nu se taxează și AWB-ul se poate relua după corectare.
- **Credite**: 0,01 credite Terrabit per AWB nou (1 credit = 1 EUR); 5 credite de probă (500 AWB-uri).
- **Nu include**: livrarea în lockere easybox și Sameday Points, expedierile plătite de destinatar.
- **Incompatibil** cu `deltatech_delivery_sd` (fac aceleași AWB-uri); importul din zip se oprește cât timp acesta e instalat.

#### 3. Dependențe

- [deltatech_delivery_online](../deltatech_delivery_online/index.md)

#### 4. Componente Cheie

**Modele**

- Fără cod Python. Modulul livrează doar date pentru modele existente: `x_iap_online_service` (serviciul `sameday_online`, server `https://terrabit.odoo.com`), `delivery.carrier` (metoda Sameday, preț fix) și `product.product` (produsul-serviciu Sameday).

**Vizualizări**

- Fără vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Serviciul folosește acțiunea `deltatech_delivery_online.action_awb_apply` pentru emiterea AWB-ului. Fără cron-uri proprii.

#### 5. Conexiuni

- [deltatech_iap_online](../deltatech_iap_online/index.md): infrastructura de servicii Terrabit (activare, credite) pe care se sprijină serviciul Sameday; modelul `x_iap_online_service` provine de acolo.
- [deltatech_delivery_sd](../deltatech_delivery_sd/index.md): varianta clasică, cu apel direct la Sameday; exclusă reciproc (`excludes`), verificată și prin garda din datele modulului.
