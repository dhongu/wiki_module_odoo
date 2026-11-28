# Website Image Watermark (localizat la `deltatech_website_watermark/index.md`)

- **Nume Tehnic:** `deltatech_website_watermark`
- **Versiune:** `20.0.1.0.10`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_website_watermark
- **Cale Locală:** `odoo-addons/bitshop/deltatech_website_watermark`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aplică filigranul companiei pe imaginile de produs afișate în magazinul online, în momentul randării. Imaginile originale rămân curate în back-office, iar magazinul își protejează vizual pozele fără a modifica fișierele încărcate.

#### 2. Funcționalități Cheie

- Filigran centrat, semitransparent (opacitate 20%), scalat la imagine, pe imaginile de produs din magazin și pe celelalte dimensiuni calculate din `image.mixin`; miniaturile mici (coș, liste scurte) rămân curate.
- Filigranul se încarcă per companie în *Settings → General Settings*, secțiunea **Companies**, câmpul **Watermark image** (PNG transparent, recomandat); fără el filigranarea nu se aplică.
- Dezactivare pe produs (bifa **Has Watermark**, tab-ul **Sales**, grupul **Ecommerce Shop**, pentru pozele care au deja filigran, inclusiv cele din Ecommerce Media) sau pe partener (bifa **Use Watermark**, tab-ul **Sales & Purchase**, implicit bifată), de exemplu pentru un revânzător care primește poze curate.
- O variantă cu poză proprie o afișează filigranată; fără poză proprie se afișează poza produsului.
- Suport WEBP: formatul WEBP se păstrează, celelalte se trimit ca JPEG (un PNG transparent își pierde transparența).
- Performanță: cache în memorie al filigranului și al dimensiunilor pregătite, compoziție alpha pe RGBA, răspuns 304 Not Modified din ETag fără regenerarea filigranului.
- Fluxul pas-cu-pas, cu capturi, este în fișa consultant.

#### 3. Dependențe

- `website_sale`
- [deltatech_watermark](../deltatech_watermark/index.md)

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` (completat cu `USAGE.md`), deci analiza componentelor este sumară.

**Modele**

- `deltatech.watermark.mixin` (abstract): câmpul calculat `watermark_image` și `has_watermark`; aplică filigranul pe imagine.
- `product.template`, `product.product`, `product.image`: folosesc mixin-ul (variantele și imaginile suplimentare își calculează propriul filigran).
- `res.partner`: câmpul `use_watermark` (implicit `True`).
- `ir.binary`: la servirea imaginii decide dacă se aplică filigranul și înlocuiește fluxul cu imaginea filigranată.

**Vizualizări**

- `product_template_form_view`: adaugă `has_watermark` pe formularul produsului.
- `view_partner_form`: adaugă `use_watermark` pe formularul partenerului.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

- [deltatech_watermark](../deltatech_watermark/index.md): modulul de bază care oferă setarea filigranului companiei.
- `website_sale`: ale cărui imagini de produs sunt filigranate de acest modul.
