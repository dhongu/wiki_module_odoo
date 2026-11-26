# Sale Withdrawal - Stock (localizat la `deltatech_sale_withdrawal_stock/index.md`)

- **Nume Tehnic:** `deltatech_sale_withdrawal_stock`
- **Versiune:** `19.0.0.2.11`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_sale_withdrawal_stock
- **Cale Locală:** `odoo-addons/bitshop/deltatech_sale_withdrawal_stock`
- **Ultima Ingestie:** `2026-11-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul asigură continuarea operațională a retragerii dintr-un contract (dreptul de retragere al consumatorului, Directiva 2011/83/UE, cu funcția de retragere din art. 11a și 14a adăugată prin Directiva (UE) 2023/2673, aplicabilă din 19 iunie 2026 oricărui comerciant care vinde online consumatorilor din UE) pe partea de stoc: atunci când un client renunță la un contract, marfa trebuie fie oprită din livrare, fie returnată. Modulul adaugă modul de execuție `stock_return` pentru `deltatech_sale_withdrawal`, disponibil în **Vânzări → Configurare → Setări → Retragere din Contract → Execuție Retragere**, ca opțiunea „Cancel or return the goods” (Anulează sau returnează marfa).

#### 2. Funcționalități Cheie

- Anulează ce nu a fost încă expediat; cantitățile retrase parțial micșorează mutarea de stoc în loc să o anuleze integral
- Ce a fost deja livrat este returnat prin wizard-ul standard de retur din Odoo, astfel încât mutările de retur rămân legate de livrările pe care le anulează
- Perioada de retragere a mărfurilor se calculează după **ultimul** colet livrat pentru linie, nu după primul
- Cantitățile care nu pot fi asociate unei mutări de stoc generează pe comanda de vânzare o activitate *To Do* („Withdrawal needs manual handling”), nefiind niciodată ignorate în tăcere; activitatea e atribuită vânzătorului comenzii (sau utilizatorului curent, dacă lipsește — la o retragere din portal poate fi un utilizator de portal, deci se recomandă vânzător setat pe fiecare comandă), cu scadența la termenul de rambursare, și numește cantitatea și produsul. Aceeași activitate apare când un pas intern (pick, pack) e deja făcut: textul spune ce marfă trebuie repusă manual în stoc. Nota există doar în activitate, nu pe formularul retragerii
- **Execuția pornește singură**, imediat ce retragerea e confirmată în portal; setarea se aplică retragerilor înregistrate după salvare. Rezultatul se verifică pe retragere (Vânzări → Comenzi → Retrageri: **Execution Mode**, **Cancelled Moves**, butonul **Returns**) și pe livrări
- Retragere integrală a mărfii nelivrate: mutările se anulează (livrarea rămâne în sistem cu starea *Anulat*), fără retur. Retragere parțială: mutarea se micșorează, iar restul comenzii pleacă normal; la livrare în mai mulți pași (pick, pack, ship) reducerea se aplică ultimului pas în așteptare și pașilor din care provine
- Marfa deja livrată: se creează un transfer de retur (starea *Ready*, nevalidat — îl validează depozitul la sosirea mărfii), legat de livrarea pe care o anulează, doar pentru mutările livrate clientului; documentul sursă indică livrarea inițială
- Cantitățile se convertesc între unitatea comenzii și cea a mutării (1 duzină = 12 bucăți)
- **Termenul de retragere** (*Withdrawal Deadline* pe comanda de vânzare) apare abia când toate mutările liniei sunt făcute și se numără de la **ultima** livrare, nu de la primirea coletului de către consumator, deci e cu câteva zile (timpul de tranzit) mai devreme decât cel legal — se păstrează o marjă. Returul creat de modul e el însuși o mutare a liniei: cât timp nu e validat, termenul dispare și comanda rămâne deschisă retragerii în portal; după validare, termenul pentru cantitatea rămasă reîncepe de la data returului. După executarea unei retrageri nu te baza pe acest câmp
- Modulul nu rambursează consumatorul și nu generează note contabile: nota de credit se emite prin fluxul obișnuit de facturare, apoi se apasă **Mark Refunded** pe retragere
- Atenție: nu folosi **Resend Acknowledgement** pe o retragere în starea *Submitted* sau *Acknowledged* — butonul reia execuția (a doua retur pentru marfa livrată, a doua reducere a livrării la o retragere parțială, activitate falsă și listă goală de mutări anulate la o retragere integrală a mărfii nelivrate)
- Cerință prealabilă: modulul de bază `deltatech_sale_withdrawal` trebuie configurat (perioadă de retragere, termen de rambursare, buton în portal)

#### 3. Dependențe

- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md)
- `sale_stock`

#### 4. Componente Cheie

**Modele**

- `deltatech.sale.withdrawal` (extins): adaugă câmpurile `return_picking_ids` (transferuri de retur), `cancelled_move_ids` (mutări anulate) și metoda `_execute_withdrawal_stock_return()`, care implementează modul de execuție `stock_return` — anulează mutările nelivrate/micșorează cantitatea pentru retrageri parțiale, iar pentru mutările deja finalizate creează retururi prin wizard-ul standard `stock.return.picking`, ca traseul de trasabilitate/valorizare să rămână intact.
- `sale.order.line` (extins): suprascrie `_bitshop_withdrawal_period_start()` pentru produsele fizice, calculând începutul perioadei de retragere pe baza datei ultimei mutări de stoc finalizate (nu a primei), și doar după ce toate mutările liniei sunt în starea `done`.
- `res.company` (extins): adaugă opțiunea `stock_return` la selecția `bitshop_withdrawal_execution_mode`.

**Vizualizări**

- `view_deltatech_sale_withdrawal_form_stock`: extinde formularul de retragere din `deltatech_sale_withdrawal` cu un buton statistic „Returns" (afișat doar când există transferuri de retur) și cu afișarea mutărilor anulate (`cancelled_move_ids`).

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul. Există însă o acțiune de fereastră `action_view_return_pickings` (metodă pe model) care deschide lista transferurilor de retur asociate retragerii, și o activitate (`mail.mail_activity_data_todo`) programată automat pe utilizatorul comenzii de vânzare atunci când există cantități ce nu au putut fi asociate unei mutări de stoc.

#### 5. Conexiuni

- [deltatech_sale_withdrawal](../deltatech_sale_withdrawal/index.md): modulul de bază pentru retragerea dintr-un contract, pe care acesta îl extinde cu execuția specifică stocului.
- `sale_stock`: dependință Odoo standard care leagă comanda de vânzare de livrări (`stock.move`, `stock.picking`).
