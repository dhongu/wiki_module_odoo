# Romania - Declarație informativă (D394) (localizat la `l10n_ro_anaf_d394/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d394`
- **Versiune:** `19.0.1.9.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d394
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d394`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul dedicat contabililor care lucrează cu legislația fiscală din România, oferind instrumentele necesare pentru generarea Jurnalului de Vânzări, a Jurnalului de Cumpărări și a Declarației Informative D394 conform cerințelor ANAF. Utilizează infrastructura centralizată din `l10n_ro_anaf_base` (validare XSD, mixin date companie/reprezentant, înregistrare MIME fișiere XDP).

#### 2. Funcționalități Cheie

- **Automatizare completă:** datele sunt preluate direct din facturile înregistrate, asigurând corelația între contabilitate și raportarea fiscală.
- **Detaliere pe cote de TVA:** rapoartele separă automat tranzacțiile pe cotele de TVA și pe tipuri de operațiuni (taxabile, scutite, taxare inversă).
- **Control și audit:** permite verificarea rapidă a sumelor prin accesarea directă a documentului sursă.
- **Gestionare TVA la încasare (CABA):** identifică automat facturile sub regimul TVA la încasare și raportează exigibilitatea taxei în momentul plății; evidențiază sumele neexigibile (din facturile neplătite) și sumele devenite exigibile în urma încasărilor/plăților din perioada curentă.
- **Taxare inversă (Reverse Charge):** identifică automat tranzacțiile cu taxare inversă și le clasifică corect — tip V pentru livrări RC, tip C pentru achiziții RC; ambele tipuri sunt incluse corect în D394, chiar dacă cota TVA este 0.
- **Export XLSX avansat:** jurnalele pot fi exportate în format Excel cu coloane dinamice pentru fiecare tip de taxă identificat în documente, optimizat pentru audit și verificare detaliată.
- **Generare D394 (XDP și XML Soft J):** butoanele „D394 file XDP" și „D394 file XML" sunt disponibile direct pe rapoartele de vânzări și cumpărări; fișierul generat poate fi importat în formularul PDF inteligent ANAF sau validat direct în aplicația DUKIntegrator (Soft J). Fișierul XML trece validatorul oficial (`D394Validator.jar`) fără erori — atributele opționale fără valoare nu mai sunt emise goale, adresa reprezentantului se completează corect prin fallback pe adresa companiei, iar `efectuat` nu mai apare alături de `solicit=0`.
- **Clasificare automată Partener 1 / Partener 2:** partenerii înregistrați în scopuri TVA (Cartușul C) sunt separați automat de persoanele fizice și juridice neînregistrate TVA (Cartușul D), conform structurii XML D394.
- **Gestionare parteneri inactivi fiscal:** operațiunile cu parteneri declarați inactivi sunt clasificate corect în Cartușul C (perioada activă) și Cartușul D (perioada de inactivitate).
- **Opțiuni declarație configurabile:** periodicitate TVA, sistem TVA la încasare, opțiune contribuabil și persoane afiliate — configurabile per companie în Setări.
- **Accesare rapoarte:** din Contabilitate → Raportare → Declarații ANAF → Declarație 394 (deschide direct raportul de vânzări; perioada implicită este luna trecută) sau din Contabilitate → Raportare → Taxe (Jurnal TVA Vânzări (RO) / Jurnal TVA Cumpărări (RO)); butonul D394 colectează automat atât vânzările, cât și cumpărările, indiferent din care raport este apăsat. Sub rândul **Total** al fiecărui jurnal, **Recapitulația pe rânduri D300** arată sumele pe rândurile decontului (coloanele **Bază D300** și **TVA D300**).
- **Raportarea pe cartușe (A–I):** structura declarației urmează cartușele ANAF — datele firmei și ale persoanei care depune (A, B), parteneri înregistrați TVA (C), neînregistrați (D; pentru persoane fizice se exportă CNP-ul din *Tax ID*, iar în lipsa lui adresa completă pe 8 componente), parteneri UE/non-UE nestabiliți în RO (E/F), încasări AMEF (G; bonul fiscal pentru care s-a emis și factură se scade din total, iar factura se raportează în C sau D), rezumat valoric (H) și plaja de facturi/facturi simplificate/autofacturi (I).
- **Tipuri de partener 1–4** (din 19.0.1.7.0), încadrate pe fiecare document, la data lui: 1 = înregistrat în scopuri de TVA (perioadele ANAF din `l10n_ro_anaf_partner`; fără ele, bifa „Plătitor de TVA” sau codul RO), 2 = neînregistrat (CNP, CUI fără RO, inactiv la data documentului, străin fără cod), 3 = alt stat UE, 4 = în afara UE, cu cod. Facturile către persoane fizice și firme neînregistrate se declară câte un rând pe beneficiar. Partenerii străini nu mai sunt excluși după țară: livrările cu TVA românesc intră la tip 3/4, iar serviciile cu taxare inversă de la prestatori din afara UE la tip 4; achizițiile intracomunitare rămân în D390, iar importul nu se declară în D394. O verificare prealabilă oprește operațiunile nepermise pe tipurile 2–4 (ex. taxare inversă către un neînregistrat).
- **Achiziții de la neînregistrați** (din 19.0.1.7.0): se declară la N (cota 0, fără TVA), pe tipul documentului; la persoanele fizice, pe codul D394 al produsului. Pentru bunurile cumpărate de la persoane fizice fără cod de produs D394 apare un avertisment pe jurnal: se declară la 34 „alte bunuri”, dar cerealele, deșeurile (22), masa lemnoasă (23), terenurile (32) și construcțiile (33) trebuie setate pe produs sau pe categorie.
- **Câmpul „Tip document D394” pe factură** (din 19.0.1.6.0; valoarea implicită vine din jurnal sau din tipul mișcării, modificabilă cât timp factura e în ciornă): *Factură simplificată* se declară doar la cartușul I, pct. 1.1–1.4 (nu în C–F); *Bon fiscal* primit cu TVA dedus merge la pct. 1.5 (doar bonuri de cel mult 100 EUR cu TVA și CUI-ul firmei; peste această valoare exportul se oprește), iar bonurile emise rămân în G; *Borderou*, *Filă de carnet*, *Contract*, *Alt document* dau `tip_document` la achizițiile N. Jurnalele au câmpul „Tip facturi D394” și plajele de facturi alocate.
- **Autofacturi și stornări:** autofacturile dintr-un jurnal de achiziții cu „Tip facturi D394” = Autofacturare (ex. ajustarea TVA, art. 319 alin. (3)) intră în plaja proprie (2.1 / 2.2) și în `<facturi>` tip 3, cu baza și TVA pe cote (din 19.0.1.9.0); factura stornată se stabilește după valoarea totală negativă a documentului, nu doar după tipul „notă de credit” (pct. 2.2.1). Facturile stornate și cele anulate se raportează cu seria și numărul în plaja de facturi.
- **TVA dedus la furnizori cu TVA la încasare** (pct. 4.1, firmă în sistem normal de TVA, din 19.0.1.8.0): `tvaDedAI*` primește TVA plătit în perioadă furnizorilor cu TVA la încasare, pe cota facturii, proporțional cu suma plătită, din notele de exigibilitate.
- **Configurare per companie** (*Setări → Contabilitate → Declarații ANAF*): *D394 Period* (L/T/S/A, implicit Lunar → `tip_D394`), *D394 VAT on Collection* (`sistemTVA`), *D394 Option* (`optiune`, bifat implicit) și *D394 Affiliated Persons* (`prsAfiliat`, OPANAF 3281/2020; partenerii afiliați se marchează în fișa partenerului, tab-ul Sales & Purchases). `op_efectuate` se calculează automat. Pentru export trebuie completate CUI, adresa completă, codul CAEN și persoana de contact ANAF; lipsurile opresc exportul cu o eroare.
- **Taxare inversă — coduri NC:** produsele supuse taxării inverse au nevoie de *Cod NC* pe fișa produsului (cereale, deșeuri, masă lemnoasă, certificate, energie electrică, construcții, aur de investiții, telefoane, microprocesoare, console/tablete/laptopuri); la electronice taxarea inversă e obligatorie doar peste 22.500 lei fără TVA.
- **Reconciliere cu D300:** la generarea D300 (`l10n_ro_anaf_d300`), jurnalele TVA sunt reconciliate informativ cu declarația (avertismente în log, fără blocarea generării). D394 nu are checklist propriu în fluxul declarațiilor fiscale.
- **Reguli de depunere:** declarația se depune până la 30 inclusiv a lunii următoare; facturile primite cu întârziere se declară în perioada înregistrării în contabilitate (D394 nu se redepune); în prima declarație a anului se exprimă acordul de consultare a tranzacțiilor bilaterale în aplicația ANAF. Din august 2025 se folosesc cotele de 21% și 11%.
- **Versiune formular acceptată:** publicat la 15.09.2025, schemă `d394_20250917.xsd`; verificat cu DUKIntegrator (Soft J 8.0.2) la 12.09.2026, fără erori.
- Ghidul pas-cu-pas, cu capturi de ecran, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d394.report.mixin`: model abstract cu logica de construcție a datelor D394 (clasificare parteneri Cartuș C/D, CABA, taxare inversă, generare XDP/XML, filtre de export).
- `l10n_ro_account_vat_journal.sale.tax.report.handler` / `l10n_ro_account_vat_journal.purchase.tax.report.handler`: extind handler-ele jurnalelor de vânzări/cumpărări din `l10n_ro_account_vat_journal` cu mixin-ul D394.
- `account.journal` (extindere): câmpurile D394 de pe jurnal („Tip facturi D394”, „Tip document D394” implicit) și plajele de facturi alocate.
- `l10n_ro.d394.invoice.range`: plajă de facturi (serie, număr de la / până la) alocată unui jurnal, pentru cartușul I.
- `account.move` (extindere): câmpul „Tip document D394” (factură, factură simplificată, bon fiscal, borderou, filă de carnet, contract, alt document).
- `res.company` (extindere): opțiuni de declarație configurabile per companie (periodicitate TVA, TVA la încasare, opțiune contribuabil, persoane afiliate).
- `res.config.settings` (extindere): expune opțiunile D394 în ecranul de setări (Setări → Contabilitate → Declarații ANAF).

**Date / Vizualizări**

- `data/d394_report.xml`: definiția raportului D394.
- `data/d394_menu.xml`: intrările de meniu.
- `views/res_config_settings_views.xml`: opțiunile de configurare (periodicitate TVA, TVA la încasare, contribuabil, persoane afiliate).
- `views/account_journal_views.xml` / `views/account_move_views.xml`: câmpurile D394 de pe jurnal (tip facturi, tip document, plaje) și de pe factură (tip document).
- `static/src/warnings.xml`: componenta web (assets backend) pentru avertismentele de pe rapoarte.
- `views/d394_report_export.xml`: exportul XDP.
- `views/d394_report_xml_export.xml`: exportul XML.
- `demo/demo_data.xml`: date de test.

**Rapoarte**

- Jurnal TVA Vânzări (RO) și Jurnal TVA Cumpărări (RO): jurnalele de vânzări și cumpărări, accesibile din Contabilitate → Raportare → Taxe, cu butoanele de export **D394 file XML (Soft J)** și **D394 file XDP (Soft A)**; exportul XLSX de detaliu (coloane pe cotă ordonate descrescător) e pentru analiză și reconciliere internă.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din rapoarte.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructură comună (validare XSD, mixin companie/reprezentant, MIME fișiere XDP) reutilizată direct de acest modul.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): aduce codul CAEN pe partener, cerut la exportul companiei (`_validate_anaf_export_company(require_caen=True)`).
- [l10n_ro_account_vat_journal](../l10n_ro_account_vat_journal/index.md): furnizează handler-ele de bază ale jurnalelor de TVA extinse de acest modul cu logica D394.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): extinde declarația D394 cu datele din vânzările Punct de Vânzare (POS).
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): Decontul de TVA (D300), pentru care jurnalele TVA din acest modul servesc drept bază.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): altă declarație informativă ANAF din același ecosistem de raportare fiscală RO.
