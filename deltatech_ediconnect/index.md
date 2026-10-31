# EDIConnect Connector (localizat la `deltatech_ediconnect/index.md`)

- **Nume Tehnic:** `deltatech_ediconnect`
- **Versiune:** `19.0.1.1.13`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_ediconnect
- **Cale Locală:** `odoo-addons/bitshop/deltatech_ediconnect`
- **Ultima Ingestie:** `2026-10-31`

#### 1. Sumar

Modulul oferă un conector EDI (Electronic Data Interchange) robust și scalabil, care facilitează schimbul automat de date între Odoo și diverși parteneri de afaceri sau sisteme externe, prin platforma EDIConnect. Din perspectivă de business, este o componentă de infrastructură pentru companiile care automatizează tranzacții de volum mare, precum facturi și comenzi de achiziție, eliminând introducerea manuală a datelor. Pe Odoo Apps modulul apare sub numele „EDIConnect Connector” (anterior „EDIConnect”); numele tehnic nu s-a schimbat.

#### 2. Funcționalități Cheie

- **Schimb automat de documente:** încărcarea și descărcarea fișierelor EDI; comenzile primite se importă ca comenzi de vânzare, iar facturile se trimit partenerilor care folosesc EDI Connect.
- **Integrare flexibilă:** suportă mai multe tipuri de documente printr-un API standardizat.
- **Autentificare securizată:** autentificare bazată pe token (Basic Auth + cheie API).
- **Gestionarea fișierelor:** listarea, recuperarea și ștergerea fișierelor de pe serverul EDI.
- **Comunicare B2B automatizată** și **integritate îmbunătățită a datelor**, prin formate EDI standardizate în locul introducerii manuale.
- **Configurare:** în setările EDI din Odoo se completează URL-ul API (documentația indică de regulă `https://portal.ediconnect.ro/api/v1`), numele de utilizator, parola și cheia API furnizate de prestatorul EDIConnect; credențialele se rețin per companie.
- **Import comenzi pe companie:** acțiunea programată importă comenzile fiecărei companii în compania credențialelor sale. Un fișier ORDER nu mai este sărit doar fiindcă există un atașament cu același nume în altă parte; contează doar cel stocat de acest import pe `sale.order` pentru compania respectivă. O comandă primită din nou sub alt nume de fișier (același număr de comandă și GLN al cumpărătorului, în aceeași companie) se leagă de comanda existentă, nu se dublează.
- **Partener:** valoarea „EDI Connect” din câmpul `edi_system` al partenerului determină trimiterea facturii prin acest conector la exportul EDI.

#### 3. Dependențe

- [deltatech_edi](../deltatech_edi/index.md)

Dependențe Python externe: `zeep`, `xmltodict`.

#### 4. Componente Cheie

*Conform fluxului de ingestie, analiza detaliată a codului este omisă, deoarece `readme/DESCRIPTION.md` este prezent. Mai jos sunt doar reperele confirmate în manifest și cod.*

**Modele**

- `sale.order` (extins): `corn_import_edi_connect()` descarcă fișierele ORDER și importă comenzile.
- `account.move` (extins): `button_export_edi()` trimite factura prin EDI Connect când partenerul comercial are `edi_system = edi_connect`.
- `res.partner` (extins): adaugă „EDI Connect” în `edi_system`.
- `res.company` (extins): URL, utilizator, parolă și cheie API EDI Connect.
- Clasa client `EDIConnect` (`models/ediconnect.py`): autentificare și operații pe fișiere (`file_put`, `file_get_list`, `file_get`, `file_delete`).

**Vizualizări**

- `views/res_config_settings_view.xml`: parametrii de conectare EDIConnect în setări.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ed_connect_get_order` („Edi Connect: Get Orders”): rulează din oră în oră `model.corn_import_edi_connect()`; este livrată **inactivă** și trebuie activată.

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): modulul de bază EDI pe care se construiește acest conector (dependență directă).
- [deltatech_edinet](../deltatech_edinet/index.md): conector EDI înrudit (EDI Net), tot peste `deltatech_edi`, care adaugă la rândul său o valoare în `edi_system` și preia `button_export_edi` pentru partenerii lui.
