# Deductibilitate TVA România (localizat la `l10n_ro_vat_deductibility/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_deductibility`
- **Versiune:** `19.0.1.4.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_vat_deductibility
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_deductibility`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează explicit deductibilitatea TVA pentru România, acoperind toate cele trei regimuri prevăzute de Codul Fiscal: TVA deductibil integral, TVA deductibil parțial prin mecanismul pro-rata și TVA nedeductibil. Este destinat companiilor cu activități mixte (taxabile și scutite) sau celor care aplică procente fixe de nedeductibilitate pe anumite categorii de achiziții.

#### 2. Funcționalități Cheie

- Câmp `l10n_ro_deductibility_mode` pe taxa de TVA cu patru regimuri: `standard`, `integral`, `parțial / pro-rata`, `nedeductibil`.
- Gestiunea înregistrărilor pro-rata (model `l10n.ro.vat.prorata`): pro-rată provizorie la începutul anului și pro-rată definitivă la final, cu validare a suprapunerii intervalelor.
- Aplicare automată a procentului deductibil (`deductible_amount`) pe liniile de factură de furnizor înainte de postare, pe baza regimului taxei și a pro-ratei confirmate.
- Afectare directă la nivel de linie de factură (`l10n_ro_vat_deductibility_type`): activitate taxabilă (100%) sau scutită (0%), pentru achizițiile atribuibile direct, scoase din calculul pro-rata (Art. 300 Cod Fiscal).
- Grup de taxe preconfigurate **TVA 21% (50% Nedeductibil)** instalat automat (Taxa A 21% + Taxa B ajustare fixă 10,5 RON), utilizabil fără configurare suplimentară.
- Wizard de **regularizare anuală pro-rata** — compară pro-rata provizorie cu cea definitivă și generează nota contabilă de diferență (Dr 4426/Cr 635 sau invers).
- Wizard de **recalcul facturi ciornă** — reaplică pro-rata confirmată pe facturile de achiziție aflate în stare ciornă după modificarea procentului.
- Wizard de **pre-verificare D300/D394** — scanează facturile de achiziție postate din perioadă și semnalează liniile cu deductibilitate incoerentă față de regimul taxei sau pro-rata confirmată.
- Integrare nativă cu câmpul standard `deductible_amount` din Odoo, fără dependență de modulul OCA `l10n_ro_nondeductible_vat`.

#### 3. Dependențe

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md)

#### 4. Componente Cheie

**Modele**

- `account.tax` (extins): adaugă `l10n_ro_deductibility_mode` (regimul de deductibilitate al taxei) și `l10n_ro_default_deductible_percent` (procent fallback dacă nu există pro-rata confirmată).
- `account.move.line` (extins): adaugă `l10n_ro_vat_deductibility_type` pentru afectarea directă a liniei (pro-rata / activitate taxabilă 100% / activitate scutită 0%) și calculează automat `deductible_amount` înainte de postarea facturii.
- `account.move` (extins): orchestrează aplicarea deductibilității pe liniile facturii de furnizor la validare.
- `l10n.ro.vat.prorata`: gestionează înregistrările de pro-rata (provizorie/definitivă) pe intervale calendaristice, per companie, cu validare de suprapunere.

**Vizualizări**

- `views/account_tax_views.xml`: configurarea regimului de deductibilitate și a procentului fallback pe taxă.
- `views/account_move_views.xml`: coloana opțională „Afectare deductibilitate TVA" pe liniile facturii de achiziție.
- `views/l10n_ro_vat_prorata_views.xml`: formular și listă pentru gestionarea înregistrărilor pro-rata.
- `wizard/l10n_ro_vat_prorata_regularization_views.xml`: wizard de regularizare anuală pro-rata.
- `wizard/l10n_ro_vat_prorata_recompute_views.xml`: wizard de recalcul al facturilor ciornă.
- `wizard/l10n_ro_vat_deductibility_precheck_views.xml`: wizard de pre-verificare D300/D394.

**Acțiuni Automate / Acțiuni Server**

*Nu sunt definite `ir.cron` sau `base.automation`; toate operațiile (regularizare, recalcul, pre-verificare) se declanșează manual din wizard-urile dedicate (`action_compute`, `action_generate_entry`, `action_recompute`, `action_run`).*

#### 5. Conexiuni

- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md): regularizarea TVA la nivel general de decont, complementară regularizării pro-rata din acest modul.
- [l10n_ro_vat_group](../l10n_ro_vat_group/index.md): gestionarea grupurilor de TVA la nivel de companie.
- [l10n_ro_vat_refund](../l10n_ro_vat_refund/index.md): rambursarea TVA, poate interacționa cu sumele nedeductibile calculate aici.
