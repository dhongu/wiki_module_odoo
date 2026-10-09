# Deltatech stock move analytic (localizat la `deltatech_stock_analytic/index.md`)

- **Nume Tehnic:** `deltatech_stock_analytic`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_analytic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_analytic`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul generează automat înregistrări analitice din mișcările de stoc. Fiecărei locații de stoc i se poate asocia un cont analitic, iar la finalizarea unei mișcări între două locații astfel configurate, valoarea mărfii transferate se reflectă în contabilitatea analitică: o linie pe contul locației sursă și una de sens opus pe contul locației destinație. Este util pentru organizațiile care vor să urmărească costurile asociate transferurilor și ajustărilor de stoc pe centre de cost sau proiecte.

#### 2. Funcționalități Cheie

- Creare automată de linii în `account.analytic.line` când o mișcare de stoc ajunge în starea „Done”, câte o pereche de linii (sursă și destinație) pentru fiecare mișcare.
- Legarea locațiilor de stoc de conturi analitice, prin câmpul **Analytic account** din formularul locației (**Inventar > Configurare > Locații**, grupul de informații suplimentare).
- Liniile se creează numai dacă **ambele** locații (sursă și destinație) au cont analitic; altfel mișcarea nu generează nimic.
- Valoarea liniilor: cantitate înmulțită cu prețul unitar al mișcării; dacă acesta lipsește, se folosește prețul unitar calculat de stoc, iar în ultimă instanță prețul standard al produsului. Linia sursă are sumă pozitivă, cea de destinație negativă.
- Fiecare linie păstrează produsul, cantitatea și unitatea de măsură; referința conține nota transferului (text simplu) și numele transferului, pentru identificare ușoară la audit.
- Rezultatul se verifică în contabilitate, la **Analytic Items**, după validarea transferului.

#### 3. Dependențe

- `stock`
- `analytic`
- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.location` (extins): adaugă câmpul `analytic_id` (cont analitic).
- `stock.move` (extins): suprascrie `write`; la trecerea în starea `done` creează liniile analitice. Metoda `can_create_analytics` verifică existența contului analitic pe ambele locații.

**Vizualizări**

- `location_analytic_form`: moștenește `stock.view_location_form` și afișează `analytic_id` în grupul `additional_info`.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- `account_analytic_account` / `account.analytic.line`: destinația înregistrărilor generate, vizibile în Analytic Items.
- Nu există legături funcționale cu alte module care au pagină wiki.
