# Impozit pe Profit (D100/D101) (localizat la `l10n_ro_profit_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_profit_tax`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_profit_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_profit_tax`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Modulul calculează automat impozitul pe profit conform Legii 227/2015 Titlul II, cu sprijin pentru D100 trimestrial (cumulat YTD) și D101 anual. Pornind de la profitul contabil dedus din `account.move.line`, aplică ajustări fiscale configurabile per cont, gestionează pierderea fiscală reportată (carry-forward 7 ani, limita 70%) și creditul fiscal pentru sponsorizări, generând nota contabilă Dr 691 = Cr 441.

#### 2. Funcționalități Cheie

- Profit contabil calculat automat din `account.move.line` (venituri 7xx − cheltuieli 6xx), cumulat YTD.
- Ajustări fiscale configurabile per cont contabil: cheltuieli nedeductibile, venituri neimpozabile, deduceri suplimentare (C-D, investiții speciale).
- Pierdere fiscală reportată (art. 31 CF): carry-forward 7 ani, FIFO, limita 70%, cu registru de utilizări și stări (activă/epuizată/expirată).
- Credit fiscal sponsorizări (art. 25¹ CF): min(0,75% CA, 20% impozit calculat, cheltuieli efective).
- Note contabile Dr 691 = Cr 441 generate la postare.
- Periodicitate D100 T1–T3 cumulativă YTD și D101 anual.

#### 3. Dependențe

- `account`
- `[[l10n_ro]]`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute`: Calculul trimestrial/anual cu mașina de stări draft → posted → cancelled și generarea notei contabile.
- `l10n.ro.tax.adjustment`: Ajustări fiscale per cont (tip și procent).
- `l10n.ro.tax.loss`: Registrul pierderilor fiscale reportate cu tracking FIFO al utilizărilor.
- `res.config.settings` (extins): Configurarea conturilor și parametrilor.

**Vizualizări / Date**

- `views/l10n_ro_profit_tax_views.xml`: Interfața de calcul, ajustări și pierderi reportate.
- `views/res_config_settings_views.xml`: Opțiunile de configurare.
- `security/ir.model.access.csv`: Drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; calculul și postarea se declanșează manual.*

#### 5. Conexiuni

- `[[l10n_ro_micro_tax]]`
- `[[l10n_ro_account_return_pl_closing]]`
