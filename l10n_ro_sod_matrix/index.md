# Matrice Segregare Atribuții (SoD) România (localizat la `l10n_ro_sod_matrix/index.md`)

- **Nume Tehnic:** `l10n_ro_sod_matrix`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_sod_matrix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sod_matrix`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este un instrument de audit și conformitate internă care detectează și gestionează conflictele de roluri (Segregation of Duties) conform cerințelor de control intern și audit financiar. Definește o matrice configurabilă de perechi de grupuri Odoo incompatibile, scanează utilizatorii pentru a identifica violările și oferă un flux de aprobare pentru recunoașterea, exceptarea sau rezolvarea acestora. Suplimentar, poate bloca la nivel de companie plata unei facturi de către același utilizator care a înregistrat-o.

#### 2. Funcționalități Cheie

- **Matrice de reguli SoD configurabilă:** perechi de grupuri incompatibile, cu severitate pe 4 niveluri (Critică / Ridicată / Medie / Redusă) și 6 reguli implicite preconfigurate conform bunelor practici de control intern.
- **Detecție automată și manuală:** buton „Scanează utilizatori" pe fiecare regulă pentru verificare imediată și cron săptămânal (inactiv implicit) pentru scanare automată.
- **Auto-rezolvare violări:** când conflictul dispare (userul pierde un grup), violarea se arhivează automat ca „Rezolvată" la următoarea scanare.
- **Gestionare violări cu flux de aprobare:** `Deschisă → Recunoscută → Exceptată / Rezolvată`, cu notă de justificare a excepțiilor, exportabilă pentru auditori.
- **Blocare auto-plată facturi (FR-57):** opțiune la nivel de companie (`Setări → Facturare`) care împiedică un utilizator să înregistreze plata unei facturi pe care el însuși a creat-o — separarea între cine introduce factura și cine o plătește.
- **Raportare audit:** filtre și grupări pentru analiza conflictelor, listă filtrată implicit pe reguli critice / violări deschise.

#### 3. Dependențe

- `base`
- `account`
- `purchase`
- `stock`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.sod.rule`: Regula SoD — perechea de grupuri incompatibile (`group_a_id`, `group_b_id`), severitatea și descrierea riscului; expune scanarea (`action_scan`, `_scan_users`) și scanarea globală pentru cron (`_l10n_ro_sod_scan_all`).
- `l10n.ro.sod.violation`: Violarea detectată, cu fluxul de aprobare (`open` → `acknowledged` → `waived`/`resolved`) și nota de justificare; constrânsă unic pe pereche `(rule_id, user_id)`.
- `res.company` (extindere): câmpul `l10n_ro_sod_block_self_payment` — activează blocarea auto-plății facturilor la nivel de companie.
- `res.config.settings` (extindere): expune `l10n_ro_sod_block_self_payment` în ecranul de setări Facturare.
- `account.payment.register` (extindere): verifică la `_create_payments()`, prin `_l10n_ro_check_sod_self_payment()`, dacă utilizatorul curent este autorul facturii plătite și blochează operațiunea cu `UserError` dacă opțiunea companiei este activă.

**Vizualizări**

- `views/l10n_ro_sod_rule_view.xml`: listă/formular reguli SoD, cu numărul de violări deschise și butonul de scanare.
- `views/l10n_ro_sod_violation_view.xml`: listă/formular violări SoD, cu acțiunile Recunoaște / Exceptează / Redeschide.
- `views/res_config_settings_view.xml`: adaugă setarea „Block Self-Payment (SoD)" în panoul de facturare al Setărilor generale.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_sod_scan` („RO SoD: Automatic scan of segregation of duties violations"): cron săptămânal (inactiv implicit) care rulează `_l10n_ro_sod_scan_all()` pe toate regulile active.
- `data/l10n_ro_sod_rules.xml`: 6 reguli SoD implicite preconfigurate (`noupdate="1"`).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): suita de localizare română din care face parte modulul.
- `account`: grupurile contabile (Manager contabilitate, Contabil) folosite în regulile implicite și restricția meniurilor SoD.
- `purchase` / `stock`: grupurile de achiziții și gestiune de stoc folosite în regulile implicite (Manager achiziții + Manager gestiune stoc etc.).
