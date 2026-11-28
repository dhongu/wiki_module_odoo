# Romania - Hide Net Weight (localizat la `l10n_ro_hide_net_weight/index.md`)

- **Nume Tehnic:** `l10n_ro_hide_net_weight`
- **Versiune:** `20.0.0.0.6`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_hide_net_weight
- **Cale Locală:** odoo-addons/l10n-romania/l10n_ro_hide_net_weight
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Ascunde câmpul „Greutate netă” (`l10n_ro_net_weight`) de pe formularul produsului, deoarece generează confuzii de interpretare pentru utilizatori. Se instalează când firma nu folosește greutatea netă a produselor.

#### 2. Funcționalități Cheie

- Câmpul **Greutate netă**, adăugat de `l10n_ro_stock_base`, dispare din formularul produsului și al variantei; în grupul **Logistică** (tab-ul **Inventar**) rămân **Masă** (greutatea brută, folosită la transport) și **Volum**.
- Câmpul este doar ascuns: valorile deja salvate rămân în baza de date, se pot exporta din lista de produse și reapar la dezinstalarea modulului.
- Nu necesită configurare.
- Atenție: dacă firma folosește liniile de greutate de transport din `l10n_ro_etransport_enhancement`, greutatea netă a produselor se folosește în continuare pentru declarația e-Transport, chiar ascunsă; se golesc mai întâi valorile salvate sau nu se instalează modulul.

#### 3. Dependențe

- `l10n_ro_stock_base`

#### 4. Componente Cheie

**Modele**

- Nu definește modele; modifică doar vizualizări ale `product.template` și `product.product`.

**Vizualizări**

- `views/product_template_views.xml`: ascunde câmpul `l10n_ro_net_weight` pe produs și pe variantă.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_etransport_enhancement](../l10n_ro_etransport_enhancement/index.md): folosește greutatea netă a produselor în declarația e-Transport, chiar dacă este ascunsă.
