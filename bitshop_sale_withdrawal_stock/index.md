# Bitshop Sale Withdrawal - Stock (localizat la `bitshop_sale_withdrawal_stock/index.md`)

- **Nume Tehnic:** `bitshop_sale_withdrawal_stock`
- **Versiune:** `19.0.0.1.0`
- **Cale:** [https://github.com/terrabit-solutions/bitshop/tree/19.0/bitshop_sale_withdrawal_stock](https://github.com/terrabit-solutions/bitshop/tree/19.0/bitshop_sale_withdrawal_stock)
- **Cale Locală:** `odoo-addons/bitshop/bitshop_sale_withdrawal_stock`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Acest modul asigură continuarea operațională a retragerii dintr-un contract (renunțare de tip consumator) pe partea de stoc: atunci când un client renunță la un contract, marfa trebuie fie oprită din livrare, fie returnată. Modulul adaugă modul de execuție `stock_return` pentru `bitshop_sale_withdrawal`, disponibil în **Vânzări → Configurare → Setări → Retragere din Contract → Execuție Retragere**.

#### 2. Funcționalități Cheie

- Anulează ce nu a fost încă expediat; cantitățile retrase parțial micșorează mutarea de stoc în loc să o anuleze integral
- Ce a fost deja livrat este returnat prin wizard-ul standard de retur din Odoo, astfel încât mutările de retur rămân legate de livrările pe care le anulează
- Perioada de retragere a mărfurilor se calculează după **ultimul** colet livrat pentru linie, nu după primul
- Cantitățile care nu pot fi asociate unei mutări de stoc sunt raportate pe retragere și generează o activitate, nefiind niciodată ignorate în tăcere

#### 3. Dependențe

- [bitshop_sale_withdrawal](../bitshop_sale_withdrawal/index.md)
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `bitshop.sale.withdrawal` (extins): adaugă câmpurile `return_picking_ids` (transferuri de retur), `cancelled_move_ids` (mutări anulate) și metoda `_execute_withdrawal_stock_return()`, care implementează modul de execuție `stock_return` — anulează mutările nelivrate/micșorează cantitatea pentru retrageri parțiale, iar pentru mutările deja finalizate creează retururi prin wizard-ul standard `stock.return.picking`, ca traseul de trasabilitate/valorizare să rămână intact.
- `sale.order.line` (extins): suprascrie `_bitshop_withdrawal_period_start()` pentru produsele fizice, calculând începutul perioadei de retragere pe baza datei ultimei mutări de stoc finalizate (nu a primei), și doar după ce toate mutările liniei sunt în starea `done`.
- `res.company` (extins): adaugă opțiunea `stock_return` la selecția `bitshop_withdrawal_execution_mode`.

**Vizualizări**

- `view_bitshop_sale_withdrawal_form_stock`: extinde formularul de retragere din `bitshop_sale_withdrawal` cu un buton statistic „Returns" (afișat doar când există transferuri de retur) și cu afișarea mutărilor anulate (`cancelled_move_ids`).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul. Există însă o acțiune de fereastră `action_view_return_pickings` (metodă pe model) care deschide lista transferurilor de retur asociate retragerii, și o activitate (`mail.mail_activity_data_todo`) programată automat pe utilizatorul comenzii de vânzare atunci când există cantități ce nu au putut fi asociate unei mutări de stoc.

#### 5. Conexiuni

- [bitshop_sale_withdrawal](../bitshop_sale_withdrawal/index.md): modulul de bază pentru retragerea dintr-un contract, pe care acesta îl extinde cu execuția specifică stocului.
- `sale_stock`: dependință Odoo standard care leagă comanda de vânzare de livrări (`stock.move`, `stock.picking`).
