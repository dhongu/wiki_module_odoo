# Fișă Modul: Avans chenzinal pe salarii

**Modul:** `l10n_ro_payroll_advance`
**Utilizator principal:** responsabil salarizare / contabil
**Prioritate:** 🟡 Medie (avansul se poate ține în afara sistemului, dar atunci 425 nu se lămurește pe salariat și statul de avansuri se face de mână)

## 1. Scop business

Firmele care plătesc salariul în două tranșe dau salariaților un avans la jumătatea lunii. Fără modul, avansul nu apare în fluturaș: contabilul plătește avansul de mână, iar la salariul lunii scade suma din plata restului, fără urmă în fluturaș și fără lichidarea contului 425. Modulul ține avansul într-un lot cu plata contabilizată pe 425, îl lichidează automat pe fluturașul lunii (`Dr 421 = Cr 425`), scade avansul din restul de plată fără să atingă brutul, contribuțiile sau impozitul, și tipărește statul de avansuri cu semnături.

## 2. Bază legală și context

- **Plata salariului**: Codul muncii, art. 166 alin. (1): salariul se plătește cel puțin o dată pe lună, la data stabilită în contractul individual sau colectiv de muncă ori în regulamentul intern. Data și mărimea avansului țin de aceste documente; legea nu fixează sume minime sau maxime.
- **Fiscalitate**: avansul nu se impozitează separat și nu generează contribuții. Impozitul și contribuțiile se calculează lunar, pe venitul total al lunii, la data ultimei plăți a salariului lunii (Codul fiscal, art. 80; HG 1/2016, Titlul IV, pct. 16 alin. 3). Avansul nu apare în D112.
- **Monografie** (OMFP 1802/2014): plata `425 = 5121 / 5311`; lichidarea pe statul de plată `421 = 425`; plata restului `421 = 5121 / 5311`.
- **Avans mai mare decât netul**: diferența rămâne pe 425 și se reține pe statul de plată al lunii următoare (`Dr 421 = Cr 425`; funcțiunea contului 425 admite pe credit doar 421 și 423); reținerile cumulate nu pot depăși jumătate din salariul net (Codul muncii, art. 169 alin. 4). Contul 4282 `Alte creanțe în legătură cu personalul` se folosește doar când suma devine creanță (de exemplu la încetarea contractului). Recuperarea automată nu este implementată.
- **Avans nerecuperat** (de exemplu la încetarea contractului): temei posibil art. 256 alin. (1) Codul muncii; practica pentru reținere fără acord scris nu este unitară, **de confirmat juridic**.

## 3. Utilizatori și roluri

Administrator salarizare (grupul *Salarizare / Administrator*): creează și confirmă loturile, tipărește statul. Contabilul verifică nota și soldul 425.

## 4. Conturi și date implicate

| Operațiune | Debit | Credit | Partener |
|---|---|---|---|
| Plata avansului (confirmarea lotului) | 425 Avansuri acordate personalului | 5121 / 5311 (contul din jurnal) | salariatul (contactul de muncă), pe ambele linii |
| Lichidarea (validarea fluturașului) | 421 Personal - salarii datorate | 425 | salariatul |
| Plata restului (butonul de plată al fluturașului) | 421 | 5121 / 5311 | salariatul |

Regula *Lichidare avans* (cod `AVANS`, secvența 205, categoria proprie *Avans de salarii*) este în afara categoriilor BASIC, ALW, DED și GROSS, deci brutul, CAS, CASS, CAM, impozitul și netul rămân neschimbate. Suma regulii este minus min(avansurile plătite ale lunii, net), de unde restul de plată nu devine negativ.

## 5. Configurare inițială

- Procentul implicit al avansului pe companie (*Setări → Salarizare*), implicit 40%.
- Conturile regulii (425 și 421) se completează automat pe planul RO; pe alte planuri se completează pe regulă.
- Jurnal de bancă sau de numerar cu cont implicit (5121 / 5311).
- Salariații au contact de muncă și contract activ în luna avansului.

## 6. Flux de utilizare

### Pasul 1 — Lotul de avans

*Salarizare → Fluturași → Avansuri de salarii* → **Nou**: luna, data plății, jurnalul, procentul sau suma fixă, apoi **Generează salariații**. Suma se poate edita pe linie.

**Verificați:** apar doar salariații cu contract activ în lună; fiecare apare o singură dată; liniile peste netul estimat sunt marcate, iar lotul arată avertizarea.

### Pasul 2 — Plata

**Confirmă plata** postează `Dr 425 = Cr 5121 / 5311`, pe salariat.

**Verificați:** în nota contabilă, totalul pe 425 este totalul lotului; fiecare linie are salariatul ca partener.

### Pasul 3 — Statul de avansuri

**Tipărește statul** (PDF A4 pe lat, cu coloană de semnătură) sau **Exportă XLSX**.

**Verificați:** numărul de linii și totalul coincid cu lotul.

### Pasul 4 — Lichidarea pe fluturaș

La calculul fluturașului lunii apare regula *Lichidare avans*, cu minus. La validare se creează nota fluturașului cu `Dr 421 = Cr 425`; linia lotului devine *Lichidat*. Nota fluturașului se postează ca de obicei: la postare, linia `Cr 425` se reconciliază automat cu liniile `Dr 425` ale lotului de avans (parțial, dacă sumele diferă), așa că în nota fluturașului rămân deschise doar 421 și contul de plată, iar butonul de plată al fluturașului acceptă nota. La invalidarea sau anularea fluturașului reconcilierea se desface.

**Verificați:** *Net* și brutul fluturașului sunt aceleași ca fără avans; restul de plată (soldul 421 al salariatului) este net − avans; soldul 425 al salariatului este zero.

### Pasul 5 — Avansul mai mare decât netul

Se scade doar netul; restul de plată este 0; pe fluturaș și pe lot apare avertizarea; diferența rămâne pe 425 (linia lotului este *Parțial lichidat*). Diferența se reține pe statul de plată al lunii următoare (`Dr 421 = Cr 425`), în limita de jumătate din salariul net pentru toate reținerile cumulate; 4282 doar când suma devine creanță (de exemplu la încetarea contractului).

### Pasul 6 — Anularea

Lotul se anulează cu **Anulează** (nota plății se stornează). Un lot lichidat pe un fluturaș validat nu se anulează înainte de anularea fluturașului. La invalidarea fluturașului, avansul revine la *Nelichidat*.

### Note de monografie și raportare

Avansul nu intră în D112 și nu modifică baza de calcul a contribuțiilor. Fișierul bancar al fluturașului conține netul întreg, fără avans: pentru avansuri plătite prin bancă, plata se face din extrasul bancar sau manual.

## 7. Legături cu alte module / declarații

| Modul | Rol |
|---|---|
| `l10n_ro_hr_payroll_enhancement` | fluturașii și regulile RO |
| `l10n_ro_hr_payroll_account_enhancement` | mecanismul de conturi pe reguli (421 și contul de personal pe linie) |
| `l10n_ro_payroll_statements` | statul de plată (doar NET, fără avans); statul de avansuri este un raport separat, al acestui modul |
| `l10n_ro_payroll_bank_export` | fișier bancar pe fluturași (netul întreg; fără avans în v1) |

**Automat:** sumele implicite, nota plății, lichidarea, plafonarea la net, avertizările. **Automat și reconcilierea 425** cu plata avansului, la postarea notei fluturașului. **Manual:** reținerea diferenței rămase pe 425 în luna următoare, plata avansului prin bancă.

## 8. Verificări pentru consultant

- [ ] Lotul conține doar salariați cu contract activ în lună, câte o linie fiecare.
- [ ] Nota plății: `Dr 425 = Cr 5121 / 5311`, cu salariatul ca partener pe ambele linii.
- [ ] Fluturașul cu avans: brut, CAS, CASS, impozit și net identice cu cele fără avans.
- [ ] La validare apare `Dr 421 = Cr 425`, pe salariat, pentru suma lichidată.
- [ ] Avans peste net: restul de plată este 0, avertizarea apare, soldul 425 este diferența.
- [ ] Anularea lotului stornează nota; un lot lichidat nu se poate anula.
- [ ] Statul PDF și XLSX au aceleași sume ca lotul.

## 9. Mesaje de eroare frecvente

| Mesaj | Cauză | Remediere |
|---|---|---|
| Adăugați cel puțin un salariat în avans | lotul nu are linii | apăsați *Generează salariații* sau adăugați linii |
| Fiecare linie trebuie să aibă o sumă mai mare decât 0 | o linie are suma zero | ștergeți linia sau completați suma |
| Jurnalul … nu are cont implicit | jurnalul de plată nu are cont | setați contul implicit al jurnalului |
| Contul 425 lipsește din planul de conturi | planul nu are 425 | adăugați contul sau completați regula |
| Avansul … este deja lichidat pe un fluturaș validat | lotul are sume lichidate | anulați fluturașul, apoi lotul |

## 10. Capturi de ecran

Capturile nu sunt generate în această versiune.

## 11. Observații pentru manual

- Netul estimat din avertizarea lotului folosește fluturașul lunii dacă este calculat, altfel salariul de bază cu CAS, CASS și impozit, fără deduceri personale: este o estimare.
- Dacă fluturașul a fost validat înainte de confirmarea avansului, avansul rămâne nelichidat: invalidați fluturașul și recalculați-l.
- Pentru mai multe loturi pe aceeași lună, avansurile se lichidează împreună pe fluturaș, în ordinea creării.
- Recuperarea automată din luna următoare și fișierul bancar al avansului sunt în ROADMAP.
- Statul de plată semnat din `l10n_ro_payroll_statements` (`wizard/l10n_ro_payroll_statement.py`) are doar coloana NET, fără avans și fără rest de plată, deși plata salariului se dovedește prin semnarea statelor (Codul muncii, art. 168 alin. 1): de completat într-un PR separat, nu în acest modul. Până atunci se semnează statul de avansuri la avans și statul de plată la lichidare.
- Regula *Lichidare avans* este legată doar de structura `hr_payroll_structure_ro_employee_salary`: pe alte structuri avansul rămâne *Nelichidat*.
- Dacă o ciornă de fluturaș are deja linia de lichidare, lotul nu se poate anula până la recalcularea sau ștergerea ei.
- Un al doilea fluturaș al aceleiași luni (corecție) nu scade din nou avansul deja lichidat pe un fluturaș validat.
