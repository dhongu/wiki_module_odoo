# Spain - City from ZIP

- **Nume Tehnic:** `l10n_es_zip`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-spain/tree/19.0/l10n_es_zip
- **Cale Locală:** `odoo-addons/l10n-spain/l10n_es_zip`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă lista localităților din Spania (localidades), cu codul poștal și regiunea, și completează automat orașul și regiunea adreselor spaniole pornind de la codul poștal. Datele provin din GeoNames (licență Creative Commons Attribution 4.0). Utilizatorii nu mai caută manual orașul sau regiunea, iar expedierile către Spania pot fi făcute fără completări manuale.

#### 2. Funcționalități Cheie

- Lista localităților spaniole cu cod poștal, legate de regiunile Spaniei; se consultă la **Contacte → Configurare → Localizare → Orașe**.
- Spania este setată cu *enforce cities*: orașul unei adrese spaniole se alege din listă.
- Pe formularul contactului, introducerea codului poștal (código postal) setează orașul și regiunea. Dacă un cod poștal este comun mai multor localități, se completează doar regiunea, iar orașul se alege din listă; dacă numele orașului introdus se potrivește cu una dintre ele (fără diacritice și indiferent de majuscule), localitatea este aleasă automat.
- Codurile poștale cu zero inițial pierdut la import (ex. `1000`) sunt readuse la 5 cifre (`01000`).
- Acțiunea *Spain: set city from ZIP* (Acțiuni, pe liste și formulare de contacte, pentru grupul de administrare a partenerilor) leagă contactele spaniole existente de orașul codului lor poștal și completează regiunea.
- La instalare, contactele spaniole sunt legate direct pe o bază mică, sau prin acțiunea programată *Spain: link contacts to the city of their ZIP*, în loturi, pe o bază mare (se dezactivează singură la final).
- Orice formular care aplică regulile de cod poștal ale contactului (ex. detaliile de livrare ale unui AWB) primește regiunea completată.
- Documentația și capturile sunt în engleză; fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): normalizare cod poștal și nume oraș, căutare oraș/regiune după cod poștal, onchange pe `zip`, metoda de legare a contactelor existente și metoda lotului pentru cron.
- `res.city` (date): localități spaniole încărcate din `data/res.city.csv`; `res.country` Spania are `enforce_cities` activat.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii; folosește formularul de contact și lista de orașe din `base_address_extended`.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip`: acțiune server pe contacte, rulează `l10n_es_fix_city_from_zip()`.
- `ir_cron_relink_partners`: acțiune programată (orară, inactivă implicit, activată la instalare pe baze mari), leagă contactele spaniole de oraș în loturi de 5000.
- `post_init_hook`: leagă contactele existente la instalare.

#### 5. Conexiuni

