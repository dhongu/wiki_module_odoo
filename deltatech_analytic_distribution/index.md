# Analytic Distribution Enforcer (localizat la `deltatech_analytic_distribution/index.md`)

- **Nume Tehnic:** `deltatech_analytic_distribution`
- **Versiune:** `20.0.0.0.7`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_analytic_distribution
- **Cale Locală:** `odoo-addons/deltatech/deltatech_analytic_distribution`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul impune completarea corectă a distribuției analitice pe facturile de la furnizori. Când validarea este activată, fiecare linie trebuie să aibă distribuția completă pe toate dimensiunile cerute (Locație, Departament, Linie de business), iar procentele trebuie să însumeze exact 100%. Astfel cheltuielile sunt repartizate complet și coerent, fără înregistrări incomplete care ar denatura analiza de costuri.

#### 2. Funcționalități Cheie

- Blochează postarea documentelor de furnizor (facturi, rambursări, bonuri) dacă o linie nu are distribuție analitică.
- Verifică ca procentele distribuției de pe fiecare linie să însumeze exact 100%.
- Cere ca fiecare distribuție să acopere exact cele trei dimensiuni analitice: Locație, Departament și Linie de business.
- Setare specifică fiecărei companii: **Contabilitate > Configurare > Setări**, secțiunea **Vendor Bills**, opțiunea **Enable Analytic Distribution Validation**. În mediu multi-companie, validarea se activează independent pentru fiecare companie.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move`: validarea distribuției analitice la postarea documentelor de furnizor.
- `res.company` și `res.config.settings`: setarea de activare a validării.

**Vizualizări**

- `views/res_config_view.xml`: opțiunea din setările de contabilitate, blocul Vendor Bills.

#### 5. Conexiuni

- Nu au fost identificate conexiuni funcționale cu alte module documentate în wiki.
