# Accounting Extensions (localizat la `deltatech_account/index.md`)

- **Nume Tehnic:** `deltatech_account`
- **Versiune:** `20.0.2.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_account
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul completează contabilitatea standard Odoo cu vizualizări îmbunătățite pentru facturi, opțiuni suplimentare pentru jurnale și o setare pentru recunoașterea costurilor în stil anglo-saxon. Este util companiilor care vor un control mai strâns al fluxurilor financiare.

#### 2. Funcționalități Cheie

- **Contabilitate anglo-saxonă:** comutator în *Accounting > Configuration > Settings*, secțiunea *Fiscal Localization* (vizibil doar utilizatorilor din grupul tehnic `base.group_no_one`). Când este activ, costul mărfurilor vândute se înregistrează în notele contabile la facturare, nu la livrare. Setarea este per companie, deci fiecare companie dintr-un mediu multi-companie o poate activa independent.
- Redenumește meniuri contabile standard pentru claritate (de exemplu „Incoming payments” pentru meniul plăților de încasat).
- Oferă o bază pentru personalizări ulterioare ale formularului standard de factură.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md` și `CONFIGURE.md`; componentele din cod sunt minimale.

**Modele**

- `res.config.settings` (extins): câmpul `use_anglo_saxon`, înrudit cu `company_id.anglo_saxon_accounting`.

**Vizualizări**

- `res_config_settings_view_form`: adaugă setarea Anglo-Saxon Accounting în setările de contabilitate.
- `views/account_invoice_view.xml`: redenumește meniul `account.menu_action_account_payments_receivable` în „Incoming payments”.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron` sau acțiuni server.

#### 5. Conexiuni

- `account`: modulul standard de contabilitate pe care `deltatech_account` îl extinde.
