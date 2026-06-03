# Simple MRP (localizat la `deltatech_mrp_simple/index.md`)

- **Nume Tehnic:** `deltatech_mrp_simple`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_mrp_simple
- **Cale Locală:** `odoo-addons/deltatech/deltatech_mrp_simple`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Modulul oferă o variantă simplificată de producție, gândită pentru cazurile în care întocmirea unei liste de materiale (BOM) complete este inutil de complexă. Utilizatorul definește direct, pe un singur ecran, ce componente intră în producție și ce produse rezultă, fără să creeze în prealabil structuri de fabricație. Modulul generează automat mișcările de stoc necesare și calculează prețul produselor rezultate pe baza prețului componentelor consumate, putând chiar să creeze automat un produs nou și o comandă de vânzare pentru rezultat. Este util pentru ambalări, reambalări, asamblări ad-hoc sau transformări simple de stoc.

#### 2. Funcționalități Cheie

- Crearea unei producții simple, cu componente și produse rezultate configurabile, fără a fi nevoie de o listă de materiale.
- Generarea a două ridicări de stoc (stock pickings), cu tip de operațiune configurabil; ridicările pot fi accesate direct din ecranul de producție simplă și pot fi validate automat sau manual.
- Calcularea automată a prețului de stoc al produsului/produselor rezultate pornind de la prețul de stoc al componentelor. Dacă rezultă mai multe produse, prețul se introduce manual.
- Dacă prețul produsului rezultat este 0, se generează o eroare. Comportamentul poate fi suprascris setând parametrul de sistem `simple_production_allow_zero_cost` la o valoare diferită de zero.
- Crearea automată a unui produs nou și a unei comenzi de vânzare pentru produsul rezultat (utilizatorul trebuie să facă parte din grupul „Sale simple production"). Prețul de vânzare al produsului rezultat este calculat pe baza prețului de vânzare al componentelor.

#### 3. Dependențe

- `stock`
- `sale`

#### 4. Componente Cheie

**Modele**

- `mrp.simple`: Documentul central de producție simplă; grupează componentele consumate și produsele rezultate, calculează prețurile și gestionează ridicările de stoc asociate.
- `mrp.simple.line.in`: Liniile cu componentele care intră în producție (materialele consumate).
- `mrp.simple.line.out`: Liniile cu produsele care rezultă din producție.
- `sale.order` (extins): Permite crearea automată a unei comenzi de vânzare pentru produsul rezultat.
- `stock.picking` (extins): Integrare cu ridicările de stoc generate de producția simplă.

**Vizualizări**

- `views/mrp_simple_view.xml`: Interfața principală a producției simple (formular și listă) cu acces la ridicările de stoc generate.
- `views/sale_order.xml`: Extinderi pe comanda de vânzare pentru produsul rezultat.
- `wizard/add_multi_lines.xml`: Asistent pentru adăugarea în masă a mai multor linii.

**Acțiuni Automate / Acțiuni Server**

- `data/ir_config_parameter.xml`: Definește parametrul de sistem `simple_production_allow_zero_cost`, care permite continuarea producției cu cost zero al produsului rezultat.

#### 5. Conexiuni

- [deltatech_mrp](../deltatech_mrp/index.md): alternativă bazată pe liste de materiale (BOM); `deltatech_mrp_simple` acoperă același scop de transformare a stocului, dar fără a necesita o structură de fabricație.
- [deltatech_mrp_cost](../deltatech_mrp_cost/index.md): tratează costurile de producție în fluxul MRP clasic, complementar abordării de calcul al prețului din producția simplă.
