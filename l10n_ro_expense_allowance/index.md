# Romania - Diurne și Deplasări (Limită Fiscală 2,5×) (localizat la `l10n_ro_expense_allowance/index.md`)

- **Nume Tehnic:** `l10n_ro_expense_allowance`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_expense_allowance
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_expense_allowance`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Extinde modulul `deltatech_expenses` (Decont Cheltuieli) cu verificarea automată a limitei fiscale de deductibilitate a diurnei, conform Codului Fiscal art. 76 alin. (2) lit. k. Diurna deductibilă este calculată ca dublul-jumătate (2,5×) al cuantumului legal stabilit prin HG 714/2018 (deplasări interne) și HG 518/1995 (deplasări externe), iar suma peste limită este evidențiată ca venit salarial impozabil.

## 2. Funcționalități Cheie

- **Tabel cuantumuri legale** (`l10n.ro.allowance.rate`) cu date preconfigurate HG 714/2018 și HG 518/1995 (DE, FR, IT, HU, GB, US).
- **Calcul automat** al limitei totale, diurnei deductibile și surplusului impozabil.
- **Banner de avertizare** pe formularul de decont când diurna depășește limita fiscală.
- **Preluare automată a cuantumului** în funcție de tipul deplasării (intern/extern) și țara destinație.
- **Multiplier configurabil** (implicit 2,5 — Cod Fiscal art. 76).

## 3. Dependențe

- `deltatech_expenses`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `l10n.ro.allowance.rate`: tabelul cuantumurilor legale ale diurnei per țară și tip de deplasare.
- Modelul de decont (`deltatech_expenses`) extins cu calculul limitei deductibile, al diurnei deductibile și al surplusului impozabil.

### Vizualizări / Date

- `views/l10n_ro_expense_allowance_view.xml`: tabelul de cuantumuri și bannerul de avertizare pe decont.
- `data/l10n_ro_allowance_rate_data.xml`: cuantumurile legale preconfigurate.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate acțiuni automate; calculul se face la completarea decontului.*

## 5. Conexiuni

- `[[l10n_ro_expense_currency]]`
