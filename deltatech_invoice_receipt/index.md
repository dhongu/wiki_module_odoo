# Invoice Receipt (localizat la `deltatech_invoice_receipt/index.md`)

- **Nume Tehnic:** `deltatech_invoice_receipt`
- **Versiune:** `19.0.2.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_invoice_receipt
- **Cale Locală:** `odoo-addons/deltatech/deltatech_invoice_receipt`
- **Ultima Ingestie:** `2026-11-04`

#### 1. Sumar

Modulul permite recepția mărfii în stoc pornind de la factura de furnizor: când factura conține produse stocabile care nu se află pe nicio comandă de achiziție, modulul creează comanda de achiziție, iar recepția se validează la postarea facturii. Elimină introducerea manuală a acestor documente și păstrează coerența dintre documentele contabile și cele de stoc, mai ales când factura sosește înaintea recepției.

#### 2. Funcționalități Cheie

- **Comandă de achiziție creată din factură**: la **Confirmă** pe o factură de furnizor, fiecare linie cu produs stocabil care nu e legată de o comandă de achiziție este pusă pe o comandă: una nouă, cu furnizorul, data, referința, poziția fiscală și moneda facturii, sau, dacă celelalte linii ale facturii provin deja dintr-o singură comandă, acea comandă. Liniile comenzii preiau produsul, unitatea, cantitatea, prețul unitar, discountul și taxele liniilor facturii, iar liniile facturii se leagă de ele. Pe factură se postează o notă cu link către comanda nouă. Dacă lipsește data facturii, apare eroare.
- **Confirmarea comenzii, apoi postarea facturii**: comanda nouă rămâne cerere de ofertă, deci postarea se oprește cu mesajul *Please confirm purchase order before posting invoice*. Se deschide comanda, se apasă **Confirmă comanda**, apoi se apasă din nou **Confirmă** pe factură.
- **Recepție validată odată cu factura**: la postarea facturii se validează recepțiile comenzilor create din facturi, cu cantitățile comandate, iar mișcările de stoc sunt datate la data comenzii (data facturii).
- **Cantități negative pe comanda de achiziție**: o linie cu cantitate negativă a unui produs stocabil creează, la confirmarea comenzii, un transfer separat de retur către furnizor, cu tipul de operațiune de retur al recepției. Dacă ulterior se mărește cantitatea negativă, se adaugă la retur doar diferența.
- Limitări: comanda și recepția automate funcționează doar pentru facturile de furnizor (notele de credit nu se procesează la postare); liniile adăugate pe o comandă obișnuită (nu cea creată din factură) nu se recepționează automat; comanda nu se confirmă automat.

#### 3. Dependențe

- `purchase_stock`

#### 4. Componente Cheie

Funcționalitățile provin din `readme/DESCRIPTION.md`; mai jos sunt reperele confirmate în cod.

**Modele**

- `account.move` (extins în `models/account_invoice.py`): `action_post` verifică comanda de achiziție și recepționează la postare; `add_to_purchase` creează sau completează comanda; `get_purchase_from_invoice` găsește comenzile generate din factură.
- `purchase.order` (extins în `models/purchase.py`): câmpul `from_invoice_id` („Generated from the invoice”), `receipt_to_stock` (validează recepția) și `_create_picking` (transferul de retur pentru linii negative).
- `purchase.order.line` (extins): `_prepare_stock_moves` produce mișcările de retur pentru cantități negative.
- `stock.picking` (extins): câmpul boolean `notice`.

**Vizualizări**

- Niciuna (fișierele de vizualizări sunt comentate în manifest).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): acoperă fluxul invers, crearea facturilor pornind din livrări, completând aprovizionarea bazată pe factură oferită de acest modul.
