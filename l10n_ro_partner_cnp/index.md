# Romania - CNP partener

- **Nume Tehnic:** `l10n_ro_partner_cnp`
- **Versiune:** `20.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_partner_cnp
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_cnp`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Adaugă pe partener codul numeric personal (CNP) al persoanelor fizice din România și validează cifra de control. Este un modul de bază, fără ecrane proprii, folosit de modulele care declară venituri plătite persoanelor fizice (zilieri, drepturi de autor).

#### 2. Funcționalități Cheie

- Câmpul **CNP** pe partener (date cu caracter personal, vizibil doar utilizatorilor interni).
- Validare la salvare: 13 cifre, prima cifră 1–8 și cifra de control corectă; un CNP greșit este respins cu mesajul „CNP invalid”, nu golit.
- Indicatorul **CNP valid**, stocat, pentru filtre și verificări înainte de declarații.
- Un CNP introdus în codul fiscal al unui partener din România se mută automat în câmpul CNP; `is_company` (calculat de Odoo din codul fiscal) nu mai marchează persoana fizică drept companie, deci e-Factura o tratează B2C, iar un CUI/CIF valid (PFA, II, IF, ONG) o face entitate (B2B).
- Fără meniu propriu: CNP-ul se completează din documentele care îl cer (registrul zilierilor, contractul de drepturi de autor, iar cu `l10n_ro_efactura_consumer` și pe formularul partenerului, sub codul fiscal).
- Câmpul are aceeași definiție ca în `l10n_ro_efactura_consumer`, deci cele două module pot fi instalate împreună fără migrare.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): `l10n_ro_cnp`, `l10n_ro_cnp_valid`, constrângerea de validare și sincronizarea identității din codul fiscal (`_l10n_ro_sync_vat_identity`).

**Vizualizări**

- Nu are vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: mută CNP-urile din codul fiscal în câmpul CNP la instalare; `migrations/20.0.1.1.0` repetă corecția la upgrade.

#### 5. Conexiuni

- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md): e-Factura B2C, cu aceeași definiție a câmpului CNP.
- `l10n_ro_payroll_day_labourers`: zilieri, declarați nominal în D112.
- `l10n_ro_payroll_copyright`: drepturi de proprietate intelectuală, declarate în D112.
