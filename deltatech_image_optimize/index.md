# Image Optimizer (localizat la `deltatech_image_optimize/index.md`)

- **Nume Tehnic:** `deltatech_image_optimize`
- **Versiune:** `20.0.1.14.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_image_optimize
- **Cale Locală:** `odoo-addons/deltatech/deltatech_image_optimize`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul curăță și ușurează imaginile de produs din catalogul eCommerce, în patru operații pe aceleași imagini: eliminarea fundalului, eliminarea unui watermark, ștergerea imaginilor duplicate și recomprimarea imaginilor supradimensionate. Totul rulează pe serverul Odoo; nicio imagine nu este trimisă către un serviciu extern. Imaginea originală nu este păstrată, de aceea rezultatul se verifică înainte de aplicare.

#### 2. Funcționalități Cheie

- **Eliminare fundal**: *Actions → Remove Image Background* pe lista de produse (pe un produs include și galeria eCommerce) sau *Background → Remove Background* din editorul website, pentru o singură imagine. Un asistent arată înainte / după, pe tablă de șah; se debifează imaginile slab decupate, apoi **Apply**.
  - Metode: **Uniform background** (după culoarea marginii, fără model AI), **AI model** (`rembg`, ISNet implicit, bibliotecă opțională) și **Automatic** (implicit); **Frame only (keep background)** încadrează produsul într-un pătrat fără a elimina fundalul.
  - Până la `bg_sync_limit` imagini (implicit 5) există previzualizare; o selecție mai mare se pune la coadă și o procesează acțiunea programată, în loturi de `bg_batch`. Imaginile care eșuează rămân neschimbate și sunt marcate *Failed*.
  - Când modelul AI pierde o parte din produs pe un fundal uniform, rândul este avertizat și debifat.
  - Rezultat salvat WebP (PNG fără encoder WebP, JPEG pentru fundal plin), cu variantele redimensionate.
- **Eliminare watermark**: *Actions → Remove Watermark*; watermark-ul semi-transparent este învățat din imaginile selectate și inversat, cu previzualizare până la `wm_sync_limit` și coadă peste. Se aplică doar imaginilor al căror watermark ai dreptul să-l elimini.
- **Imagini duplicate**: *Website → eCommerce → Products → Duplicated Images* (administrator) listează grupurile de conținut identic byte cu byte; **Remove Duplicated Images** păstrează imaginea afișată prima pe fiecare produs. O imagine partajată între produse este raportată, niciodată ștearsă.
- **Recomprimare**: acțiunea programată *Image Optimizer: recompress oversized images* (inactivă după instalare) reduce originalele la maximum 1920 px, re-codifică în JPEG progresiv (calitate 85) sau WebP pentru transparență, apoi recomprimă variantele; rezultatul se păstrează doar dacă este mai mic. Parametrii sunt în *Settings → Technical → Parameters → System Parameters*, chei `deltatech_image_optimize.*`.
- `force_jpeg` este distructiv (transparența devine neagră definitiv) și nu se activează fără verificarea catalogului.

Fluxul pas-cu-pas, cu capturi, se găsește în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- `website_sale`

Dependență Python opțională, nedeclarată în manifest: `rembg` (pentru fotografii pe fundal real); pentru eliminarea watermark-ului este necesar `numpy`.

#### 4. Componente Cheie

**Modele**

- `deltatech.image.background.mixin`: logica de eliminare a fundalului, moștenită de `product.template`, `product.product` și `product.image`.
- `deltatech.image.background.wizard` / `deltatech.image.background.wizard.line`: asistentul cu previzualizare înainte / după.
- `deltatech.image.watermark.profile`: watermark-ul învățat, folosit de acțiunea programată pentru imaginile din coadă.
- `deltatech.image.watermark.wizard` / `deltatech.image.watermark.wizard.line`: asistentul de eliminare a watermark-ului.
- `deltatech.product.image.duplicate`: grupurile de imagini cu conținut identic.
- `deltatech.product.image.dedup`: asistentul de ștergere a duplicatelor.
- `ir.attachment` (extins): recomprimarea imaginilor supradimensionate.
- `product.image` (extins): checksum pentru detectarea duplicatelor.

**Vizualizări**

- `view_image_background_wizard_form`: asistentul Remove Image Background.
- `view_image_watermark_wizard_form`: asistentul Remove Watermark.
- `view_product_image_duplicate_list` / `view_product_image_duplicate_search`: lista și filtrele pentru Duplicated Images.
- `view_product_image_dedup_form` / `view_product_image_dedup_list`: asistentul Remove Duplicated Images.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_dt_image_optimize` (*Image Optimizer: recompress oversized images*): zilnic, dezactivată implicit.
- `ir_cron_dt_image_remove_background` (*Image Optimizer: remove product image background*): procesează coada în loturi.
- `ir_cron_dt_image_remove_watermark` (*Image Optimizer: remove product image watermark*): procesează coada de watermark.
- `action_product_template_remove_background` / `action_product_image_remove_background`: acțiuni server *Remove Image Background*.
- `action_product_template_remove_watermark` / `action_product_image_remove_watermark`: acțiuni server *Remove Watermark*.

#### 5. Conexiuni

- [deltatech_website_watermark](../deltatech_website_watermark/index.md): modul din aceeași suită legat tematic de watermark-urile imaginilor; folosește aceeași tehnică de înregistrare a plugin-ului WebP pentru Pillow.
