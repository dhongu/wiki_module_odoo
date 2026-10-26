# Romania - Cont de manoperă în producție (localizat la `l10n_ro_mrp_labour_account/index.md`)

- **Nume Tehnic:** `l10n_ro_mrp_labour_account`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_mrp_labour_account
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_mrp_labour_account`
- **Ultima Ingestie:** `2026-10-26`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul configurează conturile contabile pentru manopera de producție conform OMFP 1802/2014, astfel încât mecanismul standard Odoo 19 (`mrp_account._post_labour()`) să genereze corect nota de cost al manoperei la finalizarea comenzilor de producție. La instalare detectează și setează contul 331 pe locația de producție și expune conturile utilizate în Setări, asigurând conformitatea evidenței costurilor de producție în context românesc.

#### 2. Funcționalități Cheie

- `post_init_hook`: la instalare detectează contul 331 din planul de conturi RO și îl setează automat ca `valuation_account_id` pe locația de producție, pentru companiile cu țara România, dacă nu era deja configurat. Dacă planul de conturi nu include 331, nu setează nimic și contul se configurează manual.
- Câmpuri pe companie cu referințe la conturile de manoperă, vizibile în **Setări → Contabilitate → Manoperă Producție (OMFP 1802)**, secțiune afișată doar pentru companiile cu țara România:
  - *Cont locație producție (Cr)*, recomandat `331`: contul creditat de `_post_labour()`;
  - *Cont cheltuieli manoperă implicit (Dr)*, recomandat `921` (cheltuieli directe) sau `923` (indirecte): propus la crearea unui centru de lucru nou, fără a suprascrie centrele existente.
- Sincronizare: modificarea contului de locație producție în Setări actualizează automat `valuation_account_id` pe locația de stoc de tip producție a companiei.
- Suport pentru monografia standard Odoo 19: Dr cont cheltuieli workcenter (921/923) = Cr cont evaluare locație producție (331); valoarea = ore efectuate × cost pe oră al centrului de lucru. Fără cost pe oră configurat, nota ajunge la 0 RON.
- Fiecare centru de lucru poate avea propriul cont de cheltuieli (**Producție → Configurare → Centre de lucru → fila „Contabilitate"**); dacă e gol, se folosește contul implicit de pe companie.
- Integrare cu [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md): notele generate de `_post_labour()` intră în `wip_move_ids` ale comenzii de producție și sunt incluse în închiderea WIP lunară.

#### 3. Dependențe

- `mrp_account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): câmpurile `l10n_ro_mrp_labour_expense_account_id` (cont cheltuieli manoperă implicit) și `l10n_ro_mrp_production_valuation_account_id` (cont evaluare locație producție).
- `res.config.settings` (extins): expune cele două conturi în Setări și sincronizează contul de evaluare cu locația de producție (`action_sync_production_location_account`, declanșată la onchange).

**Vizualizări**

- `views/res_config_settings_views.xml`: secțiunea Manoperă Producție din setările de contabilitate.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: rulează la instalare pentru a seta contul 331 pe locația de producție.

#### 5. Conexiuni

- [l10n_ro_wip_closing](../l10n_ro_wip_closing/index.md): notele de manoperă sunt incluse în închiderea WIP lunară.
