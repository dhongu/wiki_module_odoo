# Romania - Stock OBYC (localizat la `l10n_ro_stock_obyc/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_obyc`
- **Versiune:** `20.0.1.0.9`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_obyc
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_obyc`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Punte între localizarea românească de stoc pe gestiuni și determinarea conturilor pe reguli OBYC. Pentru produsele cu clasă de evaluare, conturile operațiilor românești (consum, dare în folosință, recepții prin RNI) se iau din regulile OBYC, nu din categoria produsului. Se instalează automat când ambele module de bază sunt prezente.

#### 2. Funcționalități Cheie

- **Patru chei de tranzacție RO:** `consumption` (607 = 371), `consumption_return`, `usage_giving` (603 = 303) și `usage_giving_return`; contul de cheltuială vine din regula clasei de evaluare (materiale 602, marfă 607, obiecte de inventar 603).
- **Storno la retur:** pe companiile cu contabilitate storno, returul iese pe aceleași conturi, cu sume negative.
- **Analitic pe linia de cheltuială:** distribuția analitică a mișcării (de exemplu proiectul bonului de consum) se pune pe linia de cheltuială a notei OBYC.
- **Conturile gestiunii din OBYC:** contul de stoc folosit pentru verificarea gestiunilor și nota RNI 371 = 408 este cel din regula OBYC a mișcării.
- **Prioritate RNI:** când recepția e contată prin RNI, OBYC nu mai generează o a doua notă; la fel la returul către furnizor stornat prin RNI.
- **Diferența de preț RNI** merge pe contul de stoc din regula OBYC a recepției (la cost standard rămâne contul nativ).
- **Configurare:** clase de evaluare (Inventar → Configurare → Account Determination Config), clasa pe produs, câte o regulă pe cheie și clasă; lipsa unei reguli dă mesajul OBYC cu buton spre configurare. Produsele fără clasă rămân pe conturile categoriei.
- Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md)
- [deltatech_obyc](../deltatech_obyc/index.md)

#### 4. Componente Cheie

**Modele**

- `product.account.determination`, `stock.move`, `stock.location`, `account.move`, `account.move.line`: extinse pentru cheile RO, storno, analitic și conturile gestiunii.

**Vizualizări**

- Fără vizualizări proprii (`data` gol).

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Modulul e `auto_install` pe `l10n_ro_stock_gestiune` și `deltatech_obyc`.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): gestiunile și nota RNI ale căror conturi le determină regulile OBYC.
- [deltatech_obyc](../deltatech_obyc/index.md): motorul de reguli OBYC pe care îl completează cu cheile RO.
