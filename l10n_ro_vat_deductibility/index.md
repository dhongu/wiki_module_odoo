# Romania - Deductibilitatea TVA (localizat la `l10n_ro_vat_deductibility/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_deductibility`
- **Versiune:** `20.0.1.5.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_vat_deductibility
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_vat_deductibility`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează explicit deductibilitatea TVA pentru România, acoperind toate cele trei regimuri prevăzute de Codul Fiscal: TVA deductibil integral, TVA deductibil parțial prin mecanismul pro-rata și TVA nedeductibil. Este destinat companiilor cu activități mixte (taxabile și scutite) sau celor care aplică procente fixe de nedeductibilitate pe anumite categorii de achiziții.

#### 2. Funcționalități Cheie

- Câmp `l10n_ro_deductibility_mode` pe taxa de TVA (Contabilitate → Configurare → Contabilitate → Taxe, fila Opțiuni Avansate) cu patru regimuri: `Standard` (comportament Odoo neschimbat), `TVA deductibil integral` (100%), `TVA deductibil parțial / pro-rata` și `TVA nedeductibil` (0%). Pentru regimul pro-rata, fără pro-rata confirmată se folosește procentul implicit de pe taxă.
- Gestiunea înregistrărilor pro-rata (model `l10n.ro.vat.prorata`, meniul Contabilitate → Configurare → Configurare TVA deductibil → TVA pro-rata): pro-rată provizorie în cursul anului și definitivă la final, cu validare a suprapunerii intervalelor; doar pro-ratele confirmate se aplică pe facturi.
- Aplicare automată a procentului deductibil (`deductible_percentage`, fracție 0–1 în Odoo 20) pe liniile facturii de furnizor la salvare și la postare, pe baza regimului taxei și a pro-ratei confirmate.
- Afectare directă la nivel de linie de factură (`l10n_ro_vat_deductibility_type`): pro-rata (implicit), activitate taxabilă (100%) sau activitate scutită (0%), pentru achizițiile atribuibile direct, scoase din calculul pro-rata (Art. 300 Cod Fiscal).
- TVA-ul nededus prin pro-rata se postează pe contul „Cont acțiuni private" setat pe jurnalul de achiziții (de regulă 6351); în cazurile de afectare directă 0% sau TVA nedeductibil, TVA-ul intră în costul liniei.
- Grup de taxe preconfigurate **TVA 21% (50% Nedeductibil)** instalat automat, utilizabil fără configurare suplimentară (ghid pentru deductibilitatea de 50%, art. 298).
- Wizard de **regularizare anuală pro-rata** — compară pro-rata provizorie cu cea definitivă și generează nota contabilă de diferență (Dr 4426/Cr 635 sau invers).
- Wizard de **recalcul facturi ciornă** — reaplică pro-rata confirmată pe facturile de achiziție aflate în ciornă după modificarea procentului; liniile cu afectare directă sunt excluse.
- Wizard de **pre-verificare D300/D394** — scanează facturile de achiziție postate din perioadă și semnalează liniile cu deductibilitate incoerentă față de regimul taxei sau pro-rata confirmată.
- Integrare nativă cu câmpul standard `deductible_percentage` din Odoo 20, fără dependență de modulul OCA `l10n_ro_nondeductible_vat`.
- Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md)
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md)

#### 4. Componente Cheie

**Modele**

- `account.tax` (extins): adaugă `l10n_ro_deductibility_mode` (regimul de deductibilitate al taxei) și `l10n_ro_default_deductible_percent` (procent fallback dacă nu există pro-rata confirmată).
- `account.move.line` (extins): adaugă `l10n_ro_vat_deductibility_type` pentru afectarea directă a liniei și calculează `deductible_percentage` înainte de postare; suprascrie constrângerea nucleului `_constrains_deductible_percentage` pentru liniile românești.
- `account.move` (extins): orchestrează aplicarea deductibilității pe liniile facturii de furnizor la validare.
- `l10n.ro.vat.prorata`: înregistrările de pro-rata (provizorie/definitivă) pe intervale calendaristice, per companie, cu validare de suprapunere.
- Handler de raport de taxe (`tax_report_handler.py`): adaptează raportul de taxe la TVA-ul parțial deductibil.

**Vizualizări**

- `views/account_tax_views.xml`: regimul de deductibilitate și procentul fallback pe taxă.
- `views/account_move_views.xml`: coloana opțională „Afectare deductibilitate TVA" pe liniile facturii de achiziție.
- `views/l10n_ro_vat_prorata_views.xml`: formular și listă pentru pro-rata.
- `wizard/l10n_ro_vat_prorata_regularization_views.xml`: wizard de regularizare anuală pro-rata.
- `wizard/l10n_ro_vat_prorata_recompute_views.xml`: wizard de recalcul al facturilor ciornă.
- `wizard/l10n_ro_vat_deductibility_precheck_views.xml`: wizard de pre-verificare D300/D394.

**Acțiuni Automate / Acțiuni Server**

*Nu sunt definite `ir.cron` sau `base.automation`; toate operațiile (regularizare, recalcul, pre-verificare) se declanșează manual din wizard-urile dedicate.*

#### 5. Conexiuni

- [l10n_ro_vat_regularization](../l10n_ro_vat_regularization/index.md): regularizarea TVA la nivel general de decont, complementară regularizării pro-rata din acest modul.
- [l10n_ro_vat_group](../l10n_ro_vat_group/index.md): grupul fiscal TVA consolidat, cu tranzacții intra-grup excluse din decont.
- [l10n_ro_vat_refund](../l10n_ro_vat_refund/index.md): rambursarea TVA, poate interacționa cu sumele nedeductibile calculate aici.
