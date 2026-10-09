# Moldova - Accounting (localizare contabilă Republica Moldova)

- **Nume Tehnic:** `l10n_md`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-moldova/tree/19.0/l10n_md
- **Cale Locală:** `odoo-addons/l10n-moldova/l10n_md`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă localizarea contabilă de bază pentru firmele din Republica Moldova: planul de conturi, cotele de TVA, jurnalele și pozițiile fiscale, încărcate automat la crearea contabilității unei companii. Planul de conturi urmează Planul general de conturi contabile (Ordinul Ministerului Finanțelor nr. 119 din 06.08.2013), iar cotele de taxe respectă Codul Fiscal al Republicii Moldova. Modulul adaugă pe companie datele de identificare locale (IDNO și IBAN) și o listă de bănci moldovenești.

#### 2. Funcționalități Cheie

(Modulul nu are `readme/DESCRIPTION.md`; informațiile provin din descrierea din `__manifest__.py` și din fișierele de date.)

- Plan de conturi „Moldova” (cod șablon `md`), cu conturi pe 3 cifre (aprox. 156 de conturi, grupate pe clase), conform Ordinului MF nr. 119/2013. Conturile de client și furnizor implicite sunt 221, respectiv 521.
- Prefixe implicite pentru conturile de lichidități: bancă 242, casă 241, transferuri de lichidități 245. Conturi implicite de venituri (611) și cheltuieli (711), plus conturi de diferențe de curs valutar (622 / 722).
- Taxe preconfigurate: TVA 20% (cota standard), TVA 8% (cota redusă) și TVA 0% (export), atât la vânzări, cât și la achiziții. TVA 20% este setat implicit pe vânzări și achiziții. Taxa colectată se postează pe contul 534, cu excepția cotei de 0%.
- Jurnale implicite: Casa, Bancă, Vânzări, Achiziții.
- Poziții fiscale: Export și Piața internă (aplicate automat), plus Fără TVA, Nerezidenți și Regim preferențial (aplicabile manual).
- Termene de plată și grupuri de taxe predefinite pentru localizare.
- Câmpuri noi pe formularul companiei, lângă codul fiscal: `IDNO (Moldova)` și `IBAN`.
- Listă de bănci din Moldova (11 înregistrări, cu cod BIC, ex. Moldova Agroindbank, Victoriabank, Moldindconbank, Mobiasbanca).
- Companie demo „Demo Moldova SRL” pentru teste.
- Descrierea din manifest menționează și cotele de impozit pe profit (12%), asigurări sociale (24%) și asigurare medicală (9%), dar în fișierul de taxe (`account.tax-md.csv`) sunt definite doar cele șase taxe de TVA.

#### 3. Dependențe

- `account`
- `base_vat`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): declară șablonul `md` prin `@template('md')` în `models/template_md.py` (nume, număr de cifre, conturi implicite de client/furnizor) și datele companiei (țara fiscală `base.md`, prefixe lichidități, conturi de curs valutar, taxe și conturi implicite de venit/cheltuială). CSV-urile din `data/template/` (conturi, grupuri de conturi, taxe, grupuri de taxe, jurnale, poziții fiscale, termene de plată) sunt încărcate de mecanismul de chart template, nu din manifest.
- `res.company` (extins): adaugă câmpurile `idno` și `iban`.

**Vizualizări**

- `view_company_form_md`: moștenește `base.view_company_form` și afișează `idno` și `iban` după câmpul `vat`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

Nu există conexiuni funcționale verificate cu alte module cu pagină wiki (în afara dependențelor din secțiunea 3).
