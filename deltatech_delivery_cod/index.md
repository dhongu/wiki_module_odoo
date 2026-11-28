# Courier COD Settlement Bridge (localizat la `deltatech_delivery_cod/index.md`)

- **Nume Tehnic:** `deltatech_delivery_cod`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_delivery_cod
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_delivery_cod`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă decontările de ramburs (cash on delivery) primite de la curieri sub formă de extrase de cont bancar, astfel încât banii încasați în numele companiei de curier să fie reconciliați prin mecanismul standard de reconciliere al Odoo, nu printr-un proces paralel. Două surse converg spre același tratament: curierii care publică un fișier de borderou și curierii care expun un endpoint de decontare, interogat pe un interval de date. Protecția la duplicate, verificarea totalului de control și linia de echilibrare a transferului sunt scrise o singură dată, nu per curier. Extrasul aterizează într-un jurnal de tip „clearing", nu direct în contul bancar: banii rămân la curier până sosește transferul, iar linia de transfer este cea care se potrivește cu mișcarea reală din bancă.

#### 2. Funcționalități Cheie

- Import unificat al decontărilor de ramburs, indiferent dacă sursa este un fișier borderou sau un API de decontare.
- Potrivirea viramentului curierului (**Match Courier Transfer**): când curierul trimite doar banii, fără borderou, modulul găsește coletele plătite de suma transferată — tot lotul livrat într-o zi sau o combinație exactă la bănuț — și le transformă în același extras de decontare; când două grupuri dau aceeași sumă, alege utilizatorul.
- Protecție la import duplicat, pe baza unei chei unice per AWB și jurnal (`unique_import_id`).
- Verificarea totalului de control transmis de curier față de suma rândurilor, cu blocarea importului dacă nu se potrivesc.
- Separarea rândurilor pe zile de decontare (payout), fiecare generând propriul extras.
- Linie automată de comision (pentru curierii care decontează net) și linie automată de transfer (opțională, per jurnal) care echilibrează extrasul la zero.
- Identificarea partenerului pe baza AWB-ului legat de expediția proprie (`stock.picking`), nu după numele destinatarului transmis de curier.
- Parsare strictă a sumelor și datelor (formate RO/EN), cu respingerea valorilor ambigue în loc de rotunjire silențioasă.
- Wizard „Fetch Courier Settlement" pentru extragerea manuală a decontărilor pe un interval de date, din jurnalul unui curier.
- Punct de extensie: o singură metodă `<delivery_type>_cod_fetch_rows(date_from, date_to)` pe `delivery.carrier` activează fluxul API pentru un curier nou.

Fluxul detaliat, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_delivery](../deltatech_delivery/index.md)
- `account_bank_statement_import`

#### 4. Componente Cheie

**Modele**

- `account.journal` (extindere): câmpurile `carrier_id` și `cod_add_transfer_line`; logica de transformare a rândurilor de decontare în extrase (`_cod_import_rows`, `_cod_prepare_statement`, `_cod_drop_already_imported`, `_cod_assert_control_total`, `_cod_find_partner` etc.).
- `delivery.carrier` (extindere): `cod_fetch_rows(date_from, date_to)` și `cod_has_feed()`, punctul de extensie pentru endpointul de decontare al curierului.
- `delivery.cod.import` (`TransientModel`): wizard cu jurnal, curier și interval de date.
- `delivery.cod.match` și `delivery.cod.match.line` (`TransientModel`): wizard-ul „Match Courier Transfer" și liniile sale (coletele propuse).
- `cod_rows.py` (modul Python pur, fără model Odoo): validarea și normalizarea rândurilor (`normalize_rows`, `parse_amount`, `parse_date`), partajat de fluxurile fișier și API.

**Vizualizări**

- `view_account_journal_form_cod`: secțiunea „Courier COD Settlement" pe formularul jurnalului.
- `view_delivery_cod_import_form`: formularul wizardului de extragere a decontării.
- `view_delivery_cod_match_form`: formularul wizardului de potrivire a viramentului.

**Acțiuni Automate / Acțiuni Server**

- `action_delivery_cod_import`: acțiune fereastră pentru wizardul „Fetch Courier Settlement".
- `action_delivery_cod_match` și `action_server_cod_match_from_line`: deschid „Match Courier Transfer", inclusiv direct dintr-o linie de extras bancar.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): furnizează modelul `delivery.carrier` extins de acest modul.
- `account_bank_statement_import`: infrastructura de import de extrase (unicitate `unique_import_id`, `_create_bank_statements`) pe care se sprijină acest bridge.
