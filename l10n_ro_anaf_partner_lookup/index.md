# Romania - ANAF Partner Lookup (localizat la `l10n_ro_anaf_partner_lookup/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_partner_lookup`
- **Versiune:** `19.0.1.3.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_anaf_partner_lookup
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_anaf_partner_lookup`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul caută o firmă românească la ANAF după CUI și întoarce datele partenerului, gata de salvat, astfel încât alte module să poată crea sau verifica un client fără să depindă de alte module de localizare. Pentru firmele din alte țări UE, interoghează VIES după codul de TVA intracomunitar. Nu are meniu, ecran sau buton propriu: este un serviciu comun, folosit indirect de operator (agent de vânzări, casier la Punctul de vânzare, client pe site) prin modulul în care tastează codul. Valoarea de afaceri: date corecte și complete ale clientului pe factură, inclusiv sectorul la București cerut de e-Factura.

#### 2. Funcționalități Cheie

- **CUI așa cum e tastat**: cu sau fără `RO`, cu spații sau cratime; cifra de control se verifică înainte de interogare, deci un cod greșit nu consumă o cerere către ANAF.
- **Date de partener gata de salvat**: denumire, cod fiscal (cu `RO` doar la plătitorii de TVA), stradă cu număr, detalii de adresă, localitate fără prefixul `Mun.`/`Oraș`/`Com.` (satul fără comună), județ, cod poștal, număr de registru comercial (în câmpul NRC) și telefon. Întreaga adresă provine dintr-un singur bloc: sediul social (cel care trebuie să apară pe factură), iar domiciliul fiscal doar când sediul lipsește.
- **Cod poștal după stradă**: când ANAF nu îl furnizează și este instalat `l10n_ro_zip`, se găsește în `res.zip` după stradă și număr (inclusiv intervalele străzilor lungi) sau după localitate.
- **București**: localitatea devine sectorul (`Sector 3`), cum cere e-Factura; dacă ANAF nu îl scrie, se deduce din codul poștal (`030167` este în Sectorul 3). Dacă nici codul poștal nu indică sectorul, localitatea rămâne ca la ANAF, pentru ca verificarea e-Factura să semnaleze lipsa.
- **Orașul din listă**: unde partenerul are `city_id` (cu orașele din `l10n_ro_city`), se alege și acesta după nume și județ, comuna satului sau codul poștal; fără potrivire unică rămâne gol.
- **Diacritice corecte**: literele vechi cu sedilă (`ş`, `ţ`) din răspunsul ANAF sunt convertite în cele cu virgulă (`ș`, `ț`); adresele scrise cu majuscule trec în forma obișnuită.
- **Stare firmă**: plătitor de TVA, inactiv, radiat, pentru ca apelantul să poată avertiza operatorul. Bifa de plătitor de TVA se completează doar dacă partenerul are câmpul `l10n_ro_vat_subjected`.
- **Răspuns clar**: găsit, negăsit, CUI invalid sau ANAF indisponibil, astfel încât apelantul să distingă o firmă inexistentă de un serviciu căzut. Timpul de așteptare este scurt (implicit 10 secunde).
- **VIES (UE)**: `vies_lookup()` interoghează VIES (serviciul gratuit al Comisiei Europene) după codul de TVA intracomunitar cu prefix de țară (`IT…`, `HU…`, `EL` pentru Grecia, `XI` pentru Irlanda de Nord); cifrele de control se verifică înainte. Întoarce denumirea și adresa împărțită în stradă, cod poștal și oraș (țara se setează din prefix; județ și telefon rămân goale, iar NRC nu se completează). Unele state membre (Germania, Spania) confirmă doar validitatea numărului: partenerul primește atunci doar codul fiscal, țara și tipul Companie. Pentru o firmă românească, VIES arată dacă este înregistrată pentru operațiuni intracomunitare. Răspunsul are aceeași formă ca la `lookup()`.
- **Parametri de sistem opționali** (Setări → Tehnic → Parametri → Parametri de sistem, în modul dezvoltator): `l10n_ro_anaf_partner_lookup.url` și `l10n_ro_anaf_partner_lookup.timeout` (secunde, implicit 10) pentru ANAF; `l10n_ro_anaf_partner_lookup.vies_url` și `l10n_ro_anaf_partner_lookup.vies_timeout` pentru VIES. Lista este goală implicit; se adaugă chei doar pentru a schimba o adresă sau un timp de așteptare (număr întreg pozitiv, scurt). Fluxul de verificare cu capturi este în fișa consultant.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.partner.lookup` (model abstract): serviciul de căutare. Metode principale: `normalize_cui`, `is_valid_cui`, `lookup` (întoarce partenerul pregătit, starea de plătitor de TVA și rezultatul interogării), `split_eu_vat` și `vies_lookup` (pentru codurile de TVA din UE), plus ajutoare interne pentru cererea către serviciul ANAF v9 și către VIES, adresă, cod poștal și oraș.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

Module care depind de acest serviciu (din manifestele lor):

- [l10n_ro_pos_partner_efactura](../l10n_ro_pos_partner_efactura/index.md): aduce un client firmă la casa Punctului de vânzare folosind acest serviciu.
- [l10n_ro_partner_autocomplete](../l10n_ro_partner_autocomplete/index.md): completarea automată a partenerului folosește acest serviciu.
- [l10n_ro_website_anaf](../l10n_ro_website_anaf/index.md): completarea datelor firmei în coșul de pe site folosește acest serviciu.

Module folosite opțional, doar dacă sunt instalate (verificat în cod):

- [l10n_ro_zip](../l10n_ro_zip/index.md): furnizează `res.zip`, din care se găsește codul poștal după stradă și orașul după codul poștal.
- `l10n_ro_city`: orașele din listă (`res.city`, câmpul `l10n_ro_municipality`) pentru `city_id`.
- `l10n_ro_config`: definește câmpul `l10n_ro_vat_subjected` pe partener, completat din starea de plătitor de TVA.
