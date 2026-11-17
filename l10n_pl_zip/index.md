# Poland - City from ZIP

- **Nume Tehnic:** `l10n_pl_zip`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-poland/tree/19.0/l10n_pl_zip
- **Cale Locală:** `odoo-addons/l10n-poland/l10n_pl_zip`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă lista localităților din Polonia (miejscowości), cu cod poștal și regiune (voievodat), și completează automat orașul și regiunea adreselor poloneze pe baza codului poștal. Astfel, adresele clienților și furnizorilor din Polonia se introduc rapid și uniform, iar expedierile către Polonia nu mai cer căutarea manuală a regiunii.

#### 2. Funcționalități Cheie

- Listă de localități poloneze cu cod poștal, legate de regiunile Poloniei; datele provin de la GeoNames (licență Creative Commons Attribution 4.0).
- Polonia este setată să impună orașele (*enforce cities*): orașul unei adrese poloneze se alege din listă.
- Pe formularul contactului, la introducerea codului poștal (kod pocztowy) se completează orașul și regiunea. Dacă un cod poștal este comun mai multor localități, se completează doar regiunea (când toate sunt în aceeași regiune); dacă numele orașului introdus corespunde uneia dintre ele (fără diacritice și indiferent de majuscule), localitatea este aleasă automat.
- Acțiunea *Poland: set city from ZIP* (Acțiuni pe contacte, în listă sau formular, pentru grupul de gestionare parteneri) leagă contactele poloneze existente sau importate de orașul codului lor poștal și completează regiunea.
- La instalare, contactele poloneze existente sunt legate direct pe o bază mică, sau prin acțiunea programată *Poland: link contacts to the city of their ZIP* în loturi pe o bază mare (se dezactivează singură la final).
- Orice formular care rulează regulile de cod poștal ale contactului (de exemplu datele de livrare ale unui AWB) primește regiunea completată.
- Căutarea localităților după cod poștal: **Contacte → Configurare → Localizare → Orașe**.
- Fișa de consultant (în engleză) conține pașii ilustrați cu capturi.

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): metode pentru determinarea orașului și regiunii din codul poștal polonez (`_l10n_pl_city_from_zip`), onchange pe `zip`, acțiunea `l10n_pl_fix_city_from_zip` și lotul/cron-ul de relegare a contactelor existente.
- `res.city` / `res.country.state` (date): localități poloneze cu cod poștal, încărcate din `data/res.city.csv`; `res.country` Polonia cu `enforce_cities` activ.

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește formularul de contact și lista de orașe din `base_address_extended`.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip` (`ir.actions.server`): *Poland: set city from ZIP*, legată de lista și formularul contactelor.
- `ir_cron_relink_partners` (`ir.cron`): *Poland: link contacts to the city of their ZIP*, la fiecare oră, inactivă implicit; este pornită de hook-ul de instalare pe baze mari și se dezactivează singură când termină.

#### 5. Conexiuni

