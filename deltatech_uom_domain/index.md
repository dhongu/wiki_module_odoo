# UoM Domain by Reference (localizat la `deltatech_uom_domain/index.md`)

- **Nume Tehnic:** `deltatech_uom_domain`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_uom_domain
- **Cale Locală:** `odoo-addons/deltatech/deltatech_uom_domain`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Până în Odoo 18.0, lista de unități de măsură dintr-un document conținea toate unitățile din categoria unității produsului. De la 19.0 categoriile au dispărut, iar unitățile trebuie legate una câte una de fiecare produs. Modulul reface comportamentul vechi pe fluxul de achiziție: oferă orice unitate convertibilă la unitatea produsului (aceeași rădăcină de arbore de conversie), fără reconfigurarea catalogului.

#### 2. Funcționalități Cheie

- Pe comenzile și facturile de achiziție, lista de unități conține orice unitate din același arbore ca unitatea produsului (un produs în bucăți oferă „Duzina”, „10 buc”, „100 buc”, nu „kg”).
- Pe linia de furnizor apar doar unitatea produsului, ambalajele lui (`uom_ids`) și unitățile din același arbore; nu mai poate fi aleasă o unitate dintr-un alt arbore (de exemplu „ml” pentru un cablu în metri).
- Câmp nou pe produs, tab-ul Achiziție: **Unitate implicită de achiziție**, echivalentul lui `uom_po_id` din 18.0. Linia de furnizor nouă o preia; comanda de achiziție o folosește când furnizorul nu are o linie valabilă (lipsă, expirată sau pentru alt furnizor).
- Modulul doar adaugă unități pe comenzi și facturi; singura restrângere este pe linia de furnizor. Liniile de furnizor existente nu se modifică; la corectarea unității se corectează și prețul.
- Intenționat nu se aplică pe vânzări, facturi emise, mișcări de stoc și rebut: e-Factura și e-Transport transmit codul UNECE al unității, iar o unitate fără cod mapat ar fi declarată ca bucată. Pentru vânzări se mapează mai întâi un cod real cu [deltatech_uom_unece](../deltatech_uom_unece/index.md).
- Multiplul regulii de reaprovizionare și codurile de bare pe ambalaj citesc tot `product.uom_ids`; pentru ele unitatea trebuie trecută pe produs.
- Utilizare: se activează **Unități de măsură** în Inventar > Configurare > Setări; nu necesită altă configurare. Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `deltatech.uom.domain.mixin`: mixin cu logica domeniului bazat pe rădăcina comună de conversie.
- `purchase.order.line`, `account.move.line`: folosesc mixinul pentru lista de unități.
- `product.supplierinfo`: `allowed_uom_ids` calculat și domeniu restrâns pe `uom_id`.
- `product.template`: `purchase_uom_id` (Unitate implicită de achiziție) și `purchase_allowed_uom_ids`.

**Vizualizări**

- `product_template_form_view`: câmpul Unitate implicită de achiziție în tab-ul Achiziție.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_uom_unece](../deltatech_uom_unece/index.md): codul UNECE al unității, necesar înainte de a extinde unitățile pe documente emise.
