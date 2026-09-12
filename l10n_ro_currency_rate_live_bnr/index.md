# Romania - Corecție curs valutar BNR (localizat la `l10n_ro_currency_rate_live_bnr/index.md`)

- **Nume Tehnic:** `l10n_ro_currency_rate_live_bnr`
- **Versiune:** `19.0.1.0.0`
- **Cale:** [https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_currency_rate_live_bnr](https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_currency_rate_live_bnr)
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_currency_rate_live_bnr`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Acest modul repară preluarea automată a cursului valutar BNR din Odoo Enterprise. Începând cu 4 august 2026, Banca Națională a României și-a mutat fluxul XML cu cursuri de la `www.bnr.ro` la `curs.bnr.ro`; adresa veche redirecționează acum către pagina principală a băncii și întoarce HTML în loc de XML, ceea ce oprește silențios actualizarea automată a cursului valutar în Odoo. Modulul corectează adresa folosită, astfel încât actualizarea automată să continue să funcționeze fără nicio intervenție a utilizatorului.

#### 2. Funcționalități Cheie

- Suprascrie complet metoda `res.company._parse_bnr_data()` din `currency_rate_live`, folosind noul endpoint `https://curs.bnr.ro/nbrfxrates.xml` (nu poate apela `super()`, fiindcă adresa veche e cablată acolo).
- Structura XML a fluxului BNR nu s-a schimbat, deci logica de parsare rămâne identică celei standard.
- Cursurile sunt salvate cu valabilitate pentru ziua următoare, conform normei metodologice românești privind cursul de schimb valutar.
- Se instalează automat (`auto_install`) atunci când `currency_rate_live` este prezent în bază, fără configurare suplimentară.
- Nu necesită nicio configurare: se folosește fluxul standard — *Contabilitate → Configurare → Setări → Monede*, serviciul **[RO] National Bank of Romania**, cu intervalul dorit și rulare manuală (*Update now*) sau prin acțiunea programată.
- Devine un no-op inofensiv în momentul în care Odoo repară adresa în amonte, în standard.

#### 3. Dependențe

- `currency_rate_live`

#### 4. Componente Cheie

**Modele**

- `res.company`: extins cu suprascrierea metodei `_parse_bnr_data()`, care preia și interpretează fluxul XML de cursuri BNR de la noul endpoint `curs.bnr.ro`.

**Vizualizări**

Modulul nu adaugă vizualizări proprii; folosește ecranele standard de configurare a monedelor din `currency_rate_live`.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește propriile `ir.cron`/`base.automation`; se bazează pe acțiunea programată standard din `currency_rate_live` pentru actualizarea cursurilor.

#### 5. Conexiuni

- `currency_rate_live`: modulul Enterprise pe care îl corectează, prin suprascrierea completă a metodei de preluare a cursului BNR.
