# Deltatech EDINET (localizat la `deltatech_edinet/index.md`)

- **Nume Tehnic:** `deltatech_edinet`
- **Versiune:** `20.0.1.6.7`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_edinet`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_edinet`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul face schimb de comenzi, avize de expediție și facturi cu lanțurile de retail prin platforma **Infinite EDINET**, rețeaua EDI folosită de mulți retaileri din România în relația cu furnizorii. Comenzile primite de la retailer devin automat comenzi de vânzare în Odoo, iar facturile și avizele de expediție ajung la retailer fără reintroducere manuală în portalul EDINET.

#### 2. Funcționalități Cheie

- **Import orar al comenzilor:** o acțiune programată citește comenzile noi (ORDERS) ale fiecărei companii din EDINET și creează comenzile de vânzare; retailerul și punctul de livrare se găsesc după GLN, iar produsele după codurile proprii ale retailerului. Fiecare comandă importată este confirmată înapoi în EDINET.
- **Verificare Edinet:** compară comanda de vânzare cu comanda EDINET din care provine (punct de livrare, produse, cantități, prețuri) și listează diferențele în chatter; verificarea este strict read-only.
- **Reimport EDI:** importă din nou comanda din mesajul XML păstrat atașat, fără intervenția suportului.
- **Facturi către retailer:** factura clientului postată se trimite la EDINET cu un clic sau în lot din lista de facturi; notele de credit pot fi trimise ca factură storno, de retur sau de corecție, cu numărul comenzii retailerului (**EDI Order Number**).
- **Aviz de expediție (DESADV):** livrarea este trimisă la EDINET ca aviz de expediție înainte de sosirea mărfii (export EDI pe transfer).
- **Linii de comandă din Excel:** liniile se pot importa într-o comandă de vânzare dintr-un fișier Excel (acțiunea de import Edinet de pe comandă).
- **Mai multe companii:** fiecare companie are propriul utilizator, parolă și adresă de servicii EDINET, deci conturile de test și de producție pot fi ținute separat.
- **Configurare:** în *Setări > Setări generale*, secțiunea **EDI Net**, se completează utilizatorul, parola și **șablonul URL WSDL** (cu `{service}` în locul numelui serviciului; Infinite furnizează adresele de test și de producție). Fără ele, exportul se oprește cu eroare de configurare, iar importul sare peste companie. Pe retailer se setează sistemul EDI *EDI Net* și codurile **GLN** (ale retailerului și ale punctelor de livrare); pe produse se completează codurile retailerului. Acțiunea programată *Edinet: Get Orders* trebuie verificată că este activă (în datele modulului este livrată inactivă).
- **Control acces dedicat:** butoanele de reimport și verificare sunt restricționate la grupul *Edinet: reimport și verificare comenzi*, implicat de *Vânzări / Administrator*.
- **Date trimise către Infinite EDINET:** facturile și avizele retailerilor care folosesc EDINET, cu linii, cantități, prețuri, numere de comandă și coduri GLN; modulul citește și comenzile retailerilor, conectându-se cu utilizatorul și parola fiecărei companii.

#### 3. Dependențe

- [deltatech_edi](../deltatech_edi/index.md)

Dependențe externe Python: `zeep`, `xmltodict`, `xlrd`.

#### 4. Componente Cheie

> Conform `readme/DESCRIPTION.md`, secțiunile de business sunt acoperite mai sus. Următoarele componente sunt sintetizate din `__manifest__.py` și cod, pentru orientare tehnică.

**Modele**

- `sale.order` (extindere): adaugă `corn_import_edinet` (cron de import ORDERS), `action_reimport_edinet_button` (reimport din atașamentul XML), `action_check_edinet_button` / `_check_edinet_message` (verificare read-only față de documentul Edinet: adresă, produse, cantități, prețuri) și `_export_edinet_data` (trimitere comandă).
- `account.move` (extindere): adaugă `export_edinet_button` / `action_mass_export_edinet` pentru exportul facturilor validate către EDINET (individual sau în masă) și suprascrie `button_export_edi` pentru partenerii cu `edi_system == "edi_net"`.
- `stock.picking` (extindere): `export_edinet_button` / `_export_edinet_data` trimit avizul de expediție (DESADV) la EDINET.
- `res.partner` (extindere): adaugă valoarea *EDI Net* în `edi_system` și câmpurile `edi_id_bayer`, `edi_id_seller`.
- `import.sale.edinet.line` (wizard): importă liniile unei comenzi de vânzare dintr-un fișier Excel.
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
