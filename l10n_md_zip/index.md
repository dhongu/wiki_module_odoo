# Moldova - City from ZIP (localizat la `l10n_md_zip/index.md`)

- **Nume Tehnic:** `l10n_md_zip`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-moldova/tree/19.0/l10n_md_zip
- **Cale Locală:** `odoo-addons/l10n-moldova/l10n_md_zip`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă localitățile din Republica Moldova împreună cu codul poștal și raionul și completează automat orașul și raionul unei adrese moldovenești pe baza codului poștal. Utilizatorii scriu codul poștal pe fișa contactului, iar adresa se completează corect și uniform, fără introducere manuală. Contactele existente pot fi legate de localitate printr-o acțiune dedicată.

#### 2. Funcționalități Cheie

- Lista localităților din Moldova cu cod poștal (aprox. 1.750 de înregistrări), legate de cele 37 de subdiviziuni ISO 3166-2:MD (raioane, municipiile Chișinău, Bălți și Bender, Găgăuzia și Stînga Nistrului), adăugate ca state ale Moldovei. Datele provin din GeoNames (CC BY 4.0).
- Moldova este setată să impună orașele (*enforce cities*): orașul unei adrese moldovenești se alege din listă.
- La introducerea codului poștal pe formularul contactului se completează orașul și raionul. Codul poate fi scris `MD-3100`, `MD3100` sau `3100` și, când localitatea este identificată, se rescrie ca `MD-3100`.
- Dacă un cod poștal este comun mai multor localități, se completează doar raionul (când toate sunt în același raion); numele orașului, dacă se potrivește cu una dintre ele (fără diacritice și fără diferență majuscule/minuscule), alege localitatea.
- Acțiunea *Moldova: set city from ZIP* pe contacte (listă și formular, pentru grupul de gestionare a partenerilor) leagă contactele moldovenești existente sau importate de orașul codului poștal. Se selectează companiile, nu persoanele de contact, care preiau adresa companiei; contactele din alte țări rămân neschimbate.
- La instalare, contactele moldovenești cu cod poștal sunt legate direct pe o bază mică, iar pe o bază mare de acțiunea programată, pe loturi (de 5.000), care se dezactivează singură la final.
- Numele localităților vin din GeoNames fără diacritice (*Balti*, *Durlesti*), iar statele le au (*Bălți*, *Chișinău*).
- Fluxul pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): metode pentru determinarea localității din codul poștal (`_l10n_md_city_from_zip`), onchange pe `zip`, completarea în masă (`l10n_md_fix_city_from_zip`, cu scriere pe grupuri și ocolirea contactelor care nu pot fi scrise) și relegarea pe loturi (`_cron_l10n_md_relink_partners`).
- `res.city` și `res.country.state`: doar date (localități și subdiviziuni ale Moldovei), fără modele noi.

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește formularul de contact și lista de orașe din **Contacte → Configurare → Localizare → Orașe**.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip` (acțiune server, *Moldova: set city from ZIP*): se rulează manual din meniul Acțiuni al contactelor.
- `ir_cron_relink_partners` (cron, *Moldova: link contacts to the city of their ZIP*): rulează din oră în oră, dar este inactiv implicit; se activează la instalare doar pe baze mari și se dezactivează când a terminat.

#### 5. Conexiuni

- `base_address_extended`: furnizează orașele (`res.city`) și strada pe câmpuri separate, pe care se sprijină localitățile încărcate.
