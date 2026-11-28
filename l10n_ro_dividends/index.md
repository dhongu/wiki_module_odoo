# Romania - Dividende și registru acționari (localizat la `l10n_ro_dividends/index.md`)

- **Nume Tehnic:** `l10n_ro_dividends`
- **Versiune:** `20.0.1.1.0`
- **Cale:** `https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_dividends`
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_dividends`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru distribuirea dividendelor conform legislației românești (Cod Fiscal art. 97), de la hotărârea AGA până la plata netă către acționari și vărsarea impozitului. Ține registrul acționarilor/asociaților, calculează dividendul brut și net al fiecăruia, reține impozitul la sursă cu cote istorice (10% pentru distribuirile din 2025, 16% din 1 ianuarie 2026) și generează notele contabile 117/457/446.

#### 2. Funcționalități Cheie

- **Registru acționari/asociați** (Contabilitate → Dividende → Registru Acționari): partener, număr de acțiuni/părți sociale, valoare nominală, procent de participare calculat automat și istoric al modificărilor structurii acționariatului. Fără acționari în registru distribuirea nu poate fi confirmată.
- **Distribuire dividende** (Contabilitate → Dividende → Distribuiri Dividende): hotărâre AGA cu referință, dată, exercițiu financiar și profit net aprobat; butonul „Preia acționari din registru” completează liniile cu procentul, dividendul brut (profit × %), impozitul și dividendul net; procentele și sumele se pot ajusta manual pentru distribuiri neproporționale, iar „Recalculează” reface calculul.
- **Cota impozitului** stabilită după data hotărârii AGA (10% pentru 2025, 16% de la 1 ianuarie 2026), fără configurare.
- **Conturi și jurnale precompletate** după planul companiei: 117, 457, 446, 5121, jurnalul de operațiuni diverse pentru AGA și jurnalul de bancă pentru plată; se verifică la prima utilizare.
- **Note contabile automate:** la confirmarea AGA `Dr 117 = Cr 457`; la plată `Dr 457 = Cr 446` (impozit reținut) și `Dr 457 = Cr 5121` (net plătit).
- **Stări:** Ciornă → Confirmat AGA → Plătit, cu anulare înainte de plată și resetare la Ciornă.
- CASS 10% pentru persoane fizice nu se reține de societate în acest modul; beneficiarul o declară prin Declarația Unică dacă depășește plafoanele.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.shareholder`: registrul acționarilor/asociaților (partener, acțiuni, valoare nominală, procent de participare).
- `l10n.ro.dividend`: distribuirea de dividende (hotărârea AGA), cu fluxul de stări, conturile/jurnalele și notele contabile generate; moștenește `mail.thread` și `mail.activity.mixin`.
- `l10n.ro.dividend.line`: linia per acționar (procent, dividend brut, cotă, impozit, net).

**Vizualizări**

- `view_l10n_ro_shareholder_tree` / `view_l10n_ro_shareholder_form` și `action_l10n_ro_shareholder`: registrul acționarilor.
- `view_l10n_ro_dividend_tree` / `view_l10n_ro_dividend_form` și `action_l10n_ro_dividend`: distribuirile de dividende.

**Acțiuni Automate / Acțiuni Server**

- Niciuna. Notele contabile se generează la confirmarea AGA și la plată.

#### 5. Conexiuni

- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): notele explicative la situațiile financiare, unde apar dividendele distribuite.
- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md): situațiile financiare în care se reflectă profitul distribuit și datoriile către acționari.
