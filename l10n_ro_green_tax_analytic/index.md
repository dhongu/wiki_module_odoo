# Romania - Taxa verde pe analitic (localizat la `l10n_ro_green_tax_analytic/index.md`)

- **Nume Tehnic:** `l10n_ro_green_tax_analytic`
- **Versiune:** `19.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_green_tax_analytic
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_green_tax_analytic`
- **Ultima Ingestie:** `2026-11-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul gestionează taxa verde (DEEE) fără linie separată pe comenzi și facturi. Fiecare produs are o categorie de taxă verde dintr-un catalog (valoare per unitate și cont analitic). La validarea transferului, taxa se înregistrează în analitic, într-un plan dedicat „Taxă verde”, iar pe factura către client se adaugă o notă cu valoarea inclusă în preț. Este o alternativă la [l10n_ro_green_stamp](../l10n_ro_green_stamp/index.md) (timbru verde pe linie separată); cele două module se exclud reciproc.

#### 2. Funcționalități Cheie

- **Catalog de categorii** (Contabilitate → Configurare → Contabilitate → Categorii taxă verde): nume, valoare per unitate în moneda companiei și cont analitic din planul „Taxă verde”; contul trebuie să aparțină aceleiași companii (sau să fie fără companie). Categoria se alege pe produs, în fila Contabilitate.
- **Plan analitic dedicat „Taxă verde”**: creat de modul; conturile analitice (câte unul pe categorie) se creează manual. Necesită Contabilitate Analitică activată.
- **Înregistrare la validarea transferului**, doar pe tipurile de operații bifate cu „Înregistrează taxa verde în analitic”: cantitate livrată (în UM-ul produsului) × valoarea din categorie.
  - Sensul îl dau locațiile mișcării: spre client (livrare, dropshipping) sau spre producție (bon de consum) linia e pozitivă; de la client (retur) e negativă.
  - Recepțiile de la furnizori, retururile la furnizori și produsele fără categorie nu produc linii.
- **Validare protejată**: dacă o categorie nu are cont analitic din planul „Taxă verde”, validarea se oprește cu mesaj ce indică produsul, categoria și transferul.
- **Valoare înghețată** la validare: modificările ulterioare ale categoriei nu afectează liniile vechi.
- **Notă pe factura/storno către client**, sub fiecare linie cu categorie, refăcută la fiecare postare (fără duplicate după resetarea la draft). Textul se setează pe fișa companiei, fila Taxă verde, cu marcajele `{valoare}` (total linie) și `{valoare_unitara}` (valoare nominală pe unitate); gol = fără notă; traducere din butonul de limbi.
- **Raport**: Contabilitate → Raportare → Management → Taxă verde (analiticele standard filtrate pe planul „Taxă verde”).

#### 3. Dependențe

- `stock`
- `account`
- `l10n_ro`
- Exclude: [l10n_ro_green_stamp](../l10n_ro_green_stamp/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro.green.tax.category`: catalogul categoriilor de taxă verde (valoare, cont analitic, companie).
- `product.template` (extins): categoria de taxă verde a produsului.
- `stock.picking.type` (extins): bifa „Înregistrează taxa verde în analitic”.
- `stock.picking` (extins): generează liniile analitice la validare.
- `account.analytic.line` (extins): legătura liniei cu taxa verde/transferul.
- `account.move` (extins): adaugă notele de taxă verde la postare.
- `res.company` (extins): textul notei de pe factură.

**Vizualizări**

- `green_tax_category_view_list` / `green_tax_category_view_form`: administrarea categoriilor.
- `product_template_form_view_green_tax`: câmpul categoriei pe produs.
- `view_picking_type_form_green_tax`: bifa pe tipul de operație.
- `view_company_form_green_tax`: fila Taxă verde pe companie.

**Acțiuni Automate / Acțiuni Server**

- `green_tax_report_action`: acțiune server pentru raportul Taxă verde (meniu `green_tax_report_menu`).
- `post_init_hook`: inițializare la instalare.

#### 5. Conexiuni

- [l10n_ro_green_stamp](../l10n_ro_green_stamp/index.md): alternativă (timbru verde pe linie separată), exclusă reciproc prin manifest.
