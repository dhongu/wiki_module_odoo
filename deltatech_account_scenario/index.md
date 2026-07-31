# Accounting Scenario Framework (localizat la `deltatech_account_scenario/index.md`)

- **Nume Tehnic:** `deltatech_account_scenario`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_scenario
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_scenario`
- **Ultima Ingestie:** `2026-06-09`

#### 1. Sumar

`deltatech_account_scenario` este un modul Odoo 19 care oferă un cadru bazat pe JSON pentru rularea și validarea unor scenarii contabile complete. Modulul permite dezvoltatorilor și contabililor să definească procese de afaceri (facturi, plăți, note contabile, mijloace fixe, recepții de stoc, livrări etc.) sub formă de scenarii JSON, să le execute pe o bază de date Odoo activă și să valideze automat înregistrările contabile și valorizările de stoc rezultate. Modulul funcționează în două moduri: modul „test", în care execută un scenariu și verifică dacă notele contabile și valorile de stoc generate corespund celor așteptate definite în JSON, și modul „demo", în care execută un scenariu pentru a genera date demonstrative fără validare contabilă strictă.

#### 2. Funcționalități Cheie

- **Scenarii definite prin JSON** — procese de afaceri complete descrise ca JSON structurat, cu pași (acțiuni) și înregistrări contabile/de stoc așteptate. Pașii se împart în pași de date master (creează sau identifică date de referință: conturi, parteneri, categorii de produse, produse) și pași tranzacționali (comenzi de aprovizionare, recepții de stoc, facturi furnizor, comenzi de vânzare, facturi, transferuri de stoc, note contabile, plăți). Fiecare pas poate include un câmp `_comment` folosit ca mesaj de jurnal.
- **Validare contabilă și de stoc** — după execuția pașilor, motorul compară liniile `account.move.line` generate cu secțiunea `expected_account_moves` din JSON, validând coduri de cont, sume debit/credit și conturi analitice; validează și cantitățile și valorile de stoc per produs prin secțiunea `checks` din fiecare pas, raportând clar neconcordanțele în jurnalul rulării.
- **Integrare în interfață** — listă de scenarii cu import de fișiere JSON (buton „Import Scenarios"), formular de scenariu cu export JSON, istoric al rulărilor (fiecare execuție înregistrată ca `account.test.run` cu jurnal complet și rezultat), navigare din jurnal direct către documentul aferent (factură, transfer, plată), butoane „Set Ready", „Execute Scenario", „Re-run Scenario", „View Runs", și meniu sub **Accounting → Account Scenarios** (Test Scenarios și Test Runs).
- **Bibliotecă de scenarii inclusă** — date de bază (`00_base_data.json`) cu categorii de produse, parteneri și produse comune, scenarii demo pentru fluxuri de achiziție/vânzare, transferuri și recepții, plus **140 de scenarii de testare a contabilității de stoc românești** sub `data/scenarios/ro_stock/`: 70 de scenarii FIFO și 70 de scenarii cost mediu ponderat (CMP), acoperind cazuri-limită conform reglementărilor contabile din România.
- **Teste automate** — teste `TransactionCase` sub `tests/test_stock_scenarios.py` și `tests/common.py` care acoperă crearea de categorii, parteneri și produse, crearea și postarea facturilor, execuția completă a scenariilor, achiziții și vânzări cu verificări contabile, precum și gestionarea erorilor pentru tipuri de pași necunoscute.

#### 3. Dependențe

- `account`
- `stock`
- `stock_account`
- `purchase_stock`
- `sale_stock`

Dependență externă Python: `markdown`.

#### 4. Componente Cheie

**Modele**

- `stock.test.scenario`: Stochează definiția scenariului JSON, modul de execuție și starea.
- `account.test.run`: Înregistrează fiecare execuție cu jurnal, rezultat și legătură către scenariu.
- `stock.test.log`: Linii individuale de jurnal pentru fiecare pas — număr pas, tip, stare (`ok`/`error`/`info`), mesaj și referință de document.

#### 5. Conexiuni

- `stock_account`: oferă valorizarea de stoc și integrarea contabilă pe care motorul de scenarii o validează.
- `purchase_stock` / `sale_stock`: furnizează fluxurile de aprovizionare și vânzare cu impact pe stoc folosite în pașii tranzacționali ai scenariilor.
