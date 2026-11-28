# Romania - Vânzări pe tipuri de încasări (localizat la `l10n_ro_sale_receipt_type_report/index.md`)

- **Nume Tehnic:** `l10n_ro_sale_receipt_type_report`
- **Versiune:** `20.0.1.0.5`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_sale_receipt_type_report](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_sale_receipt_type_report)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sale_receipt_type_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul aduce situația periodică „Vânzări pe tipuri de încasări" ca raport nativ Odoo (`account.report`), pentru reconcilierea lunară a încasărilor pe canal. Spre deosebire de Registrul de casă sau Jurnalul de bancă, care citesc un singur cont, raportul unifică încasările de la casa de marcat (`pos.payment`) cu încasările contabile din afara POS-ului (`account.payment`) într-o singură vedere pe patru canale: numerar, card, transfer bancar (OP) și platformă de plată online. Nu este un formular legal, ci o situație de gestiune internă.

#### 2. Funcționalități Cheie

- Patru secțiuni pliabile, fiecare cu totalul perioadei în antet: Casă — Numerar, Casă — Card, Transfer bancar (OP), Platformă online; secțiunile fără date în perioadă nu apar. Rând de total general la final.
- Meniu: **Contabilitate → Raportare → Rapoarte de extras → Vânzări pe tipuri de încasări (RO)**; se deschide pe luna curentă.
- Fiecare secțiune desfășurată listează încasările individuale (dată, partener, document, factură, sumă), cu drill-down la comanda POS sau la plata contabilă. Coloana „Invoice" arată numărul real al facturii, distinct de memo-ul plății.
- Clasificarea Casă — Numerar / Card pentru POS se face după tipul jurnalului metodei de plată, nu după numele ei; metodele POS trebuie deci să aibă jurnal configurat.
- Pentru plățile contabile din afara POS: tranzacție de plată online asociată → Platformă online; jurnal de tip numerar → Casă — Numerar; altfel → OP.
- Excluderi deliberate: metodele „Cont client" (pay later), comenzile POS nefinalizate, plățile de decontare a sesiunii POS (ar dubla încasarea) și plățile de tip ieșire.
- Beneficiază de framework-ul `account_reports`: filtru de dată, selector multi-companie, export PDF/XLSX.
- Limitare cunoscută: o încasare cu cardul înregistrată manual în contabilitate (fără POS și fără provider online) ajunge la OP.
- `account_payment` este declarat explicit în dependențe: câmpul `account.payment.payment_transaction_id` trăiește în acest modul-punte, nu în `payment`.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- `point_of_sale`
- `payment`
- `account_payment`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_sale_receipt_type_report.handler` (`AbstractModel`, moștenește `account.report.custom.handler`): construiește liniile dinamice ale raportului din `pos.payment` și `account.payment` (inbound, postat, fără sesiune POS), grupate pe categorie, și expune `_caret_options_initializer` pentru drill-down.

**Vizualizări**

*Nu există vizualizări proprii; interfața este generată de framework-ul `account_reports`.*

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`. Datele definesc raportul (`data/l10n_ro_sale_receipt_type_report.xml`):

- `l10n_ro_sale_receipt_type_report` (`account.report`): raportul, cu filtru de dată, selector multi-companie și coloanele Date/Partner/Document/Invoice/Amount.
- `action_l10n_ro_sale_receipt_type_report` (`ir.actions.client`): acțiunea care deschide raportul.
- `menu_l10n_ro_sale_receipt_type_report`: meniul raportului în Contabilitate.

#### 5. Conexiuni

- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md): registrul de casă pe zile; acest raport reconciliază pe canal de încasare — complementar.
- [l10n_ro_bank_register_report](../l10n_ro_bank_register_report/index.md): jurnalul de bancă pe zile, un singur cont — complementar.
- `account_reports`: framework-ul Enterprise de raportare folosit ca bază tehnică.
- `point_of_sale`: sursa `pos.payment` / `pos.order` / `pos.payment.method`.
