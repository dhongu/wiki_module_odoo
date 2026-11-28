# Romania - Cash Journal Numbering (localizat la `l10n_ro_account_sequence/index.md`)

- **Nume Tehnic:** `l10n_ro_account_sequence`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_account_sequence
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_account_sequence`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Acest modul asigură numerotarea separată a documentelor din jurnalul de casă, în conformitate cu cerințele de evidență din localizarea contabilă pentru România. Pe scurt, documentele de casă primesc o secvență de numerotare distinctă față de alte tipuri de documente, astfel încât registrul de casă să fie corect și ușor de urmărit.

#### 2. Funcționalități Cheie

- Numerotarea separată a documentelor din jurnalul de casă.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

Secțiune omisă: `readme/DESCRIPTION.md` este prezent și nu solicită explicit analiza componentelor tehnice (modele, vizualizări, acțiuni).

#### 5. Conexiuni

- [l10n_ro_cash_register](../l10n_ro_cash_register/index.md): registrul de casă zilnic, care folosește numerotarea separată a jurnalului de casă.
- `account`: modulul extinde fluxul nativ de plăți/încasări pentru a aplica numerotarea separată în jurnalul de casă.
- `l10n_ro`: face parte din ecosistemul de localizare contabilă pentru România.
