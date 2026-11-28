# Romania - Provizioane pentru litigii și riscuri (151) (localizat la `l10n_ro_provisions/index.md`)

- **Nume Tehnic:** `l10n_ro_provisions`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_provisions
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_provisions`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul urmărește provizioanele conform OMFP 1802/2014 pct. 373-381 (conturi 151x). Gestionează dosare de provizion pe tipuri, cu flux de aprobare, ajustare (majorare/diminuare) și soluționare, generând automat nota contabilă la fiecare etapă. Păstrează istoricul modificărilor de estimare și alertează trimestrial pentru revizuirea provizioanelor vechi.

#### 2. Funcționalități Cheie

- Dosare de provizion per tip: litigii (1511), garanții (1512), dezafectare (1513), restructurare (1514), alte (1518); conturile 151x, 6812 și 7812 se completează automat din planul RO.
- Monografie automată: constituire Dr 6812 = Cr 151x; majorare Dr 6812 = Cr 151x (diferență); diminuare Dr 151x = Cr 7812 (diferență); soluționare favorabilă Dr 151x = Cr 7812; soluționare nefavorabilă Dr 151x = Cr 5121 + Cr 7812 (rest).
- Flux de lucru din meniul Contabilitate → Înregistrări → Provizioane Litigii: Aprobă → Actualizează estimare (wizard cu motiv obligatoriu) → Soluționare favorabilă / nefavorabilă (wizard). Detaliile pas-cu-pas sunt în fișa consultant.
- Istoric complet al modificărilor de estimare, cu motivație și referință la nota contabilă.
- Probabilitate de materializare (implicit 50%) cu calcul automat al valorii așteptate.
- Cron trimestrial de alertă pentru revizuirea estimărilor mai vechi de 90 de zile.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `mail`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.provision`: Dosarul de provizion (tip, estimare, probabilitate, stări, note contabile), cu `mail.thread` și activități.
- `l10n.ro.provision.history`: Istoricul modificărilor de estimare.
- `l10n.ro.provision.update.wizard`: Wizard de majorare/diminuare a estimării.
- `l10n.ro.provision.settle.wizard`: Wizard de soluționare (favorabilă/nefavorabilă).

**Vizualizări**

- `views/l10n_ro_provision_view.xml`: Interfața de gestionare a dosarelor de provizion.
- `wizard/l10n_ro_provision_update_wizard_view.xml` și `wizard/l10n_ro_provision_settle_wizard_view.xml`: Wizardele de ajustare și soluționare.

**Acțiuni Automate / Acțiuni Server**

- `cron_provision_review_reminder` (`ir.cron`, „RO: Quarterly Provision Review Alert"): rulează la 3 luni și emite alerte pentru provizioanele cu estimări mai vechi de 90 de zile.

#### 5. Conexiuni

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): închiderea perioadei, în care provizioanele se revizuiesc.
