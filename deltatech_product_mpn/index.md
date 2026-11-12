# Product MPN (localizat la `deltatech_product_mpn/index.md`)

- **Nume Tehnic:** `deltatech_product_mpn`
- **Versiune:** `19.0.0.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_mpn
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_mpn`
- **Ultima Ingestie:** `2026-11-12`

#### 1. Sumar

Furnizorii și clienții denumesc adesea un produs după codul de piesă al producătorului (MPN — Manufacturer Part Number), care poate diferi de referința internă. Modulul adaugă acest cod pe produse și îl face căutabil în lista de produse, astfel încât articolele să poată fi găsite rapid după codul producătorului.

#### 2. Funcționalități Cheie

- **Câmpul MPN:** formularul produsului afișează un câmp text *MPN* (ajutor: Manufacturer Part Number), opțional, fără verificare de unicitate sau de format.
- **Căutare după MPN:** bara de căutare a listei de produse primește o căutare *MPN*; modulul nu adaugă căutare după MPN în lista de variante sau în câmpurile de produs din documente.
- **Coloane opționale:** lista de produse și lista de variante pot afișa o coloană *MPN*, ascunsă implicit și vizibilă când este bifată în meniul coloanelor opționale.
- **O valoare pe produs:** MPN aparține produsului (șablonului), nu variantei, deci toate variantele afișează aceeași valoare; câmpul nu este adăugat pe formularul variantei.
- Modulul nu adaugă meniuri, setări sau grupuri de securitate, deci oricine poate edita un produs îi poate edita și MPN-ul. Codul este doar stocat și afișat: nu este copiat în comenzi, facturi, rapoarte sau pe site.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

Conform prioritizării Readme (`readme/DESCRIPTION.md` prezent), analiza detaliată a componentelor a fost omisă; mai jos sunt doar reperele confirmate în cod.

**Modele**

- `product.template` (extins): câmpul `mpn` (Char, „MPN”).

**Vizualizări**

- `product_template_only_form_view` (extindere): câmpul `mpn` după referința internă pe formularul produsului.
- `product_template_search_view` (extindere): căutare după `mpn` în lista de produse.
- `product_template_tree_view` și `product_product_tree_view` (extinderi): coloană opțională `mpn`, ascunsă implicit, în lista de produse și în cea de variante.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale verificate către alte module cu pagină wiki existentă.
