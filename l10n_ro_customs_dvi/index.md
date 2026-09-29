# Romania - Customs Import Declaration (DVI) (localizat la `l10n_ro_customs_dvi/index.md`)

- **Nume Tehnic:** `l10n_ro_customs_dvi`
- **Versiune:** `19.0.2.1.0`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_customs_dvi`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_customs_dvi`
- **Ultima Ingestie:** `2026-09-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Nume anterior:** `terrabit_dvi` (redenumit la 2026-09-23; vezi [terrabit_dvi](../terrabit_dvi/index.md))

#### 1. Sumar

Modulul înregistrează Declarația Vamală de Import (DVI) pentru importurile din afara Uniunii Europene, legând factura furnizorului extern de costurile vamale printr-un cost de aterizare (landed cost) atașat recepției. Din wizardul deschis de pe factura furnizor se transcriu sumele din declarație — taxa vamală (poziția A00), baza de impozitare și TVA-ul din vamă (poziția B00) — iar modulul repartizează taxa în costul stocului și generează nota de TVA. Taxele vamale majorează costul mărfii, în timp ce TVA-ul la import nu atinge costul. Nota contabilă primește ca referință numărul MRN al declarației, astfel încât plata către vamă să poată fi reconciliată pe contul 4462 per declarație. Modulul acoperă atât plata efectivă a TVA-ului în vamă, cât și amânarea plății pentru firmele cu certificat de amânare.

#### 2. Funcționalități Cheie

- Wizard DVI pornit cu butonul **DVI** de pe factura furnizorului extern postată, care creează un cost de aterizare legat de recepțiile comenzii de achiziție. Sumele (taxă vamală A00, bază de impozitare, TVA B00, cotă, număr DVI) se **transcriu** din declarație, nu se recalculează; baza propusă implicit (netul facturii) este doar un punct de plecare, nu baza legală de la art. 289 din Legea 227/2015.
- Repartizează taxa vamală (A00) în costul de achiziție al mărfii, prin mecanismul nativ de cost adițional.
- **Două regimuri de TVA în vamă, comutate prin taxa aleasă în wizard** (fără câmp de configurare):
  - *plata efectivă* (art. 326 alin. (3)) — taxă obișnuită de achiziție, cu o singură linie de repartiție pe 4426: `Dr 4426 = Cr 4462`, datoria se stinge ulterior prin plată;
  - *amânarea de la plată* (art. 326 alin. (4)-(5)) — taxă cu taxare inversă (două linii, 4426 și 4427, ex. „VAT Reverse Tax”): `Dr 4426 = Cr 4427`, fără 4462 și fără plată, taxa apărând în decont și ca deductibilă, și ca colectată. Firmele cu certificat de amânare trebuie să aleagă taxa corespunzătoare.
- Nota de TVA poartă etichetele fiscale ale taxei, plus o pereche tehnică echilibrată pe contul neutru 473 care poartă eticheta de bază, ca rândul din D300 să nu iasă cu TVA și cu bază zero.
- Taxa vamală se creditează pe **4462** „Alte impozite, taxe și vărsăminte asimilate — reluate într-o perioadă de până la un an” (datorie curentă; atenție, 4461 înseamnă peste un an). Dacă planul nu are 4462, se folosește orice cont 446.
- Numărul declarației (MRN) devine referința notei contabile, pentru reconcilierea plății pe 4462 per declarație. Biroul vamal **nu** se creează ca partener; soldul se urmărește pe cont.
- Câmpuri DVI pe costul de aterizare (tip, număr MRN, cotă, bază, valoare TVA), filtru dedicat și coloană în listă; meniu propriu „DVI — Costuri vamale”, cu lista filtrată pe costurile de tip DVI și grupată pe dată.
- Ajutoare extinse pe fiecare câmp al wizardului și casetă de îndrumare cu maparea poziție din declarație → câmp. Valoarea „TVA plătit în vamă” nu se recalculează la schimbarea bazei sau a cotei — se modifică manual.
- **Comisionul vamal a fost eliminat** (nu există comision datorat autorității vamale; câmpul era folosit greșit pentru onorariul brokerului). Onorariul **comisionarului vamal** nu se operează prin wizard: brokerul e furnizor obișnuit cu sold pe 401, factura lui se înregistrează pe un produs serviciu marcat „Este un cost adițional”. Contul de cheltuială al produsului este **473** (tranzit) dacă onorariul se capitalizează prin butonul „Creați costuri adiționale” de pe factură, respectiv **622** dacă nu se capitalizează. Atenție: dacă onorariul a fost inclus în baza B00, poate fi facturat fără TVA.
- Fișa consultant detaliază baza legală (art. 289, 290, 294, 299, 326), tratamentul transportului, monografia și verificările de după validare; nu sunt refăcute aici.
- Produsul de serviciu generat pentru taxa vamală e marcat ca cost adițional, deci funcționează și pe traseul nativ „factură furnizor → Creați costuri adiționale”.
- Se exclude reciproc cu modulul OCA `l10n_ro_dvi`.

#### 3. Dependențe

- `stock_account`
- `account`
- `sale`
- `l10n_ro`
- `purchase_stock`
- `stock_landed_costs`

#### 4. Componente Cheie

**Modele**

- `account.invoice.dvi` (wizard tranzitoriu): colectează sumele din declarație și creează costul adițional. Precompletează baza cu netul facturii furnizorului — valoare orientativă. `_get_customs_payable_account()` caută întâi 4462, apoi orice 446, filtrat pe companie.
- `stock.landed.cost` (extins): câmpurile `landed_type`, `dvi_number`, `tax_id`, `tax_base`, `tax_value`; la validare adaugă nota de TVA la import. `_prepare_tax_lines()` urmează liniile de repartiție ale taxei (plată efectivă sau amânare), `_prepare_tax_base_lines()` adaugă perechea tehnică pe 473, iar referința notei devine numărul MRN.
- `account.move` (extins): câmpul `dvi_id` și butonul **DVI**, vizibil doar pe facturile furnizor postate. Refuză pornirea dacă partenerul nu are țara completată.

**Vizualizări**

- `views/account_invoice_view.xml`: butonul DVI pe factura furnizor.
- `views/stock_landed_cost_view.xml`: câmpurile DVI, filtrul și coloana în lista costurilor de aterizare, meniul „DVI — Costuri vamale”.
- `wizard/account_dvi_view.xml`: formularul wizardului DVI, cu ajutoare pe câmpuri și caseta de îndrumare.

**Acțiuni Automate / Acțiuni Server**

- `pre_init_hook`: la instalare preia înregistrările `ir_model_data` ale modulului redenumit `terrabit_dvi`, ca actualizarea să nu producă view-uri, acțiuni și meniuri duplicate. Nu există cron-uri.

#### 5. Conexiuni

- `stock_landed_costs`: mecanismul nativ de repartizare a costurilor adiționale în valoarea stocului, folosit pentru taxele vamale și pentru onorariul brokerului.
- `l10n_ro`: localizarea contabilă românească, sursa pentru conturile 446/4462, 4426, 4427 și 473 și pentru taxele cu taxare inversă.
- `l10n_ro_dvi`: modul OCA cu funcționalitate similară, exclus prin manifest (`excludes`) — cele două nu pot coexista pe același `addons_path`.
- [`l10n_ro_invoice_dvi_protect`](../l10n_ro_invoice_dvi_protect/index.md): complementar; blochează resetarea facturii și anularea costului de aterizare după ce stocul a fost consumat FIFO.
- [`terrabit_dvi`](../terrabit_dvi/index.md): numele anterior, păstrat ca modul tranzitoriu fără conținut, până la portarea pe 20.0.
- [`l10n_ro_anaf_d300`](../l10n_ro_anaf_d300/index.md): TVA-ul la import ajunge în declarație prin etichetele fiscale ale taxei.

#### 6. Istoric

- **19.0.2.1.0** (2026-09-23) — amânarea plății TVA în vamă (art. 326 alin. (4)-(5)): nota urmează liniile de repartiție ale taxei alese; cu taxare inversă se generează `Dr 4426 = Cr 4427`, fără datorie la buget. Fișa descrie acum cele două regimuri.
- **19.0.2.0.0** (2026-09-23) — eliminat câmpul „Comision vamal”: nu există un comision datorat autorității vamale, cel de 0,5% a dispărut odată cu aderarea la UE. Taxa vamală trece pe analiticul **4462** (datorie curentă), onorariul brokerului se contabilizează pe 622 (sau 473 în tranzit, dacă se capitalizează), iar baza importului ajunge în decont printr-o pereche tehnică pe **473**.
- **19.0.1.3.0** (2026-09-23) — redenumit din `terrabit_dvi`; comisionul mutat de pe 447 pe 446; ajutoare și casetă de îndrumare în wizard.
