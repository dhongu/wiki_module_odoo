# Plată Ramburs / la Livrare (COD) (localizat la `deltatech_payment_on_delivery/index.md`)

- **Nume Tehnic:** `deltatech_payment_on_delivery`
- **Versiune:** `19.0.4.1.2`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_payment_on_delivery`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_on_delivery`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul integrează o metodă de plată „Ramburs la livrare" (Cash On Delivery – COD) în ecosistemul Odoo, concepută special pentru a gestiona particularitățile plăților efectuate după livrare, păstrând în același timp coerența cu fluxurile standard de plată și vânzare ale Odoo. Astfel, clienții pot alege să achite comanda în momentul recepției mărfii, iar afacerea beneficiază de un control corect al stărilor tranzacției și al reconcilierii contabile.

#### 2. Funcționalități Cheie

- **Integrare Ramburs la livrare (COD):** adaugă un furnizor și o metodă de plată dedicate COD, permițând clienților să aleagă plata la primirea mărfurilor.
- **Stări de tranzacție configurabile:** flexibilitate în modul de tratare a tranzacțiilor după confirmarea comenzii — tranzacția poate rămâne în starea „Pending" (utilă pentru verificare sau urmărire manuală) sau poate fi automat „Authorized".
- **Prag de sumă minimă:** se poate seta o sumă minimă (`minimum_amount`) pentru opțiunea COD; metoda devine disponibilă clientului doar dacă totalul comenzii (convertit în moneda furnizorului) atinge sau depășește acest prag.
- **Filtrare inteligentă de compatibilitate:** asigură afișarea furnizorului COD doar atunci când este compatibil cu criteriile comenzii, inclusiv moneda și limitele de sumă.
- **Protecția integrității:** pentru a garanta fluxuri contabile corecte, modulul împiedică trecerea manuală a tranzacțiilor COD în starea „Done", protejând procesul de reconciliere; starea „Done" se atinge doar prin validare corespunzătoare (de exemplu, prin wizard-ul de import).
- **Wizard de import al plăților COD:** utilitar specializat pentru importul confirmărilor de plată de la curieri, care automatizează validarea tranzacțiilor COD prin potrivirea referințelor de tracking și a sumelor, trecând tranzacțiile în stările finale.
- **Suport pentru valute multiple:** efectuează conversii automate la evaluarea constrângerilor de sumă minimă în medii multi-valutare.
- **Restricție pe categorie de produs:** anumite categorii de produse pot fi marcate cu „No Cash On Delivery"; dacă o comandă conține un produs dintr-o astfel de categorie, metoda de plată COD este dezactivată.
- **Integrare cu Deltatech Delivery:** modulul este utilizat și de `deltatech_delivery` pentru a îmbunătăți fluxurile de plată legate de curier și a simplifica gestionarea încasărilor la livrare.

#### 3. Dependențe

- `payment`
- `sale`
- `delivery`
- `payment_custom`
- `account`
- `stock_delivery`
- `website_sale`

#### 4. Componente Cheie

Conform fluxului de ingestie, secțiunile de componente sunt omise deoarece `readme/DESCRIPTION.md` este prezent și acoperă Sumarul și Funcționalitățile Cheie. (Funcționalitățile menționate în Readme indică, la nivel tehnic, un furnizor și o metodă de plată COD, un wizard de import al plăților și extinderi pe categoria de produs și pe tranzacția de plată.)

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): utilizează acest modul pentru a îmbunătăți fluxurile de plată legate de curier și încasările la livrare.
