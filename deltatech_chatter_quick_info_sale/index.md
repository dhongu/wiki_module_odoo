# Chatter Quick Info: Ultimul preț către client

- **Nume Tehnic:** `deltatech_chatter_quick_info_sale`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_chatter_quick_info_sale
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_sale`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în chatter-ul ofertelor și comenzilor de vânzare un panou „Ultimul preț către client”. Pentru fiecare produs de pe comandă, agentul vede prețul la care a fost vândut ultima dată aceluiași client, deci nu mai face o ofertă sub prețul de data trecută fără să observe.

#### 2. Funcționalități Cheie

- Pentru fiecare linie: prețul curent și ultimul preț (ambele după discount și fără TVA), diferența în procente (roșu când prețul curent e mai mic, verde când e mai mare).
- Ultima comandă (link) și data ei; tooltip-ul ultimului preț arată cantitatea, unitatea și prețul comenzii respective.
- Antet care numără produsele cu preț sub ultima vânzare; chip-uri pentru produsele vândute pentru prima dată și data ultimei comenzi a clientului.
- Ultimul preț provine din ultima comandă confirmată a aceleiași companii către compania clientului (inclusiv comenzile contactelor și adreselor sale), fără comanda curentă; se convertește în unitatea de măsură a liniei și, la monede diferite, în moneda comenzii la cursul zilei.
- Comenzile altor agenți se iau în calcul chiar dacă utilizatorul vede doar comenzile proprii (citire cu drepturi de administrator, intenționat). Linkul către comandă apare doar dacă utilizatorul o poate citi.
- Configurare: panoul e vizibil utilizatorilor de vânzări; se modifică din *Setări > Tehnic > Interfață utilizator > Chatter Quick Info* (mod dezvoltator). Dacă prețurile colegilor trebuie să rămână private, se scot din panou utilizatorii „Vânzări / Utilizator: documente proprii”.

#### 3. Dependențe

- `deltatech_chatter_quick_info`
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): calculează datele panoului „Ultimul preț către client”.
- `chatter.quick.info` (înregistrare de date): definește panoul pentru `sale.order`.

**Vizualizări**

- Panoul din chatter, definit prin `chatter_quick_info_sale_order_last_price`; modulul nu adaugă formulare sau liste proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `deltatech_chatter_quick_info`: cadrul de panouri din chatter pe care se sprijină modulul.
- `deltatech_chatter_quick_info_stock`: panou similar pe transferuri de stoc.
