# Romania - Matrice de segregare a atribuțiilor (SoD) (localizat la `l10n_ro_sod_matrix/index.md`)

- **Nume Tehnic:** `l10n_ro_sod_matrix`
- **Versiune:** `19.0.1.1.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_sod_matrix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sod_matrix`
- **Ultima Ingestie:** `2026-11-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul este un instrument de audit și conformitate internă care detectează și gestionează conflictele de roluri (Segregation of Duties) conform cerințelor de control intern și audit financiar. Definește o matrice configurabilă de perechi de grupuri Odoo incompatibile, scanează utilizatorii pentru a identifica violările și oferă un flux de aprobare pentru recunoașterea, exceptarea sau rezolvarea acestora. Suplimentar, poate bloca la nivel de companie plata unei facturi de către același utilizator care a înregistrat-o. Modulul nu generează note contabile; remedierea (reorganizarea rolurilor) rămâne o decizie de management.

#### 2. Funcționalități Cheie

- **Matrice de reguli SoD configurabilă** (**Contabilitate → Configurare → Contabilitate → Matrice SoD → Reguli SoD**): perechi de grupuri incompatibile, cu severitate pe 4 niveluri (Critică / Ridicată / Medie / Redusă), descrierea riscului pentru auditori și numărul de violări deschise; lista se deschide filtrată implicit pe **Critică**. La instalare se încarcă 6 reguli implicite (de ex. Administrator sistem + Manager contabilitate, Manager achiziții + Manager gestiune stoc), care pot fi dezactivate (câmpul „Activ”), modificate sau completate cu reguli proprii; upgrade-ul nu le resetează.
- **Detecție automată și manuală:** butonul „Scanează utilizatori” pe fiecare regulă verifică imediat utilizatorii activi și nu duplică violările existente; scanarea automată rulează săptămânal prin cron, **activ la o instalare nouă** (starea aleasă de client se păstrează la upgrade; se poate verifica din **Setări → Tehnic → Automatizare → Acțiuni planificate**). Scanarea ține cont și de grupurile moștenite (ex. „Manager contabilitate” include „Facturare”).
- **Gestionare violări cu flux de aprobare** (**Matrice SoD → Violări SoD**, deschisă filtrat pe **Deschise**): `Deschisă → Recunoscută → Exceptată / Rezolvată`, cu acțiunile **Recunoaște**, **Exceptează** (cu justificare în notă) și **Redeschide**; lista se poate filtra după severitate și status și exporta pentru auditori.
- **Auto-rezolvare violări:** când utilizatorul pierde unul dintre grupurile incompatibile, violarea „Deschisă” trece în „Rezolvată” la următoarea scanare; violările recunoscute sau exceptate își păstrează decizia documentată (pentru a le închide se apasă întâi **Redeschide**). O violare „Rezolvată” nu se redeschide singură dacă grupurile revin: se șterge și se rescanează regula.
- **Blocare auto-plată facturi (FR-57):** setarea **Blochează autoplata (SoD)** din **Contabilitate → Configurare → Setări**, blocul **Plăți furnizori** (pe companie, oprită implicit), împiedică un utilizator să înregistreze plata unei facturi create de el (**Plătește → Crează plata**); plata o înregistrează alt utilizator.
- **Acces:** meniurile Matrice SoD și Violări SoD sunt vizibile doar grupului **Contabilitate / Manager** (`account.group_account_manager`). Fluxul pas-cu-pas este în fișa consultantului.

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
- `res.config.settings` (extindere): expune `l10n_ro_sod_block_self_payment` în ecranul de setări.
- `account.payment.register` (extindere): verifică la `_create_payments()`, prin `_l10n_ro_check_sod_self_payment()`, dacă utilizatorul curent este autorul facturii plătite și blochează operațiunea cu `UserError` dacă opțiunea companiei este activă.

**Vizualizări**

- `views/l10n_ro_sod_rule_view.xml`: listă/formular reguli SoD, cu numărul de violări deschise și butonul de scanare.
- `views/l10n_ro_sod_violation_view.xml`: listă/formular violări SoD, cu acțiunile Recunoaște / Exceptează / Redeschide.
- `views/res_config_settings_view.xml`: adaugă setarea „Block Self-Payment (SoD)” în Setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_sod_scan` („RO SoD: Automatic scan of segregation of duties violations”): cron săptămânal (la 7 zile), activ la instalarea nouă, care rulează `_l10n_ro_sod_scan_all()` pe toate regulile active; înregistrarea are `noupdate="1"`.
- `data/l10n_ro_sod_rules.xml`: 6 reguli SoD implicite preconfigurate (`noupdate="1"`).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): suita de localizare română din care face parte modulul.
- `account`: grupurile contabile (Manager contabilitate, Contabil) folosite în regulile implicite și restricția meniurilor SoD.
- `purchase` / `stock`: grupurile de achiziții și gestiune de stoc folosite în regulile implicite (Manager achiziții + Manager gestiune stoc etc.).
