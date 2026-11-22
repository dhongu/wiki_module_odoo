# Romania - Pistă de audit imuabilă (FR-14) (localizat la `l10n_ro_audit_immutable/index.md`)

- **Nume Tehnic:** `l10n_ro_audit_immutable`
- **Versiune:** `19.0.1.2.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_audit_immutable
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_audit_immutable`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul implementează o pistă de audit imuabilă pentru documentele contabile și susține respectarea OMFP 2634/2015, anexa 1, pct. 58 lit. d) și h): fără inserări sau ștergeri ulterioare în lista cronologică a operațiunilor și fără modificări într-o perioadă închisă. Orice operație de creare, modificare sau ștergere pe înregistrările financiare cheie este înregistrată automat și protejată prin două straturi independente de imuabilitate, la nivel ORM și direct în baza de date prin triggere PostgreSQL, iar un lanț de hash SHA-256 permite verificarea integrității pistei.

#### 2. Funcționalități Cheie

- **Pistă de audit imuabilă:** înregistrează automat operațiunile INSERT / UPDATE / DELETE pe `account.move`, `account.move.line`, `account.journal`, `account.account` și `account.tax`; la creare și ștergere se scrie un eveniment pe document, la modificare câte unul pentru fiecare câmp schimbat, cu valoarea veche și cea nouă. Auditarea pornește la instalare și nu acoperă retroactiv înregistrările anterioare; operațiile din cron se înregistrează pe utilizatorul tehnic, fără IP.
- **Câmpuri auditate implicit:** `account.move` (name, date, state, journal_id, partner_id, amount_total, payment_state, ref), `account.move.line` (account_id, partner_id, debit, credit, name, date), `account.journal` (name, code, type, currency_id, default_account_id, restrict_mode_hash_table), `account.account` (name, code, account_type, deprecated, reconcile), `account.tax` (name, amount, amount_type, active). Se stochează și IP-ul sesiunii și un snapshot al utilizatorului (rezistent la ștergerea contului).
- **Dublu strat de imuabilitate:** la nivel ORM, `write()` și `unlink()` pe `l10n.ro.audit.log` aruncă `UserError`; la nivel PostgreSQL, triggerele `BEFORE UPDATE/DELETE` blochează inclusiv operațiunile `sudo()`.
- **Hash chain SHA-256 al pistei:** fiecare firmă are lanțul ei, numerotat fără goluri și calculat imediat după salvare (cron de siguranță la 5 minute pentru intrările rămase neînlănțuite). Butonul **Verifică integritatea** din lista pistei reparcurge lanțul și afișează o notificare verde (lanț inviolat) sau roșie, cu prima intrare coruptă. Intrările create înainte de 19.0.1.2.0 rămân în lanțul vechi, comun firmelor.
- **Hash chain pe jurnale:** `restrict_mode_hash_table = True` se activează automat pe toate jurnalele companiilor românești la instalare și pe jurnalele create ulterior; dezactivarea este blocată pe jurnalele RO, cu mesaj explicit de conformitate. Starea se vede în **Contabilitate → Configurare → Jurnale**, coloana **Secvență Blocată**.
- **Vizualizare read-only** în **Contabilitate → Raportare → Management → Pistă de Audit**, vizibilă doar grupului **Cititor Pistă Audit** (`group_audit_reader`, acordat din fișa utilizatorului, secțiunea Contabilitate). Filtre după utilizator, model, înregistrare, câmp, acțiune și dată, grupări și export XLSX/CSV; decorare vizuală pe tip de acțiune (creare, modificare, ștergere); în configurație multicompanie, fiecare înregistrare poartă compania.
- **Extindere la alte modele:** prin mixinul `l10n.ro.audit.mixin` și metoda `_l10n_ro_audit_fields()`, auditul poate fi extins la modele suplimentare.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.audit.log`: jurnalul de audit imuabil (utilizator, acțiune, model, înregistrare, câmp, valoare veche/nouă, companie, IP, `sequence_number`, `previous_hash`, `secure_hash`); `write`/`unlink` blocate, triggere create în `_auto_init`, înlănțuire după commit și verificarea integrității (`action_l10n_ro_check_integrity`).
- `l10n.ro.audit.mixin` (mixin): interceptează `create`/`write`/`unlink` și scrie evenimentele de audit pe baza câmpurilor din `_l10n_ro_audit_fields()`.
- `account.move`, `account.move.line`, `account.journal`, `account.account`, `account.tax` (extinse cu mixinul): auditate implicit; `account.journal` blochează în plus dezactivarea hash chain-ului pe jurnalele RO și îl activează la creare.

**Vizualizări**

- `l10n_ro_audit_log_view_list` / `l10n_ro_audit_log_view_search` / `l10n_ro_audit_log_view_form`: lista read-only (cu butonul **Verifică integritatea**), căutarea cu filtre și fișa evenimentului, cu hash-ul de integritate.
- `menu_l10n_ro_audit_log` („Audit Trail”): meniul din Contabilitate → Raportare → Management.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_l10n_ro_audit_chain_pending` („Audit trail: chain pending entries”): rulează la 5 minute `model._cron_l10n_ro_chain_pending()` și înlănțuie intrările rămase fără număr de secvență și hash.
- `post_init_hook`: la instalare activează `restrict_mode_hash_table` pe jurnalele companiilor românești.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate în cod/manifest către alte module (dincolo de dependențele directe de mai sus).
