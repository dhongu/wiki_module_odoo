# Romania - Închiderea soldurilor reziduale pe terți (localizat la `l10n_ro_residual_balance_writeoff/index.md`)

- **Nume Tehnic:** `l10n_ro_residual_balance_writeoff`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_residual_balance_writeoff
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_residual_balance_writeoff`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul închide în masă soldurile reziduale mici rămase pe clienți și furnizori după încasări și plăți: resturi de câțiva bani din rotunjiri, comisioane bancare reținute de plătitor sau plăți făcute cu o mică diferență. În Odoo standard un astfel de rest se închide doar factură cu factură, la reconciliere. Modulul le găsește pe toate deodată, le arată într-o previzualizare și generează notele contabile cu reconcilierea automată a liniilor.

#### 2. Funcționalități Cheie

- Asistentul **Închidere solduri reziduale**, disponibil în **Contabilitate → Clienți** și **Contabilitate → Furnizori**.
- Selecție pe interval de date, parteneri, conturi (implicit toate conturile de clienți și furnizori, cu posibilitatea de a adăuga 409/419 sau alte conturi reconciliabile), monedă și sensul soldului (debitor, creditor sau ambele).
- Prag configurabil: sumă fixă, procent din document sau minimul dintre ele; pragul implicit (implicit 1 leu) se setează în **Contabilitate → Configurare → Setări**, secțiunea *Închidere solduri reziduale (RO)*, și trebuie aprobat prin politica contabilă a firmei.
- Previzualizare cu restul în valută și în lei, componenta de închis, diferența de curs și contul de contrapartidă; liniile se pot debifa, iar contul de contrapartidă se schimbă pe linie sau pe toate liniile selectate.
- Conturi de contrapartidă din setări: cheltuieli (implicit 65882), venituri (implicit 7588), comisioane bancare (627, motiv alegibil doar pe resturile de la clienți).
- Note contabile câte una pe partener sau o singură notă pentru toată selecția, reconciliate automat cu documentele închise.
- Monografie pe sens: client cu rest de încasat `65882 = 4111`, client plătit în plus `4111 = 7588`, furnizor cu rest datorat `401 = 7588`, furnizor plătit în plus `65882 = 401`, comision bancar `627 = 4111`.
- Documente în valută: restul în valută la cursul din data închiderii merge pe 65882/7588, iar diferența până la soldul în lei este diferență de curs realizată pe 665/765, în aceeași notă.
- Fără ajustare de TVA pe resturile închise (art. 287 Cod fiscal); documentele cu TVA la încasare sunt semnalate și excluse implicit.
- **Lista de închidere** în PDF, cu rubricile Întocmit / Aprobat, atașată automat la fiecare notă generată ca document justificativ.
- Fluxul pas cu pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.residual.writeoff`: asistentul (wizard) de căutare, previzualizare și generare a notelor de închidere.
- `l10n.ro.residual.writeoff.line`: linia de previzualizare, cu restul, componenta de închis, diferența de curs și contul de contrapartidă.
- `res.company` / `res.config.settings`: conturile de contrapartidă și pragul implicit.
- `account.move`: extins pentru filtrarea notelor de închidere.

**Vizualizări**

- `view_l10n_ro_residual_writeoff_form`: formularul asistentului, cu criterii și previzualizare.
- `res_config_settings_view_form_residual_writeoff`: setările conturilor și ale pragului.
- `view_account_move_filter_residual_writeoff`: filtru pentru notele de închidere în căutarea notelor contabile.
- `action_report_residual_writeoff`: raportul PDF „Lista de închidere”.

**Acțiuni Automate / Acțiuni Server**

- Nu are acțiuni automate; are acțiunea de fereastră a asistentului și meniurile `menu_l10n_ro_residual_writeoff_receivable` și `menu_l10n_ro_residual_writeoff_payable`.

#### 5. Conexiuni

- `l10n_ro`: planul de conturi românesc din care se preiau conturile implicite (65882, 7588, 627, 665, 765).
