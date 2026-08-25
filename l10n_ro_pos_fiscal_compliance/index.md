# Romania - Conformitate fiscală POS (AMEF) (localizat la `l10n_ro_pos_fiscal_compliance/index.md`)

- **Nume Tehnic:** `l10n_ro_pos_fiscal_compliance`
- **Versiune:** `19.0.2.0.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_pos_fiscal_compliance`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_fiscal_compliance`
- **Ultima Ingestie:** `2026-08-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul asigură conformitatea fiscală pentru vânzarea cu amănuntul prin POS, conform OUG 28/1999 privind aparatele de marcat electronice fiscale (AMEF). Completează POS-ul Odoo și driverele de fiscalizare (ex. `deltatech_pos`) cu evidența fiscală cerută în România: urmărirea bonului fiscal pe fiecare comandă, blocarea închiderii sesiunii când există comenzi plătite fără bon emis, raportul Z reconciliat cu vânzările și încasările, returul fiscal legat de bonul inițial și arhivarea jurnalului electronic AMEF. Din versiunea 19.0.2.0.0, modulul poate importa direct arhiva periodică a casei de marcat (`.zip` cu fișiere `.p7b`, exportul semnat CMS/PKCS7 primit de la aparat), extrăgând bonurile și raportul Z fără intervenție manuală și reconciliindu-le automat, bon cu bon, cu comenzile din Odoo. Modulul acoperă latura de conformitate (evidență, blocaj, raport Z, arhivă, import și reconciliere) peste POS-ul Odoo; comunicarea efectivă cu aparatul fiscal se face printr-un driver opțional, modulul nedepinzând de un driver anume.

#### 2. Funcționalități Cheie

- **Urmărirea bonului fiscal** pe fiecare comandă POS: serie, număr, dată/oră fiscală și stare (de fiscalizat / emis / eroare), cu punct de integrare pentru răspunsul aparatului fiscal.
- **Blocarea închiderii sesiunii** POS dacă există comenzi plătite fără bon fiscal emis și fără eroare justificată.
- **Raportul Z fiscal** cu defalcare pe cote TVA și pe metode de plată, reconciliat cu vânzările și încasările din Odoo, evidențiind diferențele.
- **Returul fiscal** care referențiază bonul inițial.
- **Arhiva jurnalului electronic AMEF** (fișiere pe perioadă și aparat fiscal, cu stări Draft / Parsed / Archived).
- **Import automat al arhivei fiscale**: butonul „Importă arhiva" extrage conținutul XML din fiecare fișier `.p7b` (structură CMS/PKCS7 SignedData, prin biblioteca `asn1crypto`, fără shell-out la `openssl` și fără nevoie de certificat sau cheie privată), parsează bonurile fiscale și raportul Z al fiecărei zile.
- **Reconciliere pe FK exact** (serie + număr bon) cu `pos.order`; doar dacă bonul din arhivă nu are corespondent înregistrat cu serie/număr, se aplică un fallback euristic pe dată apropiată + sumă identică, în aceeași zi și punct de lucru.
- **Populare automată a raportului Z** (`l10n.ro.pos.z.report`) din arhivă: totalul declarat și plățile declarate pe metodă, urmate de reconcilierea automată cu totalurile din sesiunea POS.
- **Verificarea completitudinii perioadei** din fișierul OPIS al arhivei (declarația `a4200`): semnalează rapoartele Z lipsă între ce apare în OPIS și ce a fost efectiv găsit în arhivă.
- **Raport de discrepanțe pe bonuri fiscale** (`l10n.ro.amef.journal.bon`), cu stări: Reconciliat, Sumă diferită, TVA diferit, Lipsă în Odoo, Lipsă în arhiva fiscală — accesibil dintr-un meniu dedicat „Fiscal Receipts Discrepancies" sau din butonul statistic al jurnalului.

#### 3. Dependențe

- `point_of_sale`
- `account`
- `l10n_ro`

Dependență externă Python (nu modul Odoo): `asn1crypto`, folosită pentru decodarea CMS/PKCS7 a fișierelor `.p7b` din arhivă.

#### 4. Componente Cheie

**Modele**

- `pos.order` (extindere): câmpurile de bon fiscal (serie, număr, dată/oră fiscală, stare de fiscalizare) și referința la bonul inițial pentru retur.
- `pos.config` / `res.config.settings` (extindere): bifa „Fiscalizare AMEF obligatorie" și seria aparatului fiscal per punct de lucru.
- `pos.session` (extindere): blocarea închiderii sesiunii cât timp există comenzi plătite fără bon fiscal emis și fără eroare justificată.
- `l10n.ro.pos.z.report` (+ liniile asociate pe cote TVA și pe metode de plată): raportul Z fiscal, cu valori calculate din sesiune vs. valori declarate de aparat, și acțiunea de reconciliere.
- `l10n.ro.amef.journal`: jurnalul electronic AMEF — arhiva `.zip` atașată, perioada, punctul de lucru și seria aparatului; orchestrează extragerea, parsarea și reconcilierea (`action_import_zip`) și arhivarea finală (`action_archive_journal`).
- `l10n.ro.amef.journal.bon` (model nou): o linie per bon fiscal găsit în arhivă, cu starea potrivirii cu `pos.order` (Matched / Amount Mismatch / VAT Mismatch / Missing in Odoo / Missing in Fiscal Archive) și notele de potrivire.
- `l10n_ro_amef_parser` (modul Python, fără model ORM): funcțiile de extragere XML din CMS/PKCS7 (`extract_xml_from_p7b`), detectarea tipului de declarație AMEF, parsarea raportului Z (`parse_declaratie_z`) și a fișierului OPIS (`parse_opis`).

**Vizualizări**

- `pos_config_views.xml`: secțiunea „Conformitate fiscală RO (AMEF)" în Setările POS.
- `pos_order_views.xml`: fila „Fiscalizare AMEF" pe formularul comenzii POS.
- `l10n_ro_pos_z_report_views.xml`: formularul și lista raportului Z, cu liniile pe TVA și plăți și acțiunea de reconciliere.
- `l10n_ro_amef_journal_views.xml`: formularul jurnalului electronic AMEF, cu atașarea arhivei, butoanele „Importă arhiva" / „Arhivează" / „Resetează la ciornă", fila „Fiscal Receipts" (bonurile reconciliate), câmpul „Missing Z Reports (OPIS)" și butonul statistic de discrepanțe.
- `pos_menus.xml`: meniul rădăcină „AMEF Fiscalization" cu submeniurile „Z Reports", „AMEF Electronic Journals" și noul „Fiscal Receipts Discrepancies".

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron` sau `base.automation`; procesarea (import arhivă, parsare, reconciliere) rulează sincron, la apăsarea butoanelor `action_import_zip` / `action_archive_journal` de pe jurnalul AMEF.

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): driver de fiscalizare POS care poate apela metoda publică de înregistrare a răspunsului fiscal (integrare opțională; modulul nu depinde de el).
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): agregă bonurile fiscale POS în declarația D394, dacă este instalat (integrare prin convenție, realizată de modulul D394, nu de acesta).
