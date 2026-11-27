# Romania - Corecții la exportul SAF-T D406 (localizat la `l10n_ro_saft_export_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_export_fix`
- **Versiune:** `19.0.1.9.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_export_fix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_export_fix`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul corectează șase defecte ale exportului SAF-T D406 din modulul Enterprise `l10n_ro_saft`, descoperite prin confruntarea fișierelor generate de Odoo cu validatorul oficial `D406Validator` din DUK Integrator și cu nomenclatorul ANAF de coduri de taxă. Printre ele: secțiuni goale care fac declarația nedepunabilă, plăți lăsate în afara declarației, TVA dedus raportat ca nedeductibil la deducerea limitată la 50%, operațiuni cu taxă de 0% raportate în afara sferei TVA, cod poștal gol în adresa partenerului și conturi cu litere în cod respinse de validator. Din versiunea 1.5.0, modulul completează și identificatorii firmei și ai partenerilor, conform tipurilor ANAF. Corecțiile se aplică fără a modifica codul Enterprise, iar declarațiile care validează deja pe baza extraselor rămân identice. Defectele sunt raportate și către Odoo; modulul acoperă perioada până la rezolvarea în amonte.

#### 2. Funcționalități Cheie

- **Eliminarea secțiunilor goale:** `SalesInvoices`, `PurchaseInvoices` și `Payments` sunt scrise doar dacă au cel puțin un document. O lună fără achiziții nu mai duce la respingerea întregului fișier.
- **Raportarea plăților fără extras:** plățile din „Înregistrează plata" și operațiunile de casă (jurnalele de casă nu mai lucrează cu extrase din 17.0) apar în `Payments`, cu latura de trezorerie citită de pe contul de tranzit (5125 / 581). `PaymentMethod` este `01` pentru numerar și `03` pentru transfer. Jurnalul de casă trebuie să aibă cont de plăți configurat (ex. 531101), altfel plata nu are notă contabilă.
- **Fără dublare:** o plată reconciliată cu un extras se raportează o singură dată, prin nota extrasului.
- **TVA cu deducere limitată la 50%:** taxa „21% ND 50%" are un singur cod SAF-T (391104), iar exportul standard însuma ambele jumătăți sub el. Modulul separă suma după repartiția taxei: partea de pe contul de TVA (4426) primește codul deductibil (341104), partea de pe cheltuială (6352) păstrează 391104. Regula se aplică și pe 19%, 11%, 9% și 5% (391101–391105 devin 341101–341105), iar codurile apar în `TaxTable`. Codul taxei nu se schimbă manual.
- **Taxe de 0%:** linia de bază iese cu tipul și codul SAF-T al taxei (ex. 308302 pentru „0% EXEMPT", 310301 pentru „0% EU G"), cu suma zero, iar taxa e adăugată în `TaxTable`, deci codurile se potrivesc cu D300. O taxă de 0% fără tip sau cod SAF-T completat rămâne pe `000/000000`.
- **Cod poștal:** tagul `<PostalCode/>` se scrie doar când partenerul are cod poștal; șablonul comun, folosit de alte țări, rămâne neschimbat.
- **Conturi cu litere în cod:** `AccountID` devine număr întreg, înlocuind fiecare grup de litere cu un cod fix de 3 cifre dintr-un tabel salvat în bază (`4111RUE5194` devine `41110015194`), consecvent în tot fișierul și în toate lunile. `StandardAccountID` primește codul real. Câmpul opțional „Cod SAF-T" de pe cont (Contabilitate → Configurare → Plan de conturi) are prioritate; un cod generat care se suprapune cu alt cont oprește exportul. Secțiunile `Owners` și `Stocks` din `l10n_ro_saft_stock` nu sunt acoperite.
- **Produse și linii de factură:** `GoodsServicesID` (`01` bunuri, `02` servicii) și `ValuationMethod` (FIFO / Cost mediu) din categoria produsului; `UOMTable` cu o intrare pe cod UNECE; `ProductCode` și `ProductDescription` pe liniile facturii; la achiziții, `InvoiceNo` este referința furnizorului (fără ea, numărul intern, cu avertisment).
- **Identificatorii firmei:** în `Header/Company`, `RegistrationNumber` păstrează RO, iar `TaxRegistration` are numărul fără RO, `TaxType` 100010 (100040 la TVA la încasare), `TaxNumber` și `TaxAuthority` ANAF.
- **Contact unic:** firma trimite un singur contact, cu funcția în `OtherTitles`, ales în Contabilitate → Configurare → Setări → „Persoană de contact SAF-T", altfel administratorul, altfel primul contact cu nume și telefon. Clienții și furnizorii nu mai trimit blocul `Contact`.
- **`CustomerID` / `SupplierID`:** `00` + CUI (România), `01` + țară + cod TVA (UE), `02` (în afara UE), `03` + CNP, `04` + cod intern (România fără CUI/CNP), `05` / `06` + țară + cod intern (firmă străină fără cod de TVA). Codul intern este referința internă a partenerului fără caractere speciale, altfel ID-ul din bază.
- **Fără meniuri noi:** declarația se generează ca înainte, din Contabilitate → Raportare → Registre → Carte Mare, meniul ⚙ → „SAF-T (Declarația D406)". Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).
- **Flux recomandat:** se rulează întâi `l10n_ro_saft_validator`, apoi se generează declarația și se validează cu DUK Integrator înainte de depunere.

#### 3. Dependențe

- `l10n_ro_saft` (modul Enterprise; fără pagină wiki). Spre deosebire de [l10n_ro_saft_fix](../l10n_ro_saft_fix/index.md), care nu depinde de el ca să se încarce înaintea lui, aici modulul trebuie încărcat DUPĂ, ca să poată moșteni șablonul și modelul de raport.

#### 4. Componente Cheie

**Modele**

- `account.general.ledger.report.handler` (abstract, extins): nucleul modulului. Suprascrie metodele `_l10n_ro_saft_fill_*` din `l10n_ro_saft` pentru taxe (separare deductibil/nedeductibil, taxe de 0%), plăți (include plățile fără extras, cu liniile de trezorerie corecte), produse, unități de măsură, linii de factură, parteneri și antet, plus calculul `AccountID` numeric și al identificatorilor firmei și partenerilor.
- `l10n_ro.saft.letter.code` (nou): corespondența fixă, pe companie, între un grup de litere din codul contului și un cod numeric de 3 cifre (unic pe companie, atât după litere, cât și după cod).
- `account.account` (extins): câmpul opțional `l10n_ro_saft_code` (Cod SAF-T) cu validări și funcția care furnizează codul numeric de export.
- `res.company` (extins): câmpul `l10n_ro_saft_contact_id`, persoana de contact trimisă în D406.
- `res.config.settings` (extins): expune persoana de contact SAF-T în setările contabilității.

**Vizualizări**

- `saft_template` și celelalte șabloane QWeb moștenite din `l10n_ro_saft` / `account_saft` (`saft_template_postal_code`, `addresses_contacts_postal_code`, `addresses_contacts_identifiers`, `saft_template_invoices_account_id`, `saft_template_products_goods_services`, `saft_template_invoices_product_lines` ș.a.): mută condiția pe tag la secțiunile goale, elimină `PostalCode` gol (prin copia `address`), folosesc `AccountID` numeric, completează produsele și identificatorii.
- `view_account_form_saft_code` / `view_account_list_saft_code`: câmpul „Cod SAF-T" pe formularul și lista contului.
- `res_config_settings_form_saft_contact`: câmpul „Persoană de contact SAF-T" în setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_saft_fix](../l10n_ro_saft_fix/index.md): modul distinct, care rezolvă o problemă de instalare a `l10n_ro_saft` (construit fără `depends` pe acesta); nu se suprapune cu corecțiile de export de aici (menționat în manifest).
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): verificare înainte de export, recomandată în documentația modulului (fără dependență în manifest sau cod).
