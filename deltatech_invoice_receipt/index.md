# Invoice Receipt (localizat la `deltatech_invoice_receipt/index.md`)

- **Nume Tehnic:** `deltatech_invoice_receipt`
- **Versiune:** `20.0.2.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_invoice_receipt
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_receipt`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Modulul permite primirea mărfii în stoc pornind de la factura de furnizor. Când o factură conține produse stocabile care nu sunt pe nicio comandă de achiziție, modulul creează comanda de achiziție, iar recepția se validează la postarea facturii. Elimină introducerea manuală a documentelor atunci când factura sosește înaintea recepției sau fluxul pornește direct de la factură.

#### 2. Funcționalități Cheie

- **Comandă de achiziție din factură:** la **Confirm** pe factură, liniile cu produse stocabile fără comandă se pun pe o comandă nouă (furnizor, data, referința, poziția fiscală și moneda facturii) sau pe comanda existentă, dacă restul liniilor provin dintr-una singură; liniile facturii se leagă de cele ale comenzii, iar pe factură se postează o notă cu link.
- **Confirmi comanda, apoi postezi factura:** comanda nouă este cerere de ofertă, deci postarea se oprește cu mesajul *Please confirm purchase order before posting invoice*; se confirmă comanda și se apasă din nou **Confirm** pe factură.
- **Recepție validată odată cu factura:** recepțiile comenzilor create din facturi se validează cu cantitățile comandate, iar mișcările de stoc au data comenzii (data facturii).
- **Cantități negative pe comanda de achiziție:** o linie cu cantitate negativă de produs stocabil generează la confirmare un transfer separat de retur către furnizor; mărirea ulterioară adaugă doar diferența.
- Limitări: doar facturi de furnizor (notele de credit nu sunt procesate), liniile adăugate pe comenzi obișnuite nu se recepționează automat, comanda nu se confirmă automat.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins în `models/account_invoice.py`): la postare creează comanda de achiziție din liniile facturii (`add_to_purchase`, `get_purchase_from_invoice`).
- `purchase.order` (extins în `models/purchase.py`): câmpul `from_invoice_id` (factura sursă), recepția în stoc (`receipt_to_stock`) și crearea transferului de retur pentru cantități negative.
- `purchase.order.line` (extins în `models/purchase.py`): pregătirea mișcărilor de stoc.
- `stock.picking` (extins): câmpul boolean `notice`.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): acoperă fluxul invers, crearea facturilor pornind de la recepții/livrări.
