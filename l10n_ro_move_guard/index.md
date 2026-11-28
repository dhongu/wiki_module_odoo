# Romania - Gărzi la postarea documentelor contabile

- **Nume Tehnic:** `l10n_ro_move_guard`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_move_guard
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_move_guard`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Mecanism comun prin care modulele de localizare românească pot **bloca** (nu doar avertiza) postarea unei facturi sau a unei note contabile. Este un modul de bază, fără ecrane proprii și fără setări, care funcționează și pe Odoo Community. Toate motivele de blocare sunt afișate utilizatorului într-un singur mesaj.

#### 2. Funcționalități Cheie

- Un singur punct de verificare la postare, comun tuturor modulelor, în locul mai multor override-uri pe `_post` care se pot încurca între ele.
- Toate motivele de blocare apar deodată, într-un singur mesaj (dialogul „Operație invalidă”), câte unul pe rând.
- Se aplică doar companiilor cu țara fiscală România; celelalte companii din aceeași bază nu sunt afectate.
- Singur, modulul nu blochează nimic: blocajul vine de la modulele care îl folosesc, fiecare cu propria bifă în setări (opt-in, pe `res.company`).
- Pentru dezvoltatori: un modul depinde de `l10n_ro_move_guard`, suprascrie `_l10n_ro_posting_guard_errors()`, apelează `super()` și adaugă motivele în listă.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): `_post` apelează `_l10n_ro_posting_guard_errors()`, punctul comun care colectează motivele de blocare.

**Vizualizări**

- Nu are vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): blochează facturile de client pe parteneri inactivi sau radiați la ANAF.
- [l10n_ro_anaf_partner_confirm](../l10n_ro_anaf_partner_confirm/index.md): blochează facturile de client pe parteneri cu adresa din ANAF neconfirmată.
- [l10n_ro_payment_instruments](../l10n_ro_payment_instruments/index.md): blochează facturile de client pe parteneri cu cecuri sau bilete la ordin refuzate.
- [l10n_ro_receivables_enhanced](../l10n_ro_receivables_enhanced/index.md): blochează facturile de client care depășesc limita de credit.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): îl instalează automat, ca instalările existente să rămână neschimbate.
