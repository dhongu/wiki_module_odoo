# Romania - Accize (FR-42) (localizat la `l10n_ro_excise_duty/index.md`)

- **Nume Tehnic:** `l10n_ro_excise_duty`
- **Nume anterior:** `l10n_ro_excise` (redenumit pe 23.09.2026: numele vechi e ocupat pe Odoo Apps de alt furnizor)
- **Versiune:** `19.0.1.5.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_excise_duty
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_excise_duty`
- **Ultima Ingestie:** `2026-11-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru gestionarea accizelor conform Titlului VIII din Codul Fiscal RO, destinat antrepozitarilor autorizați și importatorilor de produse accizabile. Acoperă întreg ciclul: configurare categorii și rate, marcare produse, calcul automat din facturi, declarații D103/D120 și export XML pentru depunere la ANAF.

#### 2. Funcționalități Cheie

- Nomenclator complet de categorii accizabile (*Contabilitate → Raportare → Accize → Categorii produse accizabile*): 16 categorii armonizate (alcool, bere, vinuri, tutun, combustibili, energie electrică — Anexele I și II CF) și 6 categorii nearmonizate H1–H6 (Legea 296/2023, art. 355¹–355⁶), preîncărcate la instalare.
- Rate 2025 conform HG 2/2025, cu istoric: nivelurile datate se rețin în `l10n.ro.excise.rate`, iar pentru o dată anterioară primului nivel se ia cel mai vechi nivel.
- Marcare produse cu categorie de acciză direct din fișa produsului (fila „Accize (RO)"); produsele fără categorie nu intră în calcul.
- Declarație persistentă D103 (lunar, antrepozit fiscal) și D120 (anual, plătitori de accize), cu state machine draft → confirmed → exported; la D120 nu apare câmpul antrepozit.
- Calcul automat al liniilor din facturile de vânzare postate în perioadă (perioada se alege după data facturii) — include stornări cu semn negativ; se iau doar categoriile autorizate ale antrepozitului ales, iar fără nicio linie de acciză declarația nu se confirmă.
- Cota aplicată e cea în vigoare la data ieșirii din antrepozit (livrarea din stoc, art. 339–340 CF); fără livrare se folosește data facturii, iar linia e marcată. O declarație recalculată după o schimbare de cotă păstrează cota corectă a perioadei. Limită cunoscută: la livrări parțiale în luni diferite, linia ia data ultimei livrări.
- Conversia cantității liniei în unitatea cotei (litri în hl, kg în tone, bucăți în 1000 buc) când conversia e pur dimensională; alcoolul etilic, berea, țigaretele și liniile cu unitate neconvertibilă sunt marcate „necesită date suplimentare": nu intră în total, declarația rămâne în ciornă și nu se poate exporta.
- Modulul calculează declarațiile, dar nu postează note contabile (acciza datorată și plata ei se înregistrează separat); la datele sursă modificate se folosește „Resetează la ciornă" și se recalculează.
- Export XML D103/D120 (`D103_<CUI>_<AnLună>.xml`), delegat modulelor ANAF dedicate (`l10n_ro_anaf_d103`, `l10n_ro_anaf_d120`); după export liniile devin needitabile.
- Evidență antrepozite fiscale cu cod ANAF (unic per companie), autorizație și stare (activ/suspendat/revocat); antrepozitul nu poate fi activat fără data autorizației.
- Evidență garanții financiare (bancară, depozit numerar, asigurare), cu butoane **Activează** / **Marchează expirată**; suma recomandată se calculează din acciza anului calendaristic anterior, pe antrepozit, cu 6% implicit (Norme HG 1/2016), fără aplicarea pragurilor minime și maxime.
- Wizard „Actualizare cote (HG)" pentru aplicarea modificărilor anuale: cote manuale sau indexare procentuală, cu dată de intrare în vigoare; adaugă un nivel nou de cotă, iar declarațiile deja calculate păstrează cotele istorice.
- Izolare pe companie: modelele au reguli de înregistrare globale, utilizatorul vede doar înregistrările companiilor la care are acces.

Fluxul detaliat pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `product`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.excise.category`: nomenclatorul categoriilor accizabile (cod, anexă CF, unitate de măsură a cotei, valabilitate).
- `l10n.ro.excise.rate`: istoricul nivelurilor datate de cotă ale unei categorii.
- `l10n.ro.excise.declaration` / `l10n.ro.excise.declaration.line`: declarația persistentă D103/D120 pe perioadă, cu calcul automat din liniile de factură postate și dispatcher generic `export_to_xml()` care deleagă exportul efectiv modulelor ANAF (`_export_d103_xml` / `_export_d120_xml`).
- `l10n.ro.excise.warehouse`: antrepozitul fiscal (CF art. 369), cu cod ANAF, autorizație și categorii de produse autorizate.
- `l10n.ro.excise.guarantee`: garanția financiară (CF art. 348), cu calculul sumei recomandate din acciza anului anterior.
- `l10n.ro.excise.rate.update` / `l10n.ro.excise.rate.update.line` (wizard tranzitoriu): actualizarea anuală a cotelor prin HG, manual sau prin indexare procentuală.
- `product.template`: extins cu `l10n_ro_excise_category_id` (categoria de acciză a produsului).

**Vizualizări**

- `view_l10n_ro_excise_category_list` / `_form`: gestionarea nomenclatorului de categorii accizabile.
- `view_l10n_ro_excise_warehouse_list` / `_form`: gestionarea antrepozitelor fiscale.
- `view_l10n_ro_excise_guarantee_list` / `_form`: gestionarea garanțiilor financiare.
- `view_l10n_ro_excise_declaration_list` / `_form`: gestionarea declarațiilor D103/D120.
- `views/product_template_views.xml`: fila „Accize (RO)" pe fișa produsului, pentru marcarea categoriei de acciză.
- `wizard/l10n_ro_excise_rate_update_views.xml`: formularul wizard-ului de actualizare a cotelor.
- `data/excise_category_data.xml`: datele inițiale ale nomenclatorului de categorii accizabile.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron` sau `base.automation`. Calculul declarațiilor (`action_compute`) și al garanțiilor (`action_compute_recommended`) se declanșează la cerere de utilizator, din formularul declarației, respectiv al garanției.

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructură comună ANAF folosită ca dependență directă.
- [l10n_ro_anaf_d103](../l10n_ro_anaf_d103/index.md): generează fișierul XML al declarației D103 la exportul din declarația de accize.
- [l10n_ro_anaf_d120](../l10n_ro_anaf_d120/index.md): generează fișierul XML al declarației D120 (decont anual accize).
- [l10n_ro_environmental_tax](../l10n_ro_environmental_tax/index.md): modul înrudit de fiscalitate specifică RO (ecotaxă), din aceeași familie de declarații.
- [l10n_ro_cbam](../l10n_ro_cbam/index.md): modul înrudit de raportare fiscală/vamală RO.
