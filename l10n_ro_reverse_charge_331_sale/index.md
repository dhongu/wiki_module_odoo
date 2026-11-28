# Romania - Taxare inversă art. 331 pe comenzile de vânzare (localizat la `l10n_ro_reverse_charge_331_sale/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_sale`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_reverse_charge_331_sale
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_sale`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde garda de înregistrare în scopuri de TVA de la art. 331 la ofertele și comenzile de vânzare. Fără el, o ofertă pentru un client neînregistrat ar afișa TVA 0%, adică un total greșit comunicat clientului, iar eroarea ar ieși la iveală abia la facturare, când factura, care preia taxele liniilor comenzii, este blocată la postare. Se instalează automat când sunt prezente `l10n_ro_reverse_charge_331` și `sale`.

#### 2. Funcționalități Cheie

- Pentru un client înregistrat în scopuri de TVA, cu poziția fiscală a plătitorilor, linia cu bunul marcat primește **0% R331**, iar totalul ofertei nu conține TVA.
- Pentru un client neînregistrat, chiar cu aceeași poziție fiscală, linia păstrează taxa domestică, cu TVA la cota bunului.
- Factura creată din comandă preia taxa de pe comandă; la postare, modulul de bază blochează taxa art. 331 către un client neînregistrat.
- Nu are setări, meniuri sau ecrane proprii; configurarea se face în [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md).
- La schimbarea clientului pe o ofertă cu linii existente taxele nu se recalculează singure: după schimbarea poziției fiscale se apasă **Actualizare Taxe** (tabul **Alte informații**) sau se șterg și se readaugă liniile.
- Fluxul de verificare este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md)
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order.line`: suprascrie `_compute_tax_ids` pentru a injecta în context statutul de plătitor TVA al partenerului comercial, astfel încât `map_tax` să aplice garda art. 331 deja pe linia ofertei sau comenzii, nu abia pe linia facturii.

**Vizualizări**

- Nu adaugă vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md): furnizează garda de bază (poziția fiscală, contextul, taxa 0% R331) aplicată aici pe fluxul de vânzări.
- [l10n_ro_reverse_charge_331_purchase](../l10n_ro_reverse_charge_331_purchase/index.md): aceeași regulă pe achiziții.
- [l10n_ro_reverse_charge_331_pos](../l10n_ro_reverse_charge_331_pos/index.md): aceeași regulă în POS.
