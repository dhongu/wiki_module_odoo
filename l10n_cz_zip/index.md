# Czechia - City from ZIP

- **Nume Tehnic:** `l10n_cz_zip`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-czechia/tree/19.0/l10n_cz_zip
- **Cale Locală:** `odoo-addons/l10n-czechia/l10n_cz_zip`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă lista localităților din Cehia (obce) cu codul poștal (PSČ) și regiunea lor și completează automat orașul și regiunea adreselor cehe pe baza codului poștal. Adresele din Cehia devin astfel consistente, iar expedierile (de exemplu AWB) pot fi făcute fără căutarea manuală a regiunii.

#### 2. Funcționalități Cheie

- Lista localităților cehe cu cod poștal, legate de regiunile Cehiei; datele provin de la [GeoNames](https://www.geonames.org) (licență Creative Commons Attribution 4.0).
- Cehia este setată cu „oraș impus”: orașul unei adrese cehe se alege din listă.
- Pe formularul contactului, la introducerea codului poștal se completează orașul și regiunea. Dacă un cod poștal aparține mai multor localități, se completează doar regiunea, iar orașul se alege din listă; dacă numele orașului introdus se potrivește (fără diacritice și indiferent de majuscule), localitatea este aleasă automat.
- Acțiunea *Czechia: set city from ZIP* (Acțiuni, pe liste și formulare de contacte, pentru grupul de manageri de parteneri) leagă contactele cehe existente sau importate de orașul codului lor poștal și completează regiunea.
- La instalare, contactele cehe sunt legate direct pe o bază mică; pe o bază mare, prin acțiunea programată *Czechia: link contacts to the city of their ZIP*, rulată pe loturi, care se dezactivează singură la final.
- Orice formular care aplică regulile de cod poștal ale contactului (de exemplu detaliile de livrare ale unui AWB) primește regiunea completată.
- Listarea localităților: **Contacte → Configurare → Localizare → Orașe**, cu căutare după codul poștal.
- Fișa de consultant (în engleză, cu capturi) conține fluxul pas cu pas.

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): calculează orașul și regiunea din codul poștal (onchange pe cod poștal), acțiunea `l10n_cz_fix_city_from_zip` și relegarea pe loturi pentru cron (`_cron_l10n_cz_relink_partners`).

**Vizualizări**

- Fără vizualizări proprii; modulul folosește formularele standard ale contactului și lista de orașe (`res.city`).

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip` (acțiune server): *Czechia: set city from ZIP*, pe contacte (listă și formular).
- `ir_cron_relink_partners` (cron): *Czechia: link contacts to the city of their ZIP*, la fiecare oră, inactiv implicit; pornit de hook-ul de post-instalare pe baze mari și se dezactivează singur la final.

#### 5. Conexiuni

- `base_address_extended`: oferă modelul `res.city` și câmpurile de adresă extinse pe care se sprijină modulul.
