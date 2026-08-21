# Romania - Accize (FR-42) (localizat la `l10n_ro_excise/index.md`)

- **Nume Tehnic:** `l10n_ro_excise`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_excise
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_excise`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru gestionarea accizelor conform Titlului VIII din Codul Fiscal RO, destinat antrepozitarilor autorizați și importatorilor de produse accizabile. Acoperă întreg ciclul: configurare categorii și rate, marcare produse, calcul automat din facturi, declarații D103/D120 și export XML pentru depunere la ANAF.

#### 2. Funcționalități Cheie

- Nomenclator complet de categorii accizabile: 16 categorii armonizate (alcool, bere, vinuri, tutun, combustibili, energie electrică — Anexele I și II CF) și 6 categorii nearmonizate H1–H6 (Legea 296/2023, art. 355¹–355⁶).
- Rate 2025 conform HG 2/2025, cu dată de intrare în vigoare și istoric.
- Marcare produse cu categorie de acciză direct din fișa produsului (fila „Accize RO").
- Declarație persistentă D103 (lunar, antrepozit fiscal) și D120 (anual, plătitori de accize), cu state machine draft → confirmed → exported.
- Calcul automat al liniilor din facturile de vânzare postate în perioadă — include stornări cu semn negativ.
- Export XML D103/D120 generat prin QWeb, gata de depunere (delegat modulelor ANAF dedicate, vezi mai jos).
- Evidență antrepozite fiscale cu cod ANAF, autorizație și stare (activ/suspendat/revocat).
- Evidență garanții financiare (bancară, depozit, asigurare) cu calcul sumă recomandată pe baza mediei declarațiilor anterioare.
- Wizard „Actualizare cote (HG)" pentru aplicarea modificărilor anuale de cote prin HG, cu mod manual sau indexare procentuală; declarațiile deja calculate păstrează cotele istorice.

#### 3. Dependențe

- `account`
- `product`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.excise.category`: nomenclatorul categoriilor accizabile (cod, anexă CF, rată, unitate de măsură, valabilitate).
- `l10n.ro.excise.declaration` / `l10n.ro.excise.declaration.line`: declarația persistentă D103/D120 pe perioadă, cu calcul automat din liniile de factură postate și dispatcher generic `export_to_xml()` care deleagă exportul efectiv modulelor ANAF (`_export_d103_xml` / `_export_d120_xml`).
- `l10n.ro.excise.warehouse`: antrepozitul fiscal (CF art. 369), cu cod ANAF, autorizație și categorii de produse autorizate.
- `l10n.ro.excise.guarantee`: garanția financiară (CF art. 348), cu calcul al sumei recomandate pe baza mediei declarațiilor D103 din ultimele N luni.
- `l10n.ro.excise.rate.update` / `l10n.ro.excise.rate.update.line` (wizard tranzitoriu): actualizarea anuală a cotelor prin HG, manual sau prin indexare procentuală.
- `product.template`: extins cu `l10n_ro_excise_category_id` (categoria de acciză a produsului).

**Vizualizări**

- `view_l10n_ro_excise_category_list` / `_form`: gestionarea nomenclatorului de categorii accizabile.
- `view_l10n_ro_excise_warehouse_list` / `_form`: gestionarea antrepozitelor fiscale.
- `view_l10n_ro_excise_guarantee_list` / `_form`: gestionarea garanțiilor financiare.
- `view_l10n_ro_excise_declaration_list` / `_form`: gestionarea declarațiilor D103/D120.
- `views/product_template_views.xml`: fila „Accize RO" pe fișa produsului, pentru marcarea categoriei de acciză.
- `wizard/l10n_ro_excise_rate_update_views.xml`: formularul wizard-ului de actualizare a cotelor.
- `data/excise_category_data.xml`: datele demo/inițiale ale nomenclatorului de categorii accizabile.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron` sau `base.automation`. Calculul declarațiilor (`action_compute`) și al garanțiilor (`action_compute_recommended`) se declanșează la cerere de utilizator, din formularul declarației, respectiv al garanției.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructură comună ANAF folosită ca dependență directă.
- [l10n_ro_environmental_tax](../l10n_ro_environmental_tax/index.md): modul înrudit de fiscalitate specifică RO (ecotaxă), din aceeași familie de declarații.
- [l10n_ro_cbam](../l10n_ro_cbam/index.md): modul înrudit de raportare fiscală/vamală RO.
