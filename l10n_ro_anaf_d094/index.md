# Romania - Declarație privind cifra de afaceri (D094) (localizat la `l10n_ro_anaf_d094/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d094`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d094
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d094`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Declarația 094 este cifra de afaceri a plătitorilor de TVA cu perioada fiscală trimestrul, care nu au efectuat achiziții intracomunitare de bunuri în anul precedent. Se depune anual, până la 25 ianuarie, iar modulul calculează cifra de afaceri din deconturile de TVA, verifică condițiile, exportă XML-ul și tipărește declarația în PDF.

#### 2. Funcționalități Cheie

- Calculul cifrei de afaceri din deconturile D300 ale anului (pct. 103 alin. (2) din Norme): livrări taxabile, scutite cu drept de deducere și cu locul în străinătate care dau drept de deducere, plus regularizările lor.
- Verificarea condițiilor: plafonul de 100.000 EUR la cursul BNR de la 31 decembrie și lipsa achizițiilor intracomunitare de bunuri (rd. 5 și 6 din D300, inclusiv cele stornate). Dacă nu sunt îndeplinite, exportul e blocat și formularul afișează motivul.
- Pentru firmele înregistrate în scopuri de TVA în cursul anului, cifra de afaceri se anualizează înainte de comparația cu plafonul.
- Export XML `D094.xml`, validat cu o schemă proprie (`d094.xsd`, reconstituită, fiindcă ANAF publică D094 doar ca PDF inteligent); tipărire în PDF pentru arhivă.
- Meniu: *Contabilitate → Raportare → Declarații ANAF → D094 Cifra de afaceri TVA trimestrial*; stări Ciornă / Confirmată. Configurare: *Contact declarații* în setările contabilității (semnatar) și cursul EUR de la 31 decembrie.
- Limite: operațiunile cu locul în străinătate fără drept de deducere se scad manual; achizițiile intracomunitare scutite sau neimpozabile nu sunt detectate; se generează doar declarația inițială.
- Versiune formular: OPANAF 631/2016, PDF inteligent ANAF v1.0.0 din 06.01.2022.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d094`: declarația D094 (cifra de afaceri, plafon, curs EUR, semnatar), cu `mail.thread`, activități și mixinul de export `l10n_ro_anaf.report.handler.mixin`.

**Vizualizări**

- `view_l10n_ro_anaf_d094_list` și `view_l10n_ro_anaf_d094_form`: lista și formularul declarației.
- `action_l10n_ro_anaf_d094`: acțiunea de meniu.
- `action_report_l10n_ro_anaf_d094`: raportul PDF *Declarația 094*.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): cifra de afaceri se calculează din rândurile deconturilor D300.
