# Cash On Delivery (COD) (localizat la `deltatech_payment_on_delivery/index.md`)

- **Nume Tehnic:** `deltatech_payment_on_delivery`
- **Versiune:** `20.0.5.0.7`
- **Cale:** https://github.com/terrabit-solutions/bitshop/tree/20.0/deltatech_payment_on_delivery
- **Cale Locală:** `odoo-addons/bitshop/deltatech_payment_on_delivery`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul extinde plata standard **Ramburs (Cash On Delivery, COD)** din Odoo — furnizorul `custom` cu modul „Cash On Delivery" din modulul `delivery` — cu regulile folosite de magazinele online și de curierii din România. Nu creează un furnizor paralel: folosește ca atare furnizorul, metoda de plată, checkout-ul, pasul „încasează plata" de la validarea livrării și crearea întârziată a plății din Odoo, adăugând controlul confirmării comenzii și reconcilierea încasărilor raportate de curieri.

#### 2. Funcționalități Cheie

- **Construit peste COD-ul standard**: fără furnizor paralel.
- **Confirmare manuală a comenzii**: implicit, o comandă plătită ramburs nu se confirmă automat la checkout; oferta e marcată ca trimisă și așteaptă un operator (risc mai mare de refuz la livrare). Opțiunea (`cod_manual_confirmation`) se poate debifa pe furnizor pentru confirmarea automată standard.
- **Restricție pe categorie de produs**: categoriile de website marcate „No Cash On Delivery" ascund opțiunea COD pentru comenzile care conțin produsele lor.
- **Fără COD după link de plată**: după generarea unui link de plată pentru o comandă, COD nu mai este oferit, ca suma să nu fie încasată de două ori.
- **Protecția integrității**: o tranzacție COD nu poate fi trecută manual în „Done"; se decontează doar prin wizardul de import.
- **Wizard de import al plăților COD**: importă extrasele COD ale curierilor (Excel, per transportator) și reconciliază tranzacțiile după referință, număr de tracking (AWB) și sumă.
- **Referință de plată pe factură**: factura unei comenzi COD folosește AWB-ul ca referință de plată.
- **Sumă minimă**: folosește restricția standard „Minimum Amount" a furnizorului.
- **Helpere pentru alte module**: `_is_cash_on_delivery()` pe tranzacții, furnizori și comenzi de vânzare.
- Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `payment`
- `sale`
- `delivery`
- `payment_custom`
- `account`
- `stock_delivery`
- `website_sale`

Dependență externă Python: `openpyxl` (citirea extraselor Excel).

#### 4. Componente Cheie

**Modele**

- `payment.provider` (extins): câmpul `cod_manual_confirmation` și logica de disponibilitate COD.
- `payment.transaction` (extins): blocarea trecerii manuale în „Done" și helperul `_is_cash_on_delivery()`.
- `sale.order` (extins): `payment_link_generated`, care dezactivează COD după un link de plată.
- `product.public.category` (extins): `no_cash_on_delivery`.
- `payment.link.wizard` (extins): marchează comanda când se generează link de plată.
- `account.move` (extins): AWB-ul ca referință de plată pe factură.
- `payment.transaction.import.file` / `payment.transaction.import` (wizard): fișierul importat al curierului și liniile de reconciliat (tranzacție, comandă, referință, AWB, sumă, dată, stare).

**Vizualizări**

- `views/payment_provider_view.xml`: opțiunile COD pe furnizor.
- `views/product_category_view.xml`: marcajul „No Cash On Delivery" pe categorie.
- `wizard/payment_import_view.xml`: wizardul de import.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite acțiuni automate; încărcarea migrărilor (`migrations/`) rulează la actualizare.

#### 5. Conexiuni

- [deltatech_delivery](../deltatech_delivery/index.md): utilizează acest modul pentru fluxurile de plată legate de curier și încasările la livrare.
