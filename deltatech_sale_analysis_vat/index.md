# Sale Analysis by VAT (localizat la `deltatech_sale_analysis_vat/index.md`)

- **Nume Tehnic:** `deltatech_sale_analysis_vat`
- **Versiune:** `19.0.1.0.1`
- **Cale:** [https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_analysis_vat](https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_analysis_vat)
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_analysis_vat`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul adaugă dimensiunea de TVA în rapoartele standard de analiză a vânzărilor, astfel încât cifra de afaceri dintr-o perioadă poate fi defalcată pe cotă de TVA direct din vizualizările pivot, fără instrumente suplimentare. Practic, ajută la citirea corectă a cifrei de afaceri fără dubla numărare a valorii atunci când o factură este emisă pentru un bon fiscal deja existent din Punctul de Vânzare (POS).

#### 2. Funcționalități Cheie

- Analiza Facturilor (`account.invoice.report`) câștigă câmpurile **Cotă TVA** (grupa de taxă) și **TVA** (taxa) ca filtru și grupare.
- Flag **Factură pentru Bon Fiscal** pe analiza facturilor, cu filtre pentru afișare/ascundere — evită dubla numărare a cifrei de afaceri atunci când analiza facturilor e citită alături de analiza POS (valoarea unei asemenea facturi e deja inclusă în bonul fiscal).
- Analiza Punctului de Vânzare (`report.pos.order`) câștigă aceleași câmpuri **Cotă TVA** și **TVA** ca filtru și grupare.
- Filtre **Bonuri fără Factură** / **Bonuri cu Factură** pe analiza POS.
- Doar taxele procentuale sunt tratate drept TVA; taxele fixe (ex: taxă verde, garanție ambalaj returnabil) sunt ignorate, astfel încât fiecare linie păstrează exact o singură cotă de TVA și nicio linie nu e duplicată în rapoarte.
- Cifra de afaceri a unei perioade, fără duplicare, se obține din Analiza POS filtrată pe „Bonuri fără Factură” plus întreaga Analiză a Facturilor pentru facturile către clienți.

#### 3. Dependențe

- `account`
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `account.invoice.report` (extindere): adaugă `vat_tax_id`, `vat_tax_group_id` și `is_fiscal_receipt` (calculate prin suprascrierea `_select()`/`_from()` din raportul SQL), determinând TVA-ul aplicabil doar din taxele procentuale și verificând dacă factura are un `pos.order` asociat.
- `report.pos.order` (extindere): adaugă `vat_tax_id` și `vat_tax_group_id`, calculate similar prin suprascrierea `_select()`/`_from()`, pornind de la taxele procentuale aplicate liniilor de comandă POS.

**Vizualizări**

- `view_account_invoice_report_search` (moștenește `account.view_account_invoice_report_search`): adaugă câmpurile și filtrele de grupare pentru cotă TVA/TVA, plus filtrele „Facturi pentru Bonuri Fiscale” / „Facturi fără Bon Fiscal”.
- `view_report_pos_order_search` (moștenește `point_of_sale.view_report_pos_order_search`): adaugă câmpurile și filtrele de grupare pentru cotă TVA/TVA, plus filtrele „Bonuri fără Factură” / „Bonuri cu Factură”.

**Acțiuni Automate / Acțiuni Server**

Modulul nu definește sarcini `ir.cron`, reguli `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate module cu pagină wiki funcțional conectate. Modulul se bazează exclusiv pe rapoartele `account.invoice.report` (din `account`) și `report.pos.order` (din `point_of_sale`), ambele fără pagină wiki proprie la momentul acestei ingestii.
