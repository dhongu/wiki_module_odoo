# Romania - Prag OSS 10.000 € (localizat la `l10n_ro_oss_threshold/index.md`)

- **Nume Tehnic:** `l10n_ro_oss_threshold`
- **Versiune:** `19.0.1.0.6`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_oss_threshold
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_oss_threshold
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul monitorizează pragul anual de 10.000 EUR pentru vânzările B2C intracomunitare (bunuri și servicii TBE), peste care firma trebuie să aplice TVA-ul statului de consum și să se înregistreze în regimul OSS (One Stop Shop), conform Directivelor (UE) 2017/2455 și 2019/1995. Este un instrument de avertizare timpurie: cumulează valoarea anuală a vânzărilor și avertizează direct pe factură, și prin activități lunare pe fișa companiei, când pragul se apropie sau este depășit.

#### 2. Funcționalități Cheie

- Cumul anual al vânzărilor B2C intracomunitare, convertit în EUR, calculat din facturile cu poziție fiscală cu aplicare automată (OSS).
- Prag configurabil (implicit 10.000 EUR) și procent de avertizare (implicit 80%, adică 8.000 EUR), setate pe companie.
- Avertizare pe factura către client, la apropierea de prag și la depășirea lui (avertizarea dispare dacă firma este marcată ca înregistrată OSS).
- Status „Înregistrat OSS" pe companie, pentru monitorizare informativă după înregistrarea în regim; decizia de înregistrare și aplicarea TVA-ului statului de consum rămân manuale.
- Sarcină `ir.cron` lunară care creează o activitate de tip Avertizare pe fișa companiei (fără duplicate) pentru companiile din România neînregistrate OSS.
- Verificare la cerere din **Contabilitate → Rapoarte → Verificare Prag OSS**: se aleg compania și anul, iar rezultatul arată vânzările B2C UE (EUR), pragul, procentul și statusul (sub prag, atenție, depășit, înregistrat OSS).
- Configurare în **Contabilitate → Configurare → Setări** (secțiunea OSS — Prag €10.000) și în tab-ul „OSS Prag €10.000" al fișei companiei, vizibile doar pentru companii cu țara România.
- Dacă verificarea returnează 0 EUR, trebuie verificat că `l10n_eu_oss` este instalat și că există poziții fiscale OSS cu aplicare automată.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmp calculat `l10n_ro_oss_threshold_warning` pentru avertizarea afișată pe factură.
- `res.company` (extins): pragul, procentul de avertizare și bifa „Înregistrat OSS"; calculul cumulului anual și al statusului.
- `res.config.settings` (extins): interfața de configurare a parametrilor OSS.
- `l10n.ro.oss.check` (wizard): verifică la cerere situația companiei față de prag.

**Vizualizări**

- `view_move_form_l10n_ro_oss`: avertizarea OSS pe formularul facturii.
- `view_company_form_l10n_ro_oss`: tab-ul OSS pe fișa companiei.
- `res_config_settings_view_form_l10n_ro_oss`: secțiunea OSS din setările de contabilitate.
- `view_l10n_ro_oss_check_form`: dialogul de verificare a pragului.

**Acțiuni Automate / Acțiuni Server**

- `cron_l10n_ro_oss_threshold_check` („RO: Verificare prag OSS €10.000 (lunar)"): rulează lunar și creează o activitate de avertizare pe fișa companiei dacă pragul este aproape sau depășit.

#### 5. Conexiuni

- [l10n_ro_anaf_d398](../l10n_ro_anaf_d398/index.md): declarația OSS se depune cu acest modul.
- `l10n_eu_oss`: poziții fiscale OSS cu aplicare automată, pe baza cărora se calculează cumulul.
