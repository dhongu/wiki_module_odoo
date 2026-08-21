# Courier COD Settlement Bridge (localizat la `deltatech_delivery_cod/index.md`)

- **Nume Tehnic:** `deltatech_delivery_cod`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_delivery_cod
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_cod`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul importă decontările de ramburs (cash on delivery) primite de la curieri sub formă de extrase de cont bancar, astfel încât banii încasați în numele companiei de către curier să fie reconciliați prin mecanismul standard de reconciliere al Odoo, nu printr-un proces paralel. Două tipuri de surse converg spre același tratament: curierii care publică un fișier de borderou (parsat local) și curierii care expun un endpoint de decontare (interogat pe un interval de date). Odată ajunse în acest punct comun, protecția la duplicate, verificarea totalului de control și linia de echilibrare a transferului bancar sunt scrise o singură dată, nu separat pentru fiecare curier. Extrasul aterizează într-un jurnal de tip „clearing", nu direct în contul bancar real: banii rămân la curier până la sosirea transferului, iar linia de transfer este cea care se potrivește cu mișcarea reală din bancă.

#### 2. Funcționalități Cheie

- Import unificat al decontărilor de ramburs, indiferent dacă sursa este un fișier borderou sau un API de decontare al curierului.
- Protecție la import duplicat, pe baza unei chei unice per AWB și jurnal (`unique_import_id`), astfel încât reimportul unor intervale suprapuse nu dublează sumele.
- Verificarea totalului de control transmis de curier față de suma efectivă a rândurilor, cu blocarea importului dacă nu se potrivesc.
- Separarea automată a rândurilor pe zile de decontare (payout), fiecare payout generând propriul extras, pentru a se putea potrivi individual cu mișcarea din bancă.
- Linie automată de comision (pentru curierii care decontează net) și linie automată de transfer bancar (opțională, configurabilă per jurnal) care echilibrează extrasul la zero.
- Identificarea automată a partenerului pe fiecare linie, pe baza AWB-ului legat de expedierea (`stock.picking`) proprie, nu după numele destinatarului transmis de curier.
- Parsare robustă și strictă a sumelor și datelor din surse eterogene (formate numerice RO/EN, separatori de mii diferiți), cu respingerea explicită a valorilor ambigue în loc de rotunjire silențioasă.
- Wizard „Fetch Courier Settlement" pentru extragerea manuală a decontărilor pe un interval de date, direct dintr-un jurnal bancar/casă configurat cu un curier.
- Punct de extensie simplu pentru curieri: implementarea unei singure metode `<delivery_type>_cod_fetch_rows(date_from, date_to)` pe `delivery.carrier` este suficientă pentru a activa fluxul de decontare API.

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `account_bank_statement_import`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extindere): adaugă câmpurile `carrier_id` (curierul asociat jurnalului) și `cod_add_transfer_line`; conține toată logica de transformare a rândurilor de decontare în extrase de cont (`_cod_import_rows`, `_cod_prepare_statement`, `_cod_statement_vals`, `_cod_drop_already_imported`, `_cod_assert_control_total`, `_cod_find_partner` etc.).
- `delivery.carrier` (extindere): adaugă `cod_fetch_rows(date_from, date_to)` și `cod_has_feed()`, punctul de extensie prin care fiecare curier își expune (opțional) propriul endpoint de decontare.
- `delivery.cod.import` (`TransientModel`): wizard care cere jurnal, curier și interval de date, apelează `cod_fetch_rows` pe curier și declanșează crearea extraselor prin `account.journal._cod_import_rows`.
- Modulul include și un modul Python pur (`cod_rows.py`, fără model Odoo) cu validarea și normalizarea rândurilor brute de decontare (`normalize_rows`, `parse_amount`, `parse_date`), partajat de ambele fluxuri (fișier și API).

**Vizualizări**

- `view_account_journal_form_cod`: extinde formularul jurnalului contabil (`account.view_account_journal_form`) cu secțiunea „Courier COD Settlement" (curier, opțiunea de linie de transfer, buton de extragere a decontării).
- `view_delivery_cod_import_form`: formularul wizardului de extragere a decontării (jurnal, curier, interval de date).

**Acțiuni Automate / Acțiuni Server**

- `action_delivery_cod_import`: acțiune fereastră care deschide wizardul „Fetch Courier Settlement", apelabilă din formularul jurnalului bancar/casă.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): furnizează modelul `delivery.carrier` extins de acest modul.
- `account_bank_statement_import`: oferă infrastructura de import de extrase bancare (unicitate `unique_import_id`, `_create_bank_statements`) pe care se sprijină acest bridge.
