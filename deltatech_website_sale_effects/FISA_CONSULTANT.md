# Fișă Modul: Efecte vizuale pentru magazinul online

**Modul:** `deltatech_website_sale_effects`
**Utilizator principal:** Consultant eCommerce / designer al site-ului (rolul Website › Editor și Designer sau administrator)
**Prioritate:** 🟢 Scăzută (aspectul magazinului; nu atinge prețuri, comenzi, stocuri sau contabilitate)

---

## 1. Scop business

Modulul aduce efectele din *Website Effects* (`deltatech_website_effects`) pe paginile magazinului
online, ca opțiuni ale editorului website: bara laterală din /shop în carduri (categorii cu număr de
subcategorii, filtre), carduri de produs animate cu efecte noi la hover (Înclinare 3D, Ridicare,
Strălucire, Holografic),
o bară de pași animată pe checkout, cu un vehicul care merge din pas în pas, și casete cu colțuri
și efecte la hover pentru adrese și metode, plus o pagină de produs mai aerisită: termenii în
casetă (*Listă de informații*), traseul livrării (*Traseu livrare*), colțuri comune pentru casete, descrierea
mutată sub imagini și secțiunile de jos (descriere, specificații, opinii) grupate în taburi. Totul se pornește din editor, fără cod; până nu
porniți o opțiune, magazinul arată ca înainte.

## 2. Bază legală și context

Nu există o bază legală: modulul ține de aspectul magazinului. Context operațional:

- opțiunile se salvează **per website** (ca și celelalte opțiuni ale paginilor de magazin) și se
  aplică pe toate paginile de același tip: toate paginile /shop, toate paginile de checkout, toate
  paginile de produs;
- conținutul casetelor de pe pagina de produs (*Listă de informații*, *Traseu livrare*) este **comun tuturor
  produselor**: se editează o singură dată;
- animațiile respectă setarea „reducerea mișcării" a vizitatorului; *Înclinare 3D* este oprită pe
  ecranele tactile.

## 3. Utilizatori și roluri

- **Consultant / designer website** — pornește opțiunile din editor (în **Setări › Utilizatori**,
  la *Website*, rolul **Editor și Designer**).
- **Cumpărătorul** — vede magazinul, checkout-ul și pagina de produs cu efectele alese.

Roluri recomandate la testare: un utilizator cu rolul *Editor și Designer* pentru editare și o fereastră
privată (vizitator anonim) pentru verificarea magazinului și a checkout-ului, inclusiv pe telefon.

## 4. Conturi și date implicate

Modulul nu are conturi contabile, modele sau câmpuri noi. Opțiunile sunt vederi QWeb activate per
website, iar efectul de hover al cardurilor de produs se salvează în clasele de design ale
magazinului (*Products Design*), alături de celelalte opțiuni native.

Date minime pentru demo (datele demo `website_sale` sunt suficiente): categorii eCommerce cu
subcategorii și produse publicate, atribute de produs (pentru filtre), un produs cu descriere
lungă (pentru *Descriere sub imagine*), o metodă de livrare și o adresă pe clientul de test
(pentru paginile de checkout).

## 5. Configurare inițială

1. Instalați modulul `deltatech_website_sale_effects` (depinde de `website_sale` și de
   `deltatech_website_effects`, care se instalează automat).
2. Nu există setări de modul: opțiunile apar în editor, în panoul **Stil** al paginii de magazin,
   al paginii de checkout și al paginii de produs.

> Modulul are traducere în română (`i18n/ro.po`): în interfața RO etichetele și valorile opțiunilor,
> ca și titlurile taburilor de pe pagina de produs, apar în română. Fișa folosește etichetele din
> interfața RO; eticheta originală (engleză) este dată în tabele, între paranteze. Etichetele
> native Odoo netraduse (*Purchase Style*, *Terms and Conditions*) apar așa cum le arată Odoo.
3. Pentru cardul de categorii, magazinul trebuie să afișeze **Categorii** în **Bară laterală**
   (nu *Sus*); pentru cardul de filtre, **Filtre** în **Bară laterală**.
4. Opțional, instalați *eCommerce Category Icons* (`deltatech_website_category_icon`): iconițele
   categoriilor apar atunci pe plăcuțe în cardul de categorii.

## 6. Flux de utilizare

### Pasul 1 — Opțiunile paginii /shop

Deschideți **Magazin** (/shop), apăsați **Editează** și dați clic pe grila de produse. În panoul
paginii de magazin, modulul adaugă:

| Opțiune | Unde apare | Ce face |
|---|---|---|
| **Card categorii** (*Categories Card*) | sub *Categorii* (doar cu *Bară laterală*) | lista de categorii într-un card alb: titlu cu iconiță, *Toate produsele* ca rând „înapoi", categoria curentă ca pastilă plină în culoarea temei, rânduri evidențiate la hover, săgeți pentru lista restrânsă |
| ↳ **Număr de subcategorii** (*Subcategory Count*) | sub *Card categorii* | afișează numărul de subcategorii lângă numele categoriilor care au (implicit oprit), cu lista restrânsă sau nu |
| **Zecimale mici** (*Small Decimals*) | înainte de *Filtre* | zecimalele prețului mai mici, pe linia de bază, și unitatea de măsură lângă preț (*$ 750,00/buc.* în captura 02); în editor se vede doar unitatea, zecimalele mici apar pe pagina salvată; urmează prețul și la schimbarea variantei sau a cantității. Aceeași opțiune există și pe pagina de produs (pasul 6), cu setare separată |
| **Carduri de produs animate** (*Animated Product Cards*) | înainte de *Filtre* | dalele de produs devin carduri cu chenar și umbră ușoară, cu raza din *Products Design › Rotunjime*; butonul de coș „sare" la hover |
| **Card filtre** (*Filters Card*) | sub *Etichete* (doar cu *Filtre* în *Bară laterală*) | filtrele de atribute și de preț într-un card, în stilul cardului de categorii |
| **Colțuri bară laterală** (*Sidebar Corners*) | când unul din carduri e pornit | colțurile ambelor carduri: *Mari* (implicit), *Medii*, *Mici*, *Drepte*; rândurile din interior le urmează |

![Opțiunile paginii /shop: Card categorii, Număr de subcategorii, Zecimale mici, Carduri de produs animate, Card filtre, Colțuri bară laterală](screenshots/01_shop_optiuni.png)

### Pasul 2 — Magazinul văzut de cumpărător

Salvați pagina. În bara laterală, categoriile și filtrele stau în două carduri cu aceleași colțuri;
*Toate produsele* este rândul de întoarcere, iar numărul din dreapta fiecărei categorii arată câte
subcategorii are. Produsele sunt carduri cu chenar și umbră; cu *Înclinare 3D* aleasă în *Products
Design* (pasul 3), cardul de sub mouse se înclină spre cursor (în captură, primul produs). Cu
*Zecimale mici*, prețurile au zecimalele mai mici și unitatea de măsură alăturată (*/buc.*).

Numărul de subcategorii diferă după cine se uită: un utilizator intern vede **toate**
subcategoriile, un vizitator doar pe cele care au produse publicate.

![Magazinul salvat: cardul de categorii cu numărul de subcategorii, cardul de filtre și cardurile de produs animate](screenshots/02_shop_magazin.png)

### Pasul 3 — Products Design › Hover Effect

Efectul de hover al cardurilor de produs se alege din panoul nativ **Products Design** (butonul cu
pensulă de lângă *Products Design*), rândul **Hover Effect** (*Efect la trecerea mouse-ului*) din
grupul *General*. Pe lângă efectele native (*Fundal*, *Zoom fundal* etc.), modulul adaugă
**Înclinare 3D**, **Ridicare**, **Strălucire** și **Holografic**, cu același comportament ca în
*Website Effects*. Efectul se salvează
cu celelalte opțiuni de design ale magazinului și funcționează pe orice design de produs
(miniaturi, carduri, listă), cu sau fără *Carduri de produs animate*.

![Products Design deschis: lista Efect la trecerea mouse-ului cu Înclinare 3D, Ridicare, Strălucire, Holografic adăugate de modul](screenshots/03_products_design_hover.png)

### Pasul 4 — Checkout: pașii animați și casetele

Adăugați un produs în coș, deschideți coșul (/shop/cart), apăsați **Editează** și dați clic pe
bara de pași. În panoul *Pagini de finalizare comandă*, sub *Pas suplimentar*, apar:

- **Pași animați** (*Animated Steps*) — înlocuiește bara de pași a checkout-ului cu un drum punctat
  între pași numerotați;
- ↳ **Vehicul** (*Vehicle*) — vehiculul de pe drum: Camion (implicit), Coș de cumpărături, Mașină,
  Motocicletă, Bicicletă, Avion, Navă, Rachetă. Rândul apare indentat imediat sub *Pași animați*,
  doar cu acesta pornit;
- **Colțuri casete** (*Box Corners*) — colțurile casetelor de pe checkout (rezumatul comenzii,
  adresele, metodele de livrare și de plată): *Temă* (implicit), *Mici*, *Medii*, *Mari*;
- **Casete la trecerea mouse-ului** (*Box Hover*) — reacția adreselor și a metodelor la mouse:
  *Fără*, *Ridicare*, *Strălucire*, *Cadru*.

Cu *Colțuri casete* sau *Casete la trecerea mouse-ului* pornite, metodele de livrare și de plată devin casete separate, în
locul listei lipite. Setările se aplică pe toate paginile de checkout ale website-ului (coș,
adresă, plată, confirmare).

![Coșul în editor: Pași animați, Vehicul = Camion, Colțuri casete = Medii, Casete la trecerea mouse-ului = Ridicare](screenshots/04_checkout_optiuni.png)

### Pasul 5 — Checkout-ul văzut de cumpărător

Pe fiecare pagină de checkout, vehiculul pleacă de la pasul anterior și se oprește la pasul curent,
iar drumul din spatele lui se umple cu culoarea temei. Pașii parcurși sunt plini și **rămân
clicabili** (cumpărătorul se poate întoarce la coș), pasul curent este evidențiat. Pentru
vizitatorii cu „reducerea mișcării", bara rămâne nemișcată, în poziția finală. Metoda de livrare,
adresa și rezumatul comenzii sunt casete cu colțurile alese (*Medii* în captură).

![Pasul Adresă: vehiculul a ajuns la pasul 2, drumul până la el e plin; casetele au colțuri Medii](screenshots/05_checkout_pasi.png)

### Pasul 6 — Opțiunile paginii de produs

Deschideți o pagină de produs, apăsați **Editează** și dați clic pe zona de detalii a produsului.
În panoul paginii de produs, modulul adaugă:

| Opțiune | Unde apare | Ce face |
|---|---|---|
| **Colțuri casete** (*Box Corners*) | sub *Purchase Style* | o singură rază pentru casetele coloanei de cumpărare: caseta de preț (*Purchase Style* = *În cutie*), termenii în casetă și traseul livrării — *Temă* (raza casetei de preț), *Mici*, *Medii*, *Mari*; cu termenii în casetă sau cu traseul sub ea, caseta de preț ia lățimea secțiunii, ca toate casetele să fie aliniate |
| **Terms and Conditions › Stil** (*Style*) | sub *Terms and Conditions*, doar dacă termenii sunt afișați | *Implicit* (cele trei rânduri mici native) sau *În cutie* (*Boxed*): blocul *Listă de informații* — titlu cu link *Detalii*, rânduri cu iconițe, linkuri de politici |
| **Zecimale mici** (*Small Decimals*) | înainte de *Traseu livrare* | ca pe /shop: zecimalele prețului mai mici și unitatea de măsură lângă preț, pe pagina de produs; în editor prețul rămâne nescindat, efectul se vede pe pagina salvată |
| **Traseu livrare** (*Delivery Route*) | înainte de *Opinii* | blocul *Traseu livrare* sub termeni: vehiculul care merge de la depozit la client |
| **Taburi jos** (*Bottom Tabs*) | după *Opinii* | descrierea, specificațiile și opiniile clienților de la baza paginii devin taburi, într-un card; primesc tab doar secțiunile prezente, iar cu mai puțin de două secțiuni nu se schimbă nimic; în editor secțiunile rămân desfăcute, ca să le puteți edita |
| **Descriere sub imagine** (*Description under Image*) | după *Bară de căutare* | descrierea lungă a produsului urcă în coloana imaginilor, sub poze, în timp ce coloana de cumpărare rămâne în vedere |

Casetele *Listă de informații* și *Traseu livrare* se editează direct în pagină (texte, iconițe,
linkuri; pentru *Traseu livrare* și vehiculul, viteza, culoarea și colțurile) și sunt **aceleași pe
toate produsele**. Textele lor implicite sunt exemple: rescrieți-le o dată, la prima configurare.
Caseta *Listă de informații* are și opțiunile de rânduri și valori ale blocului (pragul de livrare gratuită,
zilele de retur, programul — vezi fișa `deltatech_website_effects`).

![Pagina de produs în editor: Purchase Style, Colțuri casete, Terms and Conditions › Stil = În cutie, Zecimale mici, Traseu livrare, Taburi jos, Descriere sub imagine](screenshots/06_produs_optiuni.png)

### Pasul 7 — Pagina de produs văzută de cumpărător

Salvați. În coloana din dreapta, caseta de preț, caseta *Livrare și retur* (*Listă de informații*)
și traseul livrării au aceleași colțuri (*Colțuri casete* = *Medii*) și aceeași lățime, iar prețul
are zecimalele mici și unitatea alăturată (*Zecimale mici*: *$ 750,00/buc.*). În coloana din
stânga, descrierea produsului (*Ergonomic*, *Făcut manual local*) stă sub imagini, așa că pagina
nu mai are un spațiu gol sub poze. Pe telefon coloanele se așază una sub alta, iar descrierea vine
după blocul de cumpărare, ca pe pagina standard. Jos, *Taburi jos* arată specificațiile și
opiniile clienților ca taburi (*Specificații*, *Recenziile clienților*); descrierea nu primește tab, pentru că este deja sub imagini.

![Pagina de produs salvată: casetele aliniate, descrierea sub imagini și taburile Specificații / Recenziile clienților jos](screenshots/07_produs_pagina.png)

### Note de monografie și raportare

Modulul nu generează note contabile, documente sau rapoarte: opțiunile sunt vederi QWeb activate
per website, iar conținutul casetelor de pe pagina de produs se salvează în zone editabile comune.

### Cum se combină opțiunile

- **Card categorii** și **Card filtre** sunt independente; **Colțuri bară laterală** apare când cel
  puțin unul e pornit și se aplică amândurora.
- **Carduri de produs animate** dă forma cardului (chenar, umbră, buton care sare), iar
  **Products Design › Efect la trecerea mouse-ului** dă mișcarea; se pot folosi separat sau împreună. Raza
  colțurilor vine din **Products Design › Rotunjime**.
- Pe pagina de produs, **Colțuri casete** are efect vizibil doar cu *Purchase Style* = *În cutie*
  sau cu *Terms and Conditions › Stil* = *În cutie* / *Traseu livrare*; dacă *Traseu livrare* are
  propriile *Colțuri rotunde* setate în editor, acestea au prioritate.
- *Terms and Conditions › Stil* apare doar când opțiunea nativă *Terms and Conditions* este pornită.
- **Taburi jos** ia descrierea doar dacă nu e mutată sub imagini (*Descriere sub imagine*);
  opiniile apar ca tab doar cu opțiunea nativă *Opinii* pornită.
- Pe checkout, **Colțuri casete** și **Casete la trecerea mouse-ului** sunt independente de **Pași
  animați**.

## 7. Legături cu alte module / declarații

| Modul / proces | Rol în flux | Tip legătură |
|---|---|---|
| `website_sale` | paginile /shop, checkout și produs, panoul *Products Design* | dependență (manifest) |
| `deltatech_website_effects` | efectele Înclinare 3D, Ridicare, Strălucire, Holografic și blocurile *Listă de informații*, *Traseu livrare* folosite pe pagina de produs | dependență (manifest) |
| `deltatech_website_category_icon` | iconițele categoriilor, afișate pe plăcuțe în *Card categorii* | opțional (dacă e instalat) |

Ce este automat: poziția vehiculului pe checkout după pasul curent, numărul de subcategorii,
alinierea casetelor pe pagina de produs, alegerea secțiunilor care devin taburi (*Taburi jos*),
oprirea animațiilor pentru „reducerea mișcării".
Ce rămâne manual: pornirea opțiunilor în editor, textele casetelor *Listă de informații* și *Traseu
livrare* (exemple de rescris), alegerea vehiculului și a colțurilor.

## 8. Verificări pentru consultant

- [ ] Cu toate opțiunile oprite, /shop, checkout-ul și pagina de produs arată ca înainte de instalare.
- [ ] Interfața în română: etichetele și valorile opțiunilor modulului sunt în română.
- [ ] *Card categorii* apare în panou doar cu *Categorii* în *Bară laterală*; *Card filtre* doar
      cu *Filtre* în *Bară laterală*.
- [ ] Cu *Număr de subcategorii* pornit, numărul apare pe rândul categoriei, lângă nume, atât cu
      *Restrânge categoria recursiv* pornit, cât și oprit; ca vizitator anonim, se numără doar
      subcategoriile cu produse publicate.
- [ ] *Colțuri bară laterală* = *Drepte* face ambele carduri cu colțuri drepte.
- [ ] *Products Design › Efect la trecerea mouse-ului* = *Înclinare 3D*: cardul de produs se
      înclină la mouse pe calculator și rămâne nemișcat pe telefon.
- [ ] *Pași animați*: pe /shop/checkout vehiculul ajunge la pasul 2; pe pagina de plată, la
      pasul 3; clic pe pasul 1 duce înapoi în coș.
- [ ] În panou, *Vehicul* stă imediat sub *Pași animați*; schimbat în *Rachetă* se vede pe toate
      paginile de checkout.
- [ ] *Colțuri casete* = *Mari* pe checkout rotunjește rezumatul, adresele și metodele; cu *Casete
      la trecerea mouse-ului* = *Ridicare*, adresa și metoda de livrare se ridică la mouse.
- [ ] *Terms and Conditions › Stil* = *În cutie*: textul editat în caseta *Listă de informații*
      pe un produs apare identic pe alt produs.
- [ ] *Colțuri casete* = *Mari*: caseta de preț, *Listă de informații* și *Traseu livrare* au
      aceeași rază și aceeași lățime.
- [ ] *Zecimale mici* pe /shop: zecimalele prețului sunt mai mici și apare unitatea de măsură;
      pe pagina de produs, setarea separată face același lucru și urmează prețul la schimbarea
      variantei.
- [ ] *Descriere sub imagine*: pe desktop descrierea stă sub imagini; pe telefon, după blocul de
      cumpărare.
- [ ] *Taburi jos* cu *Opinii* pornit: jos apar taburile *Specificații* și *Recenziile clienților*;
      clic pe numărul de recenzii de sus deschide tabul de opinii.

## 9. Mesaje de eroare frecvente

| Mesaj / simptom | Cauză probabilă | Remediere |
|---|---|---|
| *Card categorii* nu apare în panou | categoriile sunt afișate *Sus*, nu în *Bară laterală* | setați *Categorii* = *Bară laterală* |
| *Terms and Conditions › Stil* nu apare | opțiunea nativă *Terms and Conditions* este oprită | porniți *Terms and Conditions* |
| *Colțuri casete* nu schimbă nimic | nu există casete în coloana de cumpărare | alegeți *Purchase Style* = *În cutie* sau porniți termenii în casetă / *Traseu livrare* |
| *Taburi jos* pornit, dar jos nu apar taburi | pe pagină sunt mai puțin de două secțiuni (descrierea e sub imagini, *Opinii* e oprit sau produsul nu are specificații) | porniți *Opinii* sau opriți *Descriere sub imagine* |
| Taburile nu apar în editor | comportament voit: în modul de editare secțiunile rămân desfăcute | verificați pe pagina salvată |
| Textele casetelor de pe pagina de produs nu se potrivesc magazinului | textele implicite ale blocurilor *Listă de informații* și *Traseu livrare* sunt exemple | editați-le o dată în pagină; se aplică pe toate produsele |
| Cardul de produs nu se înclină | ecran tactil sau „reducerea mișcării" activă la vizitator | comportament voit |

## 10. Capturi de ecran

Capturile (`readme/screenshots/`) sunt generate automat din `tests/test_screenshots.py` (mixinul
`ScreenshotCase` din `l10n_ro_doc_screenshots`, import defensiv), cu interfața în română, pe
produsele demo ale magazinului. Testul pornește opțiunile modulului, pune un produs în coș și
fotografiază site-ul și editorul, cu rândurile modulului evidențiate:

1. `01_shop_optiuni.png` — opțiunile paginii /shop: Card categorii, Număr de subcategorii,
   Zecimale mici, Carduri de produs animate, Card filtre, Colțuri bară laterală.
2. `02_shop_magazin.png` — magazinul salvat, cu cardurile din bara laterală și cardurile de produs.
3. `03_products_design_hover.png` — Products Design › Efect la trecerea mouse-ului cu Înclinare 3D,
   Ridicare, Strălucire, Holografic.
4. `04_checkout_optiuni.png` — coșul în editor: Pași animați, Vehicul, Colțuri casete, Casete la
   trecerea mouse-ului.
5. `05_checkout_pasi.png` — bara de pași animată și casetele pe pasul Adresă.
6. `06_produs_optiuni.png` — opțiunile paginii de produs: Colțuri casete, Terms and Conditions ›
   Stil, Zecimale mici, Traseu livrare, Taburi jos, Descriere sub imagine.
7. `07_produs_pagina.png` — pagina de produs salvată: casetele aliniate, descrierea sub imagini,
   taburile de jos.

Regenerare (produsele, categoriile și atributele vin din datele demo `website_sale`):

```bash
./odoo/odoo-bin -c odoo.conf -d <db> -i deltatech_website_sale_effects,l10n_ro_doc_screenshots \
    --test-tags=fise_screenshots --stop-after-init
```

## 11. Observații pentru manual

- Insistați pe faptul că opțiunile sunt **per website și per tip de pagină**: o setare făcută pe un
  produs se vede pe toate produsele, iar casetele *Listă de informații* / *Traseu livrare* sunt
  comune.
- Înainte de a porni *Zecimale mici*, verificați denumirea unităților de măsură: ea apare lângă
  preț (*/buc.*), deci trebuie să fie scurtă și în limba clientului.
- Recomandați ca, la prima configurare, consultantul să rescrie textele casetelor de pe pagina de
  produs (exemple generice) și să verifice linkurile *Detalii* / politicile (implicit `/terms`).
- *Număr de subcategorii* merge cu lista de categorii restrânsă sau nerestrânsă (*Restrânge
  categoria recursiv*): în ambele cazuri numărul stă pe rândul categoriei.
- *Taburi jos* și *Descriere sub imagine* se completează: cu descrierea sub imagini, taburile de
  jos conțin doar specificațiile și opiniile; fără *Descriere sub imagine*, descrierea devine
  primul tab.
