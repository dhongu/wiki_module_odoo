# Germany - City from ZIP

- **Nume Tehnic:** `l10n_de_zip`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-germany/tree/19.0/l10n_de_zip
- **Cale Locală:** `odoo-addons/l10n-germany/l10n_de_zip`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul încarcă lista localităților din Germania (Orte) cu codul poștal și landul (regiunea) și completează automat orașul și regiunea pe adresele germane, pornind de la codul poștal (Postleitzahl). Datele provin de la GeoNames (licență Creative Commons Attribution 4.0). Operatorul scrie mai puțin și face mai puține greșeli, iar expedierile spre Germania au regiunea completată fără căutare manuală.

#### 2. Funcționalități Cheie

- Lista localităților germane cu cod poștal, legate de landurile Germaniei (sursa: GeoNames), vizibilă la **Contacte → Configurare → Localizare → Orașe**.
- Germania este setată să impună orașele: orașul unei adrese germane se alege din listă.
- Pe formularul de contact, la introducerea codului poștal se completează orașul și regiunea. Dacă un cod poștal este comun mai multor localități, se completează doar regiunea; orașul se alege din listă sau este ales automat când numele introdus se potrivește (fără diacritice și indiferent de majuscule).
- Codul poștal are 5 cifre: un zero inițial pierdut la import este reintrodus (`1000` devine `01000`).
- Acțiunea **Germany: set city from ZIP** (din meniul Acțiuni al contactelor, listă și formular) leagă contactele germane existente sau importate de orașul codului lor poștal și completează regiunea.
- La instalare, contactele germane sunt legate direct pe o bază mică; pe o bază mare, acțiunea programată **Germany: link contacts to the city of their ZIP** le leagă pe loturi (5000) și se dezactivează singură la final. Un contact care nu poate fi scris este înregistrat în jurnal și sărit, fără a opri lotul.
- Orice formular care aplică regulile de cod poștal ale contactului (de exemplu datele de livrare ale unui AWB) primește regiunea completată.

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): onchange pe `zip` pentru completarea orașului și regiunii, metoda `l10n_de_fix_city_from_zip` (acțiunea în masă) și metoda cron `_cron_l10n_de_relink_partners`.

**Vizualizări**

- Modulul nu definește vizualizări proprii; folosește lista de orașe (`res.city`) și formularul de contact existente.

**Acțiuni Automate / Acțiuni Server**

- `action_partner_fix_city_from_zip` (acțiune server): *Germany: set city from ZIP*, pe contacte, pentru grupul Contact Creation/Partner Manager.
- `ir_cron_relink_partners` (cron, la oră, inactiv implicit): *Germany: link contacts to the city of their ZIP*; activat de hook la instalare pe baze mari, se dezactivează după terminare.

#### 5. Conexiuni

- `base_address_extended`: oferă `city_id` și regulile de adresă pe care modulul le completează.
