# Romania - Partner Financial Data (MFinanțe) (localizat la `l10n_ro_partner_financials/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_financials`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_financials
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_financials`
- **Ultima Ingestie:** 2026-09-12

#### 1. Sumar

Modulul aduce pe fișa partenerului situațiile financiare publice depuse la Ministerul Finanțelor, preluate direct din serviciul deschis MFinanțe/ANAF, fără abonament la un furnizor comercial de date. Pe lângă cifrele brute (cifră de afaceri, profit, datorii, capitaluri, salariați), calculează automat indicatori de bonitate — inclusiv un semnal dedicat pentru capitaluri proprii negative — utili în evaluarea rapidă a riscului comercial al unui client sau furnizor.

#### 2. Funcționalități Cheie

- Preluare din registrul public MFinanțe/ANAF a poziției financiare (active, stocuri, creanțe, disponibilități, datorii totale, provizioane, capitaluri proprii, capital subscris vărsat) și a performanței (cifră de afaceri netă, venituri/cheltuieli totale, rezultat brut și net, număr mediu de salariați), plus denumirea raportată și codul CAEN.
- Indicatori de bonitate calculați automat: lichiditate (active circulante/datorii totale), solvabilitate (capitaluri proprii/total active), grad de îndatorare, marjă netă, rentabilitatea capitalului, cifră de afaceri pe salariat.
- Avertizare de **capitaluri proprii negative** (situația din art. 153^24 din Legea 31/1990), afișată pe fișa partenerului și disponibilă ca filtru dedicat în lista de contacte (*Negative Equity*).
- Buton **Retrieve from MFinanțe** pe fila *Financial Data* a partenerului, plus buton statistic în antet către istoricul complet pe ani.
- Fila *Reported Indicators* a fiecărui an păstrează lista brută a indicatorilor exact cum au fost raportați de ANAF, pentru audit.
- Raport de ansamblu la *Contabilitate → Raportare → Partner Financial Data*, cu filtre pentru capitaluri proprii negative, parteneri pe pierdere și societăți care depun alt formular decât cel standard (non-financiar).
- Acțiune programată „RO: Fetch partner financial data (MFinanțe)" pentru preluare automată în loturi (livrată dezactivată), cu cadență de o cerere pe secundă și reinterogare temporizată a partenerilor fără bilanț depus.
- Configurare la *Contabilitate → Configurări → Setări → Partner Financial Data (RO)*: numărul de ani fiscali de preluat (implicit 3) și numărul de zile după care se reinterogează un partener fără bilanț găsit (implicit 30); adresa serviciului e reglabilă din parametrul de sistem `l10n_ro_partner_financials.mfinante_url`.
- Nu include scoruri proprietare de tip rating financiar sau probabilitate de insolvență — acestea rămân în module-conector separate, cu abonamentul furnizorului respectiv.

#### 3. Dependențe

- `base`
- `account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.partner.financials`: o înregistrare per partener/an, cu indicatorii de poziție financiară și performanță preluați de la MFinanțe, plus rezultatele derivate (`gross_result`, `net_result`, `total_assets`) și indicatorii de bonitate (`liquidity_ratio`, `solvency_ratio` etc.), calculați din câmpurile brute. Maparea indicatorilor ANAF pe câmpurile modelului se face după denumirea normalizată a indicatorului, nu după codul „I<n>", pentru că acele coduri nu sunt stabile între formularele de raportare (societăți nefinanciare vs. instituții de credit).
- `res.partner` (extensie): adaugă `l10n_ro_financials_ids` (one2many către istoricul pe ani) și câmpuri de rezumat calculate pe ultimul an disponibil (`l10n_ro_financials_turnover`, `..._net_result`, `..._equity`, `..._employees`, `..._liquidity`, `..._negative_equity`); expune metodele de preluare (`l10n_ro_financials_fetch`, `action_l10n_ro_financials_fetch`) și logica de eligibilitate — doar persoane juridice române cu CUI, cu excluderea partenerilor companiilor proprii din baza de date.
- `res.config.settings` (extensie): parametrii `l10n_ro_partner_financials.years` (Years to Retrieve) și `l10n_ro_partner_financials.retry_days` (Retry After).

**Vizualizări**

- `l10n_ro_partner_financials_views.xml`: formularul/lista anului financiar (bilanț, cont de profit și pierdere, indicatori de bonitate, fila *Reported Indicators*) și raportul de ansamblu din meniul Contabilitate → Raportare.
- `res_partner_views.xml`: fila *Financial Data* pe fișa partenerului (buton *Retrieve from MFinanțe*, buton statistic, avertizare capitaluri negative) și filtrul *Negative Equity* în lista de contacte.
- `res_config_settings_views.xml`: secțiunea *Partner Financial Data (RO)* din setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_cron.xml` — „RO: Fetch partner financial data (MFinanțe)": rulează `_cron_l10n_ro_financials_fetch`, care completează în loturi (implicit 100 parteneri) bilanțurile lipsă pentru ultimul an disponibil; livrată dezactivată, se activează din Setări → Tehnic → Acțiuni programate.

#### 5. Conexiuni

- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): modul înrudit din aceeași suită, tot pentru sincronizare de date de partener cu ANAF, dar pe un serviciu diferit (scpTVA/validare partener, nu bilanțuri publice).
