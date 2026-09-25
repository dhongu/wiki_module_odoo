# Romania - Taxare inversă art. 331 (localizat la `l10n_ro_reverse_charge_331/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reverse_charge_331
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331`
- **Ultima Ingestie:** `2026-09-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aplică automat taxarea inversă pe plan intern prevăzută de **articolul 331 din
Codul fiscal** (Legea 227/2015), și numai atunci când legea o permite. Articolul 331
listează livrările pentru care TVA-ul este datorat de cumpărător, nu de furnizor:
cherestea și materiale lemnoase, deșeuri feroase și neferoase, cereale și plante
tehnice, certificate de emisii de gaze cu efect de seră, energie electrică către un
comerciant, aur de investiții, telefoane mobile, dispozitive cu circuite integrate,
console de jocuri, tablete și laptopuri — dar doar dacă **atât furnizorul, cât și
cumpărătorul** sunt înregistrați în scopuri de TVA conform art. 316. Pentru o parte
neînregistrată, operațiunea rămâne taxabilă la cota standard. Odoo nu poate exprima
singur această condiție — poziția fiscală a regimului național din planul de conturi RO
se aplică automat oricărui partener, plătitor sau nu — așa că modulul adaugă taxe
dedicate, un gardian pe statutul de TVA al celeilalte părți și un blocaj la postarea
documentelor greșit configurate. De la versiunea 1.1.0, taxarea inversă acoperă și
partea de **achiziție**: cumpărătorul de bunuri art. 331 își autolichidează singur
TVA-ul, cu o taxă dedicată de 21%.

#### 2. Funcționalități Cheie

- Adaugă o taxă de vânzare dedicată, **0% R331**, raportată pe rândul 13 din decontul
  D300 („livrări supuse măsurilor de simplificare") și purtând mențiunea legală impusă
  de art. 331 alin. (3) pe o factură fără TVA colectată.
- Adaugă o taxă de achiziție dedicată, **21% R331**, care autolichidează TVA-ul
  (`Dr 4426 = Cr 4427`), cu baza și TVA-ul raportate pe rândurile 12.1 și 26.1 din D300;
  totalul facturii de furnizor rămâne suma netă, fiindcă furnizorul nu facturează TVA.
- Adaugă o bifă **Reverse Charge Art. 331** pe fiecare taxă domestică, de vânzare sau de
  achiziție — bifarea ei pe taxa folosită pentru cherestea, deșeuri sau cereale este
  întreaga configurare; modulul scrie singur maparea inversă din Odoo 19
  (`original_tax_ids` și `fiscal_position_ids`). Pe achiziție, taxa marcată trebuie să
  aibă aceeași cotă ca **21% R331** — cumpărătorul autolichidează la cota bunului, nu la
  o cotă arbitrară.
- Adaugă o bifă **Reverse Charge Art. 331** pe poziția fiscală a plătitorilor de TVA
  (consultantul o declară — poziția domestică a companiei nu poate fi dedusă automat,
  fiindcă pe o bază cu poziții separate pentru plătitori și neplătitori, la aceeași
  secvență, câștigă id-ul mai mic, care poate fi tocmai cea a neplătitorilor).
- Gardian pe înregistrarea în scopuri de TVA a celeilalte părți (câmpul RO „Plătitor de
  TVA — scpTVA" dacă e disponibil, altfel prefixul „RO" din CUI): pe vânzare se
  verifică cumpărătorul, pe achiziție furnizorul; înlocuirea de taxă se omite pentru o
  parte neînregistrată, atât pe ofertă/comandă de achiziție, cât și pe factură/bon.
- Blocaj la postare pentru orice factură de vânzare sau bon de furnizor care încă
  poartă taxa art. 331 către/de la o parte neînregistrată — acoperă poziții fiscale
  atribuite manual pe partener, taxe alese direct pe linie și documente importate.
- Refuză configurarea contradictorie: o taxă domestică deja înlocuită de altă taxă pe
  aceeași poziție fiscală, sau o taxă marcată care nu e domestică.
- Documentele deja existente nu sunt rescrise: taxele de pe oferte confirmate și
  facturi postate sunt stocate, nu recalculate; recalculul se declanșează schimbând
  partenerul sau poziția fiscală pe document.
- La instalare pe o bază cu plan de conturi deja încărcat, taxele **0% R331** și
  **21% R331** sunt create automat (sau adoptate, dacă existau deja create manual) și
  primesc etichetele de raportare de la taxele native `tvati` / `tvatip21` din `l10n_ro`.
- Materialele lemnoase derivate (PAL, OSB, placaj) nu intră sub incidența art. 331
  lit. b) și rămân pe taxa standard, separate de cheresteaua propriu-zisă, care nu are
  termen de expirare și nici prag valoric.
- Dacă `account_edi_ubl_cii` e instalat, taxa **0% R331** primește explicit codul
  UNCL5305 `AE` (motiv `VATEX-EU-AE`) pentru factura electronică, în loc de codul
  implicit `E` (scutit), semantic greșit pentru o taxare inversă.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.tax`: câmpurile `l10n_ro_reverse_charge_331` (bifă pe taxa domestică sursă,
  de vânzare sau de achiziție) și `l10n_ro_is_reverse_charge_331` (marcaj tehnic pe
  taxa de destinație, **0% R331** sau **21% R331**); ține maparea
  `original_tax_ids`/`fiscal_position_ids` sincronizată cu bifele, refuză o sursă
  nedomestică, o cotă de achiziție diferită de cea a autolichidării și o dublă
  înlocuire a aceleiași surse pe aceeași poziție fiscală.
- `account.fiscal.position`: câmpul `l10n_ro_reverse_charge_331`; suprascrie `map_tax`
  pentru a anula înlocuirea art. 331 când partenerul (cumpărătorul pe vânzare,
  furnizorul pe achiziție) nu e înregistrat în scopuri de TVA (citit din context, nu
  din partener, fiindcă `map_tax` nu primește partenerul).
- `account.move.line`: suprascrie `_get_computed_taxes` pentru a propaga în context
  statutul de TVA al partenerului relevant (beneficiar sau furnizor) către `map_tax`.
- `account.move`: `_l10n_ro_check_reverse_charge_331`, apelat din `_post`, blochează
  postarea unei facturi de vânzare sau a unui bon de furnizor cu taxă art. 331 către o
  parte neînregistrată.
- `res.partner`: `_l10n_ro_is_vat_registered`, sursa unică de adevăr pentru statutul de
  TVA (câmpul `l10n_ro_vat_subjected` dacă există, altfel prefixul „RO" din CUI).
- `account.chart.template`: creează pe planul de conturi RO taxele **0% R331** (rândul
  13 din D300, grup `tvati`) și **21% R331** (autolichidare 21%, `Dr 4426 = Cr 4427`,
  rândurile 12.1 și 26.1, grup `tvatip21`).

**Vizualizări**

- `view_tax_form` / `view_tax_tree` (moștenite din `account`): adaugă bifa
  `l10n_ro_reverse_charge_331` pe formularul și lista de taxe, vizibilă doar pentru
  taxe de vânzare sau de achiziție, domestice RO.
- `view_account_position_form` (moștenit din `account`): adaugă bifa
  `l10n_ro_reverse_charge_331` pe poziția fiscală și un mesaj informativ care explică
  ambele sensuri (vânzare → **0% R331**, achiziție → **21% R331**), întrucât formularul
  poziției fiscale nu mai are tab de taxe în Odoo 19.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare, creează sau adoptă taxele **0% R331** și **21% R331**
  pe companiile RO cu plan de conturi deja încărcat, copiind etichetele de raportare și
  repartiția de pe taxele native `tvati` / `tvatip21`; leagă apoi pozițiile fiscale deja
  bifate de taxele nou apărute (folosit și de migrarea la 1.1.0, pentru bazele unde
  modulul acoperea deja doar vânzarea).

#### 5. Conexiuni

- `l10n_ro`: sursa taxelor native de taxare inversă `tvati` (vânzare) și `tvatip21`
  (achiziție 21%), folosite ca referință pentru etichete, conturi și grup de taxe, și a
  poziției fiscale „Reverse Tax Regime".
- `l10n_ro_config`: sursa câmpului `l10n_ro_vat_subjected` folosit de gardianul de
  înregistrare TVA, dacă e instalat (OCA, `auto_install`).
- `l10n_ro_anaf_partner`: alternativă pentru `l10n_ro_vat_subjected`, sincronizat din
  registrul ANAF.
- `account_edi_ubl_cii`: dacă e instalat, modulul setează explicit codul UNCL5305
  `AE` pe taxa **0% R331**, pentru ca factura electronică să declare corect taxarea
  inversă în locul codului implicit `E` (scutit).
