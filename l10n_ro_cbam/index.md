# Romania - CBAM (FR-56) (localizat la `l10n_ro_cbam/index.md`)

- **Nume Tehnic:** `l10n_ro_cbam`
- **Versiune:** `19.0.1.7.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_cbam
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cbam`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru Carbon Border Adjustment Mechanism (CBAM), conform Regulamentului (UE) 2023/956. Sprijină importatorii români care introduc pe piața UE produse din categoriile vizate (oțel și fier, aluminiu, ciment, îngrășăminte, electricitate, hidrogen) să declare emisiile de CO₂ incorporate și, din regimul definitiv (1 ianuarie 2026), să determine certificatele CBAM necesare. Este construit peste modulul `esg` (Enterprise), reutilizând `esg.emission.factor` și `esg.emission.source` în loc să le dubleze, și peste `account_intrastat` pentru codul CN.

#### 2. Funcționalități Cheie

- **Profil produs CBAM:** marcaj `cbam_liable`, categorie derivată automat din codul CN (Intrastat), factor de emisie din nomenclator sau override verificat per instalație, țară de origine și preț carbon plătit în origine (certificat sau nu).
- **Nomenclator factori de emisie:** extindere `esg.emission.factor` cu factori impliciți conform Reg. delegat (UE) 2024/3212; sursă ESG dedicată „Importuri CBAM" în Scope 3 (Category 1: Purchased goods).
- **Captură automată la import:** la postarea facturii de la furnizor din afara UE, generează linii CBAM (`l10n.ro.cbam.import.line`) cu cantitatea în tone și emisiile incorporate; smart button pe factură; retururile compensează cu semn negativ.
- **Declarație CBAM:** trimestrială (regim de tranziție, Oct 2023 – Dec 2025) sau anuală (regim definitiv, din 2026); agregă liniile din perioadă, calculează totalurile de emisii și deducerea prețului carbonului plătit în origine.
- **Prețuri de referință ale certificatelor** (`l10n.ro.cbam.certificate.price`): nomenclator introdus manual pe măsură ce Comisia Europeană publică mediile (trimestriale pentru 2026, săptămânale ulterior), folosit automat la calculul declarației.
- **Verificare trimestrială de deținere** (regula 50%, din 2027): declarație definitivă cu trimestru completat funcționează ca checkpoint de deținere, distinct de declarația anuală de predare.
- **Generare notă contabilă** pentru obligația de certificate CBAM (declarație definitivă anuală), cu conturi configurabile (652/462).
- **Export XML** pentru Registrul CBAM (conform Reg. de punere în aplicare (UE) 2023/1570 pentru tranziție) și **raport PDF** „Situație CBAM".
- **Analiză CBAM:** vizualizări grafic/pivot pe emisii, grupate pe lună, categorie și țară de origine.

#### 3. Dependențe

- `esg`
- `account`
- `account_intrastat`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.cbam.import.line`: liniile CBAM generate la postarea facturii de import, cu cantitate în tone, emisii incorporate și deducerea prețului carbonului din origine.
- `l10n.ro.cbam.declaration`: declarația CBAM (tranziție trimestrială sau definitivă anuală/checkpoint trimestrial), cu agregarea liniilor, calculul certificatelor necesare/deținute și generarea notei contabile.
- `l10n.ro.cbam.certificate.price`: nomenclatorul prețurilor de referință ale certificatelor CBAM, publicate periodic de Comisia Europeană.
- `esg.emission.factor` (extins): câmpuri CBAM (`cbam_liable`, `cbam_category`, `cbam_cn_code_pattern`, `cbam_default_factor_t`) pentru factorii impliciți din Reg. delegat (UE) 2024/3212.
- `product.template` (extins): profilul produs CBAM — `cbam_liable`, categorie CN, factor de emisie/override, țară de origine, preț carbon plătit în origine și indicator de certificare.
- `account.move` (extins): capturarea automată a liniilor CBAM la postarea facturii de furnizor din afara UE și smart button spre liniile generate.
- `res.company` / `res.config.settings` (extinse): setările companiei CBAM (cod EORI, preț certificat implicit, jurnal și conturi pentru nota de certificate).

**Vizualizări**

- `views/l10n_ro_cbam_declaration_views.xml`, `views/l10n_ro_cbam_import_line_views.xml`: formularele și listele pentru declarații și liniile de import.
- `views/l10n_ro_cbam_certificate_price_views.xml`: nomenclatorul prețurilor de referință.
- `views/product_template_views.xml`: tab-ul CBAM pe fișa produsului.
- `views/esg_emission_factor_views.xml`: câmpurile CBAM pe nomenclatorul de factori de emisie ESG.
- `views/account_move_views.xml`: smart button-ul „linii CBAM" pe factură.
- `views/res_config_settings_views.xml`: secțiunea CBAM din setările de contabilitate.
- `views/l10n_ro_cbam_menus.xml`: meniurile ESG → CBAM (Declarații, Analiză, Factori emisie, Prețuri certificate).
- `data/cbam_emission_source_data.xml`, `data/cbam_emission_factor_data.xml`: sursa ESG dedicată și factorii de emisie impliciți.
- `report/cbam_declaration_report.xml`, `report/cbam_declaration_templates.xml`: raportul PDF „Situație CBAM".

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: pregătește datele inițiale CBAM la instalare (sursă ESG dedicată și factori de emisie impliciți).

#### 5. Conexiuni

- [l10n_ro_environmental_tax](../l10n_ro_environmental_tax/index.md): ambele module tratează obligații de mediu specifice pieței românești, deși nu au dependență directă de cod.
- [l10n_ro_excise](../l10n_ro_excise/index.md): modul conex de fiscalitate specială la import/producție, din aceeași familie de localizare română enterprise.
