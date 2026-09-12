# Romania - Taxare inversă art. 331 (localizat la `l10n_ro_reverse_charge_331/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reverse_charge_331
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331`
- **Ultima Ingestie:** `2026-09-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aplică automat taxarea inversă pe plan intern prevăzută de **articolul 331 din
Codul fiscal** (Legea 227/2015), și numai atunci când legea o permite. Articolul 331
listează livrările pentru care TVA-ul este datorat de cumpărător, nu de furnizor:
cherestea și materiale lemnoase, deșeuri feroase și neferoase, cereale și plante
tehnice, certificate de emisii de gaze cu efect de seră, energie electrică către un
comerciant, aur de investiții, telefoane mobile, dispozitive cu circuite integrate,
console de jocuri, tablete și laptopuri — dar doar dacă **atât furnizorul, cât și
cumpărătorul** sunt înregistrați în scopuri de TVA conform art. 316. Pentru un
cumpărător neînregistrat, livrarea rămâne taxabilă la cota standard. Odoo nu poate
exprima singur această condiție — poziția fiscală a regimului național din planul de
conturi RO se aplică automat oricărui partener, plătitor sau nu — așa că modulul
adaugă o taxă dedicată, un gardian pe statutul de TVA al cumpărătorului și un blocaj
la postarea facturilor greșit configurate.

#### 2. Funcționalități Cheie

- Adaugă o taxă de vânzare dedicată, **0% R331**, raportată pe rândul 13 din decontul
  D300 („livrări supuse măsurilor de simplificare") și purtând mențiunea legală impusă
  de art. 331 alin. (3) pe o factură fără TVA colectată.
- Adaugă o bifă **Reverse Charge Art. 331** pe fiecare taxă de vânzare domestică —
  bifarea ei pe taxa folosită pentru cherestea, deșeuri sau cereale este întreaga
  configurare; modulul scrie singur maparea inversă din Odoo 19 (`original_tax_ids` și
  `fiscal_position_ids`).
- Adaugă o bifă **Reverse Charge Art. 331** pe poziția fiscală a plătitorilor de TVA
  (consultantul o declară — poziția domestică a companiei nu poate fi dedusă automat,
  fiindcă pe o bază cu poziții separate pentru plătitori și neplătitori, la aceeași
  secvență, câștigă id-ul mai mic, care poate fi tocmai cea a neplătitorilor).
- Gardian pe înregistrarea în scopuri de TVA a cumpărătorului (câmpul RO „Plătitor de
  TVA — scpTVA" dacă e disponibil, altfel prefixul „RO" din CUI): înlocuirea de taxă se
  omite atât pe ofertă, cât și pe factură, pentru un cumpărător neînregistrat.
- Blocaj la postare pentru orice factură de vânzare care încă poartă taxa art. 331
  către un cumpărător neînregistrat — acoperă poziții fiscale atribuite manual pe
  partener, taxe alese direct pe linie și documente importate.
- Documentele deja existente nu sunt rescrise: taxele de pe oferte confirmate și
  facturi postate sunt stocate, nu recalculate; recalculul se declanșează schimbând
  clientul sau poziția fiscală pe document.
- Acoperă doar partea de vânzare; pe achiziții, taxarea inversă rămâne pe fluxul
  standard `l10n_ro` (poziția fiscală „Reverse Tax Regime" pe furnizor).
- Materialele lemnoase derivate (PAL, OSB, placaj) nu intră sub incidența art. 331
  lit. b) și rămân pe taxa standard, separate de cheresteaua propriu-zisă.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.tax`: câmpurile `l10n_ro_reverse_charge_331` (bifă pe taxa domestică sursă)
  și `l10n_ro_is_reverse_charge_331` (marcaj tehnic pe taxa de destinație 0% R331);
  ține maparea `original_tax_ids`/`fiscal_position_ids` sincronizată cu bifele și
  refuză o dublă înlocuire a aceleiași surse pe aceeași poziție fiscală.
- `account.fiscal.position`: câmpul `l10n_ro_reverse_charge_331`; suprascrie `map_tax`
  pentru a anula înlocuirea art. 331 când cumpărătorul nu e înregistrat în scopuri de
  TVA (citit din context, nu din partener, fiindcă `map_tax` nu primește partenerul).
- `account.move.line`: suprascrie `_get_computed_taxes` pentru a propaga în context
  statutul de TVA al cumpărătorului către `map_tax`.
- `account.move`: `_l10n_ro_check_reverse_charge_331`, apelat din `_post`, blochează
  postarea unei facturi de vânzare cu taxa art. 331 către un cumpărător neînregistrat.
- `res.partner`: `_l10n_ro_is_vat_registered`, sursa unică de adevăr pentru statutul de
  TVA (câmpul `l10n_ro_vat_subjected` dacă există, altfel prefixul „RO" din CUI).
- `account.chart.template`: template-ul care creează taxa **0% R331** pe planul de
  conturi RO, cu eticheta de raportare rândul 13 și grupul de taxe preluate de la
  `tvati` (taxa de taxare inversă livrată de `l10n_ro`).

**Vizualizări**

- `view_tax_form` / `view_tax_tree` (moștenite din `account`): adaugă bifa
  `l10n_ro_reverse_charge_331` pe formularul și lista de taxe, vizibilă doar pentru
  taxe de vânzare, domestice RO.
- `view_account_position_form` (moștenit din `account`): adaugă bifa
  `l10n_ro_reverse_charge_331` pe poziția fiscală și un mesaj informativ care explică
  unde se face maparea, întrucât formularul poziției fiscale nu mai are tab de taxe
  în Odoo 19.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare, copiază etichetele de raportare de pe taxa `tvati` a
  companiei pe taxa nou-creată **0% R331**, astfel încât ambele să raporteze pe același
  rând din D300.

#### 5. Conexiuni

- `l10n_ro`: sursa taxei native de taxare inversă `tvati` (folosită ca referință pentru
  etichete și grup de taxe) și a poziției fiscale „Reverse Tax Regime" pentru achiziții.
- `l10n_ro_config`: sursa câmpului `l10n_ro_vat_subjected` folosit de gardianul de
  înregistrare TVA, dacă e instalat (OCA, `auto_install`).
- `l10n_ro_anaf_partner`: alternativă pentru `l10n_ro_vat_subjected`, sincronizat din
  registrul ANAF.
- `account_edi_ubl_cii`: dacă e instalat, modulul setează explicit codul UNCL5305
  `AE` pe taxa 0% R331, pentru ca factura electronică să declare corect taxarea
  inversă în locul codului implicit `E` (scutit).
