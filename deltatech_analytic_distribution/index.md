# Analytic Distribution Enforcer (localizat la `deltatech_analytic_distribution/index.md`)

- **Nume Tehnic:** `deltatech_analytic_distribution`
- **Versiune:** `19.0.0.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_analytic_distribution
- **Cale Locală:** odoo-addons/deltatech/deltatech_analytic_distribution
- **Ultima Ingestie:** `2026-10-30`

#### 1. Sumar

Modulul blochează postarea facturilor de la furnizori până când fiecare linie are distribuția analitică completă. Când validarea este activată pentru o companie, fiecare linie trebuie să aibă distribuția analitică completată cu toate cele trei dimensiuni cerute (Locație, Departament, Linie de business), iar procentele să însumeze exact 100%. Astfel cheltuielile sunt repartizate complet și coerent, iar înregistrările incomplete nu mai denaturează analiza de costuri.

#### 2. Funcționalități Cheie

- Blochează postarea facturilor de furnizor, a notelor de credit furnizor și a bonurilor de achiziție (`in_invoice`, `in_refund`, `in_receipt`) dacă o linie nu are distribuție analitică.
- Verifică ca procentele distribuției de pe fiecare linie să însumeze exact 100%.
- Cere ca fiecare intrare de distribuție să acopere exact trei dimensiuni analitice: Locație, Departament și Linie de business.
- Setare specifică companiei: se activează din **Contabilitate → Configurare → Setări**, în blocul **Vendor Bills** (Facturi furnizori), cu bifa **Enable Analytic Distribution Validation**, independent pentru fiecare companie dintr-un mediu multi-company.
- Validarea urmează compania facturii, nu compania curentă a utilizatorului, inclusiv când se postează în lot facturi din companii diferite; alte tipuri de documente din același lot se postează fără verificare.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): `action_post()` validează fiecare factură de furnizor din selecție pe liniile de factură — distribuție prezentă, trei dimensiuni pe fiecare intrare, total 100%.
- `res.config.settings` (extins): câmpul `analytic_distribution_validation_enabled`, legat de câmpul companiei (`res.company`), cu eticheta „Enable Analytic Distribution Validation".
- `res.company` (extins): stochează comutatorul de validare, per companie.

**Vizualizări**

- `views/res_config_view.xml`: bifa de activare în setările de contabilitate, blocul Vendor Bills.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; validarea rulează la postarea facturii.

#### 5. Conexiuni

- `account`: modulul extinde postarea nativă a facturilor de furnizor și distribuția analitică a liniilor.
