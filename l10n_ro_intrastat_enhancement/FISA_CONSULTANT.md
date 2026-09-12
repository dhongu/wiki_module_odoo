# Fișă Modul: Intrastat România — export XML INS, praguri și verificare erori

**Modul:** `l10n_ro_intrastat_enhancement`
**FR:** FR-47
**Utilizator principal:** Contabil / responsabil raportări statistice (Intrastat)
**Prioritate:** 🟡 Medie (obligatorie doar peste prag; lunară pentru declaranți)

> **INS = Institutul Național de Statistică** — autoritatea la care se depune declarația
> Intrastat, **nu** ANAF. Intrastat este o raportare *statistică*, cu portal propriu
> (https://intrastat.ro) și termen propriu, separată de declarațiile fiscale (D390, D300).
> Peste tot în modul și în această fișă, „INS" desemnează această autoritate: butonul
> **Verificare INS** verifică datele față de cerințele INS, **Export XML INS** produce
> fișierul în formatul cerut de INS, iar **pragurile INS** sunt cele publicate anual de INS.

---

## 1. Scop business

Modulul extinde declarația Intrastat din Odoo Enterprise cu tot ce trebuie pentru **depunerea
efectivă la Institutul Național de Statistică (INS)**: **export XML** în formatul oficial INS,
**monitorizarea pragurilor anuale** (cu avertizări automate la apropierea/depășirea pragului),
o **verificare a erorilor** care prinde câmpurile lipsă înainte de depunere și un mecanism de
**actualizare a codurilor CN** (Nomenclatura Combinată) publicate anual de INS.

Se instalează automat când sunt prezente raportul Intrastat de bază (`l10n_ro_intrastat`) și
gestionarea livrărilor (`stock_delivery`).

## 2. Bază legală și context

Declarația statistică Intrastat este obligatorie pentru operatorii care depășesc pragurile
anuale de expediere/sosire de bunuri în relația intra-UE, conform **Regulamentului (UE)
2019/2152** și normelor metodologice INS (Legea 422/2006 privind organizarea statisticii
Intrastat). Pragurile sunt stabilite **anual** de INS printr-o decizie proprie — modulul
livrează doar niște **valori implicite** (**1.000.000 RON expedieri / 900.000 RON sosiri**),
care trebuie confirmate/actualizate manual în Setări la fiecare an, pe baza deciziei INS
în vigoare (verificați anul curent pe https://intrastat.ro înainte de a vă baza pe ele).
Declarația se depune lunar, **până la data de 15 a lunii următoare lunii de referință**, pe
portalul INS (https://intrastat.ro).

> Intrastat este o raportare **statistică**, nu fiscală — modulul nu generează note contabile.

## 3. Utilizatori și roluri

Contabilul / responsabilul de raportări depune declarația lunară și urmărește pragurile.

Roluri recomandate pentru testare:
- Administrator funcțional: instalează modulul, configurează pragurile pe companie;
- Utilizator operațional (grup „Contabil" — `account.group_account_user`): rulează verificarea
  de erori, exportă XML, consultă verificarea de prag;
- Contabil/manager: confirmă obligația de declarare și volumul față de prag.

## 4. Conturi și date implicate

Modulul **nu atinge conturi contabile** — lucrează cu raportul Intrastat (date statistice din
facturile postate). Datele relevante pentru o linie corectă:
- pe **produs**: codul Intrastat **NC8** (Nomenclatura Combinată) și țara de origine;
- pe **partener**: codul TVA intra-UE (la expedieri) și țara;
- pe **mișcare/factură**: natura tranzacției, masa netă / unitățile suplimentare, modul de
  transport și regiunea (la declarația extinsă).

Date minime pentru demo: companie RO, parteneri din alte state UE, produse cu cod Intrastat,
facturi de vânzare/achiziție intra-UE postate în luna declarată.

## 5. Configurare inițială

1. Instalați modulul (auto-install când există `l10n_ro_intrastat` + `stock_delivery`).
2. Deschideți **Setări → Contabilitate**, blocul **Intrastat — Praguri INS România**:
   bifați **Declarat Intrastat obligatoriu** (dacă firma a depășit deja pragul), ajustați
   **Pragul expedieri** / **Pragul sosiri** (RON/an) și **Avertizare la % din prag** (implicit 80%).
3. Marcați produsele comercializate intra-UE cu **codul Intrastat (NC8)** pe fișa produsului.
4. Verificați versiunile nomenclatoarelor (CN, transport, termeni de livrare, țări) — se
   stochează în parametri de sistem și se pot actualiza anual fără modificări de cod.

![Blocul de setări Intrastat — Praguri INS România](screenshots/01_setari_praguri.png)

## 6. Flux de utilizare

### Pasul 1 — Statusul pragului, direct în raportul Intrastat

Accesați **Contabilitate → Raportare → Intrastat**. Dacă firma este românească, în **antetul
raportului** apare automat un **banner de alertă** — fără niciun click suplimentar — cu, pe
ambele direcții (expedieri și sosiri): volumul calculat (RON, pe anul perioadei deschise),
pragul INS configurat, procentul atins și starea — **sub prag** (verde) / **atenție**
(portocaliu) / **depășit** (roșu) / **declarat obligatoriu** (albastru). Volumul se calculează
din facturile și stornările postate către parteneri UE (exclus România) ale căror produse au
cod Intrastat, convertite în RON.

**Găsiți pe ecran**: banner-ul colorat, imediat sub filtrele raportului (fără să fie nevoie să
deschideți vreun wizard sau meniu separat).

**Verificați**: dacă o direcție arată **depășit** sau **atenție**, firma trebuie să declare
Intrastat pentru acea direcție; bifați „Declarat obligatoriu" în setări dacă nu e deja (secțiunea
5 de mai sus).

![Raportul Intrastat, cu banner-ul de status prag vizibil în antet](screenshots/02_raport_prag_banner.png)

> Acțiunea tehnică `action_l10n_ro_intrastat_check` (fostul wizard „Verificare Prag Intrastat")
> rămâne disponibilă ca acces secundar, fără meniu propriu — utilă pentru un recalcul punctual
> pe un an anume, în afara raportului.

### Pasul 2 — Raportul Intrastat și verificarea erorilor (înainte de export)

Deschideți **Contabilitate (sau Facturare, în funcție de ediție) → Raportare → Intrastat**
(raportul standard Enterprise), cu luna și filtrele de declarație (mod normal/extins,
direcție). Bara de instrumente a raportului (pentru companii RO) conține, pe lângă
**PDF**/**XLSX**: butoanele **XML** și **Verificare INS** adăugate de modul — acesta este
punctul din care se lansează verificarea erorilor și exportul XML pentru INS.

> Butonul se citește „Verificare [pentru depunerea la] **INS**" — *Institutul Național de
> Statistică*, autoritatea care colectează Intrastat. Verificarea este locală, în Odoo: nu
> trimite nimic la INS și nu necesită conexiune la portal.

**Verificarea erorilor INS** rulează exact aceeași interogare ca exportul și listează liniile
cu câmpuri obligatorii lipsă — **cod NC8**, valoare, masă netă/unități suplimentare, natura
tranzacției, **cod TVA partener** (la expedieri), **țară de origine** (la sosiri), mod de
transport/regiune (la declarația extinsă). Acestea sunt cauzele tipice de respingere la INS.

**Verificați**: lista de erori e goală (sau corectați produsele/partenerii semnalați și
reverificați) **înainte** de a genera fișierul.

![Raportul Intrastat, cu butoanele XML și Verificare INS](screenshots/03_raport_intrastat.png)

![Lista erorilor INS — câmpuri obligatorii lipsă](screenshots/04_erori_ins.png)

### Pasul 3 — Exportul XML pentru INS

După ce verificarea e curată, selectați perioada (**o singură lună calendaristică**) și o
**singură direcție** (sosiri SAU expedieri) și lansați exportul **XML**. Modulul generează
declarația în structura XML oficială INS — normalizează codul TVA al partenerului și CUI-ul
companiei în forma cerută de INS — și o descarcă, gata de încărcat pe portalul INS.

> Validări aplicate la export: o singură lună și o singură direcție per fișier; altfel exportul
> e refuzat cu mesaj explicit.

### Pasul 4 — Reconciliere cu D390 (opțional, dacă `l10n_ro_anaf_d390` e instalat)

Dacă suita include modulul D390, în bara de instrumente a raportului Intrastat apare și
butonul **Reconciliere D390**. Apăsarea lui compară, pentru aceeași perioadă, valoarea
bunurilor din Intrastat cu declarația recapitulativă D390: **sosiri Intrastat ↔ achiziții
intracomunitare de bunuri D390 (cod „A")** și **expedieri Intrastat ↔ livrări + operațiuni
triunghiulare D390 (coduri „L"+„T")**. Fereastra afișează cele două valori, diferența absolută
și procentuală, plus un status: **Concordant** / **Diferență minoră** (sub 5%) / **De
verificat** (peste 5%).

**Verificați**: un status „De verificat" merită investigat înainte de depunere — diferențe mici
sunt normale (Intrastat urmărește mișcarea fizică a bunurilor, D390 baza facturii), dar una mare
poate semnala o linie omisă sau clasificată greșit.

### Note de monografie și raportare

Modulul **nu generează note contabile** (niciun Dr/Cr) — Intrastat e raportare statistică.
Sursa de date este raportul Intrastat (facturi intra-UE postate). Remindere automate: o
acțiune programată lunară creează, per direcție, o singură **activitate de avertizare deschisă**
(nu se dublează cât timp cea anterioară nu a fost închisă manual — dedup-ul nu ține cont de an)
la atingerea procentului de alertă/depășirea pragului, plus o **activitate reminder de
depunere** înainte de data de 15 a lunii, recreată la fiecare rulare lunară a cron-ului.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `l10n_ro_intrastat` | raportul Intrastat RO de bază | dependență (manifest) |
| `stock_delivery` | datele de livrare (mod transport etc.) | dependență (manifest) |
| `account_intrastat` (Enterprise) | raportul `account.report` Intrastat + meniul | dependență tranzitivă |
| `l10n_ro_anaf_d390` (opțional) | reconciliere Intrastat ↔ D390 pe bunuri | buton condiționat, fără dependență hard |
| produse cu cod Intrastat (NC8) | sursa codurilor de marfă | date de configurare |

Ce este automat: calculul volumului față de prag, verificarea erorilor, generarea XML,
remindele lunare, actualizarea nomenclatorului CN din XML-ul INS.
Ce rămâne manual: marcarea produselor cu NC8, completarea datelor lipsă semnalate, încărcarea
efectivă a fișierului pe portalul INS, ajustarea pragurilor la valorile INS ale anului.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează (auto-install) fără erori; blocul de praguri apare în Setări → Contabilitate.
- [ ] La deschiderea raportului **Contabilitate → Raportare → Intrastat** (companie română),
      banner-ul de status prag apare automat în antet, fără click suplimentar, cu volum/prag/
      procent/stare pentru ambele direcții.
- [ ] Anul folosit de banner corespunde perioadei selectate în raport (nu anul calendaristic curent,
      dacă raportul e deschis pe alt an).
- [ ] Bifa „Declarat obligatoriu" comută starea pe **Declarat obligatoriu** (albastru) indiferent de volum.
- [ ] Acțiunea tehnică `action_l10n_ro_intrastat_check` (fostul wizard) rămâne funcțională ca
      acces secundar — fără meniu propriu, se deschide din **Setări → Tehnic → Acțiuni →
      Acțiuni fereastră** (necesită modul dezvoltator activat).
- [ ] În raportul Intrastat apar butoanele **XML** și **Verificare INS** (doar pentru companii
      RO), lângă PDF/XLSX — verificați că sunt vizibile direct în bară, nu doar în meniul-rotiță.
- [ ] Dacă `l10n_ro_anaf_d390` e instalat, apare și butonul **Reconciliere D390**.
- [ ] **Verificare INS** listează liniile cu câmpuri lipsă; o linie completă nu apare în listă.
- [ ] **XML** refuză perioada multi-lună și selecția ambelor direcții, cu mesaj clar.
- [ ] Exportul XML reușit produce un fișier în structura INS, cu CUI și cod TVA normalizate.
- [ ] Cron-ul de remindere există; nu creează o a doua activitate de avertizare per direcție
      cât timp una anterioară e încă deschisă (necitită/neînchisă).

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Wrong date range selected. The intrastat declaration export has to be done monthly." | Perioada selectată acoperă mai mult de o lună calendaristică | Selectați o singură lună înainte de export |
| „You cannot select both arrivals and dispatches." | Ambele direcții bifate la export | Exportați separat sosirile și expedierile |
| „Missing date options for Intrastat export." | Raportul nu are perioada setată | Alegeți perioada în filtrele raportului |
| Verificare INS: „Lipsește codul NC8 (cod marfă) — setați-l pe produs" | Produsul nu are cod Intrastat | Completați NC8 pe fișa produsului |
| Verificare INS: „Lipsește codul TVA al partenerului (obligatoriu la expedieri)" | Partener UE fără cod TVA | Completați codul TVA intra-UE pe partener |
| Verificare INS: „Lipsește țara de origine (obligatorie la sosiri)" | Produsul/linia fără țară de origine | Completați țara de origine |

## 10. Capturi de ecran

Capturile (`readme/screenshots/`) sunt **generate automat** din `tests/test_screenshots.py`
(mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în **limba română**,
pe planul de conturi RO; seedul postează facturi intra-UE și exersează verificarea de prag și
de erori — fără conexiune la INS:

1. `01_setari_praguri.png` — blocul de setări Intrastat (praguri, % avertizare, obligatoriu).
2. `02_raport_prag_banner.png` — raportul Intrastat cu banner-ul de status prag (volum/prag/procent/stare) vizibil în antet.
3. `03_raport_intrastat.png` — raportul Intrastat cu butoanele XML și Verificare INS.
4. `04_erori_ins.png` — lista erorilor INS (câmpuri obligatorii lipsă).

Regenerare:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i l10n_ro_intrastat_enhancement,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

Subliniați secvența corectă: **verifică pragul** (sunt obligat să declar?) → **verifică
erorile** (datele sunt complete?) → **exportă XML** (o lună, o direcție) → **încarcă pe
intrastat.ro**. Intrastat e raportare statistică, nu fiscală — nu există nota contabilă de
verificat, ci completitudinea datelor de pe produse și parteneri. Reamintiți că pragurile se
schimbă anual prin decizie INS și trebuie actualizate în setări.
