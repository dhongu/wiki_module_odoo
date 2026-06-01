# Romania - ANAF D398 Declaration (VAT OSS) (localizat la `l10n_ro_anaf_d398/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d398`
- **Versiune:** `19.0.0.0.1`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d398
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d398`
- **Ultima Ingestie:** 2026-06-01

#### 1. Sumar

Acest modul permite generarea Declarației Speciale de TVA (D398) direct din Odoo, conform formatului ANAF pentru regimul special One Stop Shop (OSS). Regimul OSS permite raportarea și plata TVA-ului datorat în mai multe state membre UE printr-o singură declarație centralizată, reglementată de Directiva (UE) 2017/2455 și transpusă prin Codul Fiscal. Declarația se întocmește în EURO și se depune trimestrial (UE/Non-UE) sau lunar (Import). Implementarea folosește infrastructura comună din `l10n_ro_anaf_base`.

#### 2. Funcționalități Cheie

- **Conversie automată în EURO** folosind cursul BCE din ultima zi a perioadei fiscale.
- **Grupare pe state membre de consum (MSCON)** a livrărilor de bunuri și prestărilor de servicii.
- **Export XDP (Soft A):** import în formularul PDF inteligent ANAF (versiunea 1.0.11+).
- **Export XML (Soft J):** XML nativ conform schemei XSD oficiale (`d398_20211101.xsd`), validat XSD automat și compatibil DUKIntegrator.
- **Date identificare automate** din configurările Odoo.
- **Distincția între bunuri și servicii** pe fiecare cotă de TVA.
- **Gap-uri rămase:** avertizarea pentru pragul OSS de 10.000 EUR și depunerea automată în portalul ANAF nu sunt încă implementate.

#### 3. Dependențe

- `l10n_ro`
- `account_reports`
- `l10n_eu_oss_reports`
- `[[l10n_ro_anaf_base]]`

#### 4. Componente Cheie

**Date / Vizualizări**

- `data/account_reports.xml`: definiția raportului OSS D398.
- `data/d398_menu.xml`: intrările de meniu.
- `views/report_export_templates.xml`: template-urile de export XML/XDP.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); exportul se declanșează manual din raportul OSS.*

#### 5. Conexiuni

- `[[l10n_ro_anaf_base]]`
- `[[l10n_ro_anaf_d300]]`
- `[[l10n_ro_anaf_d318]]`
