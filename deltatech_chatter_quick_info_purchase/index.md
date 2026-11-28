# Chatter Quick Info: Product Sales on Purchases

- **Nume Tehnic:** `deltatech_chatter_quick_info_purchase`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_chatter_quick_info_purchase
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_purchase`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă un panou **Product sales** în chatterul facturilor furnizor, notelor de credit furnizor și comenzilor de achiziție: cât din produsele de pe document s-a vândut efectiv, astfel încât cumpărătorul vede pe loc dacă marfa se mișcă înainte de a o comanda din nou.

#### 2. Funcționalități Cheie

- Pentru fiecare produs de pe document: cantitatea vândută de la data documentului (din cantitatea de pe document), cantitatea vândută în total, suma fără TVA vândută de la data documentului și data ultimei vânzări.
- Antetul arată suma vândută de la data documentului; chip-urile arată totalurile și câte produse nu s-au vândut (rândurile lor apar estompate). Cele mai bine vândute vin primele, iar numele produsului deschide produsul.
- Vânzare = linie dintr-o comandă de vânzare confirmată din aceeași companie; sumele sunt fără TVA, în moneda companiei. Data documentului: data facturii la facturi furnizor; data confirmării (altfel data comenzii) la comenzi de achiziție.
- Panoul se vede utilizatorilor *Purchase / User* și se reîmprospătează la 120 s (implicit din date); se modifică în *Settings > Technical > User Interface > Chatter Quick Info* (mod dezvoltator), la cele două panouri *Product sales*.
- Citirea vânzărilor se face intenționat cu drepturi de administrator, ca cumpărătorii să vadă rotația fără acces la comenzile de vânzare; sunt afișate doar totaluri per produs, nu clienți sau comenzi.

#### 3. Dependențe

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md)
- `purchase`
- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): metoda `_chatter_quick_info_product_sales` pentru facturi/note de credit furnizor.
- `purchase.order` (extins): aceeași metodă pentru comenzi de achiziție.
- `product.product` (extins): calculul vânzărilor per produs.

**Vizualizări**

- Fără vizualizări XML; panourile sunt înregistrări `chatter.quick.info` din date.

**Acțiuni Automate / Acțiuni Server**

- `chatter_quick_info_purchase_order_sales` și `chatter_quick_info_account_move_sales`: definițiile panoului pe `purchase.order` și `account.move` (condiție: stare diferită de anulat; grup *Purchase / User*; reîmprospătare 120 s). Nu sunt acțiuni programate.

#### 5. Conexiuni

- [deltatech_chatter_quick_info_pack](../deltatech_chatter_quick_info_pack/index.md): pachetul care îl instalează împreună cu panourile pentru vânzări și stoc.
- [deltatech_chatter_quick_info_sale](../deltatech_chatter_quick_info_sale/index.md): panou-soră, ultimul preț către client.
- [deltatech_chatter_quick_info_stock](../deltatech_chatter_quick_info_stock/index.md): panou-soră, stoc și rezervări.
