# Romania - Stock OBYC (localizat la `l10n_ro_stock_obyc/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_obyc`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_obyc
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_obyc`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Punte între localizarea românească de stoc și determinarea conturilor pe reguli OBYC. Pentru produsele cu clasă de evaluare, conturile operațiilor românești (consum, dare în folosință, recepție prin RNI) se iau din regulile OBYC, nu din categoria produsului, astfel că fiecare clasă (materiale, marfă, obiecte de inventar) are propriul cont de cheltuială. Modulul se instalează automat când `l10n_ro_stock`, `l10n_ro_stock_gestiune` și `deltatech_obyc` sunt prezente. Produsele fără clasă de evaluare rămân pe conturile categoriei, ca înainte.

#### 2. Funcționalități Cheie

- **Chei de tranzacție RO** pentru locațiile specifice României, necunoscute de OBYC:
  - `consumption` (Stoc → Consum, ex. marfă 607 = 371);
  - `consumption_return` (Consum → Stoc: 371 = 607 sau storno 607 = 371 în roșu);
  - `usage_giving` (Stoc → Dare în folosință, ex. 603 = 303);
  - `usage_giving_return` (retur din dare în folosință: 303 = 603 sau storno în roșu).
- **Cont de cheltuială pe clasă de evaluare:** materiale 602, marfă 607, obiecte de inventar 603, nu un cont fix pe locația de consum.
- **Storno la retur:** pe companiile cu contabilitate storno, returul de consum iese pe aceleași conturi ca bonul de consum, cu sume negative.
- **Analitic pe linia de cheltuială:** distribuția analitică a mișcării (ex. proiectul de pe bonul de consum, din `project_stock_account`) ajunge pe linia de cheltuială / venit a notei OBYC, nu pe linii analitice separate; consumul apare în rapoartele contabile pe analitic, iar la retur storno costul proiectului scade.
- **Conturile gestiunii din OBYC:** contul de stoc folosit de `l10n_ro_stock_gestiune` (verificarea gestiunilor cu cont propriu, nota RNI 371 = 408, stornarea ei) este cel din regula OBYC a mișcării.
- **Prioritate RNI:** când recepția e contată prin RNI, OBYC nu mai generează a doua notă pentru aceeași mișcare; la fel la returul către furnizor stornat prin RNI.
- **Diferența de preț RNI:** pentru produsele cu clasă, diferența de preț de la factură merge pe contul de stoc din regula OBYC a recepției (la cost standard rămâne contul nativ de diferențe de preț).
- **Configurare:**
  - clase de evaluare: `Inventar → Configurare → Account Determination Config → Evaluation Class`;
  - câmpul *Valuation Class* pe produsul stocabil;
  - câte o regulă (`Product Account Determination`) pe clasă și pe cheie de tranzacție; operațiile fără notă (ex. transferuri interne în aceeași gestiune) primesc o regulă fără conturi;
  - opțional, *account modifier* pe tipul de operație (ex. „Bon consum proiect”);
  - storno: `Contabilitate → Configurare → Setări → Storno accounting`;
  - dacă lipsește o regulă, la validare apare mesajul OBYC *No account determination rule found…*, cu buton spre configurare.
- **Consum pe proiect:** cu `project_stock_account`, se bifează *Analytic Costs* pe tipul de operație (se setează din modul debug pentru tipurile interne) și se completează *Proiect* pe transfer.
- **Limitări cunoscute (ROADMAP):** consumul nu apare încă în panoul de profitabilitate al proiectului; transferurile între gestiuni (481 / tranzit) folosesc încă conturile setate pe gestiune.

#### 3. Dependențe

- `l10n_ro_stock`
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)
- [deltatech_obyc](../deltatech_obyc/index.md)

#### 4. Componente Cheie

**Modele**

- `product.account.determination` (extins): adaugă în câmpul `transaction_key` cheile `consumption`, `consumption_return`, `usage_giving`, `usage_giving_return`.
- `stock.move` (extins): `_compute_transaction_key` mapează perechile de usage (internal/consume, internal/usage_giving și inversele) la cheile RO; `_l10n_ro_get_stock_account` ia contul de stoc din regula OBYC; `_get_account_move_line_vals` pune analiticul pe liniile de cheltuială / venit; `_create_analytic_move` evită liniile analitice duplicate; `_should_create_account_move` dă prioritate notei RNI.
- `account.move` (extins): `_l10n_ro_get_price_diff_account_for_line` duce diferența de preț RNI pe contul de stoc din regula OBYC a recepției.

**Vizualizări**

- Modulul nu definește vizualizări sau fișiere de date.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_obyc](../deltatech_obyc/index.md): motorul generic de reguli OBYC extins de această punte.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): gestiuni cu cont propriu și nota RNI, aliniate la regulile OBYC.
- `project_stock_account`: sursa distribuției analitice (proiect) de pe bonul de consum, dacă este instalat.
