# Romania - Subvenții și Fonduri Nerambursabile (FR-38) (localizat la `l10n_ro_grants/index.md`)

- **Nume Tehnic:** `l10n_ro_grants`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_grants
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_grants`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

MVP pentru FR-38 — Subvenții și Fonduri Nerambursabile conform OMFP 1802/2014 și IAS 20. Modulul gestionează contractele de finanțare nerambursabilă cu state machine, bugetul pe categorii de cheltuieli eligibile, tranșele de plată cu generare automată de note contabile (475/131/132) și recunoașterea veniturilor (manuală sau prin cron lunar liniar), precum și calculul cheltuielilor eligibile per categorie din înregistrările contabile cu distribuție analitică pe proiect. Acoperă surse precum PNRR, Fonduri Structurale UE, programe naționale și ajutoare de minimis.

#### 2. Funcționalități Cheie

- **Contract de finanțare nerambursabilă** cu state machine (draft → contractat → activ → finalizat).
- **Buget pe categorii de cheltuieli eligibile** cu urmărire realizat vs. aprobat și alertă la procentul configurat din buget consumat.
- **Tranșe de plată primite** cu generare automată notă `Dr 5121 = Cr 475/131/132`.
- **Recunoaștere venituri** (`Dr 475/131 = Cr 7584/7411`) — manuală sau prin cron lunar liniar.
- **Calcul cheltuieli eligibile** per categorie din AML-uri cu distribuție analitică pe proiect.
- **Cron lunar opțional** pentru recunoașterea liniară a subvențiilor pentru active (inactiv implicit).
- **Cereri de rambursare (claim)** generate pe perioadă, cu linii agregate per categorie bugetară care separă eligibilul net de sumele excluse (conturi neeligibile precum 4426 TVA recuperabil și furnizori afiliați/părți legate), calculul sumei solicitate (`eligibil net × procent nerambursabil`) și fluxul propriu de stare (ciornă → depusă → aprobată → rambursată/respinsă).
- **Rapoarte PDF/Excel** ale cererii de rambursare, pentru dosarul depus la finanțator.

#### 3. Dependențe

- `account`
- `analytic`
- `mail`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.grant`: contractul de finanțare nerambursabilă, cu state machine, conturile contabile, bugetul pe categorii și excluderile din baza eligibilă (conturi neeligibile, furnizori afiliați).
- `l10n.ro.grant.budget.line`: linia de buget pe categorie de cheltuieli eligibile (buget aprobat, conturi eligibile, realizat, prag de alertă).
- `l10n.ro.grant.tranche`: tranșa de plată primită de la finanțator, cu contabilizare automată (`Dr 5121 = Cr 475/131/132`).
- `l10n.ro.grant.recognition`: recunoașterea venitului din subvenție (`Dr 475/131 = Cr 7584/7411`), manuală sau generată de cronul lunar.
- `l10n.ro.grant.claim` (moștenește și `l10n_ro_anaf.report.handler.mixin`): cererea de rambursare depusă periodic la finanțator, cu perioada acoperită, generarea liniilor din AML-uri, totalurile eligibil/exclus/brut, suma solicitată și export PDF/Excel.
- `l10n.ro.grant.claim.line`: linia cererii de rambursare, agregată per categorie bugetară (eligibil net, exclus, cheltuit brut).

**Vizualizări**

- `l10n_ro_grant_views.xml`: formularul și lista contractului de finanțare, cu tab-urile Buget pe categorii, Tranșe primite, Recunoașteri venituri și Excluderi din baza eligibilă.
- `l10n_ro_grant_claim_views.xml`: formularul și lista cererilor de rambursare, cu liniile per categorie și butoanele de generare/depunere.

**Rapoarte**

- `report_actions.xml` / `report_grant_claim.xml`: raportul PDF al cererii de rambursare (situația eligibilității pentru dosarul depus la finanțator); export Excel disponibil din model (`xlsxwriter`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron.xml`: cron lunar **Recunoaștere lunară subvenții active (475→7584)**, inactiv implicit — calculează și contabilizează automat suma liniară pentru granturile de tip `475` aflate în starea „În derulare".

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): mixin de raportare (`l10n_ro_anaf.report.handler.mixin`) folosit de cererea de rambursare.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): schema notelor contabile pentru tranșe și recunoașterea veniturilor.
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): corelarea recunoașterii subvenției pentru active cu amortizarea activului finanțat.
