# Romania - Impozit pe profit (D100/D101) (localizat la `l10n_ro_profit_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_profit_tax`
- **Versiune:** `20.0.1.2.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_profit_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_profit_tax`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul calculează automat impozitul pe profit conform Legii 227/2015 Titlul II, cu sprijin pentru D100 trimestrial (cumulat de la 1 ianuarie) și D101 anual. Pornind de la profitul contabil (venituri 7xx − cheltuieli 6xx), aplică ajustări fiscale configurabile per cont, gestionează pierderea fiscală reportată și creditul fiscal pentru sponsorizări și generează nota contabilă Dr 691 = Cr 441 la postare. Include și un Registru de evidență fiscală (OMFP 870/2005), reconciliat cu calculul anual. Se adresează companiilor plătitoare de impozit pe profit la cota de 16%.

#### 2. Funcționalități Cheie

- Calcul profit contabil YTD din rulaje (venituri 7xx − cheltuieli 6xx), cumulat de la 1 ianuarie, fără notele de închidere pe 121; partea financiară e separată pe prefixe de cont.
- Rânduri calculate din conturi: impozitul pe profit (691, 692, 694, 697), protocolul peste limita de 2% (6231) și amortizarea contabilă (6811), cu amortizarea fiscală editabilă.
- Ajustări fiscale configurabile per cont (meniul Contabilitate → Configurare → Impozit Profit → Ajustări fiscale): cheltuieli nedeductibile, venituri neimpozabile (dividende de la persoane juridice române), deduceri suplimentare (C-D), cu procent per regulă.
- Pierdere fiscală reportată (art. 31 CF): 5 ani (7 ani pentru pierderile de până în 2023), deducere FIFO, limita 70% din profitul impozabil, cu tracking al utilizărilor per calcul și buton „Sugerează deducere pierdere".
- Credit fiscal sponsorizări (art. 25 alin. (4) lit. i) CF): min(0,75% din cifra de afaceri netă, 20% din impozitul calculat, cheltuieli efective); cheltuiala 6584 se adaugă automat la baza impozabilă.
- Model persistent cu stări `draft → posted → cancelled`; anularea eliberează utilizările de pierdere. Cota de impozit se poate modifica pe calcul (ex. cotă redusă prin tratat).
- Notă contabilă automată Dr 691 = Cr 441 la postare (meniul Contabilitate → Contabilitate → Impozit pe Profit), cu verificări: conturi existente, impozit de plată pozitiv, limita de 70% respectată.
- Periodicitate YTD: T1–T3 cumulativ de la 1 ianuarie (D100, art. 41 CF) și calcul anual independent pentru D101.
- Registru de evidență fiscală (OMFP 870/2005): generare din calculul anual, reconciliere automată, închidere imutabilă pe an. Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute`: Calculul trimestrial/anual cu mașina de stări `draft → posted → cancelled` și generarea notei contabile Dr 691 = Cr 441.
- `l10n.ro.tax.adjustment`: Ajustări fiscale per cont contabil (tip nedeductibil / neimpozabil / deducere și procent).
- `l10n.ro.tax.loss`: Registrul pierderilor fiscale reportate, cu deducere FIFO și expirare.
- `l10n.ro.tax.loss.usage`: Utilizările de pierdere per calcul.
- `l10n.ro.tax.register`: Registrul de evidență fiscală (OMFP 870/2005), reconciliat cu calculul anual.
- `l10n.ro.tax.register.line`: Rândurile registrului fiscal (ajustare + temei legal).
- `res.company` / `res.config.settings` (extinse): Conturile și parametrii de calcul.

**Vizualizări**

- `views/l10n_ro_profit_tax_views.xml`: Interfața de calcul, ajustări fiscale și pierderi reportate.
- `views/l10n_ro_tax_register_views.xml`: Interfața registrului de evidență fiscală.
- `views/res_config_settings_views.xml`: Opțiunile de configurare.
- `report/report_tax_register.xml`: Raportul PDF al registrului de evidență fiscală.

**Acțiuni Automate / Acțiuni Server**

*Nu există acțiuni automate; calculul, postarea, sugerarea deducerii pierderii și generarea registrului se declanșează manual. Modulul definește doar o secvență (`data/ir_sequence.xml`).*

#### 5. Conexiuni

- [l10n_ro_micro_tax](../l10n_ro_micro_tax/index.md): regimul alternativ de impozitare (micro) pentru companiile sub pragul de impozit pe profit.
- [l10n_ro_account_return_pl_closing](../l10n_ro_account_return_pl_closing/index.md): închiderea de cont de profit și pierdere, sursă a rezultatului contabil.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declararea impozitului trimestrial (D100).
- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md): declararea anuală a impozitului pe profit.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): raportarea creditului fiscal pentru sponsorizări.
- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md): corelarea rezultatului fiscal cu cel contabil.
