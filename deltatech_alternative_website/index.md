# Website Alternative Codes (localizat la `deltatech_alternative_website/index.md`)

- **Nume Tehnic:** `deltatech_alternative_website`
- **Versiune:** `20.0.1.0.13`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_alternative_website
- **Cale Locală:** `odoo-addons/deltatech/deltatech_alternative_website`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde magazinul online Odoo astfel încât clienții să regăsească produsele și după codurile alternative (echivalente) definite pentru ele: coduri OEM, coduri de referință încrucișată sau coduri de producător, folosite frecvent de distribuitorii de piese de schimb și de furnizorii industriali. Codurile apar pe pagina produsului și sunt vizibile motorului de căutare al site-ului, deci un client care caută după un cod diferit de SKU-ul intern găsește produsul corect.

#### 2. Funcționalități Cheie

- Codurile alternative ale produsului (`alternative_ids`) se afișează ca elemente `<span>` ascunse cu `itemprop="alternateName"`, disponibile motoarelor de căutare externe și căutării interne a site-ului.
- Pe pagina produsului apare secțiunea **„Alternative code”** cu valoarea `alternative_code`, vizibilă doar utilizatorilor autentificați.
- Secțiunea **„Used For”** apare când câmpul `used_for` este completat (de ex. vehiculul pentru care se potrivește piesa).
- Cele două blocuri sunt șabloane website opționale (`customize_show`), care se pornesc sau se opresc din **Website > Customize**, pe pagina unui produs.
- Căutarea full-text din magazin (`/shop`) include `alternative_ids.name` printre câmpurile căutabile.
- Interogarea de căutare este normalizată prin `website.searchable.mixin`: spațiile de la capete sunt eliminate și spațiile multiple sunt reduse, deci mai puține rezultate „0" false.
- Codurile se definesc în tabul **Alternatives** al produsului, adăugat de [deltatech_alternative](../deltatech_alternative/index.md); sunt căutabile pe site imediat după salvare.

#### 3. Dependențe

- `website`
- `website_sale`
- [deltatech_alternative](../deltatech_alternative/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template`: extinde `website.searchable.mixin` cu `alternative_ids.name` în câmpurile de căutare.
- `website.searchable.mixin`: normalizarea interogării de căutare.

**Vizualizări**

- `views/templates.xml`: șabloanele paginii de produs pentru codul alternativ și „Used For”.

#### 5. Conexiuni

- [deltatech_alternative](../deltatech_alternative/index.md): modulul de bază care definește codurile alternative și câmpul `used_for`; acest modul le expune în magazinul online.
