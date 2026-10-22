# Romania - Account VAT Change - Obsolete (localizat la `l10n_ro_vat_change/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_change`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/l10n_ro_vat_change
- **Cale Locală:** `odoo-addons/terrabit/l10n_ro_vat_change`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul a fost creat pentru trecerea României la noile cote de TVA (21% și 11%) începând cu 01.08.2025: adaugă taxele noi, maparea lor pe pozițiile fiscale și actualizează automat taxele implicite ale firmelor și ale produselor. **Pe 19.0 modulul este retras** (`installable: False`): nucleul Odoo 19 (`l10n_ro`) conține deja cotele de 21%/11% și maparea corectă în declarația D300, iar modulul nu mai funcționează pe 19.0. Nu trebuie instalat în implementările pe 19.0; pe bazele existente se dezinstalează, nu se repară.

#### 2. Funcționalități Cheie

- **Stare pe 19.0: retras.** Odoo 19 a eliminat modelul intermediar `account.fiscal.position.tax` (`tax_src_id`/`tax_dest_id`) pe care se baza maparea taxelor; încărcarea șabloanelor eșua cu `KeyError: 'tax_src_id'` și bloca orice instalare/actualizare de modul sau de limbă.
- **Rânduri proprii în raportul de TVA (D300)** pentru 21%/11% (66/67 livrări, 68_1/69_1 achiziții, plus 124/125 și 274/275), divergente de cele din nucleu (rd09/rd10/rd24/rd25); exportul D300 mapează în grila R doar rândurile din nucleu, deci sumele de pe rândurile 66–69 nu ajungeau în declarație.
- **Taxe noi la 21%/11%** (inclusiv variantele „inclus în preț" și cele cu TVA nedeductibil 50%), grupuri de taxe și poziție fiscală de tranziție („VAT Percent Change"), încărcate din șabloane CSV pentru șablonul de plan contabil `ro`.
- **Actualizare automată (cron zilnic, de la 01.08.2025):** înlocuiește cotele 5/9/19 cu 11/21 pe produse (taxe de vânzare și de achiziție, în loturi de 1000), setează taxele implicite ale firmelor RO la 21% (bunuri și servicii).
- **Migrarea bazelor existente:** dezinstalarea singură nu ajunge; trebuie aduse liniile de repartizare ale taxelor pe etichetele șablonului `l10n_ro` din nucleu, dezinstalat modulul, rescrise grilele pe înregistrările postate de la 01.08.2025 (cu `account_update_tax_tags`) și arhivată poziția fiscală de tranziție. Etichetele rămase fără rând de raport nu se șterg.
- Taxele `tvac_11_inc`, `tvac_11_s_inc`, `tvac_21_inc`, `tvac_21_s_inc`, `tva_ic_ned_11_50`, `tva_ic_ned_21_50` rămân în baza de date după dezinstalare (xml_id aparține modulului `account`) și funcționează în continuare.

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): adaugă taxele, grupurile de taxe și pozițiile fiscale din CSV pentru șablonul `ro` și mapările de taxe pe pozițiile fiscale (nefuncțional pe 19.0).
- `res.company` (extins): metoda `_l10n_ro_update_default_taxes` — actualizează taxele implicite ale firmelor și taxele produselor.

**Vizualizări**

- Modulul nu definește vizualizări; doar `data/account_tax_report_data.xml` (rânduri/expresii de raport TVA).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_ro_vat_change` („Romania VAT Change"): rulează zilnic (prima rulare 2025-08-01) `_l10n_ro_update_default_taxes()`; se redeclanșează singur dacă mai sunt produse de procesat.

#### 5. Conexiuni

- `l10n_ro_reports_d300` (Enterprise) și `l10n_ro_anaf_d300`: exportul D300 mapează doar rândurile din nucleu, nu și cele adăugate de acest modul.
- `account_update_tax_tags`: folosit la migrarea grilelor pe înregistrările deja postate.
