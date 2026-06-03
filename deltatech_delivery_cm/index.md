# Courier Manager Shipping (localizat la `deltatech_delivery_cm/index.md`)

- **Nume Tehnic:** `deltatech_delivery_cm`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_cm
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_cm`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul integrează Odoo cu platforma de curierat Courier Manager, permițând trimiterea coletelor printr-un singur transportator și urmărirea lor online. Pe baza unui document de livrare, modulul generează automat AWB-ul (scrisoarea de transport) și sincronizează informațiile cu Courier Manager, astfel încât echipele de logistică pot expedia comenzile și pot vedea evoluția livrării direct din Odoo, fără a folosi o aplicație externă.

#### 2. Funcționalități Cheie

- Generarea AWB în format PDF
- Generarea AWB în format ZPL (pentru imprimante de etichete)
- Ștergerea unui AWB
- Obținerea tarifelor pentru o expediere
- Obținerea listei de orașe și a listei de județe
- Urmărirea istoricului de statusuri pentru o expediere
- Expediere cu mai multe colete
- Expediere cu valoare declarată (asigurare)
- Expediere cu ramburs (cash on delivery)
- Expediere cu identificator de oraș și de județ (city id / county id)
- Expediere doar cu nume de oraș, fără identificator de oraș

Funcționalități neacoperite (limitări cunoscute):

- Generarea AWB în format HTML
- Obținerea listei de lockere sau a punctelor de ridicare (pickup point)
- Expediere cu dimensiuni
- Nota de retur în AWB
- Opțiunea de livrare sâmbăta
- Opțiunea de colet deschis
- Restricționarea ridicării doar dintr-un anumit pickup point id
- Transmiterea unui locker id în AWB

#### 3. Dependențe

- `delivery`
- `mail`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

> Conform fluxului de ingestie, secțiunea Componente Cheie este omisă deoarece modulul conține un fișier `readme/DESCRIPTION.md`, iar acesta nu solicită explicit analiza componentelor tehnice.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru transportatori și AWB pe care acest modul îl extinde pentru integrarea cu Courier Manager.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionarea statusurilor de livrare, complementară urmăririi istoricului de statusuri al expedierilor Courier Manager.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): suport pentru livrarea la lockere; relevant ca parte a ecosistemului de livrare (notă: lockerele nu sunt acoperite de acest modul, vezi limitările).
