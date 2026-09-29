# Image Optimizer (localizat la `deltatech_image_optimize/index.md`)

- **Nume Tehnic:** `deltatech_image_optimize`
- **Versiune:** `19.0.1.9.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_image_optimize
- **Cale Locală:** `odoo-addons/deltatech/deltatech_image_optimize`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul face două lucruri pe aceleași imagini: recomprimă atașamentele de tip
imagine (poze de produs, avatare etc.) supradimensionate, pentru a elibera
spațiu din filestore-ul Odoo, și elimină imaginile de produs stocate de două ori
în aceeași fișă de produs. Fiecare imagine originală este redusă ca dimensiune și recodată în JPEG
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
- Metodele de batch întorc două cifre: `freed` (suma diferențelor per atașament)
  și `freed_disk` (doar atașamentele al căror fișier din filestore nu e
  partajat). Odoo păstrează un singur fișier per checksum, deci `freed`
  supraestimează câștigul când aceeași poză apare pe mai multe înregistrări;
  spațiul real se raportează cu `freed_disk`. Filestore-ul crește înainte să
  scadă — spațiul revine abia după GC.
- **Imagini de produs duplicate:** detectează înregistrările `product.image` cu
  conținut identic (după checksum-ul SHA1 calculat deja de Odoo, deci fără
  decodarea imaginilor) și le raportează grupat pe conținut. Se șterg doar
  copiile care se repetă în cadrul aceluiași produs/variantă; se păstrează
  imaginea cu `sequence, id` cel mai mic. Aceeași poză folosită pe mai multe
  produse (de ex. o fotografie generică din feed-ul furnizorului) este raportată,
  dar **niciodată ștearsă**. Înregistrările cu `video_url` sunt păstrate mereu.
- Meniu: Website → Configurare → eCommerce → Produse → **Imagini duplicate**
  (doar administratori). Lista se deschide filtrată pe grupurile care se pot
  curăța; acțiunea **Remove Duplicated Images** afișează în prealabil exact ce
  se va șterge (wizard), și poate rula și fără selecție, pe tot catalogul.
- Nu detectează aceeași poză reexportată/redimensionată (checksum diferit — ar
  necesita hash perceptual). Ștergerea duplicatelor curăță catalogul, dar
  eliberează puțin spațiu pe disc; pentru spațiu se folosește recomprimarea.
- La instalare, un hook completează `image_checksum` printr-un singur `UPDATE`
  SQL din `ir_attachment`; ulterior se poate reface cu
  `env["product.image"]._dedup_backfill_checksums()`.

#### 3. Dependențe

- `base`
- `website_sale`: definește `product.image` (dependență adăugată în 19.0.1.9.0).

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

- `product.image` (extins): adaugă `image_checksum` (indexat, preluat din
  atașament) și `duplicate_count`; metode `_dedup_backfill_checksums()` și
  `action_view_duplicates()`.
- `deltatech.product.image.duplicate` (vedere SQL, `_auto = False`): o linie per
  conținut distinct, cu numărul de copii, numărul de produse și numărul de
  imagini ce se pot elimina; acțiuni `action_view_images()` și `action_clean()`.
- `deltatech.product.image.dedup` (wizard tranzitoriu): previzualizare și
  aplicare a ștergerii (`action_apply()`).

**Vizualizări**

- `view_product_image_duplicate_list` / `view_product_image_duplicate_search`:
  lista și căutarea grupurilor de imagini duplicate.
- `view_product_image_dedup_form` (wizard) și `view_product_image_dedup_list`:
  previzualizarea și lista imaginilor de produs vizate.
- Meniul `menu_product_image_duplicate` (sub `website_sale.menu_catalog`).
- Configurarea recomprimării se face prin parametrii de sistem (Settings →
  Technical → System Parameters) și acțiunile programate standard.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_dt_image_optimize` (*Image Optimizer: recompress oversized
  images*): rulează zilnic (implicit dezactivată) și apelează
  `_dt_image_optimize_cron()` pe `ir.attachment`.
- Parametri de sistem definiți la instalare (`data/ir_config_parameter.xml`):
  `deltatech_image_optimize.quality`, `.max_dim`, `.min_size`, `.batch`,
  `.flush_every`, `.target_fields`, `.variant_fields`, `.variant_quality`,
  `.webp_quality`, `.force_jpeg`, `.variant_min_size` — toate `noupdate="1"`
  pentru a nu suprascrie modificările utilizatorului la upgrade. De la 19.0.1.8.1
  și `ir_cron.xml` este `noupdate="1"`: activarea cron-ului supraviețuiește
  upgrade-urilor (pe bazele existente, cron-ul oprit anterior de un upgrade
  trebuie reactivat manual).

#### 5. Conexiuni

- [deltatech_website_watermark](../deltatech_website_watermark/index.md): folosește aceeași tehnică de înregistrare a
  plugin-ului WebP pentru Pillow (menționată explicit în codul acestui modul
  ca precedent).
