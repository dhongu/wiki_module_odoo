# Fișă Modul: Sporuri, ore suplimentare și muncă de noapte

**Modul:** `l10n_ro_payroll_allowances`
**Utilizator principal:** Responsabil salarizare / contabil
**Prioritate:** 🟡 Medie (sporurile se configurează o dată; calculul lunar e automat)

## 1. Scop business

Aduce în brutul fluturașului sporurile pe care firmele din România le plătesc lunar: sporuri permanente (vechime, condiții vătămătoare, ...), spor pentru orele suplimentare și spor pentru munca de noapte. Contabilul nu mai calculează sporurile de mână și nu mai introduce sume ca «prime»: procentul și baza se configurează o dată, iar fluturașul le calculează, le include în CAS, CASS, CAM și impozit și le trece în media indemnizației de concediu, acolo unde legea cere.

## 2. Bază legală și context

- Codul muncii, art. 123 alin. (2): ore suplimentare compensate cu timp liber în 90 de zile (art. 122), iar dacă nu e posibil, cu un spor de cel puțin 75% din salariul de bază.
- Codul muncii, art. 125–126: munca de noapte (22:00–06:00); salariatul de noapte (cel puțin 3 ore de noapte din programul normal) primește program redus cu o oră sau un spor de cel puțin 25% din salariul de bază.
- Codul muncii, art. 137–138 și 142: munca în repausul săptămânal suspendat sau cumulat (cel puțin 150%) și în sărbătorile legale (cel puțin 100%) — **nu** sunt acoperite de modul.
- Codul muncii, art. 150: media indemnizației de concediu include sporurile cu caracter permanent.
- Codul fiscal, art. 76 alin. (1): sporurile sunt venituri din salarii, deci intră în baza CAS, CASS, CAM și a impozitului.

## 3. Utilizatori și roluri

- **Utilizator salarizare:** adaugă sporurile pe angajat și introduce orele de noapte.
- **Administrator salarizare:** configurează nomenclatorul de sporuri.

## 4. Conturi și date implicate

- **641** Cheltuieli cu salariile personalului = **421** Personal – salarii datorate, prin linia `GROSS` (sporurile nu au conturi proprii).
- Date minime: un angajat cu versiune de contract, salariu lunar și prezențe generate pentru luna calculată.

## 5. Configurare inițială

1. Instalați `l10n_ro_payroll_allowances` (nu se instalează automat: schimbă brutul).
2. Verificați *Stat de plată → Configurare → Sporuri salariale*: există *Spor pentru ore suplimentare* (75%) și *Spor pentru munca de noapte* (25%), cu procentele minime legale; nu pot fi coborâte sub minim.
3. Creați sporurile permanente ale firmei (tip *Permanent*, procent, bază, bifa «în baza orelor suplimentare» doar dacă o prevede contractul).

## 6. Flux de utilizare

### Pasul 1 — Nomenclatorul de sporuri

*Stat de plată → Configurare → Sporuri salariale*. Fiecare spor are cod, tip, procent implicit și bază: **salariul de bază** (integral), **salariul aferent timpului lucrat** (reduce absențele fără plată) sau **salariul de bază plus celelalte sporuri permanente**.

![Nomenclatorul de sporuri](screenshots/01_nomenclator_sporuri.png)

**Verificați:** procentul orelor suplimentare ≥ 75, al sporului de noapte ≥ 25 (sporurile de ore suplimentare și de noapte nu se arhivează); baza sporurilor legate de munca prestată e *Salariu aferent timpului lucrat*.

**În luna cu concediu** (de odihnă, medical sau fără plată), sporurile pe *Salariu de bază*, *Salariu de bază plus sporuri* și sumele fixe se proratează cu timpul lucrat, iar indemnizația de concediu include deja drepturile permanente (media pe 3 luni și pragul din art. 150). Baza *Salariu aferent timpului lucrat* se proratează oricum.

### Pasul 2 — Sporurile permanente ale angajatului

*Angajați → fișa angajatului → fila Stat de plată → secțiunea Sporuri permanente (RO)*: adăugați sporul, procentul (sau suma fixă) și perioada de valabilitate. Un spor expirat sau început după lună nu intră în fluturaș. La schimbarea sporului pe un rând, procentul se preia din nomenclator (îl puteți modifica apoi); suma fixă are prioritate față de procent.

![Sporurile permanente pe fișa angajatului](screenshots/02_sporuri_angajat.png)

**Verificați:** fiecare rând are procent sau sumă fixă și data de început.

### Pasul 3 — Ore suplimentare și ore de noapte

- **Ore suplimentare:** vin din prezențele lunii, de tipul *Ore suplimentare* (de exemplu din pontaj, cu `l10n_ro_hr_pontaj_payroll`); le vedeți în fila *Zile lucrate* a fluturașului. Ele se plătesc la tariful orar prin salariul de bază (100%), iar sporul de 75% se adaugă separat. Folosiți acest tip numai pentru orele **plătite**; orele compensate cu timp liber se pontează pe alt tip de prezență, neplătit. Tipul de prezență *Ore suplimentare* trebuie să aibă rata 100%: sporul de 75% îl adaugă modulul (la o rată peste 100% diferența se scade din spor).

![Orele suplimentare în Zile lucrate](screenshots/03_fluturas_zile_lucrate.png)

- **Ore de noapte:** pe fluturaș, fila *Salary Inputs* (intrări), adăugați intrarea *Ore de noapte* cu numărul de ore.

![Intrarea Ore de noapte](screenshots/04_fluturas_ore_noapte.png)

**Verificați:** orele de noapte sunt cele lucrate între 22:00 și 06:00 de un salariat care are cel puțin 3 ore de noapte în programul normal.

### Pasul 4 — Fluturașul

Calculați fluturașul. În *Calcul Salariu* apar liniile *Sporuri permanente: …*, *Spor pentru ore suplimentare* și *Spor pentru munca de noapte*, în brut, înaintea liniei de salariu impozabil.

![Fluturașul cu sporuri](screenshots/05_fluturas_sporuri.png)

**Verificați** cifrele din exemplu (salariu 6.000 lei, septembrie 2026 cu 176 de ore normale):

- tarif orar: 6.000 / 176 = 34,09 lei/oră; salariul de bază cu cele 10 ore suplimentare la 100%: 6.000 + 10 × 34,09 = 6.340,91;
- sporuri permanente: vechime 10% × 6.000 = 600, condiții vătămătoare 5% din timpul lucrat = 300, total 900;
- tarif pentru sporurile de ore suplimentare și de noapte: (6.000 + 600 vechime marcată «în baza orelor suplimentare») / 176 = 37,50 lei/oră;
- spor ore suplimentare: 10 × 37,50 × 75% = 281,25; spor noapte: 24 × 37,50 × 25% = 225,00;
- *Salariu impozabil* = 6.340,91 + 900 + 281,25 + 225 = 7.747,16; CAS 1.937, CASS 775, impozit 503, net 4.532,16.

### Note de monografie și raportare

- La validare (cu `l10n_ro_hr_payroll_account_enhancement` instalat; fără el fluturașul nu generează nota), pe exemplul de mai sus:
    - **Dr 641 = Cr 421** 7.747,16 (brutul, inclusiv sporurile; sporurile nu au conturi proprii);
    - **Dr 421 = Cr 4315** 1.937 (CAS) și **Dr 421 = Cr 4316** 775 (CASS);
    - **Dr 421 = Cr 444** 503 (impozit);
    - **Dr 646 = Cr 436** 174 (CAM).
    Soldul 421 rămâne 4.532,16, egal cu netul.
- D112 (din fluturași, cu `l10n_ro_anaf_d112_payroll`): sporurile intră în venitul brut (`E3_8`) și în bazele CAS, CASS și impozit ale asiguratului.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `l10n_ro_hr_payroll_enhancement` | fluturașul, regulile și media concediului de odihnă |
| `l10n_ro_hr_pontaj_payroll` | prezențele de tip *Ore suplimentare* din pontaj |
| `l10n_ro_hr_payroll_account_enhancement` | nota contabilă a fluturașului (641 = 421 etc.) |
| `l10n_ro_anaf_d112` / `l10n_ro_anaf_d112_payroll` | declararea veniturilor în D112, din fluturașii validați |

**Automat:** calculul sporurilor, includerea lor în brut și în media CO (sporurile permanente), minimul legal al procentului. **Manual:** pontarea orelor compensate, orele de noapte, munca în sărbători și repaus săptămânal, clauza de mobilitate.

## 8. Verificări pentru consultant

- [ ] Procentele minime: ore suplimentare ≥ 75%, noapte ≥ 25%.
- [ ] Sporul permanent apare în fluturaș, în brut, cu denumirea lui în titlul liniei.
- [ ] Sporul permanent expirat nu apare.
- [ ] Tipul de prezență *Ore suplimentare* are rata 100%.
- [ ] Într-o lună cu concediu, sporul pe salariul de bază e proratat cu timpul lucrat (nu se plătește integral).
- [ ] Orele suplimentare: *Salariu de bază* crește cu orele × tariful orar, iar *Spor pentru ore suplimentare* = ore × tarif × 75%.
- [ ] Orele din sărbători legale și repaus săptămânal nu sunt trecute ca *Ore suplimentare* (nu li se aplică 100% / 150%).
- [ ] Orele compensate cu timp liber nu sunt pontate ca *Ore suplimentare*.
- [ ] CAS, CASS și impozitul includ sporurile.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| Minimul legal al acestui spor este de 75% / 25% | procent sub minim la ore suplimentare sau noapte | folosiți cel puțin minimul legal |
| Procentul și suma unui spor nu pot fi negative | valori negative pe rândul sporului | folosiți valori pozitive |
| Sporurile pentru ore suplimentare și muncă de noapte nu se pot arhiva | arhivarea sporurilor de ore suplimentare sau de noapte | lăsați-le active (procentul ar deveni 0) |
| Completați un procent sau o sumă fixă pentru spor | rând de spor fără procent și fără sumă | completați unul dintre ele |
| Data de sfârșit a unui spor nu poate fi înaintea celei de început | perioadă inversă | corectați datele |
| Codul sporului trebuie să fie unic pe companie | cod dublat | alegeți alt cod |

## 10. Capturi de ecran

Generate automat din `tests/test_screenshots.py` (mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, care trebuie instalat în baza de regenerare; altfel testul se sare), în RO, pe planul RO. Regenerare: `odoo-bin -c <conf> -d <baza_cu_ro_RO> -u l10n_ro_payroll_allowances --test-tags=fise_screenshots:TestAllowancesScreenshots --stop-after-init`.

- `01_nomenclator_sporuri.png`: nomenclatorul de sporuri.
- `02_sporuri_angajat.png`: sporurile permanente pe fișa angajatului.
- `03_fluturas_zile_lucrate.png`: orele suplimentare în fila *Zile lucrate*.
- `04_fluturas_ore_noapte.png`: intrarea *Ore de noapte*.
- `05_fluturas_sporuri.png`: fluturașul cu sporuri, ore suplimentare și de noapte.

## 11. Observații pentru manual

- Tariful orar este salariul lunar împărțit la orele normale ale lunii (variază de la lună la lună); se scrie în regulamentul intern sau contractul colectiv.
- În luna cu timp nelucrat, sporurile pe salariul de bază și sumele fixe se proratează cu timpul lucrat.
- Sporurile marcate «în baza orelor suplimentare» depășesc minimul legal (salariul de bază nu conține sporuri, art. 160 alin. (2)); se bifează doar dacă contractul le prevede.
- Munca în sărbători (100%) și în repausul săptămânal suspendat sau cumulat (150%) rămâne în afara modulului.
- Clauza de mobilitate (art. 76 alin. (4^1), neimpozabilă, în D112) nu este implementată.
- Sporurile de ore suplimentare și de noapte se calculează pe salariul de bază al lunii; în luna cu concediu, sporurile permanente se proratează, iar pragul minim al indemnizației de concediu folosește sporul proratat.
