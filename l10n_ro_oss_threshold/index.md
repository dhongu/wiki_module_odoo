# Prag OSS €10.000 (FR-22) (localizat la `l10n_ro_oss_threshold/index.md`)

- **Nume Tehnic:** `l10n_ro_oss_threshold`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_oss_threshold
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_oss_threshold`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul monitorizează pragul anual de 10.000 EUR pentru vânzările B2C către alte state membre UE, relevant pentru regimul OSS (One Stop Shop). Urmărește cumulat valoarea vânzărilor intracomunitare către consumatori și avertizează compania la apropierea sau depășirea pragului, peste care taxarea trebuie să se facă cu cota TVA din statul de consum. Include un cron de verificare lunară și un wizard de control la cerere.

#### 2. Funcționalități Cheie

- Monitorizarea cumulată a vânzărilor B2C către UE pentru raportare la pragul anual de 10.000 EUR.
- Avertismente pe facturi și la nivel de companie privind apropierea sau depășirea pragului OSS.
- Cron lunar de verificare automată a pragului.
- Wizard de verificare la cerere a situației curente față de prag.
- Configurare a parametrilor OSS în setările companiei și în setările generale de contabilitate.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): Logica de identificare și cumulare a vânzărilor B2C intracomunitare relevante pentru OSS, cu avertismente pe factură.
- `res.company` (extins): Stochează configurarea și starea curentă față de pragul OSS.
- `res.config.settings` (extins): Interfața de configurare a parametrilor OSS.
- `l10n.ro.oss.check` (wizard): Verifică la cerere situația companiei față de pragul de 10.000 EUR.

**Vizualizări / Date**

- `views/account_move_views.xml`: Afișarea avertismentelor OSS pe facturi.
- `views/res_company_views.xml` și `views/res_config_settings_views.xml`: Configurarea pragului și a stării OSS.
- `wizard/l10n_ro_oss_check_views.xml`: Interfața wizardului de verificare.
- `data/cron_data.xml`: Definește cron-ul lunar de verificare a pragului.

**Acțiuni Automate / Acțiuni Server**

- "RO: Verificare prag OSS €10.000 (lunar)": cron care recalculează cumulul vânzărilor B2C UE și actualizează starea față de prag.

#### 5. Conexiuni

- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): declarația specială OSS în România.
- `l10n_eu_oss` / `l10n_eu_oss_reports`: aplicarea efectivă a cotelor OSS și raportarea.
