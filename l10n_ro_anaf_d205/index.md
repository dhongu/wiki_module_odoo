# Romania - ANAF Declarația 205 (WHT PF Nerezidente) (localizat la `l10n_ro_anaf_d205/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d205`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d205
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d205`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Acest modul generează Declarația informativă 205 privind impozitul reținut la sursă pe veniturile plătite persoanelor fizice nerezidente (art. 221-226 Cod Fiscal). Fișierul XML este validat față de schema XSD ANAF `d205_2025_v3.xsd` (namespace v2) și este gata de depunere în Soft J ANAF.

#### 2. Funcționalități Cheie

- **Import automat** din contul 446x pentru parteneri PF cu flag WHT activ.
- **Grupare automată** pe tipuri de venit (sect_II) conform XSD.
- **Validare XML** față de schema XSD ANAF înainte de export.
- **Export fișier XML** gata de depus în Soft J ANAF.
- **Workflow** draft → confirmată.

#### 3. Dependențe

- `account`
- `l10n_ro`
- `[[l10n_ro_anaf_base]]`
- `l10n_ro_partner_screening`

#### 4. Componente Cheie

**Vizualizări / Securitate**

- `views/l10n_ro_anaf_d205_view.xml`: formularele și listele pentru gestionarea declarației D205.
- `security/ir.model.access.csv`: drepturile de acces pentru entitățile D205.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul și exportul se declanșează manual.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d207]]`
- `[[l10n_ro_anaf_d107]]`
