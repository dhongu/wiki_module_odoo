# Deltatech Invoice Receipt (localizat la `deltatech_invoice_receipt/index.md`)

- **Nume Tehnic:** `deltatech_invoice_receipt`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_receipt
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_receipt`
- **Ultima Ingestie:** `2026-06-02`

#### 1. Sumar

Modulul automatizează crearea documentelor de aprovizionare pornind de la o factură de achiziție. Atunci când o factură de furnizor este validată, modulul generează automat comanda de achiziție și recepția aferentă, eliminând introducerea manuală a acestor documente. Este util în situațiile în care factura sosește înaintea recepției efective sau când fluxul de lucru pornește direct de la factură, asigurând astfel coerența între documentele contabile și cele de stoc.

#### 2. Funcționalități Cheie

- Generarea automată a unei comenzi de achiziție și a unei recepții la validarea unei facturi de furnizor.
- Permite cantități negative în comanda de achiziție (necesar pentru ajustări sau retururi).

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins în `models/account_invoice.py`): logica de generare automată a comenzii de achiziție și a recepției la validarea facturii de furnizor.
- `purchase.order` / `purchase.order.line` (extins în `models/purchase.py`): suport pentru cantități negative în comanda de achiziție.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): acoperă fluxul invers — crearea facturilor pornind de la recepții/livrări — completând astfel aprovizionarea bazată pe factură oferită de acest modul.
