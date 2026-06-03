# Deltatech SMS Sale

- **Nume Tehnic:** `deltatech_sms_sale`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sms_sale
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sms_sale`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul Deltatech SMS Sale trimite automat un mesaj SMS către client în momentele cheie ale ciclului unei comenzi de vânzare: la confirmarea comenzii și la transmiterea (postarea) acesteia, de exemplu dintr-un magazin online. Astfel, clientul primește o notificare imediată de tipul „Comanda dumneavoastră nr. ... a fost confirmată”, îmbunătățind comunicarea și încrederea, fără intervenție manuală din partea echipei de vânzări. Trimiterea este configurabilă per companie și se bazează pe șabloane SMS editabile, folosind numărul de telefon al clientului din comandă.

#### 2. Funcționalități Cheie

- Trimitere automată a unui SMS către client la **confirmarea** comenzii de vânzare.
- Trimitere automată a unui SMS la **postarea** comenzii (de ex. din magazinul online).
- Mesaje bazate pe **șabloane SMS** predefinite și personalizabile (text de tipul „...your order n° ... has been confirmed.”).
- Activare/dezactivare și alegerea șablonului **per companie**, din Setări (configurare specifică companiei în mediu multi-company).
- Trimiterea se face doar dacă partenerul are completat numărul de telefon.

#### 3. Dependențe

- `sale`
- `sales_team`
- `sms`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): suprascrie `_send_order_confirmation_mail` și `action_confirm` pentru a trimite SMS-ul prin `_message_sms_with_template`, folosind șablonul configurat pe companie și telefonul partenerului.
- `res.company` (extins): adaugă comutatoarele și șabloanele de SMS — `sale_order_sms_post`, `sale_order_sms_post_template_id`, `sale_order_sms_confirm`, `sale_order_sms_confirm_template_id` (cu valori implicite din șabloanele livrate de modul).
- `res.config.settings` (extins): expune în Setări câmpurile companiei (related) pentru activarea și alegerea șabloanelor de SMS.

**Vizualizări**

- `res_config_settings_view_form_sale`: extinde formularul de Setări Vânzări, adăugând secțiunile „SMS Sale Order Post” și „SMS Sale Order Confirm”, fiecare cu comutator și selectarea șablonului SMS aferent.

**Acțiuni Automate / Acțiuni Server**

- `data/sms_data.xml` (`noupdate="1"`): definește două șabloane `sms.template` pe modelul `sale.order` — `sms_template_data_sale_order_confirm` (mesaj la confirmare) și `sms_template_data_sale_order_post` (mesaj la postare). Nu există cron-uri sau acțiuni server; trimiterea este declanșată de evenimentele pe comanda de vânzare.

#### 5. Conexiuni

Modulul face parte din familia de notificări prin SMS a suitei Deltatech, alături de modulul de bază `deltatech_sms`, care nu are încă pagină în wiki. Nu au fost identificate alte conexiuni funcționale cu module documentate în wiki.
