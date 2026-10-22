# Courier COD Settlement Bridge (localizat la `deltatech_delivery_cod/index.md`)

- **Nume Tehnic:** `deltatech_delivery_cod`
- **Versiune:** `19.0.1.2.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_delivery_cod
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_cod`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă decontările de ramburs (cash on delivery) primite de la curieri sub formă de extrase de cont bancar, astfel încât banii încasați în numele companiei de către curier să fie reconciliați prin mecanismul standard de reconciliere al Odoo, nu printr-un proces paralel. Sursele converg spre același tratament: curierii care publică un fișier de borderou (parsat local), curierii care expun un endpoint de decontare (interogat pe un interval de date) și curierii care virează doar banii, fără borderou (coletele plătite sunt găsite din suma virată). Odată ajunse în acest punct comun, protecția la duplicate, verificarea totalului de control și linia de echilibrare a transferului bancar sunt scrise o singură dată, nu separat pentru fiecare curier. Extrasul aterizează într-un jurnal de tip „clearing", nu direct în contul bancar real: banii rămân la curier până la sosirea transferului, iar linia de transfer este cea care se potrivește cu mișcarea reală din bancă.

#### 2. Funcționalități Cheie

- Import unificat al decontărilor de ramburs, indiferent dacă sursa este un fișier borderou, un API de decontare al curierului sau potrivirea unui virament fără borderou.
- **Potrivește viramentul curierului** (nou în 19.0.1.1.0): pentru curierii care trimit doar banii, fără borderou, wizardul caută coletele cu ramburs livrate și nedecontate într-o fereastră de căutare (implicit 20 de zile înainte de virament) și găsește ce plătește suma virată. Ordinea ipotezelor: mai întâi tot lotul livrat până într-o zi (curieri care virează pe ciclu, evidență de la 8 colete în sus), apoi o combinație exactă la cent. Când două grupuri diferite dau aceeași sumă, nu alege automat, ci lasă alegerea utilizatorului; **Selectează livrate până la** bifează dintr-o dată un ciclu întreg. Coletele bifate devin același extras de decontare pe care l-ar produce un borderou (un rând per AWB și rândul de transfer), iar potrivirea cu facturile rămâne în seama reconcilierii standard Odoo.
- Wizardul de potrivire se pornește din linia grupată din extrasul băncii (Acțiune > Match Courier Transfer) sau din jurnalul de clearing (buton „Match Transfer Without Borderou").
- Protecție la import duplicat, pe baza unei chei unice per AWB și jurnal (`unique_import_id`), astfel încât reimportul unor intervale suprapuse nu dublează sumele.
- Verificarea totalului de control transmis de curier față de suma efectivă a rândurilor, cu blocarea importului dacă nu se potrivesc.
- Separarea automată a rândurilor pe zile de decontare (payout), fiecare payout generând propriul extras, pentru a se putea potrivi individual cu mișcarea din bancă.
- Linie automată de comision (pentru curierii care decontează net) și linie automată de transfer bancar (opțională, configurabilă per jurnal) care echilibrează extrasul la zero.
- Identificarea automată a partenerului pe fiecare linie, pe baza AWB-ului legat de expedierea (`stock.picking`) proprie, nu după numele destinatarului transmis de curier. Expedierea se caută doar în compania jurnalului (și sucursalele ei) și printre expedierile aceluiași curier; expedierile fără curier rămân acceptate (feed-ul GLS leagă doar după AWB).
- Extrasele create din API-ul curierului au acum liniile în jurnalul de clearing, nu în jurnalul bancar implicit al companiei.
- Parsare robustă și strictă a sumelor și datelor din surse eterogene (formate numerice RO/EN, separatori de mii diferiți), cu respingerea explicită a valorilor ambigue în loc de rotunjire silențioasă.
- Wizard „Fetch Courier Settlement" pentru extragerea manuală a decontărilor pe un interval de date, direct dintr-un jurnal bancar/casă configurat cu un curier.
- Punct de extensie simplu pentru curieri: implementarea unei singure metode `<delivery_type>_cod_fetch_rows(date_from, date_to)` pe `delivery.carrier` este suficientă pentru a activa fluxul de decontare API.
- **Rambursul de decontat** (nou în 19.0.1.2.0): fiecare rând AWB din extrasul de decontare este legat de expedierea sa (din borderou, din API sau din „Match Courier Transfer"); expedierea arată linia de extras și suma plătită de curier. La upgrade, extrasele deja importate sunt legate retroactiv. Lista **COD to Settle** (*Contabilitate → Clienți*) arată coletele cu ramburs livrate pe care curierul nu le-a decontat după perioada `delivery_cod.settlement_days` (10 zile implicit), grupate pe curier, doar pentru curierii care au jurnal de decontare; filtrul „Settled with Difference" listează coletele plătite cu altă sumă decât rambursul.
- **Alertă zilnică opțională** (inactivă implicit): un cron plasează câte o activitate „COD Settlement" pe fiecare jurnal de clearing cu colete încă datorate (număr, sumă, cea mai veche zi de livrare), în limba contabilului căruia îi este atribuită; se trimite către utilizatorul implicit al tipului de activitate, fără el nu se programează nimic.
- Configurare: jurnalul de clearing se creează pe un analitic dedicat 5125 (sume în curs de decontare), cu **Curier** setat în Configurări Avansate; fără curier, butoanele de decontare nu apar. Fluxul pas cu pas, conturile și exemplul numeric sunt în fișa consultantului.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `account_bank_statement_import`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extindere): adaugă câmpurile `carrier_id` (curierul asociat jurnalului) și `cod_add_transfer_line`; conține toată logica de transformare a rândurilor de decontare în extrase de cont (`_cod_import_rows`, `_cod_prepare_statement`, `_cod_statement_vals`, `_cod_drop_already_imported`, `_cod_assert_control_total`, `_cod_find_partner` etc.).
- `delivery.awb` (extindere): adaugă legătura către linia de extras care a plătit coletul (`cod_statement_line_id`), suma decontată, indicatorii „decontat cu diferență" și „decontare întârziată", plus metoda cronului de alertă `_cron_cod_settlement_alerts`.
- `account.bank.statement.line` (extindere): leagă liniile de decontare de AWB-urile corespunzătoare.
- `delivery.carrier` (extindere): adaugă `cod_fetch_rows(date_from, date_to)` și `cod_has_feed()`, punctul de extensie prin care fiecare curier își expune (opțional) propriul endpoint de decontare.
- `delivery.cod.import` (`TransientModel`): wizard care cere jurnal, curier și interval de date, apelează `cod_fetch_rows` pe curier și declanșează crearea extraselor prin `account.journal._cod_import_rows`.
- `delivery.cod.match` (`TransientModel`, nou): wizardul „Match Courier Transfer Without Borderou"; are jurnal de clearing, linia de extras bancar, suma și data virată, fereastra de căutare, starea (`search`, `lot`, `proposed`, `ambiguous`, `manual`) și totalurile selecției; creează extrasul de decontare din coletele bifate.
- `delivery.cod.match.line` (`TransientModel`, nou): un colet (`delivery.awb`) candidat, cu bifa „Paid", clientul, livrarea și data livrării.
- Module Python pure, fără model Odoo: `models/cod_rows.py` (validarea și normalizarea rândurilor brute: `normalize_rows`, `parse_amount`, `parse_date`), partajat de fluxurile fișier și API, și `models/cod_match.py` (nou; `prefix_lot`, `subset_sum`, `exact_combinations` pe cenți, cu limite `LOT_MIN_ITEMS`=8, `MAX_CANDIDATES`=80).

**Vizualizări**

- `view_account_journal_form_cod`: extinde formularul jurnalului contabil (`account.view_account_journal_form`) cu secțiunea „Courier COD Settlement" (curier, opțiunea de linie de transfer, butoanele „Fetch Settlement" și „Match Transfer Without Borderou" pe un rând propriu).
- `view_delivery_awb_cod_list` / `view_delivery_awb_cod_search` (nou): lista și căutarea „COD to Settle" pe `delivery.awb`, cu filtre pentru întârziate și decontate cu diferență, grupare pe curier; meniu `menu_delivery_awb_cod` sub *Contabilitate → Clienți*.
- `view_delivery_cod_import_form`: formularul wizardului de extragere a decontării (jurnal, curier, interval de date).
- `view_delivery_cod_match_form` (nou): formularul wizardului de potrivire a viramentului, cu lista coletelor candidate și „Select Delivered Up To".

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_cod_settlement_alerts`: „Delivery: Alert for COD not settled by the courier", rulează zilnic ca OdooBot, **inactiv implicit**; creează/actualizează activitatea `mail_activity_type_cod_settlement` pe jurnalele de clearing și o marchează ca făcută când nu mai e nimic datorat.
- `action_delivery_awb_cod`: acțiune fereastră „COD to Settle".
- `action_delivery_cod_import`: acțiune fereastră care deschide wizardul „Fetch Courier Settlement", apelabilă din formularul jurnalului bancar/casă.
- `action_delivery_cod_match`: acțiune fereastră care deschide wizardul „Match Courier Transfer" din formularul jurnalului (nou).
- `action_server_cod_match_from_line`: acțiune server legată de `account.bank.statement.line` (liste și formulare), meniul Acțiune, care pornește wizardul pe linia grupată de virament (nou).

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): furnizează modelul `delivery.carrier` extins de acest modul și `delivery.awb` folosit la potrivirea viramentelor.
- `account_bank_statement_import`: oferă infrastructura de import de extrase bancare (unicitate `unique_import_id`, `_create_bank_statements`) pe care se sprijină acest bridge.
