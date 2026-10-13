# Romania - Corecții rapoarte contabile (localizat la `l10n_ro_reports_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_reports_fix`
- **Versiune:** `19.0.0.0.14`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reports_fix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reports_fix`
- **Ultima Ingestie:** 2026-10-13
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul corectează **Balanța de verificare (RO)**, cu 4 și 5 coloane, din `l10n_ro_reports`, astfel încât soldul inițial și soldul final al fiecărui cont să apară pe o singură coloană (Debit sau Credit), conform contabilității românești (OMFP 1802/2014). Pe lângă corecția de calcul, oferă trei opțiuni de afișare în meniul **Opțiuni**: **Balanță brută** (fără închiderea virtuală făcută de Odoo), **Ascunde conturile extrabilanțiere** și **Conturile extrabilanțiere în bloc separat**. Se adresează contabililor care pregătesc balanța pentru situațiile financiare, pentru audit sau pentru comparația cu o balanță primită din altă aplicație.

#### 2. Funcționalități Cheie

Funcționalitățile urmează tabelul „Ce înseamnă fiecare funcționalitate” din fișa consultant.

**Corecții mereu active**

- **Sold inițial net:** Odoo pune la soldul inițial sumele debitoare și creditoare cumulate până la începutul perioadei, deci un cont poate avea sume pe ambele coloane. Modulul afișează soldul de deschidere net, pe o singură coloană (un client facturat și încasat anul trecut începe cu 0 / 0).
- **Sold final:** era deja net pe cont în `l10n_ro_reports`; modulul corectează grupele (fără compensare) și aplică natura contului, dacă e definită.
- **Suma totală recalculată:** Suma totală = Soldul inițial net + rulajul perioadei; egalitatea Debit = Credit se păstrează.
- **Grupe și total fără compensare:** pe o grupă, soldurile debitoare și cele creditoare ale conturilor se adună separat, deci o grupă poate avea sold și pe Debit, și pe Credit (de exemplu clasa 4 Conturi de terți). Valorile se propagă corect la fiecare nivel al ierarhiei.
- **Natura contului activ / pasiv** (doar cu `l10n_ro_storno_enhancement`, câmpul `l10n_ro_usage`): contul activ își arată soldul doar pe Debit, cel pasiv doar pe Credit. Un sold „pe partea greșită” apare cu minus (de exemplu un furnizor plătit în avans), ca să iasă în evidență. Conturile fără natură completată se comportă ca bifuncționale.

**Opțiuni în meniul Opțiuni**

- **Balanță brută:** la începutul fiecărui exercițiu, Odoo mută soldurile din anii precedenți ale conturilor **6xx, 7xx și 121** pe linia „Result Brought Forward”. Opțiunea oprește această închidere virtuală: fiecare cont își arată soldul real, iar linia „Result Brought Forward” dispare. La firmele care înregistrează notele de închidere, e varianta corectă pentru RO (121 cu soldul lui, 6 și 7 cu zero); altfel, arată notele de închidere lipsă. Utilă la migrarea soldurilor și la comparația cu balanțe externe.
- **Ascunde conturile extrabilanțiere:** balanța conține doar conturile din bilanț (clasele 1–7); conturile de tip „În Afara bilanțului” (clasele 8 și 9) nu apar nici în linii, nici în totaluri.
- **Conturile extrabilanțiere în bloc separat:** grupa 80 apare sub totalul general, cu subtotal propriu, ca evidență în partidă simplă (OMFP 1802/2014, cap. 16); contrapartida tehnică 803999 nu apare, iar grupa 89 „Bilanț” rămâne în totalul general (partidă dublă).
- **Varianta implicită** (nicio opțiune bifată): clasa 8 intră în balanță și în totalul general, inclusiv contrapartida 803999, iar balanța rămâne egală; servește reconcilierii contrapartidei.
- Opțiunile se pot combina; dacă sunt bifate și „Ascunde”, și „Bloc separat”, are prioritate „Ascunde”. Ierarhia pe grupe se activează din **Opțiuni → Ierarhia și subtotalurile**.
- **Export:** PDF și XLSX păstrează varianta aleasă pe ecran.
- **Cale de meniu:** Contabilitate → Raportare → Registre → Balanța de verificare (raportul „Balanța de verificare (5 coloane) (RO)” sau varianta cu 4 coloane).
- **Notă extrabilanțieră:** notele din grupa 80 se fac pe o contrapartidă tehnică comună, contul 803999, în jurnalul EXTR, deoarece Odoo nu acceptă o notă care amestecă conturi „În Afara bilanțului” cu conturi de bilanț. Contul și jurnalul vin din `l10n_ro_off_balance`, opțional.

#### 3. Dependențe

- `l10n_ro_reports`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md` și fișei consultant; detaliile de cod sunt din `models/trial_balance.py`.

**Modele**

- `l10n.ro.trial.balance.5.column.report.handler` (extins): handlerul balanței RO. Suprascrie inițializarea opțiunilor, motorul de calcul al balanței, postprocesarea liniilor (sold net, natura contului, recalcularea grupelor și a totalului) și mutarea grupei 80 în bloc separat.

**Vizualizări**

- `static/src/components/account_report/filters/filters.esm.js` (asset `web.assets_backend`): componentă OWL care adaugă în meniul Opțiuni cele trei opțiuni (Raw trial balance, Hide off-balance accounts, Off-balance accounts in a separate block) și completează eticheta butonului de opțiuni.

**Acțiuni Automate / Acțiuni Server**

*Nu sunt definite; modulul intervine pe motorul de raportare și pe interfața raportului.*

#### 5. Conexiuni

- [l10n_ro_off_balance](../l10n_ro_off_balance/index.md): creează contul 803999, jurnalul EXTR și grupele 8 / 80 / 801–809 / 89, folosite de opțiunile pentru conturi extrabilanțiere (opțional).
- [l10n_ro_storno_enhancement](../l10n_ro_storno_enhancement/index.md): câmpul `l10n_ro_usage` (natura contului activ/pasiv) folosit la afișarea soldului final (opțional).
