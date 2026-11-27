# Sales Plan by Customer (Planul de vânzări pe clienți)

- **Nume Tehnic:** `deltatech_sale_plan`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sale_plan
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_plan`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un plan anual de vânzări pe client B2B: directorul de vânzări stabilește o țintă pentru fiecare client, ținta se împarte pe luni după un șablon de sezonalitate, iar directorul și fiecare agent urmăresc valoarea facturată față de plan, pe lună și de la începutul anului. Modulul răspunde la întrebarea „care dealeri sunt în urmă față de ținta anuală și cu cât?”, pe care o pun lunar distribuitorii și producătorii care vând prin dealeri. Odoo 20 nu are o țintă pe client: planurile de comision țintesc agenții, iar bugetele cer un cont analitic pe client.

#### 2. Funcționalități Cheie

- **Șabloane de sezonalitate** (Vânzări › Configurare › Seasonality Templates): douăsprezece procente lunare cu suma 100%, scrise de mână sau calculate din facturile ultimilor ani (*Compute from History*, implicit 2 ani). Un șablon cu suma diferită de 100% nu se poate salva.
- **Plan anual** (Vânzări › Sales Plan › Plans): un plan pe companie și an, cu stări Ciornă, Confirmat, Închis; câte o țintă pe client (firma, cu facturile tuturor contactelor ei), împărțită imediat pe luni; diferența de rotunjire intră în decembrie. Un client cu ritm propriu primește procente proprii (linie *Custom*).
- **Completare rapidă**: *Generate from Last Year* (facturat în anul de bază plus procent de creștere, cu prag minim de facturare și opțiunea de actualizare a liniilor existente) sau import din fișier (*Plan*, *Customer VAT* sau *Customer*, *Yearly Target*, opțional *Seasonality*).
- **Revizuire în cursul anului**: pe un plan confirmat, o țintă anuală nouă păstrează lunile trecute și distribuie restul pe lunile rămase; un client adăugat are 0 pe lunile trecute; fiecare modificare apare în chatter. Liniile se șterg doar pe plan în ciornă (pe plan confirmat ținta se pune 0).
- **Realizare** (Vânzări › Sales Plan › Achievement): pivot, grafic și listă cu ținta lunară, facturatul (facturi postate minus note de credit, fără TVA, în moneda companiei, după data facturii, fără avansuri), diferența și procentul realizat la fiecare nivel de grupare; comenzile confirmate încă nefacturate apar separat, niciodată adunate la realizat; clienții facturați dar neplanificați apar cu țintă 0.
- **Tablou de bord** (Vânzări › Sales Plan › Dashboard): plan anual, facturat de la începutul anului (lunile încheiate), diferență, clienți sub plan, luna curentă, comandat nefacturat, grafic lunar și clienți ordonați după diferență; managerul vede și clasamentul agenților și poate alege un agent.
- **Drepturi** (Setări › Utilizatori › Sales Plan): *Own customers* pentru agenți (văd doar clienții lor și nu modifică nimic) și *All customers* pentru manager; facturatul unui client planificat se atribuie agentului de pe linia de plan. Planurile și realizarea sunt pe companie.
- Fluxul pas-cu-pas, cu capturi, este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `sale_management`
- `account`
- `deltatech_web_kpi_cards`

#### 4. Componente Cheie

**Modele**

- `sale.plan`: planul anual pe companie (cu `mail.thread`), cu stările ciornă, confirmat, închis.
- `sale.plan.line`: ținta anuală a unui client în plan, cu agent și sezonalitate.
- `sale.plan.month`: ținta lunară a unei linii de plan.
- `sale.plan.season`: șablonul de sezonalitate (procente lunare).
- `sale.plan.generate` (wizard): generarea planului din facturile anului de bază.
- `sale.plan.report`: raport SQL de realizare (țintă, facturat, diferență, procent, comandat nefacturat).

**Vizualizări**

- Formulare și liste pentru plan, linii de plan (țintă client), șabloane de sezonalitate.
- Raport de realizare: pivot, grafic, listă.
- Tablou de bord cu carduri KPI (componente OWL în `static/src/dashboard`).
- Wizardul *Generate from Last Year*.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește cron-uri sau acțiuni server.

#### 5. Conexiuni

- `deltatech_web_kpi_cards`: oferă cardurile KPI folosite de tabloul de bord.
- `sale`, `account`: sursa comenzilor confirmate și a facturilor postate din care se calculează realizatul.
