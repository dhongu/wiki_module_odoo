# Terrabit Base

- **Nume Tehnic:** `terrabit_base`
- **Versiune:** `19.0.1.0.10`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/19.0/terrabit_base
- **Cale Locală:** `odoo-addons/terrabit/terrabit_base`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Terrabit Base este un modul de tip „metapachet": nu adaugă logică proprie, ci instalează dintr-o singură mișcare setul de bază de aplicații Odoo (stocuri, vânzări, achiziții, contabilitate) și modulele de localizare pentru România și extensiile Terrabit de care au nevoie aproape toți clienții locali. Valoarea lui este o configurare inițială rapidă și uniformă a unei baze de date noi.

#### 2. Funcționalități Cheie

Fișierul `readme/DESCRIPTION.md` nu conține decât titlul „Features:", așa că descrierea provine din `__manifest__.py` (sumar „Terrabit Base module with essential dependencies"). Modulul nu are modele, vizualizări sau cod Python; efectul lui vine exclusiv din dependențe:

- Fluxuri de bază pentru stocuri (inclusiv evaluarea stocului și costurile suplimentare de achiziție), vânzări și achiziții.
- Contabilitate (`accountant`) și localizarea română Odoo (`l10n_ro`, `l10n_ro_edi`) completată cu modulele OCA: orașe, configurare, creare parteneri după CUI, TVA la încasare, unicitate parteneri.
- Extensii Terrabit pentru România: îmbunătățiri e-Factura, rapoarte de factură și de livrare, registru de casă, buton de creare partener după CUI, mesaje SPV pentru achiziții.
- Module deltatech de uz general: blocarea creării rapide, procese de business, inventar de stoc, creare factură din comanda de achiziție, import UBL în achiziții.
- Modulul este marcat ca aplicație (`application: True`) și nu se instalează automat (`auto_install: False`).
- Câteva module sunt lăsate comentate în manifest (de ex. `l10n_ro_stock_account`, `l10n_ro_stock_report`, `l10n_ro_stock_account_notice`, `deltatech_sale_store`); nu fac parte din pachetul de bază și se instalează separat, după caz.

#### 3. Dependențe

- `stock`
- `stock_account`
- `stock_landed_costs`
- `sale`
- `sale_management`
- `purchase`
- `purchase_stock`
- `accountant`
- [deltatech_no_quick_create](../deltatech_no_quick_create/index.md)
- [deltatech_business_process](../deltatech_business_process/index.md)
- [deltatech_stock_inventory](../deltatech_stock_inventory/index.md)
- [deltatech_purchase_create_bill_button](../deltatech_purchase_create_bill_button/index.md)
- `l10n_ro_edi`
- `l10n_ro`
- `l10n_ro_city`
- `l10n_ro_config`
- `l10n_ro_partner_create_by_vat`
- `l10n_ro_vat_on_payment`
- `l10n_ro_partner_unique`
- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md)
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md)
- [l10n_ro_stock_picking_report](../l10n_ro_stock_picking_report/index.md)
- [l10n_ro_cash_register](../l10n_ro_cash_register/index.md)
- [l10n_ro_partner_create_by_vat_button](../l10n_ro_partner_create_by_vat_button/index.md)
- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md)
- [l10n_ro_message_spv_purchase](../l10n_ro_message_spv_purchase/index.md)

#### 4. Componente Cheie

**Modele**

Niciunul; modulul nu definește și nu extinde modele.

**Vizualizări**

Niciuna.

**Acțiuni Automate / Acțiuni Server**

Niciuna. Singurul fișier de date este `security/ir.model.access.csv`.

#### 5. Conexiuni

- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md): completează fluxul e-Factura din localizarea Odoo.
- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md): împreună cu mesajele SPV acoperă primirea facturilor de achiziție în format UBL.
