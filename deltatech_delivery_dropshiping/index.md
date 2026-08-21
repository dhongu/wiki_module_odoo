# Deltatech Delivery Dropshiping (localizat la `deltatech_delivery_dropshiping/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dropshiping`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dropshiping
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dropshiping`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

**Modul depreciat pe 19.0 — nu se instalează (`installable: False`).** Modulul optimiza operațiunile de dropshipping automatizând transmiterea AWB-ului (scrisoare de transport) și a detaliilor de livrare către furnizori, pentru un flux de onorare a comenzilor fără sincope. Pe Odoo 19, [deltatech_delivery](../deltatech_delivery/index.md) acoperă deja acest scenariu: `post_message_delivery()` din acel modul identifică atașamentul cu eticheta, îl redenumește după AWB și, atunci când ridicarea are o comandă de achiziție (`purchase_id`), postează eticheta pe acea comandă **și notifică furnizorul** — exact ceea ce încerca să facă acest modul, dar fără notificare. Codul a rămas în depozit, dezinstalabil, doar ca bazele de date care îl aveau deja instalat să continue să pornească.

#### 2. Funcționalități Cheie

- Onorare automată: trimite automat etichetele de expediere și informațiile AWB către furnizori pentru procesarea imediată a comenzii.
- Acuratețe îmbunătățită: se asigură că furnizorii primesc informații de livrare corecte și actualizate, reducând erorile de expediere și retururile.
- Ciclu de comandă mai rapid: simplifică tranziția de la confirmarea comenzii la onorarea de către furnizor.
- Vizibilitate sporită: urmărește comenzile în regim de dropshipping prin actualizări de stare a livrării integrate în Odoo.
- Logistică scalabilă: gestionează ușor un număr mare de parteneri de dropshipping prin automatizarea sarcinilor de expediere de rutină.

> Notă corecție: aceste funcționalități sunt acum asigurate de [deltatech_delivery](../deltatech_delivery/index.md) (funcția `post_message_delivery` → `send_mail_to_vendor`), iar acest modul rămâne doar pentru compatibilitate cu instalările vechi.

#### 3. Dependențe

- `stock_dropshipping`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extindere): suprascrie `send_shipping()` — pentru fiecare ridicare (`picking`) de tip dropship cu etichetă atașată și comandă de achiziție asociată, redenumește atașamentul etichetei după codul AWB (`awb_<carrier_tracking_ref>.pdf`) și postează un mesaj simplu (fără notificare de destinatari) pe comanda de achiziție, cu eticheta ca atașament.

Modulul nu conține date XML, vizualizări proprii sau acțiuni automate — logica se limitează la suprascrierea de mai sus în `models/delivery.py`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): înlocuiește complet funcționalitatea acestui modul pe 19.0, cu suport suplimentar de notificare a furnizorului.
- `stock_dropshipping`: modul standard Odoo pe care se bazează fluxul de dropshipping (câmpul `is_dropship` pe `stock.picking`).
