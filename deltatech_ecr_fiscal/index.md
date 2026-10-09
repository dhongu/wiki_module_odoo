# ECR Fiscal Audit Fields (localizat la `deltatech_ecr_fiscal/index.md`)

- **Nume Tehnic:** `deltatech_ecr_fiscal`
- **Versiune:** `19.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_ecr_fiscal
- **Cale Locală:** `odoo-addons/deltatech/deltatech_ecr_fiscal`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul definește într-un singur loc câmpurile în care se păstrează rezultatul tipăririi pe o casă de marcat fiscală (ECR/AMEF): numărul bonului, numărul documentului fiscal, raportul Z, starea și eroarea raportată de aparat. Câmpurile sunt scrise de driverul casei de marcat (ecranul de plată din POS sau acțiunea de tipărire din magazin) și citite de rapoarte, de modulele de conformitate fiscală și de localizarea românească. Modulul depinde doar de `account`, deci contractul poate fi folosit și fără Point of Sale. Nu adaugă ecrane proprii.

#### 2. Funcționalități Cheie

- Câmpuri de audit fiscal, doar în citire și necopiate la duplicare:
  - **Bon fiscal (BF):** numărul bonului în cadrul raportului Z curent, care se reia la fiecare Z.
  - **Document fiscal (NR):** număr unic pe aparat; se folosește când documentul trebuie identificat fără ambiguitate.
  - **Raport Z:** numărul raportului Z din care face parte bonul.
  - **Stare fiscală:** rezultatul raportat de driverul aparatului.
  - **Eroare fiscală:** mesajul de eroare, când aparatul a refuzat sau a eșuat.
- Câmpurile sunt aplicate pe **notele contabile / facturi** (`account.move`) aici și pe **comenzile POS** prin `deltatech_pos`, folosind mixinul abstract `deltatech.ecr.fiscal.mixin`.
- Un driver de casă de marcat care vrea să scrie câmpurile moștenește mixinul pe modelul său; pentru simpla citire este suficientă declararea modulului în `depends`, fără modulele driverului.
- Migrare fără pierderi: la instalare, un `pre_init_hook` preia înregistrările `ir_model_data` ale vechilor proprietari (`deltatech_pos`, `deltatech_sale_store`), astfel încât coloanele și numerele de bon deja înregistrate nu se pierd la actualizarea acestora.

#### 3. Dependențe

- `account`

#### 4. Componente Cheie

**Modele**

- `deltatech.ecr.fiscal.mixin` (abstract): definește câmpurile `fiscal_receipt_number`, `fiscal_doc_number`, `fiscal_z`, `fiscal_state`, `fiscal_error`.
- `account.move`: moștenește mixinul. Prin `_inherits`, câmpurile sunt disponibile și pe `account.bank.statement.line`.

**Vizualizări**

- Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

- Nu există. Singura logică activă este `pre_init_hook` (`hooks.py`), care mută proprietatea câmpurilor de la `deltatech_pos` (`pos.order`) și `deltatech_sale_store` (`account.move`, `account.bank.statement.line`).

#### 5. Conexiuni

- [deltatech_pos](../deltatech_pos/index.md): aplică mixinul pe `pos.order` și scrie câmpurile după tipărire.
- [deltatech_sale_store](../deltatech_sale_store/index.md): alternativa de magazin fără POS; scrie câmpurile pe facturi.
- [l10n_ro_pos_fiscal_compliance_ecr](../l10n_ro_pos_fiscal_compliance_ecr/index.md): depinde de modul și traduce starea driverului în starea fiscală AMEF.
