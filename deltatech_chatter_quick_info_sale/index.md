# Chatter Quick Info: Last Price to the Customer (localizat la `deltatech_chatter_quick_info_sale/index.md`)

- **Nume Tehnic:** `deltatech_chatter_quick_info_sale`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_chatter_quick_info_sale
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_sale`
- **Ultima Ingestie:** `2026-10-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă în chatter-ul ofertelor și al comenzilor de vânzare panoul **Ultimul preț la client**. Pentru fiecare produs de pe document, panoul arată prețul la care a fost vândut ultima dată aceluiași client, astfel încât agentul de vânzări vede pe loc o ofertă sub prețul anterior, fără să caute în istoric.

#### 2. Funcționalități Cheie

- Pentru fiecare linie de comandă: prețul unitar de acum și ultimul preț, ambele după discount și fără TVA.
- Diferența în procente: roșu când prețul de acum e mai mic, verde când e mai mare (diferențele sub 0,05% rămân necolorate).
- Ultima comandă (link către ea) și data ei; tooltip-ul ultimului preț indică cantitatea, unitatea și prețul din acea comandă.
- Antetul numără produsele sub ultimul preț; chip-urile arată produsele vândute pentru prima dată clientului și data ultimei comenzi a clientului. Produsele noi pentru client apar estompate.
- Ultimul preț provine din ultima comandă confirmată a aceleiași companii către firma-mamă a clientului (inclusiv comenzile pe persoane de contact și adrese), cu excluderea comenzii curente.
- Prețul se convertește la unitatea de măsură a liniei curente și, când monedele diferă, la moneda comenzii, la cursul de azi.
- Sunt luate în calcul și comenzile altor agenți, chiar dacă utilizatorul vede doar documentele proprii.
- Implicit panoul se vede utilizatorilor de vânzări și doar pe oferte (ciornă și trimise); condiția și grupurile se modifică din *Setări > Tehnic > Interfață utilizator > Chatter Quick Info* (mod dezvoltator).
- Panoul este informativ: nu modifică liniile ofertei sau lista de prețuri. Fluxul detaliat este în fișa consultant.

#### 3. Dependențe

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md)
- `sale`

#### 4. Componente Cheie

**Modele**

- `sale.order` (extins): metoda `_chatter_quick_info_last_price` construiește conținutul panoului (rânduri, chip-uri, coloane); `_chatter_quick_info_last_sale_lines` găsește, printr-o interogare SQL, ultima linie confirmată pe produs pentru firma clientului.

**Vizualizări**

- Modulul nu definește vizualizări proprii; panoul este afișat de cadrul *Chatter Quick Info*.

**Acțiuni Automate / Acțiuni Server**

- `chatter_quick_info_sale_order_last_price` (înregistrare `chatter.quick.info`, `noupdate`): definește panoul pe `sale.order`, cu domeniul `state in (draft, sent)` și grupul `sales_team.group_sale_salesman`.
- Migrare `19.0.1.0.1/post-migration.py`: însoțește schimbarea condiției implicite a panoului.

#### 5. Conexiuni

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md): cadrul de panouri din chatter pe care se sprijină modulul (și dependență directă).
