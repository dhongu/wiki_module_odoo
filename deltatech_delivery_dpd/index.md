# DPD Romania Shipping (localizat la `deltatech_delivery_dpd/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dpd`
- **Versiune:** `20.0.0.8.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_dpd
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dpd`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul DPD Romania Shipping integrează Odoo cu serviciul de curierat DPD, automatizând expedierile direct din ERP: calculul tarifelor, generarea etichetelor (AWB), urmărirea coletelor și gestionarea livrărilor, fără introducere manuală a datelor. Din contul DPD România se importă localitățile tuturor țărilor europene deservite de DPD, deci expedierile externe se adresează ca cele interne. Se construiește peste modulul de bază Deltatech Delivery.

#### 2. Funcționalități Cheie

- **Servicii DPD**: import automat al serviciilor din contract (DPD Standard, DPD International etc.) și al **DPD Client IDs** prin butonul **Initialization**; autentificare cu **User** și **Password**.
- **AWB**: etichete PDF sau ZPL, formate A4, A6, A4_4xA6; **Contents** (implicit „Marfa", maximum 100 de caractere) și **Shipment Payer** (Sender, Recipient, Third Party); **Print AWB** cere eticheta din nou dacă livrarea nu o are; AWB-ul se salvează înainte de cererea etichetei, deci rămâne valid chiar dacă eticheta nu poate fi obținută; **Cancel AWB** anulează expedierea la DPD.
- **Tarife**: pe comanda de vânzare, **Shipping** > **Get rate** > **Add**; un preț fix fără prag ocolește DPD, iar cu prag înlocuiește prețul DPD mai mic decât pragul.
- **Localități**: **Get city** importă localitățile DPD pentru țările europene și le potrivește cu orașele Odoo; butonul **To map** arată localitățile încă nepotrivite.
- **Locații de ridicare**: tab-ul **Pickup Location**, cu sursa *From Carrier*, depozitul livrării sau compania; **Ref** al adresei este client id-ul DPD trimis ca expeditor.
- **Urmărire**: link de tracking, istoric în tab-ul **History** (**Refresh**), o acțiune programată citește starea coletului, iar **Delivery State** o urmează.
- **Opțiuni de expediere**: ramburs, valoare declarată (asigurare), colete multiple, pachet deschis, livrare sâmbăta.
- **Retururi**: pe o recepție cu metoda DPD părțile se inversează (clientul expeditor, compania destinatar); cu **Shipment Payer** *Third Party* plătește tot compania.
- **Atenție**: DPD publică o singură adresă API; comutarea metodei pe *Test Environment* nu ferește apelurile de contul real, doar credențialele.
- **Neacoperit**: AWB în format HTML, listă de lockere și de puncte de ridicare, expediere cu dimensiuni, notă de restituire, id de locker în AWB, restricționare la un singur punct de ridicare. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea „Componente Cheie" este omisă: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar componentele tehnice nu sunt cerute explicit în Readme.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru curierat peste care se construiește integrarea DPD; furnizează modelul și fluxul generic de livrare.
