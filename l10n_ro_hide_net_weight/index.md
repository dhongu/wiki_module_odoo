# Romania - Hide Net Weight (localizat la `l10n_ro_hide_net_weight/index.md`)

- **Nume Tehnic:** `l10n_ro_hide_net_weight`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_hide_net_weight
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_hide_net_weight`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul ascunde câmpul „Greutate netă” (`l10n_ro_net_weight`) de pe formularul produsului, deoarece generează confuzii de interpretare pentru utilizatori. Datele din câmp nu sunt șterse sau modificate, doar eticheta și câmpul nu mai apar în interfață.

#### 2. Funcționalități Cheie

- Ascunde pe formularul de produs (`product.template`) câmpul „Greutate netă” definit de `l10n_ro_stock`, împreună cu eticheta lui.
- Nu adaugă logică nouă: este un modul de tranziție, păstrat cât timp `l10n_ro_stock` definește câmpul.
- Planul de retragere: după ce câmpul este scos din `l10n_ro_stock`, vederile ascunse nu mai au țintă, modulul se declară învechit și se elimină (inclusiv din `depends` ale proiectelor care îl folosesc).
- Pentru e-Transport se folosește greutatea standard a produsului (`product.weight`), nu greutatea netă.

#### 3. Dependențe

- `l10n_ro_stock`

#### 4. Componente Cheie

**Modele**

- `product.template`: nicio extindere Python; modulul modifică doar vederea formularului.

**Vizualizări**

- `product_template_form_view_hide_net_weight`: moștenește `product.product_template_form_view` și setează `invisible` pe eticheta și pe containerul (`div[@name='l10n_ro_net_weight']`) câmpului `l10n_ro_net_weight`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `l10n_ro_stock`: definește câmpul `l10n_ro_net_weight` ascuns de acest modul.
- `l10n_ro_edi_stock`: e-Transport folosește `product.weight`.
- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md): e-Transport folosește `product.weight`, nu greutatea netă.
