# Purchase Price History

- **Nume Tehnic:** `deltatech_purchase_price_history`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_purchase_price_history
- **Cale Locală:** `odoo-addons/deltatech/deltatech_purchase_price_history`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul afișează, direct în fișa produsului, prețul minim, maxim și mediu de achiziție din ultimele 12 luni. Valorile se calculează din facturile de la furnizori, ceea ce ajută la negocierea cu furnizorii și la evaluarea rapidă a variațiilor de preț, fără rapoarte separate.

#### 2. Funcționalități Cheie

- Prețul minim, maxim și mediu de achiziție din ultimele 12 luni apare în tab-ul Achiziții (Purchase) al șablonului de produs.
- Valorile sunt stocate pe produs și recalculate periodic de o acțiune planificată (zilnic), nu la fiecare deschidere a fișei.
- Calculul pornește din liniile facturilor de achiziție (furnizor) validate, cu cantitate pozitivă, din ultimele 12 luni; prețul unitar este dedus din sold/cantitate, deci este exprimat mereu în moneda companiei.
- Nu este recomandat în medii multi-company, deoarece companiile pot avea monede diferite.
- Starea de dezvoltare din manifest: Beta.

#### 3. Dependențe

- `purchase`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpurile `min_purchase_price`, `max_purchase_price`, `avg_purchase_price` și metoda `compute_purchase_history()`, care face un singur UPDATE SQL în bloc pe baza facturilor `in_invoice` postate din ultimele 12 luni.

**Vizualizări**

- `product_template_form_view`: extinde formularul produsului și adaugă grupul cu cele trei prețuri în tab-ul Achiziții.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_product_purchase_price_history` (Get purchase price history): rulează zilnic `compute_purchase_history()`, ca utilizator root.

#### 5. Conexiuni

- `account`: sursa datelor sunt liniile facturilor de furnizor (`account.move.line`).
