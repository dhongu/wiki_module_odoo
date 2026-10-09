# Image Optimizer (localizat la `deltatech_image_optimize/index.md`)

- **Nume Tehnic:** `deltatech_image_optimize`
- **Versiune:** `19.0.1.12.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_image_optimize
- **Cale Locală:** `odoo-addons/deltatech/deltatech_image_optimize`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul păstrează imaginile de produs din catalogul eCommerce curate și ușoare,
prin patru operații pe aceleași imagini: eliminarea fundalului fotografiilor de
produs (produsul este decupat și salvat pe fundal transparent sau pe o culoare
uniformă), eliminarea unui filigran (watermark) pe care îl poartă imaginile
catalogului, ștergerea imaginilor stocate de două ori în aceeași fișă de produs
și recomprimarea imaginilor supradimensionate, pentru a elibera spațiu în
filestore și a face paginile magazinului mai rapide. Totul rulează pe serverul
Odoo; nicio imagine nu este trimisă către un serviciu extern. Imaginea
originală nu se păstrează după eliminarea fundalului, a filigranului sau după
recomprimare, de aceea rezultatul se verifică înainte de aplicare.

#### 2. Funcționalități Cheie

**Eliminare fundal**

- Acțiunea **Remove Image Background** (Actions) pe produse (include galeria
  eCommerce a produsului) și pe imaginile de produs; necesită dreptul
  *Products: Create*, iar pentru imaginile din galerie și *Sales:
  Administrator* sau *Website: Restricted Editor*.
- Un wizard arată fiecare imagine **înainte / după**, pe un fundal în
  carouri (zonele transparente rămân vizibile). Se debifează rândurile
  nereușite, apoi **Apply**; nimic nu se scrie înainte. **Refresh Preview**
  reface previzualizarea și bifările.
- Trei metode de decupare (`bg_method`): **uniform** (fără model AI — fundalul
  este ceea ce are culoarea marginii imaginii și o atinge; accesoriile închise
  la culoare de lângă produs și zonele albe din interiorul produsului, de ex.
  eticheta, rămân intacte), **AI** (model local de segmentare `rembg`, ISNet
  implicit, pentru fotografii pe fundal real) și **auto** (implicit: uniform
  când marginea are o singură culoare, altfel AI).
- Fragmentele mici rămase lângă produs se elimină (`bg_min_island`). Când
  modelul AI pierde o parte din produs pe fundal uniform (`bg_lost_warning`),
  rândul primește avertisment și este **debifat**.
- Până la `bg_sync_limit` imagini (implicit 5, imaginea principală și cele din
  galerie numărate separat) se face previzualizare; peste limită selecția intră
  într-o **coadă** procesată pe loturi (`bg_batch`) de o acțiune programată.
  Imaginile eșuate rămân neschimbate și marcate *Failed*.
- Rezultatul se salvează WebP (PNG dacă serverul nu are encoder WebP; JPEG dacă
  se setează o culoare de fundal `bg_color`), cu variantele redimensionate
  regenerate. Starea apare în câmpul *Background Removal*
  (*Pending / Removed / Failed*).
- `rembg` este dependență Python opțională (nedeclarată în manifest); fără ea,
  fundalurile uniforme se decupează totuși după culoare. Modelul se descarcă la
  prima utilizare și se ține încărcat un singur model per worker.
  `birefnet-general` nu mai e în lista wizardului (epuiza memoria workerului).

**Eliminare filigran (nou față de pagina veche)**

- Acțiunea **Remove Watermark** pe produse și imagini de produs. Filigranul este
  **învățat din imaginile selectate** (nu desenat manual) și apoi inversat. Se
  elimină un filigran semi-transparent al cărui amestec a scăzut și
  transparența imaginii (masca exactă a logo-ului rămâne în canalul alfa); un
  filigran care nu a lăsat urmă în transparență este raportat ca negăsit.
- Wizardul arată filigranul detectat (*Detected Watermark*), apoi fiecare imagine
  înainte / după; imaginea curățată se salvează opacă. Previzualizare până la
  `wm_sync_limit` imagini (implicit 10), peste limită coada, cu filigranul
  învățat păstrat ca înregistrare *Learned Image Watermark*. Se învață din cel
  mult `wm_learn_limit` imagini (60); lot `wm_batch` (20).
- Wizardul se deschide cu un avertisment juridic: se elimină doar un filigran
  propriu sau cu acordul scris al titularului drepturilor (Directiva
  2001/29/CE, art. 7). Pentru pozele furnizorilor se cer imaginile fără
  filigran. Pe fundaluri simple pot rămâne contururi slabe ale logo-ului la zoom
  100%. Necesită biblioteca `numpy`.

**Imagini duplicate**

- Detectează înregistrările `product.image` cu conținut identic, după checksum-ul
  SHA1 deja calculat de Odoo (fără decodarea imaginilor, o singură interogare
  indexată). Se șterg doar copiile care se repetă în același produs/variantă;
  se păstrează imaginea afișată prima pe site (`sequence, id` minim) și
  imaginile cu `video_url`. Aceeași poză pe mai multe produse este raportată,
  **niciodată ștearsă**.
- Meniuri (doar administratori): Website → eCommerce → Produse →
  **Imagini duplicate** (lista se deschide filtrată pe grupurile curățabile;
  filtrul *Shared Across Products* arată pozele folosite pe mai multe produse;
  butonul *Images* deschide imaginile grupului) și **Remove Duplicated Images**
  (wizard cu previzualizarea exactă a ce se șterge și ce se păstrează;
  poate rula și fără selecție, pe tot catalogul).
- Nu detectează aceeași poză reexportată sau redimensionată (checksum diferit).
  Curăță catalogul, dar eliberează puțin spațiu pe disc; pentru spațiu se
  folosește recomprimarea.
- La instalare, un hook completează `image_checksum` printr-un singur `UPDATE`
  SQL; ulterior: `env["product.image"]._dedup_backfill_checksums()`.

**Recomprimare**

- Recomprimă imaginile „originale" (implicit `image_1920`, `image_variant_1920`)
  la maximum `max_dim` (1920 px), JPEG progresiv de calitate `quality` (85),
  doar pentru originale mai mari de `min_size` (100 KB), în loturi de `batch`
  (50). Rezultatul se păstrează doar dacă e efectiv mai mic.
- Detectează transparența reală și păstrează imaginile cu transparență ca WebP
  (PNG optimizat dacă Pillow nu are encoder WebP); GIF-urile animate sunt sărite.
- Scrie prin înregistrarea proprietară, deci Odoo regenerează variantele
  (`image_1024/512/256/128`); variantele deja stocate se recodează separat
  (`variant_quality`, `variant_min_size`), fără propagare spre original.
- Atașamentele procesate se marchează (`deltatech_image_optimized`) și sunt
  sărite ulterior; imaginile noi sau schimbate sunt reluate automat.
- Acțiunea programată zilnică este **dezactivată implicit** și își păstrează
  starea la upgrade (`noupdate="1"`); se rulează întâi manual pe staging. La
  final se apelează garbage collection-ul filestore-ului.
- Metodele de batch întorc `freed` (suma diferențelor per atașament, supraestimată
  când aceeași poză apare pe mai multe înregistrări) și `freed_disk` (doar
  fișierele nepartajate — cifra de comunicat). Filestore-ul crește înainte să
  scadă; spațiul revine după GC.
- `force_jpeg` (implicit 0) ignoră canalul alfa: transparența devine
  **neagră, ireversibil**. De activat doar după verificarea catalogului
  (metoda `_dt_image_recompress` permite proba fără scriere); un eșantion real
  a arătat 32% imagini cu alfa într-un catalog presupus fără transparență.
- Parametrii se configurează în Settings → Technical → System Parameters, chei
  cu prefixul `deltatech_image_optimize.` (detaliat în fișa consultant și în
  `readme/CONFIGURE.md`).

#### 3. Dependențe

- `base`
- `website_sale`: definește `product.image` (dependență din 19.0.1.9.0).

Dependențe Python opționale (nedeclarate în manifest): `rembg[cpu]` (model AI de
decupare) și `numpy` (eliminare filigran).

#### 4. Componente Cheie

**Modele**

- `ir.attachment` (extins): câmpul `deltatech_image_optimized` (Datetime) și
  metodele de recomprimare/optimizare:
  - `_dt_image_optimize_params()`: citește configurația din
    `ir.config_parameter`.
  - `_dt_image_recompress()`: funcție pură de recomprimare a octeților unei
    imagini (JPEG/WebP/PNG), fără scriere.
  - `_dt_image_shared_file()`: verifică dacă fișierul din filestore e partajat
    (același `store_fname`), pentru `freed_disk`.
  - `_dt_image_optimize_run()` / `_dt_image_optimize_variants_run()` /
    `_dt_image_optimize_cron()`: lot pe originale, lot pe variante, respectiv
    punctul de intrare al acțiunii programate (originale, variante, apoi GC).
  - `_dt_bg_remove_cron()` și `_dt_wm_remove_cron()`: punctele de intrare ale
    cozilor pentru eliminarea fundalului, respectiv a filigranului.
- `deltatech.image.background.mixin` (abstract): `bg_removal_state` și
  `action_dt_remove_background()`; moștenit de `product.template` și
  `product.image` (ambele extinse).
- `deltatech.image.background.wizard` (+ `.line`): previzualizare înainte/după,
  `action_refresh()` și `action_apply()` pentru eliminarea fundalului.
- `deltatech.image.watermark.profile` (*Learned Image Watermark*): filigranul
  învățat (`kind`, `model_data` JSON, `image_count`, `preview`), folosit de coadă.
- `deltatech.image.watermark.wizard` (+ `.line`): previzualizare, `action_apply()`
  pentru eliminarea filigranului; `action_dt_remove_watermark()` pe mixin.
- `product.image` (extins): `image_checksum` (indexat), `duplicate_count`,
  `_dedup_backfill_checksums()`, `action_view_duplicates()`.
- `deltatech.product.image.duplicate` (vedere SQL, `_auto = False`): o linie per
  conținut distinct (copii, produse, imagini eliminabile);
  `action_view_images()` și `action_clean()`.
- `deltatech.product.image.dedup` (wizard): previzualizare și aplicare a
  ștergerii (`action_apply()`).
- Fără modele ORM în `bg_mask.py` și `watermark.py`: logică pură (Pillow, numpy)
  pentru măștile de decupare și învățarea/inversarea filigranului.

**Vizualizări**

- `view_image_background_wizard_form`: wizardul de eliminare a fundalului
  (metodă, model AI, previzualizare pe carouri, avertismente); stil în
  `static/src/scss/image_background_wizard.scss` (`web.assets_backend`).
- `view_image_watermark_wizard_form`: wizardul de eliminare a filigranului
  (avertisment juridic, filigran detectat, previzualizare).
- `view_product_image_duplicate_list` / `view_product_image_duplicate_search`:
  lista și căutarea grupurilor de imagini duplicate.
- `view_product_image_dedup_form` / `view_product_image_dedup_list`: wizardul de
  ștergere a duplicatelor și lista imaginilor vizate.
- Meniurile `menu_product_image_duplicate` și `menu_product_image_dedup` (sub
  `website_sale.menu_catalog`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_dt_image_optimize` (*Image Optimizer: recompress oversized images*):
  zilnic, **dezactivat implicit**; apelează `_dt_image_optimize_cron()`.
- `ir_cron_dt_image_remove_background` (*Image Optimizer: remove product image
  background*): din oră în oră, **activ implicit**; procesează coada, apelează
  `_dt_bg_remove_cron()`.
- `ir_cron_dt_image_remove_watermark` (*Image Optimizer: remove product image
  watermark*): din oră în oră, **activ implicit**; apelează `_dt_wm_remove_cron()`.
- Acțiuni server legate de `product.template` și `product.image` (grup
  `product.group_product_manager`): `action_product_template_remove_background`,
  `action_product_image_remove_background`,
  `action_product_template_remove_watermark`,
  `action_product_image_remove_watermark`.
- Parametri de sistem (`data/ir_config_parameter.xml`, `noupdate="1"`):
  recomprimare — `quality`, `max_dim`, `min_size`, `batch`, `flush_every`,
  `target_fields`, `variant_fields`, `variant_quality`, `webp_quality`,
  `force_jpeg`, `variant_min_size`; fundal — `bg_method`, `bg_model`,
  `bg_tolerance`, `bg_min_island`, `bg_lost_warning`, `bg_crop`, `bg_margin`,
  `bg_color`, `bg_sync_limit`, `bg_batch`; filigran — `wm_sync_limit`,
  `wm_learn_limit`, `wm_batch`.

#### 5. Conexiuni

- [deltatech_website_watermark](../deltatech_website_watermark/index.md): legat
  tematic (filigran pe imagini); acest modul folosește aceeași tehnică de
  înregistrare a plugin-ului WebP pentru Pillow (precedent menționat în cod).
