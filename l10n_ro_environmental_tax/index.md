# Romania - Taxe de Mediu / AFM (FR-48) (localizat la `l10n_ro_environmental_tax/index.md`)

- **Nume Tehnic:** `l10n_ro_environmental_tax`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_environmental_tax
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_environmental_tax`
- **Ultima Ingestie:** 2026-06-01

## 1. Sumar

MVP pentru FR-48 — Taxe de mediu / AFM, cu focus inițial pe ambalaje. Modulul permite definirea profilurilor AFM pe produse, a liniilor de ambalaj cu material și greutate, a cotelor AFM pe material și generarea declarației AFM persistente per perioadă, calculată automat din facturile de vânzare postate, cu trasabilitate până la documentul sursă.

## 2. Funcționalități Cheie

- **Profil AFM pe produs** cu marcarea bunurilor supuse taxelor de mediu.
- **Linii de ambalaj** cu material, tip și greutate per unitate.
- **Cote AFM pe material** configurabile.
- **Declarație AFM persistentă** pe perioadă.
- **Calcul automat din facturile de vânzare postate** pentru cantitățile introduse pe piață și cantitățile scutite/exportate, cu trasabilitate până la documentul sursă.
- Pregătit pentru extindere spre baterii, DEEE și alte categorii AFM.

## 3. Dependențe

- `account`
- `product`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- Model material AFM: nomenclatorul materialelor de ambalaj.
- Model cotă AFM: cotele per material.
- Model linie de ambalaj pe produs: material, tip și greutate per unitate.
- Model declarație AFM: declarația persistentă pe perioadă, cu calcul din facturi.

### Vizualizări / Date

- `views/l10n_ro_environmental_tax_views.xml`: vizualizările declarației AFM.
- `views/product_template_views.xml`: profilul AFM și liniile de ambalaj pe produs.
- `data/afm_material_data.xml`, `data/afm_rate_data.xml`: nomenclatoarele de materiale și cote.

### Acțiuni Automate / Acțiuni Server

*Calculul declarației se realizează la cerere din facturile de vânzare postate în perioadă.*

## 5. Conexiuni

- `[[l10n_ro_cbam]]`
- `[[l10n_ro_excise]]`
