# Deltatech POS Fix (localizat la `deltatech_pos_fix/index.md`)

- **Nume Tehnic:** `deltatech_pos_fix`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_fix
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_fix`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul corectează felul în care Punctul de Vânzare (POS) calculează totalul unei linii de comandă atunci când o poziție fiscală schimbă taxele unui produs de la „taxă inclusă în preț” la o taxă neinclusă (de exemplu taxare inversă/reverse charge cu 0%). Fără această corecție, POS păstrează prețul unitar neschimbat și calculează greșit baza impozabilă, în timp ce modulul de Vânzări face deja acest calcul corect — modulul aliniază comportamentul POS la cel din Vânzări, atât în interfața de vânzare, cât și pe facturile generate din comenzile POS.

#### 2. Funcționalități Cheie

- Recalculează corect prețul unitar în POS atunci când taxele se schimbă prin maparea poziției fiscale.
- Asigură consistență între modulul Vânzări și POS în privința tratării taxelor incluse în preț.
- Adaptează prețul unitar pe liniile de factură generate din comenzile POS, pentru a reflecta corect noua mapare de taxe.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `pos.order.line`: extinde `_prepare_base_line_for_taxes_computation` — dacă poziția fiscală a comenzii schimbă taxele liniei față de taxele originale, recalculează prețul unitar cu `account.tax._adapt_price_unit_to_another_taxes`, pentru consistență cu facturile generate din POS.

**Frontend (JavaScript, OWL)**

- `pos_order_line.esm.js`: patch pe `PosOrderline.prepareBaseLineForTaxesComputationExtraValues` — atunci când comanda are o poziție fiscală, recalculează `price_unit` folosind `accountTaxHelpers.adapt_price_unit_to_another_taxes` pe baza taxelor originale și a taxelor rezultate din poziția fiscală, pentru ca totalul afișat în interfața POS să fie corect.

**Vizualizări**

Modulul nu adaugă vizualizări (fără fișiere în `views/`, `data: []` în manifest).

**Acțiuni Automate / Acțiuni Server**

Nu există cron-uri, `base.automation` sau `ir.actions.server` definite de acest modul.

#### 5. Conexiuni

- `point_of_sale`: modulul aplică un fix direct peste comportamentul de calcul al taxelor din POS (fără pagină wiki proprie pentru modulul core).
