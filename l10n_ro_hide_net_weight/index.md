# Romania - Hide Net Weight (localizat la `l10n_ro_hide_net_weight/index.md`)

- **Nume Tehnic:** `l10n_ro_hide_net_weight`
- **Versiune:** `19.0.0.0.5`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_hide_net_weight
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_hide_net_weight`
- **Ultima Ingestie:** `2026-11-04`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul ascunde câmpul „Greutate netă” (`l10n_ro_net_weight`) de pe formularul produsului, deoarece generează confuzii de interpretare pentru utilizatori. Datele din câmp nu sunt șterse sau modificate, doar eticheta și câmpul nu mai apar în interfață.

#### 2. Funcționalități Cheie

- Ascunde pe formularul de produs (`product.template`) câmpul „Greutate netă” definit de `l10n_ro_stock_base`, împreună cu eticheta lui (**Inventar → Produse → Produse**, fila **Inventar**, grupul **Logistică**: rămân vizibile doar **Greutate** și **Volum**). Câmpul e ascuns și pe formularul variantei de produs.
- Nu necesită configurare: se instalează când firma nu folosește greutatea netă a produselor. Greutatea se introduce în câmpul **Greutate** (greutatea brută, folosită la transport).
- Valorile deja salvate rămân în baza de date, pot fi exportate din lista de produse și reapar dacă modulul este dezinstalat.
- Atenție la e-Transport: dacă firma folosește liniile de greutăți la expediere din `l10n_ro_etransport_enhancement`, greutatea netă a produselor se folosește în continuare pentru greutatea netă din declarația e-Transport, chiar și când câmpul e ascuns. Valorile salvate se golesc mai întâi (export, setare la 0, import; pentru produse cu variante, din **Inventar → Produse → Variante de produs**) sau modulul nu se instalează.
- Nu adaugă logică nouă: este un modul de tranziție, păstrat cât timp `l10n_ro_stock_base` definește câmpul. Dacă câmpul este scos de acolo, vederile ascunse nu mai au țintă, modulul se declară învechit și se elimină (inclusiv din `depends` ale proiectelor care îl folosesc).

#### 3. Dependențe

- `l10n_ro_stock_base`

#### 4. Componente Cheie

**Modele**

- `product.template`: nicio extindere Python; modulul modifică doar vederea formularului.

**Vizualizări**

- `product_template_form_view_hide_net_weight`: moștenește `product.product_template_form_view` și setează `invisible` pe eticheta și pe containerul (`div[@name='l10n_ro_net_weight']`) câmpului `l10n_ro_net_weight`.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `l10n_ro_stock_base`: definește câmpul `l10n_ro_net_weight` ascuns de acest modul (anterior definit de modulul OCA `l10n_ro_stock`).
- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md): calculează greutatea netă a liniilor de greutăți la expediere din `l10n_ro_net_weight`, când câmpul există; ascunderea nu golește valorile.
