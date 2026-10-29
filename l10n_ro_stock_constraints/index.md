# Romania - Constrângeri de integritate a stocului (localizat la `l10n_ro_stock_constraints/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_constraints`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_constraints
- **Cale Locală:** odoo-addons/l10n_ro_ent/l10n_ro_stock_constraints
- **Ultima Ingestie:** `2026-10-29`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul protejează integritatea datelor de stoc după validare: împiedică modificarea mișcărilor de stoc deja înregistrate contabil și stocul negativ pe locațiile interne. Este complementar cu [deltatech_stock_negative](../deltatech_stock_negative/index.md), care blochează stocul negativ înainte de validare. Nu are meniuri sau ecrane proprii și nu cere configurare: protecțiile sunt active imediat după instalare.

#### 2. Funcționalități Cheie

- **Blocare modificare mișcări valorizate:** interzice modificarea cantității pe liniile unei mișcări finalizate cu valorizare contabilă și adăugarea de linii noi pe o astfel de mișcare, ca să nu apară discrepanțe între cantitățile fizice și cele contabile.
- **Stoc non-negativ pe locații interne:** constrângere PostgreSQL pe `stock.quant` (`quantity >= 0`) pentru locațiile de tip intern, instalată la instalarea modulului; locațiile de tranzit, input sau virtuale (producție, pierderi, clienți, furnizori) nu sunt afectate. Încălcarea ei se vede la utilizator ca o eroare internă a bazei de date.
- **Mesaje de blocare:** „Nu se poate modifica cantitatea pe o mișcare/transfer finalizat cu valorizare contabilă." și „Nu se poate crea o linie pe o mișcare finalizată cu valorizare contabilă existentă."
- **Corecții permise:** un transfer finalizat se corectează doar prin ajustare de inventar (**Inventar → Operațiuni → Ajustări fizice**), retur sau storno.
- **Mereu activ:** nu există opțiune de dezactivare din interfață; pentru situații speciale (de exemplu migrări de date) se contactează administratorul tehnic.
- **Adaptat pentru Odoo 19:** valorizarea este pe `stock.move` (`is_valued`), nu pe `stock.valuation.layer`, eliminat în această versiune.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.move.line` (extins): constrângere pe `quantity` și blocarea creării de linii pe mișcări finalizate cu `is_valued`.
- `stock.quant` (extins): câmp stocat `location_usage` (din tipul locației), necesar constrângerii SQL.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: adaugă pe `stock_quant` constrângerea `check_positive_quantity_for_internal_location`, dacă nu există deja.

#### 5. Conexiuni

- [deltatech_stock_negative](../deltatech_stock_negative/index.md): blochează stocul negativ înainte de validare; cele două module se instalează împreună fără conflict.
