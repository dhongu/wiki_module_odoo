# POS Add Extra Line (localizat la `deltatech_sale_add_extra_line_pos/index.md`)

- **Nume Tehnic:** `deltatech_sale_add_extra_line_pos`
- **Versiune:** `19.0.1.0.0`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_sale_add_extra_line_pos`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_sale_add_extra_line_pos`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Acest modul extinde mecanismul de linii suplimentare al modulului [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md) pentru a funcționa direct în interfața Punctului de Vânzare (POS). Atunci când casierul adaugă în coșul POS un produs configurat cu un *produs extra* (de exemplu o taxă de mediu, o garanție de ambalaj sau un cost de manipulare), aplicația adaugă automat, în timp real, o linie separată pentru produsul extra, cu cantitatea calculată corect. Astfel se elimină uitarea sau adăugarea manuală a acestor taxe/produse conexe la vânzarea la casă, casierii câștigă timp, iar bonul de casă rămâne transparent pentru client.

#### 2. Funcționalități Cheie

- **Integrare în timp real cu POS**: adăugarea automată a liniei extra se face direct în interfața de vânzare, cu feedback vizual instantaneu pe partea de client (JavaScript, fără roundtrip la server).
- **Calcul dinamic al cantității**: cantitatea produsului extra se recalculează automat pe baza cantității produsului principal și a multiplicatorului configurat pe fișa produsului (`Cantitate extra = Σ(Cantitate produs principal × multiplicator)`).
- **Consolidarea liniilor**: dacă mai multe produse din coș trimit către același produs extra, modulul le consolidează într-o singură linie, cu cantitatea totalizată.
- **Actualizare la modificarea cantității**: la schimbarea cantității produsului principal în coșul POS, linia produsului extra este recalculată și actualizată instantaneu.
- **Sincronizare configurare produs**: câmpurile de configurare a liniei extra (`extra_product_id`, `extra_percent`, `extra_qty`) definite pe șablonul de produs sunt încărcate automat în datele POS ale sesiunii.

#### 3. Dependențe

- `point_of_sale`
- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md)

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): metoda `_load_pos_data_fields` adaugă la lista de câmpuri încărcate în POS pe `extra_product_id`, `extra_percent` și `extra_qty`, astfel încât configurarea liniei extra să fie disponibilă pe partea de client (frontend POS).
- `pos.session` (extins): pregătit pentru a extinde parametrii de încărcare a datelor de sesiune POS (în cod există doar o metodă comentată, fără logică activă la momentul ingestiei).

**Vizualizări**

- Nu sunt definite vizualizări backend (`data: []` în manifest) — modulul acționează exclusiv prin logică JavaScript în interfața POS (`static/src/js/models.esm.js`), fără ecrane de configurare proprii în Odoo backend.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`. Automatizarea este implementată prin patch-uri OWL/JavaScript pe `PosStore`, `PosOrder` și `PosOrderline` (adăugare linie extra la `addLineToCurrentOrder`, recalcul la `setQuantity`).

#### 5. Conexiuni

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md): modulul de bază — definește câmpurile de configurare pe `product.template` și logica echivalentă pentru comenzile de vânzare standard/website; acest modul este dependența directă listată mai sus, dar este menționat și aici pentru claritatea relației (extensie POS a aceluiași mecanism).
- `point_of_sale`: modulul standard Odoo ale cărui modele de front-end (`PosStore`, `PosOrder`, `PosOrderline`) sunt extinse prin patch JavaScript.
