# Impozit pe Profit (D100/D101) (localizat la `l10n_ro_profit_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_profit_tax`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_profit_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_profit_tax`
- **Ultima Ingestie:** 2026-06-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează automat impozitul pe profit conform Legii 227/2015 Titlul II, cu sprijin pentru D100 trimestrial (cumulat YTD) și D101 anual. Pornind de la profitul contabil (venituri 7xx − cheltuieli 6xx, cumulat de la 1 ianuarie), aplică ajustări fiscale configurabile per cont, gestionează pierderea fiscală reportată (carry-forward 7 ani, deducere FIFO, limita 70%) și creditul fiscal pentru sponsorizări, generând nota contabilă Dr 691 = Cr 441 la postare. Modulul include și un Registru de evidență fiscală (OMFP 870/2005) care listează ajustările pe rânduri, cu temei legal, și se reconciliază cu calculul anual. Se adresează companiilor plătitoare de impozit pe profit la cota de 16%.

#### 2. Funcționalități Cheie

- Calcul profit contabil YTD din `account.move.line` (venituri 7xx − cheltuieli 6xx), cumulat de la 1 ianuarie.
- Ajustări fiscale configurabile per cont contabil: cheltuieli nedeductibile (amenzi, protocol 50%), venituri neimpozabile (dividende subsidiare), deduceri suplimentare (C-D).
- Pierdere fiscală reportată (art. 31 CF): carry-forward 7 ani, deducere FIFO, limita 70% din profitul impozabil, cu tracking complet al utilizărilor per calcul.
- Credit fiscal sponsorizări (art. 25¹ CF) calculat pe contul 6582: `min(0,75% CA, 20% impozit calculat, cheltuieli efective)`.
- Model persistent cu mașină de stări `draft → posted → cancelled`; anularea eliberează automat utilizările de pierdere.
- Notă contabilă automată Dr 691 = Cr 441 la postare, cu verificări (conturi existente, impozit > 0, limita 70% respectată).
- Registru de evidență fiscală (OMFP 870/2005): generare din calculul anual, reconciliere automată, închidere imutabilă pe an.
- Periodicitate YTD: D100 T1–T3 cumulativ de la 1 ianuarie (art. 41 CF) și D101 anual independent.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute`: Calculul trimestrial/anual cu mașina de stări `draft → posted → cancelled` și generarea notei contabile Dr 691 = Cr 441.
- `l10n.ro.tax.adjustment`: Ajustări fiscale per cont contabil (tip nedeductibil / neimpozabil / deducere și procent).
- `l10n.ro.tax.loss`: Registrul pierderilor fiscale reportate, cu deducere FIFO și expirare la 7 ani.
- `l10n.ro.tax.loss.usage`: Utilizările de pierdere per calcul (tracking al sumei deduse).
- `l10n.ro.tax.register`: Registrul de evidență fiscală (OMFP 870/2005), reconciliat cu calculul anual.
- `l10n.ro.tax.register.line`: Rândurile registrului fiscal (ajustare + temei legal).
- `res.config.settings` (extins): Configurarea conturilor și a parametrilor de calcul.

**Vizualizări**

- `views/l10n_ro_profit_tax_views.xml`: Interfața de calcul, ajustări fiscale și pierderi reportate.
- `views/l10n_ro_tax_register_views.xml`: Interfața registrului de evidență fiscală.
- `views/res_config_settings_views.xml`: Opțiunile de configurare.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; calculul, postarea, sugerarea deducerii pierderii și generarea registrului se declanșează manual.*

#### 5. Conexiuni

- [l10n_ro_micro_tax](../l10n_ro_micro_tax/index.md): regimul alternativ de impozitare (micro) pentru companiile sub pragul de impozit pe profit.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): închiderea de cont de profit și pierdere, sursă a rezultatului contabil.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declararea impozitului trimestrial (D100).
- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md): declararea anuală a impozitului pe profit.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): raportarea creditului fiscal pentru sponsorizări.
- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md): corelarea rezultatului fiscal cu cel contabil.
