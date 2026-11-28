# Website B2B Doar pentru Companii

- **Nume Tehnic:** `deltatech_b2b_website_restrict`
- **Versiune:** `20.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_b2b_website_restrict
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_website_restrict`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un website închis vizitatorilor, deasupra portalului B2B: un vizitator neautentificat ajunge doar la pagina de prezentare B2B cu formularul de cerere de cont (`/b2b`), plus autentificare, resetare de parolă și înregistrare. Orice altă adresă îl redirecționează la `/b2b`.

#### 2. Funcționalități Cheie

- Se activează per website, prin bifa *Doar clienți companie* (în *Website ▸ Configurare ▸ Website-uri*, vizibilă în modul dezvoltator); celelalte website-uri ale bazei rămân deschise.
- Redirecționarea acoperă atât rutele, cât și paginile din website builder.
- Prețurile și catalogul nu sunt publice cât timp *Cont client* rămâne pe *La invitație* (cu înregistrare liberă, vizitatorul își poate crea singur un cont de portal).
- Catalogul nu este indexat de două ori de motoarele de căutare când magazinul retail rulează pe alt website din aceeași bază.
- Utilizatorii autentificați (portal sau interni) navighează normal. Pașii sunt în fișa consultantului.

#### 3. Dependențe

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md)

#### 4. Componente Cheie

**Modele**

- `website` (extins): câmpul `b2b_only` (*Doar clienți companie*).
- `ir.http` (extins): redirecționarea vizitatorilor către `/b2b` în `_dispatch` și la servirea paginilor din website builder.

**Vizualizări**

- `website_views.xml`: bifa pe formularul website-ului.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): pagina `/b2b` și cererea de cont către care se redirecționează.
- [deltatech_b2b_announcement](../deltatech_b2b_announcement/index.md) și [deltatech_b2b_price_tier](../deltatech_b2b_price_tier/index.md): alte extensii ale portalului B2B.
