# Sameday Shipping EasyBox (localizat la `deltatech_delivery_sd_easybox/index.md`)

- **Nume Tehnic:** `deltatech_delivery_sd_easybox`
- **Versiune:** `19.0.0.0.10`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_sd_easybox
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_sd_easybox`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul adaugă livrarea către lockerele Easybox ale curierului Sameday în magazinul online. Practic, extinde integrarea de bază Sameday astfel încât, la finalizarea comenzii, cumpărătorul să poată alege ca punct de livrare un automat de tip Easybox în loc de o adresă clasică. Modulul aduce și clase CSS pentru a personaliza butoanele de selectare a adresei de livrare și a metodei de curierat în pagina de checkout, oferind o experiență vizuală adaptată magazinului.

#### 2. Funcționalități Cheie

- Plugin Easybox pentru integrarea Sameday, care permite alegerea unui locker Easybox ca punct de livrare în comerțul online.
- Clase CSS pentru personalizarea butoanelor de selectare a adresei de livrare: `.select-button-carrier`, `.select-button-easybox`.
- Clasă CSS pentru butonul de adăugare a adresei: `.add-delivery-button`.
- Pentru ca un produs să fie disponibil pentru livrare la Easybox, trebuie bifată o opțiune specifică pe produs.

#### 3. Dependențe

- [deltatech_delivery_sd](../deltatech_delivery_sd/index.md): integrarea de bază Sameday.
- [deltatech_delivery_locker_website](../deltatech_delivery_locker_website/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunea de componente nu a fost detaliată din cod, deoarece `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie, iar acesta nu solicită explicit analiza modelelor, vizualizărilor sau acțiunilor.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): cadrul general de livrare peste care se construiește integrarea Sameday Easybox.
- [deltatech_delivery_status](../deltatech_delivery_status/index.md): urmărirea stării livrărilor, relevantă pentru comenzile expediate prin Sameday.
- [deltatech_delivery_locker](../deltatech_delivery_locker/index.md): suportul generic pentru livrarea la lockere/puncte de ridicare, din care face parte cazul specific Easybox.

---

> **Avertisment:** Modul în stadiul `Beta`; nu a fost testat pe un sistem de producție (conform `readme/DESCRIPTION.md`).
