# Website Vehicle Fitment

- **Nume Tehnic:** `deltatech_website_vehicle_fitment`
- **Versiune:** `20.0.1.3.2`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_vehicle_fitment
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_vehicle_fitment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Selector de vehicul pentru magazinul online, construit pe catalogul de vehicule și pe compatibilitățile din `deltatech_vehicle_fitment`. Clientul alege marca, modelul și motorul, iar magazinul îi arată doar piesele care se potrivesc.

#### 2. Funcționalități Cheie

- Blocul de website **Vehicle Selector** (grupul **Catalog**): clientul alege marca, modelul și, dacă modelul are motoare sau alte variante înregistrate, motorul. Blocul arată vehiculul, numărul de piese compatibile, numărul celor în stoc (dacă Inventory e instalat) și principalele categorii din magazin cu piesele potrivite fiecăreia. Textele blocului se editează în editorul de website.
- **See the parts** deschide magazinul filtrat pe vehicul. Vehiculul rămâne în sesiunea vizitatorului: fiecare pagină, categorie și căutare arată doar piesele compatibile plus cele universale, cu o bandă care numește vehiculul și trimite la schimbare sau la afișarea tuturor pieselor.
- **Pagina produsului**: secțiunea *Compatibility* listează vehiculele pe care se potrivește piesa, pe mărci, și spune dacă se potrivește vehiculului ales de client.
- Doar mărcile cu cel puțin un model sunt oferite; sigla mărcii se încarcă pe formularul mărcii (fără siglă se afișează inițialele). Modulul nu livrează sigle, fiind mărci înregistrate.
- Pasul de motor apare când motoarele sunt valori ale unui atribut de vehicul setate pe modele; o compatibilitate restrânsă la un motor este omisă când clientul alege alt motor. Pentru piese la comandă se debifează *Vehicle Selector: Parts in Stock* în setările website-ului.
- Vizitatorii publici și utilizatorii de portal pot citi catalogul de vehicule și compatibilitățile; nimic altceva nu e expus. Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- `deltatech_vehicle_fitment`
- `website_sale`

#### 4. Componente Cheie

**Modele**

- `product.template`: extins cu logica de compatibilitate pentru filtrarea magazinului.
- `website`: vehiculul ales în sesiune și numărătorile selectorului.
- `res.config.settings`: setarea *Vehicle Selector: Parts in Stock*.

**Vizualizări**

- `views/s_vehicle_selector.xml` și `views/snippets.xml`: blocul Vehicle Selector.
- `views/shop.xml`: filtrarea magazinului și banda vehiculului.
- `views/product.xml`: secțiunea Compatibility.
- `views/res_config_settings_views.xml`: setările website-ului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `deltatech_vehicle_fitment`: catalogul de vehicule și compatibilitățile (*Sales > Configuration > Vehicles*).
