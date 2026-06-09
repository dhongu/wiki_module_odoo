# Romania - ANAF D120 Declaration (localizat la `l10n_ro_anaf_d120/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d120`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d120
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d120`
- **Ultima Ingestie:** 2026-06-09

#### 1. Sumar

Modulul adaugă exportul în format XML ANAF al **Decontului privind accizele (D120)**, peste declarația de accize gestionată de modulul `l10n_ro_excise`. D120 este decontul depus de importatorii și operatorii de produse accizabile (alcool, bere, produse energetice, tutun etc.), reglementat de Codul Fiscal Titlul VIII. Modulul nu adaugă un ecran nou: pe o declarație de accize de tip D120, butonul „Export XML" generează fișierul în formatul ANAF D120 (namespace `mfp:anaf:dgti:d120:declaratie:v5`), validat față de schema XSD oficială, în locul template-ului D103. Astfel, responsabilul fiscal obține fișierul de depunere fără operare manuală.

#### 2. Funcționalități Cheie

- **Export XML D120:** generarea decontului de accize în formatul ANAF (`D120_<CUI>_<AAAALL>.xml`), pe baza liniilor declarației de accize.
- **Mapare automată pe rândurile D120:** fiecare categorie de acciză (bere, vin, alcool etilic, țigarete, motorină, GPL, gaz natural, energie electrică, plus categoriile nearmonizate din Legea 296/2023) este pusă pe rândul corespunzător din formular (R0, R3, R9, R20 etc.).
- **Calcul totaluri:** subtotaluri și totaluri (accize armonizate, nearmonizate, total general) calculate automat din liniile declarației.
- **Validare XSD:** XML-ul este validat față de schema oficială ANAF v5 (`d120_13052025.xsd`) înainte de livrare; datele de identificare ale companiei (CUI, CAEN, adresă) sunt verificate la export.

#### 3. Dependențe

- [l10n_ro_excise](../l10n_ro_excise/index.md)
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.excise.declaration`: model extins (inherit) din `l10n_ro_excise`, combinat cu mixinul `l10n_ro_anaf.report.handler.mixin`. Suprascrie metoda `export_to_xml()` pentru a genera XML-ul D120 atunci când tipul declarației este `d120` (altfel deleagă la comportamentul de bază — ex. D103).

**Acțiuni Automate / Acțiuni Server**

- La încărcarea modulului se înregistrează profilul de declarație ANAF D120 (`register_anaf_profile`, versiune `v5-20250513`, XSD `d120_13052025.xsd`), folosit la export pentru rezolvarea schemei de validare.

#### 5. Conexiuni

- [l10n_ro_excise](../l10n_ro_excise/index.md): furnizează declarația de accize, categoriile și cotele (modelul de bază extins de acest modul).
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF (validare date companie, profil de declarație, validare XSD).
- D103 (`cod`): decontul lunar al antrepozitului fiscal, construit pe **același model** de declarație de accize, dar cu alt tip și alt template XML.
