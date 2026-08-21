# Image Optimizer (localizat la `deltatech_image_optimize/index.md`)

- **Nume Tehnic:** `deltatech_image_optimize`
- **Versiune:** `19.0.1.8.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_image_optimize
- **Cale Locală:** `odoo-addons/deltatech/deltatech_image_optimize`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul recomprimă automat atașamentele de tip imagine (poze de produs, avatare
etc.) care sunt supradimensionate, pentru a elibera spațiu din filestore-ul
Odoo. Fiecare imagine originală este redusă ca dimensiune și recodată în JPEG
(sau WebP/PNG dacă are transparență reală), păstrând doar rezultatul dacă e
efectiv mai mic decât originalul — fără să afecteze vizual imaginile publicate
pe site sau în documente.

#### 2. Funcționalități Cheie

- Recomprimă imaginile „originale" (implicit `image_1920` și
  `image_variant_1920`) la o dimensiune maximă configurabilă (implicit 1920 px)
  și o calitate JPEG configurabilă (implicit 85).
- Detectează transparența reală (nu doar modul de culoare) și păstrează
  imaginile cu transparență ca WebP (sau PNG optimizat dacă Pillow nu are
  encoder WebP), fără să le transforme niciodată în JPEG implicit.
- Sare peste GIF-urile animate — nu le aplatizează niciodată.
- Scrie imaginea optimizată prin înregistrarea proprietară, astfel încât Odoo
  regenerează automat variantele redimensionate (`image_1024/512/256/128`).
- Recomprimă separat și variantele deja stocate (fără redimensionare, doar
  recodare la o calitate mai mică), fără să propage schimbarea înapoi spre
  imaginea originală.
- Marchează atașamentele deja procesate (`deltatech_image_optimized`) ca să nu
  fie reprocesate la rulările următoare; imaginile noi/schimbate sunt reluate
  automat pentru că Odoo creează un atașament nou la fiecare modificare.
- Rulează prin acțiune programată (`ir.cron`) zilnică, **dezactivată implicit**
  — trebuie activată manual după testare pe staging.
- Configurare completă prin parametri de sistem (`ir.config_parameter`):
  calitate JPEG/WebP, dimensiune maximă, dimensiune minimă de procesat,
  dimensiune batch, câmpuri țintă, frecvență de flush ORM.
- Opțiune destructivă `force_jpeg` (dezactivată implicit) care ignoră complet
  canalul alfa și forțează JPEG pentru economie maximă — documentată explicit
  ca ireversibilă și recomandată doar după verificare prealabilă a
  catalogului.
- La finalul rulării cron, apelează garbage collection-ul filestore-ului
  pentru a recupera efectiv spațiul de pe disc.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `ir.attachment` (extins): adaugă câmpul `deltatech_image_optimized`
  (Datetime) și metodele de recomprimare/optimizare:
  - `_dt_image_optimize_params()`: citește configurația din
    `ir.config_parameter`.
  - `_dt_image_recompress()`: funcție pură de recomprimare a octeților unei
    imagini (JPEG/WebP/PNG), fără scriere, folosită și pentru testare/probă
    manuală a efectului `force_jpeg`.
  - `_dt_image_shared_file()`: verifică dacă fișierul din filestore e partajat
    cu alte atașamente (același `store_fname`), pentru a raporta corect
    spațiul eliberat efectiv pe disc (`freed_disk`) față de suma diferențelor
    per-atașament (`freed`).
  - `_dt_image_optimize_run()`: rulează un batch de optimizare pe imaginile
    originale (`image_1920`, `image_variant_1920`).
  - `_dt_image_optimize_variants_run()`: recomprimă în același mod variantele
    redimensionate (`image_1024/512/256/128`), fără a le redimensiona din nou.
  - `_dt_image_optimize_cron()`: punctul de intrare pentru acțiunea
    programată — rulează întâi originalele, apoi variantele, apoi GC-ul
    filestore-ului.

**Vizualizări**

Modulul nu adaugă vizualizări proprii; configurarea se face prin parametrii de
sistem standard (Settings → Technical → System Parameters) și prin ecranul
standard de acțiuni programate (Settings → Technical → Scheduled Actions).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_dt_image_optimize` (*Image Optimizer: recompress oversized
  images*): rulează zilnic (implicit dezactivată) și apelează
  `_dt_image_optimize_cron()` pe `ir.attachment`.
- Parametri de sistem definiți la instalare (`data/ir_config_parameter.xml`):
  `deltatech_image_optimize.quality`, `.max_dim`, `.min_size`, `.batch`,
  `.flush_every`, `.target_fields`, `.variant_fields`, `.variant_quality`,
  `.webp_quality`, `.force_jpeg`, `.variant_min_size` — toate `noupdate="1"`
  pentru a nu suprascrie modificările utilizatorului la upgrade.

#### 5. Conexiuni

- [deltatech_website_watermark](../deltatech_website_watermark/index.md): folosește aceeași tehnică de înregistrare a
  plugin-ului WebP pentru Pillow (menționată explicit în codul acestui modul
  ca precedent).
