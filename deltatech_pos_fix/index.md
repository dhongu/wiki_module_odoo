# POS Tax-Included Total Fix (localizat la `deltatech_pos_fix/index.md`)

- **Nume Tehnic:** `deltatech_pos_fix`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_fix
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_fix`
- **Ultima Ingestie:** `2026-11-18`

#### 1. Sumar

Modulul corectează două situații în care Punctul de Vânzare (POS) diferă de restul Odoo. Prima: când o poziție fiscală schimbă taxele unui produs de la „taxă inclusă în preț" la o taxă neinclusă (de exemplu taxare inversă cu 0%), POS calculează greșit totalul, în timp ce modulul de Vânzări îl calculează corect; modulul aliniază POS la comportamentul din Vânzări, atât în interfața de vânzare, cât și pe facturile generate din comenzile POS. A doua: factura unei comenzi POS plătite în numerar, cu rest, rămânea neachitată când contul de creanțe al POS coincide cu cel al clientului (4111 în planul de conturi românesc).

#### 2. Funcționalități Cheie

- Recalculează corect prețul unitar în POS atunci când taxele se schimbă prin maparea poziției fiscale.
- Asigură consistență între modulul Vânzări și POS în privința tratării taxelor incluse în preț.
- Adaptează prețul unitar pe liniile de factură generate din comenzile POS, pentru a reflecta corect noua mapare de taxe.
- Reconciliază factura unei comenzi POS plătite în numerar cu rest, atunci când contul de creanțe al POS este contul de creanțe al clientului; fără corecție, factura rămâne neachitată.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `pos.order.line`: extinde `_prepare_base_line_for_taxes_computation` — dacă poziția fiscală a comenzii schimbă taxele liniei față de cele originale, recalculează prețul unitar cu `account.tax._adapt_price_unit_to_another_taxes`, pentru consistență cu facturile generate din POS.
- `pos.payment`: extinde `_get_receivable_lines_for_invoice_reconciliation`, folosit la reconcilierea facturii cu plata POS (cazul numerarului cu rest).

**Frontend (JavaScript, OWL)**

- `pos_order_line.esm.js`: patch pe `PosOrderline.prepareBaseLineForTaxesComputationExtraValues` — când comanda are o poziție fiscală, recalculează `price_unit` cu `accountTaxHelpers.adapt_price_unit_to_another_taxes`, pe baza taxelor originale și a celor rezultate din poziția fiscală, pentru ca totalul afișat în POS să fie corect. Modulul include și teste unitare JS (`web.assets_unit_tests`).

**Vizualizări**

Modulul nu adaugă vizualizări (`data: []` în manifest).

**Acțiuni Automate / Acțiuni Server**

Nu există cron-uri, `base.automation` sau `ir.actions.server` definite de acest modul.

#### 5. Conexiuni

Modulul este un patch mic peste `point_of_sale` standard și rulează alături de restul suitei POS Terrabit și de modulele de conformitate fiscală românești, fără suprapuneri:

- [deltatech_pos](../deltatech_pos/index.md): tipărește bonuri fiscale și gestionează numerarul pe casa de marcat certificată.
- [deltatech_pos_base](../deltatech_pos_base/index.md): setările casei de marcat și codurile ECR.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): model comun de document fiscal, convertor de format ECR și expeditor Terrabit Connect.
- [deltatech_pos_stock](../deltatech_pos_stock/index.md): afișează stocul disponibil direct în POS.
- [deltatech_pos_price_sync](../deltatech_pos_price_sync/index.md): propagă modificările de preț în sesiunile POS deschise.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): urmărirea bonurilor AMEF, reconcilierea raportului Z și blocarea sesiunii.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): raportează bonurile fiscale POS în declarația D394 (op. 2).
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): factură de retur și linie de casă dedicate pentru fiecare retur POS.
