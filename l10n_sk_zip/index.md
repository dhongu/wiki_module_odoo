# Slovakia - City from ZIP (localizat la `l10n_sk_zip/index.md`)

- **Nume Tehnic:** `l10n_sk_zip`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/dhongu/l10n-slovakia/tree/20.0/l10n_sk_zip
- **Cale Locală:** odoo-addons/l10n-slovakia/l10n_sk_zip
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă localitățile (obce) cu codul poștal și regiunea aferentă și completează automat orașul și regiunea adreselor din țara respectivă pe baza codului poștal. Utilizatorul nu mai caută manual orașul sau regiunea, iar adresele rămân uniforme, ceea ce ajută la livrări și rapoarte. Datele provin din GeoNames (Creative Commons Attribution 4.0).

#### 2. Funcționalități Cheie

- Lista localităților cu codul poștal (PSČ), legate de regiunile țării (modulul își încarcă propriile regiuni, `res_country_state_data.xml`); vizibilă la **Contacte → Configurare → Localizare → Orașe**.
- Țara este setată cu opțiunea *impune orașe*: orașul unei adrese se alege din listă.
- Pe fișa contactului, completarea codului poștal setează orașul și regiunea. Dacă același cod este comun mai multor localități, se completează doar regiunea, iar orașul se alege din listă (sau se potrivește după nume, fără diacritice și fără diferență majuscule/minuscule).
- Codul poștal este adus la formatul local NNN NN (ex. `11000` devine `110 00`).
- Acțiunea de pe contacte *Slovakia: set city from ZIP* leagă contactele existente de orașul codului lor poștal și completează regiunea (selectate din listă, meniul *Acțiuni*).
- La instalare, contactele din țară sunt legate direct (bază mică) sau, pe o bază mare, de acțiunea programată *Slovakia: link contacts to the city of their ZIP*, în loturi; aceasta se dezactivează singură la final.
- Orice formular care aplică regulile de cod poștal ale contactului (ex. detaliile de livrare ale unui AWB) primește regiunea completată, deci expedierea poate fi făcută fără căutare manuală.
- Detaliile pas-cu-pas, cu capturi, sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): onchange pe codul poștal, acțiunea de completare a orașului și metodele de relegare în loturi (`l10n_sk_fix_city_from_zip`, `_cron_l10n_sk_relink_partners`).
- `res.city`: înregistrările de localități sunt încărcate din `data/res.city.csv`.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii; folosește formularul de contact și lista de orașe standard.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip`: acțiune server pe contacte (listă și formular), pentru grupul Contact Manager.
- `ir_cron_relink_partners`: acțiune programată orară, inactivă implicit; se activează la instalare doar pe baze mari și se dezactivează singură.

#### 5. Conexiuni

- Nu are legături funcționale cu alte module care au pagină wiki.
