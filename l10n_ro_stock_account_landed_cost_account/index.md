# Romania - Stock Accounting Landed Cost Account

- **Nume Tehnic:** `l10n_ro_stock_account_landed_cost_account`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_stock_account_landed_cost_account
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_stock_account_landed_cost_account
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Cheltuielile de transport, manipulare sau vamă, facturate separat de marfă, se adaugă la costul de achiziție al stocului. Modulul completează documentul standard Odoo „Costuri adiționale” cu determinarea contului din locația de stoc și cu completarea automată a costului din factura furnizorului, astfel încât nota contabilă să respecte localizarea românească (371 pe debit, contul de cheltuieli al liniei pe credit).

#### 2. Funcționalități Cheie

- Determinarea contului de evaluare a stocului din locație (destinație la intrări, sursă la ieșiri), împreună cu poziția fiscală a jurnalului.
- Completarea automată a costului adițional creat din factura furnizorului: recepțiile comenzii de achiziție și contul fiecărei linii se preiau din factură.
- Opțional, rutarea creditului de clasa 6 printr-un cont intermediar tehnic, setat pe companie (**Metodă cost adițional clasa 6**: *Standard* sau *Prin cont intermediar*, plus **Cont Intermediar**, în *Contabilitate > Configurare > Setări*, blocul România).
- La metoda *Prin cont intermediar*, forma notei depinde de bifa **Storno accounting** a companiei (a doua pereche în roșu sau clasică); setările afișează un avertisment dacă bifa e oprită.
- Funcționează pentru ambele moduri de recepție (fără Aviz și pe bază de aviz) și tratează stocul rezervat sau deja vândut la validarea costului. Fluxul detaliat este în fișa consultantului.

#### 3. Dependențe

- `stock_landed_costs`
- `l10n_ro_stock_account`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `res.company` / `res.config.settings`: câmpurile `l10n_ro_landed_cost_method` și `l10n_ro_landed_cost_intermediary_account_id`.
- `stock.valuation.adjustment.lines`: determinarea conturilor pentru nota costului adițional.
- `account.move` / `account.move.line`: completarea costului adițional din factură, cu `l10n.ro.mixin`.

**Vizualizări**

- `res_config_settings_view_form`: blocul de setări pentru metoda de cost adițional și contul intermediar.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `l10n_ro_stock_account`: modulul de bază al contabilității de stoc, a cărui notă de evaluare o completează.
