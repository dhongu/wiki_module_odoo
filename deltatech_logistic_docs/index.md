# Logistic Documents (localizat la `deltatech_logistic_docs/index.md`)

- **Nume Tehnic:** `deltatech_logistic_docs`
- **Versiune:** `19.0.1.0.3`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_logistic_docs`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_logistic_docs`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Acest modul oferă un depozit centralizat pentru documentația logistică și de transport în Odoo. Este conceput pentru a simplifica gestionarea documentelor fizice (precum scrisori de trăsură CMR, certificate de origine sau avize de însoțire a mărfii) de-a lungul diferitelor etape ale lanțului de aprovizionare. În loc ca fișierele să fie risipite pe comenzi, livrări și facturi separate, echipele de logistică au un singur loc din care pot accesa și verifica toate documentele relevante pentru o expediere sau o tranzacție.

#### 2. Funcționalități Cheie

- **Hub unificat de documentație**: adaugă o vizualizare dedicată **Documente Logistică** care agregă atașamentele din mai multe modele și urmărește documentele legate de **Comenzi de Vânzare**, **Comenzi de Achiziție**, **Transferuri de Stoc** și **Facturi** într-un singur loc.
- **Legare inteligentă**: identifică și leagă automat documentele pe baza fluxului logic al documentelor Odoo (de la Comandă la Livrare și apoi la Factură), permițând echipelor de logistică să acceseze rapid toate fișierele relevante pentru o anumită expediere sau tranzacție.
- **Categorizarea documentelor**: permite etichetarea și clasificarea fișierelor logistice pentru o filtrare și o căutare mai ușoară în timpul auditurilor.
- **Utilizare**: documentele se accesează dintr-un meniu dedicat, cu opțiuni de căutare și filtrare după **Partener**, **Comandă** sau **Livrare**; fișierele noi se încarcă direct pe documentul relevant (comandă de vânzare, livrare etc.) și apar în vizualizatorul central, de unde pot fi descărcate sau vizualizate pentru verificare în timpul procesului de expediere și livrare.

#### 3. Dependențe

- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile pentru Sumar și Funcționalități Cheie au fost preluate din `readme/DESCRIPTION.md`, care nu solicită explicit detalierea componentelor tehnice. Analiza codului pentru această secțiune a fost, prin urmare, omisă. La nivel general, modulul extinde modelele `stock.picking`, `sale.order`, `purchase.order`, `account.move` și `ir.attachment`, cu vizualizările aferente pentru centralizarea documentelor logistice.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): leagă livrările de facturi, completând fluxul Comandă → Livrare → Factură pe care acest modul îl folosește pentru centralizarea documentelor.
