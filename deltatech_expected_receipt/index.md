# Expected Card Receipts (localizat la `deltatech_expected_receipt/index.md`)

- **Nume Tehnic:** `deltatech_expected_receipt`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_expected_receipt
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expected_receipt`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Plățile cu cardul încasate la terminalul bancar ajung în bancă la câteva zile, într-un singur transfer grupat pe zi, fără detalii. Până atunci clientul pare neplătit, iar contabilul trebuie să desfacă manual suma. Modulul înregistrează plata cu cardul în momentul încasării și o decontează, la bani, față de transferul bancar grupat.

#### 2. Funcționalități Cheie

- Buton **Card Payment** pe comenzi de vânzare, pe facturi client și pe client (pentru un sold mai vechi); plățile parțiale sunt normale.
- Plata se postează imediat pe jurnalul băncii terminalului, pe contul de decontări în curs (5125 în România): soldul clientului scade imediat, iar banii așteaptă pe 5125 până la transfer.
- Pe comenzi nefacturate plata este avans: modulul emite factura de avans din comandă și o plătește; oferta plătită cu cardul se confirmă. Alternative la plată: factură deja emisă sau fără factură (doar manageri, suma rămâne credit client).
- Registrul **Expected Receipts**: fiecare plată cu terminal, casier, document și stare (în așteptare, decontată, anulată), cu pivot, grafic, căutare după sumă și filtrul *Late*.
- **Card Settlement** (din linia de extras, **Action > Card Settlement**): găsește grupul de plăți în așteptare a cărui sumă este exact cea transferată (subset-sum exact pe bani) și le reconciliază dintr-un clic. Când două grupuri dau aceeași sumă, le afișează și contabilul bifează grupul corect.
- Comisionul bancar se așteaptă pe o linie separată de extras (627 = 5121); dacă banca virează net, plățile se bifează manual, iar comisionul se contabilizează ca diferență (627 = 5125).
- Grupul *Card Cashier* înregistrează plăți și vede doar încasările proprii, fără drepturi de contabilitate.
- Anularea unei încasări greșite (**Cancel Receipt**, manageri); o încasare decontată sau dintr-o perioadă închisă se corectează prin stornare.
- Setările stau pe terminalele de card (**Contabilitate > Configurare > Card Terminals**): jurnal bancar, utilizator implicit, fereastra de potrivire (implicit 4 zile) și pragul de alertă (implicit 3 zile).
- Necesită **Downpayment Account** setat (419 în România), altfel refuză facturile de avans; contul de decontări în curs trebuie să permită reconcilierea.
- Nu înlocuiește bonul fiscal: pentru vânzările către persoane fizice nu se emite și factură de avans pentru aceeași vânzare dacă ea se contabilizează din raportul Z.

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `deltatech.expected.receipt`: încasarea cu cardul așteptată (terminal, casier, document, stare).
- `deltatech.card.terminal`: terminalul de card cu jurnalul și pragurile.
- `deltatech.card.payment`: wizard de înregistrare a plății.
- `deltatech.card.settlement`, `deltatech.card.settlement.line`: wizard de decontare față de linia de extras.
- `sale.order`, `account.move`, `account.bank.statement.line`: extinse cu butoanele și legăturile.

**Vizualizări**

- `view_expected_receipt_list`, `view_expected_receipt_form`, `view_expected_receipt_pivot`, `view_expected_receipt_graph`, `view_expected_receipt_search`: registrul încasărilor.
- `view_card_terminal_list`, `view_card_terminal_form`: terminalele.
- `view_card_payment_form`, `view_card_settlement_form`: wizardurile.

**Acțiuni Automate / Acțiuni Server**

- `cron_sync_settlements`: la 2 ore, sincronizează registrul când contabilul reconciliază din ecranul standard.
- `action_server_card_settlement`: deschide decontarea de pe linia de extras.

#### 5. Conexiuni

- `l10n_ro`: contul 5125 și planul de conturi românesc.
- [deltatech_sale_store_payment_terminal](../deltatech_sale_store_payment_terminal/index.md): plăți prin terminal în magazin.
