# Explicație Reaprovizionare (localizat la `deltatech_replenishment_explain/index.md`)

- **Nume Tehnic:** `deltatech_replenishment_explain`
- **Versiune:** `19.0.1.1.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_replenishment_explain`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_replenishment_explain`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul adaugă în Odoo o fereastră de tip „explică-mi" pentru regulile de reaprovizionare (`stock.warehouse.orderpoint`), care arată pas cu pas cum a ajuns Odoo la cantitatea prognozată (forecast) și la cantitatea de comandat (to order) pentru un produs. Dialogul reconstituie, cu date live, calculul intern al Odoo — stocul disponibil, intrările și ieșirile programate, orizontul de aprovizionare (lead time + orizont de reaprovizionare) și rotunjirea la multiplu — și semnalează riscuri precum cerere programată dincolo de orizont (invizibilă pentru prognoză), lipsa unui furnizor configurat (care introduce tăcut un termen de +365 zile), un posibil stockout chiar și atunci când nu se comandă nimic, rotunjiri care umflă cantitatea, suprascrieri manuale sau reguli amânate (snooze). Astfel, gestionarii de stoc și responsabilii de achiziții înțeleg rapid de ce o regulă de reaprovizionare propune o anumită cantitate, în loc să acorde încredere oarbă cifrei calculate automat.

#### 2. Funcționalități Cheie

- Fereastră (dialog) read-only, deschisă din raportul de Reaprovizionare (Acțiune ▸ „Why this replenishment?") sau direct din antetul formularului Regulilor de comandă (Reordering Rules).
- Reconstituie construcția prognozei: stoc disponibil + recepții programate − cerere programată, calculate până la orizontul lead-time-ului.
- Reconstituie matematica cantității de comandat: `max(Min, Max) − prognoză`, rotunjită în sus la multiplul de reaprovizionare.
- Detaliază descompunerea lead time + Orizont de Reaprovizionare, care fixează data orizontului de lead-time.
- Rezumat vizual în partea de sus a dialogului: o bară SVG a cantităților (prognoză vs. Min/Max, cu diferența „de comandat") și o cronologie a orizontului (azi → lead time → data orizontului de lead-time).
- Semnalează constatări de risc: cerere programată dincolo de orizont (invizibilă pentru prognoză), lipsă furnizor configurat (întârziere tăcută de +365 zile), posibil stockout chiar și fără nicio comandă (când există un termen-limită/deadline), inflație provocată de rotunjire, suprascrieri manuale ale cantității și reguli amânate (snooze).

#### 3. Dependențe

- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.warehouse.orderpoint` (extins): adaugă acțiunea `action_explain_replenishment()` care deschide dialogul; metodele private `_get_replenishment_explanation()`, `_explain_scheduled_moves()`, `_explain_diagram_geometry()` și `_get_replenishment_risks()` reconstituie cu date live calculul de prognoză/cantitate de comandat al Odoo, geometria diagramei SVG și lista de constatări de risc.
- `stock.replenishment.explanation` (model tranzient): wizardul din spatele dialogului — reține regula de comandă (`orderpoint_id`) și câmpuri legate (`product_id`, `warehouse_id`, `qty_forecast`, `qty_to_order`); câmpul calculat `explanation_html` randează șablonul QWeb al explicației; metoda `action_open_forecast_report()` deschide raportul de prognoză al produsului.

**Vizualizări**

- `view_warehouse_orderpoint_form_explain` (extinde `stock.view_warehouse_orderpoint_form`): adaugă în antetul formularului Regulii de comandă butonul „Why this replenishment?".
- `view_stock_replenishment_explanation_form`: formularul (dialog modal) al wizardului, care afișează conținutul HTML calculat al explicației.
- `replenishment_explanation_templates.xml`: șablonul QWeb `deltatech_replenishment_explain.replenishment_explanation` — construiește conținutul dialogului (bara SVG de cantități, cronologia orizontului, tabelul de descompunere a lead time-ului și lista de constatări de risc).

**Acțiuni Automate / Acțiuni Server**

- `action_explain_replenishment_server` (`ir.actions.server`, legată de listă/formular pe `stock.warehouse.orderpoint`): apelează `action_explain_replenishment()` pe regula de comandă selectată, pentru a deschide dialogul din meniul de acțiuni al raportului de Reaprovizionare.

#### 5. Conexiuni

- Nu au fost identificate conexiuni către alte module cu pagină wiki; funcționalitatea se bazează exclusiv pe modelele native ale modulului `stock`.
</content>
