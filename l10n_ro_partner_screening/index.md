# Partner Screening (localizat la `l10n_ro_partner_screening/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_screening`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_screening
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_screening`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de conformitate fiscală și AML (Anti-Money Laundering) pentru partenerii din Odoo, adaptat cerințelor legislative românești. Marchează partenerii din paradisuri fiscale (HG 1/2024), verifică partenerii față de listele de sancțiuni OFAC și UE și semnalează aplicabilitatea impozitului la sursă pentru nerezidenți. Consolidează rezultatele într-un status de screening cu badge colorat, vizibil pe fișa partenerului și pe facturi.

#### 2. Funcționalități Cheie

- Paradisuri fiscale (HG 1/2024): marcare automată a țărilor necooperante, câmp `l10n_ro_is_tax_haven` pe `res.country` și `res.partner`, cu avertisment pe partener și factură.
- Liste de sancțiuni OFAC și UE: model dedicat `l10n.ro.sanction.entry`, import automat din OFAC SDN List și EU Consolidated Sanctions List.
- Buton "Verifică Sancțiuni" pe fișa partenerului, cu potrivire fuzzy după denumire și banner roșu pe partener și factură când entitatea este sancționată.
- Impozit la Sursă (WHT): câmp `l10n_ro_wht_applicable` sugerat automat pentru nerezidenți, cu avertisment informativ pe factură (D205/D207).
- Status screening calculat `l10n_ro_screening_status` cu priorități sanctioned > tax_haven > wht > ok, afișat ca badge colorat în lista de parteneri și în header-ul formularului.

#### 3. Dependențe

- `base`
- `account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.sanction.entry`: Stochează local entitățile sancționate importate din OFAC și UE.
- `res.partner` (extins): Câmpurile de tax haven, WHT și statusul de screening, plus butonul de verificare sancțiuni.
- `res.country` (extins): Marcajul de paradis fiscal conform HG 1/2024.
- `account.move` (extins): Avertismentele de screening (sancțiuni, paradis fiscal, WHT) pe facturi.

**Vizualizări / Date**

- `views/l10n_ro_sanction_view.xml`, `views/res_partner_view.xml`, `views/res_country_view.xml`, `views/account_move_view.xml`: Interfețele de gestionare a sancțiunilor și afișare a statusului.
- `data/l10n_ro_tax_haven_countries.xml`: Lista țărilor paradis fiscal (HG 1/2024).
- `data/ir_cron.xml`: Cron-ul de import al listelor de sancțiuni.

**Acțiuni Automate / Acțiuni Server**

- Cron import sancțiuni: actualizează periodic listele OFAC SDN și EU Consolidated Sanctions.

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
