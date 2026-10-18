# Website Effects (localizat la `deltatech_website_effects/index.md`)

- **Nume Tehnic:** `deltatech_website_effects`
- **Versiune:** `19.0.1.2.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_effects
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_effects`
- **Ultima Ingestie:** `2026-10-18`

#### 1. Sumar

Modulul adaugă pe site-ul web o colecție de efecte vizuale și de blocuri gata făcute, care fac magazinul online mai atractiv fără intervenție de programator. Efectele se aleg din editorul de website, în opțiunile elementului selectat (sau cu o clasă CSS într-un șablon QWeb), iar pe site nu se schimbă nimic până când nu se alege un efect. Efectele se opresc pentru vizitatorii care au cerut sistemului „mișcare redusă”, iar înclinarea 3D este dezactivată pe ecranele tactile.

#### 2. Funcționalități Cheie

**Coloane și carduri**

- **Hover Effect**: 3D Tilt (înclinare spre cursor, cu o lumină care urmărește mouse-ul; culoarea se alege la *Highlight*), Lift, Glow, Frame, Holo, Border Reveal (bandă colorată pe stânga) și Background Color (fundal care virează spre o culoare aleasă).
- **Imagini**: trecere de la alb-negru la color sau zoom lent.
- **Shape**:
  - *Price Tag*: etichetă de preț cu orificiu, cu variantă „pointed”; se leagănă la hover.
  - *Accent Card*: bară colorată sus și fundal în tonul cardului (culoarea temei sau unul din 8 tonuri: green, blue, amber, gold, red, olive, slate, purple); împreună cu 3D Tilt formează carduri de categorie.
  - *Glass*: panou mat în stil iPhone, cu **Blur** Light / Medium / Strong; necesită ceva colorat în spate (imagine sau gradient).
- **Attention**: Pulse (halou care „respiră” de trei ori la încărcarea paginii) și Nudge icons (iconițele se mișcă scurt la hover).

**Secțiuni**

- Hover Overlay (strat de culoare peste imaginea de fundal), Background Pan (imaginea de fundal alunecă lent) și Hover Focus (celelalte coloane se estompează la hover pe una).

**Butoane**

- Hover Animation: Grow, Shrink, Pulse, Float, Bob, Wobble, Buzz, Push, Shine sau Press.

**Header**

- **Glass**: după ce header-ul rămâne lipit sus, pagina trece pe sub o bară mată (se activează din opțiunile header-ului, în modul de editare).
- **Menu Hover**: subliniere care crește sau fundal care se umple la elementele de meniu.

**Blocuri noi (grupul „Inner content”)**, fiecare cu **Round Corners** propriu:

- **Delivery Route**: un vehicul (camion, cărucior, mașină, motocicletă, bicicletă, avion, vapor, rachetă) parcurge un drum punctat de la depozit la ușa clientului; etapele și iconițele sunt editabile, iar vehiculul, viteza și culoarea se setează în opțiuni.
- **Info List**: card cu titlu și link *Details*, rânduri cu iconiță (livrare, livrare gratuită, plată, retur, ridicare personală) și linkuri de politici; casete bifabile afișează/ascund titlul, rândurile și linkurile, iar câmpuri setează suma și greutatea pentru livrare gratuită, zilele de retur și programul.
- **Help Box**: card cu întrebare (ex. „Nu ești sigur că e piesa potrivită?”), răspuns scurt și modalități de ajutor: buton WhatsApp, buton către formularul de contact și număr de telefon.
- **Copy Codes**: listă etichetată de coduri (numere de piesă alternative, referințe) afișate ca „chips”; click sau Enter copiază codul, iar chip-ul devine verde cu bifă. Orice element cu clasa `tb_fx_copy` se comportă la fel (ex. în șablonul paginii de produs).
- **Flip Card**: card cu față și verso care se întoarce la hover sau la focus de la tastatură; **Back Color** poate fi culoare unică sau gradient; în modul de editare ambele fețe sunt afișate una sub alta.
- Blocul **Tabs** din Odoo primește opțiunea **Card Style** (blocul în card, bara de tab-uri pe un antet discret, tab-ul activ ridicat pe o plăcuță albă cu subliniere de accent).

**În șablon QWeb**: se adaugă clasa efectului pe element, de ex. `tb_fx_tilt`, `tb_fx_lift`, `tb_fx_glow`, `tb_fx_price_tag` (+ `tb_fx_price_tag_pointed`), `tb_fx_accent_card` (+ `tb_fx_tone_<ton>`), `tb_fx_pulse`, `tb_fx_copy`, `tb_fx_tabs_card` (pe `.s_tabs`), `tb_fx_glass` (+ `tb_fx_glass_light` / `tb_fx_glass_strong`), `tb_fx_nudge`.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele Python; este exclusiv front-end (SCSS, interacțiuni JS, opțiuni de editor, șabloane QWeb).

**Vizualizări**

- `views/snippets/snippets.xml` (`snippets`, moștenește `website.snippets`): înregistrează blocurile în „Inner content”.
- `views/snippets/s_tb_delivery_route.xml`, `s_tb_info_list.xml`, `s_tb_help_box.xml`, `s_tb_codes.xml`, `s_tb_flip_card.xml`: șabloanele blocurilor noi.
- `views/header.xml`: variante de header activabile din editor (`header_glass`, plus cele pentru Menu Hover subliniere / umplere), care adaugă clasele `tb_fx_glass_header`, `tb_fx_menu_underline`, `tb_fx_menu_fill` pe layout.
- `static/src/website_builder/`: opțiunile de editor (`effects_option.xml`, `header_glass_option.xml`, `tabs_card_option.xml`) și pluginul `EffectsOptionPlugin` (`effects_option_plugin.esm.js`), înregistrat în `website-plugins`.
- `static/src/interactions/`: `tilt.esm.js` (3D Tilt, activ doar cu cursor fin și fără „mișcare redusă”) și `copy.esm.js` (Copy Codes).

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nu există legături funcționale verificate în cod cu alte module; modulul depinde doar de `website`.
