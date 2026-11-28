# EDIConnect Connector (localizat la `deltatech_ediconnect/index.md`)

- **Nume Tehnic:** `deltatech_ediconnect`
- **Versiune:** `20.0.1.1.16`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_ediconnect
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ediconnect`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul este un conector EDI (Electronic Data Interchange) care automatizează schimbul de date între Odoo și partenerii de afaceri prin platforma EDIConnect. Din perspectivă de business, este o componentă de infrastructură pentru companiile cu volum mare de tranzacții: comenzile primite se importă automat ca comenzi de vânzare, iar facturile emise se trimit către EDIConnect, fără introducere manuală a datelor.

#### 2. Funcționalități Cheie

- **Import programat de comenzi:** o acțiune programată descarcă de pe serverul EDIConnect fișierele de comandă primite (ORDERS) și creează comenzile de vânzare în Odoo.
- **Export de facturi:** facturile clienților postate se trimit către EDIConnect direct din factură.
- **Documente suportate:** comenzi primite (ORDERS) și facturi emise; avizele de expediție (DESADV) nu sunt trimise de acest modul.
- **Autentificare securizată:** autentificare cu utilizator și parolă (Basic Auth) plus cheie API.
- **Gestionarea fișierelor:** listarea, preluarea și ștergerea fișierelor procesate de pe serverul EDI.
- **Comunicare B2B automatizată:** integritate sporită a datelor și vizibilitate asupra schimburilor electronice direct în Odoo.

**Configurare:** din **Setări → EDI Connect** se introduc URL-ul API-ului furnizat de prestatorul EDIConnect, numele de utilizator, parola și cheia API. Acțiunea programată de import este livrată inactivă și se activează după configurare.

#### 3. Dependențe

- [deltatech_edi](../deltatech_edi/index.md)

Dependențe Python externe: `zeep`, `xmltodict`.

#### 4. Componente Cheie

Componentele detaliate sunt acoperite prin fișierul `readme/DESCRIPTION.md` (vezi secțiunile 1 și 2); analiza suplimentară a codului a fost omisă, întrucât Readme-ul este prezent. La nivel de manifest, modulul livrează vizualizarea de configurare `views/res_config_settings_view.xml` (parametrii de conectare EDIConnect) și acțiunea programată `ir.cron` „Edi Connect: Get Orders” din `data/ir_cron_data.xml` (import orar al comenzilor, inactivă implicit).

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): modulul de bază EDI pe care se construiește acest conector (dependență directă).
- [deltatech_edinet](../deltatech_edinet/index.md): conector EDI înrudit din aceeași suită, alternativă/complement pentru schimbul electronic de documente.
