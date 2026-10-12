# Romania - Declarație privind cifra de afaceri (D094)

- **Nume Tehnic:** `l10n_ro_anaf_d094`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d094
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d094`
- **Ultima Ingestie:** `2026-10-12`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Declarația 094 raportează cifra de afaceri a persoanelor impozabile care au perioada fiscală trimestrul calendaristic și nu au făcut achiziții intracomunitare de bunuri în anul precedent. Se depune anual, până la 25 ianuarie, pentru anul precedent. Modulul calculează cifra de afaceri direct din deconturile de TVA (D300) ale anului, verifică condițiile de depunere, generează fișierul XML pentru ANAF și tipărește declarația în PDF pentru arhivă.

#### 2. Funcționalități Cheie

- Calcul al cifrei de afaceri din deconturile D300 ale anului, conform pct. 103 alin. (2) din Normele metodologice: livrări taxabile, scutite cu drept de deducere și cu locul în străinătate care dau drept de deducere, plus regularizările lor; livrările scutite fără drept de deducere nu intră.
- Verificarea condițiilor: plafon de 100.000 EUR la cursul BNR de la 31 decembrie și lipsa achizițiilor intracomunitare de bunuri (rd. 5 și 6 din D300), inclusiv a celor stornate ulterior. Dacă nu sunt îndeplinite, formularul afișează motivul, iar exportul e blocat (bifa „Declarație datorată”).
- Pentru firmele înregistrate în scopuri de TVA în cursul anului, cifra de afaceri se anualizează (pe un an calendaristic întreg) înainte de comparația cu plafonul (art. 322 alin. (5)), pe baza datei înregistrării în scopuri de TVA.
- Flux pe stări Ciornă / Confirmată: butoanele **Calculează din contabilitate**, **Confirmă**, **Exportă XML** și **Readu la ciornă**; sumele rămân editabile (de ex. pentru operațiuni cu locul în străinătate fără drept de deducere).
- Export XML `D094_<CUI>_<an>12.xml` (luna este întotdeauna 12, CUI fără prefixul RO, cifra de afaceri în lei întregi), validat cu o schemă proprie `d094.xsd`; fișierul rămâne atașat declarației.
- Tipărire PDF a declarației (meniul Tipărire → Declarația 094).
- Semnatar și funcție preluate implicit din contactul pentru declarații ANAF al companiei; câmpuri pentru împuternicit.
- Meniu: Contabilitate → Raportare → Declarații ANAF → D094 Cifra de afaceri TVA trimestrial. Configurare: contact declarații în Setări (secțiunea Declarații ANAF România) și cursul EUR pentru 31 decembrie.
- Versiune formular acceptată: OPANAF 631/2016, PDF inteligent ANAF v1.0.0 din 06.01.2022 (soft A, fără validator DUKIntegrator).
- Limite: operațiunile de pe rd. 3 D300 fără drept de deducere se scad manual; achizițiile intracomunitare scutite/neimpozabile nu sunt detectate; se generează doar declarația inițială, nu și cea rectificativă.

Fluxul detaliat pas cu pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d094`: declarația D094 (an fiscal, cifră de afaceri, anualizată, achiziții intracomunitare, curs EUR, plafon, stare, semnatar, fișier XML); folosește mixinul `l10n_ro_anaf.report.handler.mixin` și `mail.thread`.

**Vizualizări**

- `view_l10n_ro_anaf_d094_list`: lista declarațiilor (an, cifră de afaceri, datorată, stare).
- `view_l10n_ro_anaf_d094_form`: formularul declarației, cu butoanele de calcul, confirmare și export.
- `action_l10n_ro_anaf_d094` și `menu_l10n_ro_anaf_d094`: acțiunea și meniul din Declarații ANAF.
- `action_report_l10n_ro_anaf_d094`: raportul PDF „Declarația 094”.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): legătură funcțională, nu dependență; D094 citește aceleași rânduri de decont (etichete fiscale ale raportului D300) din liniile contabile, nu modelul declarației D300.
