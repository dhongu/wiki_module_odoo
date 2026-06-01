# Romania - ANAF Declarația 107 (Sponsorizări) (localizat la `l10n_ro_anaf_d107/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d107`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d107
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d107`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Acest modul gestionează și exportă Declarația 107 privind sponsorizările și bursele private acordate în cursul exercițiului fiscal, conform art. 25 alin. (4) lit. i din Codul Fiscal. Modulul preia automat sponsorizările din contabilitate, calculează scăzământul de impozit conform formulei legale și generează fișierul XML pentru depunere prin SPV.

#### 2. Funcționalități Cheie

- **Import automat din contabilitate:** preia sponsorizările înregistrate pe conturile 658x grupate pe parteneri, cu sumele debitoare din perioada anului fiscal.
- **Calcul scăzământ** conform formulei legale: `scăzământ = min(total sponsorizări, min(0,75% × CA, 20% × impozit datorat))`.
- **Export XML** în formatul ANAF pentru depunere prin SPV (Soft J).
- **Flux de confirmare:** ciornă → confirmată (blochează modificările după depunere).
- **Cine depune:** contribuabilii plătitori de impozit pe profit sau impozit pe micro-întreprindere care au acordat sponsorizări eligibile.
- **Termen:** anual, odată cu declarația de impozit pe profit (D101) sau până la termenul de depunere a declarației de impozit micro.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `[[l10n_ro_anaf_base]]`

#### 4. Componente Cheie

**Vizualizări / Securitate**

- `views/l10n_ro_anaf_d107_view.xml`: formularele și listele pentru gestionarea declarației D107.
- `security/ir.model.access.csv`: drepturile de acces pentru entitățile D107.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul și exportul se declanșează manual.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d100]]`
- `[[l10n_ro_anaf_d205]]`
- `[[l10n_ro_anaf_d207]]`
