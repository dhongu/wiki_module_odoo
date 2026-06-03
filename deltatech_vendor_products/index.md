# Produse Furnizori (localizat la `deltatech_vendor_products/index.md`)

- **Nume Tehnic:** `deltatech_vendor_products`
- **Versiune:** `19.0.1.1.3`
- **Cale:** https://github.com/terrabit-ro/bitshop/tree/19.0/deltatech_vendor_products
- **Cale Locală:** `odoo-addons/bitshop/deltatech_vendor_products`
- **Ultima Ingestie:** `2026-06-03`

#### 1. Sumar

Deltatech Vendor Products automatizează și simplifică gestiunea datelor de produs provenite de la mai mulți furnizori. Modulul creează o punte între cataloagele de produse ale furnizorilor și inventarul Odoo, facilitând importul, actualizarea și sincronizarea informațiilor despre produse — inclusiv prețuri, disponibilitate și imagini. Astfel, companiile care lucrează cu mulți furnizori pot administra cataloage mari fără intervenție manuală: economisesc timp, păstrează informațiile la zi, asigură consistența prețurilor și reduc erorile de introducere a datelor. Un avantaj important este că permite definirea unui catalog de produse furnizor fără ca acestea să fie create obligatoriu ca produse în baza de date Odoo, iar pe baza listei importate se pot crea produse noi sau actualiza cele existente.

#### 2. Funcționalități Cheie

- Import produse furnizor din formate variate de fișier (XLSX, CSV, XML)
- Import date de produs din URL-uri sau feed-uri de furnizor
- Procesarea feed-urilor de produse de la furnizori, inclusiv format feed XML [Google Merchant Center](https://support.google.com/merchants/answer/7052112)
- Potrivire automată a produselor cu cele existente în Odoo (algoritmi avansați de matching)
- Creare de produse noi din datele furnizorului
- Actualizare prețuri pe baza unor reguli configurabile (preț de bază, adaos, discount) cu suport pentru conversie valutară
- Sincronizarea disponibilității produselor de la furnizori
- Descărcarea și atașarea automată a imaginilor de produs
- Atribuire automată a categoriei de produs și maparea codurilor de produs furnizor către coduri interne
- Importul unui număr foarte mare de produse (50.000 în ~30 secunde) cu procesare în fundal
- Stă la baza altor module care permit căutarea pe website după codul de produs al furnizorului

#### 3. Dependențe

- `product`
- `purchase`
- `stock`
- `purchase_stock`

#### 4. Componente Cheie

Sumarul și funcționalitățile cheie au fost preluate din `readme/DESCRIPTION.md`; conform fluxului de ingestie, analiza detaliată a codului pentru această secțiune este omisă.

#### 5. Conexiuni

- [deltatech_vendor_products_granit](../deltatech_vendor_products_granit/index.md): extensie care adaugă integrarea specifică furnizorului Granit peste cadrul de import al acestui modul.
- [deltatech_vendor_products_website](../deltatech_vendor_products_website/index.md): extensie care expune produsele de furnizor pe website, permițând căutarea după codul de produs al furnizorului.
- `deltatech_vendor_products_kramp`: extensie care adaugă integrarea specifică furnizorului Kramp peste cadrul de import al acestui modul.
