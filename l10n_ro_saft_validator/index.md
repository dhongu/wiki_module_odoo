# Romania - Pre-validator SAF-T D406 (localizat la `l10n_ro_saft_validator/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_validator`
- **Versiune:** `20.0.1.3.10`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_validator](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_validator)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_validator`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md) — overview, cu fișe dedicate pe speță: [L/T](FISA_CONSULTANT_LT.md), [A](FISA_CONSULTANT_A.md), [C](FISA_CONSULTANT_C.md)

#### 1. Sumar

Modulul rulează verificări **înainte** de generarea declarației SAF-T D406, identificând datele incomplete care ar duce la respingerea fișierului de către ANAF. Wizardul acoperă cele trei spețe de depunere (lunar/trimestrial, anual pentru active, la cerere pentru stocuri) și arată problemele ca listă structurată, fiecare cu legătură directă la înregistrarea de corectat. Verificările se uită și la documentele perioadei, nu doar la configurație, iar regulile provin din confruntarea unui fișier generat de Odoo cu validatorul oficial `D406Validator` din DUK Integrator. Totul rulează local, fără apeluri externe.

#### 2. Funcționalități Cheie

- **Trei seturi de verificări** după *Tip declarație*: **LT** (lunar/trimestrial), **A** (anual — active), **C** (la cerere — stocuri); verificarea datelor de companie rulează pentru toate. Meniu: **Contabilitate → Raportare → Validator SAF-T**.
- **Date de companie și prerechizite de export:** CUI, adresă, județ, telefon, cont bancar, baza de impozitare SAF-T și un contact cu nume din două cuvinte și telefon. În Odoo 20, firma neplătitoare de TVA are CUI-ul în „Company ID" (identificatorul `RO_EN`), la fel și CNP-ul persoanelor fizice; se semnalează lipsa ambelor coduri sau un CUI cu cifră de control greșită.
- **Parteneri cu rulaj:** fără CUI/CNP, fără țară sau cu cod non-ISO2, fără localitate, fără județ sau cu județ în afara nomenclatorului ISO 3166-2:RO; tip fiscal incoerent (țara și prefixul TVA se contrazic, ceea ce decide `RegistrationType`). Un partener fără TVA și fără CUI/CNP e semnalat ca persoană fizică (avertisment).
- **Note contabile fără partener** pe conturi de creanțe/datorii (40x/41x); conturile „Non-comercial" nu sunt verificate.
- **Secțiuni care ar ieși goale** (`SalesInvoices`, `PurchaseInvoices`, `Payments`) și **plăți absente din export** (doar cele venite dintr-un extras bancar ajung în fișier).
- **Articole, conturi și taxe:** referință internă, categorie, conturi de venit/cheltuială lipsă; conturi fără `account_type`; taxe fără tipul SAF-T.
- **Speța A — active:** imobilizări fără categorie SAF-T mapată. **Speța C — stocuri:** tipuri de operație fără cod de mișcare și unități de măsură fără cod UNECE.
- **Severități și buclă de corecție:** erori (blochează), avertismente (recomandate), informații; după corectare se reapasă *Validează* până apare „Nicio problemă detectată".
- Nu generează fișierul XML; exportul se face cu `l10n_ro_saft` (Enterprise), apoi validare oficială cu DUK Integrator. Fluxul pas-cu-pas este în fișele consultant.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.saft.validator`: wizardul (transient) care rulează verificările; câmpurile `declaration_type`, `date_from`/`date_to` și contoarele de erori/avertismente/informații; `action_validate` orchestrează verificările pe speță.
- `l10n.ro.saft.validator.line`: linia de rezultat — severitate, tip de verificare, mesaj și legături către partener, cont, notă contabilă sau articol.

**Vizualizări**

- `view_l10n_ro_saft_validator_form`: formularul wizardului (bannere pe severitate, sumar, lista problemelor), cu acțiunea `action_l10n_ro_saft_validator` și meniul `menu_l10n_ro_saft_validator`.
- `demo/account_asset_demo.xml`: active demo cu categorie SAF-T mapată, pentru speța A.
- `security/ir.access.csv`: drepturile pe cele două modele tranzitorii.

**Acțiuni Automate / Acțiuni Server**

*Nu sunt definite acțiuni automate; validarea se rulează manual din wizard.*

#### 5. Conexiuni

- `l10n_ro_saft` (Enterprise): generează efectiv fișierul D406 din raportul Cartea Mare; sursa mai multor reguli de verificare.
- `l10n_ro_saft_stock` (Enterprise): exportul pentru speța C și codul de mișcare pe tipul de operație.
- [l10n_ro_anaf_duk](../l10n_ro_anaf_duk/index.md): rulează DUK Integrator pe stația contabilului — validarea oficială de după această pre-verificare.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): verificare încrucișată — soldurile din SAF-T trebuie să corespundă cu D300.
