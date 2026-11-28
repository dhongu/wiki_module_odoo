# Moldova - Accounting (localizat la `l10n_md/index.md`)

- **Nume Tehnic:** `l10n_md`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-moldova/tree/20.0/l10n_md
- **Cale Locală:** `odoo-addons/l10n-moldova/l10n_md`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modul de localizare contabilă pentru Republica Moldova. Instalează planul de conturi (conturi de gradul I) din Planul general de conturi contabile, aprobat prin Ordinul Ministerului Finanțelor nr. 119 din 06.08.2013, împreună cu cotele de taxe conform Codului Fiscal al Republicii Moldova. Modulul nu are încă fișă de consultant; aceasta va fi adăugată la finalizarea planului de conturi.

#### 2. Funcționalități Cheie

- Șablon de plan de conturi `md` („Moldova”), încărcat prin mecanismul standard de chart template, cu conturi cu 3 cifre.
- Cote de TVA pentru vânzări și achiziții: 20%, 8% și 0%; sunt definite și impozitul pe profit 12%, asigurările sociale 24% și asigurarea medicală 9%, conform Codului Fiscal.
- Jurnale, grupuri de taxe, poziții fiscale și condiții de plată predefinite pentru Moldova.
- Setări implicite la crearea companiei: conturi de creanțe, datorii, venituri, cheltuieli, diferențe de curs, prefixe pentru bancă, numerar și transferuri, țara fiscală Moldova și taxele implicite (TVA 20%).
- Pe formularul companiei apar câmpurile **IDNO (Moldova)** și **IBAN**.
- Date demo: o companie demonstrativă pentru Moldova.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): șablonul `md` și valorile implicite ale companiei (`models/template_md.py`); datele sunt în `data/template/*.csv`.
- `res.company` (extins): câmpurile `idno` (IDNO) și `iban`.

**Vizualizări**

- `view_company_form_md`: adaugă IDNO și IBAN după câmpul de cod fiscal pe formularul companiei.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_md_zip](../l10n_md_zip/index.md): localități moldovenești cu cod poștal și raion, completate din codul poștal; se folosește alături de acest modul în Republica Moldova.
