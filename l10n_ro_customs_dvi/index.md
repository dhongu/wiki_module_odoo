# Romania - Customs Import Declaration (DVI) (localizat la `l10n_ro_customs_dvi/index.md`)

- **Nume Tehnic:** `l10n_ro_customs_dvi`
- **Versiune:** `19.0.2.1.13`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_customs_dvi`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_customs_dvi`
- **Ultima Ingestie:** `2026-10-24`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)
- **Nume anterior:** `terrabit_dvi` (redenumit la 2026-09-23; vezi [terrabit_dvi](../terrabit_dvi/index.md))

#### 1. Sumar

Modulul înregistrează Declarația Vamală de Import (DVI) pentru importurile din afara Uniunii Europene, legând factura furnizorului extern de costurile vamale printr-un cost de aterizare (landed cost) atașat recepției. Din wizardul deschis de pe factura furnizor se transcriu sumele din declarație — taxa vamală (poziția A00), baza de impozitare și TVA-ul la import (poziția B00) — iar modulul repartizează taxa în costul stocului și generează nota de TVA. Taxele vamale majorează costul mărfii, în timp ce TVA-ul la import nu atinge costul. Nota contabilă primește ca referință numărul MRN al declarației, astfel încât plata către vamă să poată fi reconciliată pe contul 4462 per declarație. Modulul acoperă atât plata efectivă a TVA-ului în vamă, cât și importul fără plata TVA în vamă (de exemplu cu certificat de amânare). Costul de aterizare rămâne legat de factura furnizorului, iar liniile de TVA sunt legate de taxă, deci apar corect în SAF-T (D406).

#### 2. Funcționalități Cheie

- Wizard DVI pornit cu butonul **DVI** de pe factura furnizorului extern postată, care creează un cost de aterizare legat de recepțiile comenzii de achiziție. Sumele (taxă vamală A00, bază de impozitare, TVA B00, cotă, număr DVI) se **transcriu** din declarație, nu se recalculează; baza propusă implicit (netul facturii) este doar un punct de plecare, nu baza legală de la art. 289 din Legea 227/2015.
- Repartizează taxa vamală (A00) în costul de achiziție al mărfii, prin mecanismul nativ de cost adițional.
- **Două regimuri de TVA la import, comutate prin taxa aleasă în wizard** (fără câmp de configurare):
  - *plata efectivă în vamă* (art. 326 alin. (3)) — taxă obișnuită de achiziție, cu o singură linie de repartiție pe 4426: `Dr 4426 = Cr 4462`, datoria se stinge ulterior prin plată;
  - *fără plata TVA în vamă* (art. 326 alin. (4)-(5)) — **nu este taxare inversă**: TVA-ul se înregistrează atât ca taxă colectată, cât și ca deductibilă. Se alege o taxă cu două linii de repartiție, pe 4426 și 4427 — „21% IMP AM” sau „11% IMP AM” din `l10n_ro_anaf_d300` (rândurile 7 și 22 din decont): `Dr 4426 = Cr 4427`, fără 4462 și fără plată. Regimul acoperă certificatul de amânare, vămuirea centralizată, înscrierea în evidențele declarantului și bunurile din art. 331 alin. (2) lit. b), c), i)–k).
  - Condiția de deducere diferă: la plata în vamă, dovada plății (art. 299 alin. (1) lit. c)); fără plată în vamă, declarația pe numele importatorului cu TVA datorat și taxa înscrisă ca colectată în aceeași perioadă (lit. d)).
- Liniile de TVA ale notei sunt legate de taxă (linia de repartiție a taxei), iar linia tehnică de bază poartă și ea taxa; astfel TVA-ul la import este exportat corect în SAF-T (D406), nu cu TaxCode 000000 și sumă zero, și este luat în calcul la închiderea TVA din Odoo. Nota de TVA poartă etichetele fiscale ale taxei, plus o pereche tehnică echilibrată pe contul neutru 473 care poartă eticheta de bază, ca rândul din D300 să nu iasă cu TVA și cu bază zero.
- Taxa vamală se creditează pe **4462** „Alte impozite, taxe și vărsăminte asimilate — reluate într-o perioadă de până la un an” (datorie curentă; atenție, 4461 înseamnă peste un an). Dacă planul nu are 4462, se folosește orice cont 446.
- Numărul declarației (MRN) devine referința notei contabile, pentru reconcilierea plății pe 4462 per declarație. Biroul vamal **nu** se creează ca partener; soldul se urmărește pe cont.
- Câmpuri DVI pe costul de aterizare (tip, număr MRN, cotă, bază, valoare TVA), filtru dedicat și coloană în listă; meniu propriu „DVI — Costuri vamale”, cu lista filtrată pe costurile de tip DVI și grupată pe dată.
- Etichete neutre, valabile în ambele regimuri: rândurile notei se numesc „Import VAT - <taxă>”, iar câmpul „Import VAT Amount”; eticheta veche „TVA plătit în vamă” era folosită greșit și la importurile fără plata TVA în vamă. Notele deja postate păstrează eticheta veche.
- Costul de aterizare creat de wizard este legat de factura furnizorului prin câmpul standard **Vendor Bill**: câmpul arată factura, factura primește butonul inteligent „Landed Costs”, iar detaliile de evaluare a stocului numesc factura. Se leagă doar facturile (nu notele de credit); costurile create înainte de 2.1.7 rămân fără legătură.
- Ajutoare extinse pe fiecare câmp al wizardului și casetă de îndrumare cu maparea poziție din declarație → câmp. Valoarea din câmpul „Import VAT Amount” (TVA la import) nu se recalculează la schimbarea bazei sau a cotei — se modifică manual.
- **Comisionul vamal a fost eliminat** (nu există comision datorat autorității vamale; câmpul era folosit greșit pentru onorariul brokerului). Onorariul **comisionarului vamal** nu se operează prin wizard: brokerul e furnizor obișnuit cu sold pe 401, factura lui se înregistrează pe un produs serviciu marcat „Este un cost adițional”. Contul de cheltuială al produsului este **473** (tranzit) dacă onorariul se capitalizează prin butonul „Creați costuri adiționale” de pe factură, respectiv **622** dacă nu se capitalizează. Atenție: dacă onorariul a fost inclus în baza B00, poate fi facturat fără TVA.
- Fișa consultant detaliază baza legală (art. 289, 290, 294, 299, 326), tratamentul transportului, monografia și verificările de după validare; conține și fluxul pas cu pas pentru importul fără plata TVA în vamă („21% IMP AM” / „11% IMP AM”, cu capturi), note despre raportare (inclusiv D406) și secțiunea despre **restituirea TVA plătit în vamă**: cazurile cu temei legal, notele contabile și un model de cerere (Anexa A). Nu sunt refăcute aici.
- Produsul de serviciu generat pentru taxa vamală e marcat ca cost adițional, deci funcționează și pe traseul nativ „factură furnizor → Creați costuri adiționale”.
- **Regim vamal** (4000 / 4200 / altul), pe wizard și pe costul de aterizare. La regimul 4200 (import scutit de TVA, art. 293 alin. (1) lit. m), urmat de livrare intracomunitară) wizardul propune taxa scutită „0% EXEMPT”, fără TVA la import, iar nota conține doar baza, pe rândul 29 din D300, prin perechea tehnică pe 473. TVA-ul reținut de vamă ca garanție nu se contabilizează; un DVI 4200 cu TVA la import este refuzat. Câmpuri informative „TVA reținut ca garanție” și „Stare garanție” (Blocată / Eliberată), buton „Marcat ca eliberat” și filtru dedicat; fără notă contabilă (înregistrările pe 2678 rămân manuale).
- **Furnizorul extern pe antetul notei DVI**: nota primește ca partener furnizorul facturii, astfel că jurnalul de cumpărări afișează importul cu numele și codul fiscal al furnizorului; se schimbă doar antetul, liniile de TVA și taxă vamală își păstrează partenerul. Fișa precizează că importul apare o singură dată în jurnalul de cumpărări, pe nota DVI, și este exclus din D394.
- **Multi-company (#685)**: contul de decontare cu bugetul (4462) se ia direct din planul companiei DVI, iar contul de cheltuială al produsului „Taxă vamală” se completează pentru acea companie la prima utilizare; înainte, la o companie diferită de cea care a creat produsul, TVA-ul plătit în vamă și taxa vamală ajungeau pe contul de cheltuială al categoriei (607).
- Dacă DVI-ul nu are taxă vamală, nota pentru TVA la import (sau baza scutită) se postează automat, nu rămâne în ciornă.
- Fișa consultant (Pasul 5) trimite la modulul [`l10n_ro_customs_dvi_import`](../l10n_ro_customs_dvi_import/index.md) pentru completarea DVI din PDF-ul declarației tipărite din SNI; transcrierea manuală rămâne pentru declarațiile primite fără acel PDF.
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
- `stock.landed.cost` (extins): câmpurile `landed_type`, `dvi_number`, `customs_regime`, `tax_id`, `tax_base`, `tax_value` (etichetat „Import VAT Amount”), `vat_guarantee_amount`, `vat_guarantee_state` (acțiunea `action_release_vat_guarantee`); `_set_dvi_move_partner()` completează partenerul antetului notei; wizardul completează și `vendor_bill_id` cu factura furnizorului; la validare adaugă nota de TVA la import. `_prepare_tax_lines()` urmează liniile de repartiție ale taxei (plată efectivă sau fără plată în vamă), legând fiecare linie de `tax_repartition_line_id`, `_prepare_tax_base_lines()` adaugă perechea tehnică pe 473 (linia de bază poartă taxa), iar referința notei devine numărul MRN.
- `account.move` (extins): câmpul `dvi_id` și butonul **DVI**, vizibil doar pe facturile furnizor postate. Refuză pornirea dacă partenerul nu are țara completată.

**Vizualizări**

- `views/account_invoice_view.xml`: butonul DVI pe factura furnizor.
- `views/stock_landed_cost_view.xml`: câmpurile DVI, filtrul și coloana în lista costurilor de aterizare, meniul „DVI — Costuri vamale”.
- `wizard/account_dvi_view.xml`: formularul wizardului DVI, cu ajutoare pe câmpuri și caseta de îndrumare.

**Acțiuni Automate / Acțiuni Server**

- `pre_init_hook`: la instalare preia înregistrările `ir_model_data` ale modulului redenumit `terrabit_dvi`, ca actualizarea să nu producă view-uri, acțiuni și meniuri duplicate. Nu există cron-uri. O migrare `post-migrate` completează partenerul pe notele DVI 2026 postate fără partener (în afara perioadelor blocate).

#### 5. Conexiuni

- `stock_landed_costs`: mecanismul nativ de repartizare a costurilor adiționale în valoarea stocului, folosit pentru taxele vamale și pentru onorariul brokerului.
- `l10n_ro`: localizarea contabilă românească, sursa pentru conturile 446/4462, 4426, 4427 și 473.
- `l10n_ro_dvi`: modul OCA cu funcționalitate similară, exclus prin manifest (`excludes`) — cele două nu pot coexista pe același `addons_path`.
- [`l10n_ro_invoice_dvi_protect`](../l10n_ro_invoice_dvi_protect/index.md): complementar; blochează resetarea facturii și anularea costului de aterizare după ce stocul a fost consumat FIFO.
- [`terrabit_dvi`](../terrabit_dvi/index.md): numele anterior, păstrat ca modul tranzitoriu fără conținut, până la portarea pe 20.0.
- [`l10n_ro_customs_dvi_import`](../l10n_ro_customs_dvi_import/index.md): modul complementar, trimiterea din Pasul 5 al fișei; completează DVI din PDF-ul declarației vamale tipărite din SNI.
- [`l10n_ro_anaf_d300`](../l10n_ro_anaf_d300/index.md): TVA-ul la import ajunge în declarație prin etichetele fiscale ale taxei; furnizează și taxele „21% IMP AM” / „11% IMP AM” pentru importul fără plata TVA în vamă.

#### 6. Istoric

- **19.0.2.1.13** (2026-10-24) — fișa consultant, Pasul 5: trimitere către `l10n_ro_customs_dvi_import` pentru completarea DVI din PDF-ul SNI.
- **19.0.2.1.12** (2026-10-24) — fix multi-company (#685): contul 4462 se ia din planul companiei DVI, nu din contul de cheltuială al categoriei produsului (607).
- **19.0.2.1.11** (2026-10-24) — fișa: furnizorul pe antetul notei DVI (Pasul 7, §2.6), jurnalul de cumpărări afișează importul o singură dată, D394 îl exclude (§7), două verificări noi (§8).
- **19.0.2.1.10** (2026-10-24) — nota DVI poartă furnizorul extern al facturii pe antet; la actualizare se completează notele DVI 2026 postate fără partener, în afara perioadelor blocate.
- **19.0.2.1.9** (2026-10-16) — fișa, regim 4200: factura intracomunitară se emite înainte de vămuire, pasul nou 12 cu fluxul de vânzare, luna de raportare și riscul unui D390 lipsă sau greșit.
- **19.0.2.1.8** (2026-10-16) — câmp nou „Regim vamal” (4000 / 4200 / altul); la 4200 nota conține doar baza, pe rândul 29 din D300; câmpuri informative pentru garanția de TVA; nota fără taxă vamală se postează acum automat.
- **19.0.2.1.7** (2026-10-16) — costul de aterizare creat de wizard este legat de factura furnizorului prin câmpul standard *Vendor Bill* (rămas până acum gol): butonul inteligent „Landed Costs” pe factură și factura numită în detaliile de evaluare. Costurile vechi rămân nelegate.
- **19.0.2.1.6** (2026-10-16) — etichete neutre „Import VAT - <taxă>” și „Import VAT Amount”, valabile în ambele regimuri; eticheta „TVA plătit în vamă” ajungea în registrul jurnal și în SAF-T și la importurile fără plata TVA în vamă.
- **19.0.2.1.5** (2026-10-16) — fișa consultant: flux pas cu pas pentru importul fără plata TVA în vamă („21% IMP AM” / „11% IMP AM”), două capturi noi, note despre D406 și secțiune despre restituirea TVA plătit în vamă (cazuri cu temei legal, note contabile, model de cerere — Anexa A).
- **19.0.2.1.4** (2026-10-16) — SAF-T (D406): liniile de TVA ale notei sunt legate de taxă (linie de repartiție), iar linia tehnică de bază poartă taxa; înainte erau exportate cu TaxCode 000000 și TaxAmount 0. Etichetele din decont rămân neschimbate, iar închiderea TVA din Odoo ia acum în calcul TVA-ul DVI.
- **19.0.2.1.3** (2026-10-09) — banner pentru Odoo Apps generat din `banner.json`.
- **19.0.2.1.2** (2026-10-04) — documentația și ajutorul câmpului: regimul fără plata TVA în vamă acoperă toate cele patru cazuri și este descris ca TVA înregistrat atât colectat, cât și deductibil, nu ca taxare inversă; taxa de ales: „21% IMP AM” / „11% IMP AM”; condiția de deducere separată pe regimuri.
- **19.0.2.1.1** (2026-09-30) — pictogramă proprie a modulului.
- **19.0.2.1.0** (2026-09-23) — amânarea plății TVA în vamă (art. 326 alin. (4)-(5)): nota urmează liniile de repartiție ale taxei alese; cu taxe „IMP AM” se generează `Dr 4426 = Cr 4427`, fără datorie la buget. Fișa descrie acum cele două regimuri.
- **19.0.2.0.0** (2026-09-23) — eliminat câmpul „Comision vamal”: nu există un comision datorat autorității vamale, cel de 0,5% a dispărut odată cu aderarea la UE. Taxa vamală trece pe analiticul **4462** (datorie curentă), onorariul brokerului se contabilizează pe 622 (sau 473 în tranzit, dacă se capitalizează), iar baza importului ajunge în decont printr-o pereche tehnică pe **473**.
- **19.0.1.3.0** (2026-09-23) — redenumit din `terrabit_dvi`; comisionul mutat de pe 447 pe 446; ajutoare și casetă de îndrumare în wizard.
