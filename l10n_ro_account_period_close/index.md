# Romania - Închidere perioadă contabilă

- **Nume Tehnic:** `l10n_ro_account_period_close`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_account_period_close
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_account_period_close
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite închiderea conturilor de venituri, de cheltuieli și a TVA între două date, pe baza unor șabloane de închidere definite de contabil. Reduce munca manuală de la sfârșitul lunii sau al anului, generând automat notele contabile de închidere.

#### 2. Funcționalități Cheie

- Șabloane de închidere (tip venituri, cheltuieli sau TVA) în **Contabilitate → Consultant → Acțiuni → Închidere perioadă**, cu jurnal, conturi de închis, cont debitor și cont creditor.
- Acțiunea **Închide perioada** (disponibilă pe șablon) deschide un wizard în care se aleg datele și se apasă „Închide”.
- Șabloanele de venituri și cheltuieli folosesc contul 121000 ca cont debitor și creditor.
- Șablonul de TVA folosește conturile de închis 442600 și 442700, debit 442400, credit 442300, cu opțiunea „Închide conturile debitoare și creditoare” bifată.
- Pentru conturile care se pot închide pe ambele părți (ex. 609, 709, 711xxx) se bifează pe cont opțiunea „Bypass Closing Side Check”.
- Accesibil doar utilizatorilor cu rol de consultant contabil.

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)

Dependență externă Python: `python-dateutil`.

#### 4. Componente Cheie

**Modele**

- `l10n.ro.account.period.closing`: șablonul de închidere (tip, jurnal, conturi, conturi de rezultat, note contabile generate).
- `l10n.ro.account.period.closing.wizard`: wizardul de închidere a perioadei.
- `account.account`, `account.move`: extinse cu mixin-ul `l10n.ro.mixin` (opțiunea de ocolire a verificării părții de închidere pe cont).

**Vizualizări**

- `view_l10n_ro_account_period_closing_tree` / `view_l10n_ro_account_period_closing_form`: lista și formularul șabloanelor.
- `view_account_period_closing_wizard`: wizardul de închidere.
- `view_account_form`: câmpul de bypass pe contul contabil.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate; închiderea se rulează manual din meniul `menu_action_account_period_closing`.

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): configurarea de bază a localizării românești.
