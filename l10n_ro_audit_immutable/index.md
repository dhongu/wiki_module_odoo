# Romania - Pistă de audit imuabilă (localizat la `l10n_ro_audit_immutable/index.md`)

- **Nume Tehnic:** `l10n_ro_audit_immutable`
- **Versiune:** `20.0.1.1.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_audit_immutable
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_audit_immutable`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează o pistă de audit imuabilă pentru documentele contabile, conform cerințelor OMFP 1802/2014 și legislației românești privind securizarea datelor contabile. Orice operație de creare, modificare sau ștergere pe înregistrările financiare cheie este înregistrată automat și protejată prin două straturi independente de imuabilitate, atât la nivel ORM cât și direct în baza de date prin trigger PostgreSQL. Auditarea pornește la instalare, fără configurare, și nu acoperă retroactiv înregistrările anterioare.

#### 2. Funcționalități Cheie

- **Pistă de audit imuabilă:** înregistrează automat operațiunile INSERT / UPDATE / DELETE pe `account.move`, `account.move.line`, `account.journal`, `account.account` și `account.tax`; la modificare, câte un eveniment pe fiecare câmp schimbat, cu valoarea veche și cea nouă.
- **Dublu strat de imuabilitate:** la nivel ORM, `write()` și `unlink()` pe înregistrările de audit aruncă `UserError`; la nivel PostgreSQL, triggerul `BEFORE UPDATE/DELETE` blochează inclusiv operațiunile `sudo()`.
- **Hash chain SHA-256:** fiecare înregistrare de audit include hash-ul celei precedente; butonul **Verifică integritatea** din listă reparcurge lanțul și raportează prima intrare coruptă, dacă există.
- **Securizare cu hash pe jurnale:** activează automat `restrict_mode_hash_table` pe toate jurnalele companiilor românești la instalare și blochează dezactivarea ei, cu mesaj explicit de conformitate.
- **Vizualizare read-only** în **Contabilitate → Raportare → Management → Pistă de Audit**, cu filtre după acțiune, model, utilizator, dată, înregistrare sau câmp, grupări și export XLSX/CSV; decorare: verde = creare, galben/portocaliu = modificare, roșu = ștergere.
- **Acces** doar pentru grupul **Cititor Pistă Audit** (`group_audit_reader`), acordat din fișa utilizatorului, secțiunea Contabilitate.
- **Date stocate:** valori vechi și noi, IP-ul sesiunii (operațiile cron se înregistrează pe utilizatorul tehnic, fără IP), snapshot al utilizatorului (rezistent la ștergerea contului) și compania, în configurații multicompanie.
- **Extensibil:** orice model poate fi inclus în pistă prin mixinul `l10n.ro.audit.mixin` și metoda `_l10n_ro_audit_fields()`.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.audit.log`: jurnalul de audit imuabil care stochează operațiunile create / write / unlink pe documentele financiare (model, câmp, valoare veche/nouă, utilizator, IP, dată, hash).
- `l10n.ro.audit.mixin` (mixin Python): permite extinderea auditului la alte modele prin definirea câmpurilor auditate (`_l10n_ro_audit_fields()`).
- `account.move`, `account.move.line`, `account.journal`, `account.account`, `account.tax`: extinse pentru a fi auditate implicit și, în cazul `account.journal`, pentru a bloca dezactivarea hash chain-ului pe jurnalele RO.

**Vizualizări**

- `views/l10n_ro_audit_log_views.xml`: vizualizările pistei de audit (listă read-only cu decorare pe tip de acțiune, formular, filtre).
- `views/menus.xml`: meniul „Pistă de Audit" din secțiunea de raportare contabilă.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: la instalare activează `restrict_mode_hash_table` pe jurnalele companiilor românești și instalează triggerele PostgreSQL `BEFORE UPDATE/DELETE` de protecție a jurnalului de audit.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate în cod/manifest către alte module (dincolo de dependențele directe de mai sus).
