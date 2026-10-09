# Romania - Report Common (localizat la `l10n_ro_report_common/index.md`)

- **Nume Tehnic:** `l10n_ro_report_common`
- **Versiune:** `19.0.1.1.2`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_report_common
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_report_common`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul oferă elementele comune folosite de rapoartele tipărite românești (factură, comandă de vânzare, aviz de livrare, confirmare de sold): antetul de identificare al firmei, conturile bancare afișate pe document și suma în litere corectă gramatical în limba română. Astfel, documentele tipărite arată unitar, iar o sumă în lei poate fi citită direct pe chitanță sau factură (ex. „cinci sute de lei”, nu „Cinci Sute Leu”).

#### 2. Funcționalități Cheie

- Șablon QWeb `l10n_ro_report_common.banks`: tipărește până la 3 conturi bancare ale partenerului marcate „Print in Report”, în moneda documentului (cu revenire la moneda companiei).
- Șablon QWeb `l10n_ro_report_common.report_address_company`: bloc de identificare a companiei cu nume, adresă, conturi bancare, CUI, nr. Reg. Com. și capital social.
- Suma în litere pentru moneda RON (suprascrie `res.currency.amount_to_text`), cu regulile limbii române: *unu* devine *un* (un leu, un ban), acord la plural, legarea particulei *de* (cinci sute **de** lei, dar o sută unu lei), valori negative cu „minus”, rotunjire după precizia monedei.
- Formularea în litere nu depinde de limba de tipărire: o sumă în lei se citește în română și pe o factură în engleză. Pentru alte monede rămâne comportamentul standard Odoo.
- Câmp nou „Print in Report” pe conturile bancare și câmp „Share Capital” pe companie.
- Numele câmpurilor coincid cu cele din OCA `l10n_ro_config`, deci bazele migrate de pe stack-ul OCA își păstrează configurația fără migrare de date; ambele module pot fi instalate împreună.
- Necesită biblioteca Python `num2words` (>= 0.5.12); dacă lipsește, se folosește formularea implicită Odoo.

#### 3. Dependențe

- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `res.company` (extins): adaugă `l10n_ro_share_capital` (capital social).
- `res.partner.bank` (extins): adaugă `l10n_ro_print_report` (afișare cont în rapoarte).
- `res.currency` (extins): `amount_to_text` rescris pentru RON.

**Vizualizări**

- `view_company_form`: moștenește `base.view_company_form`, adaugă capitalul social.
- `view_partner_bank_form` / `view_partner_bank_tree`: adaugă bifa „Print in Report” pe formularul și lista conturilor bancare.
- `banks`, `report_address_company`: șabloane QWeb reutilizabile în rapoarte.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite.

#### 5. Conexiuni

- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md): factura folosește șabloanele comune (declară dependență de acest modul).
- [l10n_ro_sale_order_report](../l10n_ro_sale_order_report/index.md): comanda de vânzare folosește șabloanele comune (declară dependență de acest modul).
- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md): avizul/transferul folosește șabloanele comune (declară dependență de acest modul).
- `l10n_ro_config`: modul OCA cu aceleași câmpuri; coexistă fără conflict.
