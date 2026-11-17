# Purchase Create Bill Button (localizat la `deltatech_purchase_create_bill_button/index.md`)

- **Nume Tehnic:** `deltatech_purchase_create_bill_button`
- **Versiune:** `19.0.1.1.5`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_create_bill_button`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_create_bill_button`
- **Ultima Ingestie:** `2026-11-17`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

În Odoo 19, butonul clasic „Create Bill" de pe formularul comenzii de achiziție a fost înlocuit cu un widget „Upload Bill" care obligă utilizatorul să atașeze un fișier înainte de a putea genera factura. Acest modul restabilește butonul clasic, cu un singur clic, lângă widget-ul de încărcare, astfel încât comenzile de achiziție să poată fi facturate direct, fără a fi nevoie de un fișier atașat — exact ca în Odoo 18. Modulul restaurează totodată și copierea automată a „Referinței Furnizorului" de pe comanda de achiziție în câmpurile „Referință" și „Referință Plată" ale facturii de furnizor generate, comportament eliminat în Odoo 19. Butonul „Create Bills" este restaurat și pe lista Requests for Quotation (lista implicită din dashboard), unde Odoo 19 îl păstrase doar pe lista „Purchase Orders". Facturile create conțin doar liniile cu cantitate de facturat.

#### 2. Funcționalități Cheie

- Restabilește butonul „Create Bill" (facturare cu un singur clic) pe formularul comenzii de achiziție, alături de widget-ul „Upload Bill", evidențiat vizual (culoare primară) pentru a fi ușor de identificat
- Permite crearea facturii de furnizor direct din comanda de achiziție, fără a fi necesară atașarea unui fișier
- Restaurează copierea automată a „Referinței Furnizorului" din comanda de achiziție în câmpurile „Referință" și „Referință Plată" ale facturii generate, replicând comportamentul din Odoo 18
- Restaurează butonul de antet „Create Bills" pe lista Requests for Quotation, astfel încât mai multe comenzi de achiziție pot fi selectate și facturate deodată; retururile (total negativ) sunt convertite automat de Odoo în notă de credit de furnizor
- Facturile create conțin doar liniile care mai au cantitate de facturat: un produs rămas în backorder după o recepție parțială nu mai ajunge pe factură cu cantitatea 0 (se va factura la recepție), iar secțiunile (și notele) rămase fără linii de produs sunt eliminate
- Dacă nicio comandă selectată nu mai are cantitate de facturat, nu se creează factură și se afișează mesajul „There is nothing to bill: no quantity left to invoice on the selected orders."; comenzile fără nimic de facturat sunt sărite
- La facturarea mai multor comenzi într-o singură factură (același furnizor), „Referința" păstrează referințele furnizor ale tuturor comenzilor; dacă sunt diferite, „Referința Plată" rămâne goală
- Butonul de pe formular apare doar când comanda e în starea „Purchase Order" și mai are de facturat; modulul nu necesită configurare și nu adaugă meniuri, setări sau grupuri de acces

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `purchase.order` (extins): `_prepare_invoice` copiază `partner_ref` în `ref` și `payment_reference`; `action_create_invoice` filtrează comenzile fără cantitate de facturat (eroare `UserError` dacă nu rămâne niciuna), elimină liniile cu cantitate 0 și secțiunile/notele orfane (`_remove_zero_quantity_bill_lines`) și reface referințele combinate pentru facturile grupate.

**Vizualizări**

- `purchase_order_form`: moștenește `purchase.purchase_order_form` și adaugă butonul „Create Bill" (`btn-primary`) înaintea widget-ului `purchase_file_uploader`.
- `purchase_order_kpis_tree`: moștenește `purchase.purchase_order_kpis_tree` și adaugă butonul de antet „Create Bills" pe lista Requests for Quotation.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale documentate către alte module cu pagină în wiki.
