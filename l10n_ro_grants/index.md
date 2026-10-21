# Romania - Subvenții și fonduri nerambursabile (FR-38) (localizat la `l10n_ro_grants/index.md`)

- **Nume Tehnic:** `l10n_ro_grants`
- **Versiune:** `19.0.1.6.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_grants
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_grants`
- **Ultima Ingestie:** 2026-10-21
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Subvenții și fonduri nerambursabile conform OMFP 1802/2014 și IAS 20. Modulul urmărește un contract de finanțare de la semnare până la cererea de rambursare: tranșele de finanțare cu nota contabilă `Dr 4451 = Cr 475x/472` (finanțatorul ca partener, încasarea venind din extrasul bancar), recunoașterea veniturilor din subvenție (manuală sau prin cron lunar liniar), bugetul pe categorii de cheltuieli eligibile și cererile de rambursare pentru finanțator. Conturile 131/132 din planul vechi nu mai sunt folosite. Acoperă surse precum PNRR, Fonduri Structurale UE (FEDR/FSE/FEADR), programe naționale (Start-Up Nation, IMM Invest) și ajutoare de minimis.

#### 2. Funcționalități Cheie

- **Contract de finanțare nerambursabilă** cu state machine (draft → contractat → în derulare → finalizat; anulare/resetare), cu tipuri de subvenție: active, exploatare, dobânzi, mixtă.
- **Conturi completate automat după tipul subvenției** (active: 47512 / 7584; exploatare: 4721 / 741x ales după natura cheltuielii; dobânzi: 4721 / 7418; 4451 pentru subvenții de primit, cu „Permite reconcilierea” bifat). Pentru tipul mixtă conturile se completează manual, de preferat prin contracte distincte.
- **Tranșe de finanțare** cu notă automată `Dr 4451 = Cr 475x/472`; încasarea (`Dr 5121 = Cr 4451`) se face o singură dată, din extrasul bancar reconciliat cu tranșa. Starea încasării (neîncasată / parțial / încasată) și restul de încasat sunt vizibile pe tranșă; totalurile pe contract numără doar sumele încasate.
- **Buton Resetează** pe tranșele neîncasate, pentru readucerea în ciornă (nota se anulează); pe o tranșă încasată se anulează întâi reconcilierea.
- **Recunoaștere venituri** (`Dr 475x = Cr 7584`, `Dr 472 = Cr 741x/7418`) — manuală sau prin cron lunar liniar, inactiv implicit.
- **Buget pe categorii de cheltuieli eligibile** cu realizat vs. aprobat, calculat din înregistrările contabile cu distribuție analitică pe proiect; **alertă de prag unică** pe categorie (o singură activitate, actualizată la fiecare recalcul, care dispare sub prag).
- **Cereri de rambursare** generate pe perioadă, cu linii per categorie bugetară (eligibil net, exclus, cheltuit brut), excluderi (conturi neeligibile precum 4426, furnizori afiliați) și suma solicitată = eligibil net × procent nerambursabil. Fără dublă decontare: cheltuielile din cereri depuse/aprobate/rambursate nu se mai cer, cele din cereri respinse pot fi cerute din nou; perioada propusă începe după ultima cerere nerespinsă; o cerere cu cheltuieli deja incluse în alta nu se poate depune.
- **Rapoarte PDF/Excel** ale cererii, pentru dosarul depus la finanțator. Cererea e document justificativ, fără notă contabilă.
- **Fișă consultant** pas-cu-pas cu 10 capturi de ecran (vezi mai sus).

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
- `l10n.ro.grant.tranche`: tranșa de plată primită de la finanțator, cu contabilizare automată (`Dr 4451 = Cr 475x/472`, încasare din extras).
- `l10n.ro.grant.recognition`: recunoașterea venitului din subvenție (`Dr 475x/472 = Cr 7584/741x/7418`), manuală sau generată de cronul lunar.
- `l10n.ro.grant.claim` (moștenește și `l10n_ro_anaf.report.handler.mixin`): cererea de rambursare depusă periodic la finanțator, cu perioada acoperită, generarea liniilor din AML-uri, totalurile eligibil/exclus/brut, suma solicitată și export PDF/Excel.
- `l10n.ro.grant.claim.line`: linia cererii de rambursare, agregată per categorie bugetară (eligibil net, exclus, cheltuit brut).

**Vizualizări**

- `l10n_ro_grant_views.xml`: formularul și lista contractului de finanțare, cu tab-urile Buget pe categorii, Tranșe primite, Recunoașteri venituri și Excluderi din baza eligibilă.
- `l10n_ro_grant_claim_views.xml`: formularul și lista cererilor de rambursare, cu liniile per categorie și butoanele de generare/depunere.

**Rapoarte**

- `report_actions.xml` / `report_grant_claim.xml`: raportul PDF al cererii de rambursare (situația eligibilității pentru dosarul depus la finanțator); export Excel disponibil din model (`xlsxwriter`).

**Acțiuni Automate / Acțiuni Server**

- `ir_cron.xml`: cron lunar **Recunoaștere lunară subvenții active (475→7584)**, inactiv implicit — calculează și contabilizează automat suma liniară pentru granturile pentru active aflate în starea „În derulare".

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): mixin de raportare (`l10n_ro_anaf.report.handler.mixin`) folosit de cererea de rambursare.
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): schema notelor contabile pentru tranșe și recunoașterea veniturilor.
- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): corelarea recunoașterii subvenției pentru active cu amortizarea activului finanțat.
