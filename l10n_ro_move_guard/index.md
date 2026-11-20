# Romania - Gărzi la postarea documentelor contabile (localizat la `l10n_ro_move_guard/index.md`)

- **Nume Tehnic:** `l10n_ro_move_guard`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_move_guard
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_move_guard`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul de bază, fără ecrane și fără setări proprii, care oferă un mecanism comun prin care modulele de localizare românească pot **bloca** (nu doar avertiza) postarea unei facturi sau a unei note contabile. Depinde doar de `account`, deci funcționează și pe Odoo Community. Singur nu blochează nimic: blocajul vine de la modulele care îl folosesc, fiecare cu propria bifă în setări.

#### 2. Funcționalități Cheie

- Un singur punct de verificare la postare, comun tuturor modulelor, în locul mai multor override-uri pe `_post` care se pot încurca între ele.
- Toate motivele de blocare apar într-un singur mesaj, câte unul pe rând, ca utilizatorul să le vadă pe toate deodată.
- Se aplică doar companiilor cu țara fiscală România; celelalte companii din aceeași bază nu sunt afectate.
- Se instalează automat odată cu modulele care îl folosesc; nu are meniuri sau ecrane.
- Pentru dezvoltatori: un modul dependent suprascrie `_l10n_ro_posting_guard_errors()`, apelează `super()` și adaugă motivele în listă; blocajul trebuie să fie opt-in, condiționat de o bifă pe `res.company`, ca instalările existente să rămână neschimbate.
- Consumatori: blocarea facturilor de client pe parteneri inactivi/radiați la ANAF, pe parteneri cu adresă ANAF neconfirmată, pe parteneri cu cecuri sau bilete la ordin refuzate și pe parteneri care depășesc limita de credit.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): `_l10n_ro_posting_guard_errors()` este hook-ul extensibil, care întoarce o listă goală (postare permisă); `_post()` îl apelează pentru mișcările companiilor cu țara fiscală RO și, dacă lista nu e goală, ridică `UserError` cu toate motivele.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

Module care folosesc hook-ul, conform descrierii modulului:

- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): blochează facturile de client pe parteneri inactivi sau radiați la ANAF.
- [l10n_ro_anaf_partner_confirm](../l10n_ro_anaf_partner_confirm/index.md): blochează facturile de client pe parteneri cu adresa din ANAF neconfirmată.
- [l10n_ro_payment_instruments](../l10n_ro_payment_instruments/index.md): blochează facturile de client pe parteneri cu cecuri sau bilete la ordin refuzate.
- [l10n_ro_receivables_enhanced](../l10n_ro_receivables_enhanced/index.md): blochează facturile de client care depășesc limita de credit.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): îl instalează automat, ca instalările existente să rămână neschimbate.
