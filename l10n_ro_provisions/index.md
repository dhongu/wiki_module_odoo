# Romania - Provizioane pentru litigii și riscuri (151) (localizat la `l10n_ro_provisions/index.md`)

- **Nume Tehnic:** `l10n_ro_provisions`
- **Versiune:** `19.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_provisions
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_provisions`
- **Ultima Ingestie:** `2026-10-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul urmărește provizioanele pentru litigii și riscuri (conturi 151x) conform OMFP 1802/2014 pct. 373-381. Gestionează dosare de provizion pe tipuri, cu workflow de constituire, ajustare (majorare/diminuare) și soluționare, generând automat monografia contabilă la fiecare etapă. Păstrează istoricul modificărilor de estimare și include un cron trimestrial de alertă pentru revizuirea provizioanelor vechi.

#### 2. Funcționalități Cheie

- Dosare de provizion per tip: litigii (1511), garanții (1512), dezafectare (1513), restructurare (1514), alte (1518). Meniu: **Contabilitate → Înregistrări → Provizioane Litigii** (vizibil pentru grupul Contabilitate / Utilizator; crearea și modificarea cer Contabilitate / Manager).
- La selectarea tipului, conturile 151x, 6812 și 7812 se completează automat din planul de conturi RO al companiei.
- Stări: Ciornă, Aprobat, Actualizat, Soluționat favorabil, Soluționat nefavorabil, Anulat.
- Monografie automată la fiecare etapă: constituire Dr 6812 = Cr 151x; majorare Dr 6812 = Cr 151x (diferență); diminuare Dr 151x = Cr 7812 (diferență); soluționare favorabilă Dr 151x = Cr 7812; soluționare nefavorabilă Dr 151x = Cr cont plată (ex. 5121) pentru suma plătită + Dr 151x = Cr 7812 pentru restul.
- Wizard de actualizare estimare (estimare nouă și motiv obligatoriu) și wizard de soluționare nefavorabilă (suma plătită efectiv și contul de plată).
- Istoric complet al modificărilor de estimare, cu motivație și referință la nota contabilă.
- Probabilitate de materializare (implicit 50%) cu calcul automat al valorii așteptate (estimare × probabilitate / 100).
- Cron trimestrial de alertă (activitate pentru creatorul dosarului) pentru estimări mai vechi de 90 de zile; este instalat inactiv și se activează din Setări → Tehnic → Automatizare → Acțiuni programate.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `mail`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.provision`: dosarul de provizion (cu `mail.thread` și `mail.activity.mixin`), cu tipul, estimarea, probabilitatea, starea, istoricul și generarea monografiei contabile.
- `l10n.ro.provision.history`: istoricul modificărilor de estimare.
- `l10n.ro.provision.update.wizard`: wizard de actualizare (majorare/diminuare).
- `l10n.ro.provision.settle.wizard`: wizard de soluționare nefavorabilă.

**Vizualizări**

- `views/l10n_ro_provision_view.xml`: interfața de gestionare a dosarelor de provizion (listă cu codificare cromatică, formular cu note contabile și istoric).
- `wizard/l10n_ro_provision_update_wizard_view.xml` și `wizard/l10n_ro_provision_settle_wizard_view.xml`: wizardele de ajustare și soluționare.

**Acțiuni Automate / Acțiuni Server**

- `cron_provision_review_reminder` (`data/ir_cron.xml`): rulează la 3 luni `_cron_provision_review_reminder()` și emite alerte pentru provizioanele cu estimări mai vechi de 90 de zile; instalat inactiv.

#### 5. Conexiuni

- [l10n_ro_period_close_enhanced](../l10n_ro_period_close_enhanced/index.md): închiderea de perioadă.
