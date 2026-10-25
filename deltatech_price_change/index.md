# Price Change (Modificare preț)

- **Nume Tehnic:** `deltatech_price_change`
- **Versiune:** `19.0.1.2.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_price_change
- **Cale Locală:** `odoo-addons/deltatech/deltatech_price_change`
- **Ultima Ingestie:** `2026-10-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul urmărește modificările prețului de vânzare al produselor și le consemnează într-un document datat și numerotat, cu procesul-verbal de modificare a prețurilor. Fiecare schimbare de preț (manuală, din import sau făcută de alt modul) este înregistrată automat într-un jurnal, iar din jurnal se întocmește documentul care arată stocul afectat și diferențele de valoare, util la controlul intern și la afișarea corectă a prețurilor la raft.

#### 2. Funcționalități Cheie

- **Jurnal al modificărilor de preț de listă:** se completează automat, la orice schimbare; este disponibil în *Vânzări > Produse > Modificări preț de listă* și prin butonul **Istoric preț** de pe fișa produsului.
- O singură linie de jurnal pe produs și zi: prețul vechi este cel dinaintea primei modificări din zi, cel nou este cel curent; dacă prețul revine la valoarea zilei precedente, linia dispare.
- O linie deja preluată într-un document confirmat nu se mai modifică; o nouă schimbare în aceeași zi pornește o linie nouă.
- **Document de modificare preț** (secvență proprie, istoric de mesaje), cu trei tipuri:
  - *Din modificări de preț*: butonul **Încarcă modificări** aduce modificările din jurnal până la data documentului, care nu sunt în alt document, cu stocul și prețul vechi, nou și diferența; confirmarea nu scrie prețuri (sunt deja schimbate);
  - *În produs*: la confirmare, prețurile noi se scriu în produse;
  - *În listă de prețuri*: la confirmare, prețurile noi se scriu ca prețuri fixe în listele de prețuri.
- La confirmare, un document fără locație se împarte în câte un document pe fiecare locație internă cu stoc din produsele lui.
- **Raport (proces-verbal)** cu prețuri cu și fără taxe, valori și semnături; se poate tipări și direct de pe produs/variantă. Dacă parametrul de sistem `price_change.public_pricelist_id` conține ID-ul unei liste de prețuri, se tipăresc doar liniile aferente ei.
- **Etichete de raft:** din document se pot tipări etichetele produselor modificate prin puntea `deltatech_price_change_label`, care se instalează automat împreună cu [deltatech_product_labels](../deltatech_product_labels/index.md).
- Modulul nu generează note contabile; fișa consultant descrie contextul legal și contabil (OMFP 1802/2014, evidența la preț de vânzare).

#### 3. Dependențe

- `base`
- `stock`
- `product`
- `sale`

#### 4. Componente Cheie

**Modele**

- `product.price.change`: documentul de modificare preț (cu `mail.thread`), cu tipul, data, locația și starea.
- `product.price.change.line`: liniile documentului, cu produs, stoc, preț vechi, preț nou, diferență.
- `product.price.change.log`: jurnalul modificărilor de preț de listă (o linie pe produs și zi).
- `product.template` / `product.product` (extinse): înregistrarea modificărilor de preț, butonul de istoric și tipărirea.

**Vizualizări**

- `view_change_price_form` / `view_product_change_price`: formularul și lista documentului de modificare preț.
- `view_price_change_log_list` / `view_price_change_log_search`: lista și căutarea în jurnal.
- `product_template_form_view`: butonul **Istoric preț** pe produs.
- `report_pricechange`, `report_pricechange_product`, `report_pricechange_variant`: șabloanele QWeb ale procesului-verbal.

**Acțiuni Automate / Acțiuni Server**

- Nu are `ir.cron` sau acțiuni server; are secvența `seq_change_price_resource` și trei rapoarte (`action_report_product_price_change`, `..._product`, `..._variant`).

#### 5. Conexiuni

- [deltatech_product_labels](../deltatech_product_labels/index.md): etichetele de raft pentru produsele modificate, prin puntea `deltatech_price_change_label` (auto-instalare).
