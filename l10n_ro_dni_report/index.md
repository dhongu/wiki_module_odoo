# Romania - Raport livrări nefacturate (418)

- **Nume Tehnic:** `l10n_ro_dni_report`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_dni_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_dni_report`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Raportul din spatele soldului contului 418 („Clienți — facturi de întocmit”): arată pentru ce avize de livrare marfa nu a fost încă facturată, către ce client și de cât timp. Soldul contului spune doar cât mai e de facturat; raportul explică și pentru ce, ceea ce se cere la închiderea lunii. Este perechea raportului de recepții nefacturate (408).

#### 2. Funcționalități Cheie

- Înregistrările de pe conturile 418 sunt grupate pe client, cu drill-down până la documentul individual.
- Coloane: valoarea livrată, cât s-a facturat, cât a rămas de facturat și vechimea (în zile) a celei mai vechi înregistrări nefacturate.
- Sold cumulat la data de sfârșit a perioadei: un aviz de acum trei luni, încă nefacturat, apare în raportul lunii curente.
- Clienții fără sold nu apar.
- La livrările pe aviz din `l10n_ro_stock_account`, coloana *Document* arată avizul (transferul), nu nota contabilă; pentru note manuale rămâne documentul contabil.
- Contul 418 se ia din configurarea companiei (contul folosit la avizul de livrare); fără ea, se folosesc conturile care încep cu 418.
- Filtre de perioadă (implicit luna curentă), client și companie; export PDF / XLSX din framework-ul de rapoarte.
- Meniu: **Contabilitate → Raportare → Livrări nefacturate (418)**.
- Control: totalul coloanei *Rămas* trebuie să fie egal cu soldul debitor al conturilor 418 din balanță la aceeași dată. Fluxul detaliat și scenariile de test sunt în fișa consultant.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.dni.report.handler`: handler personalizat de raport (`account.report.custom.handler`), cu motorul `_report_custom_engine_dni` care calculează pe baza liniilor contabile postate de pe 418 valorile livrat / facturat / rămas / vechime / document.

**Vizualizări**

- `dni_report` (`account.report`): definiția raportului, cu coloanele Document, Delivered, Invoiced, Remaining, Age (days), grupare pe partener și apoi pe linie.
- `action_dni_report` și `menu_dni_report`: acțiune client și meniu sub rapoartele legale din Contabilitate.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- `l10n_ro_stock_account`: avizul de livrare (418 = 707) și legătura notei contabile cu transferul; folosit opțional, dacă este instalat.
- [l10n_ro_rni_report](../l10n_ro_rni_report/index.md): perechea pentru recepții nefacturate (408).
- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): tipărirea avizului de însoțire a mărfii.
