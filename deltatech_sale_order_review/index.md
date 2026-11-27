# Sale Order Review (localizat la `deltatech_sale_order_review/index.md`)

- **Nume Tehnic:** `deltatech_sale_order_review`
- **Versiune:** `19.0.0.1.9`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_order_review
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_order_review`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul reține comenzile de vânzare care nu sunt sigure de procesat și arată clar de ce, astfel încât operatorul vede dintr-o privire ce trebuie verificat, fără ca nimic să iasă din depozit pe baza unei presupuneri. Odoo poate bloca o comandă, dar nu explică motivul: o ofertă care rămâne ofertă, o livrare care rămâne în așteptare, o notă îngropată într-un chatter pe care nimeni nu-l citește. Modulul atașează fiecărei rețineri un **motiv**, păstrat pe comandă, cu propria stare și cu loc vizibil în lista de comenzi.

#### 2. Funcționalități Cheie

- **Două puncte de blocare (gate-uri)** — *Înainte de confirmare*: comanda rămâne ofertă cât timp motivul e deschis (fereastră de așteptare după plasarea comenzii, mesaj de la client); *Înainte de livrare*: comanda e confirmată (stocul e rezervat), dar livrarea rămâne reținută (ramburs mare, plată cu cardul neîncheiată, adresă incompletă, ridicare personală solicitată pe o comandă online).
- **Două tipuri de motiv** — *Temporar*: se rezolvă singur când condiția dispare (plata se încheie, fereastra de așteptare trece) și escaladează la aprobare manuală după o întârziere configurabilă; *Manual*: așteaptă aprobarea unei persoane din grupul de securitate potrivit, cu istoric al cine/când/pentru ce valoare a aprobat; dacă valoarea se schimbă ulterior (rambursul crește), motivul se redeschide.
- **Reguli configurabile per companie** — fiecare verificare e o regulă cu prag, întârziere și grup de aprobare propriu; regulile livrate acoperă fereastra de așteptare, rambursul, plata online în așteptare, adresa incompletă și ridicarea personală pe comenzi online; alte module pot adăuga reguli proprii cu o singură înregistrare de date și o metodă.
- **Interfața operatorului** — banner pe comandă cu motivele deschise și un buton *Aprobă* per motiv, o etichetă și filtrele *De Revizuit* / *În Așteptare Revizuire* în lista de comenzi, acțiunea *Aprobă Reviziile* pentru o selecție întreagă, plus istoricul complet din butonul inteligent *Revizii*. Butonul *Confirmă* de pe o ofertă reținută deschide lista motivelor în loc să confirme orbește.
- **Coada de lucru** (Vânzări → Comenzi, filtrul **De Revizuit**) — filtrul **În Așteptare Revizuire** arată comenzile care se vor debloca singure; aprobarea în masă se face din *Acțiuni → Aprobă Reviziile*.
- **Configurare reguli** (Vânzări → Configurare → Reguli de Revizuire a Comenzilor) — fiecare regulă are: Gate (Înainte de Confirmare / Înainte de Livrare), Tip (Temporar / Aprobare Manuală), prag valoric, minute de așteptare, întârziere de escaladare, grup de aprobare (gol = orice agent de vânzări; managerii de vânzări sunt impliciți în grupul *Approve held sale orders*) și companie (goală = se aplică peste tot). **Toate regulile sunt inactive după instalare** (de la 19.0.0.1.3): instalarea nu schimbă nimic pe comenzi până când o regulă e activată; bazele existente își păstrează starea regulilor (înregistrările sunt `noupdate`).
- **Ridicare personală** — pe metodele de livrare cu ridicare de către client se bifează *Pickup by Customer* (Inventar → Configurare → Metode de Livrare); metodele Click & Collect sunt recunoscute automat, fără bifă.
- **Reevaluare automată** — acțiunea programată *Sale Order Review: re-evaluate held orders* rulează la fiecare 5 minute și elimină ferestrele de așteptare expirate, escaladând motivele temporare.
- **Integrare pentru fluxuri automate** — alte module (import marketplace, confirmări prin cron) verifică `order._review_can_auto_confirm()` înainte de a confirma; o comandă reținută rămâne ofertă cu motivele vizibile, în loc să eșueze silențios.
- Gândit ca bază pentru conectorii de marketplace (fereastră de așteptare, mesaj de la client, discrepanță de total), suita de curierat (livrări reținute, acțiuni în masă care sar peste comenzile reținute) și modulul de limită de credit.

#### 3. Dependențe

- `sale`
- `delivery`

#### 4. Componente Cheie

Secțiunile 1–2 sunt preluate din `readme/DESCRIPTION.md`, `USAGE.md` și `CONFIGURE.md`, care nu cer explicit detalierea componentelor; analiza codului a fost limitată la lista fișierelor din manifest și din `models/`.

**Modele**

- `sale.order.review.rule`: regula de verificare (gate, tip, prag, minute, întârziere de escaladare, grup de aprobare, companie).
- `sale.order.review.reason`: motivul reținerii, păstrat pe comandă, cu stare proprie și istoric de aprobare.
- `sale.order.review.approve.wizard` (wizard): aprobarea motivelor, pe o comandă sau pe o selecție (*Aprobă Reviziile*).
- `sale.order` (extins): evaluarea regulilor, banner, filtre și `_review_can_auto_confirm()` pentru fluxurile automate.
- `sale.order.line` (extins): reevaluează comanda la crearea, ștergerea sau modificarea liniilor (produs, cantitate, preț, discount, taxe).
- `payment.transaction` (extins): reevaluează comenzile la orice schimbare de stare a tranzacției (plată încheiată, expirată sau eșuată).
- `delivery.carrier` (extins): bifa *Pickup by Customer*.

**Vizualizări**

- `views/review_rule_views.xml`: configurarea regulilor (*Vânzări → Configurare → Reguli de Revizuire a Comenzilor*).
- `views/review_reason_views.xml`: lista și formularul motivelor (butonul inteligent *Revizii*).
- `views/sale_order_views.xml`: bannerul motivelor, eticheta și filtrele *De Revizuit* / *În Așteptare Revizuire* pe comenzi.
- `views/delivery_carrier_views.xml`: bifa *Pickup by Customer* pe metodele de livrare.
- `wizard/review_approve_wizard_views.xml`: formularul wizardului de aprobare; stilul bannerului e în `static/src/scss/review_banner.scss`.

**Acțiuni Automate / Acțiuni Server**

- `Sale Order Review: re-evaluate held orders` (`data/ir_cron_data.xml`): acțiune programată la fiecare 5 minute; elimină ferestrele de așteptare expirate și escaladează motivele temporare.
- `data/review_rule_data.xml`: regulile livrate (fereastră de așteptare, ramburs mare, plată online în așteptare, adresă incompletă, ridicare personală pe comandă online), toate inactive.

#### 5. Conexiuni

- [terrabit_partner_credit_limit](../terrabit_partner_credit_limit/index.md): modulul de limită de credit pe partener se bazează pe motivele de reținere definite aici.
- [deltatech_delivery_review](../deltatech_delivery_review/index.md): aliniază regula *Ramburs mare* cu suma de pe AWB și numește motivul în dialogurile de curierat.
- [deltatech_delivery_status_review](../deltatech_delivery_status_review/index.md): amână efectiv livrările comenzilor reținute pe poarta *Înainte de livrare*.
- [deltatech_marketplace_review](../deltatech_marketplace_review/index.md): conectorii de marketplace folosesc regulile (fereastră de așteptare, mesaj client, discrepanță de total) definite aici.
