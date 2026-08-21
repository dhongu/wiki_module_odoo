# Website alternative code (localizat la `deltatech_alternative_website/index.md`)

- **Nume Tehnic:** `deltatech_alternative_website`
- **Versiune:** `19.0.1.0.8`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_alternative_website`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative_website`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul extinde magazinul online Odoo astfel încât clienții să poată regăsi produsele și după codurile alternative (echivalente) definite pentru acestea — coduri OEM, coduri de referință încrucișată sau coduri de producător, folosite frecvent de distribuitorii de piese de schimb și furnizorii industriali. Modulul afișează aceste coduri direct pe pagina produsului și le face vizibile motorului de căutare al site-ului, astfel încât un client care caută după un cod cu care este obișnuit (diferit de SKU-ul intern) găsește totuși produsul corect.

#### 2. Funcționalități Cheie

- Afișează codurile alternative ale produsului (`alternative_ids`) ca elemente `<span>` ascunse cu `itemprop="alternateName"`, disponibile atât motoarelor de căutare externe, cât și căutării interne a site-ului.
- Afișează pe pagina produsului o secțiune dedicată **„Cod alternativ”** (vizibilă doar utilizatorilor autentificați) cu valoarea principală `alternative_code`.
- Afișează o secțiune **„Se folosește pentru”** pe pagina produsului atunci când câmpul `used_for` este completat, indicând vehiculul/echipamentul pentru care se potrivește piesa.
- Extinde căutarea full-text a magazinului online (`_search_get_detail`) pentru a include `alternative_ids.name` printre câmpurile căutabile, astfel încât clienții găsesc produsele după oricare dintre codurile lor de referință încrucișată.
- Îmbunătățește normalizarea interogărilor de căutare prin `website.searchable.mixin`: elimină spațiile de la început/sfârșit și reduce spațiile multiple înainte de executarea căutării, scăzând numărul de rezultate „0" false.
- Depinde de [deltatech_alternative](../deltatech_alternative/index.md) pentru câmpurile de bază `alternative_ids` și `used_for` de pe `product.template`.

#### 3. Dependențe

- [website](../website/index.md)
- `website_sale`
- [deltatech_alternative](../deltatech_alternative/index.md)

#### 4. Componente Cheie

Conform fișierului `readme/DESCRIPTION.md`, funcționalitatea principală este afișarea codurilor alternative pe pagina produsului și extinderea căutării site-ului cu aceste coduri. Întrucât descrierea modulului este disponibilă și acoperă secțiunea de componente, nu a fost efectuată o analiză suplimentară a codului.

#### 5. Conexiuni

- [deltatech_alternative](../deltatech_alternative/index.md): modulul de bază care definește codurile alternative (echivalente) și câmpul `used_for` ale produselor; acest modul de website expune respectivele date în magazinul online.
