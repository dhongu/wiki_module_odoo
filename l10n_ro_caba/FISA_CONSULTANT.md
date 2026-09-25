# Fișă Modul: TVA la încasare (CABA)

**Modul:** `l10n_ro_caba`
**Capitol manual:** Cap 3.6 — TVA la Încasare (4428)
**Utilizator principal:** Contabil, Manager Contabilitate
**Prioritate:** 🔴 Ridicată
**FR:** FR-16
**Poziție plan:** D3

---

## 1. Scop business

Firmele care aplică sistemul de TVA la încasare (sau care cumpără de la furnizori înregistrați în
acest sistem) nu declară TVA-ul la emiterea facturii, ci la încasarea ori plata ei. Până atunci,
TVA-ul stă în contul **4428 „TVA neexigibilă"**: 44281 pentru TVA colectată, 44282 pentru TVA
deductibilă.

Odoo are mecanismul nativ pentru asta, numit **CABA** — de la ***Ca**sh **Ba**sis*, „bază de
numerar": taxa e exigibilă la plată, nu la facturare. CABA e și codul jurnalului în care Odoo
înregistrează, la fiecare încasare sau plată, nota care mută TVA-ul din 4428 în 4427 / 4426.

Planul de conturi RO din Odoo aduce deja taxele la încasare (`TVA la colectare ...`), poziția
fiscală **Sistem de colectare TVA** și jurnalul CABA. Lasă însă nesetate câteva lucruri, iar
setările sunt împrăștiate și prost traduse. Modulul:

- setează automat, la instalare și la încărcarea planului RO, ce a rămas gol: bifa **Baza de
  numerar**, **jurnalul CABA** și **contul tehnic pentru baza impozabilă 442830**;
- nu suprascrie nicio valoare deja aleasă de contabil;
- pune singur poziția fiscală la încasare pe toate facturile și comenzile firmei în sistem (bifa
  **Compania aplică TVA la încasare**, din Setări) și o scoate de pe facturile de vânzare ale firmei
  normale — vezi cele 8 cazuri de la 5.4;
- adaugă în **Setări → Contabilitate → Taxe** o verificare a configurării, cu buton de completare;
- redenumește câmpul „Cont de primire fiscală de bază" (traducere greșită din nucleu) în
  **„Cont tehnic pentru baza TVA la încasare"**, cu explicație.

Modulul **nu depinde** de OCA `l10n_ro_vat_on_payment`. Acela citește regimul partenerilor din
lista ANAF, cu datele de intrare și ieșire; se poate instala în paralel. Fără el, bifa de pe
partener se pune manual (vezi pasul 2).

---

## 2. Noțiuni și abrevieri

| Termen | Ce înseamnă |
|---|---|
| **TVA la încasare** | Sistemul din art. 282 alin. (3)–(8) Cod fiscal: TVA-ul devine exigibil la încasarea facturii, nu la emiterea ei. Pentru cumpărător, deducerea se amână până la plată. |
| **CABA** | De la *Cash Basis* („bază de numerar"): mecanismul Odoo pentru taxele exigibile la plată. Tot CABA se numește jurnalul în care Odoo pune notele de exigibilitate. |
| **Exigibilitate** | Momentul în care statul poate pretinde TVA-ul și trebuie declarat în D300. În Odoo, câmpul **Exigibilitatea taxei**: *Pe baza facturii* (obișnuit) sau *Pe baza plății* (la încasare). |
| **TVA neexigibilă (4428)** | TVA facturată, dar încă nedeclarabilă. **44281** — colectată (la vânzare), **44282** — deductibilă (la cumpărare). Se golește la fiecare încasare sau plată. |
| **Cont de tranziție a bazei de numerar** | Contul de pe taxa la încasare în care stă TVA-ul până la plată: 44281 sau 44282. |
| **Cont tehnic pentru bază (442830)** | Contul pe care nota CABA scrie baza impozabilă, o dată pe debit și o dată pe credit, doar pentru rândurile de bază din D300. Are mereu sold zero. |
| **Nota CABA** / **nota de exigibilitate** | Nota creată automat la reconcilierea unei încasări sau plăți cu factura: mută TVA-ul proporțional din 4428 în 4427 / 4426. |
| **Persoană afiliată** | În practică, o firmă din același grup (legătura e definită la art. 7 pct. 26 Cod fiscal). Între firme din același grup, vânzătorul facturează cu TVA obișnuit, nu la încasare (art. 282 alin. (6) lit. d)). |
| **Companie / partener în sistem** | Înregistrat(ă) la ANAF în sistemul TVA la încasare. În Odoo: bifa **Compania aplică TVA la încasare** (Setări), respectiv poziția fiscală **Sistem de colectare TVA** pe partener. |
| **Poziție fiscală** | Regula Odoo care înlocuiește pe factură o taxă cu alta. **Sistem de colectare TVA** înlocuiește TVA-ul obișnuit cu cel la încasare. |
| **Plată parțială** | Încasarea unei părți din factură. TVA-ul exigibil e proporțional: suma × cotă / (100 + cotă), ex. 605 × 21/121 = 105. |
| **D300** | Decontul de TVA depus la ANAF. |
| **D406 (SAF-T)** | Fișierul standard de control fiscal: registrul jurnal și balanța, cu toate conturile, inclusiv 442830. |
| **ANAF** | Agenția Națională de Administrare Fiscală; publică lista contribuabililor în sistemul TVA la încasare. |
| **FR-16** | Cerința din catalogul suitei `l10n_ro_ent` pentru TVA la încasare. |

---

## 3. Bază legală

- **Codul fiscal art. 282 alin. (3)–(8)** — sistemul de TVA la încasare; exigibilitatea la data
  încasării, fiecare încasare incluzând proporțional și taxa aferentă. Plafonul de aplicare:
  5.000.000 lei în perioada 1 martie – 31 decembrie 2026 și 5.500.000 lei din 1 ianuarie 2027
  (OUG 8/2026).
- **Codul fiscal art. 297 alin. (2)–(3)** — deducerea amânată la plată, când furnizorul sau firma
  proprie aplică sistemul.
- **Codul fiscal art. 282 alin. (6)** — operațiunile excluse (regulile generale de exigibilitate).
- **Codul fiscal art. 319 alin. (20) lit. p)** — mențiunea „TVA la încasare" pe factură.
- **Normele metodologice (HG 1/2016), titlul VII, pct. 26** — momentul încasării (data din extras),
  compensarea și cesiunea de creanță, alegerea liniilor încasate la plăți parțiale.
- **OMFP 1802/2014** — funcțiunea contului 4428 „TVA neexigibilă" (bifuncțional).

---

## 4. Utilizatori și roluri

| Rol | Acțiune |
|-----|---------|
| Manager Contabilitate | Verifică și completează configurarea din Setări; decide contul tehnic pentru bază |
| Contabil | Pune poziția fiscală pe partenerii în sistem; emite facturi, înregistrează încasări și plăți |
| Consultant implementare | Verifică maparea taxelor și notele CABA la punerea în funcțiune |

Configurarea cere grupul **Contabilitate / Administrator** (`account.group_account_manager`).

---

## 5. Configurare inițială

### 5.1 Verificarea din Setări

Meniu: **Contabilitate → Configurare → Setări**, secțiunea **Taxe**.

Blocul nativ **Baza de numerar** conține jurnalul și contul tehnic. Imediat sub el, modulul
adaugă blocul **Configurare TVA la încasare (RO)**, vizibil doar pe companiile cu țara fiscală
România:

- verde — configurarea e completă;
- galben, cu lista problemelor — ce lipsește sau e greșit (vezi secțiunea 8);
- butonul **Completează configurarea** setează doar câmpurile goale.

Verificarea citește valorile **salvate** pe companie: după o modificare, salvați și reveniți.

![Setări → Taxe: Baza de numerar, contul tehnic 442830 și verificarea RO](screenshots/01_setari_caba.png)

Cu o greșeală de configurare, de exemplu contul tehnic pus pe 44281, verificarea o arată cu roșu:

![Verificarea semnalează contul tehnic pus pe contul de tranziție 44281](screenshots/02_setari_caba_eroare.png)

| Câmp (interfață) | Câmp tehnic | Valoare recomandată |
|---|---|---|
| Baza de numerar | `tax_exigibility` | bifat |
| Jurnalul bazei de numerar a taxei | `tax_cash_basis_journal_id` | jurnalul **CABA** „Taxe pe bază de numerar" |
| Cont tehnic pentru baza TVA la încasare | `account_cash_basis_base_account_id` | **442830 Bază TVA - cont tehnic (sold zero)** |
| Compania aplică TVA la încasare | `l10n_ro_caba_company` | bifat doar dacă firma e în sistem |

### 5.2 Contul tehnic pentru bază: de ce 442830 și nu 473

La fiecare încasare, nota CABA conține pe lângă TVA și **baza impozabilă**, de două ori, o dată pe
debit și o dată pe credit, cu aceeași sumă. Liniile există doar ca să ducă baza în rândurile de
bază din D300; soldul lor e mereu zero. Contul pe care se scriu e câmpul de mai sus. Dacă e gol,
Odoo le scrie pe contul de venit/cheltuială al facturii (707, 607, 371...), care capătă rulaje
debit = credit fără nicio legătură cu activitatea.

Opinia expertului contabil (Pacioli) a comparat cele două variante folosite până acum în casă:
**473** „Decontări din operații în curs de clarificare" și un analitic al lui 4428 (**442830**).
Niciuna nu se potrivește perfect cu funcțiunea contului, pentru că baza impozabilă nu e nici TVA,
nici o sumă de clarificat. Varianta care face mai puțin rău e **442830**:

| Criteriu | 473 | 442830 (analitic 4428) |
|---|---|---|
| Funcțiunea contului (OMFP 1802/2014) | 473 ține sume „în curs de clarificare", care cer cercetări suplimentare. Liniile de bază nu au nimic de clarificat: contul e folosit în afara funcțiunii. | 4428 ține TVA-ul neexigibil. Baza nu e TVA, dar ține de același regim fiscal. |
| La control | Rulaje mari pe 473 atrag cereri de justificare: 473 înseamnă „ceva neclarificat". | Rulajul unui analitic „bază TVA, cont tehnic" lângă 44281/44282 se explică singur. |
| Balanță și SAF-T (D406) | Liniile tehnice se amestecă cu sumele reale în curs de clarificare de pe 473. | Crește rulajul sinteticului 4428, dar TVA-ul real rămâne izolat pe 44281/44282, unde se face reconcilierea. |
| Alte module care folosesc același câmp | Aceeași problemă și pentru DVI și TVA nedeductibil. | Aceeași convenție ca OCA (`l10n_ro_nondeductible_vat`), deci o singură regulă în toate modulele. |

Conturile în afara bilanțului (clasa 8) nu sunt o opțiune: Odoo nu permite amestecarea lor cu
conturi bilanțiere în aceeași notă.

Ce **nu** trebuie pus acolo: **44281** sau **44282**. Acelea sunt conturile de tranziție ale
taxelor, cu TVA-ul real neexigibil; baza s-ar amesteca cu TVA-ul pe același cont. Verificarea din
Setări marchează acest caz cu roșu.

Modulul folosește 442830 dacă există deja (de exemplu creat după convenția OCA) și îl creează doar
dacă lipsește, ca **Datorii curente**, nereconciliabil. La implementare, verificați ca 442830 să
fie mapat pe contul standard 4428 în nomenclatorul SAF-T (D406).

### 5.3 Taxele și poziția fiscală

Meniu: **Contabilitate → Configurare → Taxe**. Planul RO aduce taxele la încasare:

| Taxă | Tip | Exigibilitatea taxei | Cont de tranziție a bazei de numerar |
|---|---|---|---|
| TVA la colectare - colectat 21% / 11% / ... | Vânzări | Pe baza plății | 44281 |
| TVA la colectare - 21% deductibil / 11% / ... | Achiziții | Pe baza plății | 44282 |

Exigibilitatea și contul de tranziție sunt în fila **Opțiuni Avansate** a taxei.

Meniu: **Contabilitate → Configurare → Poziții fiscale → Sistem de colectare TVA**. Poziția
înlocuiește pe factură taxele obișnuite cu cele la încasare (TVA colectat 21% → TVA la colectare
21% etc.). Nu are „Detectare automată": la firma în sistem o pune modulul; la firma normală se pune
pe furnizorii în sistem (pasul 2).

![Taxa la încasare 21%: Pe baza plății, cont de tranziție 44281](screenshots/03_taxa_tva_incasare.png)

Taxele pe care le înlocuiește poziția se văd din butonul **Taxe** al poziției fiscale, în coloana
**Înlocuiește**:

![Taxele poziției fiscale Sistem de colectare TVA, cu taxele înlocuite](screenshots/04_pozitie_fiscala.png)

### 5.4 Cele 8 cazuri: cine e la încasare

Contează doar regimul **emitentului** facturii și, la achiziții, și regimul **companiei proprii**
(art. 282, art. 297 alin. (2)–(3)). Regimul clientului nu schimbă nimic pentru vânzător.

| # | Compania proprie | Operațiune | Partener | Rezultat | TVA pe factură | La încasare / plată |
|---|---|---|---|---|---|---|
| 1 | normală | vânzare | client normal | TVA obișnuit | 4427 | — |
| 2 | normală | vânzare | client **în sistem** | **TVA obișnuit** | 4427 | — |
| 3 | normală | achiziție | furnizor normal | TVA obișnuit | 4426 | — |
| 4 | normală | achiziție | furnizor **în sistem** | la încasare | 44282 | 4426 = 44282 |
| 5 | **în sistem** | vânzare | client normal | la încasare | 44281 | 44281 = 4427 |
| 6 | **în sistem** | vânzare | client în sistem | la încasare | 44281 | 44281 = 4427 |
| 7 | **în sistem** | achiziție | furnizor normal | la încasare (alin. (3)) | 44282 | 4426 = 44282 |
| 8 | **în sistem** | achiziție | furnizor în sistem | la încasare | 44282 | 4426 = 44282 |

Cum decide modulul poziția fiscală pe factură:

- **Compania aplică TVA la încasare** bifat → poziția **Sistem de colectare TVA** pe toate
  facturile, comenzile de vânzare și de achiziție cu parteneri din România (cazurile 5–8);
- nebifat → poziția vine de pe partener: se pune pe furnizorii în sistem (cazul 4), iar comenzile și
  facturile de achiziție de la ei o preiau. Pe **facturile de vânzare** modulul o scoate, pentru că
  regimul clientului nu contează (cazul 2).

Excepții, pe regulile generale (detalii la secțiunea 7):

- **Firme din același grup** (persoane afiliate, art. 7 pct. 26 Cod fiscal; afilierea se apreciază
  la data facturii — Norme, pct. 26 alin. (14)). Între ele, vânzătorul facturează cu TVA obișnuit
  (art. 282 alin. (6) lit. d)). Modulul nu le recunoaște singur:
  - **firma în sistem vinde unei firme din grup:** pe **factura respectivă**, schimbați poziția în
    **Regimul național (TVA)** înainte de confirmare. Nu puneți poziția pe partener: achizițiile de la
    el trebuie să rămână cu deducerea la plată (art. 297 alin. (3) nu exceptează firmele din grup);
  - **firma normală cumpără de la un furnizor în sistem din grup:** nu puneți poziția la încasare pe
    el — factura lui e cu TVA obișnuit, deci deducerea e imediată (Norme, pct. 67 alin. (6)).
- **Operațiuni cu locul livrării în afara României** (art. 282 alin. (6) teza I): modulul le
  recunoaște după țara partenerului și nu pune poziția pentru partenerii din alte țări. **Limitare:**
  o vânzare taxabilă în România către un partener străin (ex. înregistrat în scopuri de TVA în
  România, livrare locală cu TVA 21%) ar trebui să fie la încasare; pe astfel de facturi schimbați
  poziția de mână.
- **Altă poziție fiscală pusă pe partener** (ex. taxare inversă): câștigă, modulul nu o schimbă.

Clienții persoane fizice sau fără CUI, cu țara România, sunt tot la încasare — legea nu îi exclude.
Partenerul fără țară e tratat tot ca intern; completați totuși țara, pentru celelalte poziții fiscale
automate (UE, export). La achizițiile firmei în sistem de la o persoană fizică sau de la un
neplătitor de TVA nu e nimic de amânat: poziția înlocuiește doar taxele interne taxabile, deci
factura fără TVA rămâne neschimbată.

**Atenție la cazul 2.** Poziția fiscală de pe partener se aplică pe **orice** document cu el, și la
vânzare, și la achiziție. La o companie normală, un furnizor în sistem care e și client ar primi
vânzări la încasare — greșit. Pe facturile de vânzare create direct modulul scoate poziția. **Limitare:**
comenzile de vânzare și comenzile din POS către acel partener o preiau de pe partener, iar factura
creată din comandă o păstrează; pe ele schimbați poziția în **Regimul național (TVA)** înainte de
confirmare. Indicatorul practic pentru orice furnizor e mențiunea „TVA la încasare" de pe factura
primită: un furnizor în sistem din același grup cu dvs. nu o pune.

---

## 6. Flux de utilizare

### Pasul 1 — Accesare și verificare

**Contabilitate → Configurare → Setări**, secțiunea **Taxe**. Dacă verificarea nu e verde, apăsați
**Completează configurarea**, apoi rezolvați manual ce a rămas în listă.

### Pasul 2 — Regimul companiei și al furnizorilor

- **Firma proprie e în sistem:** în **Setări → Contabilitate → Taxe** bifați **Compania aplică TVA
  la încasare** (captura de la 5.1). Nu mai e nimic de pus pe parteneri.
- **Firma proprie e normală:** pe fiecare furnizor în sistem, **Contabilitate → Furnizori →
  Furnizori**, fila **Vânzări & Achiziții**, grupul **Informație fiscală**, câmpul **Poziție
  fiscală** = **Sistem de colectare TVA**. Comenzile și facturile de achiziție de la el o preiau.

![Furnizorul cu poziția fiscală Sistem de colectare TVA](screenshots/05_furnizor_tva_incasare.png)

Regimul partenerilor se verifică în lista ANAF a contribuabililor în sistemul TVA la încasare. Cu
OCA `l10n_ro_vat_on_payment` instalat, lista se descarcă și se aplică automat, cu datele de intrare
și ieșire din sistem.

### Pasul 3 — Factura de vânzare

Cazurile 5–6 (firma proprie în sistem). Factura: 1.000 lei + TVA 21% = 1.210 lei; poziția
**Sistem de colectare TVA** se pune singură. Taxa de pe linie
devine **TVA la colectare - colectat 21%**. Pe factură trebuie să apară mențiunea „TVA la
încasare" (art. 319 alin. (20) lit. p)).

| Cont | Debit | Credit |
|---|---:|---:|
| 4111 Clienți | 1.210 | |
| 707 Venituri din vânzarea mărfurilor | | 1.000 |
| 44281 TVA neexigibilă colectată | | 210 |

În fila **Elemente jurnal**, TVA-ul apare pe 44281, nu pe 4427. Contul de venit depinde de produs
(în captură, 701 al produsului de test):

![Factura de vânzare: 4111 = 70x + 44281](screenshots/06_factura_vanzare.png)
### Pasul 4 — Încasare parțială

Încasare 605 lei (extras bancar sau **Înregistrare plată** pe factură, apoi reconciliere). La
reconciliere, Odoo creează în jurnalul **CABA** nota de exigibilitate, proporțional:
605 × 21/121 = 105 lei TVA, bază 500 lei.

| Notă | Cont | Debit | Credit |
|---|---|---:|---:|
| Încasare | 5121 / 4111 | 605 | 605 |
| CABA — TVA | 44281 / 4427 | 105 | 105 |
| CABA — bază (tehnic) | 442830 / 442830 | 500 | 500 |

La încasarea restului se repetă aceleași note; la final, 44281 are sold zero pentru factură.

Nota se deschide din butonul **Înregistrări pe bază de numerar** de pe factură:

![Nota CABA la încasare: 44281 → 4427 105 lei, baza 500 pe 442830](screenshots/07_nota_caba_vanzare.png)

### Pasul 5 — Achiziția

Cazurile 4, 7 și 8 (furnizorul sau firma proprie în sistem). Factură de 1.000 lei + 210 TVA; poziția
**Sistem de colectare TVA** vine de pe furnizor sau, la firma în sistem, se pune singură.

| Moment | Cont | Debit | Credit |
|---|---|---:|---:|
| Factura | 371 (sau 607 / 6xx) | 1.000 | |
| | 44282 TVA neexigibilă deductibilă | 210 | |
| | 401 Furnizori | | 1.210 |
| Plată 605 | 401 / 5121 | 605 | 605 |
| CABA — deducere | 4426 / 44282 | 105 | 105 |
| CABA — bază (tehnic) | 442830 / 442830 | 500 | 500 |

![Factura de achiziție: 6xx + 44282 = 401](screenshots/08_factura_achizitie.png)

![Nota CABA la plată: 4426 = 44282 105 lei, baza 500 pe 442830](screenshots/09_nota_caba_achizitie.png)

### Pasul 6 — Verificarea în D300

Baza și TVA-ul intră în decontul **perioadei încasării sau plății**, pe **rândurile generale** de
livrări / achiziții taxabile cu cota respectivă, proporțional cu suma încasată. Nu există rânduri
principale separate pentru TVA la încasare; decontul are doar câmpuri informative pentru TVA
neexigibilă. Din exemplu, în luna încasării și a plății: rândul 9 (livrări 21%) — bază 500, TVA 105;
rândul 24 (achiziții 21%) — bază 500, TVA 105.

Meniu: **Contabilitate → Raportare → Declarații fiscale**, raportul **VAT Raport D300 (RO)**, luna
încasării (în captură, cu liniile goale ascunse):

![Raportul D300 în luna încasării: rândurile 9 și 24, bază 500 și TVA 105](screenshots/10_d300_luna_incasarii.png)

---

## 7. Legături cu alte module / declarații

| Modul / declarație | Legătură |
|---|---|
| D300 (`l10n_ro_anaf_d300`) | Rândurile de bază și TVA se alimentează din grilele de pe nota CABA, în luna încasării. |
| `l10n_ro_vat_on_payment_lock` | Blochează desfacerea reconcilierii dacă nota CABA e într-o perioadă deja declarată. |
| OCA `l10n_ro_vat_on_payment` | Opțional: lista ANAF și poziția fiscală automată pe factură. |
| Vânzări / Achiziții (comenzi) | La firma în sistem, comenzile de vânzare și de achiziție primesc poziția la încasare, iar facturile create din ele o preiau. La firma normală, comenzile de achiziție preiau poziția furnizorului. |
| Comenzi de vânzare / POS, firmă normală | **Limitare:** către un furnizor în sistem care e și client, comanda preia poziția la încasare de pe partener, iar factura creată din ea o păstrează. Schimbați poziția în **Regimul național (TVA)** pe comandă sau pe factură. |
| OCA `l10n_ro_dvi`, `l10n_ro_nondeductible_vat` | Folosesc același cont tehnic pentru liniile lor de bază. TVA-ul nedeductibil nu trece prin 44282 — se amână doar partea deductibilă (Norme, pct. 67 alin. (8)). |
| SAF-T (D406) | 442830 apare în balanță și în registrul jurnal cu rulaje egale; trebuie mapat pe 4428. |
| Jurnale TVA (`l10n_ro_account_vat_journal`) | Raportează TVA-ul la încasare în luna încasării. |

**Operațiuni excluse la vânzare** (art. 282 alin. (6)): pe ele se aplică regulile generale chiar dacă
firma e în sistem, deci nu primesc taxa la încasare:

- taxarea inversă (art. 307 alin. (2)–(6) și art. 331);
- operațiunile scutite de TVA;
- regimurile speciale din art. 311–313 (agenții de turism, second-hand, artă, aur de investiții);
- livrările către firme din același grup (persoane afiliate) — poziția se schimbă de mână pe
  factură, vezi 5.4.

**Nu amână deducerea** (art. 297 alin. (3)): importul, achizițiile intracomunitare și taxarea
inversă — TVA-ul din DVI nu trece prin 44282. Nici TVA-ul nedeductibil: se amână doar partea
deductibilă (Norme, pct. 67 alin. (8)).

Poziția fiscală mapează doar taxele interne taxabile, deci aceste operațiuni rămân pe regulile
generale dacă au taxele lor proprii.

**Intrarea și ieșirea din sistem.** Ieșirea la cerere sau prin depășirea plafonului produce efecte de
la prima zi a perioadei fiscale următoare (art. 282 alin. (5)); la mijloc de perioadă se iese doar la
scoaterea din evidența TVA sau la intrarea într-un grup fiscal unic (Norme, pct. 26 alin. (17)).
Facturile emise cât s-a aplicat sistemul rămân la încasare oricând s-ar încasa (art. 282 alin. (3));
pentru facturile de avans emise înainte de ieșire, cu livrarea după ieșire, sistemul continuă doar
pentru suma facturată înainte (art. 282 alin. (7) lit. b)), iar încasările parțiale se atribuie
întâi părții facturate înainte de ieșire (Norme, pct. 26 alin. (15) lit. b)). Simetric, facturile
emise înainte de intrare nu intră în sistem (art. 282 alin. (7) lit. a)). La achiziții, TVA-ul de pe
facturile primite cât ați aplicat sistemul se deduce tot la plată.

**Bifa și poziția nu au dată:** schimbați **Compania aplică TVA la încasare** exact la data de efect,
după ce ați confirmat ciornele; comenzile și ciornele create înainte păstrează poziția veche —
verificați-le. La fel, scoateți poziția **Sistem de colectare TVA** de pe furnizor la data ieșirii
lui din registrul ANAF (automat cu OCA `l10n_ro_vat_on_payment`). Facturile confirmate nu se modifică, iar
soldul 4428 nu se reclasifică.

**Facturi neîncasate:** nu există un termen după care TVA-ul devine exigibil automat; soldul rămâne
pe 4428 până la încasare, compensare sau cesiune, ori până la o ajustare după art. 287.

---

## 8. Mesaje de eroare frecvente

Mesajele apar în blocul de verificare din Setări.

| Mesaj | Cauză | Remediere |
|---|---|---|
| Baza de numerar nu e activată | Bifa **Baza de numerar** e debifată | Bifați-o sau **Completează configurarea** |
| Nu e setat jurnalul bazei de numerar | Jurnalul CABA lipsește din setări | Alegeți jurnalul CABA sau **Completează configurarea** |
| Taxe la încasare fără cont de tranziție | O taxă „Pe baza plății" nu are cont 4428 | Completați contul în fila **Opțiuni Avansate** a taxei |
| Contul tehnic pentru bază este și cont de tranziție | Pe câmp e pus 44281 / 44282 | Puneți 442830 |
| Nu e setat contul tehnic pentru bază | Câmpul e gol, baza rulează pe 7xx / 6xx | **Completează configurarea** (setează 442830) |
| Contul tehnic pentru bază este un cont de venituri/cheltuieli | Pe câmp e un cont de clasa 6 / 7 | Puneți 442830 |
| Taxe interne nemapate de poziția fiscală | Taxe taxabile fără echivalent la încasare | Pe factură rămân exigibile la emitere. Planul RO nu mapează 9% art. 3 și TVA nedeductibil 50%; dacă le folosiți în sistem, creați taxa la încasare și legați-o de poziție |

---

## 9. Capturi de ecran

Generate reproductibil de `tests/test_screenshots.py` (companie RO, plan RO, date de test):

| # | Fișier | Ce arată |
|---|---|---|
| 1 | `01_setari_caba.png` | Setări → Taxe: Baza de numerar, jurnalul CABA, contul tehnic 442830, bifa „Compania aplică TVA la încasare" și verificarea RO |
| 2 | `02_setari_caba_eroare.png` | Verificarea cu contul tehnic pus greșit pe 44281 |
| 3 | `03_taxa_tva_incasare.png` | Taxa la încasare 21%, fila Opțiuni Avansate |
| 4 | `04_pozitie_fiscala.png` | Taxele poziției Sistem de colectare TVA și ce înlocuiesc |
| 5 | `05_furnizor_tva_incasare.png` | Furnizorul cu poziția fiscală Sistem de colectare TVA |
| 6 | `06_factura_vanzare.png` | Factura de vânzare, elemente jurnal (44281) |
| 7 | `07_nota_caba_vanzare.png` | Nota CABA după încasarea parțială |
| 8 | `08_factura_achizitie.png` | Factura de achiziție, elemente jurnal (44282) |
| 9 | `09_nota_caba_achizitie.png` | Nota CABA după plata parțială |
| 10 | `10_d300_luna_incasarii.png` | D300 în luna încasării: rândurile 9 și 24 |

Regenerare:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i l10n_ro_caba,l10n_ro_doc_screenshots,account_reports \
    --test-tags=/l10n_ro_caba:TestL10nRoCabaScreenshots --stop-after-init
```
