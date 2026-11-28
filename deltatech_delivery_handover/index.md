# Courier Handover Report

- **Nume Tehnic:** `deltatech_delivery_handover`
- **Versiune:** `20.0.1.1.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_handover
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_handover`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Predarea coletelor către curier direct din lista de AWB-uri sau de livrări, cu un proces-verbal de predare-primire tipăribil, semnat de șofer. Confirmarea predării marchează momentul în care coletele pleacă din depozit și poate solicita curierului ridicarea, ca o singură comandă pentru toate coletele.

#### 2. Funcționalități Cheie

- **Action → Hand Over to Courier** pe AWB-uri sau livrări selectate: se creează câte o predare per curier, cu AWB-urile încă predabile (AWB-ul curent al unei livrări de ieșire, necunoscut încă curierului și neaflat pe altă predare); celelalte sunt omise, iar predarea spune de ce.
- Predarea conține curierul, data, cine a predat, șoferul, vehiculul și coletele (destinatar, oraș, număr colete, greutate, ramburs) cu totaluri.
- **Confirm Handover**: livrările trec *În tranzit*, data predării se păstrează pe ele, iar o interogare de status care răspunde încă cu pre-avizul nu le mai readuce; un AWB poate fi pe o singură predare, dacă aceasta nu e anulată.
- Raport **Courier Handover Report** (proces-verbal de predare-primire colete) cu totaluri (AWB-uri, colete, greutate, ramburs pe monedă) și casete de semnătură; scanarea semnată se atașează în *Signed Report*.
- Ridicare curier: FAN Courier se comandă din predare (**Order Courier Pickup**, în fereastra setată pe curier, anulabilă); Cargus își rezervă singur comenzile, iar **Check Pickup** doar citește comanda; GLS și Sameday ridică odată cu AWB-ul.
- Predările se văd în *Inventar → Operațiuni → Delivery AWB → Courier Handovers*; o predare ciornă o anulează orice utilizator de inventar, una confirmată doar un manager (coletele revin la *Pre advice*). Cu `deltatech_delivery_dashboard`, confirmarea datează predarea pe AWB. Flux pas cu pas: vezi fișa consultant.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.handover`: predarea către curier (curier, dată, șofer, vehicul, totaluri, comandă de ridicare), cu `mail.thread` și activități.
- `delivery.handover.line`: linia de predare legată de un AWB, cu destinatar, oraș, colete, greutate și ramburs.
- `delivery.carrier`, `delivery.awb`, `stock.picking` (extinse): suport pentru ridicare curier și data predării.

**Vizualizări**

- `view_delivery_handover_list` / `view_delivery_handover_form` / `view_delivery_handover_search` / `action_delivery_handover`: lista și formularul predărilor.
- `view_picking_form_handover`, `view_delivery_carrier_form_pickup`: legătura cu livrarea și setările de ridicare pe curier.
- `action_report_delivery_handover`: raportul de predare-primire.

**Acțiuni Automate / Acțiuni Server**

- `action_server_handover_from_awb`, `action_server_handover_from_picking`: acțiunea *Hand Over to Courier* pe AWB-uri, respectiv livrări.
- Secvență `ir.sequence` pentru numărul predării.

#### 5. Conexiuni

- [deltatech_delivery_dashboard](../deltatech_delivery_dashboard/index.md): predarea confirmată pornește SLA-ul și numără coletul ca predat azi.
