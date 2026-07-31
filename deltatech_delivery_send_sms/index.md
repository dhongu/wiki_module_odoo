# Deltatech Delivery Send SMS (localizat la `deltatech_delivery_send_sms/index.md`)

- **Nume Tehnic:** `deltatech_delivery_send_sms`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_delivery_send_sms
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_send_sms`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul optimizează experiența clientului și transparența livrării prin trimiterea automată de notificări SMS atunci când eticheta de transport (AWB) este generată sau când coletul este preluat de curier. Din perspectivă de business, aceste actualizări instant pe mobil reduc semnificativ întrebările de tip „Unde este comanda mea?”, deoarece clienții primesc actualizări de stare în timp real direct pe telefon.

#### 2. Funcționalități Cheie

- Comunicare imediată cu clientul: trimite actualizări SMS instant despre starea livrării, pentru vizibilitate maximă.
- Reducerea solicitărilor de suport: minimizează volumul de muncă manuală al echipei de suport prin automatizarea notificărilor privind progresul expedierii.
- Consolidarea încrederii în brand: construiește încrederea clientului printr-o comunicare consecventă și profesională pe tot parcursul ciclului de onorare a comenzii.
- Îmbunătățirea ratei de livrare cu succes: asigură că fiecare client știe momentul exact în care coletul a pornit la drum, reducând tentativele de livrare eșuate.
- Suport logistic scalabil: gestionează automat notificările SMS pentru un volum mare de comenzi, fără intervenție manuală.

#### 3. Dependențe

- `delivery`
- `sms`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie de mai sus provin din `readme/DESCRIPTION.md`, prin urmare analiza detaliată a codului pentru componente nu a fost solicitată de Readme și a fost omisă conform fluxului de ingestie.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionează stările de livrare (AWB creat / preluat) pe care acest modul le folosește ca declanșator pentru trimiterea SMS-urilor.
- [deltatech_delivery_relay](../deltatech_delivery_relay/index.md): face parte din aceeași suită de gestionare a livrărilor și curierilor.
- [deltatech_delivery](../deltatech_delivery/index.md): modul de bază al suitei de livrare din care derivă funcționalitatea de notificare.
