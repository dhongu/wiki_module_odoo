# Modificare prețuri (Price Change)

- **Nume Tehnic:** `deltatech_price_change`
- **Versiune:** `20.0.1.2.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_price_change
- **Cale Locală:** odoo-addons/deltatech/deltatech_price_change
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Controlează modificările prețului de vânzare al produselor, printr-un document de modificare de preț datat și numerotat și raportul său (procesul-verbal de modificare a prețurilor). Fiecare schimbare a prețului de listă este înregistrată automat într-un jurnal.

#### 2. Funcționalități Cheie

- **Jurnal al modificărilor de preț de listă:** orice schimbare (manuală, prin import sau din alt modul) apare în Vânzări > Produse > List Price Changes și pe produs (butonul **Price History**). Se păstrează o linie per produs și zi: prețul vechi e cel dinaintea primei modificări a zilei, cel nou e cel curent; dacă prețul revine la cel din ziua precedentă, linia se șterge. O linie deja preluată într-un document confirmat nu se mai modifică.
- **Document de modificare de preț:** tip *From price changes* (butonul **Load Price Changes** aduce modificările din jurnal până la data documentului, cu stoc și valori vechi, noi și diferență; confirmarea nu scrie prețuri), *In product* (prețurile noi se scriu în produse la confirmare) și *In pricelist* (se scriu ca prețuri fixe în liste de prețuri).
- **Împărțire pe locații:** la confirmare, un document fără locație se împarte într-unul pe fiecare locație internă cu stoc din produsele sale.
- **Raport:** prețuri cu și fără taxe, valori și semnături. Se poate tipări și din produs; dacă parametrul `price_change.public_pricelist_id` conține ID-ul unei liste de prețuri, se tipăresc doar liniile acelei liste.
- **Etichete:** cu [deltatech_price_change_label](../deltatech_price_change_label/index.md) se tipăresc etichetele produselor modificate.
- Pașii detaliați sunt în fișa consultantului.

#### 3. Dependențe

- `base`
- `stock`
- `product`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.price.change.log`: jurnalul modificărilor de preț de listă (o linie per produs și zi).
- `product.price.change`: documentul de modificare de preț (cu `mail.thread`, numerotat prin secvența `price.change`).
- `product.price.change.line`: liniile documentului.
- `product.template` / `product.product` (extinse): urmărirea schimbărilor de preț și butonul de istoric.

**Vizualizări**

- `view_price_change_log_list` / `view_price_change_log_search`: jurnalul modificărilor.
- `view_change_price_form`, `view_product_change_price`: documentul de modificare de preț.
- `product_template_form_view`: butonul Price History pe produs.
- `action_report_product_price_change` (și variantele `_product`, `_variant`): raportul procesului-verbal.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [deltatech_price_change_label](../deltatech_price_change_label/index.md): tipărirea etichetelor din documentul de modificare de preț (auto-install).
- [deltatech_product_labels](../deltatech_product_labels/index.md): wizardul de etichete folosit de legătura de mai sus.
