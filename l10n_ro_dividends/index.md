# Romania - Dividende și registru acționari (localizat la `l10n_ro_dividends/index.md`)

- **Nume Tehnic:** `l10n_ro_dividends`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_dividends
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_dividends`
- **Ultima Ingestie:** 2026-10-25
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru gestionarea completă a distribuirii de dividende conform legislației românești (Cod Fiscal art. 97). Acoperă registrul acționarilor/asociaților, hotărârea AGA de distribuire, calculul dividendului brut și net per acționar, reținerea impozitului la sursă cu cote istorice (10% pentru 2025, 16% din 1 ianuarie 2026) și generarea automată a notelor contabile aferente.

#### 2. Funcționalități Cheie

- **Registru Acționari / Asociați** (**Contabilitate → Dividende → Registru Acționari**): înregistrarea acționarilor cu partener, număr de acțiuni/părți sociale și valoare nominală; procentul de participare se calculează automat din totalul acțiunilor; istoric al modificărilor structurii de acționariat.
- **Distribuire Dividende** (**Contabilitate → Dividende → Distribuiri Dividende**): hotărâre AGA cu referință, dată, exercițiu financiar și profit net aprobat; butonul *Preia acționari din registru* completează liniile cu procentele din registru, iar *Recalculează* reface calculul (ambele doar în Ciornă). Procentele și sumele pot fi ajustate manual când distribuirea nu e proporțională cu participarea.
- **Calcul dividend:** brut (profit × % participare), impozit reținut și net de plată, per acționar și în total.
- **Reținere impozit la sursă** în funcție de data hotărârii AGA: 10% pentru 2025, 16% începând cu 1 ianuarie 2026; nu necesită configurare.
- **Note contabile automate:** la confirmare `Dr 117 = Cr 457` (profit → dividende de plată); la înregistrarea plății `Dr 457 = Cr 446` (impozit reținut) și `Dr 457 = Cr 5121` (net plătit). Conturile și jurnalele (operațiuni diverse pentru AGA, bancă/casă pentru plată) se precompletează după planul de conturi al companiei și merită verificate la prima utilizare.
- **Validări:** confirmarea cere cel puțin un acționar, conturile 117 și 457 și jurnalul; plata cere conturile 446 și 5121, jurnalul de plată și data plății efective.
- **Flux de lucru:** Ciornă → Confirmat AGA → Plătit, cu anulare înainte de plată și resetare la Ciornă.
- **CASS:** pentru persoane fizice nu se reține de societate; beneficiarul o declară prin Declarația Unică dacă veniturile extrasalariale cumulate ating plafoanele legale. Impozitul din contul 446 se declară prin D100, iar datele alimentează D205.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.shareholder`: registrul acționarilor/asociaților — partener, număr de acțiuni, valoare nominală, capital social și procent de participare.
- `l10n.ro.dividend`: distribuirea de dividende (hotărârea AGA), cu `mail.thread` și `mail.activity.mixin`; ține exercițiul, profitul aprobat, conturile 117/457/446/5121, jurnalele, starea și notele contabile generate (distribuire și plată).
- `l10n.ro.dividend.line`: linia per acționar — procent, dividend brut, cota și suma impozitului, dividend net.

**Vizualizări**

- `view_l10n_ro_shareholder_tree` / `view_l10n_ro_shareholder_form`: lista și formularul registrului de acționari.
- `view_l10n_ro_dividend_form`: formularul distribuirii, cu butoane de stare, bară de stare, butoane inteligente către nota de distribuire și nota de plată, conturile contabile și liniile acționarilor cu totaluri.
- `view_l10n_ro_dividend_tree`: lista distribuirilor, colorată după stare.
- Meniul **Contabilitate → Dividende** (sub `account.menu_finance_entries`) cu *Distribuiri Dividende* și *Registru Acționari*; drepturile de acces sunt în `security/ir.model.access.csv`.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni `ir.cron`, `base.automation` sau `ir.actions.server`; notele contabile se generează la confirmarea AGA și la plată (`action_confirm`, `action_pay`).*

#### 5. Conexiuni

- [l10n_ro_shareholder_loan](../l10n_ro_shareholder_loan/index.md): împrumuturile de la asociați; depinde direct de acest modul (registrul de acționari).
- [l10n_ro_financial_notes](../l10n_ro_financial_notes/index.md): nota explicativă are câmpul „Dividende distribuite” (fără dependență tehnică).
- [l10n_ro_financial_statements](../l10n_ro_financial_statements/index.md): raportul F30 afișează dividendele plătite din rulajul contului 457 (fără dependență tehnică).
