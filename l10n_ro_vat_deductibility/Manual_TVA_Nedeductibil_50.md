# TVA deductibilă 50% (art. 298 Cod fiscal)

Pentru achizițiile cu deducere limitată la 50% (de exemplu combustibil, reparații sau leasing pentru
autoturisme care nu sunt folosite exclusiv în scop economic) folosiți taxa standard **21% ND 50%**
(respectiv **11% ND 50%**) din planul de conturi românesc. Nu este nevoie de taxe suplimentare.

Limitarea privește vehiculele rutiere motorizate de cel mult 3.500 kg și cel mult 9 locuri
(art. 298 alin. (1)). Nu se aplică vehiculelor folosite exclusiv în scop economic, justificat cu
foaia de parcurs (HG 1/2016, normele la art. 298), și nici celor exceptate de art. 298 alin. (2)
(de exemplu intervenție, pază, curierat, taxi, închiriere, agenți de vânzări sau de recrutare).
Pentru acestea se folosește taxa integral deductibilă.

## Taxa standard „21% ND 50%”

`Contabilitate > Configurare > Taxe`, taxa **21% ND 50%** (achiziții, 21%, procent din preț):

| Linie de repartizare | % | Cont | Grilă |
|---|---|---|---|
| Bază | 100 | — | 24 - TAX BASE |
| Taxă | 50 | 4426 | 24 - VAT |
| Taxă | 50 | 6352 | — |

**SAF-T (D406):** cu `l10n_ro_saft_export_fix` instalat, la export partea dedusă (4426) primește
codul 341104, iar partea nededusă (6352 sau contul liniei) codul 391104, conform notei „Situația 1”
din nomenclatorul ANAF (factură înregistrată direct cu deducere de 50%). Detalii: fișa
`l10n_ro_saft_export_fix/readme/FISA_CONSULTANT.md`.

`6352` este un analitic al contului 635 din planul de conturi românesc
(„Cheltuieli cu alte impozite, taxe și vărsăminte asimilate nedeductibile”).

### Nota contabilă

Factură de furnizor: 2 buc. × 250 lei = 500 lei + TVA 21% = 105 lei.

| Debit | Credit | Sumă |
|---|---|---|
| 6xx (contul liniei) | 401 | 500,00 |
| 4426 | 401 | 52,50 |
| 6352 | 401 | 52,50 |

Pe 4426 se înregistrează direct partea dedusă; nu există mișcare creditoare pe 4426.

### Partea nedeductibilă pe contul de cheltuială al liniei

Dacă vreți ca TVA-ul nededus să intre pe același cont cu cheltuiala (de exemplu 6022 pentru
combustibil), ștergeți contul **6352** de pe a doua linie de repartizare a taxei. Fără cont, Odoo
folosește contul liniei de factură:

| Debit | Credit | Sumă |
|---|---|---|
| 6022 | 401 | 500,00 |
| 4426 | 401 | 52,50 |
| 6022 | 401 | 52,50 |

Soldurile conturilor sunt aceleași ca în varianta cu înregistrare brută
(4426 = 401 105,00 urmat de 6022 = 4426 52,50); diferă rulajul contului 4426 și, în SAF-T,
codurile de taxă. Varianta brută („Situația 2” din nomenclator: 301104 pe factură și 391104 pe nota
de corecție 6xx = 4426) nu este tratată automat la export; codurile se verifică manual.

### Achiziția autoturismului

La cumpărarea autoturismului (imobilizare), TVA-ul nededus face parte din costul de achiziție
(OMFP 1802/2014, pct. 8, definiția 6 a costului de achiziție): partea nedeductibilă se înregistrează pe contul de imobilizare (213x), nu
pe 6352. Folosiți varianta cu partea nedeductibilă pe contul liniei.

## Decontul de TVA (D300)

Conform instrucțiunilor de completare a D300, achiziția apare cu TVA-ul brut pe rândurile de
achiziții și doar cu TVA-ul dedus pe rândul 31. Pentru exemplul de mai sus:

| Rând | Bază | TVA |
|---|---|---|
| rd. 24 | 500 | 105 |
| rd. 30 | 500 | 105 |
| rd. 31 | — | 53 |

Sumele din D300 sunt în lei întregi: 52,50 se rotunjește la 53, iar partea nededusă este diferența.

## Impozitul pe profit

Cheltuielile cu vehiculele care intră sub limitarea de la art. 298 sunt deductibile la impozitul pe
profit în proporție de 50% (art. 25 alin. (3) lit. l) Cod fiscal), inclusiv partea nedeductibilă din
TVA (HG 1/2016, normele la titlul II, pct. 16). În exemplu: (500 + 52,50) × 50% = 276,25 lei
nedeductibili la profit. Denumirea contului 6352 („… nedeductibile”) nu înseamnă că suma este
integral nedeductibilă la profit.

## Alternativă: „Deductibilitate” 50% pe linia facturii

Câmpul **Deductibilitate** 50% de pe linie, pe o taxă de 21% integral deductibilă, duce la aceeași
notă ca varianta cu partea nedeductibilă pe contul liniei: baza și TVA-ul nededus pe contul liniei,
50% din TVA pe 4426. D300 iese la fel. Diferența este codul SAF-T: taxa folosită rămâne cea integral
deductibilă (301104), iar separarea 341104 / 391104 nu se aplică, deci pentru art. 298 este
preferată taxa dedicată „21% ND 50%”.

## Ce nu se recomandă

- **Grupuri de taxe cu o ajustare de tip „Fixă”**. O taxă fixă se aplică pe unitate, indiferent de
  preț: o ajustare de 10,50 lei este corectă doar pentru o linie de 1 × 100 lei. Grilele D300 și
  codul SAF-T trebuie configurate pe taxele din grup; fără ele achiziția nu apare în decont.
