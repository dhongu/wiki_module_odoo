# Relay Delivery – AWB Attach (localizat la `deltatech_delivery_relay/index.md`)

- **Nume Tehnic:** `deltatech_delivery_relay`
- **Versiune:** `19.0.0.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_relay
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_relay`
- **Ultima Ingestie:** `2026-11-15`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul atașează în Odoo etichetele AWB în format PDF primite din afara sistemului, de la client sau de la un sistem extern (de exemplu un marketplace), fără să apeleze vreun curier. Personalul din depozit găsește eticheta lângă livrare, o tipărește și o lipește pe colet, fără să o caute prin e-mailuri sau portaluri externe, iar documentația de expediere rămâne centralizată în ERP.

#### 2. Funcționalități Cheie

- **Metodă de livrare fără curier**: adaugă tipul de metodă *Relay Delivery* (în interfața în limba română, „Livrare la punct de ridicare”, fără legătură cu lockerele), care nu are conturi sau credențiale și pune pe comandă doar prețul fix.
- **Atașarea etichetei pe comandă**: eticheta se încarcă la alegerea metodei pe comanda de vânzare, automat dintr-un fișier `awb_…` primit pe comandă (răspunsul clientului la e-mail sau un atașament din istoric), sau pe livrare, din **Carrier Details**; apoi trece pe livrare și se tipărește cu **Print AWB**.
- **Numărul AWB din numele fișierului**: pentru `awb_1234567890.pdf` numărul este `1234567890`. Într-un mesaj, un fișier este recunoscut doar dacă numele începe cu `awb_`; la confirmarea comenzii și la deschiderea ferestrei de transport se preia orice fișier al cărui nume conține `awb_`.
- **Cerere automată către client**: la confirmarea unei comenzi cu această metodă și fără etichetă, clientul primește un e-mail care îi cere un fișier AWB cu numele începând cu `awb_`.
- **Eticheta în portal**: clientul vede în listele de oferte și comenzi o coloană **AWB** cu linkul de descărcare, iar pagina comenzii arată dacă are AWB.
- **Stare de livrare presupusă**: Odoo nu citește starea de la un curier; o livrare validată, cu AWB, este considerată *Livrat* după 5 zile de la creare.
- **Limitări**: AWB-ul nu se anulează din Odoo (aparține curierului clientului sau sistemului extern); un fișier `awb_…` pus pe o comandă cu altă metodă de livrare schimbă metoda și înlocuiește linia de transport cu una la preț 0, deci totalul comenzii scade; validarea unei livrări fără etichetă „emite” totuși un AWB cu numărul comenzii.

#### 3. Dependențe

- `sale`
- `delivery`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md`, a cărui formulare e generică; comportamentul concret a fost verificat în cod și în fișa consultant.

**Modele**

- `delivery.carrier` (extins): adaugă tipul `relay`; `relay_rate_shipment` întoarce prețul fix, `relay_send_shipping` nu apelează niciun curier și folosește ca referință de urmărire valoarea existentă, numele comenzii sau al livrării, iar `relay_get_status_history` trece în *delivered* livrările validate mai vechi de 5 zile. Capabilitățile declarate sunt doar `ship` și `tracking`.
- `delivery.carrier.service` și `stock.package.type` (extinse): adaugă tipul `relay`.
- `sale.order` (extins): `label_attachment`, `with_label`; `get_awb_from_attachment` și `set_order_label_attachment` preiau fișierul `awb_…`, setează metoda de tip relay și copiază eticheta și numărul AWB pe livrare; `_action_confirm` trimite clientului cererea de AWB; `get_label_attachment` pregătește linkul pentru portal.
- `stock.picking` (extins): `carrier_generate_label` preia eticheta de pe comandă când livrarea nu are una.
- `choose.delivery.carrier` și `delivery.carrier.details` (wizard-uri extinse): câmpurile pentru atașamentul etichetei și referința de urmărire.

**Vizualizări**

- `choose_delivery_carrier_view_form`: fereastra *Add a shipping method* cu atașamentul etichetei și referința de urmărire.
- `view_delivery_carrier_details_form`: fereastra **Carrier Details** de pe livrare, cu aceleași câmpuri.
- `portal_my_quotations`, `portal_my_orders`, `awb_attachments`: coloana AWB în portal și starea AWB pe pagina comenzii.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server proprii; trecerea în *Livrat* după 5 zile rulează prin acțiunea programată de actualizare a stării din [deltatech_delivery](../deltatech_delivery/index.md).

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază pentru livrare (**Carrier Details**, **Print AWB**, lista AWB, actualizarea periodică a stării), pe care se sprijină acest modul.
- `mail`: e-mailul către client și preluarea fișierelor `awb_…` din mesaje.
- Module de marketplace (opțional): comenzile importate cu AWB-ul generat de marketplace.
