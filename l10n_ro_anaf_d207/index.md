# Romania - Declarația 207 ANAF (impozit la sursă nerezidenți) (localizat la `l10n_ro_anaf_d207/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d207`
- **Versiune:** `20.0.1.2.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d207
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d207`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru întocmirea și exportul **Declarației 207** — declarația informativă privind impozitul reținut la sursă pe veniturile plătite **nerezidenților, persoane fizice și juridice** (art. 231 Cod fiscal). Se depune anual la ANAF, până în ultima zi din februarie a anului următor. Beneficiarii persoane fizice rezidente se declară în D205.

#### 2. Funcționalități Cheie

- Import automat al beneficiarilor nerezidenți din conturile 446x: parteneri cu bifa „Impozit la sursă (WHT)" sau cu țară diferită de România, persoane fizice și juridice; țara de rezidență este obligatorie.
- Identificatori separați automat: CUI sau CNP/NIF românesc valid în `cifR`, codul fiscal din statul de rezidență în `cifS`.
- Nomenclatorul oficial al naturii veniturilor (art. 223 și 229 Cod fiscal), cu venituri impozabile și scutite (codurile 12–21); importul propune codul 07 (servicii prestate de nerezidenți).
- Totalurile secțiunii II ca în validatorul ANAF: baza veniturilor scutite în `Tscutit`, suma de control cu toate totalurile.
- Verificările validatorului la confirmare și export: stat de rezidență, CUI/CNP/NIF valid, impozit 0 pe venit scutit, beneficiar dublat pe același cod.
- Validare XML cu schema `d207_20025020.xsd` (namespace v2) și export **XML ANAF** (`D207_<CUI>_<an>12.xml`); formular acceptat: OPANAF 179/2022.
- Export **Soft A**: formularul PDF ANAF completat, sau doar XDP / arhivă ZIP, după tipul de export din **Setări → Contabilitate → Declarații ANAF**.
- Workflow ciornă → confirmată, cu declarație rectificativă (`d_rec`).
- Raport de previzualizare live cu buton „Generează ciornă D207"; integrare cu `account.return` (ciornă generată, beneficiari fără cod fiscal, termen calculat automat).

Fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d207`: declarația D207 persistentă (ciornă/confirmată), cu beneficiarii nerezidenți, totaluri și exporturile XML și Soft A.
- `l10n.ro.anaf.d207.line`: linia unui beneficiar (nume, cifR/cifS, țara de rezidență, tip venit, scutire, bază, impozit reținut, bază legală).
- `l10n_ro_anaf_d207.report.handler`: handlerul raportului de previzualizare, proiecție live peste conturile 446x; oferă butonul „Generează ciornă D207".
- `account.return` (extindere): termenul legal de depunere și verificările specifice D207.

**Vizualizări**

- `views/l10n_ro_anaf_d207_view.xml`: lista și formularul declarației (identificare, grila beneficiarilor, workflow).
- `views/d207_xdp_export.xml`: exportul Soft A (XDP / PDF).
- `data/d207_report.xml`: raportul „D207 — Previzualizare impozit la sursă nerezidenți".

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul, generarea ciornei și exportul se declanșează manual. Tipul de declarație `account.return` și pașii de verificare vin din `data/d207_return_data.xml` și `data/d207_return_checks.xml`.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): registrul profilurilor de declarații ANAF, mixin-ul de handler și meniul comun.
- [l10n_ro_anaf_d205](../l10n_ro_anaf_d205/index.md): declară persoanele fizice rezidente, complementar cu D207.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): declarație informativă ANAF înrudită, din aceeași suită de raportare fiscală.
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md): bifa „Impozit la sursă (WHT)" pe partener, folosită la importul nerezidenților.
