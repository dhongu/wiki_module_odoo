# Slovakia - City from ZIP (localizat la `l10n_sk_zip/index.md`)

- **Nume Tehnic:** `l10n_sk_zip`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-slovakia/tree/19.0/l10n_sk_zip
- **Cale Locală:** `odoo-addons/l10n-slovakia/l10n_sk_zip`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă lista localităților (obce) din Slovacia, cu cod poștal și regiune, și completează automat orașul și regiunea adreselor slovace pe baza codului poștal (PSČ). Astfel, adresele de contact și datele de livrare către Slovacia se introduc mai repede și fără erori, fără căutare manuală a regiunii.

#### 2. Funcționalități Cheie

- Listă de localități slovace cu cod poștal, legate de regiunile Slovaciei; datele provin din GeoNames (licență Creative Commons Attribution 4.0).
- Slovacia este setată cu „oraș obligatoriu din listă” (*enforce cities*): orașul unei adrese slovace se alege din listă.
- Pe formularul de contact, la introducerea codului poștal al unei adrese din Slovacia se completează orașul și regiunea. Dacă un cod poștal este comun mai multor localități, se completează doar regiunea; orașul se alege din listă sau este ales automat când numele introdus corespunde uneia dintre localități (comparație fără diacritice și fără diferențe de majuscule).
- Codul poștal este normalizat la formatul `NNN NN` (ex. `11000` devine `110 00`).
- Acțiunea *Slovakia: set city from ZIP* pe contacte (listă și formular, pentru grupul de manageri de parteneri) leagă contactele slovace existente sau importate de orașul codului lor poștal și completează regiunea.
- La instalare, contactele slovace existente sunt legate direct pe o bază mică; pe o bază mare, rulează în loturi acțiunea programată *Slovakia: link contacts to the city of their ZIP*, care se dezactivează singură la final.
- Orice formular care aplică regulile de cod poștal ale contactului (de ex. datele de livrare ale unui AWB) primește regiunea completată, deci expedierea spre Slovacia nu cere căutare manuală.
- Localitățile se consultă la **Contacte → Configurare → Localizare → Orașe** (căutare după cod poștal).

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): metode `_l10n_sk_city_from_zip` (returnează orașul și regiunea pentru un cod poștal), onchange pe `zip` pentru adrese din SK, `l10n_sk_fix_city_from_zip` (acțiunea pe contacte existente) și `_cron_l10n_sk_relink_partners` (relegare în loturi de 5000).
- `res.city` (date): localități slovace cu cod poștal și regiune, încărcate din `data/res.city.csv`.

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește lista de orașe și formularul de contact standard.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip`: acțiune server pe `res.partner` (listă și formular), *Slovakia: set city from ZIP*.
- `ir_cron_relink_partners`: acțiune programată, *Slovakia: link contacts to the city of their ZIP*; inactivă implicit, pornită de hook-ul de post-instalare pe baze mari, rulează din oră în oră și se oprește singură.

#### 5. Conexiuni

