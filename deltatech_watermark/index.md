# Watermark (Filigran) (localizat la `deltatech_watermark/index.md`)

- **Nume Tehnic:** `deltatech_watermark`
- **Versiune:** `19.0.3.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_watermark
- **Cale Locală:** `odoo-addons/deltatech/deltatech_watermark`
- **Ultima Ingestie:** `2026-11-02`

#### 1. Sumar

Acest modul permite încărcarea o singură dată, în setări, a imaginii de filigran (watermark) a companiei, pentru ca alte module să o folosească acolo unde este nevoie. Modulul stochează imaginea pe fiecare companie și o afișează în Setări generale. El nu modifică singur nicio pagină sau vreun document: modulul [deltatech_website_watermark](../deltatech_website_watermark/index.md) o folosește pentru a marca pozele de produs din magazinul online.

#### 2. Funcționalități Cheie

- **Un filigran pentru fiecare companie**: fiecare companie își păstrează propria imagine de filigran. Într-o bază de date multi-company, setarea se aplică companiei curente.
- **Configurare în Setări generale**: imaginea se încarcă în *Settings > General Settings*, secțiunea *Companies*, câmpul **Watermark image**, cu previzualizare. Pentru companii cu filigrane diferite, se schimbă compania activă și se repetă încărcarea.
- **Bază pentru Website Watermark**: modulul de website aplică filigranul pe pozele de produs ale magazinului la afișare, astfel încât imaginile originale rămân curate. Dacă imaginea este goală, modulele dependente afișează pozele nemodificate.
- **Dependențe minime**: depinde doar de setările standard (`base_setup` și `web`), deci alte module pot construi pe el fără să aducă website-ul.

#### 3. Dependențe

- `base_setup`
- `web`

#### 4. Componente Cheie

**Modele**

- `res.company`: extins cu câmpul binar `watermark_image` (imaginea de filigran a companiei).
- `res.config.settings`: expune `watermark_image` câmp `related` pe `company_id.watermark_image`, editabil, în Setări generale.

**Vizualizări**

- `res_config_settings_view.xml`: adaugă câmpul de filigran în Settings > General Settings, secțiunea Companies.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- [deltatech_website_watermark](../deltatech_website_watermark/index.md): modul de extensie care depinde de acest modul și aplică filigranul pe pozele de produs din website.
