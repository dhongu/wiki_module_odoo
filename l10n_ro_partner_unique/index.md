# Romania - Partners Unique (localizat la `l10n_ro_partner_unique/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_unique`
- **Versiune:** `20.0.0.4.1`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_partner_unique
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_partner_unique`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul impune unicitatea partenerilor români pe baza CUI (VAT) și, opțional, a numărului din Registrul Comerțului (NRC), prevenind dublurile de clienți și furnizori.

#### 2. Funcționalități Cheie

- Constrângere la salvare: două companii din aceeași firmă nu pot avea același CUI; comparația ignoră prefixul `RO` și diferențele de majuscule.
- Regula se aplică doar partenerilor românești, companiilor fără companie-părinte, în cadrul aceleiași firme (company_id).
- Parametrul de sistem `l10n_ro_partner_unique.vat_nrc_unique` alege regula: `vat` (implicit, doar CUI) sau `vat_nrc` (CUI împreună cu NRC).
- Mesaj de eroare clar cu perechea (CUI, NRC) duplicată.
- Asistentul standard de îmbinare a partenerilor ocolește constrângerea, pentru ca îmbinarea dublurilor să rămână posibilă.

#### 3. Dependențe

- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `res.partner`: constrângerea `_check_vat_nrc_unique` și domeniul de căutare a dublurilor.
- `base.partner.merge.automatic.wizard`: rulează îmbinarea cu contextul `partner_merge`, care dezactivează verificarea.

**Vizualizări**

- Nu sunt definite.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_config](../l10n_ro_config/index.md): stabilește compania românească (`is_l10n_ro_record`) pentru care se aplică regula.
