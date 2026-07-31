# Product Unique Code (localizat la `deltatech_product_unique_code/index.md`)

- **Nume Tehnic:** `deltatech_product_unique_code`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_product_unique_code
- **Cale Locală:** `odoo-addons/deltatech/deltatech_product_unique_code`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul împiedică existența unor coduri duplicate pe articole: Referința Internă
(`default_code`) și Codul de Bare (`barcode`) trebuie să fie unice, inclusiv față
de produsele arhivate. Astfel se elimină erorile de identificare a articolelor
(scanare greșită la gestiune, confuzii de referință în comenzi) cauzate de coduri
reciclate sau introduse din greșeală de mai multe ori.

#### 2. Funcționalități Cheie

- Restricționează utilizarea de Referințe Interne (`default_code`) și Coduri de Bare
  (`barcode`) duplicate pe articole.
- Verificarea de unicitate include și produsele arhivate, pentru a preveni
  refolosirea codurilor de la înregistrări vechi.
- Validarea se face atât pe șabloanele de produs (`product.template`), cât și pe
  variantele de produs (`product.product`).
- Se validează doar valorile care se schimbă efectiv (politica „fără duplicate
  noi"): produsele care au deja un duplicat istoric pot fi în continuare curățate
  (arhivate, corectate câte un câmp odată, cod șters sau redenumit) de utilizatorii
  obișnuiți — dar orice valoare nouă sau modificată trebuie să fie unică.
- Include un grup de securitate „Allow duplicate product codes" care permite
  anumitor utilizatori să ocolească aceste restricții, dacă este necesar.

#### 3. Dependențe

- `product`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): suprascrie `create()`/`write()` pentru a declanșa
  verificarea de unicitate pe variantele generate/afectate atunci când `default_code`
  sau `barcode` se modifică pe șablon.
- `product.product` (extins): suprascrie `create()`/`write()` și expune metodele
  centrale de validare — `_check_unique_code_all()`, `_check_unique_field_all()` —
  care caută duplicate în `product.product` și `product.template` (inclusiv
  înregistrări arhivate, via `active_test=False`) și ridică `ValidationError` cu
  lista articolelor care dețin deja codul respectiv.

**Vizualizări**

- Modulul nu adaugă vizualizări proprii; validarea acționează transparent la
  salvarea articolelor prin ecranele standard de produs.

**Acțiuni Automate / Acțiuni Server**

- Nu conține `ir.cron`, `base.automation` sau `ir.actions.server` — logica rulează
  sincron în `create()`/`write()`.

Definit suplimentar în `security/security.xml`: grupul de securitate
`group_product_duplicate_code` ("Allow duplicate product codes"), atribuit implicit
utilizatorilor `base.user_root` și `base.user_admin`; membrii acestui grup ocolesc
verificarea de unicitate.

#### 5. Conexiuni

- [deltatech_product_code](../deltatech_product_code/index.md): ambele module gestionează codificarea articolelor (referință internă/cod), zonă funcțională înrudită.
