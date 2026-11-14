# Website Alternative Codes (localizat la `deltatech_alternative_website/index.md`)

- **Nume Tehnic:** `deltatech_alternative_website`
- **Versiune:** `19.0.1.0.13`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_alternative_website
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative_website`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde magazinul online Odoo astfel încât clienții să poată regăsi produsele și după codurile alternative (echivalente) definite pentru ele — coduri OEM, coduri de referință încrucișată sau coduri de producător, folosite frecvent de distribuitorii de piese de schimb și furnizorii industriali. Codurile sunt expuse pe pagina produsului și în căutarea site-ului, astfel încât un client care caută după un cod cu care este obișnuit (diferit de SKU-ul intern) găsește totuși produsul corect.

#### 2. Funcționalități Cheie

- **Coduri alternative pentru motoarele de căutare**: codurile produsului (`alternative_ids`) care nu sunt ascunse sunt afișate ca elemente `<span>` invizibile cu `itemprop="alternateName"`, citibile de motoarele de căutare externe și de căutarea internă.
- **Secțiunea „Alternative code”** pe pagina produsului, cu valoarea principală `alternative_code`, vizibilă doar utilizatorilor autentificați.
- **Secțiunea „Used For”** pe pagina produsului, afișată când `used_for` este completat (de ex. „Ford Focus 2005-2011”), pentru vehiculul/echipamentul căruia îi este destinată piesa.
- **Căutare după codul alternativ**: căutarea din `/shop` include `alternative_ids.name` printre câmpurile căutabile, deci orice produs cu un cod alternativ care se potrivește apare în rezultate.
- **Normalizarea interogării**: spațiile de la capete sunt eliminate, iar spațiile multiple sunt reduse la unul înainte de căutare (`website.searchable.mixin`).
- **Activare/dezactivare**: ambele secțiuni sunt șabloane opționale (`customize_show`), care se pornesc sau se opresc din *Website → Customize* pe pagina unui produs.
- **Configurarea codurilor**: se face în [deltatech_alternative](../deltatech_alternative/index.md), în tab-ul *Alternatives* al produsului (*Inventar → Produse → Produse* sau *Vânzări → Produse*).

#### 3. Dependențe

- `website`
- `website_sale`
- [deltatech_alternative](../deltatech_alternative/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): `_search_get_detail()` adaugă `alternative_ids.name` la câmpurile de căutare și la maparea rezultatelor, și scoate `description` / `description_sale` din câmpurile căutate (dacă sunt prezente), deci căutarea din magazin nu mai folosește descrierile produsului.
- `website.searchable.mixin` (extins): `_search_build_domain()` curăță spațiile din textul căutat înainte de a construi domeniul.

**Vizualizări**

- `product_alternative_code` (moștenește `website_sale.product`, `customize_show`): spanurile ascunse `alternateName` și blocul „Alternative code” pentru utilizatorii autentificați.
- `product_used_for` (moștenește `website_sale.product`, `customize_show`): blocul „Used For”, afișat când `used_for` este completat.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- [deltatech_alternative](../deltatech_alternative/index.md): modulul de bază care definește codurile alternative și câmpul `used_for`; acest modul le expune în magazinul online.

---

#### 6. Roadmap

`readme/ROADMAP.md` descrie funcționalități planificate, încă neimplementate în cod:

- Căutare semantică cu embeddings (pgvector, index HNSW), ca plasă de siguranță când căutarea exactă nu returnează nimic.
- Căutare în trepte pe `/shop`: potrivire exactă (SQL, `default_code`, `barcode`, coduri alternative), apoi parțială (`ILIKE`), apoi vectorială.
- Pre-normalizarea căutării (litere mici, separatori de cod unificați în cratimă, eliminarea cuvintelor de zgomot) și cache pentru embeddings.
- Indexurile PostgreSQL necesare căutării parțiale (trigram pe codurile produselor și pe `product_alternative.name`) există deja; `ilike` le folosește doar dacă funcția `unaccent` este `IMMUTABLE` în bază (vezi `deltatech_alternative`).
