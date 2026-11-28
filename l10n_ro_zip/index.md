# Romania - Postal Codes (localizat la `l10n_ro_zip/index.md`)

- **Nume Tehnic:** `l10n_ro_zip`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_zip
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_zip`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă nomenclatorul codurilor poștale din România, gata de folosit imediat după instalare: aproximativ 73.000 de înregistrări, actualizate după posta-romana.ro (noiembrie 2026) pentru toate cele 42 de județe. La completarea adresei unui partener, utilizatorul poate căuta strada și alege codul poștal dintr-o listă filtrată după localitate, iar câmpul standard de cod poștal se completează automat. Se reduc erorile de introducere manuală, utile pentru livrări, facturare și e-Factura.

#### 2. Funcționalități Cheie

- Modelul `res.zip` cu coduri poștale românești: cod poștal, localitate, județ, tip stradă, nume stradă, sector (București), oficiu poștal.
- Nomenclator cu străzile celor 54 de orașe cu coduri pe stradă și oficiul poștal al fiecărei localități; străzile celor 269 de orașe mici la care Poșta are un singur cod vin din OpenStreetMap (ODbL), în modulul separat [l10n_ro_zip_osm](../l10n_ro_zip_osm/index.md), care se instalează automat.
- Datele se importă la instalare dintr-un fișier SQL; fiecare cod e legat de județ după primele două cifre și, când [l10n_ro_city](../l10n_ro_city/index.md) e instalat, de localitatea din nomenclatorul lui.
- Formularul partenerului primește câmpul `Cod Poștal (zip_id)`, filtrat după localitate, care completează automat câmpul standard `zip` la selecție.
- Căutare după codul numeric sau după numele străzii (ordinea cuvintelor nu contează; datele Poștei nu au diacritice).
- Suport pentru sectoarele municipiului București (1–6), cu legătură directă la localitățile corespunzătoare.
- Lista se găsește la **Contacte → Configurare → Localizare → Coduri poștale**; fluxul detaliat este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base_address_extended`
- `contacts`

#### 4. Componente Cheie

**Modele**

- `res.zip`: Codul poștal, cu stradă, localitate, județ, sector și oficiu poștal.
- `res.partner`: Extins cu câmpul `zip_id` și completarea automată a `zip`.
- `res.city`: Extins pentru legarea codurilor poștale de localități.

**Vizualizări**

- `view_res_zip_form`, `view_res_zip_tree`: formularul și lista codurilor poștale (acțiunea `action_res_zip`).
- `view_res_partner_form_inherit_zip`: câmpul de cod poștal din formularul partenerului.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: importă `data/res_zip.sql` la instalare, dacă tabela este goală.

#### 5. Conexiuni

- [l10n_ro_city](../l10n_ro_city/index.md): furnizează localitățile cu care sunt corelate codurile poștale.
- [l10n_ro_zip_osm](../l10n_ro_zip_osm/index.md): străzile orașelor mici din OpenStreetMap, instalat automat.
