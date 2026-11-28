# Garanția produselor

- **Nume Tehnic:** `deltatech_warranty`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_warranty
- **Cale Locală:** odoo-addons/deltatech/deltatech_warranty
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul păstrează perioada de garanție pe fiecare produs și o tipărește automat pe oferta și comanda de vânzare, astfel încât lista garanțiilor să nu mai fie scrisă manual la fiecare vânzare.

#### 2. Funcționalități Cheie

- Câmpul **Garanție (luni)** pe fișa produsului, în fila *Informații generale*; se completează din *Vânzări > Produse > Produse*.
- Pagină suplimentară de garanție, pe foaie nouă, în PDF-ul *Ofertă / Comandă*, afișată doar dacă măcar o linie are produs cu garanție.
- Tabelul paginii conține eticheta liniei (denumirea și descrierea produsului) și garanția în luni.
- Liniile fără garanție, secțiunile și notele sunt omise; dacă nicio linie nu are garanție, PDF-ul rămâne neschimbat.

#### 3. Dependențe

- `sale`

#### 4. Componente Cheie

**Modele**

- `product.template`: extins cu câmpul `warranty_months` (Garanție în luni).

**Vizualizări**

- `product_template_form_view`: adaugă câmpul de garanție în formularul produsului.
- `sale_order_warranty_data`: șablon QWeb moștenit din `sale.report_saleorder_document`, care adaugă pagina de garanție.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- `sale`: oferta și comanda pe care se tipărește pagina de garanție.
