# Fișă Modul: Mijloace Fixe Complet

**Poziție plan:** B6.1
**Modul:** `l10n_ro_fixed_assets`
**FR:** FR-19
**Capitol manual:** Cap 7.1
**Utilizator principal:** Contabil mijloace fixe, Responsabil patrimoniu
**Prioritate:** 🟡 Medie

---

## 1. Scop business

Această fișă descrie utilizarea modulului `l10n_ro_fixed_assets` pentru scenariul **Mijloace Fixe Complet**.
Consultantul folosește documentul pentru reproducerea fluxului în baza demo și
pentru pregătirea capitolului Cap 7.1 din manualul utilizator.

## 2. Bază legală și context

OMFP 1802/2014; HG 2139/2004 (Catalogul privind clasificarea și duratele normale de funcționare a
mijloacelor fixe); Codul Fiscal art. 28 (amortizare fiscală)

## 3. Utilizatori și roluri

Contabil Active Fixe

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul și verifică meniurile
- Utilizator operațional: rulează fluxul zilnic sau lunar
- Contabil/manager: validează rezultatele contabile și rapoartele

## 4. Conturi și date implicate

21x (active), 281x (amortizare cumulată), 6811 (cheltuieli amortizare), 105 (rezerve din
reevaluare), 1175 (rezultat reportat — transfer rezervă la casare), 6813 (depreciere ce depășește
soldul 105), 6583 (valoarea neamortizată la casare / „Cont Pierderi"), 7583 (venit din vânzarea
activelor / „Cont Venituri"), 4111/461 (creanța clientului la vânzare, după contul configurat pe
partener), 4427 (TVA colectată la vânzare)

Date minime pentru demo:
- companie românească cu localizarea contabilă instalată
- perioadă contabilă deschisă
- jurnale și conturi configurate conform scenariului
- documente de test postate, acolo unde fluxul pornește din contabilitate, stocuri, HR sau vânzări

## 5. Configurare inițială

1. Instalați modulul `l10n_ro_fixed_assets` (necesită `account_asset`, `l10n_ro_saft`, `l10n_ro`).
2. Verificați jurnalul de tip **Active fixe** și conturile 21x/281x/6811/105/6813/1175/6583 pe planul
   de conturi RO.
3. **Setări → Contabilitate**, secțiunea Active: setați **6583** pe **„Cont Pierderi"**
   (`loss_account_id`) și **7583** pe **„Cont Venituri"** (`gain_account_id`) — fără ele, motorul
   nu are unde posta rezultatul net la casare/vânzare.
4. **Setări → Contabilitate**: activați **„Contabilitate Storno"** (`account_storno`) — fără el,
   nota de vânzare a unui mijloc fix produce un rulaj în oglindă (debit) pe contul de venit (7583),
   deformând cifra de afaceri din operațiuni de capital.
5. Verificați secvența **„Număr Inventar Mijloc Fix RO"** (`l10n_ro.asset_inventory_number`, format
   `MF/AAAA/NNNN`).
6. Pe activele de test, setați **Metodă = Linie dreaptă** și **Perioadă = 1 lună** — fix-ul „amortizare
   din luna următoare PIF" (secțiunea 12) se aplică doar când perioada este lunară.
7. Completați pe fiecare activ de test câmpurile **Nr. Inventar** și **Data PIF** (obligatorii pentru
   SAF-T D406).

## 6. Flux de utilizare

### Pasul 1 — Lista mijloacelor fixe

Accesați **Contabilitate → Active și pasive → Active**. Lista afișează mijloacele fixe cu coloanele RO:
valoare inițială, metodă, contul de activ (213), starea și **numărul de inventar** (`MF/AAAA/NNNN`).
Conturile de amortizare (281) și cheltuială (681) sunt disponibile ca **coloane opționale**
(selectorul din dreapta antetului listei).

![Lista mijloacelor fixe cu coloanele RO (nr. inventar, conturi, stare)](screenshots/01_lista_active.png)

### Pasul 2 — Formularul activului (tab „Active")

Deschideți un mijloc fix. Tab-ul **„Active"** arată valorile (valoare inițială, **metodă „Linie
dreaptă"**, durată), conturile contabile și jurnalul; în antet, numărul de inventar generat automat
și smart button-ul **„Rezervă 105"** (rezerva din reevaluare). Butonul **„Confirmă"** validează
activul și generează planul de amortizare.

![Formularul mijlocului fix — tab „Active" (valori, metodă, conturi)](screenshots/02_formular_active.png)

### Pasul 3 — Datele specifice RO (tab „Informații RO")

Tab-ul **„Informații RO"** grupează câmpurile cerute de localizare: **Data PIF** (punere în
funcțiune), **DNU** (durata normală din Catalogul HG 2139/2004), **Cod de clasificare**,
**Responsabil custodie**, **Locație**, metoda de **amortizare fiscală** (Cod Fiscal art. 28) și
lista **Reevaluări** (cu rezerva contului 105 vizibilă și în smart button-ul din antet). Secțiunea
**Casare** rămâne goală până la cedarea efectivă a activului — câmpurile ei devin vizibile abia în
starea „Cedat".

![Tab „Informații RO" — identificare/localizare, amortizare fiscală, casare, reevaluări](screenshots/03_informatii_ro.png)

### Pasul 4 — Registrul Imobilizărilor

Accesați **Contabilitate → Raportare → Statement Reports → Fixed Assets Register (RO)**. Raportul
este nativ `account.report` (Enterprise), nu mai e un wizard separat: filtrul **„As of Date"** din
antet stabilește data de referință (implicit, ziua curentă), iar situația se recalculează automat
pentru acea dată — inclusiv amortizarea cumulată, luată doar din notele postate până atunci.

Activele sunt grupate pe **contul de imobilizări**, cu subtotal pe cont și **total general** în
capul tabelului. Fiecare linie e un activ confirmat (activele în ciornă nu apar în registru); click
pe o linie deschide direct fișa activului respectiv (drill-down). Butoanele **PDF** / **XLSX** din
colțul stânga-sus exportă exact ce se vede pe ecran.

![Registrul Imobilizărilor — grupare pe cont, subtotaluri, total general, filtrul „As of Date"](screenshots/04_registrul_imobilizarilor.png)

### Note de monografie și raportare

- **Amortizare lunară:** `Dr 6811 (cheltuieli amortizare) = Cr 281x (amortizare cumulată)`.
- **Reevaluare (creștere):** `Dr 21x (activ) = Cr 105 (rezerve din reevaluare)`.
- **Depreciere peste soldul 105:** `Dr 6813 (cheltuieli deprecieri) = Cr 21x (activ)`, pentru partea
  care depășește rezerva disponibilă din 105.
- **Casare (fără vânzare — activ complet sau parțial amortizat, fără încasare):** scoaterea din
  evidență `Dr 281x (amortizare cumulată) + Dr 6583 (valoare neamortizată) = Cr 21x (activ, valoare
  brută)`, cu **Decizie de casare** (raport PDF) ca document justificativ. Aici toată valoarea
  neamortizată ajunge direct în 6583 (`loss_account_id`).
- **Vânzare mijloc fix:** factura de vânzare generează separat `Dr 461/4111 (creanța clientului,
  după contul configurat pe partener) = Cr 7583 (venit din vânzare active) + Cr 4427 (TVA
  colectată)`. Nota de cedare a activului reia linia de venit din factură și adaugă `Dr 281x
  (amortizare cumulată) = Cr 21x (activ, valoare brută)`; **diferența** dintre valoarea neamortizată
  și prețul de vânzare (câștig sau pierdere) se închide în contul configurat pe companie — **7583**
  („Cont Venituri", `gain_account_id`) dacă vânzarea aduce câștig, **6583** („Cont Pierderi",
  `loss_account_id`) dacă aduce pierdere. Fără **Contabilitate Storno** activată, această notă
  produce un rulaj suplimentar (debit) pe 7583, pe lângă cel din factură.
- **La casare/cedare, dacă activul are rezervă de reevaluare (105) nesoldată:** transfer automat
  `Dr 105 (rezerve din reevaluare) = Cr 1175 (rezultat reportat)` (OMFP 1802/2014 pct. 103).
- **Amortizare fiscală vs. contabilă** (Cod Fiscal art. 28): se urmărește separat de cea contabilă,
  pentru calculul impozitului pe profit. Baza de calcul este **valoarea fiscală de intrare**, nu
  valoarea reevaluată — un surplus din reevaluare nu se amortizează fiscal.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux |
|---|---|
| `account_asset` | motorul de active și amortizare |
| `l10n_ro_inventory_register` | registrul anual include imobilizările |
| `l10n_ro_financial_statements` | raportare bilanț și anexe |
| SAF-T | câmpuri necesare pentru active |

Ce este automat: completarea câmpurilor RO și urmărirea amortizării.
Ce rămâne manual: validarea numărului de inventar, codului nomenclator și DNU.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori pe baza demo.
- [ ] Meniurile și acțiunile sunt vizibile pentru rolul de utilizator potrivit.
- [ ] Fluxul poate fi reprodus de la cap la coadă cu date fictive românești.
- [ ] Rezultatul contabil sau operațional corespunde descrierii din plan.
- [ ] Mesajele de eroare sunt clare pentru un utilizator non-tehnic.
- [ ] Exporturile sau rapoartele se descarcă și conțin datele testate.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Commissioning date (PIF) cannot be before the acquisition date." | Data PIF a fost setată înaintea datei de achiziție a activului. | Corectați data PIF — trebuie să fie egală sau ulterioară achiziției. |
| „The journal entry … is linked to asset … but has no depreciation beginning date. The 'Asset' field is reserved for entries generated automatically…" *(mesaj momentan netradus în ro.po)* | O notă contabilă (ex. de reevaluare) a fost legată manual la câmpul tehnic „Asset", fără ca acesta să provină din motorul de amortizare. | Nu legați manual câmpul „Asset" pe notele contabile — el este completat automat de planul de amortizare/reevaluare. |
| „Account 6813 not found. Please fill in the 'Account 6813' field on the revaluation." | Deprecierea depășește soldul disponibil în 105, iar contul 6813 nu e configurat pe planul de conturi sau pe reevaluare. | Completați câmpul „Cont 6813" pe reevaluare sau adăugați contul 6813 pe planul de conturi RO. |
| „The revaluation has already been confirmed." / „…has a posted accounting entry. Please reset the journal entry first." | Se încearcă re-confirmarea unei reevaluări deja postate. | Resetați mai întâi nota contabilă asociată (draft), apoi reluați reevaluarea. |
| „Missing inventory number on fixed assets" / „Missing commissioning date on fixed assets" (avertisment SAF-T) | Activul nu are completat Nr. Inventar sau Data PIF, câmpuri obligatorii pentru declarația SAF-T D406. | Completați câmpurile lipsă direct din acțiunea „Fill in…" oferită de avertisment. |

## 10. Capturi de ecran

Capturile din `readme/screenshots/` se obțin din `tests/test_screenshots.py` (mixinul `ScreenshotCase`
din `l10n_ro_doc_screenshots`, HttpCase + Playwright), pe companie RO, în lei, cu plan de conturi RO.

1. `01_lista_active.png` — lista mijloacelor fixe cu coloanele RO (nr. inventar, conturi, stare).
2. `02_formular_active.png` — formularul, tab „Active": valori, metodă „Linie dreaptă", durată,
   conturi (213/281/681), jurnal, nr. inventar și smart button „Rezervă 105".
3. `03_informatii_ro.png` — tab „Informații RO": Data PIF, locație, DNU (HG 2139/2004), responsabil
   custodie, amortizare fiscală (Cod Fiscal art. 28), casare, reevaluări (rezerva 105).
4. `04_registrul_imobilizarilor.png` — Registrul Imobilizărilor (`account.report`): filtrul
   „As of Date", grupare pe cont cu subtotaluri, total general, 3 active confirmate.

Regenerare:
```
./odoo/odoo-bin -c odoo.conf -d <db> -i l10n_ro_fixed_assets,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init --http-port=8987 --gevent-port=8988
```

## 11. Observații pentru manual

În manualul final, păstrați explicația orientată pe activitatea utilizatorului:
ce problemă rezolvă modulul, când se rulează, ce date trebuie pregătite și cum se verifică rezultatul.

> **Notă terminologică (nu ține de acest modul):** traducerea RO livrată de Odoo Enterprise pentru
> `account_asset` folosește „Devalorizare" în loc de „Amortizare" (ex. tabul „Panou Devalorizare",
> grupul „Metoda de Devalorizare"). Este o traducere din pachetul Enterprise, nu din
> `l10n_ro_fixed_assets` — în manual, înlocuiți mental „devalorizare" cu „amortizare" la explicarea
> capturilor.

## 12. Corecții relevante pentru consultant

Fixuri livrate pe acest modul, relevante pentru discuția cu clientul (ce s-a schimbat, de ce, de la ce versiune):

| Versiune | Ce era greșit (simptom pentru client) | Ce s-a corectat |
|---|---|---|
| **19.0.1.1.0** (versiune inițială) | Pe planul de conturi RO, contul de amortizare cumulată 281x este clasificat drept cont de cheltuială — fără o corecție explicită, planul de amortizare nu se genera deloc (linia Dr 6811 și cea Cr 281x se anulau reciproc). | Latura de amortizare cumulată este exclusă corect din calculul liniei de cheltuială, astfel încât planul de amortizare se generează cu valorile corecte (`Dr 6811 = Cr 281x`). |
| **19.0.1.2.0** (2026-09-14) | Amortizarea contabilă/fiscală începea chiar din luna punerii în funcțiune (PIF), proporțional cu zilele rămase din acea lună — nu din luna următoare, cum cere legea. | `prorata_date` pornește acum din prima zi a lunii **următoare** PIF (art. 28 alin. (12) lit. a) Legea 227/2015; OMFP 1802/2014 pct. 238). Se aplică companiilor RO cu amortizare lunară. |
| **19.0.1.2.0** (2026-09-14) | La vânzarea/casarea unui mijloc fix parțial amortizat în cursul lunii, programul amortiza proporțional cu zilele scurse până la data vânzării — deși amortizarea e strict lunară, iar luna vânzării nu ar trebui amortizată deloc. | Ultima lună amortizată la casare este acum luna anterioară vânzării, indiferent de ziua exactă din lună. Monografia de casare/vânzare (secțiunea 6) era deja corectă structural — discrepanța era doar efectul sumei greșite de amortizare. |
| **19.0.1.2.1** (2026-09-14) | Amortizarea fiscală afișată pe activ (câmpurile „Amortizare fiscală cumulată" / „an curent") putea arăta cumulatul **mai mic** decât amortizarea anului curent pentru un activ pus în funcțiune în anul curent — incoerență imposibilă contabil, cauzată de o formulă care numără luna PIF diferit în cele două cifre. | Ambele cifre folosesc acum aceeași convenție „luna următoare PIF", simetric cu fix-ul din 19.0.1.2.0; pentru primul an de amortizare, cumulatul și amortizarea anului curent coincid. |
| **19.0.1.2.2** (2026-09-14) | Amortizarea fiscală se calcula pe **valoarea curentă** a activului (`original_value`), care crește la o reevaluare — un surplus din reevaluare (nedeductibil fiscal, Cod Fiscal art. 28) ajungea astfel inclus greșit în baza de amortizare fiscală, umflând cifra afișată. | Baza de calcul este acum câmpul nou **„Fiscal Original Value"**, înghețat la valoarea de intrare din momentul creării activului — neafectat de reevaluări ulterioare. |
| **19.0.1.2.0** (2026-09-14) | Legarea manuală a unei note contabile (ex. o notă de reevaluare) la câmpul tehnic „Asset" al unei note contabile, fără completarea datei de început a amortizării, bloca ulterior orice calcul de valoare reziduală a activului, inclusiv din wizard-ul „Modifică". Incident reprodus pe o instanță client. | Legarea manuală incompletă este acum respinsă explicit la salvare, cu un mesaj clar (deocamdată doar în engleză) — câmpul „Asset" rămâne rezervat notelor generate automat de motorul de amortizare. |
| **19.0.1.1.1** (2026-07-17) | Butonul/acțiunea „Reevaluează Mijlocul Fix" din lista de active (meniu contextual) arunca o eroare la orice utilizare, blocând reevaluarea din acel punct de intrare. | Acțiunea apelează corect wizard-ul de reevaluare; funcționează identic cu butonul „Reevaluare" din formularul activului. |
| **19.0.1.3.0** (2026-09-15) | Registrul Imobilizărilor se genera printr-un wizard separat (dată + companie), care producea un PDF static; exportul PDF putea eșua cu o eroare de server (`IndexError`, template incomplet — corectat separat, chiar înainte de această migrare). | Raportul a fost migrat la framework-ul nativ `account.report`: se accesează direct din **Contabilitate → Raportare → Statement Reports → Fixed Assets Register (RO)**, cu filtru „As of Date", grupare pe cont cu subtotaluri, drill-down pe fiecare activ și export PDF/XLSX din bara de instrumente a raportului — fără wizard intermediar. |

> Notă: fix-urile de amortizare (din luna următoare PIF, fără prorata la vânzare) și blocarea legării
> manuale sunt acoperite direct de teste automate (`tests/test_fixed_assets_ro.py`), reproduse cu date
> fictive RO. Fix-ul acțiunii „Reevaluează" este verificat doar indirect (testul acoperă metoda
> apelată, nu punctul exact de eroare din acțiunea de server). Istoricul complet, în engleză și cu
> detalii tehnice, e în `readme/HISTORY.md`.
