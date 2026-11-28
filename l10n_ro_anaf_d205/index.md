# Romania - Declarația 205 ANAF (impozit reținut la sursă, beneficiari PF) (localizat la `l10n_ro_anaf_d205/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d205`
- **Versiune:** `20.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d205
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d205`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru întocmirea **Declarației 205** — declarația informativă privind impozitul reținut la sursă și câștigurile/pierderile din investiții, pe beneficiari de venit **persoane fizice** (art. 132 alin. (2) Cod fiscal). Se adresează contabililor care plătesc persoanelor fizice dividende, dobânzi, premii, chirii sau alte venituri cu impozit reținut la sursă, cel mai des dividende către asociați. Declarația se depune până în ultima zi a lunii februarie a anului următor. Beneficiarii sunt în principal rezidenți; veniturile nerezidenților se declară în general în D207.

#### 2. Funcționalități Cheie

- Raport de previzualizare live (motor `account.report`) cu impozitul reținut pe conturile 446x pentru persoanele fizice rezidente, grupat pe beneficiar și document.
- Generarea ciornei D205 dintr-un clic, cu import din 446x pentru PF rezidente (fără țară sau cu țara România, fără bifa de nerezident „Impozit la sursă (WHT)"), din **Contabilitate → ANAF → Declarații ANAF → Declarație 205**.
- Nomenclatorul oficial al naturii veniturilor (13 coduri: 04, 08, 09, 11, 12, 16, 18, 25–30) și regimul fiscal pe cod (0 / 2 impozit final / 3 neimpozabil prin convenție); importul propune codul 16, de schimbat pe natura reală a venitului.
- Câmpuri specifice pe cod: dividende distribuite și plătite (08), câștig și pierdere (25), venit în natură și garanția chiriei (29).
- Rezidență pe beneficiar, cu statul de rezidență și CIF-ul străin doar la nerezidenți (admiși doar la codurile 04, 16, 18, 25–30).
- Verificările validatorului ANAF la confirmare: CNP/NIF, rezidență pe cod, regim fiscal pe cod, beneficiar unic pe cod de venit, suma de control.
- Export XML validat cu schema `d205_2025_v3.xsd` și verificat cu DUKIntegrator; formular acceptat: OPANAF 102/2025.
- Integrare în lista de verificări `account.return` pentru închiderea anuală, cu pas manual de atașare a XML-ului semnat sau a recipisei.
- Declarație rectificativă și declarație depusă de succesor.

Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d205`: declarația persistentă D205 (an fiscal, stare ciornă/confirmată, rectificativă/succesor, linii beneficiari, totaluri); moștenește `l10n_ro_anaf.report.handler.mixin` și expune importul din contabilitate și exportul XML.
- `l10n.ro.anaf.d205.line`: linia unui beneficiar (CNP/NIF, rezidență, tip venit, regim fiscal, bază impozabilă, impozit reținut, câmpuri specifice codurilor 08, 25, 29).
- `l10n_ro_anaf_d205.report.handler` (`AbstractModel`): handlerul raportului de previzualizare `account.report`, peste conturile 446x pentru PF rezidente.
- `account.return` (extindere): termenul legal de depunere (ultima zi din februarie a anului următor) și verificările D205 din închiderea anuală.

**Vizualizări**

- `views/l10n_ro_anaf_d205_view.xml`: lista și formularul declarației D205, cu importul din 446x, confirmarea/resetarea și exportul XML.
- `data/d205_report.xml`: raportul de previzualizare „D205 — Previzualizare impozit reținut la sursă (PF rezidente)".

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul, generarea ciornei și exportul XML se declanșează manual. Modulul înregistrează tipul de declarație `account.return` și pașii de verificare din `data/d205_return_data.xml` și `data/d205_return_checks.xml`.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): mixin-ul comun de handler ANAF, registrul profilurilor de declarații și butoanele de export.
- [l10n_ro_anaf_d207](../l10n_ro_anaf_d207/index.md): declară veniturile nerezidenților, persoane fizice sau juridice, complementar cu D205.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): declarație informativă ANAF înrudită, din același ecosistem de raportare fiscală.
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md): furnizează bifa „Impozit la sursă (WHT)" pe partener, folosită la separarea rezidenților de nerezidenți.
