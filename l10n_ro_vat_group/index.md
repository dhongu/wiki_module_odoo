# Romania - Grup fiscal TVA consolidat (localizat la `l10n_ro_vat_group/index.md`)

- **Nume Tehnic:** `l10n_ro_vat_group`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_vat_group
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_vat_group
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează grupurile fiscale TVA conform art. 269² Cod Fiscal și OPANAF 2731/2016. Permite definirea unui grup de companii cu relații de control ca un singur subiect fiscal TVA, cu CUI unic, marcarea automată a tranzacțiilor intra-grup, excluse din baza TVA, și generarea unui raport TVA consolidat per companie membră, pentru D300-ul unic depus de membrul raportor.

#### 2. Funcționalități Cheie

- **Grup fiscal TVA** (**Contabilitate → Configurare → Contabilitate → Grupuri Fiscale TVA**, vizibil pentru rolul Contabilitate / Administrator): denumire, CUI de grup (`RO_GRP_XXXXXX`), data înregistrării la ANAF, membrul raportor și companiile membre; stările `În constituire → Activ → Dizolvat`.
- **Activare cu validări:** cel puțin 2 companii membre, membru raportor inclus între membri și CUI de grup completat; la activare câmpul „Grup fiscal TVA" se setează pe toate companiile membre.
- **Marcare automată intra-grup:** la postarea unei facturi către o companie membră (partenerul asociat exact companiei), factura primește bifa „Tranzacție intra-grup TVA" și un banner de avertizare; bifa rămâne editabilă manual, inclusiv după postare.
- **Marcare retroactivă:** butonul „Marchează retroactiv intra-grup" marchează facturile postate dintre membri care nu erau încă marcate; se rulează la activarea inițială și după adăugarea unui membru.
- **Raport TVA consolidat** (wizard, pe o perioadă): per companie membră TVA colectată (4427), TVA deductibilă (4426), intra-grup colectat și deductibil, TVA net, plus total consolidat fără intra-grup; toate companiile trebuie să lucreze în RON.
- **Blocare perioadă sincronizată:** după validarea D300 consolidat, „Blochează perioada" setează data de blocare fiscală pe toate companiile membre (necesită drept de administrator).
- **Buton smart „Intra-grup":** lista facturilor marcate intra-grup, pentru audit și corecții.
- **Membru nou sau dizolvare:** pentru un membru nou se resetează grupul la ciornă, se adaugă compania și se reactivează; la dizolvare facturile ulterioare nu mai sunt marcate, iar raportul consolidat nu mai este disponibil.
- **Ce nu include:** generarea XML-ului D300 consolidat cu CUI de grup (necesită extensia `l10n_ro_anaf_d300`) și formularul 045 de constituire a grupului, planificat pentru o versiune ulterioară.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.vat.group`: grupul fiscal TVA, cu companii membre, membru raportor, CUI unic, stări și acțiunile de activare, dizolvare, resetare, marcare retroactivă (are chatter).
- `l10n.ro.vat.group.report.wizard` / `l10n.ro.vat.group.report.line` (wizard): raportul TVA consolidat și blocarea perioadei pe toate companiile.
- `account.move` (extins): marcajul „Tranzacție intra-grup TVA".
- `res.company` (extins): referința către grupul fiscal TVA.

**Vizualizări**

- `view_l10n_ro_vat_group_form` / `view_l10n_ro_vat_group_list`: fișa și lista grupurilor fiscale (meniu `menu_l10n_ro_vat_group`).
- `view_move_form_l10n_ro_vat_group`: bifa și bannerul intra-grup pe factură.
- `view_l10n_ro_vat_group_report_wizard_form`: wizardul raportului consolidat.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește cron-uri sau acțiuni server; marcarea intra-grup se aplică la postarea facturilor.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): extensia necesară pentru generarea XML-ului D300 consolidat cu CUI de grup.
