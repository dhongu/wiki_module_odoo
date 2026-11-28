# Romania - ANAF Partner Lookup

- **Nume Tehnic:** `l10n_ro_anaf_partner_lookup`
- **Versiune:** `20.0.1.4.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_anaf_partner_lookup
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_anaf_partner_lookup`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Caută o firmă românească la ANAF după CUI și întoarce datele partenerului, pentru ca alte module să poată crea sau verifica un client fără să depindă de alte module de localizare. Modulul nu are ecran propriu: este folosit, de exemplu, de [l10n_ro_pos_partner_efactura](../l10n_ro_pos_partner_efactura/index.md) pentru a aduce clientul persoană juridică la casă.

#### 2. Funcționalități Cheie

- **CUI așa cum e tastat**: cu sau fără `RO`, cu spații sau cratime; cifra de control se verifică înainte de interogare, deci un cod greșit nu consumă o cerere.
- **Date gata de salvat**: denumire, cod fiscal (cu `RO` doar pentru plătitorii de TVA), stradă cu număr, localitate fără prefixul `Mun.`/`Oraș`/`Com.`, județ, cod poștal, număr de registrul comerțului (în câmpul NRC) și telefon. Adresa vine dintr-un singur bloc: sediul social, iar dacă lipsește, domiciliul fiscal.
- **Cod poștal după stradă**: când ANAF nu îl dă și `l10n_ro_zip` este instalat, se găsește în `res.zip` după stradă și număr, sau cel al satului.
- **București**: localitatea este sectorul (`Sector 3`), cum cere e-Factura; când ANAF nu îl scrie, se citește din codul poștal.
- **Orașul din listă**: dacă partenerul are `city_id`, se alege după nume și județ, comuna satului sau codul poștal; fără potrivire unică rămâne gol.
- **Diacritice corecte**: literele cu sedilă (`ş`, `ţ`) devin cele cu virgulă (`ș`, `ț`).
- **Stare**: plătitor de TVA, TVA la încasare (RTVAI), inactiv, radiat, pentru avertizarea apelantului. Cu `l10n_ro_anaf_partner` instalat, valorile includ și marcajul *TVA la încasare (RTVAI)*.
- **Răspuns clar**: găsit, negăsit, CUI invalid sau ANAF indisponibil; timpul de așteptare este scurt.
- **VIES**: `vies_lookup()` interoghează serviciul gratuit al Comisiei Europene pentru un cod de TVA intracomunitar (cu prefixul țării) și întoarce denumirea și adresa împărțită în stradă, cod poștal, oraș. Unele state (Germania, Spania) spun doar dacă numărul e valid.
- Parametri de sistem opționali: `l10n_ro_anaf_partner_lookup.url`, `.timeout` (10 secunde implicit), `.vies_url`, `.vies_timeout`.
- Configurarea și exemplele cu capturi sunt în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.partner.lookup`: model abstract de serviciu, cu căutarea după CUI la ANAF, normalizarea adresei și `vies_lookup()`.

**Vizualizări**

- Nu are.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_pos_partner_efactura](../l10n_ro_pos_partner_efactura/index.md): folosește căutarea pentru clientul de la casă.
- [l10n_ro_zip](../l10n_ro_zip/index.md): codul poștal după stradă.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): marcajul RTVAI în valorile partenerului.
- `l10n_ro_city`: alegerea orașului din listă.
