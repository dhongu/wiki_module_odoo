# DSC Shipping (localizat la `deltatech_delivery_dsc/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dsc`
- **Versiune:** `19.0.1.2.2`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dsc`
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dsc`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul integrează Odoo cu serviciul de curierat Dragon Star Curier (DSC), permițând expedierea coletelor și urmărirea lor online direct din platformă. Prin conectarea la API-ul curierului, utilizatorii pot genera automat documentul de transport (AWB) pentru livrările lor, pot obține tarife estimative, pot organiza ridicarea coletelor de la mai multe puncte de lucru și pot urmări starea expedierilor, eliminând astfel pașii manuali din procesul de expediere.

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
- Suport pentru mai multe puncte de lucru (pcId)
- Obținerea ultimei stări (status) pentru o expediere
- Crearea comenzii de ridicare (cerere de colectare de către curier)
- Crearea borderoului (rezumatul expedierilor de sfârșit de zi)
- Link de urmărire (tracking) pentru expediere

Funcționalități neacoperite în versiunea curentă: obținerea istoricului complet al stărilor unei expedieri, obținerea stării AWB-ului de retur, tipărirea borderoului în format PDF, expediere cu dimensiuni (lungime, lățime, înălțime), opțiune de returnare colet și notă de restituire în AWB.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

Dependență externă Python: `phonenumbers`.

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea de Componente Cheie a fost omisă deoarece există un fișier `readme/DESCRIPTION.md` care acoperă Sumarul și Funcționalitățile Cheie, iar acesta nu solicită explicit detalierea modelelor, vizualizărilor sau acțiunilor.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru gestiunea livrărilor pe care `deltatech_delivery_dsc` îl extinde cu integrarea curierului Dragon Star Curier.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): modul înrudit din suita de livrare, folosit pentru urmărirea stării expedierilor.
