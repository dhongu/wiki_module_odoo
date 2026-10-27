# Romania - Declarația D101 ANAF (localizat la `l10n_ro_anaf_d101/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d101`
- **Versiune:** `19.0.1.1.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d101
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d101`
- **Ultima Ingestie:** `2026-10-27`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează Declarația 101 (impozitul pe profit anual) pentru depunerea la ANAF,
pornind de la calculul de impozit pe profit deja existent în modulul `l10n_ro_profit_tax`.
Contabilul nu reintroduce date: alege înregistrarea de calcul anual, apasă un buton și
obține fie fișierul XML validat conform schemei ANAF, gata de import în DUKIntegrator, fie
formularul PDF oficial ANAF completat (XDP), pe care îl verifică, îl semnează și îl depune.

#### 2. Funcționalități Cheie

- Butoane **Export D101 XML** și **Export D101 XDP** pe înregistrarea de calcul impozit pe
  profit (`l10n.ro.profit.tax.compute`), vizibile doar pentru perioada **Anual** și doar
  după postare. Căi: **Contabilitate → Contabilitate → Impozit pe Profit**.
- **XML:** elementul `declaratie101` cu indicatorii principali (P1–P53): venituri și
  cheltuieli totale, profit/pierdere contabilă, cheltuieli nedeductibile, venituri
  neimpozabile, deduceri suplimentare, profit impozabil, pierdere fiscală dedusă, bază
  impozabilă, impozit calculat, credit fiscal sponsorizări, impozit de plată. Se descarcă
  `D101_<CUI>_<an>.xml`.
- **XDP:** aceleași date sunt puse în formularul PDF oficial ANAF
  `D101_XML_2025_091026` (care corectează corelația rd. 43 ≤ 20% × (rd. 41 − rd. 42)).
  Se deschide în Adobe Reader; se verifică în special rândurile 35 (profit impozabil),
  41.1 (impozit) și 52 (de plată), apoi se validează, se semnează și se încarcă pe portalul
  ANAF. Adresa firmei se scrie pe un singur rând, cum cere formularul.
- **Setarea Tip export** (**Contabilitate → Configurare → Setări**, blocul *Declarații ANAF
  România*, din `l10n_ro_anaf_base`): *Arhivă ZIP cu XDP și PDF* (implicit) sau *Descărcare
  directă XDP* (doar fișierul de date).
- Schema folosită este **v10** (OPANAF 206/11.02.2025, `d101_v10.xsd`), structura citită de
  validatorul oficial ANAF J11.0.4; schema publicată încă declară v3. XML-ul este validat
  automat împotriva XSD-ului la export. Verificat cu DUKIntegrator la 26.10.2026.
- **Scadență și număr de evidență a plății:** calculate automat; de la exercițiul 2021
  termenul este **25 iunie a anului următor** (pentru 2021–2025 derogare temporară; de la
  anul fiscal 2026 art. 42 alin. (1) Cod fiscal, modificat prin OUG 8/2026), deci 25.06.2027
  pentru exercițiul 2026. Cazurile cu termen propriu (an fiscal modificat, dizolvare) nu sunt
  tratate: scadența se calculează pentru exercițiul încheiat în decembrie.
- Reutilizează infrastructura ANAF comună din `l10n_ro_anaf_base`: datele declarantului,
  validarea datelor companiei (CUI, adresă, CAEN, județ, persoană de contact) și validarea XML.
- Tipul obligației este tratat intern: câmpul `l10n_ro_d101_cod_obligatie` (102/103/104/105,
  implicit 103 — impozit pe profit, PJ române) există pe model, dar **nu apare în niciun
  view**, deci nu se editează din formular; exportul folosește valoarea implicită.
- Modulul nu generează note contabile (nota de impozit aparține `l10n_ro_profit_tax`).
- **Limitări:** exportul automat acoperă doar scenariul de profit; dacă un indicator ar
  deveni negativ (pierdere fiscală), exportul este blocat cu mesaj explicit, iar declarația se
  completează manual. Maparea pe rânduri este simplificată: totul pe exploatare, rezultat
  financiar 0, ajustările pe câte un singur rând; impozitul iese corect, iar rândurile de
  detaliu se corectează în formularul XDP, dacă e nevoie.

#### 3. Dependențe

- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md)
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md) — aduce câmpul de cod CAEN pe
  partenerul companiei, cerut de `_validate_anaf_export_company(require_caen=True)` la
  generarea declarației.

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute` (extindere, în `models/l10n_ro_profit_tax_compute.py`,
  moștenește și `l10n_ro_anaf.report.handler.mixin`): mapează indicatorii P1–P53 din valorile
  calculate pe înregistrarea de impozit pe profit, calculează scadența și numărul de evidență,
  expune acțiunile `action_export_d101_xml` și `action_export_d101_xdp` și adaugă câmpul
  intern `l10n_ro_d101_cod_obligatie`. Înregistrează profilul D101 (schema v10-J11.0.4, XSD
  `d101_v10.xsd`, PDF `D101_XML_2025_091026.pdf`) în registrul comun de profile ANAF din
  `l10n_ro_anaf_base`.

**Vizualizări**

- `d101_xml_export.xml`: template QWeb pentru XML-ul `declaratie101` (structura v10).
- `d101_xdp_export.xml`: template QWeb pentru datele XDP ale formularului PDF ANAF.
- `l10n_ro_profit_tax_views.xml` (`view_l10n_ro_profit_tax_form_d101`): extinde formularul de
  calcul impozit pe profit cu butoanele Export D101 XML și Export D101 XDP.

**Acțiuni Automate / Acțiuni Server**

Nu există `ir.cron`, `base.automation` sau `ir.actions.server` — exportul se declanșează
manual, prin butoane.

#### 5. Conexiuni

- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declarația D100 (plăți anticipate),
  complementară D101 (anual) — ambele reutilizează infrastructura ANAF comună din
  `l10n_ro_anaf_base`.
