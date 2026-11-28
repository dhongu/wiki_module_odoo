# Romania - Taxare inversă art. 331 pe comenzile de achiziție (localizat la `l10n_ro_reverse_charge_331_purchase/index.md`)

- **Nume Tehnic:** `l10n_ro_reverse_charge_331_purchase`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_reverse_charge_331_purchase
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_reverse_charge_331_purchase`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde garda de înregistrare în scopuri de TVA de la art. 331 la cererile de ofertă și la comenzile de achiziție. Fără el, o comandă către un furnizor neînregistrat în scopuri de TVA ar purta taxa de autolichidare **21% R331**, iar factura creată din comandă ar copia taxa, eroarea ieșind la iveală abia când factura este blocată la postare. Se instalează automat când sunt prezente `l10n_ro_reverse_charge_331` și `purchase`.

#### 2. Funcționalități Cheie

- Pe cererile de ofertă și comenzile de achiziție, taxa de autolichidare art. 331 se aplică doar când furnizorul este înregistrat în scopuri de TVA; altfel linia păstrează taxa deductibilă a produsului.
- Factura creată din comandă păstrează `21% R331` și se postează cu autolichidarea 4426 = 4427.
- Aceeași regulă pentru cererile de ofertă generate din reaprovizionare (ruta **Cumpără**).
- Nu are ecrane proprii; configurarea (poziția fiscală a plătitorilor și taxa deductibilă dedicată bunului, bifate *Taxare inversă art. 331*) se face în [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md).
- Taxele comenzilor existente nu se recalculează singure la schimbarea statutului de TVA al furnizorului: se readaugă linia sau se schimbă poziția fiscală.
- Fluxul de verificare este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_reverse_charge_331](../l10n_ro_reverse_charge_331/index.md)
- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order.line`: suprascrie `_compute_tax_id` și `_prepare_purchase_order_line` ca să transmită statutul de TVA al furnizorului către logica art. 331.

**Vizualizări**

- Nu adaugă vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_reverse_charge_331_sale](../l10n_ro_reverse_charge_331_sale/index.md): aceeași regulă pe ofertele și comenzile de vânzare.
- [l10n_ro_reverse_charge_331_pos](../l10n_ro_reverse_charge_331_pos/index.md): aceeași regulă în POS.
