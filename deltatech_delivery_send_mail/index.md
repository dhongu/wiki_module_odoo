# Delivery Notification – Email (localizat la `deltatech_delivery_send_mail/index.md`)

- **Nume Tehnic:** `deltatech_delivery_send_mail`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_send_mail
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_send_mail`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul trimite automat e-mailuri clientului când se generează AWB-ul sau când coletul este ridicat de curier. Clienții sunt ținuți la curent cu livrarea, ceea ce reduce întrebările de tipul „Unde este comanda mea?” și munca manuală a suportului.

#### 2. Funcționalități Cheie

- Notificare proactivă a clientului despre progresul livrării (AWB generat, colet ridicat), pe baza șabloanelor de e-mail `mail_template_awb_create` și `mail_template_awb_picked`.
- Reducerea costurilor de suport prin automatizarea actualizărilor de status de rutină.
- Transparență imediată după ce comanda este împachetată și pregătită pentru transport.
- Comunicare scalabilă pentru volume mari de comenzi zilnice.
- Setările se află pe metoda de livrare și în setările companiei.

#### 3. Dependențe

- `delivery`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

Conform fluxului de ingestie, deoarece există `readme/DESCRIPTION.md`, analiza codului pentru această secțiune este omisă. Pentru orientare, modulul extinde `delivery.carrier`, `res.company`, `res.config.settings` și `stock.picking`, și conține vizualizările `view_delivery_carrier_form` și `res_config_settings_view_form`, plus cele două șabloane de e-mail.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): statusurile de livrare care declanșează notificările.
- [deltatech_delivery](../deltatech_delivery/index.md): baza ecosistemului de livrare și curierat.
