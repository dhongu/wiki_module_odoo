# Romania - Taxare inversă art. 331 pe comenzile de vânzare (localizat la `l10n_ro_reverse_charge_331_sale/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_sale`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reverse_charge_331_sale
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_sale`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Modulul extinde garda de taxare inversă de la articolul 331 (deja aplicată pe facturi de `l10n_ro_reverse_charge_331`) și la oferte și comenzi de vânzare. Fără el, o ofertă către un client neînregistrat în scopuri de TVA ar afișa greșit 0% TVA — corectă doar la facturare — și ar comunica clientului un total eronat încă din faza de ofertare.

#### 2. Funcționalități Cheie

- Aplică statutul de plătitor de TVA al clientului (`res.partner._l10n_ro_is_vat_registered()`) direct la calculul taxelor pe linia de ofertă/comandă de vânzare (`sale.order.line._compute_tax_ids`), nu doar la facturare.
- Ofertele către clienți neplătitori de TVA arată cota normală (nu 0%), iar cele către clienți plătitori de TVA cu poziția fiscală art. 331 arată taxarea inversă (TVA 0%, dar total corect).
- La confirmarea comenzii și generarea facturii, taxa de pe linia comenzii se păstrează pe factură, fără recalculare divergentă.
- Se instalează automat (`auto_install`) când sunt prezente ambele module `l10n_ro_reverse_charge_331` și `sale` — nu necesită configurare manuală.

#### 3. Dependențe

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md)
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order.line`: suprascrie `_compute_tax_ids` pentru a injecta în context cheia `RC331_VAT_REGISTERED_CONTEXT_KEY` (statutul de plătitor TVA al partenerului comercial), astfel încât `fiscal_position.map_tax()` să aplice garda art. 331 deja pe linia de ofertă/comandă, nu abia pe `account.move.line`.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md): furnizează garda de bază (poziția fiscală, cheia de context, taxa 0% art. 331) aplicată aici și pe fluxul de vânzări.
- `sale`: modelul `sale.order.line` extins de acest modul.
