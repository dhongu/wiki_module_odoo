# Accounting Extensions (localizat la `deltatech_account/index.md`)

- **Nume Tehnic:** `deltatech_account`
- **Versiune:** `19.0.2.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_account
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account`
- **Ultima Ingestie:** `2026-10-28`

#### 1. Sumar

Modulul completează contabilitatea standard Odoo cu o setare pentru recunoașterea costurilor în sistem anglo-saxon și cu mici ajustări de meniu, utile companiilor care vor un control mai strâns asupra fluxurilor financiare. Setarea permite înregistrarea costului mărfurilor vândute direct în notele contabile, în momentul facturării, iar redenumirea unor meniuri face interfața mai clară.

#### 2. Funcționalități Cheie

- Adaugă comutatorul **Anglo-Saxon Accounting** în **Contabilitate > Configurare > Setări**, secțiunea *Localizare fiscală*. Când e activ, costul mărfurilor vândute se înregistrează în notele contabile la facturare, nu la livrare.
- Setarea este vizibilă doar utilizatorilor din grupul tehnic `base.group_no_one` (mod dezvoltator) și depinde de companie: în configurații multi-companie, fiecare companie o poate activa sau dezactiva independent.
- Redenumește meniuri contabile standard pentru claritate (de exemplu, meniul plăților de încasat apare ca „Incoming payments”).
- Oferă punctul de plecare pentru personalizări ulterioare ale formularului de factură; fișierul de vizualizări pentru facturi este în prezent gol.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `res.config.settings` (extins): adaugă câmpul `use_anglo_saxon` („Anglo-Saxon Accounting”), legat de `company_id.anglo_saxon_accounting`, editabil.

**Vizualizări**

- `res_config_settings_view_form`: extinde `account.res_config_settings_view_form`; adaugă setarea `use_anglo_saxon_setting` în blocul de localizare fiscală (grup `base.group_no_one`) și ajustează eticheta aplicației în „Accounting”.
- `account_invoice_view.xml`: fără înregistrări în prezent.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server. Modulul redenumește doar meniurile `account.menu_finance` („Accounting”) și `account.menu_action_account_payments_receivable` („Incoming payments”).

#### 5. Conexiuni

- `account`: modulul standard de contabilitate Odoo pe care `deltatech_account` îl extinde (setări și meniuri).
