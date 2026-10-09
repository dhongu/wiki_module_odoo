# Romania - Declarația 205 ANAF (impozit reținut la sursă, beneficiari PF) (localizat la `l10n_ro_anaf_d205/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d205`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d205
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d205`
- **Ultima Ingestie:** 2026-10-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru întocmirea Declarației 205 — declarația informativă privind impozitul reținut la sursă și câștigurile/pierderile din investiții, pe beneficiari de venit **persoane fizice**. Se depune de plătitorii de venituri cu regim de reținere la sursă (art. 132 alin. (2) Cod fiscal), până în ultima zi a lunii februarie a anului următor. Este adresat contabililor care plătesc persoanelor fizice dividende, dobânzi, premii, chirii sau alte venituri cu impozit reținut la sursă — cel mai des, dividende către asociații persoane fizice. Beneficiarii sunt în principal **rezidenți**; veniturile nerezidenților se declară în general în D207 (modulul [l10n_ro_anaf_d207](../l10n_ro_anaf_d207/index.md)). Fluxul merge de la previzualizarea mișcărilor contabile până la exportul XML validat.

#### 2. Funcționalități Cheie

- Raport de previzualizare live (motor `account.report`) cu impozitul reținut pe conturile 446x pentru persoanele fizice rezidente, grupat pe beneficiar și document
- Generarea ciornei D205 dintr-un clic, cu import din 446x pentru PF rezidente (fără țară sau cu țara România, fără bifa de nerezident „Impozit la sursă (WHT)"); meniu: Contabilitate → ANAF → Declarații ANAF → Declarație 205
- Nomenclatorul oficial al naturii veniturilor (13 coduri: 04, 08, 09, 11, 12, 16, 18, 25–30); importul propune codul 16, care trebuie schimbat pe natura reală (ex. 08 — Dividende)
- Regim fiscal pe cod (0 / 2 impozit final / 3 neimpozabil prin convenție), propus automat după cod (0 pentru 25, 2 pentru restul; 3 posibil la 26 și 27)
- Câmpuri specifice pe cod: dividende distribuite și plătite (08), câștig și pierdere în loc de bază și impozit (25), venit brut în natură și garanția chiriei (29)
- Rezidență pe beneficiar (implicit rezident); statul de rezidență și CIF-ul străin se completează și se exportă doar la nerezidenți (admiși doar la codurile 04, 16, 18, 25–30)
- Verificările validatorului ANAF la confirmare și la export, cu toate problemele raportate odată: CNP/NIF lipsă, rezidență nepermisă pe cod, nerezident fără stat, regim fiscal nepermis, același CNP/NIF de două ori pe același cod de venit
- Export XML conform structurii ANAF 2025, validat cu schema `d205_2025_v3.xsd` și verificat cu DUKIntegrator; suma de control `totalPlata_A` calculată după formula ANAF (număr de beneficiari plus totalurile secțiunii II)
- Workflow ciornă → confirmată, cu resetare la ciornă pentru corecții
- Integrare în lista de verificări `account.return` pentru închiderea anuală: generarea ciornei din 446x, beneficiari fără CNP/NIF, atașarea manuală a XML-ului semnat / recipisei
- Declarație rectificativă și declarație depusă de succesor (cu CIF succesor)

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d205`: declarația persistentă D205 (an fiscal, stare ciornă/confirmată, flag rectificativă/succesor, linii beneficiari, totaluri); moștenește `l10n_ro_anaf.report.handler.mixin`, expune importul din 446x, validarea regulilor ANAF și generarea/exportul XML.
- `l10n.ro.anaf.d205.line`: linia unui beneficiar (CNP/NIF România, rezidență, stat de rezidență și CIF străin pentru nerezidenți, tip venit, regim fiscal, bază, impozit, plus câmpurile specifice codurilor 08, 25 și 29).
- `l10n_ro_anaf_d205.report.handler` (`AbstractModel`): handler pentru raportul de previzualizare `account.report` — interoghează conturile 446x pentru PF rezidente, oferă butoanele „Generate D205 Draft" și export XML și populează date demo (`_load_demo_wht`).
- `account.return` (extindere): adaugă termenul legal de depunere (ultima zi a lunii februarie a anului următor) și verificările D205 în fluxul de închidere anuală.

**Vizualizări**

- `views/l10n_ro_anaf_d205_view.xml`: formularul și lista declarației D205, cu acțiunile de import din contabilitate, confirmare/resetare și export XML.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul, generarea ciornei și exportul XML se declanșează manual, din raportul de previzualizare sau din formularul declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează mixin-ul comun de handler ANAF, registrul de profile de declarații și butoanele de export.
- [l10n_ro_anaf_d207](../l10n_ro_anaf_d207/index.md): declarația veniturilor nerezidenților (PF și PJ), complementară D205, care acoperă beneficiarii nerezidenți.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): declarație informativă ANAF înrudită (același ecosistem de raportare fiscală RO).
- `account.return` (din `account`): fluxul de închidere anuală în care D205 își înregistrează verificările proprii.
