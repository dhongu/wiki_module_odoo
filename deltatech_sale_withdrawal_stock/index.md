# Sale Withdrawal - Stock (localizat la `deltatech_sale_withdrawal_stock/index.md`)

- **Nume Tehnic:** `deltatech_sale_withdrawal_stock`
- **Versiune:** `20.0.0.2.8`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_sale_withdrawal_stock
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_withdrawal_stock`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul asigură continuarea operațională a retragerii dintr-un contract (renunțare de tip consumator) pe partea de stoc: atunci când un client renunță la un contract, marfa trebuie fie oprită din livrare, fie returnată. Modulul adaugă modul de execuție `stock_return` pentru [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md), disponibil în **Vânzări → Configurare → Setări → Retragere din Contract → Execuție Retragere**.

#### 2. Funcționalități Cheie

- Anulează ce nu a fost încă expediat; cantitățile retrase parțial micșorează mutarea de stoc în loc să o anuleze integral
- Ce a fost deja livrat este returnat prin fluxul standard de retur din Odoo, astfel încât mutările de retur rămân legate de livrările pe care le anulează
- Perioada de retragere a mărfurilor se calculează după **ultimul** colet livrat pentru linie, nu după primul
- Perioada de retragere începe la livrarea din depozit, nu la primirea de către consumator; returul influențează termenul retragerii, iar fluxul pas-cu-pas stă în fișa consultant.
- Cantitățile care nu pot fi asociate unei mutări de stoc generează o activitate pe retragere, nefiind niciodată ignorate în tăcere

#### 3. Dependențe

- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md)
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.withdrawal` (extins): adaugă câmpurile `return_picking_ids` (transferuri de retur), `cancelled_move_ids` (mutări anulate) și metoda `_execute_withdrawal_stock_return()`, care implementează modul de execuție `stock_return` — anulează mutările nelivrate/micșorează cantitatea pentru retrageri parțiale, iar pentru mutările deja finalizate creează retururi prin fluxul standard de retur al transferului (`stock.picking._create_return()`; wizard-ul `stock.return.picking` nu mai există în Odoo 20), ca traseul de trasabilitate/valorizare să rămână intact.
- `sale.order.line` (extins): suprascrie `_deltatech_withdrawal_period_start()` pentru produsele fizice, calculând începutul perioadei de retragere pe baza datei ultimei mutări de stoc finalizate (nu a primei), și doar după ce toate mutările liniei sunt în starea `done`.
- `res.company` (extins): adaugă opțiunea `stock_return` la selecția `deltatech_withdrawal_execution_mode`.

**Vizualizări**

- `view_deltatech_sale_withdrawal_form_stock`: extinde formularul de retragere din `deltatech_sale_withdrawal` cu un buton statistic „Returns" (afișat doar când există transferuri de retur) și cu afișarea mutărilor anulate (`cancelled_move_ids`).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul. Există însă o acțiune de fereastră `action_view_return_pickings` (metodă pe model) care deschide lista transferurilor de retur asociate retragerii, și o activitate (`mail.mail_activity_data_todo`) programată automat pe utilizatorul comenzii de vânzare atunci când există cantități ce nu au putut fi asociate unei mutări de stoc.

#### 5. Conexiuni

- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md): modulul de bază pentru retragerea dintr-un contract, pe care acesta îl extinde cu execuția specifică stocului.
- `sale_stock`: dependință Odoo standard care leagă comanda de vânzare de livrări (`stock.move`, `stock.picking`).
