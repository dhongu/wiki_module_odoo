# Fișă Modul: Retururi și garanții (RMA)

**Modul:** `deltatech_rma`
**Versiune:** 19.0.1.0.0
**Suită:** bitshop
**Dependențe:** `sale_stock`, `portal`

---

## 1. Scop business

Clientul cere returul unui produs direct din comanda lui, iar cererea trece printr-un flux cu
decizie: noi aprobăm sau refuzăm, primim coletul, verificăm marfa și spunem ce se întâmplă cu ea.

Odoo nu are RMA. Ce are este wizardul de retur pe o livrare, pornit de un coleg din depozit, și
panoul After-Sales din Helpdesk Enterprise. Niciunul nu-i dă clientului o cale să **ceară** returul
și niciunul nu cunoaște o politică de retur.

Ce aduce modulul, în ordinea în care se vede:

- cererea deschisă de client din portal, per linie de comandă, cu poze;
- **fișa de retur PDF cu cod de bare**, trimisă pe mail, pe care clientul o pune în colet;
- **recepția coletului prin scanare**: un singur câmp, codul de pe fișă sau AWB-ul;
- verdict per produs și repunerea în stoc doar a ce e bun, prin transferul standard de retur;
- politica de retur ca date: taxă, poze obligatorii, cine plătește transportul, per motiv.

## 2. Bază legală și context

Returul comercial **nu** e același lucru cu retragerea în 14 zile.

| | Retragere (Directiva 2011/83/UE) | Retur comercial / garanție |
|---|---|---|
| cine decide | consumatorul, unilateral | comerciantul, după verificare |
| motiv | interzis a fi cerut (art. 9) | obligatoriu |
| stare de aprobare | nu există | există |
| taxă reținută | nu | da, dacă politica o prevede |

Retragerea e acoperită de `deltatech_sale_withdrawal`, care **nu are** stare de aprobare, tocmai
pentru că nu are voie. Modulul acesta stă lângă el, nu peste el. Ce împart cele două e partea în
care legea tace: marfa se întoarce prin `stock.return.picking`, niciodată prin mișcări scrise de
mână.

Garanția legală de conformitate (OUG 140/2021, 2 ani) e valoarea implicită a ferestrei de
eligibilitate pentru cererile de tip garanție. Fereastra se schimbă din Setări, nu din cod.

## 3. Utilizatori și roluri

| Grup | Ce poate |
|---|---|
| **Retururi / Utilizator** | vede registrul, deschide cereri, aprobă, preia colete, pune verdicte, creează transferul de retur |
| **Retururi / Responsabil** | în plus: configurează motive, etichete și motive de închidere, șterge cereri |
| **Portal** | vede doar cererile proprii și ale firmei lui, trimite cereri și mesaje pe ele |

**La instalare, orice utilizator intern devine Utilizator de retururi**, inclusiv cei adăugați de
acum încolo — ca în `agroamat_retururi`. Dacă firma vrea să dea accesul doar unor oameni anume,
debifează *Toți utilizatorii interni lucrează cu retururi* în setări (vezi secțiunea 5); de atunci
grupul se atribuie de mână. O dezactivare rămâne dezactivată și după actualizarea modulului.

Regula de acces pe client e `child_of` pe partenerul comercial: un angajat al firmei client vede
cererile firmei, nu doar pe ale lui. Multi-companie: regulă globală pe `company_id`.

## 4. Conturi și date implicate

Modulul **nu** generează note contabile singur. Singurul document contabil pe care îl produce e o
**notă de credit în ciornă** (`account.move`, tip `out_refund`), pe valoarea rambursabilă:

```
valoare returnată − taxă de manipulare = valoare rambursabilă
```

Creditarea se face linie cu linie, cu prețul net de taxa liniei, ca totalul notei să fie exact
valoarea rambursabilă, iar cotele de TVA se preiau de pe linia comenzii originale. Nota rămâne în
**ciornă**: o pregătim, nu o înregistrăm în locul contabilului.

Nota contabilă, la înregistrarea notei de credit de către contabil, e cea standard de stornare
vânzare:

| Cont | Descriere | Dr | Cr |
|---|---|---|---|
| 4111 | Clienți | | X |
| 707 / 701 | Venituri din vânzări (stornare) | X | |
| 4427 | TVA colectată (stornare) | X | |

Marfa se întoarce în stoc prin transferul de retur, cu mișcările legate de livrarea pe care o
anulează (`origin_returned_move_id`). Fără legătura asta valorizarea nu poate reconcilia returul,
iar costul repus în stoc ar fi cel curent, nu cel cu care a ieșit.

## 5. Configurare inițială

1. **Retururi → Configurare → Motive de retur** — politica. Fiecare motiv are categoria, intervalul
   taxei (minim / propus / maxim), dacă cere poze, cine plătește transportul și explicația pentru
   client. Motivele livrate sunt un punct de plecare, cu `noupdate="1"`: ce schimbați rămâne.
2. **Vânzări → Configurare → Setări → Retururi și garanții** — cine are acces (toți utilizatorii
   interni sau doar cei aleși), fereastra de eligibilitate (luni pentru garanție, zile pentru retur),
   motiv obligatoriu sau opțional, taxa implicită.
3. **Produse** — bifa „Nu se poate returna” pe produsele de tip taxă și pe categoriile lor, ca să nu
   apară în formularul clientului.
4. **Retururi → Configurare → Etichete** și **Motive de închidere** — opțional, pentru raportare.
5. Verificați că firma are adresă completă și e-mail: fișa de retur tipărește adresa unde vine
   coletul, din `company_id.partner_id`.

## 6. Flux de utilizare

Fluxul are două jumătăți, cu utilizatori diferiți: clientul, în portalul lui, și echipa, în back
office. Fiecare pas de mai jos are ecranul lui în `readme/screenshots/`.

### Partea clientului

#### 6.1 De unde pleacă

![Cardul din Contul meu](screenshots/01_portal_cont.png)

*Contul meu* → cardul **Retururi și garanții**, lângă comenzi și facturi. Mai există două intrări:
meniul din dreapta sus (*Retururile mele*, *Cere retur*) și butonul de pe pagina fiecărei comenzi
confirmate.

![Butonul de pe comandă](screenshots/02_portal_buton_comanda.png)

Butonul de pe comandă sare direct la pasul cu produsele, cu comanda deja aleasă.

#### 6.2 Ce s-a întâmplat

![Alegerea tipului](screenshots/03_portal_tip_cerere.png)

Trei cartonașe, nu o listă de motive. Sub fiecare scrie politica: cine plătește transportul, dacă
pozele sunt obligatorii, ce taxă se poate reține. **Textele se calculează din catalogul de motive**,
nu sunt scrise în șablon: dacă schimbați o taxă în configurare, se schimbă și ce citește clientul.

#### 6.3 Din ce comandă

![Alegerea comenzii](screenshots/04_portal_comanda.png)

Doar comenzile lui confirmate, filtrate pe fereastra de eligibilitate a tipului ales. Pasul lipsește
dacă a intrat cu butonul de pe o comandă.

#### 6.4 Ce produse

![Produsele](screenshots/05_portal_produse.png)

Bifează produsele, cantitatea, motivul per produs, descrierea și pozele. Nu apar în listă:
transportul, taxele, serviciile, produsele marcate „nu se poate returna" și ce a cerut deja pe altă
cerere. Cantitatea e plafonată la cât a cumpărat.

Eticheta câmpului de poze urmează motivul: „opțional” cât timp niciun produs bifat nu le cere,
„obligatorii la motivul ales” altfel. Când motivul cere poze și clientul n-a atașat niciuna, formularul **nu pleacă**: mesajul apare pe loc,
lângă câmpul de poze, fără drum la server. Serverul verifică oricum încă o dată — dacă pozele atașate
nu se pot deschide ca imagine, clientul se întoarce la formular cu un mesaj, nu rămâne cu o cerere
fără dovadă.

![Garanție fără poze: formularul se oprește în pagină](screenshots/05a_portal_fara_poze.png)

La returul de tip renunțare și la produsul greșit — cele care se pot încheia cu banii înapoi —
formularul cere și **IBAN-ul pentru rambursare**. E opțional: gol, echipa îl cere la rezolvare. Dacă e
completat, se verifică (țară, lungime, sumă de control), iar unul greșit întoarce clientul la formular.
Aceeași verificare se aplică în back office, când colegul îl tastează de la telefon.

![IBAN-ul pentru rambursare](screenshots/05b_portal_iban.png)

#### 6.5 Confirmarea

![Cererea trimisă](screenshots/06_portal_trimis.png)

Banda cu șase pași îi arată unde e. Cât timp cererea e la noi, scrie explicit să **nu** trimită
coletul.

#### 6.6 Aprobată: fișa și AWB-ul

![Cererea aprobată](screenshots/07_portal_stadiu.png)

După aprobare descarcă **fișa de retur (PDF)** și își poate scrie numărul AWB. Când îl scrie, cererea
trece singură în „așteptăm coletul".

#### 6.7 Rezolvată

![Cererea rezolvată](screenshots/08_portal_rezolvat.png)

La final vede decizia și textul scris de noi, plus taxa reținută și suma care i se întoarce, dacă e
cazul.

### Partea echipei

#### 6.8 Fișa de retur

![Fișa de retur](screenshots/09_fisa_retur_pdf.png)

Pleacă atașată la mailul de aprobare. Codul de bare e chiar numărul cererii — de el se agață
recepția prin scanare.

#### 6.9 Registrul

![Registrul, listă](screenshots/10_registru_lista.png)

*Retururi → Retururi și garanții*, cu filtrul implicit „În lucru" și vârsta fiecărei cereri.

![Registrul, pe stări](screenshots/11_registru_kanban.png)

Aceleași cereri pe stări, pentru cine lucrează pe fluxul zilnic.

#### 6.10 Decizia

![Cererea, cu butoanele de decizie](screenshots/12_cerere_decizie.png)

**Aprobă și trimite fișa** trimite clientului mailul cu fișa atașată. O cerere cu motiv care cere
poze, venită fără nicio poză, e semnalată pe formular înainte de aprobare. **Refuză** închide cererea
cu explicația scrisă de dumneavoastră.

#### 6.11 Recepția coletului

![Recepția prin scanare](screenshots/13_receptie_scanare.png)

Un singur câmp. Se scanează codul de pe fișă sau AWB-ul; pistolul trimite Enter, iar cererea se
deschide singură. Dacă fișa lipsește din colet, coletul se alege din lista celor așteptate.

#### 6.12 Verificarea

![Verdictele](screenshots/14_verificare_verdicte.png)

Cantitatea primită se pregătește cu cea cerută, iar lipsa se vede pe coloana ei. Verdictul se pune pe
fiecare produs; **Toate sunt bune** face coletul întreg dintr-o apăsare. Fără verdict pe fiecare
linie nu se trece mai departe.

#### 6.13 Rezolvarea

![Decizia finală](screenshots/15_rezolvare.png)

Înlocuire, reparație, banii înapoi sau refuz. Banii cer IBAN-ul. De aici pleacă nota de credit în
ciornă și comanda de înlocuire, tot în ciornă.

#### 6.14 Repunerea în stoc

![Transferul de retur](screenshots/16_transfer_retur.png)

**Repune în stoc** creează transferul **numai** din liniile cu verdictul „bun". Observați
*Document sursă: Return of …* — legătura cu livrarea pe care o anulează. Marfa intră în stoc când
**validați** transferul, nu înainte.

### Configurarea

![Motivele de retur](screenshots/17_motive_politica.png)

*Retururi → Configurare → Motive de retur*: politica întreagă, ca date. Taxa minimă / propusă /
maximă, pozele obligatorii, cine plătește transportul, explicația pentru client.

![Setările pe companie](screenshots/18_setari.png)

*Vânzări → Configurare → Setări → Retururi și garanții*: fereastra de eligibilitate, motivul
obligatoriu sau opțional, taxa implicită.

![Analiza](screenshots/19_analiza.png)

*Retururi → Analiză*: retururile pe luni și tipuri, iar pe liniile de retur, cantitatea returnată
față de cea vândută — adică rata de retur per produs.

## 7. Legături cu alte module / declarații

| Modul | Legătura |
|---|---|
| `deltatech_sale_withdrawal` | retragerea în 14 zile, act juridic diferit; model separat, intenționat |
| `sale_stock` | comanda, livrarea, transferul de retur |
| `account` | nota de credit în ciornă |
| `deltatech_marketplace_sale` | `marketplace.return.request` e a treia entitate, a eMAG / Shopify; se leagă printr-o punte, nu se contopește |

Niciun raport ANAF nu se alimentează din acest modul. Nota de credit, odată înregistrată de
contabil, intră în D300 și D394 ca orice storno de vânzare.

## 8. Verificări pentru consultant

- [ ] Motivele de retur reflectă politica scrisă a clientului (taxă, poze, transport), confirmată
      de el, nu presupusă.
- [ ] Fereastra de eligibilitate e cea agreată; la garanție, cel puțin 24 de luni.
- [ ] Produsele de tip taxă și transport au bifa „Nu se poate returna”.
- [ ] Firma are adresă completă și e-mail — apar pe fișa de retur.
- [ ] Fișa de retur se tipărește corect, iar codul de bare se scanează cu pistolul clientului.
- [ ] Un retur de test intră în stoc cu **costul cu care a ieșit**, nu cu cel curent: verificați
      evaluarea pe transferul de retur.
- [ ] Nota de credit de test are TVA-ul corect, preluat de pe comanda originală.
- [ ] Clientul de portal vede doar cererile lui: testați cu doi clienți diferiți.

## 9. Mesaje de eroare frecvente

| Mesaj | Ce înseamnă | Ce faceți |
|---|---|---|
| „Pune verdictul pe fiecare produs” | o linie a rămas fără verdict | completați verdictul sau apăsați *Toate sunt bune* |
| „Nimic de repus în stoc” | nicio linie cu verdict „bun” și cantitate primită legabilă de o livrare validată | verificați verdictele și dacă livrarea originală e validată |
| „Returul X e deja închis” | s-a scanat un colet pe o cerere finalizată | deschideți cererea din registru și redeschideți-o |
| „Nu găsesc nicio cerere cu codul …” | cod greșit sau cerere din altă companie | căutați clientul în registru |
| „Ca să dăm banii înapoi avem nevoie de IBAN” | decizie „banii înapoi” fără IBAN | completați IBAN-ul sau sunați clientul |
| „La «motiv», taxa poate fi doar între X% și Y%” | s-a depășit intervalul motivului | schimbați procentul sau motivul |

## 10. Capturi de ecran

Cele 21 de capturi din `readme/screenshots/` sunt cele folosite în secțiunea 6, în ordinea fluxului:
zece de pe partea clientului (01–08, plus 05a fără poze și 05b cu IBAN-ul), șase de pe partea echipei (09–16) și trei de configurare și
analiză (17–19).

Se generează cu testul `tests/test_screenshots.py`, în română, pe planul de conturi RO:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_rma,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

Testul își face singur datele: client de portal, comenzi livrate, cereri în fiecare stare, un
transfer de retur și puțin istoric, ca ecranul de analiză să arate o distribuție, nu o singură bară.

## 11. Observații pentru manual

- Insistați, la instruire, pe **fișa din colet**: fără ea recepția prin scanare se face pe AWB, iar
  dacă nici AWB-ul n-a fost declarat, coletul se caută de mână. Fișa e ce face diferența.
- Taxa de manipulare se discută **înainte** de implementare, cu cifre. E singura parte a modulului
  care produce discuții cu clienții finali.
- Transferul de retur rămâne nevalidat până îl validează cineva. Asta e intenționat: marfa se
  numără fizic înainte să intre în stoc.
