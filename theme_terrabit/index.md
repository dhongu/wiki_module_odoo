# Terrabit Theme (localizat la `theme_terrabit/index.md`)

- **Nume Tehnic:** `theme_terrabit`
- **Versiune:** `19.0.1.99.0`
- **Cale:** https://github.com/terrabit-ro/terrabit-erp/tree/19.0/theme_terrabit
- **Cale Locală:** `proiecte/terrabit-erp/theme_terrabit`
- **Ultima Ingestie:** `2026-11-17`

#### 1. Sumar

Tema de website pentru terrabit.ro, construită pe sistemul de design Terrabit: paleta verde din logo, titluri în Manrope, text în Roboto, colțuri pătrate și o pagină de start alcătuită din snippeturi editabile. Include și paginile de conținut ale site-ului (servicii, ERP, localizare, aplicații, resurse), astfel încât imaginea și conținutul rămân coerente și ușor de întreținut.

#### 2. Funcționalități Cheie

- Identitate vizuală Terrabit: paletă verde, fonturi Manrope/Roboto, colțuri pătrate, temă luminoasă și întunecată.
- Pagină de start din snippeturi editabile în website builder.
- Pagini de prezentare: aplicații Odoo Apps (cifre actualizate la 9 noiembrie 2026: 756 de module în total, 600 pentru Odoo 19, 485 pentru Odoo 20), servicii, despre noi, ERP, localizare, achiziții, planificarea producției, retururi, contracte de service, pontaj, helpdesk AI, livrare, marketplace, licențe.
- Pagină nouă `/cloud-erp-guide`: ghid pentru începători despre ERP în cloud (IaaS, PaaS, SaaS, cloud vs. on-premise, alegerea furnizorului), cu trimitere la `/contactus`; traducere în română în `i18n/ro.po`.
- Pagina `/calendar` (calendarul de programări) este vizibilă doar pentru vizitatorii autentificați (clienți cu cont de portal și echipă); cardul „Programează o întâlnire” din `/resources` apare tot doar acestora.
- Optimizare SEO: date structurate, reguli de noindex pentru anumite pagini, enumerare personalizată a paginilor pentru sitemap, reguli de rescriere URL.
- Antet fix, subsol, banner de cookies, insigne și figuri reutilizabile.
- Traducere în română pentru textele temei.
- Atenție: linkul Google de programare a fost public până acum; cine îl deține se poate programa în continuare, până la generarea unui link nou în Google Calendar.

#### 3. Dependențe

- `theme_common`

#### 4. Componente Cheie

**Modele**

- `website` (extins): decide ce pagini sunt noindex (`_theme_terrabit_is_noindex`) și completează enumerarea paginilor pentru sitemap (`_enumerate_pages`).
- `theme.utils` (extins): setări aplicate la instalarea temei: antet fix, vizibilitate „Signed In” pentru calendar, post-copiere (`_theme_terrabit_post_copy`).

**Vizualizări**

- `views/homepage.xml`, `apps.xml`, `services.xml`, `about.xml`, `erp.xml`, `localization.xml` și celelalte: paginile și snippeturile site-ului.
- `views/footer.xml`, `cookies.xml`, `badges.xml`, `figures.xml`: elemente comune.
- `views/structured_data.xml`, `seo.xml`: date structurate și meta SEO.
- `data/ir_asset.xml`: încărcarea stilurilor și a fonturilor temei.
- `data/website_rewrite.xml`: reguli de rescriere/redirecționare URL.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server. Migrările versiunii aplică vizibilitatea paginii `/calendar` pe site-urile care au deja tema.

#### 5. Conexiuni

- `website`: platforma pe care se aplică tema.
- `theme_common`: baza comună a temelor Odoo.
