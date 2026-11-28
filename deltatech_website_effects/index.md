# Efecte pentru site (Website Effects)

- **Nume Tehnic:** `deltatech_website_effects`
- **Versiune:** `20.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_effects
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_effects`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă o colecție de efecte vizuale și blocuri gata făcute pentru site-ul web, setate din editorul de site, în opțiunile elementului selectat, sau printr-o clasă CSS într-un șablon QWeb. Nimic nu se schimbă pe site până nu este ales un efect. Efectele se opresc pentru vizitatorii care au cerut mișcare redusă de la sistem, iar înclinarea 3D este dezactivată pe ecrane tactile.

#### 2. Funcționalități Cheie

- **Coloane, carduri și blocuri**: *Hover Effect* (3D Tilt, Lift, Glow, Frame, Holo, Border Reveal, Background Color), imagini din alb-negru în culoare sau zoom, forme (*Price Tag* cu varianta ascuțită, *Accent Card* cu tonuri, *Glass* cu intensitate Light/Medium/Strong) și atenționări (*Pulse*, *Nudge icons*, *Glow Border* în două culori).
- **Secțiuni**: Hover Overlay, Background Pan, Cursor Spotlight, Columns Cascade, Hover Focus, Count Up Numbers (numerele cresc de la zero, valorile reale rămân în pagină), Title Animation (Words Up, Words Blur), Title Shimmer, Aurora și Floating Shape (logo sau Blob, Ring, Arc, Rounded Square, cu poziție, mărime și culoare).
- **Butoane**: Hover Animation (Grow, Shrink, Pulse, Float, Bob, Wobble, Buzz, Push, Shine, Press, Magnetic).
- **Antet**: Glass la lipirea de marginea de sus și Menu Hover (subliniere sau fundal).
- **Tema > Efecte**, la nivel de site: Logo Watermark, Cursor Trail (Glow, Snow, Sparks, Liquid, Tire Tracks, Rolling Tire, Harvest, Tractor), Click Effect separat (Glow, Snow, Sparks, Liquid, Harvest, Bolts & Washers, Skid Mark), Accent Color, Browser Bar Color (Theme, Header, Custom) și Page Transitions. Sezonul efectului Snow se setează în *Website > Configurare > Setări > Website Effects* (implicit 1 decembrie - 28 februarie).
- **Separatoare**: *Draw Line*, linia se desenează la apariția în ecran, de la stânga sau din centru.
- **Blocuri noi** (Inner content, fiecare cu *Round Corners*): *Delivery Route* (vehicul pe un drum punctat de la depozit la ușa clientului, editabil), *Info List* (card cu rânduri pentru livrare, plată, retur, garanție, locker etc., cu valori setabile), *Flip Card* și stil de card pentru file.
- Efectele cu cursorul rămân ușoare: forme desenate o dată și reutilizate, număr limitat de particule, nimic nu rulează când mouse-ul stă.

#### 3. Dependențe

- `website`

#### 4. Componente Cheie

**Modele**

- `website` (extins): setările de efecte la nivel de site (culoarea barei browserului, sezonul Snow ș.a.).
- `res.config.settings` (extins): setările din *Website Effects*.

**Vizualizări**

- Opțiunile de editor (website builder) pentru coloane, carduri, secțiuni, butoane, antet, separatoare și blocurile noi, plus blocul *Efecte* din fila *Tema*.

**Acțiuni Automate / Acțiuni Server**

- Nu are sarcini cron sau acțiuni server.

#### 5. Conexiuni

- [deltatech_website_sale_effects](../deltatech_website_sale_effects/index.md): aduce aceste efecte în paginile eCommerce (magazin, pagină de produs, checkout).
