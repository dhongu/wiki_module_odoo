# Provizioane Litigii și Riscuri (151) (localizat la `l10n_ro_provisions/index.md`)

- **Nume Tehnic:** `l10n_ro_provisions`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_provisions
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_provisions`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul urmărește provizioanele pentru litigii și riscuri (conturi 151x) conform OMFP 1802/2014 pct. 373-381. Gestionează dosare de provizion pe tipuri, cu workflow de constituire, ajustare (majorare/diminuare) și soluționare, generând automat monografia contabilă la fiecare etapă. Păstrează istoricul modificărilor de estimare și include un cron trimestrial de alertă pentru revizuirea provizioanelor vechi.

#### 2. Funcționalități Cheie

- Dosare de provizion per tip: litigii (1511), garanții (1512), dezafectare (1513), restructurare (1514), alte (1518).
- Monografie automată la fiecare etapă: constituire Dr 6812 = Cr 151x; majorare Dr 6812 = Cr 151x (diferență); diminuare Dr 151x = Cr 7812 (diferență); soluționare favorabilă Dr 151x = Cr 7812; soluționare nefavorabilă Dr 151x = Cr 5121 + Cr 7812 (rest).
- Istoric complet al modificărilor de estimare, cu motivație și referință la nota contabilă.
- Probabilitate de materializare cu calcul automat al valorii așteptate.
- Cron trimestrial de alertă pentru revizuirea estimărilor mai vechi de 90 de zile.

#### 3. Dependențe

- `account`
- `[[l10n_ro]]`
- `mail`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.provision`: Dosarul de provizion cu tipul, estimarea, probabilitatea, istoricul și generarea monografiei contabile.
- Wizard de actualizare (majorare/diminuare) și wizard de soluționare a provizionului.

**Vizualizări / Date**

- `views/l10n_ro_provision_view.xml`: Interfața de gestionare a dosarelor de provizion.
- `wizard/l10n_ro_provision_update_wizard_view.xml` și `wizard/l10n_ro_provision_settle_wizard_view.xml`: Wizardele de ajustare și soluționare.
- `data/ir_cron.xml`: Cron-ul trimestrial de alertă.
- `security/ir.model.access.csv`: Drepturile de acces.

**Acțiuni Automate / Acțiuni Server**

- Cron trimestrial de revizuire: emite alerte pentru provizioanele cu estimări mai vechi de 90 de zile.

#### 5. Conexiuni

- `[[l10n_ro_period_close_enhanced]]`
