# Bulgaria - City from ZIP (localizat la `l10n_bg_zip/index.md`)

- **Nume Tehnic:** `l10n_bg_zip`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-bulgaria/tree/20.0/l10n_bg_zip
- **Cale Locală:** `odoo-addons/l10n-bulgaria/l10n_bg_zip`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Încarcă localitățile bulgare cu codul poștal și provincia și completează automat orașul și provincia adreselor din Bulgaria pe baza codului poștal introdus. Utilizatorii nu mai caută manual localitatea, iar livrările (de exemplu AWB-urile) pot fi trimise fără completări manuale.

#### 2. Funcționalități Cheie

- Încarcă cele 28 de provincii (oblasti) cu cod ISO 3166-2:BG; provinciile introduse manual (latin sau chirilic) sunt reutilizate, iar duplicatele sunt îmbinate. Denumirile localităților sunt în latină (transliterare oficială), cu traducerea bulgară în chirilic pentru utilizatorii în limba bulgară; prefixul "BG-" al codului poștal este ignorat.
- Listă de localități cu cod poștal, legate de provincia țării, din [GeoNames](https://www.geonames.org) (licență Creative Commons Attribution 4.0).
- Țara este setată pe *oraș obligatoriu din listă* (enforce cities): orașul unei adrese se alege din lista încărcată.
- Pe formularul contactului, la introducerea codului poștal se completează orașul și provincia. Dacă un cod poștal este comun mai multor localități, se completează doar provincia, iar orașul se alege din listă; numele orașului, dacă se potrivește (fără diacritice și indiferent de majuscule), alege localitatea.
- Acțiunea *Actions → ... : set city from ZIP* pe contacte leagă contactele existente sau importate de orașul codului lor poștal și completează provincia.
- La instalare, contactele existente sunt legate direct (bază mică) sau în loturi, prin acțiunea programată de legare a contactelor (bază mare; se dezactivează singură la final).
- Orice formular care rulează regulile de cod poștal ale contactului (de exemplu detaliile de livrare ale unui AWB) primește provincia completată.
- Lista localităților se consultă la **Contacts → Configuration → Localization → Cities**. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): onchange pe codul poștal, acțiunea de completare a orașului și metodele de legare în loturi a contactelor existente.
- `res.city` (date): localitățile încărcate din `data/res.city.csv`.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii; folosește formularul contactului și lista de orașe din Contacts → Configuration → Localization → Cities.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip`: acțiune server pe contacte (listă și formular) care completează orașul și provincia din codul poștal; necesită grupul de manager de parteneri.
- `ir_cron_relink_partners`: acțiune programată (din oră în oră, inactivă implicit) care leagă contactele de orașul codului poștal în loturi pe baze mari și se dezactivează la final.

#### 5. Conexiuni

- `base_address_extended`: furnizează câmpurile de adresă extinse și lista de orașe pe care o completează modulul.
- [l10n_ro_zip](../l10n_ro_zip/index.md): modulul echivalent pentru România.
