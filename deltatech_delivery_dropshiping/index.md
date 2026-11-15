# Deltatech Delivery Dropshiping (localizat la `deltatech_delivery_dropshiping/index.md`)

- **Nume Tehnic:** `deltatech_delivery_dropshiping`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_delivery/tree/19.0/deltatech_delivery_dropshiping
- **Cale Locală:** `odoo-addons/bitshop_delivery/deltatech_delivery_dropshiping`
- **Ultima Ingestie:** `2026-11-15`

#### 1. Sumar

**Modul depreciat pe 19.0 — nu se instalează (`installable: False`, `development_status: Deprecated`).** Modulul optimiza operațiunile de dropshipping automatizând transmiterea AWB-ului (scrisoare de transport) și a detaliilor de livrare către furnizori. Pe Odoo 19, [deltatech_delivery](../deltatech_delivery/index.md) acoperă deja acest scenariu: `post_message_delivery()` din acel modul identifică atașamentul cu eticheta, îl redenumește după AWB și, când ridicarea are o comandă de achiziție (`purchase_id`), apelează `send_mail_to_vendor()`, care postează eticheta pe acea comandă **și notifică furnizorul**. Acest modul doar adăuga un mesaj în plus, fără notificare, așa că pe comanda de achiziție ajungeau două mesaje cu același AWB (duplicarea exista deja pe 18.0). Codul a rămas în depozit, neinstalabil, doar ca bazele de date care îl au deja instalat să continue să pornească.

#### 2. Funcționalități Cheie

- Onorare automată: trimite automat etichetele de expediere și informațiile AWB către furnizori pentru procesarea imediată a comenzii.
- Acuratețe îmbunătățită: furnizorii primesc informații de livrare corecte și actualizate, ceea ce reduce erorile de expediere și retururile.
- Ciclu de comandă mai rapid: simplifică tranziția de la confirmarea comenzii la onorarea de către furnizor.
- Vizibilitate sporită: urmărește comenzile în regim de dropshipping prin actualizări de stare a livrării integrate în Odoo.
- Logistică scalabilă: gestionează ușor un număr mare de parteneri de dropshipping prin automatizarea sarcinilor de expediere de rutină.

> Notă: aceste funcționalități sunt acum asigurate de [deltatech_delivery](../deltatech_delivery/index.md) (`post_message_delivery` → `send_mail_to_vendor`), iar acest modul rămâne doar pentru compatibilitate cu instalările vechi. Singura diferență este filtrul `is_dropship`: `deltatech_delivery` trimite eticheta pentru orice ridicare legată de o comandă de achiziție, nu doar pentru cele de tip dropship; dacă distincția contează pentru un client, locul corect pentru ajustare este `send_mail_to_vendor`, nu un modul separat.

#### 3. Dependențe

- `stock_dropshipping`
- [deltatech_delivery](../deltatech_delivery/index.md)

#### 4. Componente Cheie

**Modele**

- `delivery.carrier` (extindere): suprascrie `send_shipping()` — pentru fiecare ridicare de tip dropship cu etichetă atașată și comandă de achiziție asociată, redenumește atașamentul etichetei după AWB (`awb_<carrier_tracking_ref>.pdf`) și postează pe comanda de achiziție un mesaj cu eticheta ca atașament (fără notificare explicită a destinatarilor).

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server și nu are date XML; logica se limitează la suprascrierea din `models/delivery.py`.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): înlocuiește complet funcționalitatea acestui modul pe 19.0, cu notificarea furnizorului în plus.
- `stock_dropshipping`: modul standard Odoo pe care se bazează fluxul de dropshipping (câmpul `is_dropship` pe `stock.picking`).
