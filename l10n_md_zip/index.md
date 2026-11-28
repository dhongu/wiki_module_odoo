# Moldova - City from ZIP (localizat la `l10n_md_zip/index.md`)

- **Nume Tehnic:** `l10n_md_zip`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-moldova/tree/20.0/l10n_md_zip
- **Cale Locală:** `odoo-addons/l10n-moldova/l10n_md_zip`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Încarcă localitățile din Republica Moldova împreună cu codul poștal și raionul și completează automat orașul și raionul adreselor moldovenești pe baza codului poștal. Operatorul introduce doar codul poștal, iar calitatea adreselor crește, cu mai puțină muncă de introducere a datelor.

#### 2. Funcționalități Cheie

- Lista localităților moldovenești cu cod poștal, legate de cele 37 de subdiviziuni ale Republicii Moldova (ISO 3166-2:MD: raioane, municipiile Chișinău, Bălți și Bender, Găgăuzia, Stînga Nistrului), pe care modulul le adaugă ca județe/state ale Moldovei. Datele provin de la [GeoNames](https://www.geonames.org) (Creative Commons Attribution 4.0).
- Moldova este setată cu **Enforce Cities**: orașul unei adrese moldovenești se alege din listă.
- Pe formularul contactului, la introducerea codului poștal se completează orașul și raionul. Codul poate fi scris `MD-3100`, `MD3100` sau `3100`; când localitatea e identificată, el este rescris `MD-3100`.
- Un cod poștal comun mai multor localități completează doar raionul (dacă toate sunt în același raion); numele orașului, dacă se potrivește (fără diacritice și fără diferențe de majuscule), alege localitatea.
- Acțiunea **Moldova: set city from ZIP** pe contacte (drept Contact: Creation) leagă contactele existente de orașul codului poștal și completează raionul; se selectează companiile, nu persoanele de contact. Contactele din alte țări rămân neschimbate.
- La instalare, contactele moldovenești cu cod poștal sunt legate de oraș: direct pe o bază mică, prin acțiunea programată **Moldova: link contacts to the city of their ZIP**, în loturi, pe una mare (se dezactivează singură la final).
- Meniuri utile: **Contacts → Configuration → Localization → Cities** pentru lista localităților. Pașii detaliați cu capturi sunt în fișa de consultant.

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): normalizarea codului poștal și a orașului, onchange pe cod poștal, metoda `l10n_md_fix_city_from_zip` și relegarea în loturi a contactelor existente.

**Vizualizări**

- Nu adaugă vizualizări proprii; folosește formularul standard de contact și lista **Cities**.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip` (acțiune server): „Moldova: set city from ZIP”, disponibilă în liste și formulare de contacte pentru grupul Contact: Creation.
- `ir_cron_relink_partners` (cron, implicit inactiv): „Moldova: link contacts to the city of their ZIP”, rulează orar în loturi după instalare pe baze mari.

#### 5. Conexiuni

- [l10n_md](../l10n_md/index.md): localizarea contabilă pentru Republica Moldova, complementară acestui modul.
