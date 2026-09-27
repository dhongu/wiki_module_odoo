# Dummy Shipping (localizat la `deltatech_delivery_dummy/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dummy`
- **Versiune:** `20.0.0.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_dummy
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dummy`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Acest modul introduce o metodă de livrare „fictivă" (dummy) în sistemul de livrare al Odoo, utilă pentru testarea și validarea fluxurilor de comandă și expediere fără a apela un curier real. Este util în special în perioadele de implementare și testare a unor canale noi de e-commerce sau fluxuri logistice, permițând simularea realistă a ciclului complet al unei comenzi fără costuri sau riscuri asociate integrărilor live cu curieri.

#### 2. Funcționalități Cheie

- Testare simplificată a fluxului: permite parcurgerea completă a procesului de finalizare comandă (checkout) și livrare fără a declanșa apeluri reale către API-uri de curierat.
- Flexibilitate operațională: oferă o metodă de livrare de tip „placeholder" pentru livrări interne sau scenarii speciale de fulfillment.
- Prototipare rapidă: accelerează implementarea și validarea customizărilor legate de livrare într-un mediu simulat, sigur.
- Cost redus de testare: elimină cheltuielile legate de utilizarea API-urilor de curierat sau generarea accidentală de etichete de expediere în timpul dezvoltării.
- Fiabilitate crescută: permite validarea completă a logicii de livrare înainte de trecerea la un furnizor real de curierat.
- Tarifare fixă la zero: metoda de livrare „dummy" returnează întotdeauna un preț de transport de 0.0, fără taxă suplimentară pentru client.
- Generare etichetă de livrare: la trimiterea coletului (`carrier_generate_label`), sistemul generează automat o etichetă PDF simplă (raportul `Delivery Dummy`) și o atașează la ridicare (`stock.picking`), iar numărul de urmărire (`carrier_tracking_ref`) este preluat din numele comenzii de vânzare sau al ridicării.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extindere): adaugă opțiunea `dummy` la selecția `delivery_type` și implementează metodele `dummy_rate_shipment` (calculează costul de transport, mereu 0.0) și `dummy_send_shipping` (simulează trimiterea coletelor, generând un răspuns cu numărul de urmărire preluat din comanda de vânzare sau din ridicare).
- `stock.picking` (extindere): suprascrie `carrier_generate_label` pentru a genera și atașa eticheta PDF a raportului „Delivery Dummy" atunci când metoda de livrare a ridicării este de tip `dummy`, folosind conținutul binar brut (bytes) specific Odoo 20.

**Vizualizări**

- `report_delivery_dummy`: șablon QWeb minimal pentru eticheta de livrare, afișând numele transportatorului pe fiecare pagină a raportului.
- `action_report_delivery_dummy`: acțiunea de raport (`ir.actions.report`) de tip `qweb-pdf`, legată de modelul `stock.picking`, care generează eticheta PDF „Delivery Dummy".

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază al livrării Terrabit, extins cu tipul de transportator `dummy`.
