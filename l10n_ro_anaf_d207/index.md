# Romania - Declarația 207 ANAF (impozit la sursă nerezidenți) (localizat la `l10n_ro_anaf_d207/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d207`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d207
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d207`
- **Ultima Ingestie:** 2026-10-09
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru întocmirea și exportul Declarației 207 — declarația informativă privind impozitul reținut la sursă pe veniturile plătite nerezidenților, persoane fizice și juridice (art. 231 Cod fiscal), depusă anual la ANAF (termen: ultima zi din februarie a anului următor). Beneficiarii persoane fizice rezidente se declară în [D205](../l10n_ro_anaf_d205/index.md).

#### 2. Funcționalități Cheie

- Import automat al beneficiarilor nerezidenți (persoane fizice și juridice) din conturile 446x: parteneri cu bifa „Impozit la sursă (WHT)" (`l10n_ro_wht_applicable`) sau cu țara diferită de România; importul cere țara de rezidență și numește partenerii care nu o au; pe linie apare coloana „Persoană juridică"
- Identificatori separați automat: CUI sau CNP/NIF românesc valid (cu cifra de control) în `cifR`, codul fiscal din statul de rezidență în `cifS`
- Nomenclatorul oficial al naturii veniturilor (art. 223 și art. 229 Cod fiscal), cu venituri impozabile și scutite (codurile 12–21); codul propus la import este 07 (servicii prestate de nerezidenți); baza legală: 1 = Codul fiscal, 2 = convenția de evitare a dublei impuneri
- Totaluri secțiunea II calculate ca în validatorul ANAF: baza veniturilor scutite în `Tscutit`, `Tbaza` 0 pe scutite, suma de control `totalPlata_A` include `Timps`
- Regulile validatorului verificate la confirmare și la export, cu toate problemele afișate odată: stat de rezidență, CUI/CNP/NIF valid, impozit 0 pe venit scutit, beneficiar dublat pe același cod de venit
- Validare XML față de schema XSD `d207_20025020.xsd` (namespace v2) și export `D207_<CUI>_<an>12.xml`, gata de semnat și depus
- Workflow ciornă → confirmată (cu „Resetează la ciornă"), cu posibilitate de rectificativă (`d_rec`)
- Raport de previzualizare live (din jurnal, defalcat partener → document) cu buton „Generează ciornă D207"; calea: Contabilitate → Raportare → Declarații ANAF → Declarație 207
- Integrare cu fluxul `account.return`: checklist „ciornă generată", „beneficiari fără cod fiscal" (niciun cod, nici românesc, nici străin) și atașarea manuală a XML-ului semnat/recipisei; termen scadență calculat automat
- Modulul nu generează note contabile: impozitul reținut trebuie să fie deja înregistrat pe 446x

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d207`: declarația D207 persistentă (ciornă/confirmată), cu liniile de beneficiari nerezidenți (PJ și PF), tipuri de venit (01–25) și export XML validat XSD.
- `l10n_ro_anaf_d207.report.handler`: handler de raport de previzualizare (proiecție live peste conturile 446x), fără date proprii persistate; oferă butonul „Generează ciornă D207".
- `account.return` (extindere): calculează termenul legal de depunere (ultima zi din februarie a anului următor) și adaugă verificările automate specifice D207 (ciornă generată, beneficiari fără cod fiscal).

**Vizualizări**

- `views/l10n_ro_anaf_d207_view.xml`: formularele și listele pentru gestionarea declarației D207 (identificare, grilă beneficiari, workflow).

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul, generarea ciornei și exportul se declanșează manual din interfață.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează registrul profilurilor de declarații ANAF (`anaf_declaration_profile`) și meniul comun al declarațiilor ANAF.
- [l10n_ro_anaf_d205](../l10n_ro_anaf_d205/index.md): declarație ANAF înrudită (impozit reținut la sursă, persoane fizice rezidente); D207 acoperă complementul nerezident.
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): declarație ANAF înrudită din aceeași suită de raportare fiscală.
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md): furnizează bifa WHT (`l10n_ro_wht_applicable`) folosită la import.
- `l10n_ro_reports`: sursa mixin-ului `account.return` peste care se integrează fluxul de verificări și termene D207.
