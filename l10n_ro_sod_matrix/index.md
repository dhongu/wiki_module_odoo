# Romania - Matrice de segregare a atribuțiilor (SoD) (localizat la `l10n_ro_sod_matrix/index.md`)

- **Nume Tehnic:** `l10n_ro_sod_matrix`
- **Versiune:** `20.0.1.1.7`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_sod_matrix](https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_sod_matrix)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_sod_matrix`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de audit și conformitate internă care detectează și gestionează conflictele de roluri (Segregation of Duties), pentru companiile care trebuie să demonstreze separarea atribuțiilor în fața auditorilor sau a controalelor interne. Definește o matrice configurabilă de perechi de grupuri Odoo incompatibile, scanează utilizatorii pentru violări și oferă un flux de aprobare pentru recunoaștere, exceptare sau rezolvare. Opțional, poate bloca plata unei facturi de către utilizatorul care a înregistrat-o.

#### 2. Funcționalități Cheie

- **Matrice de reguli configurabilă:** perechi de grupuri incompatibile, cu severitate pe 4 niveluri (Critică / Ridicată / Medie / Redusă) și 6 reguli implicite (ex. Administrator sistem + Manager contabilitate, Manager achiziții + Manager gestiune stoc). Meniu: **Contabilitate → Configurare → Contabilitate → Matrice SoD → Reguli SoD**.
- **Scanare manuală și automată:** butonul „Scanează utilizatori" pe regulă și un cron săptămânal, activ implicit la instalare nouă (la upgrade se păstrează starea existentă). Scanarea ține cont și de grupurile moștenite.
- **Flux de violări:** Deschisă → Recunoscută → Exceptată / Rezolvată, cu notă de justificare exportabilă pentru auditori; la **Violări SoD**. Violările deschise se auto-rezolvă când utilizatorul pierde un grup, iar cele recunoscute sau exceptate își păstrează decizia.
- **Blocare autoplată (opțional, pe companie):** setarea „Blochează autoplata (SoD)" din **Contabilitate → Configurare → Setări** împiedică înregistrarea plății de către autorul facturii.
- **Raportare audit:** filtre și grupări; lista e filtrată implicit pe reguli critice / violări deschise. Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `base`
- `account`
- `purchase`
- `stock`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.sod.rule`: regula SoD — perechea de grupuri (`group_a_id`, `group_b_id`), severitatea, descrierea riscului; `action_scan`, `_scan_users`, `_l10n_ro_sod_scan_all` (cron).
- `l10n.ro.sod.violation`: violarea detectată, cu fluxul de aprobare; unică pe perechea (regulă, utilizator).
- `res.company` / `res.config.settings` (extinderi): câmpul `l10n_ro_sod_block_self_payment`.
- `account.payment.register` (extindere): `_l10n_ro_check_sod_self_payment()` blochează cu `UserError` plata facturii proprii când opțiunea e activă.

**Vizualizări**

- `views/l10n_ro_sod_rule_view.xml`: listă/formular reguli, cu violări deschise și buton de scanare.
- `views/l10n_ro_sod_violation_view.xml`: listă/formular violări, cu acțiunile Recunoaște / Exceptează / Redeschide.
- `views/res_config_settings_view.xml`: setarea de blocare a autoplății.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_sod_scan`: cron săptămânal care rulează `_l10n_ro_sod_scan_all()` pe regulile active.
- `data/l10n_ro_sod_rules.xml`: 6 reguli implicite (`noupdate="1"`).

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): suita de localizare română din care face parte modulul.
- `account`: grupurile contabile folosite în regulile implicite.
- `purchase` / `stock`: grupurile de achiziții și gestiune de stoc folosite în regulile implicite.
