# SMS on Sale Order Confirmation

- **Nume Tehnic:** `deltatech_sms_sale`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_sms_sale
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sms_sale`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Clienților le place să afle imediat că le-a fost înregistrată comanda. Modulul trimite automat un SMS către client când o comandă de vânzare este confirmată și când este trimis e-mailul de confirmare a comenzii, folosind șabloane SMS pe care le puteți edita. Modulul nu are furnizor SMS propriu: numărul de telefon al clientului și textul mesajului merg către serviciul SMS configurat în Odoo, iar mesajele se trimit imediat, nu în coadă.

#### 2. Funcționalități Cheie

- **SMS la confirmare:** la confirmarea comenzii, clientul primește mesajul din șablonul ales la *SMS Sale Order Confirm*, dacă opțiunea este activă și clientul are număr de telefon.
- **SMS la postare:** de fiecare dată când Odoo trimite e-mailul de confirmare a comenzii, pleacă în același mod mesajul ales la *SMS Sale Order Post*. Setările numesc acest moment „postarea” comenzii (textul de ajutor: din website).
- **Texte implicite:** ambele șabloane livrate încep cu numele companiei și precizează că numărul comenzii a fost confirmat, respectiv postat.
- **Setări per companie:** ambele opțiuni se află în setările de Vânzări, se stabilesc per companie și sunt active implicit. Cât timp o opțiune este activă, șablonul ei este obligatoriu.
- **Drepturi pe șabloane:** managerii de vânzări pot crea, modifica și șterge șabloanele SMS ale comenzilor de vânzare, și doar pe acestea.

#### 3. Dependențe

- `sale`
- `sales_team`
- `sms`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): suprascrie `_send_order_confirmation_mail` și `action_confirm` pentru a trimite SMS-ul prin `_message_sms_with_template` (fără coadă), folosind șablonul configurat pe companie și telefonul partenerului.
- `res.company` (extins): adaugă comutatoarele și șabloanele de SMS — `sale_order_sms_post`, `sale_order_sms_post_template_id`, `sale_order_sms_confirm`, `sale_order_sms_confirm_template_id` (active și cu valori implicite din șabloanele livrate de modul).
- `res.config.settings` (extins): expune în Setări câmpurile companiei pentru activarea și alegerea șabloanelor de SMS.

**Vizualizări**

- `res_config_settings_view_form_sale`: extinde formularul de Setări Vânzări, adăugând secțiunile „SMS Sale Order Post” și „SMS Sale Order Confirm”, fiecare cu comutator și selectarea șablonului SMS aferent.

**Acțiuni Automate / Acțiuni Server**

- `data/sms_data.xml` (`noupdate="1"`): definește două șabloane `sms.template` pe modelul `sale.order` — `sms_template_data_sale_order_confirm` (mesaj la confirmare) și `sms_template_data_sale_order_post` (mesaj la postare). Nu există cron-uri sau acțiuni server; trimiterea este declanșată de evenimentele de pe comanda de vânzare.

#### 5. Conexiuni

- [deltatech_sms](../deltatech_sms/index.md): modulul de bază al familiei de notificări prin SMS din suita Deltatech.
