# Chatter Quick Info: Stock and Reservations

- **Nume Tehnic:** `deltatech_chatter_quick_info_stock`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_chatter_quick_info_stock
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_stock`
- **Ultima Ingestie:** `2026-10-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în chatter-ul transferurilor de stoc panoul **Stoc și rezervări**, ca gestionarul să vadă dintr-o privire ce poate pleca și ce blochează livrarea, fără să deschidă prognoza fiecărui produs. Pe recepții arată, în plus, ce transferuri deschise așteaptă marfa care intră.

#### 2. Funcționalități Cheie

- **Livrări și transferuri interne:** pentru fiecare produs stocabil, în locația sursă și sublocațiile ei: cantitatea rezervată pe transfer din cea cerută, stocul fizic, rezervările altor transferuri (tooltip cu lista lor), stocul liber, cantitatea așteptată și data următoarei recepții.
- Antetul spune dacă transferul este acoperit; chip-urile numără produsele neacoperite și pe cele care s-ar acoperi eliberând rezervările altor transferuri. Produsele neacoperite apar primele, cu stocul liber în roșu.
- **Recepții:** calcul pe tot depozitul (la recepția în 2–3 pași marfa intră în Intrare, nu în Stoc): stoc, liber și cantitatea încă lipsă pe transferurile deschise care așteaptă produsul, cu denumirile lor.
- Panoul se reîmprospătează automat la 30 de secunde cât timp transferul este deschis.
- Este vizibil implicit grupului Inventar / Operator; grupurile, intervalul de reîmprospătare, starea pliată și condiția (panoul dispare după Validează / Anulează) se configurează din **Setări → Tehnic → Interfață utilizator → Informații rapide în chatter** (modul dezvoltator).
- Panoul este doar informativ: nu rezervă, nu eliberează și nu validează nimic.
- Fluxul pas-cu-pas este în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md)
- `stock`

#### 4. Componente Cheie

**Modele**

- `stock.picking` (extins): metoda `_chatter_quick_info_stock` și helperii pentru rândurile și panourile de livrare / recepție.

**Vizualizări**

- Fără vizualizări XML proprii; panoul se afișează prin cadrul Chatter Quick Info.

**Acțiuni Automate / Acțiuni Server**

- `chatter_quick_info_stock_picking_stock` (înregistrare `chatter.quick.info`, `noupdate`): definește panoul pe `stock.picking`, pentru transferurile care nu sunt `done`/`cancel`, grup `stock.group_stock_user`, reîmprospătare 30 s. Nu există cron-uri.

#### 5. Conexiuni

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md): cadrul pe care este construit panoul.
