# Romania - Închiderea soldurilor reziduale pe terți

- **Nume Tehnic:** `l10n_ro_residual_balance_writeoff`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_residual_balance_writeoff
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_residual_balance_writeoff`
- **Ultima Ingestie:** `2026-10-09`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul închide în masă soldurile reziduale mici rămase pe clienți și furnizori după încasări și plăți: resturi de câțiva bani din rotunjiri, comisioane bancare reținute de plătitor sau plăți făcute cu o mică diferență. În Odoo standard, un astfel de rest se închide doar factură cu factură, la reconciliere. Modulul le găsește pe toate deodată, le arată într-o previzualizare și generează notele contabile cu reconcilierea automată a liniilor.

#### 2. Funcționalități Cheie

- Asistent **Închidere solduri reziduale**, disponibil în meniurile **Contabilitate → Clienți** și **Furnizori**.
- Selecție pe interval de date al documentelor, parteneri (gol = toți), conturi (implicit toate conturile de clienți și furnizori, cu posibilitatea de a adăuga 409/419 sau alte conturi reconciliabile), monedă și sens (sold debitor, creditor sau ambele).
- Prag configurabil: **sumă fixă**, **procent din document** sau **minimul dintre ele**; valorile implicite se setează în **Contabilitate → Configurare → Setări**, secțiunea *Închidere solduri reziduale (RO)* (pragul trebuie aprobat prin politica contabilă a firmei).
- Previzualizare cu restul în valută și în lei, componenta de închis, diferența de curs și contul de contrapartidă; liniile se pot debifa înainte de generare.
- Contul de contrapartidă e propus din setări și se poate schimba pe fiecare linie sau pe toate liniile selectate deodată („Cont pentru toate liniile” + „Aplică liniilor selectate”). Generarea se oprește dacă un cont nu corespunde sensului (clasa 6 pentru rest pierdut, clasa 7 pentru rest câștigat; 473 și 461/462 sunt admise pe orice sens).
- Motiv **Comision bancar** pe resturile de la clienți, cu contrapartidă 627.
- Note contabile **câte una pe partener** (implicit) sau **o singură notă** pentru toată selecția, în jurnal de tip Diverse, reconciliate automat cu documentele închise (acestea devin plătite).
- Monografie pe sens:

  | Situație | Notă contabilă |
  |---|---|
  | Client cu rest de încasat | `65882 = 4111` |
  | Client care a plătit în plus | `4111 = 7588` |
  | Furnizor căruia i se mai datorează un rest | `401 = 7588` |
  | Furnizor plătit în plus | `65882 = 401` |
  | Rest cauzat de comisionul bancar al plătitorului | `627 = 4111` |

- Documente în valută: restul în valută, evaluat la cursul de la data închiderii, merge pe 65882/7588, iar diferența până la soldul în lei e diferență de curs realizată pe 665/765, în aceeași notă (fără notă separată în jurnalul de diferențe de curs).
- Fără ajustare de TVA pe resturile închise (art. 287 Cod fiscal); documentele cu **TVA la încasare** sunt semnalate și excluse implicit (se pot include cu o bifă dedicată).
- **Lista de închidere** în PDF (criterii, motive, totaluri, rubrici Întocmit/Aprobat), atașată automat la fiecare notă generată ca document justificativ.
- Filtru **Închideri solduri reziduale** pe Note contabile. Anularea se face prin Resetare la Ciornă, apoi Anulează (desface reconcilierea).
- Recomandare: resturile se închid înainte de reevaluarea valutară de la sfârșitul lunii. Reducerile de preț și refuzurile parțiale se rezolvă prin factură de corecție, nu prin acest modul.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.residual.writeoff` (wizard): criterii de selecție, căutarea resturilor, generarea și reconcilierea notelor, tipărirea listei.
- `l10n.ro.residual.writeoff.line`: rândul de previzualizare (document, rest în valută/lei, de închis, diferență de curs, motiv, cont de contrapartidă, bifă de selecție).
- `res.company` / `res.config.settings` (extinse): conturile de cheltuieli, venituri și comisioane bancare, plus pragul implicit (sumă și procent).
- `account.move` (extins): marcaj boolean `l10n_ro_residual_writeoff` pentru notele generate de modul.

**Vizualizări**

- `view_l10n_ro_residual_writeoff_form`: formularul asistentului cu criterii și previzualizare.
- `res_config_settings_view_form_residual_writeoff`: setările de conturi și prag.
- `view_account_move_filter_residual_writeoff`: filtrul „Închideri solduri reziduale” pe note contabile.
- `action_l10n_ro_residual_writeoff` și meniurile `menu_l10n_ro_residual_writeoff_receivable` / `_payable`.

**Acțiuni Automate / Acțiuni Server**

- `action_report_residual_writeoff`: raportul PDF „Lista de închidere”. Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- `l10n_ro_doc_screenshots`: folosit doar de testele care generează capturile fișei (nu e dependență).
