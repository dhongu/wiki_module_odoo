# Romania - Declarația D101 ANAF (localizat la `l10n_ro_anaf_d101/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d101`
- **Versiune:** `19.0.1.3.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d101
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d101`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează Declarația 101 (impozitul pe profit anual) pentru depunerea la ANAF,
pornind de la calculul de impozit pe profit deja existent în modulul `l10n_ro_profit_tax`.
Contabilul nu reintroduce date: alege calculul anual postat, apasă un buton și obține fie
fișierul XML validat conform schemei ANAF, gata de import în DUKIntegrator, fie formularul
PDF oficial ANAF completat (XDP), pe care îl verifică, îl semnează și îl depune.

#### 2. Funcționalități Cheie

- Butoane **Export D101 XML** și **Export D101 XDP** pe calculul de impozit pe profit
  (`l10n.ro.profit.tax.compute`), vizibile doar pentru perioada **Anual** și doar după
  postare. Cale: **Contabilitate → Contabilitate → Impozit pe Profit**.
- **XML:** elementul `declaratie101` cu indicatorii P1–P53 (venituri și cheltuieli,
  profit/pierdere contabilă, nedeductibile, neimpozabile, deduceri suplimentare, profit
  impozabil, pierdere dedusă, bază impozabilă, impozit calculat, credit de sponsorizare,
  impozit de plată). Se descarcă `D101_<CUI>_<an>.xml`.
- **Validare:** schema v10 (OPANAF 206/11.02.2025, `d101_v10.xsd`), verificată cu
  validatorul oficial ANAF (DUKIntegrator, J 11.0.4) la 26.10.2026; XML-ul este validat
  automat față de XSD la export, iar erorile apar înainte de descărcare.
- **XDP:** aceleași date completează formularul PDF oficial `D101_XML_2025_091026`. Se
  deschide în Adobe Reader; se verifică rândurile 35 (profit impozabil), 41.1 (impozit) și
  52 (de plată), apoi se validează, se semnează și se încarcă pe portalul ANAF.
- **Setarea Tip export** (**Contabilitate → Configurare → Setări**, blocul *Declarații ANAF
  România*, din `l10n_ro_anaf_base`): *PDF cu datele incluse* (implicit), *Arhivă ZIP cu XDP
  și PDF* sau *Descărcare directă XDP* (doar fișierul de date).
- **Tip impozit D101** (grupul Configurare, vizibil pe perioada Anual): `102` plăți
  anticipate (societăți bancare), `103` impozit pe profit PJ române (implicit), `104`
  agricultori / ONG, `105` PJ străine. Se poate schimba și după postare, fiindcă nu atinge
  nota contabilă.
- **Rânduri completate automat** (sume rotunjite la leu): exploatare (rd. 1–3), financiar
  (rd. 4–6, conturi cu prefixele din setări), rezultat brut (rd. 7), amortizare fiscală
  (rd. 11), deduceri suplimentare (rd. 15; rd. 15.1 cercetare-dezvoltare rămâne manual),
  impozit pe profit (rd. 23), protocol peste 2% (rd. 26), sponsorizare (rd. 27), amortizare
  contabilă (rd. 28), alte nedeductibile (rd. 33, inclusiv partea nedeductibilă la ieșirea
  activelor) și pierderea de recuperat (rd. 39 / 39.1).
- **Pierdere fiscală:** exportul merge; rd. 3, 6, 7, 10, 22, 35 și 38.1 pot fi negative,
  rd. 40.1 ia pierderea anului, iar impozitul și rd. 39.1 sunt 0. Pierderea anului și
  creditul de sponsorizare nefolosit **nu se reportează automat**. La orice alt indicator
  negativ exportul se oprește cu mesaj explicit.
- **Scadență și număr de evidență a plății:** calculate automat; scadența este **25 iunie a
  anului următor** (25.06.2027 pentru exercițiul 2026). Cazurile cu termen propriu (an
  fiscal modificat, dizolvare) nu sunt tratate.
- **Date companie cerute la export** (validate prin `l10n_ro_anaf_base`): CUI, adresă, cod
  CAEN, județ, persoană de contact (nume, prenume, funcție); lipsa lor dă eroare explicită.
- Modulul nu generează note contabile (nota Dr 691 = Cr 4411 aparține `l10n_ro_profit_tax`).
  Fluxul pas-cu-pas este în fișa consultantului.

#### 3. Dependențe

- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md)
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md) — aduce codul CAEN, cerut de
  `_validate_anaf_export_company(require_caen=True)` la generarea declarației.

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute` (extindere, `models/l10n_ro_profit_tax_compute.py`;
  moștenește și `l10n_ro_anaf.report.handler.mixin`): mapează indicatorii P1–P53 din
  valorile calculului, calculează scadența și numărul de evidență, expune
  `action_export_d101_xml` și `action_export_d101_xdp` și adaugă câmpul
  `l10n_ro_d101_cod_obligatie` (Tip impozit D101). Înregistrează profilul D101 (XSD
  `d101_v10.xsd`, PDF `D101_XML_2025_091026.pdf`) în registrul comun de profile ANAF.

**Vizualizări**

- `d101_xml_export.xml`: template QWeb pentru XML-ul `declaratie101` (v10).
- `d101_xdp_export.xml`: template QWeb pentru datele XDP ale formularului PDF ANAF.
- `view_l10n_ro_profit_tax_form_d101` (`l10n_ro_profit_tax_views.xml`): adaugă pe formularul
  de calcul butoanele de export și câmpul Tip impozit D101.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server`; exportul se declanșează
manual, prin butoane.

#### 5. Conexiuni

- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md): sursa calculului anual și modelul extins.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura ANAF comună (declarant, validare companie, validare XSD, descărcare).
