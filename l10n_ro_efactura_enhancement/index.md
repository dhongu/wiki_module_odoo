# e-Factura Enhancements (localizat la `l10n_ro_efactura_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_efactura_enhancement`
- **Versiune:** `20.0.0.5.11`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_efactura_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_efactura_enhancement`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde e-Factura standard din Odoo pentru piața din România, cu validări și automatizări care reduc erorile și munca manuală. Validează datele obligatorii ale partenerilor români, trimite automat facturile postate în SPV și urmărește statusul lor, iar XML-urile generate rămân în limitele de lungime ale standardului UBL / CIUS-RO. Include și un tablou de bord „eFactura SPV" pentru monitorizarea trimiterilor.

#### 2. Funcționalități Cheie

- **Completare automată cu 13 zerouri** în câmpul de TVA pentru persoanele fizice, la generarea e-facturii; o firmă din România fără CUI nu mai pleacă în SPV.
- **Validare de adresă**: partenerii români trebuie să aibă țara, județul, orașul și strada completate înainte de postarea facturii.
- **Sugestie de format EDI**: `ciusro` pentru partenerii români.
- **Automatizări e-Factura**:
    - cron pentru **trimiterea automată** a facturilor postate în SPV (cu limită de 3 reîncercări pe factură);
    - cron pentru **preluarea statusului** din SPV;
    - cron pentru trimiterea emailului cu facturile validate și raport de rulare a cron-ului;
    - **acțiune server „Trimite in SPV"** din lista de facturi, fără trimitere de email;
    - setare în Contabilitate care controlează dacă cron-ul trimite doar în SPV, fără email;
    - setare per companie „Nu importa automat facturile primite din SPV", care evită duplicarea facturilor de furnizor, păstrând sincronizarea statusului facturilor trimise;
    - buton „Retrimite în SPV" pentru facturile respinse și tratarea facturilor rămase „Neindexate".
- **Trunchiere și sanitizare**: denumiri de produs la 100 de caractere, descrieri la 200, note la 300, referințe de comandă și aviz la 200 (avizul de plată la 140, conform BR-RO-L140).
- **Integrare POS**: facturile provenite din Punctul de Vânzare pleacă cu tipul de document 751 (factură specializată).
- **Storno**: nota de credit pleacă în SPV cu referința facturii corectate (număr și dată).
- **Parametri de sistem**: `efactura.embed_pdf` (implicit True), `efactura.use_line_description` (False), `efactura.replace_unit_uom` (cod de înlocuire pentru `C62`) și `efactura.get_all_banks` (include băncile marcate pentru tipărire, în moneda facturii).
- **Urmărirea lungimii liniilor**: câmpuri calculate pe liniile de factură pentru lungimea descrierii și a denumirii produsului.
- **Tablou de bord „eFactura SPV"** (spreadsheet dashboard) pentru starea trimiterilor.
- Fluxul pas-cu-pas, cu capturi, se află în fișa de consultant.

#### 3. Dependențe

- `l10n_ro_edi`
- [l10n_ro_report_common](../l10n_ro_report_common/index.md)
- `spreadsheet_dashboard`
- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md)
- `account_edi_ubl_cii`
- `spreadsheet_dashboard_account`

#### 4. Componente Cheie

**Modele**

- `account.move`: validări, cron-uri, contor de trimiteri eșuate, tip 751 pentru POS, retrimitere în SPV.
- `account.edi.xml.ubl_ro` / `account.edi.ubl` / `account.edi.xml.ubl_bis3`: generarea UBL cu logică proprie pentru adrese, descrieri, trunchieri și bănci multiple.
- `res.partner`: sugestia formatului EDI pentru entitățile românești.
- `account.move.line`: ajutoare de interfață pentru lungimea etichetelor.
- `res.company` / `res.config.settings`: setările e-Factura SPV.
- `account.move.send` / `account.move.send.wizard`: comportamentul de trimitere pentru e-Factura.
- `l10n.ro.efactura.dashboard`: sursa tabloului de bord „eFactura SPV".

**Vizualizări**

- Extinderi ale formularului/listei de factură, ale setărilor de configurare și vizualizările tabloului de bord (`account_move.xml`, `res_config_settings_views.xml`, `efactura_dashboard_views.xml`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_l10n_ro_edi_auto_send` („E-Factura: Send TO SPV"): trimite zilnic facturile postate în SPV.
- `ir_cron_l10n_ro_edi_fetch_status` („E-Factura: Fetch From SPV"): la 4 ore, preia statusul facturilor trimise.
- `ir_cron_l10n_ro_spv_send_validated_emails`: la 15 minute, trimite emailurile facturilor validate de ANAF.
- `action_send_invoices_to_spv_only`: acțiune server „Trimite in SPV" din lista de facturi.

#### 5. Conexiuni

- `l10n_ro_edi`: nucleul EDI/OAuth2 ANAF pentru localizarea românească, peste care acest modul adaugă automatizări.
- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md): mesajele SPV, folosite la trimiterea și urmărirea facturilor.
- [l10n_ro_report_common](../l10n_ro_report_common/index.md): definește câmpul `l10n_ro_print_report` al conturilor bancare, folosit când `efactura.get_all_banks` este activ.
- [l10n_ro_edi_ubl_sale_store](../l10n_ro_edi_ubl_sale_store/index.md): regula 751 pentru vânzările cu bon fiscal.
