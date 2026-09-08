# Credit Control Cockpit (localizat la `deltatech_credit_control/index.md`)

- **Nume Tehnic:** `deltatech_credit_control`
- **Versiune:** `19.0.0.0.2`
- **Cale:** `https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_credit_control`
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_credit_control`
- **Ultima Ingestie:** `2026-09-08`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul construiește un clasament al clienților cu restanțe și arată clar cui trebuie sunat primul. Raportul standard de balanță pe vechimi spune cât este restant, dar nu spune pe cine să suni prima dată — acest modul răspunde exact la acea întrebare. Fiecare client cu sold restant primește un scor de risc de la 0 la 100, calculat din vechimea celei mai vechi restanțe, valoarea ei, comportamentul istoric la plată și numărul de documente neîncasate; pe baza scorului, clienții sunt împărțiți în patru benzi de risc (critic, ridicat, mediu, mic). Modulul nu scrie nimic în contabilitate — este o interogare live peste liniile contabile de creanță, la fiecare deschidere a ecranului.

#### 2. Funcționalități Cheie

- Scor de risc 0-100 per client, calculat din patru componente ponderate (vechime, valoare, comportament la plată, număr de documente), fiecare pondere și prag de saturație fiind configurabile.
- Patru benzi de risc: critic, ridicat, mediu, mic — etichetele din interfață.
- Lista de lucru „Clienți de urmărit" (**Contabilitate → Control creanțe → Clienți de urmărit**), sortată după suma restantă, colorată pe nivel de risc, cu numărul de telefon direct pe rând; se poate grupa pe agent de vânzări sau pe județ.
- Vedere „Cazuri critice" — aceleași date, sub formă de carduri, utilă pentru ședința de dimineață.
- „Documente neîncasate" — liniile contabile de creanță una câte una, cu tranșa de vechime calculată automat; filtre rapide *Peste 90 zile* și *În litigiu*.
- Fișa clientului centralizează: date de contact, sold, vechime, comportament la plată pe ultimele 12 luni (întârziere obișnuită, întârziere maximă, ultima plată, număr de documente stinse) și lista documentelor deschise, cu butoane rapide către facturile deschise și către fișa de contact.
- Cifra de afaceri pe ultimele 12 luni afișată lângă restanță, pentru a pune datoria în context.
- Plafon de credit și depășirea lui, ținând cont și de plafonul implicit al companiei, nu doar de cel setat individual pe client.
- Rapoarte pivot și grafic pe agent de vânzări, stare, țară și luna scadenței.
- Raport PDF „Situație control creanțe" per client, generabil în masă din listă (**Print / Credit control statement**), cu datele de contact și documentele deschise.
- Datele provin din liniile contabile de creanță postate și nereconciliate (conturi de tip creanțe, ex. 411x), citite live, nu dintr-o copie stocată — aceeași bază ca raportul standard de balanță pe vechimi, deci cele două reconciliază.
- Acces controlat printr-un grup dedicat (**Control creanțe → Vede rapoartele**, acces read-only), setat din Setări → Utilizatori; necesită și un drept minim de Contabilitate (Facturare), altfel aplicația Contabilitate rămâne ascunsă.
- Configurare per companie în **Contabilitate → Configurare → Setări**, bloc „Control creanțe": ponderi scor (implicit vechime 40, valoare 25, istoric plăți 20, nr. documente 15 — însumează 100), praguri de saturație (90 zile, 10.000 monedă companie, 30 zile întârziere uzuală, 10 documente), praguri de risc (critic 70, ridicat 45, mediu 25), prag minim de ignorare a restanțelor (implicit 1) și opțiunea de a include facturile contestate (stare de plată „Blocat").
- Recalcularea situației la o dată din trecut, prin transmiterea cheii de context `credit_control_date` (ex. `{'credit_control_date': '2026-12-31'}`).

#### 3. Dependențe

- `account`
- `sales_team`

#### 4. Componente Cheie

Documentația pentru 'Sumar' și 'Funcționalități Cheie' a fost preluată din fișierul `readme/DESCRIPTION.md` (completată cu detalii operaționale din `readme/USAGE.md` și `readme/CONFIGURE.md`). Conform fluxului de ingestie, analiza detaliată a componentelor (Modele, Vizualizări, Acțiuni) din cod este omisă, deoarece nu este menționată explicit în Readme.

#### 5. Conexiuni

- [l10n_ro_receivables_enhanced](../l10n_ro_receivables_enhanced/index.md): calculul efectiv al penalităților de întârziere (Legea 72/2013) se face acolo, nu în acest modul, care doar clasifică și clasează riscul.
