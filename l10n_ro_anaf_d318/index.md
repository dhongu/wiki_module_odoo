# Romania - ANAF D318 Declaration (localizat la `l10n_ro_anaf_d318/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d318`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d318
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d318`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul permite generarea Declarației 318 (Cerere de rambursare a TVA de către persoanele impozabile stabilite în România, depusă în alt stat membru UE) direct din Odoo Enterprise. Modulul este esențial pentru companiile românești care efectuează achiziții în alte state membre UE (combustibil, transport, cazare etc.) și doresc să recupereze TVA-ul plătit local în acele țări, conform procedurii stabilite prin Directiva 2008/9/CE.

#### 2. Funcționalități Cheie

- **Categorisire automată:** maparea cheltuielilor pe codurile standard ANAF (1-10) pentru o raportare corectă.
- **Filtrare inteligentă:** identificarea facturilor de furnizor din UE care conțin TVA plătit în statul respectiv.
- **Integrare nativă:** export XML direct din interfața de raportare fiscală Odoo, gata pentru validare și depunere.
- **Gestionare Pro-rata:** posibilitatea de a aplica procentul de deducere specific fiecărei cereri de rambursare.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`

#### 4. Componente Cheie

**Modele / Vizualizări**

*Modulul nu conține fișiere `data`; logica este implementată în handlerul de raport din `models/` care extinde infrastructura de raportare fiscală Odoo.*

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raportul de taxe.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d300]]`
- `[[l10n_ro_anaf_d398]]`
