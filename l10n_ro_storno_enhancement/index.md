# Romania - Storno Enhancements (`l10n_ro_storno_enhancement`)

- **Nume Tehnic:** `l10n_ro_storno_enhancement`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_storno_enhancement
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_storno_enhancement`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul extinde contabilitatea storno din Odoo pentru localizarea românească: corecțiile se înregistrează „în roșu”, cu sume negative pe aceeași parte a contului ca nota inițială, astfel încât rulajul conturilor să nu fie umflat de o inversare pe partea opusă.

#### 2. Funcționalități Cheie

- **Storno la orice inversare:** Odoo standard aplică storno doar notelor de credit și doar firmelor cu storno activat (automat, când țara fiscală este România). Cu modulul, orice notă inversată, inclusiv notele contabile diverse, se postează în roșu, iar inversarea unei note storno redă o notă normală.
- **Storno manual pe notele contabile:** opțiunea „Storno (red reversal)” pe o notă diversă în ciornă postează toate liniile în roșu, pentru corecții introduse manual.
- **Utilizarea contului:** câmpul „Usage” pe conturi le clasifică în Activ (sold debitor), Pasiv (sold creditor) sau Bifuncțional (implicit). Se completează automat la instalare pentru conturile planului de conturi românesc și poate fi schimbat per cont.
- **Fost nume:** modulul s-a numit `l10n_ro_account_storno`. Instalat pe o bază care îl are pe cel vechi, preia automat datele acestuia, păstrând valorile de utilizare a conturilor.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.account` (extins): câmpul `l10n_ro_usage` (Activ / Pasiv / Bifuncțional).
- `account.move` (extins): câmpul `l10n_ro_force_storno` pentru storno manual și logica storno la inversare.
- `res.company` (extins): setări legate de storno.

**Vizualizări**

- `view_account_form` (`account_account_view.xml`): adaugă câmpul de utilizare pe formularul contului.
- `view_move_form` (`account_move_view.xml`): adaugă opțiunea Storno pe nota contabilă.

**Acțiuni Automate / Acțiuni Server**

- `pre_init_hook` / `post_init_hook`: preiau datele fostului `l10n_ro_account_storno` și completează utilizarea conturilor din planul românesc. Nu există cron-uri.

#### 5. Conexiuni

- [l10n_ro_account_storno](../l10n_ro_account_storno/index.md): fostul nume al modulului, ale cărui date sunt preluate la instalare.
