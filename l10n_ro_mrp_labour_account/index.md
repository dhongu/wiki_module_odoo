# Romania - Cont de manoperă în producție (localizat la `l10n_ro_mrp_labour_account/index.md`)

- **Nume Tehnic:** `l10n_ro_mrp_labour_account`
- **Versiune:** `20.0.1.0.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_mrp_labour_account
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_mrp_labour_account`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul configurează conturile contabile pentru manopera de producție conform OMFP 1802/2014, astfel încât mecanismul standard Odoo (`mrp_account._post_labour()`) să genereze corect nota de cost al manoperei la finalizarea comenzilor de producție. La instalare detectează și setează contul 331 pe locația de producție și expune conturile utilizate în Settings, asigurând conformitatea evidenței costurilor de producție în context românesc.

#### 2. Funcționalități Cheie

- `post_init_hook`: la instalare detectează contul 331 din planul de conturi RO și îl setează automat ca `valuation_account_id` pe locația de producție, dacă nu era deja configurat.
- Câmpuri pe companie cu referințe la conturile de manoperă, vizibile în Setări → Contabilitate → Manoperă Producție.
- Sincronizare: modificarea contului de locație producție în Settings actualizează automat `valuation_account_id` pe locația de stoc.
- Nota generată de Odoo la finalizarea comenzii: Dr 331 (contul locației de producție) = Cr contul de cheltuieli al centrului de lucru; valoarea = ore efectuate × cost pe oră. Conturile 921/923 (în afara bilanțului) nu pot fi folosite pe centrul de lucru; tratamentul contabil este în analiză (issue l10n_ro_ent#1359).
- Secțiunea de setări apare doar pentru companiile cu țara România.

#### 3. Dependențe

- `mrp_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): Stochează referințele la conturile de manoperă producție.
- `res.config.settings` (extins): Configurarea conturilor și sincronizarea cu locația de producție.

**Vizualizări / Date**

- `views/res_config_settings_views.xml`: Secțiunea Manoperă Producție din setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: rulează la instalare pentru a seta contul 331 pe locația de producție.

#### 5. Conexiuni

- [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md): închiderea WIP lunară pentru comenzile de producție din aceeași localizare.
