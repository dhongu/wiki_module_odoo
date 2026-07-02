# Romania - Dividende și Registru Acționari (localizat la `l10n_ro_dividends/index.md`)

- **Nume Tehnic:** `l10n_ro_dividends`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/l10n_ro_ent/tree/19.0/l10n_ro_dividends
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_dividends`
- **Ultima Ingestie:** 2026-06-01
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

## 1. Sumar

Modul pentru gestionarea completă a distribuirii de dividende conform legislației românești (Cod Fiscal art. 97). Acoperă registrul acționarilor/asociaților, hotărârea AGA de distribuire, calculul dividendului brut și net per acționar, reținerea impozitului la sursă cu cote istorice (10% pentru 2025, 16% din 1 ianuarie 2026) și generarea automată a notelor contabile aferente.

## 2. Funcționalități Cheie

- **Registru Acționari / Asociați:** înregistrarea acționarilor cu număr de acțiuni/părți sociale, valoare nominală, calcul automat al procentului de participare și istoric al modificărilor.
- **Distribuire Dividende:** hotărâre AGA cu referință, dată și exercițiu financiar; preluare automată a acționarilor și procentelor; calcul dividend brut (profit × % participare).
- **Reținere impozit la sursă** în funcție de data distribuirii: 10% pentru 2025, 16% începând cu 1 ianuarie 2026; calcul dividend net plătit.
- **Note contabile automate:** la confirmare AGA `Dr 117 = Cr 457`; la plată `Dr 457 = Cr 446` (impozit) și `Dr 457 = Cr 5121` (net).
- **Flux de lucru:** Ciornă → Confirmat AGA → Plătit, cu posibilitate de anulare înainte de plată.

## 3. Dependențe

- `account`
- `l10n_ro`

## 4. Componente Cheie

### Modele

- Model registru acționari/asociați: stochează acționarii, numărul de acțiuni și procentul de participare.
- Model distribuire dividende (hotărâre AGA): gestionează exercițiul, profitul distribuit, cotele de impozit și notele contabile generate.

### Vizualizări / Date

- `views/l10n_ro_dividends_view.xml`: vizualizările registrului de acționari și ale distribuirii de dividende.
- `security/ir.model.access.csv`: drepturile de acces.

### Acțiuni Automate / Acțiuni Server

*Nu au fost identificate acțiuni automate; notele contabile se generează la confirmarea AGA și la plată.*

## 5. Conexiuni

- `[[l10n_ro_financial_notes]]`
- `[[l10n_ro_financial_statements]]`
