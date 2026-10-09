# Romania - Împrumuturi de la asociați (contract de creditare, 455) (localizat la `l10n_ro_shareholder_loan/index.md`)

- **Nume Tehnic:** `l10n_ro_shareholder_loan`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_shareholder_loan
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_shareholder_loan`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul ține evidența împrumuturilor primite de societate de la asociați sau acționari, pe baza unui contract de creditare. Tranșele încasate și rambursările făcute din casă sau bancă se leagă de contract, iar pe contract se văd mereu sumele primite, cele restituite și soldul datorat. Contractul se poate tipări în PDF, cu anexă care cuprinde mișcările și soldul.

#### 2. Funcționalități Cheie

- **Contract de creditare**: asociatul se alege din registrul asociaților (modulul `l10n_ro_dividends`); se completează suma convenită, moneda, data, durata în luni, scadența (calculată din dată și durată, modificabilă), dobânda anuală (opțională, doar informativă) și destinația împrumutului. Pe pagina **Detalii contract** se completează reprezentantul legal, funcția acestuia și actul de identitate al asociatului.
- **Cont propus după durată**: 45511 pentru împrumuturi restituite în cel mult un an, 45512 pentru cele pe termen mai lung; dacă lipsesc analiticele, se propune primul cont 455 disponibil.
- **Stări**: Ciornă → Activ → Închis (sau Anulat). Închiderea e posibilă doar când soldul datorat este zero; un contract închis poate fi redeschis. Confirmarea leagă automat operațiile deja postate pe contul și partenerul contractului, de la data contractului.
- **Tranșe și rambursări din casă și bancă**: încasările (Dr 5311/5121 = Cr 455) și restituirile (Dr 455 = Cr 5311/5121) se înregistrează ca de obicei, în registrul de casă, extrasul de cont sau notă contabilă, cu asociatul ca partener. La postare, linia se leagă singură de contractul activ al asociatului, dacă acesta are un singur contract pe contul respectiv.
- **Acțiunea „Contract de creditare”** (din nota contabilă sau din linia de extras): leagă operația de un contract existent (când sunt mai multe contracte active) sau creează contractul în ciornă direct din operație, cu suma, data, moneda și contul preluate; dacă operația e deja legată, deschide contractul.
- **Sold**: pe contract — *Primit*, *Restituit*, *Sold datorat*, *Neprimit încă*; butonul **Operații** listează notele legate. Meniul **Sold pe asociat** este un pivot pe asociat și contract, filtrabil după dată pentru soldul la o anumită zi (sold negativ = sumă datorată asociatului).
- **Contract tipărit (PDF)**: părțile, obiectul, dobânda (sau mențiunea „fără dobândă”), durata, termenul de rambursare și semnăturile; în anexă, sumele primite și restituite până la data tipăririi, cu soldul datorat.
- **Drepturi**: *Contabilitate / Contabil* creează și modifică contracte; doar *Contabilitate / Administrator* le șterge.
- **Meniu**: Contabilitate → Contabilitate → Împrumuturi de la asociați (Contracte de împrumut, Sold pe asociat).
- **Atenție la numerar**: modulul nu verifică plafoanele din Legea nr. 70/2015 pentru încasări și plăți în numerar.

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_dividends](../l10n_ro_dividends/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.shareholder.loan`: contractul de creditare (asociat, sumă, monedă, durată, scadență, cont 455, stări, sume calculate primit/restituit/sold); folosește chatter și activități.
- `l10n.ro.shareholder.loan.link` (wizard): leagă liniile de contabilitate de un contract existent sau creează contractul din operație.
- `account.move.line` (extins): câmpul `l10n_ro_shareholder_loan_id` și legarea automată la postare.
- `account.move` și `account.bank.statement.line` (extinse): acțiunea „Contract de creditare” și declanșarea legării automate la `_post`.

**Vizualizări**

- `view_l10n_ro_shareholder_loan_list` / `_form` / `_search`: lista, formularul și filtrele contractelor.
- `view_l10n_ro_shareholder_loan_pivot` și `view_l10n_ro_shareholder_loan_move_line_pivot`: pivotul soldului pe asociat și contract.
- `view_l10n_ro_shareholder_loan_link_form`: wizardul de legare/creare contract.
- `view_move_form_l10n_ro_shareholder_loan`: legătura cu contractul pe nota contabilă.
- Raport QWeb `action_report_l10n_ro_shareholder_loan`: contractul de împrumut în PDF.

**Acțiuni Automate / Acțiuni Server**

- `action_server_l10n_ro_shareholder_loan_move` și `action_server_l10n_ro_shareholder_loan_statement_line`: acțiunea „Contract de creditare” pe notă contabilă, respectiv pe linia de extras.
- `seq_l10n_ro_shareholder_loan`: secvență pentru numerotarea contractelor (nu există cron-uri).

#### 5. Conexiuni

- [l10n_ro_dividends](../l10n_ro_dividends/index.md): furnizează registrul asociaților din care se alege împrumutătorul (și dependență directă).
- `l10n_ro`: planul de conturi românesc cu analiticele 45511 / 45512.
