# Delivery Notification – Email (localizat la `deltatech_delivery_send_mail/index.md`)

- **Nume Tehnic:** `deltatech_delivery_send_mail`
- **Versiune:** `19.0.1.0.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_send_mail
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_send_mail`
- **Ultima Ingestie:** `2026-11-15`

#### 1. Sumar

Modulul trimite automat clientului e-mailuri atunci când AWB-ul (eticheta de expediere) a fost generat sau când coletul a fost ridicat de curier. Comunicarea automată reduce întrebările de tip „Unde este comanda mea?”, deoarece clienții sunt informați din timp despre starea livrării.

#### 2. Funcționalități Cheie

- **E-mail la generarea AWB-ului**: după înregistrarea AWB-ului la curier, clientul primește un mesaj cu numărul de urmărire și linkul de urmărire al curierului.
- **E-mail la ridicarea coletului**: când starea livrării iese din *Ciornă* / *Pre-aviz* (coletul a fost preluat de curier), clientul primește un mesaj cu aceleași detalii de urmărire.
- **Activare pe două niveluri**: opțional **per curier** (bifa `send_email_awb` pe metoda de livrare) și **per companie**, din Inventar > Setări, secțiunea de expediere: *Email AWB Create* și *Email AWB Picked up*, fiecare cu propriul șablon de e-mail, completat implicit cu șabloanele din modul (setările sunt specifice companiei).
- **Destinatar**: adresa partenerului livrării; dacă lipsește, e-mailul se preia de la compania-părinte, iar în lipsa ei de la clientul comenzii de vânzare.
- **Șabloane dedicate** (în română, `Delivery: AWB Created` și `Delivery: AWB Picked Up`), cu numărul AWB și linkul de urmărire al curierului.
- **Eșecul notificării nu afectează livrarea**: o eroare la trimiterea e-mailului nu anulează AWB-ul și nu blochează schimbarea stării; ea este consemnată în jurnal și în chatter, ca operatorul să nu creadă că clientul a fost notificat. Se poate folosi și un server de e-mail dat în context (`mail_server_id`).

#### 3. Dependențe

- `delivery`
- [deltatech_delivery_status](../deltatech_delivery_status/index.md)

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md`; detaliile operaționale au fost verificate în cod, iar numele afișat din Apps (*Delivery Notification – Email*, fost *Delivery Send Mail*) provine din `readme/HISTORY.md` (versiunea `19.0.1.0.8`).

**Modele**

- `delivery.carrier` (extins): câmpul `send_email_awb`.
- `res.company` (extins): `stock_email_awb_create`, `stock_email_awb_template_id`, `stock_email_awb_picked`, `stock_email_awb_picked_template_id`, cu șabloanele din modul ca valori implicite.
- `res.config.settings` (extins): câmpurile aferente, legate de companie.
- `stock.picking` (extins): `send_to_shipper` trimite e-mailul „AWB creat”; `write` trimite e-mailul „AWB ridicat” când `delivery_state` iese din *draft* / *pre_advice*; metode ajutătoare `_send_awb_email`, `_send_awb_picked_email`, `_get_so_partner` și `_log_awb_email_failure`.

**Vizualizări**

- `view_delivery_carrier_form`: bifa `send_email_awb` în grupul de detalii al furnizorului, pe metoda de livrare.
- `res_config_settings_view_form`: setările *Email AWB Create* și *Email AWB Picked up* cu șabloanele lor, în blocul de expediere din Inventar.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server. Datele conțin șabloanele de e-mail `mail_template_awb_create` și `mail_template_awb_picked` (`noupdate`).

#### 5. Conexiuni

- [deltatech_delivery_status](../deltatech_delivery_status/index.md): furnizează starea livrării (`delivery_state`) care declanșează e-mailul „AWB ridicat”.
- [deltatech_delivery](../deltatech_delivery/index.md): modul înrudit, cu integrările de curierat care generează AWB-ul.
