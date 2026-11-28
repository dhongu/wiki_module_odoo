# Web Scan Base

- **Nume Tehnic:** `deltatech_web_scan`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_web_scan
- **Cale Locală:** odoo-addons/deltatech/deltatech_web_scan
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Bază tehnică pentru modulele care citesc pagini de produs de pe web, de exemplu paginile concurenților sau ale furnizorilor care nu oferă feed. Nu are meniu și nici date proprii; modulele care o folosesc hotărăsc ce se citește și ce se scrie.

#### 2. Funcționalități Cheie

- Citire sigură: doar adrese publice (loopback, rețele private, link-local și metadatele cloud sunt refuzate, cu verificare repetată la deschiderea conexiunii); redirecturi urmate manual, cel mult 5; pagina este tăiată la 3 MiB, iar tipurile de conținut neașteptate sunt refuzate.
- Citire politicoasă: respectă `robots.txt` (stare *Blocked*, dezactivabil per site de modulul care folosește baza), pauză între cereri către același site, site-uri luate pe rând; protecțiile anti-robot (CAPTCHA, Cloudflare, 403, 429) dau doar starea *Blocked*, fără ocolire.
- Date extrase: schema.org (JSON-LD și Microdata) cu nume, brand, SKU, MPN, cod de bare, imagini, descriere și oferte (se păstrează cea mai ieftină în stoc); selectori (XPath, CSS, regex, JSON-LD) cu tabel de valori pentru site-urile fără schema.org; tipare HTML uzuale ca ultimă soluție, doar pentru preț, fără prețurile vechi tăiate.
- Prețuri în format românesc sau englezesc (`1.299,00 lei`, `1,299.00`, `1 299,99`).
- Verificări: *Other Product* când pagina declară alt cod de bare sau alt cod decât produsul așteptat; *Suspect* când prețul s-a schimbat peste un procent setat față de citirea anterioară, până la confirmare.
- Pentru dezvoltatori: mixin-urile `web.scan.source.mixin` și `web.scan.history.mixin` și funcțiile `utils.fetch`, `utils.extract`, `utils.codes`, `utils.scan`. Fluxul pentru consultant este în fișa atașată.

#### 3. Dependențe

- `base`
- Dependență externă Python: `extruct`

#### 4. Componente Cheie

**Modele**

- `web.scan.source.mixin` (abstract): pagină citită periodic, cu stare, ultima citire și numărul de eșecuri consecutive; acțiunea programată o sare după 5 eșecuri.
- `web.scan.history.mixin` (abstract): istoricul valorilor afișate de pagină, ca intervale; linie nouă doar la schimbarea unei valori.

**Vizualizări**

- Niciuna.

**Acțiuni Automate / Acțiuni Server**

- Niciuna definită în acest modul; citirea programată este în modulele care folosesc baza.

#### 5. Conexiuni

- Niciuna verificată în cod.
