# Impozit Micro-Întreprindere (localizat la `l10n_ro_micro_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_micro_tax`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_micro_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_micro_tax`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul calculează și înregistrează trimestrial impozitul pe veniturile micro-întreprinderilor conform Legii 227/2015 Titlul III, actualizat prin OUG 115/2023 și OUG 21/2024. Determină automat baza impozabilă din veniturile din exploatare (cu excluderi configurabile), aplică cota corectă (1% cu cel puțin un salariat, 3% fără salariat) și generează nota contabilă aferentă. Include monitorizarea plafonului de 500.000 EUR cu alerte și tranziție automată la regimul de impozit pe profit.

#### 2. Funcționalități Cheie

- Model persistent `l10n.ro.micro.tax.compute` cu mașină de stări draft → posted → cancelled.
- Calcul automat al veniturilor din `account.move.line` pentru conturile de tip income / income_other.
- Conturi excluse configurabile pe companie (dividende ct. 761, subvenții ct. 7411/7584, diferențe de curs favorabile, reluări de provizioane).
- Cotă automată: 1% cu cel puțin un salariat, 3% fără salariat; numărul de salariați preluat din modulul HR dacă este instalat sau completat manual.
- Notă contabilă Dr 698 = Cr 4418 generată la postare (ct. 698, nu 691, conform OMFP 1802/2014).
- Cron lunar de monitorizare a pragului: alertă la 80% și tranziție automată la profit la 100% din plafonul de 500.000 EUR.
- Configurare în Settings: regim fiscal, prag EUR, conturi excluse.
- 9 teste automate (TC-01 → TC-09).

#### 3. Dependențe

- `account`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.micro.tax.compute`: Calculul trimestrial al impozitului micro, cu mașina de stări și generarea notei contabile.
- `res.config.settings` (extins): Configurarea regimului fiscal, a pragului și a conturilor excluse.

**Vizualizări / Date**

- `views/l10n_ro_micro_tax_views.xml`: Interfața de creare și postare a calculelor de impozit micro.
- `views/res_config_settings_views.xml`: Opțiunile de configurare a regimului micro.
- `data/ir_cron.xml`: Cron-ul lunar de monitorizare a plafonului.

**Acțiuni Automate / Acțiuni Server**

- Cron lunar de monitorizare prag: emite alertă la 80% și declanșează tranziția la regimul de profit la 100% din plafon.

#### 5. Conexiuni

- `[[l10n_ro_profit_tax]]`
