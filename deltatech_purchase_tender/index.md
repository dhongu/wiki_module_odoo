# Reguli de licitație la achiziții

- **Nume Tehnic:** `deltatech_purchase_tender`
- **Versiune:** `20.0.1.0.0`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_purchase_tender`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_purchase_tender`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul impune o procedură de licitație pe achizițiile alese de companie. Comenzile cu produse din categoriile marcate **Necesită oferte de la furnizori** (de exemplu consumabile, întreținere, echipamente de protecție) trebuie să aibă oferte cu preț de la un număr minim de furnizori și, peste un prag, aprobarea unui aprobator de achiziții. Mărfurile reaprovizionate automat, din alte categorii, nu sunt afectate, deci restul achizițiilor nu este încetinit.

#### 2. Funcționalități Cheie

- **Număr minim de oferte**: peste o sumă configurabilă, comanda nu poate fi confirmată până când cererea de ofertă și alternativele ei au oferte cu preț de la cel puțin *N* furnizori diferiți (3 implicit). Alternativele anulate la confirmarea celei alese se numără în continuare; o cerere fără preț nu e ofertă, iar contactele aceleiași companii contează o singură dată.
- **Excepție motivată** (furnizor unic sau urgență): un aprobator poate confirma cu mai puține oferte, cu motiv obligatoriu, reținut pe comandă și publicat în chatter; cumpărătorul nu poate confirma cu excepție.
- **Aprobare peste prag**: comanda trece în *De aprobat*, aprobatorii primesc o activitate *Aprobare achiziție*, închisă pentru toți la aprobare, iar doar grupul *Licitație achiziții / Aprobator* poate aproba. Dubla validare la nivel de companie nu este folosită.
- **Contor de oferte** în fila *Alternative*: oferte primite și oferte necesare.
- Setări în *Achiziții > Configurare > Setări > Comenzi*: **Oferte furnizori** (minim de oferte, 0 sau 1 dezactivează; prag) și **Aprobare licitație** (activare, prag). Sumele sunt fără TVA, în moneda companiei; pragul 0 înseamnă fiecare comandă.
- Marcajul **Necesită oferte de la furnizori** se setează pe categoriile de produse (subcategoriile moștenesc) înainte de crearea comenzilor; comenzile existente nu se reclasifică.
- Aprobatorii se stabilesc în *Setări > Utilizatori*, fila Drepturi de acces, **Licitație achiziții = Aprobator**.
- Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `purchase_alternative`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): contorul de oferte, câmpurile de excepție și aprobare; suprascrie `button_confirm`, `button_approve` și `button_cancel`.
- `product.category` (extins): marcajul de licitație obligatorie.
- `res.company` și `res.config.settings` (extinse): pragurile și numărul minim de oferte.

**Vizualizări**

- `purchase_order_form`: contorul de oferte, motivul excepției, butonul de aprobare.
- `product_category_form_view`: marcajul **Necesită oferte de la furnizori**.
- `res_config_settings_view_form`: setările modulului.
- `view_purchase_order_filter`, `purchase_order_view_search`: filtre de căutare.

**Acțiuni Automate / Acțiuni Server**

- Tipul de activitate **Aprobare achiziție** (`data/mail_activity_type_data.xml`); nu există cron sau acțiuni server.

#### 5. Conexiuni

- Niciuna verificată cu alte pagini wiki existente.
