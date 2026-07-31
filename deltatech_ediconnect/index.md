# Deltatech EDIConnect (localizat la `deltatech_ediconnect/index.md`)

- **Nume Tehnic:** `deltatech_ediconnect`
- **Versiune:** `19.0.1.1.9`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_ediconnect`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ediconnect`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul oferă un conector EDI (Electronic Data Interchange) robust și scalabil, care facilitează schimbul automat și fără cusur de date între Odoo și diverse sisteme externe sau parteneri de afaceri, prin intermediul platformei EDIConnect. Din perspectivă de business, este o componentă de infrastructură critică pentru companiile care au nevoie să automatizeze tranzacții de volum mare, precum facturi, comenzi de achiziție și detalii de livrare, eliminând introducerea manuală a datelor și oferind vizibilitate în timp real asupra schimburilor electronice direct în Odoo.

#### 2. Funcționalități Cheie

- **Schimb automat de documente**: încărcarea și descărcarea fără cusur a fișierelor EDI.
- **Integrare flexibilă**: suportă mai multe tipuri de documente printr-un API standardizat.
- **Autentificare securizată**: folosește autentificare bazată pe token (Basic Auth + cheie API).
- **Gestionarea fișierelor**: capabilități integrate pentru listarea, recuperarea și ștergerea fișierelor procesate de pe serverul EDI.
- **Comunicare B2B automatizată**: automatizează schimbul de documente electronice cu partenerii de afaceri.
- **Integritate îmbunătățită a datelor**: elimină erorile de introducere manuală prin utilizarea formatelor EDI standardizate.
- **Vizibilitate în timp real**: oferă o imagine imediată asupra stării tuturor schimburilor de date electronice.

**Configurare:** integrarea EDIConnect se configurează din setările EDI din Odoo, furnizând: URL-ul API (de regulă `https://portal.ediconnect.ro/api/v1`), numele de utilizator și parola contului EDIConnect, precum și cheia API furnizată de prestatorul serviciului EDIConnect.

#### 3. Dependențe

- [deltatech_edi](../deltatech_edi/index.md)

Dependențe Python externe: `zeep`, `xmltodict`.

#### 4. Componente Cheie

Componentele detaliate sunt acoperite prin fișierul `readme/DESCRIPTION.md` (vezi secțiunile 1 și 2). Conform fluxului de ingestie, analiza suplimentară a codului a fost omisă, întrucât Readme-ul este prezent. La nivel de manifest, modulul livrează vizualizarea de configurare `views/res_config_settings_view.xml` (parametrii de conectare EDIConnect) și o sarcină programată `ir.cron` definită în `data/ir_cron_data.xml` (sincronizarea fișierelor EDI).

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): modulul de bază EDI pe care se construiește acest conector (dependență directă).
- [deltatech_edinet](../deltatech_edinet/index.md): conector EDI înrudit din aceeași suită, alternativă/complement pentru schimbul electronic de documente.
