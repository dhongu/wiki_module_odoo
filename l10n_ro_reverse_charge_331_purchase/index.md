# Romania - Taxare inversă art. 331 pe comenzile de achiziție (localizat la `l10n_ro_reverse_charge_331_purchase/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_purchase`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reverse_charge_331_purchase
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_purchase`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul extinde garda de taxare inversă de la articolul 331 din Codul fiscal la cererile de ofertă și la comenzile de achiziție. Fără el, o comandă către un furnizor care nu este înregistrat în scopuri de TVA ar purta taxa de autolichidare de 21% R331, iar factura de furnizor creată din comandă ar prelua această taxă fără recalculare; eroarea ar ieși la iveală abia când factura este blocată la postare. Cu modulul instalat, taxa corectă este stabilită încă din comandă. Se instalează automat când sunt prezente `l10n_ro_reverse_charge_331` și `purchase`.

#### 2. Funcționalități Cheie

- Aplică garda art. 331 pe statutul de TVA al furnizorului direct la calculul taxelor pe liniile comenzii de achiziție: furnizorul înregistrat în scopuri de TVA primește autolichidarea 21% R331, cel neînregistrat păstrează taxa internă.
- Aceeași gardă se aplică și liniilor create prin reaprovizionare (reguli de reaprovizionare / achiziție automată), care nu trec prin calculul obișnuit al taxelor.
- Factura de furnizor generată din comandă copiază taxele liniei, deci moștenește direct taxa corectă și nu mai este blocată la postare.
- Statutul de TVA este evaluat pe partenerul comercial (`commercial_partner_id`) al furnizorului.
- Este un modul-punte separat, pentru ca modulul contabil să nu depindă de `purchase`; o companie care doar înregistrează facturi de furnizor folosește garda fără modulul de achiziții.
- Nu adaugă câmpuri, meniuri sau vizualizări noi.

#### 3. Dependențe

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md)
- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order.line` (extins): suprascrie `_compute_tax_id`, care injectează în context statutul de TVA al furnizorului (cheia `RC331_VAT_REGISTERED_CONTEXT_KEY`, din `l10n_ro_reverse_charge_331`) înainte de apelul `super()`, și `_prepare_purchase_order_line`, care face același lucru pentru liniile create de reaprovizionare. Necesar deoarece ambele apelează `fiscal_position.map_tax()` fără a transmite partenerul.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Modulul nu definește acțiuni automate sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md): oferă taxele R331, gardianul pe statutul de TVA și cheia de context folosită aici (importată în cod).
