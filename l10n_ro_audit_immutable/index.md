# Romania - Pistă de Audit Imuabilă (FR-14) (localizat la `l10n_ro_audit_immutable/index.md`)

- **Nume Tehnic:** `l10n_ro_audit_immutable`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_audit_immutable
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_audit_immutable`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Modulul implementează o pistă de audit imuabilă pentru documentele contabile, conform cerințelor OMFP 1802/2014 și legislației românești privind securizarea datelor contabile. Înregistrează automat toate operațiunile de creare, modificare și ștergere asupra documentelor financiare cheie și protejează jurnalul de audit împotriva alterării atât la nivel ORM, cât și direct în baza de date prin triggere PostgreSQL.

## 2. Funcționalități Cheie

- **Pistă de audit imuabilă:** înregistrează automat operațiunile create / write / unlink pe `account.move`, `account.move.line`, `account.journal`, `account.account` și `account.tax`.
- **Dublu strat de protecție:** la nivel ORM, `write()` și `unlink()` pe `l10n.ro.audit.log` aruncă `UserError`; la nivel PostgreSQL, triggerele `BEFORE UPDATE/DELETE` blochează inclusiv operațiunile `sudo()` care ocolesc record rules.
- **Hash chain SHA-256 pe jurnale:** activează automat `restrict_mode_hash_table = True` pe toate jurnalele companiilor românești la instalare și blochează dezactivarea lanțului de hash pe jurnalele RO.
- **Vizualizare audit:** meniu dedicat „Pistă de Audit" în Rapoarte contabile, cu filtre rapide (acțiune, model, utilizator, dată) și decorare vizuală (verde=creare, portocaliu=modificare, roșu=ștergere).
- **Extindere la alte modele:** prin mixinul `l10n.ro.audit.mixin` și metoda `_l10n_ro_audit_fields()`, auditul poate fi extins la modele suplimentare.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- `l10n.ro.audit.log`: jurnalul de audit imuabil care stochează operațiunile create / write / unlink pe documentele financiare.
- `l10n.ro.audit.mixin` (Mixin Python): permite extinderea auditului la alte modele prin definirea câmpurilor auditate.
- `account.move`, `account.move.line`, `account.journal`, `account.account`, `account.tax`: extinse pentru a fi auditate implicit.

### Vizualizări / Date

- `views/l10n_ro_audit_log_views.xml`: vizualizările pistei de audit (listă, formular, filtre).
- `views/menus.xml`: meniul „Pistă de Audit" din secțiunea Rapoarte contabile.
- `security/l10n_ro_audit_security.xml` și `security/ir.model.access.csv`: drepturile de acces pentru jurnalul de audit.

### Acțiuni Automate / Acțiuni Server

- `post_init_hook`: la instalare activează `restrict_mode_hash_table` pe jurnalele RO și instalează triggerele PostgreSQL de protecție.

## 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_account_chart]]`
