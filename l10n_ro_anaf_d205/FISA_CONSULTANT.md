# Fișă Modul: Declarația D205 — Impozit reținut la sursă, beneficiari persoane fizice

**Modul:** `l10n_ro_anaf_d205`
**FR:** FR-26
**Utilizator principal:** Contabil declarații, Contabil șef
**Prioritate:** 🟡 Medie (anual; obligatorie pentru orice societate care plătește dividende asociaților persoane fizice)

---

## 1. Scop business

Declarația **205** este informativă: repartizează pe **beneficiari persoane fizice** impozitul
**reținut la sursă** în cursul anului — cel mai des pe **dividendele plătite asociaților**, dar și pe
dobânzi, premii, chirii sau venituri din activități independente cu reținere. Modulul are **trei
straturi care lucrează împreună**, consecvent cu celelalte declarații ANAF:

1. un **pas în „Declarații fiscale"** (framework-ul `account.return`) care ghidează operatorul prin pașii
   de generare, cu **termen-limită** și **checklist**;
2. un **raport de previzualizare** (în stil contabil Enterprise) peste conturile **446x**, cu defalcare
   **partener → document** și buton **„Generează ciorna D205"**;
3. **declarația persistentă** (pe beneficiari), care aplică regulile validatorului ANAF și exportă
   fișierul **XML** validat cu schema oficială.

## 2. Bază legală și context

- **Art. 132 alin. (2) Cod fiscal** (Legea 227/2015, Titlul IV) — plătitorii de venituri cu regim de
  reținere la sursă depun, pe fiecare beneficiar, declarația privind impozitul calculat și reținut, până
  în **ultima zi a lunii februarie a anului următor**. Veniturile declarate în D112 (salarii, pensii,
  drepturi de proprietate intelectuală, arendă) nu intră în D205.
- **Art. 97 Cod fiscal** — impozitul pe veniturile din investiții. Cota pe dividende se stabilește
  după data **distribuirii** (aprobarea AGA), nu a plății: 5% pentru dividendele distribuite în 2016–2022,
  8% pentru cele distribuite în 2023–2024 (OG 16/2022), 10% pentru cele distribuite în 2025 (inclusiv dividendele
  interimare, fără recalculare la regularizarea din 2026) și 16% pentru cele distribuite din
  1.01.2026 (Legea 141/2025). Impozitul reținut se declară și se plătește lunar prin D100; D205 îl repartizează
  anual pe beneficiari.
- **OPANAF nr. 102/2025** — modelul și structura formularului; XML-ul respectă schema
  **`d205_2025_v3.xsd`** și structura ANAF modificată la 12.02.2026.

> **Rezidenți și nerezidenți.** D205 este în principal declarația beneficiarilor **rezidenți**.
> Structura admite nerezidenți (*Rezident/Nerezident* = 2) numai la codurile 04, 16, 18, 25–30; la
> **08 dividende, 09 dobânzi, 11 lichidare, 12 premii** validatorul cere rezident (regula R32).
> Veniturile nerezidenților, persoane fizice sau juridice, se declară în general în **D207**
> (art. 231 Cod fiscal, modulul `l10n_ro_anaf_d207`).

## 3. Utilizatori și roluri

Contabil declarații / Contabil șef.

Rol recomandat pentru testare: utilizator cu drepturi de contabilitate. Punctele de intrare:
- **Contabilitate → Contabilitate → Închidere → Declarații fiscale** (cockpit-ul `account.return`);
- **Contabilitate → Raportare → Declarații ANAF → Declarație 205** (lista declarațiilor persistente).

## 4. Conturi și date implicate

- **446x** „Alte impozite, taxe și vărsăminte asimilate" — sursa raportului de previzualizare și a
  importului: impozitul reținut, adică **rulajul creditor** 446x pe partener (nu soldul, care după
  plata la buget e de regulă zero), pentru **persoane fizice rezidente**
  (`is_company = False`, fără țară sau cu țara România, fără bifa de nerezident **Impozit la sursă
  (WHT)** din `l10n_ro_partner_screening`);
- per beneficiar: **denumire**, **CNP/NIF din România** (`cifR`), **rezidență**, **tip venit** (codurile
  oficiale 04, 08, 09, 11, 12, 16, 18, 25–30), **regim fiscal** (0 / 2 impozit final / 3 neimpozabil
  prin convenție), **bază** și **impozit**; la nerezidenți, **statul de rezidență** și **CIF-ul din
  străinătate**;
- câmpuri pe cod: **dividende distribuite / plătite** (08), **câștig / pierdere** (25, în locul bazei
  și impozitului), **venit în natură / garanția chiriei** (29).

**Date demo incluse:** la instalarea cu date demo, modulul creează doi beneficiari PF rezidenți
(„Ion Popescu (demo D205)", „Maria Ionescu (demo D205)", cu CNP) și **note contabile de reținere a
impozitului pe dividende** (`457 = 446`, cu beneficiarul ca partener) în anul anterior, astfel încât raportul de previzualizare și generarea ciornei sunt imediat funcționale.

## 5. Configurare inițială

1. Instalați modulul `l10n_ro_anaf_d205` (dependențe: `account`, `l10n_ro`, `l10n_ro_anaf_base`,
   `l10n_ro_partner_screening`, `l10n_ro_reports`). Necesită **Odoo Enterprise** (rapoarte contabile +
   `account.return`).
2. Completați **CNP-ul** asociaților și al celorlalți beneficiari persoane fizice în câmpul de cod
   fiscal al partenerului; importul îl preia în `cifR`.
3. Lăsați bifa **Impozit la sursă (WHT)** doar pe partenerii **nerezidenți** (se sugerează automat
   pentru o țară diferită de România) — ei se declară în D207 și nu sunt preluați în D205.
4. Asigurați-vă că impozitul reținut este înregistrat pe conturile **446x**, cu beneficiarul ca
   partener pe linie.
5. Pentru export, completați la firmă **CUI-ul** și **adresa fiscală** (stradă, localitate, cod poștal,
   țară), iar în **Contabilitate → Configurare → Setări**, secțiunea **Declarații ANAF România**,
   **persoana de contact pentru declarații** și **funcția** ei. Fără ele, ambele exporturi (XML și
   formular PDF) se opresc cu un mesaj explicit.

## 6. Flux de utilizare

### Pasul 1 — Pasul D205 din „Declarații fiscale" (termen + checklist)

**Contabilitate → Contabilitate → Închidere → Declarații fiscale**. Pentru anul fiscal expirat se generează
(automat prin cron sau manual cu **Nou**) o intrare **D205** cu **termen 28/29 februarie** și un set de
pași de bifat:

- **Generează ciorna D205 din 446x** — deschide raportul de previzualizare (Pasul 2);
- **Beneficiari fără CNP/NIF din România (cifR)** — semnalează liniile fără CNP/NIF;
- **Atașează D205 (XML semnat / recipisă ANAF)** — încărcarea dovezii de depunere.

![Pasul D205 în cockpitul Declarații fiscale, cu termen și checklist](screenshots/01_return_checklist.png)

### Pasul 2 — Raportul de previzualizare 446x și generarea ciornei

Din pasul de mai sus (sau direct), se deschide **raportul de previzualizare D205**: impozitul reținut pe
**446x** pentru PF rezidente, grupat **pe partener**, cu **drill-down în documente** (notele contabile).
După verificarea sumelor, apăsați **„Generează ciorna D205"** din antetul raportului — se creează (sau se
reactualizează) **ciorna anului fiscal** și se deschide formularul ei.

> **Atenție:** pe o ciornă existentă, generarea repetată **șterge liniile** și le reface din 446x,
> inclusiv tipul de venit, baza și câmpurile completate manual. Același efect îl are butonul
> **„Importă din contabilitate (446x)"** din formularul declarației (cere confirmare).

![Raport previzualizare 446x cu defalcare partener → document](screenshots/02_raport_preview_446x.png)

### Pasul 3 — Completarea beneficiarilor

În formularul declarației, verificați pentru fiecare beneficiar **CNP/NIF (cifR)**, **tipul de venit**,
**baza impozabilă** și câmpurile specifice codului. Totalurile (bază, impozit) se calculează automat;
**regimul fiscal** se propune după cod (2 — impozit final; 0 la codul 25; la 26 și 27 se poate alege 3).
**Anul fiscal** apare ca număr simplu (de exemplu „2025”, fără separator de mii), în formular și în
lista declarațiilor.

> La generare, modulul preia **impozitul reținut** (rulajul creditor 446x) pe beneficiar, cu
> **Rezidență = 1**, **baza impozabilă = 0** și **tip venit = „16 — Alte surse"**. Schimbați tipul pe
> natura reală (pentru asociați, **08 — Dividende**, cu dividendele distribuite și plătite) și
> completați baza.
>
> La codul **29** (cedarea folosinței bunurilor), baza de calcul este **venitul net**: venitul brut
> minus cota forfetară de 20% (art. 84^1 Cod fiscal); de exemplu, chirie brută 24.000 lei → bază
> 19.200 lei, impozit 10% = 1.920 lei.
>
> Un beneficiar **nerezident** se adaugă manual, cu **Rezidență = 2**, **statul de rezidență** și,
> opțional, **CIF-ul din străinătate** — numai la codurile admise de structură.

![Declarația D205 — beneficiari PF și totaluri](screenshots/03_declaratie_d205.png)

### Pasul 4 — Confirmarea

Apăsați **„Confirmă"**. Modulul aplică regulile validatorului ANAF și afișează toate problemele odată:
CNP/NIF lipsă, nerezident la un cod rezervat rezidenților, nerezident fără stat de rezidență, regim
fiscal nepermis pentru cod, același CNP/NIF de două ori la același cod de venit. Declarația trece în
starea **Confirmată** (câmpurile devin readonly); se poate reveni la ciornă cu „Resetează la ciornă".
Exporturile de la pașii 5 și 6 merg și din ciornă, ca verificare: aceleași reguli rulează la export.

![Declarația D205 confirmată](screenshots/04_declaratie_confirmata.png)

### Pasul 5 — Exportul XML pentru ANAF

Apăsați **„Export XML ANAF"** (din formular) sau butonul de export din raport. Modulul grupează
beneficiarii pe **tip de venit** (`sect_II`), calculează suma de control `totalPlata_A` după formula
ANAF (numărul de beneficiari plus toate totalurile), validează structura cu **XSD-ul ANAF** și descarcă
fișierul (nume standardizat `D205_<CUI>_<an>12.xml`). Fișierul trece validarea **DUKIntegrator**
(verificat pe dividende, dobânzi, chirii, aur de investiții și un nerezident la codul 16).

Sumele se rotunjesc la leu pe beneficiar, de la 50 de bani în sus (1.234,50 lei devine 1.235), iar
totalurile pe tip de venit se fac din valorile rotunjite. Extras simplificat (antetul fără adresă și
date de contact, rândul de dividende din secțiunea II și cei doi asociați; `…` marchează rândurile
omise, iar `totalPlata_A` cuprinde și rândurile omise):

```xml
<declaratie205 xmlns="mfp:anaf:dgti:d205:declaratie:v3" luna="12" an="2025" d_rec="0" d_succ="0"
    cui="20603502" den="Exemplu Consult SRL" nume_declar="Marinescu" prenume_declar="Elena"
    functie_declar="Administrator" totalPlata_A="166336">
  <sect_II tip_venit="08" nrben="2" Tcastig="0" Tpierd="0" Tbaza="100000" Timp="10000" T_VB="0" T_GAR="0"/>
  …
  <benef id_inreg="1" tip_venit1="08" den1="Ionescu Maria" cifR="2850719123460" tip_plata="2" Rezid="1"
      baza1="40000" imp1="4000" divid_D="40000" divid_P="30000"/>
  <benef id_inreg="2" tip_venit1="08" den1="Popescu Ion" cifR="1780312123455" tip_plata="2" Rezid="1"
      baza1="60000" imp1="6000" divid_D="60000" divid_P="60000"/>
  …
</declaratie205>
```

La Ionescu Maria, baza (40.000) este cea a dividendelor distribuite, deși s-au plătit doar 30.000:
pentru dividendele distribuite și neplătite până la sfârșitul anului în care s-a aprobat distribuirea
lor, impozitul se datorează oricum și se plătește până la 25 ianuarie a anului următor (art. 97
alin. (7) Cod fiscal), deci intră în bază.

### Pasul 6 — Exportul în formularul PDF ANAF (Soft A)

Alternativ la XML (Soft J), apăsați **„Export formular ANAF (Soft A)"** din formularul declarației sau
**„D205 file XDP (Soft A)"** din bara de butoane a raportului de previzualizare, lângă „D205 file XML (Soft J)" (în acest caz declarația
anului trebuie generată în prealabil cu „Generează ciorna D205"). Declarația trebuie să aibă cel puțin
un beneficiar. Butonul stă în bara formularului declarației, lângă **„Export XML ANAF"**:

![Declarația D205 cu butoanele de export XML și formular ANAF (Soft A)](screenshots/03_declaratie_d205.png)

Ce se descarcă depinde de câmpul **Tip export**, ales la `Contabilitate → Configurare → Setări`, secțiunea
**Declarații ANAF România**:

| Tip de export | Fișier descărcat | Utilizare |
|---|---|---|
| **PDF cu datele incluse** (implicit) | `D205_<CUI>_<an>12.pdf` — formularul ANAF `D205_XML_2025_120226.pdf` completat | se deschide în Adobe Acrobat Reader, se apasă **Validare**, se semnează și se depune |
| **Descărcare directă XDP** | `D205_<CUI>_<an>12.xdp` | se importă în formularul descărcat de pe site-ul ANAF (**Import Date**) |
| **Arhivă ZIP cu XDP și PDF** | arhivă cu `.xdp` și formularul PDF | aceeași utilizare ca la XDP |

Completarea PDF-ului cere pe server biblioteca **pypdf 5.0 sau mai nouă**; fără ea, opțiunea „PDF cu
datele incluse" descarcă arhiva ZIP, iar setările ANAF ale firmei afișează un avertisment.

Formularul conține: identificarea firmei și a declarantului, secțiunea II pe tipuri de venit cu totalul
general, suma de control `totalPlata_A`, bifele de la secțiunea III pentru tipurile de venit folosite și
câte un tabel de beneficiari pentru fiecare tip de venit. Coloanele 7 și 8 ale beneficiarului depind de
cod: la **08** dividendele distribuite și plătite, la **25** câștigul și pierderea (fără bază și
impozit), la **29** venitul în natură (VB) și garanția chiriei (GAR). La nerezidenți se completează
statul de rezidență și CIF-ul din străinătate.

Verificați înainte de depunere că totalurile din formularul PDF ANAF coincid cu cele din fișierul XML:
ambele exporturi folosesc aceleași valori, rotunjite la leu pe beneficiar (de la 50 de bani în sus),
iar totalurile se fac din valorile rotunjite. Totalurile din ecranul declarației din Odoo sunt
nerotunjite, deci la sume cu bani pot diferi cu câțiva lei de cele exportate.

### Pasul 7 — Închiderea pasului în checklist

Reveniți la pasul D205 din **Declarații fiscale**, **atașați** fișierul semnat / recipisa și marcați pașii
ca **revizuiți**; declarația poate fi trecută pe **Trimis**.

![Lista declarațiilor D205](screenshots/05_lista_d205.png)

### Note de monografie și raportare

- Modulul **nu generează note contabile** — este o declarație informativă; impozitul reținut este deja
  înregistrat (446x) la momentul plății. Notele din amonte, la dividende: `117 = 457` (distribuire),
  `457 = 446` (reținerea impozitului, cu asociatul ca partener), `457 = 5121` (plata netă), `446 = 5121`
  (plata impozitului la buget, declarat lunar în D100).
- Raportul și importul preiau doar **persoane fizice rezidente** cu rulaj creditor pe 446x în perioada
  selectată; firmele și nerezidenții (bifa WHT sau țară străină) rămân pe dinafară.
- `Rezid` = 1 pentru rezidenți (fără `Stat_R` și `cifS`), 2 pentru nerezidenți (cu `Stat_R` obligatoriu).
- La codul 25 se declară câștigul și pierderea, nu baza și impozitul; la 08, dividendele distribuite și
  plătite; la 29, venitul în natură și garanția chiriei.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `account` | sursa impozitului reținut (446x) | dependență (manifest) |
| `account_reports` (via `l10n_ro_reports`) | raportul de previzualizare + cockpitul `account.return` | dependență (manifest) |
| `l10n_ro_reports` | tipul de return RO, țara, integrarea cu Declarații fiscale | dependență (manifest) |
| `l10n_ro_anaf_base` | profilul declarației, validarea XSD, numele standardizat al fișierului, butoanele de export | dependență (manifest) |
| `l10n_ro_partner_screening` | bifa **Impozit la sursă (WHT)**, care marchează nerezidenții excluși din D205 | dependență (manifest) |
| `l10n_ro_anaf_d207` | declarația pentru beneficiarii **nerezidenți** | modul-pereche |
| `l10n_ro_dividends` | dividendele către asociați (cod 08). **Atenție:** nota de plată pune impozitul pe 446 într-o singură linie, fără partener, așa că importul D205 nu îl preia — beneficiarii de dividende se adaugă manual până la corecția modulului | flux în amonte |

Ce este automat: pasul cu termen în Declarații fiscale, raportul de previzualizare cu drill-down, preluarea
beneficiarilor rezidenți din 446x la „Generează ciorna", rezidența și regimul fiscal propuse, calculul
totalurilor și al sumei de control, regulile validatorului, validarea XSD și numele fișierului.
Ce rămâne manual: tipul de venit real și baza, câmpurile specifice codului, beneficiarii nerezidenți,
confirmarea, exportul și atașarea dovezii de depunere în SPV.

## 8. Verificări pentru consultant

- [ ] Modulul se instalează fără erori (necesită `l10n_ro_anaf_base`, `l10n_ro_partner_screening`,
      `l10n_ro_reports`).
- [ ] În **Declarații fiscale** apare un pas **D205** cu termen **28/29 februarie** și 3 verificări.
- [ ] Raportul de previzualizare arată impozitul pe 446x pentru PF rezidente, grupat pe partener, cu
      drill-down în documente; un partener străin sau cu bifa WHT nu apare.
- [ ] Butonul **„Generează ciorna D205"** creează/actualizează ciorna anului și deschide formularul.
- [ ] Liniile importate au **Rezidență = 1** și **Regim fiscal = 2**; totalurile reflectă suma liniilor.
- [ ] Verificarea „Beneficiari fără CNP/NIF" devine **anomalie** dacă lipsește `cifR` și **revizuită**
      după completare.
- [ ] Un nerezident pe codul 08 este refuzat la confirmare; pe codul 16, cu stat de rezidență, este admis.
- [ ] Confirmarea fără beneficiari este blocată; a doua confirmare este blocată.
- [ ] Exportul XML produce `declaratie205`, `sect_II` per tip de venit și `benef` per beneficiar, și
      trece validarea DUKIntegrator.
- [ ] Numele fișierului respectă formatul `D205_<CUI>_<an>12.xml`.
- [ ] Fără persoana de contact sau funcția ei în setările ANAF ale firmei, exportul se oprește cu mesaj.
- [ ] **Export formular ANAF (Soft A)** pe o declarație fără beneficiari este refuzat; cu beneficiari,
      descarcă fișierul potrivit tipului de export din setările firmei (PDF, XDP sau ZIP).
- [ ] În formular, bifele secțiunii III corespund tipurilor de venit din declarație, iar totalul general
      și `totalPlata_A` coincid cu cele din XML.
- [ ] La codul 08 coloanele 7 și 8 arată dividendele distribuite și plătite; la 25, câștigul și pierderea;
      la 29, VB și GAR.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|-----------------|-----------------|-----------|
| „Nu s-au găsit conturi 446x în planul de conturi." | Planul de conturi nu conține 446x | Verificați planul de conturi RO |
| „Nu s-au găsit înregistrări de impozit reținut la sursă pe conturile 446x pentru PF rezidente …" | Niciun beneficiar PF rezident cu rulaj creditor pe 446x în anul ales | Verificați partenerul de pe liniile 446x și bifa WHT |
| „Nu există o declarație D205 pentru anul fiscal selectat…" (la export din raport) | Nu a fost încă generată ciorna | Apăsați „Generează ciorna D205" |
| „Adăugați cel puțin un beneficiar înainte de confirmare." | Declarație fără linii | Generați sau adăugați manual beneficiari |
| „…: lipsește CNP-ul/NIF-ul din România (cifR)." | Beneficiar fără CNP/NIF | Completați CNP-ul pe partener sau pe linie |
| „…: tipul de venit 08 se declară numai pentru rezidenți…" | Nerezident pe un cod rezervat rezidenților | Declarați-l în D207 sau corectați rezidența |
| „…: regimul fiscal … nu este admis pentru tipul de venit …" | Regim fiscal schimbat manual greșit | 0 la codul 25, 2 sau 3 la 26/27, 2 în rest |
| „…: același CNP/NIF apare de două ori la tipul de venit …" | Două linii pentru același beneficiar și cod | Comasați liniile |
| „Compania '…' nu are configurat un contact pentru declarații." / „… nu are configurată o funcție pentru declarații." | Lipsește persoana de contact ANAF sau funcția ei | Completați-le în Setări → Declarații ANAF România |
| „Adresa fiscală a companiei '…' este incompletă (stradă, localitate, cod poștal, țară)." | Adresa firmei incompletă | Completați adresa pe fișa firmei |
| „Nu există beneficiari de exportat." (la Export formular ANAF) | Declarație fără linii | Generați sau adăugați manual beneficiari |
| Eroare de validare XSD la export | Date incomplete/invalide față de schema ANAF | Corectați câmpurile semnalate |

## 10. Capturi de ecran

Capturile (`static/description/`) sunt **generate automat** din `tests/test_screenshots.py`
(mixinul `ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), în **limba română**,
pe planul de conturi RO (`setup_country("ro")`), cu datele demo de mai sus:

1. `01_return_checklist.png` — cardul D205 din cockpitul Declarații fiscale („3 în așteptare", workflow Revizuire → Trimite); termenul și verificările se văd în formularul pasului.
2. `02_raport_preview_446x.png` — raportul de previzualizare 446x, cu partenerii desfășurați pe documente (drill-down), cu butoanele „D205 file XML (Soft J)" și „D205 file XDP (Soft A)" în bara raportului.
3. `03_declaratie_d205.png` — formularul cu beneficiari PF rezidenți (dividende la cota anului și chirie la cod 29, pe venitul net), totaluri și butoanele de export (referită și la Pasul 6).
4. `04_declaratie_confirmata.png` — declarația în starea Confirmată.
5. `05_lista_d205.png` — lista declarațiilor D205.

Regenerare:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i l10n_ro_anaf_d205,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

În manualul final, păstrați explicația orientată pe activitatea utilizatorului: când se depune D205
(anual, termen ultima zi din februarie, pentru impozitul reținut la sursă pe beneficiari persoane
fizice — în primul rând dividendele către asociați), cum se parcurg pașii din **Declarații fiscale**, cum
se folosește **raportul de previzualizare** pentru a verifica și **genera ciorna**, cum se completează
beneficiarii (CNP, tip de venit, bază, câmpurile pe cod) și cum se obține fișierul XML validat pentru SPV
sau formularul PDF ANAF completat (Soft A).
Subliniați delimitarea: **rezidenții în D205, nerezidenții în D207** (cu excepțiile admise de structura
D205) și că impozitul trebuie deja reflectat pe 446x.
