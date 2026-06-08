# Romania - Repartizare costuri indirecte pe centre de cost (localizat la `l10n_ro_cost_centers/index.md`)

- **Nume Tehnic:** `l10n_ro_cost_centers`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_cost_centers
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_cost_centers`
- **Ultima Ingestie:** `2026-06-08`

#### 1. Sumar

Modulul automatizează repartizarea cheltuielilor indirecte pe centre de cost (conturi analitice), conform contabilității de gestiune din România (OMFP 1802/2014). Costurile colectate pe un centru comun/indirect se redistribuie pe centrele productive printr-o notă contabilă care păstrează un impact financiar zero pe contul de cheltuială (creditul 6xx de pe centrul comun este egal cu debitele 6xx de pe centrele țintă), mutând costul doar pe dimensiunea analitică — fără a folosi obligatoriu conturile din clasa 9. Este un instrument de control de gestiune, neutru financiar, care nu modifică balanța contabilă.

#### 2. Funcționalități Cheie

- Repartizarea automată a cheltuielilor indirecte de pe un centru de cost sursă (comun/indirect) pe mai multe centre țintă (productive).
- Cheie de repartizare configurabilă: **manual** (procente fixe), **suprafață** (m²), **nr. angajați** sau **cifră de afaceri** (venituri 7xx pe centru).
- Câmpuri proprii pe centrul de cost (cont analitic): **Suprafață (m²)** și **Nr. angajați**, folosite ca baze de repartizare.
- Colectarea costului de pe centrul sursă pe o perioadă aleasă și calculul automat al procentelor și sumelor per centru țintă.
- Generarea unei note contabile de redistribuire analitică echilibrată, cu impact financiar zero pe contul de cheltuială (costul migrează doar pe dimensiunea analitică).
- Anularea repartizării readuce nota în ciornă și anulează nota contabilă generată.
- Bazat pe contabilitatea analitică nativă Odoo; planurile analitice ierarhice, distribuția analitică obligatorie la postare, bugetele pe centre și rapoartele P&L pe dimensiuni rămân acoperite de baza nativă (analytic + Enterprise account_budget / account_reports).

#### 3. Dependențe

- `account`
- `analytic`
- `l10n_ro`

#### 4. Componente Cheie

Fișierul `readme/DESCRIPTION.md` acoperă Sumarul și Funcționalitățile Cheie și nu solicită explicit analiza componentelor tehnice. Conform fluxului de ingestie din `schema.md`, analiza codului pentru această secțiune este **omisă**.

#### 5. Conexiuni

- `account_budget` (Enterprise): bugete pe centre de cost — nativ, opțional, necuplat de modul.
- `account_reports` (Enterprise): rapoarte P&L pe dimensiuni analitice — nativ, opțional.
