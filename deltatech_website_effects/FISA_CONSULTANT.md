# Fișă Modul: Efecte vizuale pentru blocurile website

**Modul:** `deltatech_website_effects`
**Utilizator principal:** Consultant website / designer al site-ului (rolul Website › Editor și Designer sau administrator)
**Prioritate:** 🟢 Scăzută (aspect vizual al site-ului; nu atinge date de business, contabilitate sau stocuri)

---

## 1. Scop business

Modulul adaugă în editorul website o colecție de efecte vizuale pe care consultantul le aplică
**bloc cu bloc**, fără cod: carduri care reacționează la mouse (se înclină, se ridică, strălucesc),
forme gata desenate (etichetă de preț, card cu accent colorat, panou de sticlă mată), animații de
atenție, efecte pe secțiuni, pe butoane și pe meniul din antet, plus cinci blocuri noi de conținut
(traseul livrării, caseta de ajutor, lista de informații, codurile de copiat și cardul care se
întoarce). Scopul este ca un magazin sau un site de prezentare să arate „viu" și modern fără
intervenția unui programator. Nimic nu se schimbă pe site până nu alegeți un efect pentru un bloc.

## 2. Bază legală și context

Nu există o bază legală: modulul ține strict de aspectul site-ului. Context operațional:

- efectele sunt clase CSS puse pe bloc din editor și se salvează odată cu pagina; dezinstalarea
  modulului le scoate efectul, dar nu strică conținutul. Excepție: cele cinci blocuri noi rămân în
  pagină fără formatare (fără stil, animație și copiere) și trebuie șterse manual;
- efectele cu mișcare respectă setarea de accesibilitate **„reducerea mișcării"** a sistemului
  vizitatorului (Windows/macOS/iOS/Android): pentru acești vizitatori animațiile sunt oprite;
- **3D Tilt** funcționează doar pe dispozitive cu mouse; pe telefon și tabletă cardul rămâne nemișcat.

## 3. Utilizatori și roluri

- **Consultant / designer website** — aplică efectele din editor (necesită drept de editare a
  site-ului: în **Setări › Utilizatori**, la *Website*, rolul **Editor și Designer**, sau **Editor
  restricționat** pe paginile permise).
- **Vizitatorul site-ului** — vede efectele; nu are nimic de configurat.

Roluri recomandate la testare: un utilizator cu rolul *Editor și Designer* pentru editare și o fereastră
privată (vizitator anonim) pentru verificarea rezultatului, inclusiv pe telefon.

## 4. Conturi și date implicate

Modulul nu are conturi contabile, modele sau câmpuri noi — lucrează doar pe conținutul paginilor
(HTML-ul salvat) și pe trei vederi opționale ale antetului (**Glass**, **Menu Hover › Underline**,
**Menu Hover › Fill**), activate per website.

Date minime pentru demo: un website cu o pagină editabilă care are o secțiune cu coloane sau
carduri (de exemplu blocul *Coloane* sau *Carduri*), o secțiune cu imagine de fundal (pentru
*Glass*, *Hover Overlay*, *Background Pan*) și un buton.

## 5. Configurare inițială

1. Instalați modulul `deltatech_website_effects` (depinde doar de `website`).
2. Nu există setări de modul: opțiunile apar direct în editorul website, în panoul **Stil** al
   blocului selectat.
3. Deschideți site-ul, apăsați **Editează** și selectați un bloc pentru a vedea opțiunile noi.

> Etichetele opțiunilor apar în interfața RO parțial traduse: cele care există și în Odoo standard
> sunt în română (*Efect la trecerea mouse-ului*, *Imagini*, *Formă*, *Evidențiază*, *Viteză*,
> *Colțuri rotunde*, *Titlu*, *Zile*, *Link-uri*), cele specifice modulului rămân în engleză
> (*Attention*, *Hover Overlay*, *Background Pan*, *Hover Focus*, *Hover Animation*, *Glass*, *Menu
> Hover*, *Vehicle*, *Color*, *Back Color*, *Card Style* și rândurile *Info List*: *Courier
> Delivery*, *Free Delivery*, *Over*, *Up to (kg)*, *Payment*, *Returns*, *Pick Up*, *Hours*).
> Textele implicite ale blocurilor noi sunt în engleză și se rescriu direct în pagină.

## 6. Flux de utilizare

### Pasul 1 — Efectele unui card sau ale unei coloane

În editor (**Site → Editează**), dați clic pe un card sau pe o coloană dintr-o secțiune. În
panoul **Stil**, sub *Animare*, modulul adaugă patru rânduri:

| Opțiune (eticheta din editor) | Valori | Ce face |
|---|---|---|
| **Hover Effect** (*Efect la trecerea mouse-ului*) | 3D Tilt, Lift, Glow, Frame, Holo, Border Reveal, Background Color | reacția blocului când mouse-ul trece peste el |
| ↳ **Highlight** (*Evidențiază*) | culoare | doar la *3D Tilt*: culoarea luminii care urmărește cursorul; goală = lumină albă neutră |
| ↳ **Color** | culoare | doar la *Border Reveal* (culoarea benzii) și *Background Color* (culoarea fundalului) |
| **Images** (*Imagini*) | Grayscale to Color, Zoom | imaginile din bloc trec din gri în color sau se măresc lent |
| **Shape** (*Formă*) | Price Tag, Price Tag (pointed), Accent Card, Glass | forma vizuală a blocului |
| ↳ **Tone** / **Blur** | 8 tonuri + Theme / Light, Medium, Strong | tonul cardului *Accent Card*, intensitatea sticlei *Glass* |
| **Attention** | Pulse, Nudge icons | atrage privirea: un halou care „respiră" de trei ori la încărcare, respectiv iconițele care se mișcă la hover |

Când selectați un card dintr-o coloană, panoul arată două grupuri cu aceleași opțiuni: unul pentru
**Coloană** și unul pentru **Bloc** (cardul). Alegeți efectul pe grupul elementului care trebuie
să se miște — de obicei cardul.

![Opțiunile modulului în panoul Stil al unui card: Hover Effect = 3D Tilt, Highlight, Images, Shape, Attention](screenshots/01_optiuni_bloc.png)

### Pasul 2 — Ce vede vizitatorul la hover

Salvați pagina și treceți cu mouse-ul peste carduri. *3D Tilt* înclină cardul spre cursor (până la
câteva grade) cu o lumină care îl urmărește, *Lift* îl ridică cu o umbră mai adâncă, *Glow* aprinde
un halou în culoarea principală a temei, *Holo* trece o strălucire irizată, *Frame* desenează un
contur la mică distanță, *Border Reveal* crește o bandă colorată în stânga și mută conținutul,
*Background Color* schimbă fundalul, iar *Images › Grayscale to Color* colorează poza (în captură,
cardul *Glow* este sub cursor).

![Pagina salvată: carduri cu efectele modulului; cardul Glow este sub cursor](screenshots/02_efecte_hover.png)

### Pasul 3 — Formele Accent Card și Price Tag

**Accent Card** pune o bară colorată sus și un fundal ușor nuanțat; la hover iconița „sare", iar
săgețile de tip *→* se depărtează de text. Tonul se alege din **Tone** (Theme sau Green, Blue,
Amber, Gold, Red, Olive, Slate, Purple). Combinat cu *3D Tilt* dă carduri de categorie (în captură,
cardul *Hidraulică* este sub cursor).
**Price Tag** transformă un text scurt într-o etichetă de preț caldă, cu o gaură perforată, care se
balansează la hover; varianta *pointed* are gaura în vârful etichetei. Pusă într-un card cu efect
la hover, eticheta se înclină când este „atins" cardul.

![Accent Card în trei tonuri (Green, Blue, Amber) cu 3D Tilt și un card cu Price Tag, Price Tag (pointed) și buton cu Hover Animation](screenshots/03_forme_accent_price_tag.png)

### Pasul 4 — Forma Glass (sticlă mată)

**Glass** face blocul translucid: ce se află în spatele lui se vede estompat și mai saturat, cu o
margine luminoasă. Are nevoie de **ceva colorat în spate** (imagine de fundal, degrade) — pe fundal
alb arată ca un card simplu. **Blur** reglează intensitatea: *Light*, *Medium* (implicit), *Strong*.
În captură, cele trei carduri de sus au *Blur* *Medium*, *Strong* și *Light*, peste o imagine cu
multe detalii; secțiunea de dedesubt este cea folosită la pasul 5.

![Trei carduri Glass (Medium, Strong, Light) peste o imagine de fundal](screenshots/04_glass.png)

### Pasul 5 — Opțiunile de secțiune

Selectați **secțiunea** (clic pe fundalul ei, nu pe o coloană). În panoul **Stil** apar:

- **Hover Overlay** + **Color** — un strat de culoare apare peste imaginea de fundal la hover
  (implicit negru transparent);
- **Background Pan** — imaginea de fundal alunecă lent în jos la hover;
- **Hover Focus** — coloana de sub mouse rămâne clară, celelalte coloane ale rândului se estompează.

![Secțiunea cu imagine de fundal selectată: Hover Overlay cu Color, Background Pan, Hover Focus](screenshots/05_optiuni_sectiune.png)

### Pasul 6 — Hover Animation pe butoane

Selectați un **buton**. În grupul *Buton* apare **Hover Animation**, cu zece variante: *Grow*,
*Shrink*, *Pulse*, *Float*, *Bob*, *Wobble*, *Buzz*, *Push*, *Shine* (o lumină trece peste buton),
*Press*. Opțiunea este pe butonul selectat, nu pe toate butoanele site-ului.

![Butonul „Adaugă în coș” selectat, cu Hover Animation = Shine](screenshots/06_buton_hover_animation.png)

### Pasul 7 — Antetul: Glass și Menu Hover

Dați clic pe **antet**. La finalul panoului apar:

- **Glass** — antetul devine din sticlă mată când pagina este derulată și antetul rămâne deasupra
  conținutului. Depinde de opțiunea nativă a antetului **Efect de derulare**: cu *Fix* antetul
  stă mereu sus și este din sticlă pe toată derularea; cu *Standard* antetul dispare la derularea
  în jos și reapare, din sticlă, la derularea în sus; cu *Derulați* antetul iese din ecran și
  efectul nu se vede;
- **Menu Hover** — *Underline* (o linie crește sub elementul de meniu de sub mouse și sub pagina
  curentă) sau *Fill* (un fundal ușor umple elementul de la stânga).

Ambele sunt setări ale **website-ului** (se aplică pe toate paginile), nu ale paginii curente.

![Opțiunile antetului: Glass activ și Menu Hover = Underline (Subliniat)](screenshots/07_antet_glass_menu_hover.png)

### Pasul 8 — Antetul pe site

Salvați și derulați pagina. Cu *Efect de derulare* = *Fix*, antetul rămâne sus, iar conținutul
trece pe sub el estompat; elementul de meniu de sub mouse (în captură, *Acasă*) are linia de
dedesubt a lui *Menu Hover › Underline*.

![Pagina derulată: antetul din sticlă peste cardurile Glass, cu „Acasă” subliniat la hover](screenshots/08_antet_site.png)

### Pasul 9 — Blocurile noi din Conținut intern

În panoul **Blocuri**, la *Conținut intern*, modulul adaugă **Delivery Route**, **Help Box**,
**Info List**, **Copy Codes** și **Flip Card**. Trageți miniatura în pagină, într-o coloană sau
lângă un text, buton sau imagine; blocul se poate apoi muta, duplica sau șterge ca orice bloc.
Textele, linkurile și iconițele se editează direct în pagină (dublu clic pe o iconiță pentru a o
înlocui). În panoul *Stil*, grupul blocului poartă numele lui (*Delivery Route*, *Info List*
etc.). Pașii 10–14 pornesc de la un bloc deja plasat.

![Panoul Blocuri › Conținut intern, cu cele cinci blocuri ale modulului evidențiate](screenshots/09_blocuri_continut_intern.png)

### Pasul 10 — Delivery Route: vehicul, viteză, culoare, colțuri

**Delivery Route** arată cum ajunge comanda la client: un vehicul merge pe un drum punctat de la
depozit la ușa clientului, apoi o ia de la capăt; cele trei etape (titlu + detaliu) și iconițele
se editează direct în pagină (dublu clic pe iconiță pentru a o înlocui). Selectați blocul; în
grupul **Delivery Route** apar:

- **Vehicle** — Truck (implicit), Shopping Cart, Car, Motorcycle, Bicycle, Plane, Ship, Rocket;
- **Speed** (*Viteză*) — Slow, Normal, Fast;
- **Color** — culoarea drumului și a vehiculului (implicit culoarea principală a temei);
- **Round Corners** (*Colțuri rotunde*) — raza colțurilor blocului, în pixeli; plăcuțele din
  interior o urmează. Aceeași opțiune o au *Help Box*, *Info List* și *Flip Card*.

![Blocul Delivery Route selectat: Vehicle, Viteză, Color, Colțuri rotunde](screenshots/10_delivery_route.png)

### Pasul 11 — Help Box, Info List și Copy Codes pe site

- **Help Box** — card cu o iconiță, o întrebare (*Not sure this is the right part?*), un răspuns
  scurt și căile de contact: buton WhatsApp, buton spre formularul de contact și un telefon.
  Linkurile (`https://wa.me/...`, `tel:...`) se completează din editor.
- **Info List** — card cu titlu și link *Details*, rânduri cu iconiță, titlu și detaliu separate
  prin linii punctate (livrare prin curier, livrare gratuită, plată, retur, ridicare din magazin)
  și linkuri de politici jos. În captură, valorile sunt schimbate din opțiuni (pasul 12): livrare
  gratuită peste *300 lei*, retur în *30* de zile, rândul de ridicare din magazin ascuns.
- **Copy Codes** — o listă de coduri (coduri alternative, referințe) afișate ca etichete; un clic
  (sau Enter) copiază codul, iar eticheta devine verde cu bifă (în captură, primul cod tocmai a fost
  atins).

![Delivery Route, Help Box, Info List și Copy Codes pe pagina salvată](screenshots/11_help_box_info_list.png)

### Pasul 12 — Info List: rânduri și valori

Selectați blocul **Info List**. În grupul lui, pe lângă *Round Corners*, apar:

| Opțiune | Tip | Ce face |
|---|---|---|
| **Title** (*Titlu*) | bifă | afișează titlul și linkul *Details* |
| **Courier Delivery** | bifă | rândul de livrare prin curier |
| **Free Delivery** | bifă | rândul de livrare gratuită; cu el bifat apar **Over** (suma de la care livrarea e gratuită, text liber, de ex. *300 lei*) și **Up to (kg)** (greutatea maximă) |
| **Payment** | bifă | rândul cu metodele de plată |
| **Returns** | bifă | rândul de retur; cu el bifat apare **Days** (*Zile*) — numărul de zile de retur |
| **Pick Up** | bifă | rândul de ridicare din magazin; cu el bifat apare **Hours** — programul |
| **Links** (*Link-uri*) | bifă | linkurile de politici de jos |

Valorile scrise în panou se înlocuiesc direct în textul rândului; restul textului se editează în
pagină. Opțiunile există doar pe blocurile *Info List* plasate din versiunea 19.0.1.2.0 încolo;
blocurile mai vechi se editează doar în pagină.

![Info List selectat: Courier Delivery, Free Delivery cu Over = 300 lei și Up to (kg), Pick Up debifat](screenshots/12_info_list_optiuni.png)

### Pasul 13 — Flip Card: fața și spatele

**Flip Card** se întoarce la hover sau la focus de la tastatură. În editor ambele fețe sunt afișate
una sub alta, ca să le puteți edita; pe site se vede doar fața. Pe lângă *Round Corners*, are
**Back Color** — culoarea feței din spate (culoare simplă sau degrade).

![Flip Card selectat în editor: fața și spatele, cu Back Color și Colțuri rotunde](screenshots/13_flip_card.png)

### Pasul 14 — Tabs: Card Style

Pe un bloc **Tabs** (Taburi), selectați blocul și porniți **Card Style**: blocul intră într-un card,
bara de taburi stă pe un antet ușor colorat, iar tabul activ este ridicat pe o plăcuță albă cu o
linie de accent.

![Blocul Tabs cu Card Style activ](screenshots/14_tabs_card_style.png)

### Note de monografie și raportare

Modulul nu generează note contabile, documente sau rapoarte: efectele se salvează în conținutul
paginilor (clase CSS pe blocuri) și, pentru antet, ca vederi active ale website-ului.

### Cum se combină efectele

- Pe același bloc se poate alege **câte o valoare** din fiecare rând: un *Hover Effect*, un efect
  *Images*, o *Shape* și un efect *Attention* (de exemplu *Accent Card* + *3D Tilt* + *Nudge icons*).
- Efectele de **secțiune** (*Hover Overlay*, *Background Pan*, *Hover Focus*) se cumulează cu cele
  ale coloanelor din ea.
- *Price Tag* pus într-un card cu *3D Tilt*, *Lift*, *Glow* sau *Accent Card* se înclină când
  cardul este sub mouse.
- *Glass* arată bine doar peste o imagine sau un degrade (secțiune cu fundal).
- Efectele se pot pune și direct în șabloane QWeb, prin clasele din `readme/USAGE.md`
  (`tb_fx_tilt`, `tb_fx_lift`, `tb_fx_accent_card`, `tb_fx_copy` etc.) — util pentru programatori.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `website` | editorul în care apar opțiunile și blocurile | dependență (manifest) |
| `deltatech_website_sale_effects` | aduce efectele pe magazin: /shop, Products Design, checkout, pagina de produs; folosește *Info List* și *Delivery Route* pe pagina de produs | modul care depinde de acesta |

Ce este automat: dezactivarea animațiilor pentru vizitatorii cu „reducerea mișcării" și a lui
*3D Tilt* pe ecranele tactile; copierea codurilor din *Copy Codes*; animația vehiculului din
*Delivery Route*.
Ce rămâne manual: alegerea efectelor bloc cu bloc, textele blocurilor noi (implicit în engleză),
linkurile *Help Box* (WhatsApp, telefon) și ale *Info List*.

## 8. Verificări pentru consultant

- [ ] După instalare, o pagină existentă arată la fel ca înainte (efectele sunt opționale).
- [ ] Pe un card, *Hover Effect* = *3D Tilt*: pe site, cu mouse-ul, cardul se înclină spre cursor;
      cu *Highlight* gol lumina este albă, cu o culoare aleasă lumina are acea culoare.
- [ ] Pe telefon (sau în modul responsive cu atingere), cardul cu *3D Tilt* nu se mai înclină.
- [ ] *Accent Card* cu *Tone* = *Blue* are bara de sus albastră; *Theme* folosește culoarea temei.
- [ ] *Glass* pe un card dintr-o secțiune cu imagine de fundal: imaginea se vede estompată prin card;
      *Blur* = *Strong* estompează vizibil mai mult decât *Light*.
- [ ] Pe secțiune, *Hover Focus*: cu mouse-ul pe o coloană, celelalte se estompează.
- [ ] *Hover Animation* pe un buton se vede doar pe acel buton.
- [ ] *Menu Hover* și *Glass* pe antet se aplică pe toate paginile website-ului; cu *Efect de
      derulare* = *Fix*, antetul este din sticlă cât timp pagina e derulată.
- [ ] *Delivery Route*: schimbarea *Vehicle*, *Speed*, *Color* se vede pe site după salvare.
- [ ] *Info List*: *Over* = *300 lei* schimbă textul rândului de livrare gratuită; debifarea lui
      *Pick Up* ascunde rândul pe site.
- [ ] *Copy Codes*: clic pe un cod îl copiază (lipiți într-un câmp text ca să verificați).
- [ ] *Flip Card* se întoarce la hover; în editor ambele fețe sunt vizibile.
- [ ] În setările de accesibilitate ale sistemului, cu „reducerea mișcării" activă, animațiile
      (*Pulse*, *Tilt*, *Hover Animation*) nu mai rulează.
- [ ] Blocurile din *Conținut intern* pot fi trase într-o coloană a paginii, iar grupul lor din
      panoul *Stil* le poartă numele.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|---|---|---|
| *„Acest bloc nu poate fi plasat nicăieri pe această pagină"* pe Delivery Route, Help Box, Info List, Copy Codes, Flip Card | versiune a modulului mai veche de 19.0.1.2.0 | actualizați modulul |
| *Info List* nu are opțiunile de rânduri și valori | blocul a fost plasat cu o versiune mai veche de 19.0.1.2.0 | ștergeți blocul și plasați-l din nou, sau editați textele direct în pagină |
| *Glass* arată ca un card alb obișnuit | în spatele blocului nu este nimic colorat | puneți o imagine de fundal sau un degrade pe secțiune |
| *3D Tilt* nu se mișcă | ecran tactil, sau vizitatorul are „reducerea mișcării" activă | comportament voit; verificați cu mouse pe un calculator fără acea setare |
| Efectul nu apare pe card, ci pe toată coloana | efectul a fost ales pe grupul *Coloană*, nu pe *Bloc* | alegeți *Fără* la coloană și setați efectul pe grupul cardului |
| Antetul nu devine din sticlă | antetul are **Efect de derulare** = *Derulați*, deci nu rămâne sus | setați la antet **Efect de derulare** = *Fix* (sau *Standard*, unde antetul apare din sticlă la derularea în sus) |

## 10. Capturi de ecran

Capturile (`readme/screenshots/`) sunt generate automat din `tests/test_screenshots.py` (mixinul
`ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), cu interfața în română. Testul
creează patru pagini demo (`/efecte-hover`, `/efecte-forme`, `/efecte-glass`, `/efecte-blocuri`) și
fotografiază site-ul și editorul, cu rândurile modulului evidențiate:

1. `01_optiuni_bloc.png` — opțiunile modulului în panoul Stil al unui card (3D Tilt, Highlight,
   Images, Shape, Attention).
2. `02_efecte_hover.png` — cardurile cu efecte pe pagina salvată; cardul Glow sub cursor.
3. `03_forme_accent_price_tag.png` — Accent Card în trei tonuri și Price Tag.
4. `04_glass.png` — carduri Glass (Medium, Strong, Light) peste o imagine de fundal.
5. `05_optiuni_sectiune.png` — opțiunile de secțiune: Hover Overlay, Color, Background Pan,
   Hover Focus.
6. `06_buton_hover_animation.png` — Hover Animation pe un buton.
7. `07_antet_glass_menu_hover.png` — Glass și Menu Hover pe antet.
8. `08_antet_site.png` — pagina derulată, cu antetul din sticlă și Menu Hover › Underline.
9. `09_blocuri_continut_intern.png` — cele cinci blocuri ale modulului în panoul Blocuri.
10. `10_delivery_route.png` — opțiunile blocului Delivery Route.
11. `11_help_box_info_list.png` — Delivery Route, Help Box, Info List și Copy Codes pe site.
12. `12_info_list_optiuni.png` — opțiunile blocului Info List: rânduri și valori.
13. `13_flip_card.png` — Flip Card în editor, cu Back Color.
14. `14_tabs_card_style.png` — blocul Tabs cu Card Style.

Regenerare:

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_website_effects,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

- Explicați diferența dintre grupul **Coloană** și grupul **Bloc** din panou: același set de efecte
  apare pe ambele, iar efectul se mișcă pe elementul pe care a fost ales.
- Subliniați că efectele sunt **opționale și reversibile** (alegeți *Fără* / debifați) și că
  vizitatorii cu „reducerea mișcării" sau pe telefon văd o variantă fără animații.
- *Glass*, *Menu Hover* și *Card Style* sunt cele mai vizibile efecte „de identitate" — capturile
  07 și 08 arată setarea și rezultatul.
- Pentru *Info List*, recomandați clientului să-și seteze o dată valorile reale (pragul de
  livrare gratuită, zilele de retur, programul) și să verifice linkurile *Details* și de politici
  (implicit `/terms`).
