# Romania - Customs Import Declaration (DVI) (localizat la `l10n_ro_customs_dvi/index.md`)

- **Nume Tehnic:** `l10n_ro_customs_dvi`
- **Versiune:** `19.0.2.0.0`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_customs_dvi`
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_customs_dvi`
- **Ultima Ingestie:** `2026-09-23`
- **Nume anterior:** `terrabit_dvi` (redenumit la 2026-09-23; vezi [terrabit_dvi](../terrabit_dvi/index.md))

#### 1. Sumar

Modulul înregistrează Declarația Vamală de Import (DVI) pentru importurile din afara Uniunii Europene, legând factura furnizorului extern de costurile vamale printr-un cost de aterizare (landed cost) atașat recepției. Din wizardul deschis de pe factura furnizor se transcriu sumele din declarație — taxa vamală (poziția A00), baza de impozitare și TVA-ul plătit în vamă (poziția B00) — iar modulul repartizează taxa în costul stocului și generează nota de TVA deductibilă. Taxele vamale majorează costul mărfii, în timp ce TVA-ul la import rămâne deductibil pe contul 4426, fără să atingă costul. Nota contabilă primește ca referință numărul MRN al declarației, astfel încât plata către vamă să poată fi reconciliată pe contul 4462 per declarație. Tot în notă intră o pereche tehnică pe un cont neutru 473, care duce baza importului în decontul de TVA.

#### 2. Funcționalități Cheie

- Wizard DVI pornit de pe factura furnizorului postată, care creează un cost de aterizare legat de recepțiile comenzii de achiziție.
- Repartizează taxa vamală (A00) în costul de achiziție al mărfii, prin mecanismul nativ de cost adițional.
- Generează nota de TVA la import — Dr 4426 = Cr 4462 — cu eticheta fiscală de taxă, plus o pereche tehnică echilibrată pe contul 473 care poartă eticheta de bază, fără de care rândul din D300 ar ieși cu TVA și cu bază zero.
- Creditează taxa vamală pe **4462** „Alte impozite, taxe și vărsăminte asimilate — reluate într-o perioadă de până la un an”: datoria vamală se stinge în zile, deci e datorie curentă (OMFP 1802/2014 pct. 360). Atenție la ordinea contraintuitivă din planul RO — 4461 înseamnă **peste** un an.
- Scrie numărul declarației (MRN) ca referință a notei contabile, pentru reconcilierea plății pe 4462 per declarație.
- Câmpuri DVI pe costul de aterizare (tip, număr MRN, cotă, bază, valoare TVA), filtru dedicat și coloană în listă.
- Meniu propriu „DVI — Costuri vamale", cu lista filtrată pe costurile de tip DVI și grupată pe dată.
- Ajutoare extinse pe fiecare câmp al wizardului și o casetă de îndrumare cu maparea poziție din declarație → câmp.
- Produsul de serviciu generat automat pentru taxa vamală e marcat ca fiind cost adițional, deci funcționează și pe traseul nativ „factură furnizor → Creați costuri adiționale”.
- Onorariul comisionarului vamal **nu** se operează prin wizard: brokerul e furnizor obișnuit, cu sold pe 401, iar onorariul se capitalizează prin mecanismul nativ de cost adițional de pe factura lui.
- Se exclude reciproc cu modulul OCA `l10n_ro_dvi`.

#### 3. Dependențe

- `stock_account`
- `account`
- `sale`
- `l10n_ro`
- `purchase_stock`
- `stock_landed_costs`

#### 4. Componente Cheie

- `account.invoice.dvi` (wizard tranzitoriu): colectează sumele din declarație și creează costul adițional. Precompletează baza cu netul facturii furnizorului — valoare orientativă, nu baza definită de art. 289 din Legea 227/2015. `_get_customs_payable_account()` alege analiticul de scadență scurtă și filtrează pe companie.
- `stock.landed.cost` (extins): câmpurile `landed_type`, `dvi_number`, `tax_id`, `tax_base`, `tax_value`; la validare adaugă nota de TVA la import, perechea tehnică de bază prin `_prepare_tax_base_lines()` și înlocuiește referința notei cu numărul MRN.
- `account.move` (extins): câmpul `dvi_id` și butonul **DVI**, vizibil doar pe facturile furnizor postate. Refuză pornirea dacă partenerul nu are țara completată.
- `pre_init_hook`: la instalare preia înregistrările `ir_model_data` ale modulului redenumit `terrabit_dvi`, ca actualizarea să nu producă view-uri, acțiuni și meniuri duplicate.

#### 5. Conexiuni

- `stock_landed_costs`: mecanismul nativ de repartizare a costurilor adiționale în valoarea stocului, pe care modulul îl folosește pentru taxele vamale.
- `l10n_ro`: localizarea contabilă românească, sursa pentru conturile 4462 și 473 folosite la DVI.
- `l10n_ro_dvi`: modul OCA cu funcționalitate similară, exclus prin manifest (`excludes`) — cele două nu pot coexista pe același `addons_path`.
- [`l10n_ro_invoice_dvi_protect`](../l10n_ro_invoice_dvi_protect/index.md): complementar; blochează resetarea facturii și anularea costului de aterizare după ce stocul a fost consumat FIFO.
- [`terrabit_dvi`](../terrabit_dvi/index.md): numele anterior, păstrat ca modul tranzitoriu fără conținut, până la portarea pe 20.0.
- `l10n_ro_anaf_d300`: TVA-ul deductibil la import ajunge în declarație prin etichetele fiscale ale taxei.

#### 6. Istoric

- **19.0.2.0.0** (2026-09-23) — eliminat câmpul „Comision vamal”: nu există un comision datorat autorității vamale, cel de 0,5% a dispărut odată cu aderarea la UE. În practică era folosit pentru onorariul brokerului, cu contul greșit (446 în loc de 401) și fără TVA deductibilă. Taxa vamală trece pe analiticul **4462** (datorie curentă), iar baza importului ajunge în decont printr-o pereche tehnică pe **473**.
- **19.0.1.3.0** (2026-09-23) — redenumit din `terrabit_dvi`; comisionul mutat de pe 447 pe 446; ajutoare și casetă de îndrumare în wizard.
