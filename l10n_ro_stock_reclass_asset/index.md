# Romania - Stock Reclassification to Fixed Assets (localizat la `l10n_ro_stock_reclass_asset/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_reclass_asset`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_reclass_asset
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_reclass_asset`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Extinde documentul de reclasificare a stocului cu reclasificarea în mijloace fixe: din stoc (371 Mărfuri, 3028 Alte materiale consumabile) în imobilizări (213x, 214), cu activul creat chiar din documentul de reclasificare, nu din factura furnizorului. E util companiilor care cumpără bunuri ca marfă sau materiale și hotărăsc ulterior să le folosească ca mijloc fix sau obiect de inventar, și țin registrul imobilizărilor în Odoo Enterprise.

#### 2. Funcționalități Cheie

- **Tip de destinație pe regulă:** mijloc fix (213x), mobilier (214) sau obiect de inventar (303), pe lângă schimbarea contului de stoc din modulul de bază.
- **Prag pe unitate:** valoarea minimă a unui mijloc fix (implicit 5.000 lei), setat pe companie în Inventar → Configurare → Setări; sub prag (pe regulă de mijloc fix) sau peste prag (pe regulă de obiect de inventar) apare doar un avertisment în chatter, fără blocare.
- **Active create din document:** la validare, după setarea *Active din reclasificare* a contului destinație (*Creează în ciornă*, *Creează și validează* sau *Nu*), se creează câte un activ pe unitate, cu modelul de amortizare al contului; seria sau IMEI-ul apare în nume, iar cu `l10n_ro_fixed_assets` activul primește număr de inventar.
- **Buton „Creează active”** pentru conturile cu opțiunea pe *Nu*.
- **Inversare:** activele rămase în ciornă se șterg; dacă un activ e validat, inversarea e refuzată până la casarea lui.
- Locația destinație: în afara stocului pentru mijloace fixe, internă pentru obiecte de inventar. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- [deltatech_stock_reclass](../deltatech_stock_reclass/index.md)
- `account_asset`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `stock.reclassification`, `stock.reclassification.line`, `stock.reclassification.rule`: extinse cu tipul de destinație și crearea activelor.
- `account.account`: setarea *Active din reclasificare* și *Un activ pe unitate*.
- `account.asset`, `account.move.line`: legătura activului cu documentul și linia de origine.
- `res.company`, `res.config.settings`: pragul pe unitate.

**Vizualizări**

- `views/reclassification_views.xml`: tipul de destinație pe regulă, contorul și butonul de active pe document.
- `views/account_account_views.xml`: opțiunile de creare a activelor pe contul destinație.
- `views/res_config_settings_views.xml`: pragul în setările de inventar.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): numărul de inventar și fila *Informații RO* pe activ, când e instalat.
- [deltatech_stock_reclass](../deltatech_stock_reclass/index.md): documentul de reclasificare a stocului pe care îl extinde.
