# Romania - Taxa verde pe analitic

- **Nume Tehnic:** `l10n_ro_green_tax_analytic`
- **Versiune:** `20.0.0.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_green_tax_analytic
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_green_tax_analytic`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Taxa verde (DEEE) fără linie separată pe comenzi și facturi. Produsul are o categorie de taxă verde dintr-un catalog (valoare pe unitate și cont analitic); la validarea transferului, taxa se înregistrează în analitic, într-un plan dedicat „Taxă verde”, iar pe factura către client se adaugă o notă cu valoarea inclusă în preț.

#### 2. Funcționalități Cheie

- **Catalog de categorii** în **Contabilitate → Configurare → Contabilitate → Categorii taxă verde**: nume, valoare pe unitate (în moneda companiei) și cont analitic din planul „Taxă verde”; pe produs se alege în fila **Contabilitate**.
- **Înregistrare la validarea transferului**, pe tipurile de operații cu bifa **Înregistrează taxa verde în analitic**: cantitate livrată × valoare; pozitivă la livrare, dropshipping sau consum, negativă la retur de la client; recepțiile de la furnizori nu produc linii.
- **Valoare înghețată** la validare; fără cont analitic pe categorie, validarea se oprește cu un mesaj explicit.
- **Notă pe factură**: sub fiecare linie cu produs cu categorie, la postarea facturii sau a storno-ului către client; notele se refac la fiecare postare, fără duplicate. Textul se setează pe compania (fila **Taxă verde**), cu `{valoare}` și `{valoare_unitara}`.
- **Raport** în **Contabilitate → Raportare → Management → Taxă verde** (analitice filtrate pe plan).
- Modulul creează doar planul analitic, nu și conturile; cere Contabilitate analitică activă. Se exclude cu `l10n_ro_green_stamp`. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `stock`
- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n_ro.green.tax.category`: catalogul categoriilor de taxă verde.
- `stock.picking`, `stock.picking.type`: înregistrarea taxei la validare, bifa pe tipul de operație.
- `account.analytic.line`: liniile analitice ale taxei.
- `account.move`: nota de taxă verde pe factură.
- `product.template`, `res.company`: categoria pe produs și textul notei.

**Vizualizări**

- `green_tax_category_view_list` / `_form`: categoriile.
- `product_template_form_view_green_tax`, `view_picking_type_form_green_tax`, `view_company_form_green_tax`: câmpurile adăugate.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook`: inițializare la instalare; planul analitic vine din `data/analytic_plan.xml`.

#### 5. Conexiuni

- [l10n_ro_green_stamp](../l10n_ro_green_stamp/index.md): alternativă cu timbru verde pe linie separată; se exclud reciproc.
- [l10n_ro_green_tax_analytic_edi](../l10n_ro_green_tax_analytic_edi/index.md): duce nota de taxă verde în XML-ul e-Factura.
