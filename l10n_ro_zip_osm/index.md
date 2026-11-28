# Romania - Postal Codes, Streets of Small Towns (localizat la `l10n_ro_zip_osm/index.md`)

- **Nume Tehnic:** `l10n_ro_zip_osm`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_zip_osm
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_zip_osm`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în nomenclatorul de coduri poștale străzile orașelor mici din România, pentru care Poșta Română publică un singur cod poștal pe oraș. Utilizatorul poate alege strada pe fișa partenerului, cu codul poștal al orașului completat corect.

#### 2. Funcționalități Cheie

- 15.968 de străzi pentru 269 de orașe sub 50.000 de locuitori (Pantelimon, Voluntari, Lugoj, Tecuci, Câmpina, Bușteni și altele), fiecare cu codul poștal al orașului.
- Numele străzilor provin din OpenStreetMap, sub licența ODbL; codurile poștale vin de pe posta-romana.ro.
- La instalare străzile se leagă de județ și, dacă `l10n_ro_city` e instalat, de localitate; o stradă existentă nu se adaugă a doua oară.
- Vizualizare: **Contacte → Configurare → Localizare → Coduri poștale**, căutând codul poștal al orașului; un oraș cu un singur rând nu este acoperit.
- Pe partener, după alegerea localității, strada se caută în câmpul de cod poștal de sub localitate; numele nu au diacritice.
- Nu are nimic de configurat; se instalează automat împreună cu `l10n_ro_zip` (sau manual din **Aplicații**, dacă `l10n_ro_zip` era deja instalat).

#### 3. Dependențe

- [l10n_ro_zip](../l10n_ro_zip/index.md)

#### 4. Componente Cheie

**Modele**

- `res.zip` (date adăugate): rândurile cu străzile, încărcate din `data/res_zip_osm.sql` de `post_init_hook`.

**Vizualizări**

- Nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: aplică străzile OSM și le leagă de județ și localitate.

#### 5. Conexiuni

- `l10n_ro_city`: localitățile la care se leagă străzile, dacă e instalat.
