# Romania - Postal Codes, Streets of Small Towns (localizat la `l10n_ro_zip_osm/index.md`)

- **Nume Tehnic:** `l10n_ro_zip_osm`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_zip_osm
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_zip_osm`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Poșta Română are un singur cod poștal pentru orașele sub 50.000 de locuitori și nu publică străzile lor, așa că nomenclatorul de coduri poștale din `l10n_ro_zip` nu are pentru ele nicio stradă. Acest modul adaugă în nomenclator străzile acestor orașe, preluate din OpenStreetMap, fiecare cu codul poștal unic al orașului. Operatorul de parteneri poate astfel căuta strada pe fișa partenerului la fel ca într-un oraș mare, iar codul poștal se completează corect.

#### 2. Funcționalități Cheie

- 15.968 de străzi pentru 269 de orașe mici (Pantelimon, Voluntari, Lugoj, Râmnicu Sărat, Tecuci, Câmpina, Bușteni, Huși și altele), toate cu codul poștal al orașului.
- Numele străzilor provin din OpenStreetMap (licența ODbL), iar codurile poștale de la posta-romana.ro; atribuirea este în Credits. Numele sunt scrise fără diacritice, ca în restul nomenclatorului.
- Se instalează automat împreună cu `l10n_ro_zip` pe o bază nouă; pe o bază unde `l10n_ro_zip` era deja instalat, se instalează manual din Aplicații.
- La instalare, străzile se leagă de județ și, dacă `l10n_ro_city` e instalat, de localitate (și la o instalare ulterioară a acestuia). O stradă deja existentă nu se adaugă a doua oară.
- Nu are meniuri, câmpuri sau setări proprii. Lista se vede în Contacte → Configurare → Localizare → Coduri poștale; pe partener, strada se caută în câmpul Cod poștal de sub localitate (se alege întâi localitatea).
- Lista OpenStreetMap poate fi incompletă; rezerva este rândul orașului, fără stradă (același cod poștal). Orașele care lipsesc din `l10n_ro_city` (de ex. Breaza, Băile Govora) au străzile doar în nomenclator, fără localitate.
- Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_zip](../l10n_ro_zip/index.md)

#### 4. Componente Cheie

**Modele**

- Modulul nu definește modele proprii; inserează rânduri în nomenclatorul `res.zip` din `l10n_ro_zip`.

**Vizualizări**

- Nu are vizualizări proprii (`data` din manifest este gol).

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare rulează `data/res_zip_osm.sql` (fără tranzacția BEGIN/COMMIT, sărind străzile existente), apoi `link_localities` din `l10n_ro_zip` pentru legarea de județ și localitate.

#### 5. Conexiuni

- [l10n_ro_zip](../l10n_ro_zip/index.md): nomenclatorul și câmpul Cod poștal de pe partener, în care apar străzile; scriptul `tools/build_delta.py` de acolo a generat fișierul SQL.
- `l10n_ro_city`: localitățile României, de care se leagă străzile (recomandat, instalat separat).
