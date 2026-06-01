# Romania - ANAF D100 Declaration (localizat la `l10n_ro_anaf_d100/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d100`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d100
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d100`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Acest modul permite generarea Declarației 100 (Declarația privind obligațiile de plată la bugetul de stat) direct din Odoo Enterprise. Declarația 100 este un document centralizator care raportează scadențele și sumele datorate pentru diverse taxe și impozite, cum ar fi impozitul pe profit, impozitul pe veniturile microîntreprinderilor, accize, redevențe și alte obligații fiscale, conform nomenclatorului ANAF.

#### 2. Funcționalități Cheie

- **Centralizare automată:** colectarea sumelor pentru multiple obligații fiscale dintr-un singur punct.
- **Mapare pe coduri ANAF:** corelarea automată a taxelor din Odoo cu codurile de obligație (ex: 103, 121, 140).
- **Flexibilitate perioadă:** suport pentru raportare lunară sau trimestrială, în funcție de tipul obligației.
- **Export XML nativ:** generarea fișierului XML conform structurii oficiale, gata pentru depunere.
- **Export XDP:** generarea fișierului Adobe XDP pentru import în formularul PDF inteligent ANAF.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- `[[l10n_ro_anaf_base]]`

#### 4. Componente Cheie

**Date / Vizualizări**

- `data/d100_report.xml`: definește raportul D100 și structura de rânduri pe coduri de obligație ANAF.
- `views/d100_xml_export.xml`: butonul și template-ul de export XML (Soft J).
- `views/d100_xdp_export.xml`: butonul și template-ul de export XDP (Soft A).

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) în modul; exportul se declanșează manual din raportul de taxe.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d300]]`
- `[[l10n_ro_anaf_d120]]`
