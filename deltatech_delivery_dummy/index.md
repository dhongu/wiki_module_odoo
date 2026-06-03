# Dummy Shipping (localizat la `deltatech_delivery_dummy/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dummy`
- **Versiune:** `19.0.0.0.1`
- **Cale:** `https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_delivery_dummy`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_delivery_dummy`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul adaugă o metodă de livrare „dummy" (fictivă) în sistemul de curierat al Odoo, menită să faciliteze testarea și flexibilitatea operațională fără a necesita integrarea cu un curier real. Din perspectivă business, este un instrument esențial în fazele de implementare și testare a unor noi canale de e-commerce sau a fluxurilor logistice, permițând simularea realistă a unui ciclu complet de comandă. Astfel, echipa poate valida întregul proces de checkout și livrare într-un mediu sigur, fără apeluri către API-urile curierilor reali și fără costurile aferente.

#### 2. Funcționalități Cheie

- Testarea simplificată a fluxului: parcurgerea întregului proces de checkout și livrare fără a declanșa apeluri reale către API-urile curierilor sau costuri asociate.
- Flexibilitate operațională: oferă o metodă de livrare „de rezervă" (placeholder) pentru livrări interne sau scenarii de fulfillment specializate.
- Accelerarea implementării: prototipare și validare rapidă a personalizărilor legate de livrare într-un mediu simulat.
- Reducerea costurilor de testare: evitarea cheltuielilor cu utilizarea API-urilor de curierat sau cu generarea accidentală de etichete de expediere în timpul dezvoltării.
- Fiabilitate sporită a sistemului: asigurarea validării complete a logicii de livrare înainte de trecerea la furnizori de transport reali.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins): adaugă tipul de livrare `dummy` în selecția `delivery_type` și implementează metodele de calcul tarif (`dummy_rate_shipment`, returnează preț 0) și de expediere (`dummy_send_shipping`, generează un număr de urmărire fictiv pe baza comenzii de vânzare).
- `stock.picking` (extins): suprascrie `carrier_generate_label` pentru a genera, în cazul curierului `dummy`, o referință de urmărire și o etichetă PDF fictivă atașată livrării.

**Vizualizări**

- `report_delivery_dummy`: șablon QWeb care randează un raport PDF minimal, afișând numele curierului.
- `action_report_delivery_dummy`: acțiune de raport (`ir.actions.report`, `qweb-pdf`) pe modelul `stock.picking`, folosită ca etichetă fictivă de livrare.

**Acțiuni Automate / Acțiuni Server**

- Nu există sarcini `ir.cron`, reguli `base.automation` sau acțiuni server `ir.actions.server` definite în modul.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): modul complementar din suita de curierat, care urmărește statusul livrărilor; se integrează în același ecosistem de metode de livrare.
