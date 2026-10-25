# Romania - Conformitate fiscală POS (AMEF) (localizat la `l10n_ro_pos_fiscal_compliance/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_fiscal_compliance`
- **Versiune:** `19.0.2.3.3`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_pos_fiscal_compliance`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_fiscal_compliance`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul asigură conformitatea fiscală pentru vânzarea cu amănuntul prin POS, conform OUG 28/1999 privind aparatele de marcat electronice fiscale (AMEF). Completează POS-ul Odoo și driverele de fiscalizare (ex. `deltatech_pos`) cu evidența fiscală cerută în România: urmărirea bonului fiscal pe fiecare comandă, blocarea închiderii sesiunii când există comenzi plătite fără bon emis, raportul Z reconciliat cu vânzările și încasările, returul fiscal legat de bonul inițial și arhivarea jurnalului electronic AMEF. Modulul importă exportul casei de marcat pentru ANAF (o arhivă `.zip` cu fișiere `.p7b` sau un singur `.p7b`, semnate CMS/PKCS7 de aparat), citit după structura ANAF A4200/A4203 din OPANAF 146/2018 și verificat pe exporturi reale Datecs. Recunoaște aparatul după NUI, reconciliază automat, bon cu bon, bonurile cu comenzile din Odoo și completează raportul Z al zilei cu cifrele aparatului: totalul, plățile pe tip și valoarea și TVA-ul pe fiecare cotă, cu diferențele față de Odoo. Modulul oferă și raportul **Vânzări TVA pe casă de marcat** — un sumar pivot/listă peste liniile de TVA ale rapoartelor Z deja existente, pe interval de dată, punct de lucru și cotă de TVA, util pentru verificarea rapidă a încasărilor declarate fiscal pe orice perioadă, comparabil direct cu jurnalul electronic transmis către ANAF. Modulul acoperă latura de conformitate (evidență, blocaj, raport Z, arhivă, import, reconciliere și raportare TVA) peste POS-ul Odoo; comunicarea efectivă cu aparatul fiscal se face printr-un driver opțional, modulul nedepinzând de un driver anume.

#### 2. Funcționalități Cheie

- **Urmărirea bonului fiscal** pe fiecare comandă POS: serie, număr, dată/oră fiscală și stare (de fiscalizat / emis / eroare), cu punct de integrare pentru răspunsul aparatului fiscal.
- **Blocarea închiderii sesiunii** POS dacă există comenzi plătite fără bon fiscal emis și fără eroare justificată.
- **Raportul Z fiscal** cu defalcare pe cote TVA și pe metode de plată, reconciliat cu vânzările și încasările din Odoo, evidențiind diferențele.
- **Returul fiscal** care referențiază bonul inițial.
- **Arhiva jurnalului electronic AMEF** (fișiere pe perioadă și aparat fiscal, cu stări Draft / Parsed / Archived).
- **Import automat al arhivei fiscale**: butonul „Importă arhiva" (acceptă un `.zip` sau un singur fișier `.p7b`, fără arhivă) extrage conținutul XML din fiecare fișier `.p7b` (structură CMS/PKCS7 SignedData, prin biblioteca `asn1crypto`, fără shell-out la `openssl` și fără nevoie de certificat sau cheie privată), parsează bonurile fiscale și raportul Z al fiecărei zile.
- **Parser conform structurii ANAF** (OPANAF 146/2018, anexa 2, A4200/A4203): numărul Z, data și NUI-ul se citesc din identificatorii `idR`, `idB`, `idM`; plățile se citesc pe tipul ANAF `tipP` (inclusiv avans în numerar, tichete valorice, metode moderne de plată).
- **NUI aparat fiscal** (și seria aparatului) pe punctul de vânzare, preluate automat pe jurnal; bonul se potrivește pe aparat, număr bon în Z și zi, iar importul se oprește dacă fișierele vin de la alt aparat. Copia `OPIS_fiscalwire_*.xml`, ilizibilă, se ignoră cu o notă.
- **Reconciliere** a bonurilor cu `pos.order` pe serie + număr bon, cu fallback euristic (dată apropiată + sumă identică, aceeași zi și punct de lucru) doar dacă bonul nu are corespondent cu serie/număr.
- **Populare automată a raportului Z** (`l10n.ro.pos.z.report`) din arhivă: totalul declarat al Z-ului din aparat (nu suma bonurilor), plățile declarate pe metodă și defalcarea pe cote declarată de aparat (valoare cu TVA și TVA, cu diferența față de Odoo; pozițiile cu aceeași cotă se adună). Importul completează și raportul Z creat manual fără număr Z, în loc să creeze un duplicat pe aceeași zi și casă; coloanele declarate rămân goale unde aparatul nu a dat date.
- **Reconciliere strictă a plăților**: raportul Z e „Reconciliat" doar dacă fiecare tip de plată coincide (un plus pe card nu mai compensează un minus pe numerar).
- **Coerența internă a fiecărui Z**, verificată la import, cu abaterile în notele jurnalului: total Z diferit de suma bonurilor sau a plăților, TVA diferit de suma pe cote, numerotarea bonurilor.
- **Verificarea completitudinii perioadei** din fișierul OPIS al arhivei: Z-urile lipsă se calculează din intervalul `nrRapI..nrRapF` și apar în câmpul „Rapoarte Z lipsă (OPIS)" din grupul perioadei.
- **Raport de discrepanțe pe bonuri fiscale** (`l10n.ro.amef.journal.bon`), cu stări: Reconciliat, Sumă diferită, TVA diferit, Lipsă în Odoo, Lipsă în arhiva fiscală — accesibil dintr-un meniu dedicat „Discrepanțe bonuri fiscale" (deschis filtrat pe discrepanțe) sau din butonul statistic al jurnalului. Un bon cu același total dar alt TVA apare acum „TVA diferit"; pe rândurile „Lipsă în arhiva fiscală", numărul bonului din comandă apare în „Nr. bon în Z (BF)", iar idB rămâne gol.
- **Raportul „Vânzări TVA pe casă de marcat"** (*Point of Sale → Fiscalizare AMEF → Vânzări TVA pe casă de marcat*): agregă liniile de TVA ale rapoartelor Z deja existente, fără recalculare, filtrabil pe interval de dată, punct de lucru și cotă de TVA, cu vizualizare pivot (implicit) și listă; implicit sunt afișate doar rapoartele Z reconciliate/închise.

#### 3. Dependențe

- `point_of_sale`
- `account`
- `l10n_ro`

Dependență externă Python (nu modul Odoo): `asn1crypto`, folosită pentru decodarea CMS/PKCS7 a fișierelor `.p7b` din arhivă.

#### 4. Componente Cheie

**Modele**

- `pos.order` (extindere): câmpurile de bon fiscal (serie, număr, dată/oră fiscală, stare de fiscalizare) și referința la bonul inițial pentru retur.
- `pos.config` / `res.config.settings` (extindere): bifa „Fiscalizare AMEF obligatorie" și seria și NUI-ul aparatului fiscal per punct de lucru.
- `pos.session` (extindere): blocarea închiderii sesiunii cât timp există comenzi plătite fără bon fiscal emis și fără eroare justificată.
- `l10n.ro.pos.z.report` (+ liniile asociate pe cote TVA și pe metode de plată): raportul Z fiscal, cu valori calculate din sesiune vs. valori declarate de aparat, și acțiunea de reconciliere.
- `l10n.ro.pos.z.report.vat.line`: liniile de TVA ale raportului Z; primite acum trei câmpuri `related`+`store` — `report_date` (din `z_report_id.date`), `config_id` (din `z_report_id.config_id`), `device_serial` (din `z_report_id.config_id.l10n_ro_fiscal_device_serial`) și `report_state` (din `z_report_id.state`) — care alimentează raportul „Vânzări TVA pe casă de marcat" fără nicio recalculare, doar agregare peste liniile deja existente.
- `l10n.ro.amef.journal`: jurnalul electronic AMEF — arhiva `.zip` atașată, perioada, punctul de lucru și seria aparatului; orchestrează extragerea, parsarea și reconcilierea (`action_import_zip`) și arhivarea finală (`action_archive_journal`).
- `l10n.ro.amef.journal.bon` (model nou): o linie per bon fiscal găsit în arhivă, cu starea potrivirii cu `pos.order` (Matched / Amount Mismatch / VAT Mismatch / Missing in Odoo / Missing in Fiscal Archive) și notele de potrivire.
- `l10n_ro_amef_parser` (modul Python, fără model ORM): funcțiile de extragere XML din CMS/PKCS7 (`extract_xml_from_p7b`), detectarea tipului de declarație AMEF, desfacerea identificatorilor (NUI, dată/oră, nr. Z, nr. bon), parsarea raportului Z (`parse_declaratie_z`) și a fișierului OPIS (`parse_opis`), pe structura ANAF A4200/A4203.

**Vizualizări**

- `pos_config_views.xml`: secțiunea „Conformitate fiscală RO (AMEF)" în Setările POS.
- `pos_order_views.xml`: fila „Fiscalizare AMEF" pe formularul comenzii POS.
- `l10n_ro_pos_z_report_views.xml`: formularul și lista raportului Z, cu liniile pe TVA și plăți și acțiunea de reconciliere.
- `l10n_ro_pos_z_report_summary_views.xml` (nou): căutare, listă și pivot pe `l10n.ro.pos.z.report.vat.line` pentru raportul „Vânzări TVA pe casă de marcat" — grupare implicită pe punct de lucru și cotă TVA, filtru implicit pe rapoarte Z reconciliate/închise, cu filtre suplimentare de grupare pe dispozitiv fiscal și pe dată.
- `l10n_ro_amef_journal_views.xml`: formularul jurnalului electronic AMEF, cu atașarea arhivei, butoanele „Importă arhiva" / „Arhivează" / „Resetează la ciornă", fila „Fiscal Receipts" (bonurile reconciliate), câmpul „Missing Z Reports (OPIS)" și butonul statistic de discrepanțe.
- `pos_menus.xml`: meniul rădăcină „AMEF Fiscalization" cu submeniurile „Z Reports", „VAT Sales by Fiscal Device" (nou), „AMEF Electronic Journals" și „Fiscal Receipts Discrepancies".

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron` sau `base.automation`; procesarea (import arhivă, parsare, reconciliere) rulează sincron, la apăsarea butoanelor `action_import_zip` / `action_archive_journal` de pe jurnalul AMEF. Raportul „Vânzări TVA pe casă de marcat" (`action_l10n_ro_pos_z_report_vat_summary`) e o simplă acțiune de fereastră (pivot+listă), fără procesare pe server — doar filtrare/agregare a datelor existente.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): driver de fiscalizare POS care poate apela metoda publică de înregistrare a răspunsului fiscal (integrare opțională; modulul nu depinde de el).
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): agregă bonurile fiscale POS în declarația D394, dacă este instalat (integrare prin convenție, realizată de modulul D394, nu de acesta).
