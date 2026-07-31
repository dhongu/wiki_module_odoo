# Deltatech UBL Despatch Advice (localizat la `deltatech_account_edi_ubl_advice/index.md`)

- **Nume Tehnic:** `deltatech_account_edi_ubl_advice`
- **Versiune:** `19.0.1.0.1`
- **Cale:** `https://github.com/dhongu/deltatech/tree/19.0/deltatech_account_edi_ubl_advice`
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_edi_ubl_advice`
- **Ultima Ingestie:** `2026-07-31`

#### 1. Sumar

Modulul îmbogățește facturile electronice (e-Factura) emise în format UBL cu referințe către documentele de livrare aferente. Când o factură de client este generată ca UBL, modulul identifică avizele de expediție (`stock.picking`) validate, legate de liniile facturii prin liniile comenzii de vânzare, și le adaugă în XML-ul facturii ca nod `cac:DespatchDocumentReference`. Astfel, destinatarul poate urmări direct din factura electronică ce avize de expediție acoperă factura respectivă.

#### 2. Funcționalități Cheie

- Adaugă nodul `cac:DespatchDocumentReference` în facturile UBL emise către clienți.
- Colectează automat referințele avizelor de expediție din livrările validate legate de factură.
- Funcționează transparent peste exportul standard de e-Factură UBL/CII, fără configurare suplimentară.

#### 3. Dependențe

- `account_edi_ubl_cii`

#### 4. Componente Cheie

> Conform `readme/DESCRIPTION.md`, secțiunile de business sunt acoperite mai sus. Componenta tehnică de mai jos este menționată doar pentru orientare, fiind un singur fișier de extindere punctuală.

**Modele**

- `account.edi.xml.ubl_bis3` (extindere, model abstract): suprascrie `_add_invoice_header_nodes` pentru a aduna avizele de expediție (`stock.picking` în starea `done`) legate de factură prin liniile comenzii de vânzare și a le insera ca nod `cac:DespatchDocumentReference`. Extinderea se agață de `ubl_bis3` (baza folosită la exportul CIUS-RO) și nu de `ubl_20`, deoarece în Odoo 19 metoda respectivă din `ubl_bis3` este un override care nu mai apelează `super()`.

#### 5. Conexiuni

- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md): extinde, la fel ca acest modul, clasa abstractă `account.edi.xml.ubl_bis3` — baza folosită și de exportul CIUS-RO (`account.edi.xml.ubl_ro`, definit în modulul standard `l10n_ro_edi`); ambele module coexistă peste același lanț de export UBL pentru e-Factura românească.
