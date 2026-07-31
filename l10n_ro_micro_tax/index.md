# Impozit Micro-Întreprindere (localizat la `l10n_ro_micro_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_micro_tax`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_micro_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_micro_tax`
- **Ultima Ingestie:** 2026-06-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează și înregistrează trimestrial impozitul pe veniturile micro-întreprinderilor conform Legii 227/2015 Titlul III, actualizat prin OUG 115/2023 și OUG 21/2024. Se adresează companiilor cu cifra de afaceri sub 500.000 EUR/an care aplică cota de 1% (cu cel puțin un salariat) sau 3% (fără salariat). Determină automat baza impozabilă din veniturile din exploatare (cu excluderi configurabile), aplică cota corectă în funcție de numărul de salariați și generează automat nota contabilă aferentă. Include monitorizarea plafonului de 500.000 EUR cu alerte și tranziție automată la regimul de impozit pe profit la depășire.

#### 2. Funcționalități Cheie

- Model persistent `l10n.ro.micro.tax.compute` cu mașină de stări `draft → posted → cancelled`.
- Calcul automat al veniturilor impozabile din `account.move.line` pentru conturile de tip `income` / `income_other`, filtrând înregistrările postate în trimestrul selectat.
- Conturi excluse din baza de calcul, configurabile pe companie (dividende 761, subvenții 7411/7584 etc.).
- Număr de salariați preluat automat din modulul HR dacă este instalat sau completat manual.
- Cotă automată: 1% (cel puțin un salariat) sau 3% (zero salariați), conform legii.
- Generare automată a notei contabile **Dr 698 = Cr 4418** la postare.
- Cron lunar de monitorizare a plafonului: alertă la 80% și tranziție automată la impozit pe profit la depășirea pragului de 500.000 EUR.
- Configurare în Setări Contabilitate — regim fiscal, prag EUR, conturi excluse.
- 9 teste automate (TC-01 → TC-09).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.micro.tax.compute`: Calculul trimestrial al impozitului micro (1%/3% din venituri), cu mașina de stări și generarea notei contabile Dr 698 = Cr 4418.
- `res.config.settings` (extins): Configurarea regimului fiscal, a pragului EUR și a conturilor excluse din baza de calcul.

**Vizualizări / Date**

- `views/l10n_ro_micro_tax_views.xml`: Interfața de listă și formular pentru crearea, calculul și postarea calculelor de impozit micro.
- `views/res_config_settings_views.xml`: Opțiunile de configurare a regimului micro în Setări Contabilitate.
- `data/ir_cron.xml`: Cron-ul lunar de monitorizare a plafonului.

**Acțiuni Automate / Acțiuni Server**

- Cron lunar „RO: Verificare prag micro-întreprindere": emite alertă pe fișa companiei la 80% din plafon și declanșează tranziția automată la regimul de impozit pe profit la depășirea celor 500.000 EUR.

#### 5. Conexiuni

- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): regimul în care tranzitează compania la depășirea plafonului micro de 500.000 EUR.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declararea obligației de impozit micro calculate.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): scăzăminte din sponsorizări, acolo unde este cazul.
- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): checklist fiscal trimestrial.
