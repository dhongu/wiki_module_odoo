# Romania - Postal Codes (localizat la `l10n_ro_zip/index.md`)

- **Nume Tehnic:** `l10n_ro_zip`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_zip
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_zip`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă o bază de date cu codurile poștale din România, gata de folosit imediat după instalare. Sunt importate automat circa 73.000 de coduri poștale, fiecare legat de județul și, acolo unde este posibil, de localitatea corespunzătoare; în orașele mari codurile sunt la nivel de stradă. La completarea adresei unui partener, utilizatorul caută strada în câmpul de cod poștal, iar codul, localitatea, județul și țara se completează automat. Astfel se elimină erorile de introducere manuală și se asigură date de adresă corecte, utile pentru livrări, facturare și e-Factura. Modulul este comercial (licență OPL-1, disponibil pe Odoo Apps) și face parte din suita `l10n_ro_ent`.

#### 2. Funcționalități Cheie

- Adaugă modelul `res.zip` cu circa 73.000 de înregistrări de coduri poștale românești, fiecare conținând: cod poștal, localitate, județ, țară, tip stradă, nume stradă, sector (București), oficiu poștal și adresa oficiului.
- Nomenclatorul este actualizat după posta-romana.ro (noiembrie 2026) pentru toate cele 42 de județe: străzile celor 54 de orașe cu coduri pe stradă și oficiul poștal al fiecărei localități. Străzile celor 269 de orașe mici, la care Poșta are un singur cod, vin din OpenStreetMap (licență ODbL) prin modulul separat [`l10n_ro_zip_osm`](../l10n_ro_zip_osm/index.md), care se instalează automat odată cu acesta.
- Datele sunt importate automat la instalare dintr-un fișier SQL, peste care se aplică un fișier de actualizare (delta); la upgrade, migrările reaplică delta și refac legăturile, iar partenerii își păstrează codul poștal. Județul fiecărui cod se stabilește după primele două cifre, dintr-o listă proprie a modulului (București 01–06, Giurgiu 08).
- Modulul nu mai depinde de `l10n_ro_city`: când acesta este instalat (în aceeași rulare sau ulterior), codurile fără localitate se leagă de localitățile românești din nomenclatorul lui, inclusiv numele scrise cu cratimă sau în forma „Sat (Comună)”. Fără `l10n_ro_city`, codurile au doar județul.
- Consultare: *Contacts → Configuration → Localization → Zip Codes*, cu căutare după primele cifre ale codului.
- Extinde formularul partenerului (`res.partner`) cu câmpul `Cod Poștal (zip_id)`, sub localitate, filtrat după localitatea partenerului. La selecție completează codul poștal standard (`zip`), localitatea, județul și țara; strada și numărul adresei rămân cum au fost introduse. Dacă se schimbă localitatea ulterior sau o actualizare a modulului schimbă codul străzii, strada se alege din nou.
- Căutarea funcționează după codul numeric, după numele străzii sau după tipul străzii. Ordinea cuvintelor nu contează („Nicolae Balcescu” găsește „Balcescu Nicolae”), iar datele oficiului poștal nu au diacritice, deci căutarea fără diacritice este mai sigură.
- Lista derulantă arată strada și, estompat, codul poștal, localitatea, sectorul și județul.
- Suportă sectoarele municipiului București (1–6): localitatea este sectorul, iar câmpul **Sector** reține numărul lui.
- Pașii detaliați, cu capturi de ecran, sunt în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_address_extended`

#### 4. Componente Cheie

**Modele**

- `res.zip`: codul poștal, cu localitate, județ, țară, tip și nume de stradă, sector, oficiu și adresă. Căutarea după nume extinde domeniul standard la stradă și tip de stradă, cuvânt cu cuvânt.
- `res.city`: extins pentru a lega codurile poștale de localitățile românești nou create (cu `l10n_ro_city` instalat în aceeași rulare sau ulterior).
- `res.partner`: extins cu `zip_id`; la selecție completează `zip`, localitatea, județul și țara.

**Vizualizări**

- `view_res_zip_form` / `view_res_zip_tree`: formularul și lista codurilor poștale, cu acțiunea `action_res_zip` și meniul *Zip Codes* sub *Contacts → Configuration → Localization*.
- `view_res_partner_form_inherit_zip`: adaugă câmpul de cod poștal pe formularul partenerului, în adresa extinsă.

**Acțiuni Automate / Acțiuni Server**

- Nu există acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`; datele se încarcă prin `post_init_hook` la instalare (fișierele SQL `res_zip.sql` și `res_zip_delta.sql`), iar la upgrade prin migrările 19.0.0.0.16 și 19.0.0.0.18.

#### 5. Conexiuni

- [l10n_ro_zip_osm](../l10n_ro_zip_osm/index.md): străzile orașelor mici din OpenStreetMap; depinde de acest modul și se instalează automat.
- `l10n_ro_city`: dependență opțională; furnizează localitățile cu care se leagă codurile poștale.
- `base_address_extended`: adresa extinsă a partenerului (localitate, stradă), în care se inserează câmpul de cod poștal.
