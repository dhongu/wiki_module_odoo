# Constrângeri Integritate Stocuri România (localizat la `l10n_ro_stock_constraints/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_constraints`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_stock_constraints
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_constraints`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Acest modul protejează integritatea datelor de stoc pentru localizarea românească, blocând modificările retroactive periculoase după înregistrarea contabilă. Complementar cu `deltatech_stock_negative` (care previne stocul negativ înainte de validare), modulul acționează după validare: interzice modificarea cantităților pe mișcările deja valorizate și impune o constrângere PostgreSQL directă pentru cantități non-negative pe locațiile interne.

## 2. Funcționalități Cheie

- **Blocare modificare mișcări valorizate:** interzice modificarea câmpului `quantity` pe `stock.move.line` în starea `done` dacă mișcarea asociată are `is_valued = True`, prevenind discrepanțe între cantitățile fizice și cele contabile.
- **Constrângere stoc non-negativ pe locații interne:** constraint SQL pe `stock.quant` (`quantity >= 0`) pentru locațiile de tip `internal`, instalat prin `post_init_hook`; locațiile de tranzit, input sau virtuale sunt excluse.
- **Adaptare Odoo 19:** ține cont de eliminarea `stock.valuation.layer`, valorizarea fiind acum pe `stock.move` (`value`, `is_valued`, `remaining_qty`).

## 3. Dependențe

- `stock_account`

## 4. Componente Cheie

Conform `readme/DESCRIPTION.md`:

### Modele

- `stock.move.line`: Extins cu constrângerea care blochează modificarea cantității după valorizare.
- `stock.quant`: Vizat de constrângerea PostgreSQL pentru cantitate non-negativă pe locații interne.

### Acțiuni Automate / Acțiuni Server

- `post_init_hook`: Instalează constrângerea SQL directă pe `stock.quant` la instalarea modulului.

## 5. Conexiuni

- `l10n_ro_stock_gestiune`
