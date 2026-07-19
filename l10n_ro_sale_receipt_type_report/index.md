# Vânzări pe Tipuri de Încasări (RO) - Raport (localizat la `l10n_ro_sale_receipt_type_report/index.md`)

- **Nume Tehnic:** `l10n_ro_sale_receipt_type_report`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_sale_receipt_type_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sale_receipt_type_report`
- **Ultima Ingestie:** `2026-07-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce situația periodică „Vânzări pe tipuri de încasări" ca raport nativ Odoo (`account.report`), cerută explicit de contabilitatea unui client (Damira) pentru reconcilierea lunară a încasărilor pe canal. Spre deosebire de Registrul de casă sau Jurnalul de bancă (care citesc doar mișcările unui singur cont), acest raport unifică două surse de date eterogene — încasările de la casa de marcat (`pos.payment`) și încasările contabile din afara POS-ului (`account.payment`) — într-o singură vedere pe patru canale: numerar, card, transfer bancar (OP) și platformă de plată online. Nu există un formular tipizat legal pentru acest raport; este o situație de gestiune internă.

#### 2. Funcționalități Cheie

- Patru secțiuni pliabile, fiecare cu totalul perioadei în antet: Casă — Numerar, Casă — Card, Transfer bancar (OP), Platformă de plată online; secțiunile fără date în perioadă nu apar.
- Fiecare secțiune desfășurată listează încasările individuale (dată, partener, document, sumă), cu drill-down la comanda POS (`pos.payment` → `pos_order_id`) sau la plata contabilă (`account.payment`).
- Rând de Total general la finalul raportului.
- Clasificare Casă — Numerar / Card după tipul jurnalului metodei de plată POS (`pos.payment.method`), nu după numele ei — câmpul `type` al metodei de plată e calculat, nestocat, deci interogarea SQL se leagă direct la `account_journal.type`.
- Clasificare OP / Platformă online după prezența unei `payment_transaction_id` pe `account.payment`.
- Excluderi deliberate: metodele „Cont client" (pay later) la POS (nu sunt o încasare reală), comenzile POS nefinalizate, plățile de decontare a sesiunii POS (`account.payment.pos_session_id`, ar duplica încasarea deja numărată din `pos.payment`), plățile contabile de tip ieșire.
- O încasare cash înregistrată direct în contabilitate (nu prin POS) e inclusă tot la secțiunea Casă — Numerar.
- Beneficiază integral de framework-ul `account_reports`: filtru de interval de dată, selector multi-companie, export PDF/XLSX din bara de instrumente.
- Limitare cunoscută (v1): o încasare cu cardul înregistrată manual în contabilitate (fără POS, fără provider de plată online) nu poate fi distinsă de un transfer bancar obișnuit — ambele ajung la secțiunea OP.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- `point_of_sale`
- `payment`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_sale_receipt_type_report.handler` (`AbstractModel`, moștenește `account.report.custom.handler`): construiește liniile dinamice ale raportului. Interoghează separat `pos.payment` (JOIN pe `pos_payment_method` + `account_journal`, filtrat pe stare comandă Paid/Posted/Invoiced) și `account.payment` (inbound, postat, cu `pos_session_id IS NULL`), unifică rândurile într-un dicționar pe categorie, generează secțiunile ierarhice (categorie → linii → total general) și expune `_caret_options_initializer` pentru drill-down pe `pos.payment` (către `pos_order_id`).

**Vizualizări**

Nu există vizualizări (`views/`) proprii; interfața este generată integral de framework-ul `account_reports` pe baza definiției raportului.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Modulul definește în schimb configurația raportului prin date (`data/l10n_ro_sale_receipt_type_report.xml`):

- `l10n_ro_sale_receipt_type_report` (`account.report`): definește raportul „Sales by Receipt Type (RO)", cu filtru de interval de dată, selector multi-companie și coloanele Date/Partner/Document/Amount.
- `action_l10n_ro_sale_receipt_type_report` (`ir.actions.client`, tag `account_report`): acțiunea client care deschide raportul.
- `menu_l10n_ro_sale_receipt_type_report`: meniul „Sales by Receipt Type (RO)", sub „Legal Statements" din meniul Contabilitate.

#### 5. Conexiuni

- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md): citește doar mișcările contului de casă, pe zile (registru legal); acest raport reconciliază pe canal de încasare, indiferent de sursă — complementar, nu duplică.
- `l10n_ro_bank_register_report`: aceeași relație — jurnalul de bancă citește un singur cont, pe zile; nu are încă pagină wiki proprie.
- `account_reports`: framework-ul Enterprise de raportare contabilă folosit ca bază tehnică (filtre, coloane, export PDF/XLSX).
- `point_of_sale`: sursa `pos.payment`/`pos.order`/`pos.payment.method` pentru secțiunile Casă — Numerar/Card.
- `payment`: câmpul `account.payment.payment_transaction_id`, folosit pentru a distinge Platformă online de OP.
