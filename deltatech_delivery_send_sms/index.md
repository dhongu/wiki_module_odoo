# Delivery Notification – SMS (localizat la `deltatech_delivery_send_sms/index.md`)

- **Nume Tehnic:** `deltatech_delivery_send_sms`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/20.0/deltatech_delivery_send_sms
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_send_sms`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul trimite automat clientului un SMS atunci când pentru livrarea sa a fost generat AWB-ul sau când curierul a preluat coletul. Clientul este informat în timp real pe telefon, ceea ce reduce numărul întrebărilor de tip „Unde este comanda mea?” și încărcarea echipei de suport, fără nicio intervenție manuală în depozit.

#### 2. Funcționalități Cheie

- Două notificări SMS: „AWB creat” (la generarea AWB-ului) și „AWB preluat” (când starea livrării trece din *Ciornă* sau *Pre-aviz* în *În tranzit*).
- Activare pe companie, din **Inventar → Configurare → Setări**, secțiunea **Livrare**: opțiunile *SMS AWB Create* și *SMS AWB Picked up*, fiecare cu șablonul său de SMS (cele două șabloane livrate sunt preselectate și pot fi editate).
- Activare pe curier: bifa **Send Sms Awb** din metoda de livrare (**Inventar → Configurare → Livrare → Metode de livrare**); doar transferurile expediate cu un astfel de curier notifică clientul.
- SMS-ul „AWB creat” se trimite doar dacă sunt bifate opțiunea companiei și bifa curierului și clientul are număr de telefon; SMS-ul „AWB preluat” nu verifică telefonul, iar pentru un client fără telefon apare ca eșuat în chatter.
- Fiecare SMS este înregistrat în chatter-ul transferului, cu textul exact trimis; un SMS eșuat (de ex. fără credit SMS) poate fi retrimis, iar un șablon invalid produce o notă explicativă. Expedierea nu este niciodată blocată.
- Textul este trimis în limba clientului; sunt livrate șabloane în engleză și română.
- Detalii pas-cu-pas, cu capturi, în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `delivery`
- `sms`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extins): câmpul `send_sms_awb`, bifa de activare a notificărilor pe curier.
- `res.company` (extins): opțiunile `stock_sms_awb_create`, `stock_sms_awb_picked` și șabloanele SMS asociate.
- `res.config.settings` (extins): expune opțiunile companiei în Setări.
- `stock.picking` (extins): trimiterea SMS-urilor (`_send_awb_sms`, `_send_awb_picked_sms`), declanșate la `send_to_shipper` și la modificarea stării de livrare, plus înregistrarea eșecurilor în chatter.

**Vizualizări**

- `view_delivery_carrier_form`: adaugă bifa *Send Sms Awb* pe formularul metodei de livrare.
- `res_config_settings_view_form`: opțiunile SMS AWB în secțiunea Livrare din setările Inventarului.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul livrează două înregistrări `sms.template`: `sms_template_awb_create` și `sms_template_awb_picked_up`.

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): gestionează stările de livrare (AWB creat / preluat) care declanșează SMS-urile.
- [deltatech_delivery_send_mail](../deltatech_delivery_send_mail/index.md): același tip de notificare, prin e-mail.
- [deltatech_delivery](../deltatech_delivery/index.md): modulul de bază al suitei de livrare.
