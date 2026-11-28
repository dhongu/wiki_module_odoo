# Romania - Validare fiscală

- **Nume Tehnic:** `l10n_ro_fiscal_validation`
- **Versiune:** `20.0.0.4.1`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_fiscal_validation
- **Cale Locală:** odoo-addons/l10n-romania-oca/l10n_ro_fiscal_validation
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul actualizează în masă datele partenerilor (firme) din serviciul web ANAF: denumire, adresă, statut de plătitor de TVA și altele. Un cron zilnic menține partenerii la zi fără intervenție manuală.

#### 2. Funcționalități Cheie

- Cron zilnic „Update Romania Partner VAT Subjected” care sincronizează partenerii cu ANAF.
- Cererea către ANAF este asincronă și în bloc: partenerii se împart în loturi (implicit 499 CUI-uri, limita ANAF fiind 500), apoi rezultatul se interoghează după `correlationId`.
- Parametri opționali în `ir.config_parameter` (Setări → Tehnic → Parametri de sistem): `l10n_ro_fiscal_validation.anaf_bulk_url`, `anaf_corr` (trebuie să conțină un singur `%s`), `anaf_bulk_number` (maxim 499).
- Cheia API ANAF (`l10n_ro_partner_create_by_vat.anaf_api_key`) și numele antetului HTTP (`anaf_api_key_header_tag`, implicit `x-api-key`) sunt partajate cu `l10n_ro_partner_create_by_vat`; fără cheie, cererea merge neautentificată.
- Fișier de exemplu pentru import: `examples/res.partner.csv`.

#### 3. Dependențe

- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md)
- [l10n_ro_vat_on_payment](../l10n_ro_vat_on_payment/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner`: metodele `update_l10n_ro_vat_subjected`, `update_l10n_ro_vat_subjected_all` și `_update_l10n_ro_vat_subjected_all` pentru sincronizarea cu ANAF.

**Vizualizări**

- Nu are vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_res_partner_vat_subjected_update_every_day`: rulează zilnic `model._update_l10n_ro_vat_subjected_all()`.

#### 5. Conexiuni

- [l10n_ro_partner_create_by_vat](../l10n_ro_partner_create_by_vat/index.md): partajează cheia API ANAF.
- [l10n_ro_vat_on_payment](../l10n_ro_vat_on_payment/index.md): TVA la încasare, actualizat din datele ANAF.
