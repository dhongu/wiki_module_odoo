# Watermark (Filigran) (localizat la `deltatech_watermark/index.md`)

- **Nume Tehnic:** `deltatech_watermark`
- **Versiune:** `19.0.3.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_watermark`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_watermark`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Acest modul oferă un câmp de bază pentru imaginea sau textul de filigran (watermark) în Odoo. Este conceput să acționeze ca un punct centralizat de stocare și configurare a filigranului, folosit în diferite zone ale sistemului, în special în rapoarte și pe website. Modulul nu aplică el însuși filigranul pe documente sau imagini — el doar pune la dispoziție câmpurile și configurarea necesare, urmând ca module de extensie specifice să realizeze efectiv aplicarea filigranului.

#### 2. Funcționalități Cheie

- **Stocare centralizată a filigranului**: adaugă un câmp dedicat **Watermark** (de obicei pe modelul companiei), oferind un loc standardizat pentru încărcarea imaginii sau definirea textului folosit la filigranarea documentelor sau mediilor corporative.
- **Setări de configurare**: se integrează cu setările standard Odoo (Settings > General Settings) pentru o administrare ușoară, permițând actualizarea rapidă și globală a filigranului corporativ.
- **Fundament pentru extensii**: acționează ca dependență necesară pentru module de filigranare mai specifice, precum cele care aplică filigranul pe imaginile de website sau pe rapoartele PDF generate.

#### 3. Dependențe

- `base_setup`
- `web`

#### 4. Componente Cheie

**Modele**

- `res.company`: extins cu câmpul de filigran (imagine/text) folosit ca sursă centralizată pentru filigranare.
- `res.config.settings`: expune câmpul de filigran în setările generale, pentru administrare globală facilă.

**Vizualizări**

- `res_config_settings_view.xml`: adaugă secțiunea de configurare a filigranului în Settings > General Settings (Business Documents).

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server` definite în acest modul.

#### 5. Conexiuni

- [deltatech_website_watermark](../deltatech_website_watermark/index.md): modul de extensie (din suita bitshop) care depinde de acest modul de bază și aplică filigranul pe imaginile de website.
