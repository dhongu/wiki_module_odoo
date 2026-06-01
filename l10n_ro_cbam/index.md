# Romania - CBAM (FR-56) (localizat la `l10n_ro_cbam/index.md`)

- **Nume Tehnic:** `l10n_ro_cbam`
- **Versiune:** `19.0.1.6.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_cbam
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cbam`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

Modul pentru Carbon Border Adjustment Mechanism (CBAM) conform Regulamentului (UE) 2023/956. Sprijină importatorii români care introduc pe piața UE produse din categoriile vizate (oțel și fier, aluminiu, ciment, îngrășăminte, electricitate, hidrogen) să declare emisiile de CO₂ incorporate și, din regimul definitiv (1 ianuarie 2026), să determine certificatele CBAM necesare. Este construit peste modulul `esg` (Enterprise), reutilizând `esg.emission.factor` și `esg.emission.source`, și peste `account_intrastat` pentru codul CN.

## 2. Funcționalități Cheie

- **Profil produs CBAM:** marcaj `cbam_liable`, categorie derivată automat din codul CN (Intrastat), factor de emisie din nomenclator sau override verificat per instalație, țară de origine și preț carbon plătit în origine.
- **Nomenclator factori de emisie:** extindere `esg.emission.factor` cu factori impliciți conform Reg. delegat (UE) 2024/3212; sursă ESG dedicată „Importuri CBAM" în Scope 3.
- **Captură la import:** la postarea facturii de la furnizor din afara UE, generează linii CBAM (`l10n.ro.cbam.import.line`) cu cantitatea în tone și emisiile incorporate; smart button pe factură; retururile compensează cu semn negativ.
- **Declarație CBAM:** trimestrială (tranziție) sau anuală (definitivă); agregă liniile din perioadă, calculează totalurile de emisii și deducerea prețului carbonului din origine, iar pentru declarația definitivă determină certificatele necesare.
- **Export XML** pentru Registrul CBAM și **raport PDF** „Situație CBAM".

## 3. Dependențe

- `esg`
- `account`
- `account_intrastat`

## 4. Componente Cheie

### Modele

- `l10n.ro.cbam.import.line`: liniile CBAM generate la import, cu cantitate în tone și emisii incorporate.
- `l10n.ro.cbam.declaration`: declarația CBAM trimestrială/anuală cu agregarea liniilor și calculul certificatelor.
- `esg.emission.factor`: extins cu factorii de emisie CBAM impliciți.
- `product.template`: extins cu profilul produs CBAM (`cbam_liable`, categorie CN, factor de emisie, țară de origine).
- `account.move`: extins cu smart button și captura liniilor CBAM la postare.

### Vizualizări / Date

- `views/l10n_ro_cbam_declaration_views.xml`, `views/l10n_ro_cbam_import_line_views.xml`: interfețele pentru declarații și linii de import.
- `views/product_template_views.xml`: profilul CBAM pe produs.
- `data/cbam_emission_source_data.xml`, `data/cbam_emission_factor_data.xml`: nomenclatoarele de surse și factori de emisie.
- `report/cbam_declaration_report.xml`, `report/cbam_declaration_templates.xml`: raportul PDF „Situație CBAM".

### Acțiuni Automate / Acțiuni Server

- `post_init_hook`: pregătește datele inițiale CBAM (sursă ESG și factori de emisie).

## 5. Conexiuni

- `[[l10n_ro_environmental_tax]]`
- `[[l10n_ro_excise]]`
