# Chatter Quick Info: Product Sales on Purchases

- **Nume Tehnic:** `deltatech_chatter_quick_info_purchase`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_chatter_quick_info_purchase
- **Cale Locală:** `odoo-addons/bitshop/deltatech_chatter_quick_info_purchase`
- **Ultima Ingestie:** `2026-10-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Adaugă în chatter-ul facturilor de furnizor, al rambursărilor de la furnizor și al comenzilor de achiziție panoul **Vânzări produse**. Acesta arată cât din produsele de pe document s-a vândut efectiv, astfel încât achizitorul vede pe loc dacă marfa se mișcă, înainte să o comande din nou, fără să deschidă rapoarte separate de vânzări.

#### 2. Funcționalități Cheie

- Pentru fiecare produs de pe document: cantitatea vândută de la data documentului (din cantitatea de pe document), cantitatea vândută în total, valoarea fără TVA vândută de la data documentului și data ultimei vânzări.
- Antetul panoului arată valoarea vândută de la data documentului; chip-urile arată totalurile și numărul de produse fără nicio vânzare de la acea dată (rândurile respective apar cu gri, la final).
- Produsele cele mai vândute apar primele; numele produsului deschide fișa produsului.
- „Vândut" înseamnă linie de comandă de vânzare confirmată, din aceeași companie; sumele sunt fără TVA, în moneda companiei. Retururile și notele de credit nu se scad, iar cantitățile nu se convertesc între unități de măsură.
- Data documentului: data facturii pentru facturile de furnizor (data contabilă pe ciorne fără dată de factură); data confirmării (altfel data comenzii) pentru comenzile de achiziție.
- Panoul se vede implicit grupului Achiziții / Operator și se reîmprospătează automat la 30 de secunde, cât timp documentul e deschis; butonul ↻ recalculează imediat.
- Configurare fără cod: **Setări > Tehnic > Interfață utilizator > Chatter Quick Info** (modul dezvoltator) — grupuri, interval de reîmprospătare, pliat implicit, condiție. Implicit panoul nu apare pe documentele anulate.
- Documentele cu peste 200 de produse afișează primele 200 în tabel; totalurile le includ pe toate.
- Fluxul detaliat pas cu pas este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md)
- `purchase`
- `sale`
- `account`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): metoda `_chatter_quick_info_product_sales` furnizează panoul pe comanda de achiziție.
- `account.move` (extins): aceeași metodă pentru facturi și rambursări de la furnizor.
- `product.product` (extins): `_chatter_quick_info_sales_panel` calculează vânzările pe produs și datele panoului.

**Vizualizări**

- Fără vizualizări proprii; panoul se afișează prin cadrul Chatter Quick Info.

**Acțiuni Automate / Acțiuni Server**

- Fără cron sau acțiuni server. Date: două definiții `chatter.quick.info` (pe `purchase.order` și `account.move`), cu condiția `state != cancel`, grupul `purchase.group_purchase_user` și reîmprospătare la 30 s.

#### 5. Conexiuni

- [deltatech_chatter_quick_info](../deltatech_chatter_quick_info/index.md): cadrul pe care se construiește panoul (dependență directă, încă fără pagină wiki).
