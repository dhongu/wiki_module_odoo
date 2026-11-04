# Logistic Documents (localizat la `deltatech_logistic_docs/index.md`)

- **Nume Tehnic:** `deltatech_logistic_docs`
- **Versiune:** `19.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_logistic_docs
- **Cale Locală:** `odoo-addons/deltatech/deltatech_logistic_docs`
- **Ultima Ingestie:** `2026-11-04`

#### 1. Sumar

Documentele de expediere (CMR, certificate de origine, avize semnate) sunt adesea atașate altei înregistrări decât cea deschisă de utilizator: CMR-ul pe livrare, certificatul pe comanda de achiziție, PDF-ul furnizorului pe factură. Modulul arată, din orice document al fluxului, și fișierele atașate documentelor înrudite, astfel încât echipele de logistică găsesc într-un singur loc tot ce ține de o expediere sau o tranzacție.

#### 2. Funcționalități Cheie

- **Buton inteligent „Documents”** pe formularul comenzii de vânzare, comenzii de achiziție, transferului și facturii sau facturii de furnizor. Arată numărul de atașamente găsite de-a lungul fluxului și le deschide în vizualizare kanban, listă sau formular.
- **Atașamente colectate de-a lungul fluxului**:
    - *Comanda de vânzare*: atașamentele proprii, ale transferurilor și ale facturilor ei.
    - *Comanda de achiziție*: atașamentele proprii, ale recepțiilor și ale facturilor de furnizor.
    - *Transferul*: atașamentele proprii, ale comenzii de vânzare sau de achiziție asociate și ale facturilor comenzii.
    - *Factura sau factura de furnizor*: atașamentele proprii și ale comenzilor de vânzare și de achiziție legate de liniile ei, împreună cu transferurile lor. Pentru alte note contabile se numără doar atașamentele proprii.
- **Fișiere noi pe documentul potrivit**: un atașament creat din vizualizarea deschisă de buton este legat implicit de documentul pe care s-a apăsat butonul.
- **Buton „Download”** pe cardul kanban al atașamentului; fișierele cu extensia `.zplpdf` se descarcă ca date brute, pentru imprimantele de etichete.
- **Factura originală de furnizor**: dacă o factură de furnizor nu are atașament principal, raportul „Original Vendor Bill” folosește primul atașament găsit în fluxul documentelor.
- Modulul nu adaugă meniu și nu necesită configurare. Corecție față de descrierea veche: nu există un meniu central „Documente Logistică” și nici etichetare/categorizare a documentelor.

#### 3. Dependențe

- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

Funcționalitățile provin din `readme/DESCRIPTION.md`; mai jos sunt reperele confirmate în cod.

**Modele**

- `sale.order`, `purchase.order`, `stock.picking`, `account.move` (extinse): câmpul calculat `doc_count` („Number of documents attached”), `get_attachment_domain()` (domeniul atașamentelor de-a lungul fluxului) și `attachment_tree_view()` (deschide atașamentele).
- `ir.attachment` (extins): `button_download`.
- `ir.actions.report` (extins): `retrieve_attachment` pentru raportul `account.report_original_vendor_bill`.

**Vizualizări**

- `view_order_form` (`sale.view_order_form`), `purchase_order_form` (`purchase.purchase_order_form`), `view_picking_form` (`stock.view_picking_form`), `view_move_form` (`account.view_move_form`): adaugă butonul inteligent **Documents**.
- `view_document_file_kanban`: moștenește `mail.view_document_file_kanban` și adaugă butonul **Download**.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): leagă livrările de facturi, în același flux Comandă → Livrare → Factură de-a lungul căruia se adună atașamentele.
