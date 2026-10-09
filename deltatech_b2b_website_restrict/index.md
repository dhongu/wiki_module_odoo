# B2B Website for Companies Only (localizat la `deltatech_b2b_website_restrict/index.md`)

- **Nume Tehnic:** `deltatech_b2b_website_restrict`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_b2b_website_restrict
- **Cale Locală:** `odoo-addons/bitshop/deltatech_b2b_website_restrict`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul transformă un website Odoo într-unul destinat exclusiv clienților persoane juridice, construit peste portalul B2B. Un vizitator neautentificat ajunge doar la pagina de prezentare B2B cu formularul de cerere de cont; orice altă adresă îl redirecționează acolo. Astfel, prețurile și catalogul companiei nu sunt niciodată publice.

#### 2. Funcționalități Cheie

- Opțiune per website, **Company customers only** (*Website ▸ Configuration ▸ Websites*): celelalte website-uri din aceeași bază rămân deschise.
- Vizitatorul neautentificat accesează doar pagina de prezentare cu formularul de cerere de cont (`/b2b`), paginile de autentificare și resetare parolă și fișierele statice necesare acestora; orice altă adresă, rută sau pagină din website builder, este redirecționată la `/b2b`.
- Prețurile și catalogul nu sunt publice.
- Catalogul nu este indexat de două ori de motoarele de căutare când magazinul retail rulează pe alt website din aceeași bază.
- Utilizatorii autentificați (portal sau interni) navighează website-ul normal.
- Activare: bifează opțiunea, salvează, apoi verifică într-o fereastră privată că orice adresă duce la pagina B2B.

#### 3. Dependențe

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md)

#### 4. Componente Cheie

**Modele**

- `website` (extins): câmpul boolean `b2b_only` („Company customers only”).
- `ir.http` (extins): `_dispatch` și `_serve_page` redirecționează la `/b2b` vizitatorii publici, cu excepția prefixelor permise (`/b2b`, `/web/login`, `/web/reset_password`, `/web/signup`, `/web/session`, `/web/webclient`, `/web/assets`, `/web/image`, `/web/binary`, `/web/static`, `/website/translations`, `/favicon.ico`, `/robots.txt`, `/mail`).

**Vizualizări**

- `view_website_form_b2b`: moștenește `website.view_website_form` și adaugă `b2b_only` după câmpul `domain`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [deltatech_b2b_portal](../deltatech_b2b_portal/index.md): oferă pagina `/b2b` și formularul de cerere de cont către care se face redirecționarea.
