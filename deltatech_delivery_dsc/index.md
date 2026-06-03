# DSC Shipping (localizat la `deltatech_delivery_dsc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dsc`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_dsc`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_dsc`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul integrează Odoo cu serviciul de curierat Dragon Star Curier (DSC), permițând expedierea coletelor și urmărirea lor online direct din platformă. Prin conectarea la API-ul curierului, utilizatorii pot genera automat documentul de transport (AWB) pentru livrările lor, pot obține tarife estimative și pot gestiona opțiuni specifice de livrare (ramburs, asigurare, livrare sâmbăta etc.), eliminând astfel pașii manuali din procesul de expediere.

#### 2. Funcționalități Cheie

- Generarea AWB-ului în format PDF
- Ștergerea unui AWB
- Obținerea tarifelor pentru o expediere
- Obținerea listei de orașe și a listei de județe
- Expediere cu mai multe colete
- Expediere cu valoare declarată (asigurare)
- Expediere cu plata ramburs (cash on delivery)
- Expediere cu nume de oraș fără id de oraș
- Opțiune pentru livrare sâmbăta
- Opțiune pentru colet deschis (open package)
- Obținerea listei de puncte de ridicare (pickup point)

Funcționalități neacoperite în versiunea curentă: generare AWB în format HTML sau ZPL, listă de lockere, istoricul stărilor unei expedieri, expediere cu id de oraș și id de județ, ridicare doar dintr-un anumit punct de ridicare, trimiterea id-ului de locker în AWB, notă de retur în AWB, expediere cu dimensiuni, opțiune de returnare colet și livrare personală în lockere.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `phonenumbers`.

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea de Componente Cheie a fost omisă deoarece există un fișier `readme/DESCRIPTION.md` care acoperă Sumarul și Funcționalitățile Cheie, iar acesta nu solicită explicit detalierea modelelor, vizualizărilor sau acțiunilor.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru gestiunea livrărilor pe care `deltatech_delivery_dsc` îl extinde cu integrarea curierului Dragon Star Curier.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): modul înrudit din suita de livrare, folosit pentru urmărirea stării expedierilor.
