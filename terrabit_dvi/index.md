# Terrabit - DVI (moved to l10n_ro_customs_dvi) (localizat la `terrabit_dvi/index.md`)

- **Nume Tehnic:** `terrabit_dvi`
- **Versiune:** `19.0.1.3.0`
- **Cale:** `https://github.com/dhongu/l10n-romania/tree/19.0/terrabit_dvi`
- **Cale Locală:** `odoo-addons/l10n-romania/terrabit_dvi`
- **Ultima Ingestie:** `2026-09-23`
- **Conținutul s-a mutat la:** [`l10n_ro_customs_dvi`](../l10n_ro_customs_dvi/index.md)

#### 1. Sumar

Modul **tranzitoriu**, fără cod și fără date. Conținutul funcțional — wizardul DVI, repartizarea taxelor vamale în costul stocului și nota de TVA la import — a fost mutat la 23.09.2026 în modulul [`l10n_ro_customs_dvi`](../l10n_ro_customs_dvi/index.md), pentru alinierea la convenția de denumire `l10n_ro_` a repo-ului: era singurul din 39 de module fără acest prefix, deși are categoria Localization și țara RO. Numele `l10n_ro_dvi` nu putea fi folosit, fiind ocupat de modulul OCA cu care se exclude reciproc. Modulul de față declară o singură dependență, către modulul nou, și există exclusiv pentru ca manifestele care îl listează ca dependență să continue să se încarce, fără a fi modificate. Pentru module noi, depindeți direct de `l10n_ro_customs_dvi`.

#### 2. Funcționalități Cheie

- Instalează automat `l10n_ro_customs_dvi`, unde se află întreaga funcționalitate.
- Păstrează compatibilitatea manifestelor existente care declară `terrabit_dvi` ca dependență.
- Nu conține modele, view-uri, acțiuni, meniuri sau reguli de acces proprii.
- Înregistrările istorice din `ir_model_data` sunt preluate automat de modulul nou, printr-un `pre_init_hook`, deci actualizarea nu produce duplicate în interfață.
- **Durata de viață:** până la portarea pe 20.0. Stub-ul **nu se portează**; la portare se actualizează manifestele dependente direct pe modulul nou.

#### 3. Dependențe

- `l10n_ro_customs_dvi`

#### 4. Componente Cheie

Modulul nu conține cod. Singurul său conținut este manifestul, care declară dependența către `l10n_ro_customs_dvi`.

#### 5. Conexiuni

- [`l10n_ro_customs_dvi`](../l10n_ro_customs_dvi/index.md): modulul care a preluat întreaga funcționalitate.
