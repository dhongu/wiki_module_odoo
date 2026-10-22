# DPD Romania Shipping (localizat la `deltatech_delivery_dpd/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dpd`
- **Versiune:** `19.0.0.6.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dpd
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dpd`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul DPD Romania Shipping permite expedierea cu DPD Romania direct din livrările Odoo: costul de transport pe comanda de vânzare, AWB-ul și eticheta lui, urmărirea și anularea expedierii, toate prin API-ul DPD, fără reintroducerea datelor în portalul curierului. Se construiește peste modulul Deltatech Delivery și reduce munca manuală și erorile la pregătirea coletelor.

#### 2. Funcționalități Cheie

- **Tarife pe comanda de vânzare**: costul de transport este calculat de DPD pentru serviciul metodei de livrare sau se folosește un preț fix, cu un prag opțional peste care se interoghează DPD.
- **AWB și etichetă**: AWB-ul se emite din comanda de livrare (**Detalii curier**, apoi validarea transferului), cu etichetă PDF sau ZPL, în format A4, A6 sau patru etichete A6 pe pagină A4; butoanele **Print AWB** și **Cancel AWB** tipăresc eticheta și anulează expedierea la DPD.
- **Servicii**: serviciile contului DPD (DPD Standard, Clasic național, Pallet one RO și celelalte active pe contract) se importă cu butonul **Initialization** (care aduce și clientul DPD al contului ca punct de ridicare), iar un serviciu se alege pentru fiecare metodă de livrare.
- **Opțiuni de expediere**: mai multe colete, valoare declarată, ramburs (cu metodele de plată tratate ca ramburs configurabile), deschidere colet înainte de plată, retur colet (swap) și plătitorul transportului: expeditor, destinatar sau terț.
- **Localități pentru toată Europa**: butonul **Get city** importă localitățile DPD pentru țările europene deservite și le mapează pe agenda de adrese Odoo; o localitate fără corespondent rămâne cu județul „de mapat".
- **Urmărire**: istoricul de stări se citește de la DPD și se scrie pe livrare; starea livrării urmează codurile de operațiune DPD (ridicat, în livrare, livrat, refuzat), iar linkul de tracking deschide expedierea pe site-ul DPD.
- **Reîncercări sigure**: un răspuns pierdut la emiterea sau anularea unui AWB este raportat ca rezultat incert, deci o nouă apăsare a butonului nu emite un al doilea AWB.
- **Date trimise către DPD**: nume, adresă, telefon și e-mail destinatar; firma, contactul și adresa expeditorului (sau id-ul de client DPD); numărul de colete și greutatea totală; valoarea declarată, suma de ramburs, referința comenzii și nota de livrare.
- **Atenție la mediul de test**: DPD publică o singură adresă API, deci comutarea metodei pe „Test Environment" nu ferește apelurile de contul real; doar credențialele diferă.
- **Neacoperit**: lockere și puncte de ridicare DPD, etichete HTML, dimensiunile coletelor și nota de restituire pe AWB.

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Secțiunea este omisă conform fluxului de ingestie: `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar componentele tehnice nu sunt cerute explicit.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru curierat peste care se construiește integrarea DPD; furnizează modelul și fluxul generic de livrare.
