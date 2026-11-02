# Accounting Scenario Framework (localizat la `deltatech_account_scenario/index.md`)

- **Nume Tehnic:** `deltatech_account_scenario`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_scenario
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_scenario`
- **Ultima Ingestie:** `2026-11-02`

#### 1. Sumar

`deltatech_account_scenario` oferă un cadru bazat pe JSON pentru rularea și validarea unor scenarii contabile complete. Procesele de afaceri (facturi, plăți, note contabile, mijloace fixe, recepții de stoc, livrări etc.) se descriu ca scenarii JSON, se execută pe o bază de date Odoo activă, iar notele contabile și valorizările de stoc rezultate se verifică automat. Este util pentru validarea unei configurări contabile înainte de punerea în funcțiune și pentru demonstrații reproductibile. Modulul funcționează în două moduri: „test", în care scenariul este rulat și comparat cu notele contabile și valorile de stoc așteptate din JSON, și „demo", în care scenariul generează date demonstrative fără validare contabilă strictă. Este un modul nou în 19.0.

#### 2. Funcționalități Cheie

- **Scenarii definite prin JSON**: procese complete descrise ca JSON structurat, cu pași și înregistrări contabile/de stoc așteptate.
  - Pașii de date master creează sau identifică datele de referință: conturi, parteneri, categorii de produse, produse (reutilizate dacă există deja).
  - Pașii tranzacționali execută operațiuni: comenzi de aprovizionare, recepții și retururi de stoc, facturi furnizor, comenzi de vânzare și facturi, inventar, transferuri, consum, note contabile, plăți, mijloace fixe.
  - Fiecare pas poate avea un câmp `_comment`, folosit ca mesaj în jurnal. Pașii pot seta taxele de pe liniile de comandă și de factură și datele documentelor (comandă, factură, programată), ca scenariul să reproducă situații de final de lună sau de exercițiu.
- **Validare contabilă și de stoc**: după execuție, liniile `account.move.line` generate sunt comparate cu secțiunea `expected_account_moves` (coduri de cont, sume debit/credit sau sold, conturi analitice); cantitățile și valorile de stoc pe produs se verifică prin secțiunea `checks` a fiecărui pas. Valorile sunt validate ca diferențe față de starea de la începutul scenariului, deci scenariile rulează corect și pe baze de date cu mișcări anterioare. Neconcordanțele apar clar în jurnalul rulării.
- **Rulare în compania scenariului**: rularea folosește compania scenariului, nu compania activă; scenariile, rulările și jurnalele altor companii sunt ascunse. Accesul este limitat la utilizatorii de contabilitate (cei cu drept doar de citire pot doar consulta), iar ștergerea cere rolul Administrator de contabilitate.
- **Integrare în interfață**: meniul **Accounting → Account Scenarios** (Test Scenarios și Test Runs); lista de scenarii cu butonul **Import Scenarios** (import de fișiere JSON, mereu vizibil); formular cu export JSON și butoanele „Set Ready", „Execute Scenario", „Re-run Scenario", „View Runs"; fiecare execuție este o rulare `account.test.run` cu jurnal complet și rezultat, descărcabil ca Markdown sau HTML; din jurnal se deschide direct documentul creat (factură, transfer, plată).
- **Bibliotecă de scenarii inclusă**: date de bază (`00_base_data.json`) cu categorii de produse, parteneri și produse comune; scenarii demo pentru fluxuri de achiziție/vânzare, transferuri și recepții; **140 de scenarii de contabilitate de stoc românească** în `data/scenarios/ro_stock/` (70 FIFO și 70 cost mediu ponderat, cu cazuri-limită conform reglementărilor din România); plus scenarii OBYC în `data/scenarios/deltatech_obyc/`. Scenariile demo se încarcă la instalarea cu date demo.
- **Teste automate**: teste `TransactionCase` pentru pașii de creare a datelor master, execuția completă a scenariilor, achiziții și vânzări cu verificări contabile și gestionarea pașilor necunoscuți.
- Formatul JSON al pașilor (câmpuri, valori) este descris în `readme/USAGE.MD` al modulului.

#### 3. Dependențe

- `account`
- `stock`
- `stock_account`
- `purchase_stock`
- `sale_stock`

Dependență externă Python: `markdown`.

#### 4. Componente Cheie

**Modele**

- `account.scenario`: definiția scenariului JSON, modul de execuție (test/demo), starea și compania; conține acțiunile de import, export, execuție și vizualizare a rulărilor.
- `account.test.run`: fiecare execuție, cu jurnal, rezultat și legătură către scenariu; conține motorul de pași (`_run_step_*`) și validările.
- `account.test.log`: liniile individuale de jurnal ale unei rulări — număr pas, tip, stare (`ok`/`error`/`info`), mesaj și referință de document, cu deschiderea documentului.

**Vizualizări**

- `view_account_scenario_form` / `view_account_scenario_list`: formularul și lista scenariilor (acțiunea `action_account_scenario`, „Test Scenarios").
- `view_account_test_run_form` / `view_account_test_run_list`: formularul și lista rulărilor (acțiunea `action_account_test_run`, „Test Runs").
- `view_account_scenario_import_wizard`: asistentul „Import Scenarios" pentru fișiere JSON.

**Acțiuni Automate / Acțiuni Server**

- `action_server_reload_demo_scenarios`: acțiune server („Reload Demo Scenarios") care reîncarcă scenariile demo.
- La instalarea cu date demo se apelează `load_base_data` și `load_demo_scenarios`. Nu există acțiuni `ir.cron` sau `base.automation`.

#### 5. Conexiuni

- `stock_account`: oferă valorizarea de stoc și integrarea contabilă pe care motorul de scenarii o validează.
- `purchase_stock` / `sale_stock`: furnizează fluxurile de aprovizionare și vânzare cu impact pe stoc folosite în pașii tranzacționali ai scenariilor.
