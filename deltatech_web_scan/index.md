# Web Scan Base (localizat la `deltatech_web_scan/index.md`)

- **Nume Tehnic:** `deltatech_web_scan`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_web_scan
- **Cale Locală:** `odoo-addons/deltatech/deltatech_web_scan`
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Baza tehnică pentru modulele care citesc **pagini de produs de pe web**: paginile concurenților și ale furnizorilor care nu oferă feed. Nu are meniu și nici date proprii; modulele care o folosesc hotărăsc ce se citește și ce se scrie. Citirea se face în siguranță (doar adrese publice) și politicos (robots.txt, pauză între cereri), fără a ocoli protecțiile site-urilor.

#### 2. Funcționalități Cheie

- **Citire sigură:** se citesc doar adrese http(s) a căror gazdă se rezolvă la IP-uri publice; loopback, rețele private, link-local și adresele de metadate cloud sunt refuzate, iar adresa reală a conexiunii este reverificată la deschidere (protecție la schimbarea răspunsului DNS). Redirecturile se urmează manual (maximum 5), fiecare verificat la fel. Pagina se citește pe bucăți și se taie la 3 MiB; tipurile de conținut neașteptate sunt refuzate.
- **Citire politicoasă:** respectă `robots.txt` (pagină interzisă = starea *Blocked*; poate fi dezactivat de modulul care folosește baza, per site); pauză între două cereri către același site, iar citirea programată alternează siturile; paginile cu protecție anti-robot (CAPTCHA, Cloudflare, 403, 429) primesc doar starea *Blocked*, fără încercări de ocolire.
- **Ce se extrage din pagină:**
  - date schema.org (JSON-LD și Microdata): nume, brand, SKU, MPN, cod de bare (GTIN), imagini, descriere și oferte (preț, monedă, disponibilitate); la mai multe oferte se păstrează cea mai ieftină aflată în stoc;
  - selectori configurați (XPath, CSS, expresie regulată, cale JSON-LD) pentru siturile fără schema.org, cu tabel de valori (ex. *In stock* → în stoc);
  - tipare HTML uzuale, ca ultimă soluție, doar pentru preț (prețurile vechi, tăiate, sunt excluse; prețul găsit astfel este marcat ca atare);
  - prețuri scrise în format românesc sau englezesc: `1.299,00 lei`, `1,299.00`, `1 299,99`.
- **Verificări:** *Other Product* când pagina declară alt cod de bare sau alt cod (comparat fără spații, cratime și puncte) decât produsul așteptat; *Suspect* când prețul s-a modificat cu mai mult decât un procent stabilit față de citirea anterioară, până la confirmare.
- **Pentru dezvoltatori:** mixin pentru o pagină citită repetat (stare, ultima citire, eșecuri consecutive; acțiunea programată sare peste o pagină după 5 eșecuri), mixin de istoric pe intervale (linie nouă doar la schimbarea valorii) și funcții utilitare fără bază de date.

#### 3. Dependențe

- `base`
- Dependență Python externă: `extruct`

#### 4. Componente Cheie

**Modele**

- `web.scan.source.mixin` (model abstract): pagină citită periodic, cu stare, ultima citire și eșecuri consecutive; conține logica citirii programate (`_scan_cron_run`, `_scan_cron_domain`).
- `web.scan.history.mixin` (model abstract): istoricul valorilor afișate de o pagină, ca intervale.

**Vizualizări**

Modulul nu definește vizualizări și nu are meniu.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește `ir.cron` propriu (`data` este gol); oferă metoda `_scan_cron_run`, apelată de acțiunile programate ale modulelor care folosesc baza. Funcțiile fără bază de date sunt în `utils/` (`fetch`, `extract`, `codes`, `scan`).

#### 5. Conexiuni

- [deltatech_vendor_products_site](../deltatech_vendor_products_site/index.md): folosește baza pentru citirea paginilor de produs ale furnizorilor fără feed.
