# Logistic Documents (localizat la `deltatech_logistic_docs/index.md`)

- **Nume Tehnic:** `deltatech_logistic_docs`
- **Versiune:** `20.0.1.0.5`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_logistic_docs
- **Cale Locală:** `odoo-addons/deltatech/deltatech_logistic_docs`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Documentele de transport (CMR, certificate de origine, avize semnate) sunt adesea atașate altui document decât cel deschis de utilizator: CMR-ul pe livrare, certificatul pe comanda de achiziție, PDF-ul furnizorului pe factură. Modulul arată, din orice document din flux, și fișierele atașate documentelor înrudite.

#### 2. Funcționalități Cheie

- Buton **Documents** pe comanda de vânzare, comanda de achiziție, transfer și factură/factură furnizor, cu numărul de atașamente găsite pe flux; se deschid în kanban, listă sau formular.
- Atașamente colectate pe flux: la comanda de vânzare, ale ei, ale transferurilor și ale facturilor; la comanda de achiziție, ale ei, ale recepțiilor și ale facturilor; la transfer, ale lui, ale comenzii asociate și ale facturilor comenzii; la factură, ale ei și ale comenzilor de vânzare/achiziție din linii, cu transferurile lor (la alte note contabile, doar propriile atașamente).
- Un atașament creat din vizualizarea deschisă de buton se leagă implicit de documentul de pe care s-a apăsat butonul.
- Buton **Download** pe cardul kanban al atașamentului; fișierele `.zplpdf` se descarcă ca date brute, pentru imprimante de etichete.
- Fără meniu și fără configurare.

#### 3. Dependențe

- `purchase_stock`
- `sale_stock`

#### 4. Componente Cheie

Secțiunile 1 și 2 provin din `readme/DESCRIPTION.md`, care nu cere analiza componentelor. Modulul extinde `stock.picking`, `sale.order`, `purchase.order`, `account.move`, `ir.attachment` și `ir.actions.report`, cu vizualizările aferente (`view_picking_form`, `view_order_form`, `purchase_order_form`, `view_move_form`, `view_document_file_kanban`).

#### 5. Conexiuni

- [deltatech_invoice_picking](../deltatech_invoice_picking/index.md): leagă livrările de facturi, completând fluxul Comandă → Livrare → Factură folosit de acest modul.
