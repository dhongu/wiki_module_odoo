# Terrabit Base (localizat la `terrabit_base/index.md`)

- **Nume Tehnic:** `terrabit_base`
- **Versiune:** `20.0.1.3.0`
- **Cale:** https://github.com/terrabit-solutions/terrabit/tree/20.0/terrabit_base
- **Cale Locală:** `odoo-addons/terrabit/terrabit_base`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Meta-modul care instalează dintr-o singură mișcare setul de bază folosit la clienții Terrabit din România: stoc, vânzări, achiziții, contabilitate, modulele Deltatech uzuale și localizarea românească (inclusiv e-Factura și mesajele SPV). Nu adaugă cod propriu; rolul lui este să ofere o configurare de pornire consecventă pentru o bază de date nouă.

#### 2. Funcționalități Cheie

- Aduce aplicațiile standard de stoc (cu evaluare și costuri de achiziție), vânzări, achiziții și contabilitate (`accountant`).
- Include utilitare Deltatech: blocarea creării rapide, procese de afaceri, inventar de stoc și buton de creare factură din achiziție.
- Include localizarea românească Odoo și OCA (`l10n_ro`, `l10n_ro_edi`, `l10n_ro_city`) și extensiile Terrabit: e-Factura, taxare inversă pe servicii, rapoarte de factură și de livrare, registru de casă.
- Include importul facturilor de achiziție UBL și mesajele SPV pentru achiziții.
- Nu are fișă de consultant; nu are descriere detaliată în `readme/` (DESCRIPTION.md conține doar un titlu).

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
- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md)
- [l10n_ro_service_tax](../l10n_ro_service_tax/index.md)
- [l10n_ro_invoice_report](../l10n_ro_invoice_report/index.md)
- [l10n_ro_picking_report](../l10n_ro_picking_report/index.md)
- [l10n_ro_cash_register](../l10n_ro_cash_register/index.md)
- [deltatech_purchase_ubl](../deltatech_purchase_ubl/index.md)
- [l10n_ro_message_spv_purchase](../l10n_ro_message_spv_purchase/index.md)

#### 4. Componente Cheie

**Modele**

- Niciunul; modulul nu definește modele.

**Vizualizări**

- Niciuna.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md): extensii e-Factura incluse în pachet.
- [l10n_ro_message_spv_purchase](../l10n_ro_message_spv_purchase/index.md): mesaje SPV pentru achiziții.
