# Romania - D101 ANAF Declaration (localizat la `l10n_ro_anaf_d101/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d101`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d101
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d101`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează fișierul XML al Declarației 101 (impozitul pe profit anual) pentru
depunerea la ANAF, pornind de la calculul de impozit pe profit deja existent în modulul
`l10n_ro_profit_tax`. Contabilul nu reintroduce date: alege înregistrarea de calcul
anual, apasă un buton și obține direct XML-ul validat conform schemei oficiale ANAF,
gata de import în DUKIntegrator.

#### 2. Funcționalități Cheie

- Buton **Export D101 XML** pe înregistrarea de calcul impozit pe profit
  (`l10n.ro.profit.tax.compute`), vizibil doar pentru perioada **Anual** și doar după
  postare.
- Generează elementul `declaratie101` cu indicatorii principali (P1–P53): venituri și
  cheltuieli totale, profit/pierdere contabilă, cheltuieli nedeductibile, venituri
  neimpozabile, deduceri suplimentare, profit impozabil, pierdere fiscală dedusă, bază
  impozabilă, impozit calculat, credit fiscal sponsorizări, impozit de plată.
- XML-ul respectă schema oficială ANAF **v3** (OPANAF 206/11.02.2025) și este validat
  automat împotriva XSD-ului la export.
- Calculează automat numărul de evidență a plății și scadența, conform structurii ANAF.
- Reutilizează infrastructura ANAF comună din `l10n_ro_anaf_base`: datele declarantului,
  validarea datelor companiei (CUI, adresă, CAEN, județ) și validarea XML împotriva
  schemei.
- Câmp **Tip obligație D101** pe înregistrarea de calcul (coduri 102/103/104/105,
  implicit 103 — Impozit pe profit, PJ române).
- **Limitare:** exportul automat acoperă doar scenariul de profit. Pentru exerciții cu
  pierdere fiscală (indicatori care ar deveni negativi), declarația se completează
  manual.

#### 3. Dependențe

- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md)
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md) — nouă în `19.0.1.0.1`; aduce
  câmpul de cod CAEN pe partenerul companiei, cerut de
  `_validate_anaf_export_company(require_caen=True)` la generarea declarației. Fără el,
  câmpul nu exista deloc pe partener.

#### 4. Componente Cheie

*(secțiune neanalizată din cod — `readme/DESCRIPTION.md` acoperă Sumarul și
Funcționalitățile Cheie; componentele tehnice reies indirect din fișiere)*

**Modele**

- `l10n.ro.profit.tax.compute` (extindere, în `models/l10n_ro_profit_tax_compute.py`,
  moștenește și `l10n_ro_anaf.report.handler.mixin`): adaugă câmpul de tip obligație
  D101, mapează indicatorii P1–P53 din valorile deja calculate pe înregistrarea de
  impozit pe profit și expune logica/butonul de export al XML-ului declarației.
  Înregistrează profilul de declarație D101 (cod `D101_A600`, schema v3-20250211) în
  registrul comun de profile ANAF din `l10n_ro_anaf_base`.

**Vizualizări**

- `d101_xml_export.xml`: acțiune/buton pentru exportul declarației D101 XML.
- `l10n_ro_profit_tax_views.xml`: extensia formularului de calcul impozit pe profit cu
  butonul de export și câmpul Tip obligație D101.

**Acțiuni Automate / Acțiuni Server**

Nu au fost identificate `ir.cron`, `base.automation` sau `ir.actions.server` în modul —
exportul se declanșează manual, prin buton, pe cerere.

#### 5. Conexiuni

- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declarația trimestrială D100
  (plăți anticipate), complementară D101 (anual) — ambele reutilizează infrastructura
  ANAF comună din `l10n_ro_anaf_base`.
</content>
</invoke>
