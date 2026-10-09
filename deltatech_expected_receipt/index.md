# Deltatech Expected Receipts (Încasări așteptate cu cardul)

- **Nume Tehnic:** `deltatech_expected_receipt`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_expected_receipt
- **Cale Locală:** `odoo-addons/deltatech/deltatech_expected_receipt`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Plățile cu cardul făcute la terminal ajung în bancă după câteva zile, ca un singur transfer grupat pe zi, fără detalii. Până atunci clientul pare neachitat, iar contabilul trebuie să împartă manual suma din extras. Modulul înregistrează plata cu cardul în momentul încasării și o decontează apoi, la bănuț, față de transferul bancar grupat.

#### 2. Funcționalități Cheie

- **Buton Plată cu cardul** pe comenzile de vânzare, pe facturile clienților și pe client (pentru un sold mai vechi, din **Contabilitate > Clienți > Plată card pe client**). Plățile parțiale sunt normale; diferența rămâne de plată. Suma este propusă din valoarea datorată, iar terminalul se alege automat după utilizator.
- Plata se postează imediat în jurnalul bancar al terminalului, pe contul de decontare al jurnalului (5125 *Sume în curs de decontare* în România; 5125 = 4111): soldul clientului scade imediat, iar banii așteaptă pe 5125 până sosește transferul.
- **Factură de avans pe comenzi nefacturate**: plata cu cardul pe o comandă nefacturată este avans, iar TVA devine exigibil la încasare. Pe comandă se alege modul de facturare: *plătește o factură emisă*, *emite factură de avans* (implicit; se creează din comandă, se postează și se achită) sau *fără factură* (doar manageri; suma rămâne credit client, de folosit doar dacă livrarea se facturează în aceeași perioadă de TVA). O ofertă plătită cu cardul este confirmată.
- **Registrul Încasări așteptate** (**Contabilitate > Clienți > Încasări așteptate**): fiecare plată cu terminal, casier, document și stare (în așteptare, decontată, anulată), cu pivot, grafic, căutare după sumă și filtrul *Întârziate* pentru plățile nedecontate după numărul de zile setat pe terminal.
- **Decontare card**: de pe linia de extras (**Acțiune > Decontare card** sau **Contabilitate > Contabilitate > Decontare card**), modulul caută grupul de plăți în așteptare a cărui sumă este exact valoarea transferată (subset-sum exact pe bani, rapid și la 60–80 de plăți) și le reconciliază dintr-un clic. Dacă două grupuri diferite dau aceeași sumă, nu alege singur: le afișează (coloana *Combinație*) și contabilul bifează grupul corect. Fără combinație exactă, mesajul arată cât lipsește. Fereastra de căutare este cea setată pe terminal.
- **Comisionul bancar** este așteptat pe o linie de extras separată (627 = 5121). Dacă banca virează suma netă, se bifează manual plățile, iar comisionul se înregistrează ca diferență pe contul de decontare (627 = 5125) în reconcilierea standard.
- **Casieri fără drepturi contabile**: grupul *Casier card* înregistrează plăți și vede doar încasările proprii; plata e scrisă de modul după verificarea companiei, terminalului și documentului.
- **Anulare încasare** (manageri): anulează și plata; factura de avans emisă rămâne postată și se stornează cu notă de credit. O încasare decontată sau dintr-o perioadă închisă se corectează prin storno contabil.
- O acțiune programată sincronizează registrul când contabilul reconciliază din ecranul standard de reconciliere bancară.
- Nu se adaugă câmpuri pe comenzi, facturi, plăți sau companii: setările stau pe terminalele de card (jurnal bancar, utilizator implicit, fereastra de potrivire - implicit 4 zile, pragul de alertă - implicit 3 zile).
- **Configurare**: grupurile *Încasări așteptate / Manager* (contabilii; administratorii contabili îl primesc automat) și *Casier card*; contul de decontare al jurnalului trebuie să permită reconcilierea; **Contul pentru avansuri** (419 în România) setat în **Facturare > Configurare > Setări**, altfel modulul refuză emiterea facturilor de avans.
- **Atenție**: modulul nu înlocuiește bonul fiscal. Dacă vânzările către persoane fizice sunt înregistrate din raportul Z, nu emiteți și factură de avans din modul pentru aceeași vânzare (venit și TVA dublate).

#### 3. Dependențe

- `account`
- `sale`

#### 4. Componente Cheie

**Modele**

- `deltatech.expected.receipt`: registrul încasărilor cu cardul (terminal, casier, document, plată, stare; cu `mail.thread`).
- `deltatech.card.terminal`: terminal de card; jurnal bancar, utilizator implicit, fereastra de potrivire și pragul de alertă.
- `deltatech.card.payment` (tranzitoriu): wizardul Plată cu cardul.
- `deltatech.card.settlement` și `deltatech.card.settlement.line` (tranzitorii): wizardul de decontare și liniile lui.
- `sale.order`, `account.move`, `account.bank.statement.line` (extinse): butoane și logica de plată, respectiv de decontare.

**Vizualizări**

- `view_expected_receipt_list`, `_form`, `_search`, `_pivot`, `_graph`: registrul încasărilor.
- `view_card_terminal_list`, `view_card_terminal_form`: terminale de card.
- `view_card_payment_form`: wizardul Plată cu cardul.
- `view_card_settlement_form`: wizardul Decontare card.
- `view_order_form`, `view_move_form`: butonul de plată pe comandă și pe factură.

**Acțiuni Automate / Acțiuni Server**

- `cron_sync_settlements`: „Expected receipts: synchronize settlements”, rulează la 2 ore (`_cron_sync_settlements`).
- `action_server_card_settlement`: acțiunea Decontare card de pe linia de extras.
- `action_card_payment_partner`: Plată cu cardul pe client.

#### 5. Conexiuni

- `account`, `sale`: documentele pe care se înregistrează plata.
- `l10n_ro`: conturile 5125, 4111, 419, 627 din planul contabil românesc.
