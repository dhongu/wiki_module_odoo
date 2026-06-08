# eFactura Enhancement (localizat la `l10n_ro_efactura_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_enhancement`
- **Versiune:** `19.0.0.3.7`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_efactura_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_efactura_enhancement`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul `l10n_ro_efactura_enhancement` extinde funcționalitatea standard de e-Facturare (e-Factura) din Odoo pentru piața din România, adăugând îmbunătățiri și automatizări care optimizează experiența utilizatorului și acoperă nevoi specifice de conformitate fiscală. Acesta validează datele obligatorii ale partenerilor români, automatizează trimiterea și urmărirea facturilor în SPV și asigură că fișierele XML generate respectă constrângerile standardului UBL, reducând astfel erorile și efortul manual.

#### 2. Funcționalități Cheie

- **Completare automată cu 13 de zero** în câmpul de TVA pentru persoanele fizice, la generarea e-facturii.
- **Validare îmbunătățită a adresei**: verifică automat că partenerii români au definite țara, județul, orașul și strada înainte de postarea facturii.
- **Sugestie format EDI**: sugerează automat formatul `ciusro` pentru partenerii români.
- **Operațiuni automate pentru e-Factură**:
    - Sarcină cron pentru **trimiterea automată** a facturilor postate în SPV.
    - Sarcină cron pentru **preluarea statusului** din SPV pentru facturile trimise.
    - **Acțiune server „Trimite in SPV"**: permite trimiterea directă în SPV a facturilor selectate din lista de facturi, fără a declanșa trimiterea emailului.
    - **Opțiune de configurare**: o setare în pagina de configurare Contabilitate controlează dacă jobul cron automat de SPV suprimă trimiterea de email (trimite doar în SPV).
- **Trunchiere și sanitizare a datelor**:
    - Trunchiază denumirile produselor la 100 de caractere și descrierile la 200 de caractere, pentru conformitate cu standardul UBL.
    - Trunchiază notele la 300 de caractere.
    - Trunchiază referințele comenzii și avizul de expediere la 200 de caractere.
- **Integrare POS**: schimbă automat codul tipului de document la 751 (Factură specializată) pentru facturile provenite din Punctul de Vânzare.
- **Parametri de sistem configurabili**:
    - `efactura.embed_pdf`: controlează includerea PDF-ului încorporat în e-factură (implicit: True).
    - `efactura.use_line_description`: dacă e activat, folosește descrierea liniei de factură în locul numelui/descrierii produsului (implicit: False).
    - `efactura.replace_unit_uom`: permite specificarea unui cod de unitate de înlocuire pentru unitatea standard „C62" (implicit: False).
    - `efactura.get_all_banks`: dacă e activat, include toate băncile marcate cu `l10n_ro_print_report` care corespund monedei facturii (implicit: False).
- **Urmărirea lungimii liniilor**: adaugă câmpuri calculate pe liniile de factură pentru a urmări lungimea descrierilor și a denumirilor de produse, ajutând utilizatorii să identifice posibilele probleme de trunchiere.

#### 3. Dependențe

- `l10n_ro_edi`
- `l10n_ro_config`
- `spreadsheet_dashboard`
- `l10n_ro_message_spv`
- `account_edi_ubl_cii`
- `spreadsheet_dashboard_account`

#### 4. Componente Cheie

Conform secțiunii „Technical Implementation" din `readme/DESCRIPTION.md`, modulul moștenește și extinde mai multe modele de bază Odoo și de localizare românească.

**Modele**

- `account.move`: adaugă validări, joburile cron și gestionarea tipului de document pentru POS.
- `account.edi.xml.ubl_ro`: îmbunătățește generarea UBL cu logică custom pentru adrese, descrieri de produse și suport multi-bancă.
- `res.partner`: suprascrie sugestia de format EDI pentru entitățile românești.
- `account.move.line`: adaugă elemente UI ajutătoare pentru lungimea etichetelor.

**Acțiuni Automate / Acțiuni Server**

- Cron de **trimitere automată** a facturilor postate în SPV.
- Cron de **preluare a statusului** din SPV pentru facturile trimise.
- Acțiune server **„Trimite in SPV"**: trimite facturile selectate direct în SPV din lista de facturi, fără trimitere de email.

#### 5. Conexiuni

- `l10n_ro_edi`: nucleul EDI/OAuth2 ANAF pentru localizarea românească, peste care acest modul adaugă automatizări.
- `l10n_ro_message_spv`: gestionarea mesajelor SPV, folosită la trimiterea și urmărirea facturilor.
- `l10n_ro_config`: configurarea de bază a localizării românești.
