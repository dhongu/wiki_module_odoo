# Romania - Contabilizare salarii, conturi implicite pe reguli (localizat la `l10n_ro_hr_payroll_account_enhancement/index.md`)

- **Nume Tehnic:** `l10n_ro_hr_payroll_account_enhancement`
- **Versiune:** `19.0.1.9.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_hr_payroll_account_enhancement
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_hr_payroll_account_enhancement`
- **Ultima Ingestie:** `2026-10-22`

> **Origine:** partea contabilă a fostului `l10n_ro_payroll_ro`, separată în 19.0.2.0.0 al modulului [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md), în linie cu perechea standard `l10n_ro_hr_payroll` / `l10n_ro_hr_payroll_account`.

#### 1. Sumar

Modulul completează salarizarea românească (`l10n_ro_hr_payroll_enhancement`) cu nota contabilă a statului de plată: pune conturile implicite pe regulile salariale, ca la validarea fluturașului să se genereze automat înregistrarea, fără configurare de mână. Se instalează automat când sunt prezente ambele module dependente.

#### 2. Funcționalități Cheie

- **Conturi implicite pe reguli** (Debit = Credit): `GROSS` 641 = 421; `CAS` 421 = 43151; `CASS` 421 = 43161; `INCOMETAX` 421 = 4441; `CAM` 6461 = 4361 (646 dacă planul nu are 6461); `TICHETE` 6422 = 5328; popriri, cesiuni, pensie alimentară, `DEDUCTION` și `RETINERI` (sindicat, pensie facultativă reținută) 421 = 4271.
- **Completează doar golurile:** regulile care au deja conturi pe companie nu se suprascriu; se aplică la instalare, la actualizare (inclusiv companiile existente) și la încărcarea planului RO. Conturile lipsă din plan sunt sărite, cu avertisment în jurnal. Contul se caută întâi după cod exact, apoi după prefix (planul RO folosește analitice: 43151, 43161, 4441, 4361, 43111).
- **CAS angajator pentru condiții deosebite / speciale** (`PENSION`, 4% / 8%, art. 138 lit. b și c Cod fiscal): 6451 = 4311 (43111 în planul RO).
- **Diferența de CAS / CASS până la baza minimă, suportată de angajator** (19.0.1.9.0): `CAS_DIFMIN` 6451 = 4315 și `CASS_DIFMIN` 6453 = 4316 (43151 / 43161 în planul RO); nu trec prin 421, pentru că nu se rețin din salariu.
- **Beneficii suportate de angajator:** pensia facultativă 6456 = 4381, pensia ocupațională 6458 = 4381, primele de asigurare voluntară de sănătate (`SAN_ANG`) 6457 = 4381, pe toată suma; factura fondului / asigurătorului se închide apoi pe 4381 = 401, nu din nou pe cheltuială. Abonamentele medicale de la o clinică nu sunt prime de asigurare: contul potrivit este 6458, de schimbat pe regulă.
- **Tichete și ajutoare:** tichete de masă, de vacanță, cadou, de creșă și culturale 6422 = 5328; ajutoare 6458 = 423 (plătite separat, 423 = 5121). Partea neimpozabilă plătită în bani (`BEN_NUMERAR`: clauza de mobilitate, educația timpurie decontată) 641 = 421.
- **Excedentul în natură fără oglindă pe 641** (19.0.1.7.0): avantajele neplătite în bani (pensii și asigurări peste plafon, tichete cadou peste plafon, hrană, cazare, servicii turistice, abonament sport, educație plătită unității) sunt în brut doar ca bază pentru contribuții și impozit. La generarea notei, suma regulilor `AVANTAJ_ANG_DED` / `CADOU_IMP_DED` se scade din liniile brutului (Dr 641 = brut − excedentul în natură), fără linii negative; rulajele 641 rămân corecte pentru balanță. Rulajul debitor al lui 641 este deci brutul din stat minus aceste linii (de ținut cont la reconcilierea cu D112). Beneficiile în natură nu au cont în fluturaș: cheltuiala e pe factura furnizorului.
- **Concedii medicale:** `CM_FNUASS` Dr 4382 = Cr 423; `CAS_CM` / `CASS_CM` / `TAX_CM` Dr 423 = Cr 4315 / 4316 / 444; indemnizația angajatorului (`CM_FS`) rămâne în brut, 641 = 421. Planul RO are analitice pe 423 (4231), deci contul se caută pe familie.
- **Impozit redirecționat** (3,5%, cu [l10n_ro_payroll_tax_redirect](../l10n_ro_payroll_tax_redirect/index.md)): Dr 4441 = Cr 462.
- **Linii cu partener:** liniile contului 421 (și 423 pentru ajutoare și concedii medicale) au ca partener angajatul (`employee_move_line`), ca plata salariilor să se poată reconcilia pe angajat; soldul 421 pe salariat este netul de plată.
- **Grupare opțională:** cu opțiunea `batch_payroll_move_lines` (pe companie) se generează o singură notă pe stat, datată în ultima zi a lunii; liniile nu mai au partener.
- **Unde se verifică:** maparea în Stat de plată → Configurare → Salariu → Reguli → fila Contabilitate; nota generată la **Validează** fluturașul, în jurnalul Salarii (Contabilitate → Note contabile).

> **Limite cunoscute:** plata netului, avansul chenzinal, plata obligațiilor către buget, achiziția tichetelor (Dr 5328 = Cr 401) și `UNEMPDISABLED` (vărsământul L448/2006, dezactivat pe fluturaș) nu sunt mapate contabil; impozitul scutit (art. 60), suma neimpozabilă, deducerile și `COSTANG` nu se înregistrează.

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)
- `l10n_ro_hr_payroll_account`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): `_configure_payroll_account_ro` completează conturile pe reguli (`PAYROLL_RULES`, `PAYROLL_ACCOUNTS` în `models/account_chart_template.py`); `_l10n_ro_payroll_account` caută contul.
- `hr.payslip` (extins): `_prepare_slip_lines` scade din liniile brutului excedentul în natură (`BASE_ONLY_RULE_CODES`), ca 641 să nu apară pe ambele laturi.

**Reguli salariale**

`data/hr_salary_rule_data.xml` setează `employee_move_line` pe `GROSS`, `CAS`, `CASS`, `INCOMETAX`, `RETINERI`, popriri, cesiuni, pensie alimentară, `DEDUCTION`, regulile de stornare a excedentelor, beneficiile în numerar, ajutoarele și regulile de concediu medical, și apelează `_load_payroll_accounts` pentru companiile RO existente.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): regulile salariale și parametrii pe care le mapează.
- [l10n_ro_payroll_tax_redirect](../l10n_ro_payroll_tax_redirect/index.md): regula de impozit redirecționat (3,5%), mapată Dr 4441 = Cr 462.
- `l10n_ro_hr_payroll_account`: integrarea contabilă standard (jurnal, notă contabilă la validare).
