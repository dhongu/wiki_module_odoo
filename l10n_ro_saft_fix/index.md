# Romania - Corecție la instalarea SAF-T (localizat la `l10n_ro_saft_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_fix`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_fix](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_fix)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_fix`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Acest modul previne o eroare de instalare care apare pe baze de date la care planul de conturi românesc a fost încărcat înainte ca o taxă nouă să fi fost adăugată în localizarea `l10n_ro` (de exemplu cele trei taxe „9% Art. 3" introduse odată cu reforma TVA din 2025). Fără el, instalarea modulului `l10n_ro_saft` (sau a oricărui modul care depinde de el, precum `l10n_ro_fixed_assets`) eșuează cu mesajul „Missing required value for the field 'Nume taxa' (name)". Este un fix temporar, de eliminat odată ce Odoo repară `l10n_ro_saft`.

#### 2. Funcționalități Cheie

- Corectează `account.chart.template._load_data()` astfel încât payload-urile parțiale de `account.tax` (doar `id`, `l10n_ro_saft_tax_type_id`, `l10n_ro_saft_tax_code`) să actualizeze doar taxe deja existente, nu să mai creeze taxe fără nume.
- Referințele de taxă lipsă pe companie sunt sărite, nu create — cu un avertisment în jurnalul serverului: `l10n_ro_saft_fix: N taxe sărite pentru compania ... : <xmlid1>, <xmlid2>, ...`.
- Nu necesită nicio configurare; se instalează pur și simplu înaintea lui `l10n_ro_saft` (sau a oricărui modul care depinde de el, ex. `l10n_ro_fixed_assets`).
- Dacă taxele sărite sunt totuși necesare (ex. facturare la cota tranzitorie de 9% conform art. III), se încarcă mai întâi din planul de conturi românesc, apoi se face upgrade la `l10n_ro_saft` ca să se scrie codurile SAF-T pe ele.
- Creările legitime (payload complet, cu `name`) trec neatinse către comportamentul standard — fix-ul e deliberat îngust, limitat la `account.tax`.

#### 3. Dependențe

- `l10n_ro`

Notă intenționată: modulul **nu** declară `l10n_ro_saft` ca dependență, deliberat — vezi Componente Cheie pentru motiv (ordinea de încărcare a modulelor).

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extindere, `AbstractModel`): suprascrie `_load_data()` — pentru payload-uri `account.tax` fără câmpul `name`, creează înregistrarea doar dacă există deja pe companie (identificată prin xml_id); altfel o sare și loghează un avertisment, apoi deleagă restul către `super()`.

**Mecanism de ordonare a încărcării**

- Modulul depinde doar de `l10n_ro` (adâncime 11 față de `base`), în timp ce `l10n_ro_saft` are adâncime 13. Odoo încarcă modulele în ordinea `(fază, adâncime, nume)`, deci `l10n_ro_saft_fix` se instalează înaintea lui `l10n_ro_saft`, exact la timp pentru ca override-ul să fie activ când rulează `post_init_hook`-ul acestuia din urmă. Adăugarea lui `l10n_ro_saft` în `depends` ar muta modulul după el în ordinea de încărcare și ar anula fix-ul.

#### 5. Conexiuni

- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): modul afectat indirect de aceeași eroare de instalare, întrucât depinde de `l10n_ro_saft`.
- `l10n_ro_saft`: modulul standard a cărui logică de `post_init_hook` (`_load_data`) este corectată de acest fix; nu are pagină wiki proprie.
