# Romania - Stock Accounting Check (localizat la `l10n_ro_stock_account_check/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_account_check`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_stock_account_check
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_stock_account_check`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Verifică dacă valoarea stocului din mișcările de stoc corespunde cu soldul din contabilitate și ajută la corectarea diferențelor găsite. În localizarea românească cele două valori sunt generate de documente diferite (de exemplu, o recepție nu postează o notă de stoc, iar debitul contului 371 vine din factura furnizorului), așa că se pot îndepărta una de alta. Raportul listează produsele cu diferențe, împreună cu prețul de cost, ultimul preț de achiziție și cantitățile din ambele părți.

#### 2. Funcționalități Cheie

- Compară, pentru fiecare produs și cont de evaluare a stocului, **valoarea din mișcările de stoc finalizate** (`stock.move.value`, cu semnul dedus din tipul de mișcare românesc) cu **soldul contabil** din înregistrările contabile (`account.move.line`).
- Afișează prețul de cost, ultimul preț de achiziție, cantitățile și abaterile de preț pentru valoare și pentru contabilitate.
- Drill-down din rezultate către mișcările de stoc și către înregistrările contabile din spatele fiecărei cifre (inclusiv către achiziții și vânzări).
- Re-postarea notei contabile a unei mișcări sau a unui transfer (*Correction Valuation*, acțiune disponibilă în mod dezvoltator).
- Postarea unei note contabile de ajustare (*Fix AML*).
- Înregistrarea unei ajustări de inventar care poartă valoarea lipsă (*Fix Valuation*).
- Mutarea evaluării unui produs pe contul definit de categoria sa.
- Alinierea prețului de cost la ultimul preț de achiziție.
- Semnalează recepțiile fără factură de furnizor, livrările fără factură de client și notele contabile cu dată diferită de cea a mișcării de stoc.
- Acces din meniul Inventar > Raportare > *Stock accounting check* (grup Utilizator stoc), cu rezultate în listă, formular și pivot.

Notă: în 19.0 `stock.valuation.layer` nu mai există; verificarea este construită direct pe `stock.move` (semnul se reconstruiește din `l10n_ro_move_type`).

#### 3. Dependențe

- `l10n_ro_stock_account`
- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `stock.accounting.check` (tranzitoriu): wizardul de generare a verificării, afișat în dialog din meniu.
- `stock.accounting.check.line` (tranzitoriu): linia de rezultat per produs/cont, cu valorile și abaterile, precum și acțiunile de detaliu și de corecție.
- `stock.move` (extins): `correction_valuation()` pentru re-postarea notei contabile a mișcării.
- `stock.picking` (extins): `correction_valuation()` aplicat mișcărilor transferului.

**Vizualizări**

- `view_stock_accounting_check_form`: formularul wizardului de verificare.
- `view_stock_accounting_check_line_tree` / `_form` / `_pivot` / `_search`: rezultatele verificării.

**Acțiuni Automate / Acțiuni Server**

- `action_stock_move_correction_valuation` și `action_stock_picking_correction_valuation`: acțiuni server *Correction Valuation* pe mișcări și transferuri (grup mod dezvoltator).
- Nu există acțiuni cron.

#### 5. Conexiuni

- `l10n_ro_stock_account`: sursa tipurilor de mișcare (`l10n_ro_move_type`) și a notelor contabile de stoc pe care le verifică raportul.
