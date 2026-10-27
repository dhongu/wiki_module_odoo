# Website Effects (localizat la `deltatech_website_effects/index.md`)

- **Nume Tehnic:** `deltatech_website_effects`
- **Versiune:** `19.0.1.2.24`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_website_effects
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_effects`
- **Ultima Ingestie:** `2026-10-18`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă o colecție de efecte vizuale și blocuri gata făcute pentru website. Efectele se aleg din editorul de website, în opțiunile elementului selectat, sau printr-o clasă CSS într-un șablon QWeb. Nimic nu se schimbă pe site până când nu se alege un efect. Efectele se opresc pentru vizitatorii care au cerut sistemului „mișcare redusă”, iar înclinarea 3D e dezactivată pe ecranele tactile.

#### 2. Funcționalități Cheie

- **Coloane, carduri și blocuri, efect la hover** (și pe blocurile interioare desenate ca o casetă: Alert, Quote, Text Highlight, Help Box, Info List, Delivery Route, Copy Codes): 3D Tilt (înclinare spre cursor, cu lumină care urmărește mouse-ul; culoarea se alege la *Highlight*), Lift, Glow, Frame, Holo, Border Reveal și Background Color (cu culoare aleasă în editor).
- **Imagini:** trecere din alb-negru în culoare sau zoom lent.
- **Forme:** Price Tag (etichetă cu orificiu, variantă cu vârf), Accent Card (bară colorată sus și fundal în tonul cardului, cu 8 tonuri) și Glass (panou mat translucid în stil iPhone, cu *Blur* Light/Medium/Strong; necesită un fundal colorat sau o imagine în spate).
- **Atenție:** Pulse (halou care „respiră” de trei ori la încărcare) și Nudge icons (iconițele se mișcă scurt la hover).
- **Secțiuni:** Hover Overlay, Background Pan, Hover Focus.
- **Butoane:** Hover Animation (Grow, Shrink, Pulse, Float, Bob, Wobble, Buzz, Push, Shine, Press).
- **Antet:** Glass (bară mată după ce antetul se fixează sus) și Menu Hover (subliniere sau fundal care se umple).
- **Blocuri noi în *Inner content*:** Delivery Route (vehicul pe drum între depozit și client; vehicul, viteză, culoare configurabile), Info List (livrare, plată, retururi, ridicare, cu sumă/greutate/zile/program configurabile), Help Box (întrebare, răspuns, WhatsApp, formular de contact, telefon), Copy Codes (coduri copiate la click sau Enter; orice element cu clasa `tb_fx_copy`) și Flip Card (față/spate, cu *Back Color* simplă sau gradient).
- **Blocul Tabs din Odoo** primește opțiunea *Card Style*.
- **Utilizare în QWeb:** clase precum `tb_fx_tilt`, `tb_fx_lift`, `tb_fx_glow`, `tb_fx_price_tag`, `tb_fx_accent_card` (+ `tb_fx_tone_<ton>`), `tb_fx_pulse`, `tb_fx_copy`, `tb_fx_tabs_card`, `tb_fx_glass`, `tb_fx_nudge`.
- Fluxul pas-cu-pas, cu capturi, e în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește modele Python; funcționează prin vizualizări QWeb, SCSS și JavaScript.

**Vizualizări**

- `views/snippets/snippets.xml`: înregistrează blocurile în categoria *Inner content*.
- `views/snippets/s_tb_delivery_route.xml`, `s_tb_help_box.xml`, `s_tb_info_list.xml`, `s_tb_codes.xml`, `s_tb_flip_card.xml`: șabloanele blocurilor.
- `views/header.xml`: opțiunile pentru antet.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- Nicio conexiune funcțională cu alte module wiki; modulul extinde doar editorul `website`.
