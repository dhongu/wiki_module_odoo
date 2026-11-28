# Romania - Declarația D101 ANAF (localizat la `l10n_ro_anaf_d101/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d101`
- **Versiune:** `20.0.1.2.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_anaf_d101
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d101`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul generează fișierul XML (sau XDP) al **Declarației 101** (impozitul pe profit anual) pentru depunerea la ANAF, pornind de la calculul existent din modulul [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md). Contabilul nu reintroduce date: alege calculul anual, apasă un buton și obține XML-ul validat conform schemei oficiale ANAF, gata de import în DUKIntegrator.

#### 2. Funcționalități Cheie

- Butoanele **Export D101 XML** și **Export D101 XDP** pe calculul de impozit pe profit (*Contabilitate → Contabilitate → Impozit pe Profit*), vizibile doar pentru perioada **Anual** și doar după postare.
- Declarația (`declaratie101`, indicatorii P1–P53) conține venituri și cheltuieli, profit/pierdere contabilă, cheltuieli nedeductibile, venituri neimpozabile, deduceri suplimentare, profit impozabil, pierdere fiscală dedusă, bază impozabilă, impozit calculat, credit de sponsorizări și impozit de plată; sumele se rotunjesc la leu.
- XML-ul respectă schema ANAF **v10** (OPANAF 206/11.02.2025, `d101_v10.xsd`) și este validat automat față de XSD la export; numărul de evidență a plății și scadența sunt calculate automat. Verificat cu DUKIntegrator (soft J 11.0.4) la 26.10.2026.
- **Export XDP:** completează formularul PDF oficial ANAF (D101_XML_2025_091026). Opțiunea **Tip export** din *Setări → Declarații ANAF România* alege între PDF cu datele incluse (implicit), arhivă ZIP cu XDP și PDF sau descărcare directă XDP.
- Câmpul **Tip impozit D101** (grupul Configurare, calcul anual): 102 plăți anticipate (societăți bancare), 103 impozit pe profit PJ române (implicit), 104 agricultori/ONG, 105 PJ străine; se poate schimba și după postare.
- Reutilizează infrastructura `l10n_ro_anaf_base`: datele declarantului, validarea datelor companiei (CUI, adresă, cod CAEN, județ, persoană de contact) și validarea XML.
- Nu generează note contabile: nota de impozit aparține modulului de calcul al impozitului pe profit.
- **Limitare:** exportul acoperă scenariul de profit; pentru exerciții cu pierdere fiscală declarația se completează manual.

#### 3. Dependențe

- [l10n_ro_profit_tax](../l10n_ro_profit_tax/index.md)
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_anaf_partner](../l10n_ro_anaf_partner/index.md): aduce câmpul de cod CAEN al companiei, cerut la validarea exportului.

#### 4. Componente Cheie

**Modele**

- `l10n.ro.profit.tax.compute` (extins, moștenește și `l10n_ro_anaf.report.handler.mixin`): adaugă tipul de impozit D101, mapează indicatorii P1–P53 din valorile calculate și implementează exporturile XML și XDP.

**Vizualizări**

- `d101_xml_export.xml` și `d101_xdp_export.xml`: acțiunile/butoanele de export XML și XDP.
- `l10n_ro_profit_tax_views.xml`: extensia formularului de calcul cu butoanele de export și câmpul Tip impozit D101.

**Acțiuni Automate / Acțiuni Server**

Nu au fost identificate `ir.cron`, `base.automation` sau `ir.actions.server`; exportul se declanșează manual, prin buton.

#### 5. Conexiuni

- [l10n_ro_anaf_d100](../l10n_ro_anaf_d100/index.md): declarația D100 (obligații lunare/trimestriale), complementară D101; ambele reutilizează infrastructura ANAF comună.
