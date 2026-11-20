# France - City from ZIP (localizat la `l10n_fr_zip/index.md`)

- **Nume Tehnic:** `l10n_fr_zip`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-france/tree/19.0/l10n_fr_zip
- **Cale Locală:** `odoo-addons/l10n-france/l10n_fr_zip`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă lista localităților (comunelor) din Franța, cu cod poștal și regiune, și completează automat orașul și regiunea adreselor franceze pe baza codului poștal. Astfel, adresele partenerilor francezi sunt corecte și uniforme, iar expedierile către Franța nu mai cer căutarea manuală a regiunii.

#### 2. Funcționalități Cheie

- Lista localităților franceze cu cod poștal, legate de regiunile Franței; datele provin de la [GeoNames](https://www.geonames.org) (Creative Commons Attribution 4.0).
- Franța este setată cu „oraș obligatoriu din listă” (*enforce cities*): orașul unei adrese franceze se alege din listă.
- Pe formularul contactului, introducerea codului poștal completează orașul și regiunea. Dacă un cod poștal e comun mai multor localități, se completează doar regiunea, iar orașul se alege din listă; dacă numele orașului introdus coincide cu una dintre ele (fără diacritice și indiferent de majuscule), localitatea este aleasă automat.
- Acțiunea *France: set city from ZIP* (pe lista sau formularul contactelor, meniul Acțiuni) leagă contactele franceze existente sau importate de orașul codului lor poștal și completează regiunea.
- La instalare, contactele franceze sunt legate direct pe o bază mică; pe una mare, această operațiune o preia acțiunea programată *France: link contacts to the city of their ZIP*, în loturi (se dezactivează singură la final).
- Orice formular care rulează regulile de cod poștal ale contactului (de exemplu datele de livrare ale unui AWB) primește regiunea completată.
- Lista localităților se consultă la **Contacte → Configurare → Localizare → Orașe**.
- Fluxul pas-cu-pas, cu capturi de ecran, este în fișa consultantului.

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): completare oraș/regiune din codul poștal (onchange), acțiunea de legare a contactelor existente și metoda lansată în loturi de cron.
- `res.city` (date): localități franceze încărcate din `data/res.city.csv`.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii; folosește formularul contactului și lista orașelor din `base_address_extended`.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip` (*France: set city from ZIP*): acțiune server pe contacte, la cerere, pentru grupul de administratori de parteneri.
- `ir_cron_relink_partners` (*France: link contacts to the city of their ZIP*): rulează din oră în oră, inactivă implicit; este activată la instalare pe baze mari și se dezactivează după terminarea legării.

#### 5. Conexiuni

