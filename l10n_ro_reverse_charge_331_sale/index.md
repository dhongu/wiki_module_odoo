# Romania - Taxare inversă art. 331 pe comenzile de vânzare (localizat la `l10n_ro_reverse_charge_331_sale/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_sale`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_reverse_charge_331_sale
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_sale`
- **Ultima Ingestie:** `2026-11-25`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde garda de taxare inversă de la articolul 331 (deja aplicată pe facturi de `l10n_ro_reverse_charge_331`) și la oferte și comenzi de vânzare. Fără el, o ofertă către un client neînregistrat în scopuri de TVA ar afișa greșit 0% TVA — corectă doar la facturare — și ar comunica clientului un total eronat încă din faza de ofertare.

#### 2. Funcționalități Cheie

- Aplică statutul de plătitor de TVA al clientului (`res.partner._l10n_ro_is_vat_registered()`) direct la calculul taxelor pe linia de ofertă/comandă de vânzare (`sale.order.line._compute_tax_ids`), nu doar la facturare.
- Ofertele către clienți neplătitori de TVA arată cota normală (nu 0%), iar cele către clienți plătitori de TVA cu poziția fiscală art. 331 arată taxarea inversă (TVA 0%, dar total corect).
- Pe linia ofertei apare taxa **`0% R331`** doar pentru clientul înregistrat în scopuri de TVA cu poziția fiscală a plătitorilor și un produs cu taxa domestică marcată **Taxare inversă art. 331**; pentru un client neînregistrat, chiar cu aceeași poziție fiscală, rămâne taxa domestică și totalul conține TVA la cota bunului.
- La confirmarea comenzii și generarea facturii, factura preia taxa de pe comandă; la postare, modulul de bază blochează o factură cu taxa art. 331 emisă către un client neînregistrat în scopuri de TVA.
- Schimbarea clientului pe o ofertă care are deja linii nu recalculează singură taxele: când se schimbă și poziția fiscală se apasă **Actualizare Taxe** din tabul **Alte informații**, altfel se șterg și se readaugă liniile.
- Nu are setări, meniuri sau ecrane proprii (se folosește *Vânzări → Comenzi → Oferte*); regimul art. 331 se configurează în modulul de bază (poziția fiscală a plătitorilor și taxele domestice marcate).
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
