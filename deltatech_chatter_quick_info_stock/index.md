# Chatter Quick Info: Stoc și rezervări

- **Nume Tehnic:** `deltatech_chatter_quick_info_stock`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_chatter_quick_info_stock
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_stock`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în chatter-ul transferurilor un panou „Stoc și rezervări”, ca depozitul să vadă ce poate pleca și ce blochează livrarea fără să deschidă prognoza fiecărui produs.

#### 2. Funcționalități Cheie

- Pe livrări și transferuri interne, pentru fiecare produs stocabil, în locația sursă și sublocațiile ei: cantitatea rezervată pe transfer din cerere; stocul disponibil, rezervat de alte transferuri (tooltip cu lista lor) și liber; cantitatea în intrare și data următoarei recepții.
- Antetul spune dacă transferul e acoperit; chip-urile numără produsele neacoperite și pe cele care ar putea fi acoperite eliberând rezervările altor transferuri. Produsele neacoperite apar primele, cu stocul liber în roșu.
- Pe recepții, la nivelul întregului depozit (o recepție în 2–3 pași intră în Input, nu în Stoc): stoc, cantitate liberă și cantitatea încă lipsă pe transferurile deschise care așteaptă produsul, cu numele lor.
- Panoul se reîmprospătează la 30 de secunde cât timp transferul e deschis.
- Configurare: vizibil utilizatorilor de inventar; se modifică din *Setări > Tehnic > Interfață utilizator > Chatter Quick Info* (mod dezvoltator), inclusiv frecvența de reîmprospătare.

#### 3. Dependențe

- `deltatech_chatter_quick_info`
- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): calculează datele panoului pentru livrări/interne și recepții.
- `chatter.quick.info` (înregistrare de date): definește panoul pentru `stock.picking`.

**Vizualizări**

- Panoul din chatter, definit prin `chatter_quick_info_stock_picking_stock`; modulul nu adaugă formulare sau liste proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- `deltatech_chatter_quick_info`: cadrul de panouri din chatter pe care se sprijină modulul.
- `deltatech_chatter_quick_info_sale`: panou similar pe comenzi de vânzare.
