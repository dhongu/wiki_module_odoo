# Romania - Constrângeri de integritate a stocului (localizat la `l10n_ro_stock_constraints/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_constraints`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_constraints
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_constraints`
- **Ultima Ingestie:** 2026-11-28
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul protejează integritatea datelor de stoc după validarea mișcărilor. Blochează modificările retroactive ale cantităților pe mișcările cu valorizare contabilă și interzice stocul negativ pe locațiile interne printr-o constrângere direct în baza de date. Completează modulul `deltatech_stock_negative`, care blochează stocul negativ înainte de validare.

#### 2. Funcționalități Cheie

- **Linii de mișcare protejate după valorizare:** modificarea cantității pe o linie de mișcare în starea *done* este interzisă dacă mișcarea este valorizată, ca să nu apară discrepanțe între stocul fizic și cel contabil.
- **Cantitate non-negativă pe locații interne:** constrângere SQL `quantity >= 0` pe `stock.quant` pentru locațiile de tip intern; tranzitul, locațiile de intrare și cele virtuale sunt excluse.
- **Mesaje de blocare și corecții permise:** utilizatorul primește mesaje explicite la blocare; corecțiile se fac prin documente (retur, ajustare), nu prin editarea mișcării validate (detalii în [fișa consultant](FISA_CONSULTANT.md)).

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

**Modele**

- `stock.move.line` (extins): blochează modificarea cantității după valorizare.
- `stock.quant` (extins): vizat de constrângerea PostgreSQL pentru cantitate non-negativă.

**Vizualizări**

Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (`hooks.py`): instalează constrângerea SQL pe `stock.quant` la instalare.

#### 5. Conexiuni

- [deltatech_stock_negative](../deltatech_stock_negative/index.md): blochează stocul negativ înainte de validare; modulul de față protejează datele după validare.
- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): gestiunile contabile de stoc, care beneficiază de aceeași protecție a datelor.
