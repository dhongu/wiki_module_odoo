# Romania - Corecție la instalarea SAF-T (localizat la `l10n_ro_saft_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_fix`
- **Versiune:** `19.0.2.3.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_fix](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_fix)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_fix`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Acest modul corectează două probleme din `l10n_ro_saft`. Prima: previne eroarea de instalare care apare pe bazele de date la care planul de conturi românesc a fost încărcat înainte ca o taxă nouă să fi fost adăugată în `l10n_ro` (de exemplu cele trei taxe „9% Art. 3" introduse odată cu reforma TVA din 2025) — fără el, instalarea lui `l10n_ro_saft` (sau a unui modul dependent, precum `l10n_ro_fixed_assets`) eșuează cu „Missing required value for the field 'Nume taxa' (name)". A doua: corectează codurile SAF-T `TaxCode` greșite ale unor taxe, care ajungeau în declarația D406. Este un fix temporar, de eliminat odată ce Odoo repară `l10n_ro_saft`.

#### 2. Funcționalități Cheie

- Restrânge `account.chart.template._load_data()` astfel încât payload-urile parțiale de `account.tax` (doar `id`, `l10n_ro_saft_tax_type_id`, `l10n_ro_saft_tax_code`) să actualizeze doar taxe deja existente, nu să mai creeze taxe fără nume.
- Referințele de taxă lipsă pe companie sunt sărite, nu create, cu un avertisment în jurnalul serverului: `l10n_ro_saft_fix: N taxe sărite pentru compania ... : <xmlid1>, ...`. Dacă taxele sărite sunt totuși necesare (ex. cota tranzitorie de 9%, art. III), se încarcă mai întâi din planul de conturi românesc, apoi se face upgrade la `l10n_ro_saft`.
- Achiziții interne cu TVA deductibil (`tvad_*`, cotele 21/11/19/9/5%, bunuri și servicii; D300 rd. 24/25/26): `l10n_ro_saft` le mapează pe familia 3001xx, rezervată în nomenclatorul ANAF achizițiilor intracomunitare cu taxare inversă. Codul corect e din familia 3011xx (ex. 21%: 300104 → 301104). Validatorul ANAF (DUK) nu prinde eroarea, fiindcă verifică doar existența codului.
- Taxe de 0% mapate pe coduri inexistente în nomenclator (ajung în D406 din `l10n_ro_saft_export_fix`, care raportează liniile de 0% cu codul taxei): `tvatine` (livrări neimpozabile) 308324 → 310324 (L24); `tvati_intrap0s` (servicii intracomunitare 0%) 300303 → 308303 (A34_100, rd. 30.1).
- Export de bunuri `tvati_extra` („0% EX G", D300 rd. 14): codul 310304 (L4, rd. 3) devine 310313 (L13, exporturi, rd. 14), deoarece exportul e scutit cu drept de deducere.
- Corecția se aplică la încărcarea datelor `l10n_ro_saft` (instalări noi), prin `post_init_hook` și prin migrările de upgrade pentru bazele unde modulul era deja instalat. Nu necesită configurare; se instalează înaintea lui `l10n_ro_saft` sau a oricărui modul dependent de el.
- D406 deja depuse nu se modifică. Pentru perioadele raportate cu codurile greșite, verificați cu contabilul dacă e nevoie de D406 rectificativă, mai ales la perioade cu cerere de rambursare TVA sau achiziții intracomunitare reale.
- Creările legitime (payload complet, cu `name`) trec neatinse către comportamentul standard.

#### 3. Dependențe

- `l10n_ro`

Notă intenționată: modulul **nu** declară `l10n_ro_saft` ca dependență — vezi Componente Cheie pentru motiv (ordinea de încărcare a modulelor).

#### 4. Componente Cheie

**Modele**

- `account.chart.template` (extindere, `AbstractModel`): suprascrie `_load_data()` — aplică dicționarul `TAX_CODE_FIXES` (xml_id taxă → cod ANAF corect) pe payload, apoi pentru payload-uri `account.tax` fără `name` păstrează înregistrarea doar dacă taxa există deja pe companie; altfel o sare și loghează avertisment; restul e delegat către `super()`. `_fix_saft_tax_codes()` aplică aceeași corecție pe taxe existente.

**Hook și migrări**

- `post_init_hook` (`hooks.py`): corectează codurile SAF-T greșite pe taxele existente la instalare.
- `migrations/19.0.2.1.0`, `19.0.2.2.0`, `19.0.2.3.0` (`end-migrate.py`): reapelează corecția la upgrade, deoarece `post_init_hook` rulează doar la instalare. Sunt `end-migrate`, nu `post-migrate`: modulul se încarcă înaintea lui `l10n_ro_saft`, iar câmpul `l10n_ro_saft_tax_code` nu e încă în registry în `post-migrate`.

**Mecanism de ordonare a încărcării**

- Modulul depinde doar de `l10n_ro` (adâncime 11 față de `base`), iar `l10n_ro_saft` are adâncime 13. Odoo încarcă modulele în ordinea `(fază, adâncime, nume)`, deci `l10n_ro_saft_fix` se încarcă înaintea lui `l10n_ro_saft`, exact când trebuie să fie activ override-ul. Un `depends` pe `l10n_ro_saft` ar muta modulul după el și ar anula fix-ul la instalarea care crapă.

#### 5. Conexiuni

- [l10n_ro_fixed_assets](../l10n_ro_fixed_assets/index.md): afectat indirect de aceeași eroare de instalare, întrucât depinde de `l10n_ro_saft`.
- [l10n_ro_saft_export_fix](../l10n_ro_saft_export_fix/index.md): exportul D406 raportează liniile de 0% cu codul taxei, deci codurile corectate aici ajung în fișier.
- `l10n_ro_saft`: modulul standard ale cărui coduri și al cărui `_load_data` sunt corectate; nu are pagină wiki proprie.
