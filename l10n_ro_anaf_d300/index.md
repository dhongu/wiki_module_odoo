# Romania - Decont de TVA (D300) (localizat la `l10n_ro_anaf_d300/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d300`
- **Versiune:** `19.0.0.0.18`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d300
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d300`
- **Ultima Ingestie:** 2026-10-05
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul destinat departamentelor financiar-contabile din România care au obligația depunerii Decontului de TVA (Declarația 300) la ANAF. Permite generarea și exportul D300 direct din Odoo, în două formate acceptate oficial, fără re-introducerea manuală a datelor.

#### 2. Funcționalități Cheie

- **Export XDP (Soft A)**: generează un fișier Adobe XDP care poate fi importat instantaneu în formularul PDF inteligent oficial ANAF (D300 v12).
- **Export XML (Soft J)**: generează fișierul XML conform structurii oficiale ANAF v12.0.0+, gata pentru validare și semnare digitală în DUKIntegrator.
- **Validare XSD automată**: fișierul XML este validat față de schema XSD oficială înainte de export; erorile de structură sunt raportate înainte de descărcare.
- **Mapare rânduri de decont**: corelează automat codurile liniilor din raportul de taxe Odoo cu câmpurile corespunzătoare din declarația D300 (rânduri R1–R44).
- **Date de identificare completate automat**: CUI, denumire companie, reprezentant legal, județ (prin mapare ANAF din `l10n_ro_anaf_base`).
- **Calcul sold reportat TVA**: preia automat soldul conturilor 4423 (TVA de plată) și 4424 (TVA de recuperat) din perioada precedentă pentru rândurile R35/R38.
- **Suport TVA la încasare (CABA)**: calculează baza și TVA neexigibil din facturile neîncasate la sfârșitul perioadei.
- **Integrare account.return**: buton „Generează D300" disponibil în fluxul de închidere lunară/trimestrială, cu pre-filtrare automată pe perioada return-ului.
- **Tip decont automat**: detectează tipul perioadei (lunar L, trimestrial T, semestrial S, anual A) și generează numărul de evidență al plății conform algoritmului ANAF.

- **Taxe și grile D300 corectate pe planul RO**: „0% EU S” are grilele rândurilor 3 și 3.1; serviciile de la prestatori din afara UE se autolichidează cu taxele „21% EX S” / „11% EX S” (rd. 7 și 22); factura furnizorului extern la import („0% EX G”) nu mai are grile, importul fiind declarat o singură dată din DVI. Planurile existente se corectează la instalare/actualizare.
- **Import cu TVA amânată la plată în vamă**: taxele „21% IMP AM” / „11% IMP AM” evidențiază TVA din DVI simultan colectat și deductibil (art. 326 alin. (5)), pe rd. 7 și 22, în decontul perioadei datei DVI; se aleg pe DVI (ex. în asistentul din `l10n_ro_customs_dvi`).
- **TVA nededusă conform instrucțiunilor D300 (OPANAF 174/2026)**: rândurile de achiziții și rd. 30 conțin TVA-ul deductibil brut (inclusiv partea nededusă), iar rd. 31 doar taxa efectiv dedusă. Se recunosc taxele cu repartiție parțială (ex. „21% ND 50%”) și „Deductibilitate” pe linie.
- **Rotunjire corectă a TVA nededusă**: rândul brut se rotunjește o singură dată pe suma întreagă (nu separat pe partea dedusă și cea nededusă), iar partea nededusă este diferența; evită abaterile de 1 leu la fracțiuni de 0,50.
- **Fără linii tehnice la „Deductibilitate”**: pentru companiile RO, `l10n_ro_vat_deductibility` nu mai creează liniile `non_deductible_product`, baza rămâne întreagă pe grilă, iar TVA-ul nededus se împarte pe rânduri după liniile de produs cu deductibilitate sub 100% (documentele vechi se citesc ca înainte).
- **Totaluri calculate din rânduri**: rd. 30 se calculează mereu ca sumă a rd. 20–28 (validatorul ANAF), fără rd. 29; rd. 3.1 are semn negativ ca rd. 3; reconcilierea cu jurnalele de TVA compară rd. 30 cu TVA dedusă + nededusă.
- **Setări la nivel de companie** (Contabilitate → Configurare → Setări, secțiunea Declarații ANAF): „depus de reprezentant”, bifa operațiuni interne și temeiul legal (0 – standard; 2 – art. 324 alin. (14) Cod fiscal).
- **Acces**: Contabilitate → Declarații ANAF → Declarație 300 (acțiunile „D300 file XDP” / „D300 file XML (Soft J)”) sau din verificarea „Generează D300 (TVA)" a fluxului `account.return`; fișierul semnat se atașează la „Atașează D300 (XML semnat)". Modulul nu transmite nimic către ANAF; necesită Odoo Enterprise (`account_reports`).
- **Fișa consultant**: fluxul pas-cu-pas de utilizare este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`
- `account_reports`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extins): completează CAEN-ul demo al companiei (`l10n_ro_caen_code`) și corectează grilele D300 / creează taxele suplimentare (EX S, IMP AM) pe planul de conturi RO (`account_chart_template_grids.py`).
- `account.report` / `tax_report_handler` (extins): logica de mapare a rândurilor raportului de taxe RO pe structura D300 și generarea fișierelor XDP/XML, inclusiv validarea companiei (`_validate_anaf_export_company`, cu `require_caen=True`).
- `res.company` (extins): câmpuri și configurări necesare identificării companiei/reprezentantului legal în decont.
- `res.config.settings` (extins): opțiuni de configurare aferente D300 în setările de contabilitate.
- `check.action.review` (extins): verificările de corelație D300 integrate în fluxul `account.return`.

**Vizualizări**

- `data/d300_grid_report.xml`: definirea grilei/structurii raportului D300.
- `data/l10n_ro_tax_report_fix.xml`: corecții ale raportului de taxe RO (inclusiv semnul rd. 3.1).
- `data/d300_menu.xml`: intrările de meniu pentru D300.
- `data/return_checks.xml`: verificările de corelație asociate decontului, afișate în fluxul de închidere (`account.return`).
- `views/tax_report_xdp_export.xml`: butonul și template-ul de export XDP (Soft A).
- `views/tax_report_xml_export.xml`: butonul și template-ul de export XML (Soft J).
- `views/res_config_settings_views.xml`: opțiunile de configurare în setări.
- `demo/demo_data.xml`: date de test pentru demonstrații.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raportul de taxe sau din verificările fluxului de închidere (`account.return`).*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează mapările comune ANAF (ex: coduri de județ) folosite la completarea automată a datelor de identificare.
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): aduce codul CAEN pe partener, cerut obligatoriu la export (`require_caen=True`).
- [l10n_ro_customs_dvi](../l10n_ro_customs_dvi/index.md): DVI-ul pe care se alege taxa de import cu TVA amânată la plată.
- [l10n_ro_vat_deductibility](../l10n_ro_vat_deductibility/index.md): „Deductibilitate” pe linie, a cărei TVA nededusă este repartizată pe rândurile D300.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): altă declarație ANAF din aceeași suită de raportare fiscală RO.
