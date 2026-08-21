# Romania - Pistă de Audit Imuabilă (FR-14) (localizat la `l10n_ro_audit_immutable/index.md`)

- **Nume Tehnic:** `l10n_ro_audit_immutable`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_audit_immutable
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_audit_immutable`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează o pistă de audit imuabilă pentru documentele contabile, conform cerințelor OMFP 1802/2014 și legislației românești privind securizarea datelor contabile. Orice operație de creare, modificare sau ștergere pe înregistrările financiare cheie este înregistrată automat și protejată prin două straturi independente de imuabilitate, atât la nivel ORM cât și direct în baza de date prin triggere PostgreSQL.

#### 2. Funcționalități Cheie

- **Pistă de audit imuabilă:** înregistrează automat operațiunile INSERT / UPDATE / DELETE pe modelele `account.move`, `account.move.line`, `account.journal`, `account.account` și `account.tax`.
- **Dublu strat de imuabilitate:** la nivel ORM, `write()` și `unlink()` pe `l10n.ro.audit.log` aruncă `UserError`; la nivel PostgreSQL, triggerele `BEFORE UPDATE/DELETE` blochează inclusiv operațiunile `sudo()` care ocolesc record rules.
- **Hash chain SHA-256 pe jurnale:** activează automat `restrict_mode_hash_table = True` pe toate jurnalele companiilor românești la instalare și blochează dezactivarea lanțului de hash pe jurnalele RO, cu mesaj explicit de conformitate.
- **Vizualizare audit read-only:** meniu dedicat „Pistă de Audit" în Contabilitate → Rapoarte, cu filtre rapide (acțiune, model, utilizator, dată) și decorare vizuală (verde=creare, portocaliu=modificare, roșu=ștergere).
- **Câmpuri auditate selectiv per model:** stochează valorile vechi și noi, IP-ul sesiunii și un snapshot al utilizatorului (rezistent la ștergerea contului).
- **Extindere la alte modele:** prin mixinul `l10n.ro.audit.mixin` și metoda `_l10n_ro_audit_fields()`, auditul poate fi extins la modele suplimentare.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.audit.log`: jurnalul de audit imuabil care stochează operațiunile create / write / unlink pe documentele financiare (model, câmp, valoare veche/nouă, utilizator, IP, dată).
- `l10n.ro.audit.mixin` (mixin Python): permite extinderea auditului la alte modele prin definirea câmpurilor auditate (`_l10n_ro_audit_fields()`).
- `account.move`, `account.move.line`, `account.journal`, `account.account`, `account.tax`: extinse pentru a fi auditate implicit și, în cazul `account.journal`, pentru a bloca dezactivarea hash chain-ului pe jurnalele RO.

**Vizualizări**

- `views/l10n_ro_audit_log_views.xml`: vizualizările pistei de audit (listă read-only cu decorare pe tip de acțiune, formular, filtre după acțiune/model/utilizator/dată).
- `views/menus.xml`: meniul „Pistă de Audit" din secțiunea Rapoarte contabile.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalarea modulului activează `restrict_mode_hash_table` pe jurnalele companiilor românești și instalează triggerele PostgreSQL `BEFORE UPDATE/DELETE` de protecție a jurnalului de audit.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate în cod/manifest către alte module (dincolo de dependențele directe de mai sus).
