# UBL Despatch Advice (localizat la `deltatech_account_edi_ubl_advice/index.md`)

- **Nume Tehnic:** `deltatech_account_edi_ubl_advice`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_account_edi_ubl_advice
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_edi_ubl_advice`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul completează facturile electronice UBL emise (e-Factura) cu o referință către documentele de livrare din spatele fiecărei facturi. Când o factură de client este generată ca UBL, se caută livrările validate (`stock.picking` în starea *done*) legate de liniile facturii prin liniile comenzii de vânzare, iar referințele lor sunt adăugate în XML. Astfel destinatarul poate afla, direct din factura electronică, ce avize de însoțire a mărfii acoperă factura.

#### 2. Funcționalități Cheie

- Adaugă nodul `cac:DespatchDocumentReference` în facturile UBL de client emise.
- Colectează automat referințele livrărilor validate, legate prin liniile comenzii de vânzare; mai multe livrări sunt listate separat prin virgulă.
- Lucrează transparent peste exportul standard UBL/CII, fără configurare suplimentară.
- Se aplică doar facturilor de client (`out_invoice`); fără modulele `sale`/`stock`/`sale_stock` exportul continuă normal, fără referința la aviz.
- Cerință: livrările trebuie să fie legate de factură prin fluxul de vânzări.

#### 3. Dependențe

- `account_edi_ubl_cii`

#### 4. Componente Cheie

**Modele**

- `account.edi.xml.ubl_bis3` (extindere, model abstract): suprascrie `_add_invoice_header_nodes` pentru a aduna livrările validate și a insera nodul `cac:DespatchDocumentReference`. Extinderea se agață de `ubl_bis3` (baza exportului CIUS-RO), deoarece metoda din `ubl_bis3` nu mai apelează `super()` și un patch pe `ubl_20` nu ar fi executat.

**Vizualizări**

Modulul nu definește vizualizări.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md): extinde, la fel, clasa abstractă `account.edi.xml.ubl_bis3`; ambele module coexistă peste același lanț de export UBL pentru e-Factura românească.
