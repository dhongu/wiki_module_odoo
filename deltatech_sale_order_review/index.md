# Sale Order Review (localizat la `deltatech_sale_order_review/index.md`)

- **Nume Tehnic:** `deltatech_sale_order_review`
- **Versiune:** `19.0.0.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_order_review
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_order_review`
- **Ultima Ingestie:** `2026-09-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul reține comenzile de vânzare care nu sunt sigure de procesat și arată clar de ce, astfel încât operatorul vede dintr-o privire ce trebuie verificat, fără ca nimic să iasă din depozit pe baza unei presupuneri. Odoo poate bloca o comandă, dar nu explică motivul: o ofertă care rămâne ofertă, o livrare care rămâne în așteptare, o notă îngropată într-un chatter pe care nimeni nu-l citește. Modulul atașează fiecărei rețineri un **motiv**, păstrat pe comandă, cu propria stare și cu loc vizibil în lista de comenzi.

#### 2. Funcționalități Cheie

- **Două puncte de blocare (gate-uri)** — *Înainte de confirmare*: comanda rămâne ofertă cât timp motivul e deschis (fereastră de așteptare după plasarea comenzii, mesaj de la client); *Înainte de livrare*: comanda e confirmată (stocul e rezervat), dar livrarea rămâne reținută (ramburs mare, plată cu cardul neîncheiată, adresă incompletă, ridicare personală solicitată pe o comandă online).
- **Două tipuri de motiv** — *Temporar*: se rezolvă singur când condiția dispare (plata se încheie, fereastra de așteptare trece) și escaladează la aprobare manuală după o întârziere configurabilă; *Manual*: așteaptă aprobarea unei persoane din grupul de securitate potrivit, cu istoric al cine/când/pentru ce valoare a aprobat; dacă valoarea se schimbă ulterior (rambursul crește), motivul se redeschide.
- **Reguli configurabile per companie** — fiecare verificare e o regulă cu prag, întârziere și grup de aprobare propriu; regulile livrate acoperă fereastra de așteptare, rambursul, plata online în așteptare, adresa incompletă și ridicarea personală pe comenzi online; alte module pot adăuga reguli proprii cu o singură înregistrare de date și o metodă.
- **Interfața operatorului** — banner pe comandă cu motivele deschise și un buton *Aprobă* per motiv, o etichetă și filtrele *De Revizuit* / *În Așteptare Revizuire* în lista de comenzi, acțiunea *Aprobă Reviziile* pentru o selecție întreagă, plus istoricul complet din butonul inteligent *Revizii*. Butonul *Confirmă* de pe o ofertă reținută deschide lista motivelor în loc să confirme orbește.
- **Coada de lucru** (Vânzări → Comenzi, filtrul **De Revizuit**) — filtrul **În Așteptare Revizuire** arată comenzile care se vor debloca singure; aprobarea în masă se face din *Acțiuni → Aprobă Reviziile*.
- **Configurare reguli** (Vânzări → Configurare → Reguli de Revizuire a Comenzilor) — fiecare regulă are: Gate (Înainte de Confirmare / Înainte de Livrare), Tip (Temporar / Aprobare Manuală), prag valoric, minute de așteptare, întârziere de escaladare, grup de aprobare (gol = orice agent de vânzări; managerii de vânzări sunt impliciți în grupul *Approve held sale orders*) și companie (goală = se aplică peste tot). Regulile *Fereastră de așteptare* și *Ridicare personală pe comandă online* sunt inactive implicit.
- **Ridicare personală** — pe metodele de livrare cu ridicare de către client se bifează *Pickup by Customer* (Inventar → Configurare → Metode de Livrare); metodele Click & Collect sunt recunoscute automat, fără bifă.
- **Reevaluare automată** — acțiunea programată *Sale Order Review: re-evaluate held orders* rulează la fiecare 5 minute și elimină ferestrele de așteptare expirate, escaladând motivele temporare.
- **Integrare pentru fluxuri automate** — alte module (import marketplace, confirmări prin cron) verifică `order._review_can_auto_confirm()` înainte de a confirma; o comandă reținută rămâne ofertă cu motivele vizibile, în loc să eșueze silențios.
- Gândit ca bază pentru conectorii de marketplace (fereastră de așteptare, mesaj de la client, discrepanță de total), suita de curierat (livrări reținute, acțiuni în masă care sar peste comenzile reținute) și modulul de limită de credit.

#### 3. Dependențe

- `sale`
- `delivery`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de mai sus (Sumar și Funcționalități Cheie) sunt preluate din `readme/DESCRIPTION.md`/`readme/USAGE.md`/`readme/CONFIGURE.md`, care nu solicită explicit detalierea Componentelor Cheie (Modele, Vizualizări, Acțiuni Automate). Analiza dedicată a codului pentru această secțiune a fost omisă intenționat.

Notă: din documentația readme reies, ca elemente tehnice menționate explicit, metoda `order._review_can_auto_confirm()` de pe `sale.order`, wizard-ul de aprobare a reviziilor și acțiunea programată (`ir.cron`) de reevaluare la 5 minute.

#### 5. Conexiuni

- `terrabit_partner_credit_limit`: modulul de limită de credit pe partener se bazează pe motivele de reținere definite aici.
- [deltatech_delivery_review](../deltatech_delivery_review/index.md): extinde regulile de reținere pe fluxul de livrare/curierat descris în DESCRIPTION.md.
- [deltatech_delivery_status_review](../deltatech_delivery_status_review/index.md): parte din suita de curierat construită peste motivele de reținere ale acestui modul.
- [deltatech_marketplace_review](../deltatech_marketplace_review/index.md): conectorii de marketplace folosesc regulile (fereastră de așteptare, mesaj client, discrepanță de total) definite aici.

(Niciunul dintre modulele de mai sus nu are încă pagină wiki proprie, deci rămân ca text `cod` conform convenției — legăturile de mai sus documentează relația funcțională, nu link-uri active.)
