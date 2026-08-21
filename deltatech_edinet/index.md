# Deltatech EDINET (localizat la `deltatech_edinet/index.md`)

- **Nume Tehnic:** `deltatech_edinet`
- **Versiune:** `19.0.1.5.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_edinet`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_edinet`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul integrează Odoo cu platforma **Infinite EDINET**, permițând schimbul electronic de documente comerciale (EDI). Acesta automatizează schimbul de comenzi de vânzare și de facturi între Odoo și platforma EDINET, reducând efortul manual și riscul de erori. Practic, comenzile de la clienți pot fi preluate automat în Odoo, iar facturile validate pot fi trimise către EDINET cu un singur clic sau în loturi.

#### 2. Funcționalități Cheie

- **Import automat al comenzilor de vânzare:** preia și procesează automat comenzile (ORDERS) din platforma EDINET.
- **Export de facturi:** trimite facturile validate (INVOICE) direct către EDINET, individual sau în lot.
- **Integrare Infinite:** proiectat special pentru a funcționa cu serviciile EDI Infinite.
- **Suport multi-companie:** se pot configura credențiale separate pentru fiecare companie din instanța Odoo.
- **Configurare flexibilă a credențialelor:** la nivel de companie (**Setări > Companii**) sau prin parametri de sistem (`deltatech_edinet.username`, `deltatech_edinet.password`) ca metodă alternativă.
- **URL WSDL configurabil per companie:** câmpul `edinet_wsdl_template` permite direcționarea integrării către noua platformă EDInet (placeholder `{service}`), fără modificări de cod, în perspectiva migrării anunțate de furnizor (Axis2 legacy → platformă nouă).
- **Reimport EDI:** buton pe comanda de vânzare (draft/trimisă, cu `client_order_ref` completat) care rerulează importul EDI din XML-ul EDInet deja atașat pe comandă, fără a mai fi nevoie de intervenția suportului.
- **Verificare Edinet:** buton care compară comanda cu XML-ul EDInet atașat (adresă de livrare, produse, cantități, prețuri) și scrie diferențele în chatter; verificarea este strict read-only și nu suprascrie comanda.
- **Control acces dedicat:** butoanele de reimport și verificare sunt restricționate la grupul de securitate *Edinet: reimport și verificare comenzi*, implicat automat de *Vânzări / Administrator*.

#### 3. Dependențe

- [deltatech_edi](../deltatech_edi/index.md)

Dependențe externe Python: `zeep`, `xmltodict`.

#### 4. Componente Cheie

> Conform `readme/DESCRIPTION.md`, secțiunile de business sunt acoperite mai sus. Următoarele componente sunt sintetizate din `__manifest__.py` și cod, pentru orientare tehnică.

**Modele**

- `sale.order` (extindere): adaugă `corn_import_edinet` (cron de import ORDERS), `action_reimport_edinet_button` (reimport din atașamentul XML), `action_check_edinet_button` / `_check_edinet_message` (verificare read-only față de documentul Edinet: adresă, produse, cantități, prețuri) și `_export_edinet_data` (trimitere comandă).
- `account.move` (extindere): adaugă `export_edinet_button` / `action_mass_export_edinet` pentru exportul facturilor validate către EDINET (individual sau în masă) și suprascrie `button_export_edi` pentru partenerii cu `edi_system == "edi_net"`.
- `res.company` (extindere): câmpurile `edinet_username`, `edinet_password` și `edinet_wsdl_template` pentru credențiale și URL-ul șablon al serviciilor SOAP.

**Vizualizări**

- `views/account_move_view.xml`: extinde formularul de factură (`account.move`) pentru acțiunile de export către EDINET.
- `views/sale_order_view.xml` (`view_order_form_edinet_reimport`): adaugă în antetul comenzii de vânzare butoanele „Reimport EDI” și „Verificare Edinet”, ambele restricționate la grupul `deltatech_edinet.group_edinet_reimport`.
- `views/res_config_settings_view.xml`: adaugă în Setări (secțiunea Integrări) câmpurile pentru credențialele și URL-ul WSDL EDINET, la nivel de companie.

**Securitate**

- `security/edinet_security.xml`: definește privilegiul „Edinet” și grupul `group_edinet_reimport` (implicat de `sales_team.group_sale_manager`), care controlează accesul la butoanele de reimport și verificare.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_cron_data.xml` (`ir_cron_edinet_get_order`, inactiv implicit): sarcină programată orară care preia automat comenzile de vânzare (ORDERS) din EDINET, pentru fiecare companie cu credențiale configurate.

#### 5. Conexiuni

- [deltatech_edi](../deltatech_edi/index.md): cadrul EDI de bază pe care se construiește acest conector (dependență directă, hook-uri pe `account.move` și șabloane EDI).
- [deltatech_ediconnect](../deltatech_ediconnect/index.md): conector EDI din aceeași familie de module, ca alternativă/complement pentru alte platforme de schimb electronic de documente.
