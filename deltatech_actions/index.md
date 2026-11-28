# Database Cleanup Actions (localizat la `deltatech_actions/index.md`)

- **Nume Tehnic:** `deltatech_actions`
- **Versiune:** `20.0.0.9.11`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_actions
- **Cale Locală:** `odoo-addons/deltatech/deltatech_actions`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un set de acțiuni programate (cron) de mentenanță, care mențin baza de date Odoo curată și rapidă: ștergerea atașamentelor duplicate sau vechi, curățarea mesajelor din chatter, unirea contactelor duplicate sau crearea regulilor de reaprovizionare lipsă. Toate sarcinile sunt prudente: vin **dezactivate** și, cele care șterg date, rulează implicit în mod **dry run** (doar consemnează ce s-ar șterge) până când administratorul le activează conștient.

#### 2. Funcționalități Cheie

- Ștergerea fișierelor XML (EDI/ANAF) duplicate de pe facturi — *Delete duplicate xml attachments* (implicit: 10 facturi/rulare, minimum 10 duplicate, maximum 50 ștergeri/factură, mai vechi de 30 de zile).
- Ștergerea PDF-urilor generate vechi de pe facturi, inclusiv a celor atașate mesajelor de e-mail — *Delete pdf invoice attachments*.
- Ștergerea PDF-urilor vechi de pe comenzile de vânzare — *Delete pdf sale order attachments*.
- Golirea etichetelor AWB (`label_attachment`) de pe livrările vechi încheiate — *Delete pdf pickings attachments*; eticheta se poate regenera de la curier, dar verificați perioada de păstrare a curierului înainte de activare.
- Ștergerea mesajelor vechi din chatter, cu atașamentele non-ANAF — *Delete mail messages* (modelele `business.%`, `project.%`, `helpdesk.%` sunt excluse implicit).
- Crearea regulilor de reaprovizionare lipsă pentru produsele stocabile — *Create missing reordering rules (0/0)* (cere `deltatech_auto_reorder_rule`).
- Unirea contactelor duplicate după e-mail și a companiilor duplicate după CUI — *Merge duplicate contacts by email* / *Merge duplicate companies by VAT*; **fără dry run** și fără cale de întoarcere, deci doar cron, fără buton *Run now*.
- Normalizarea sufixelor din denumirile firmelor (SRL → S.R.L., SA → S.A., PFA → P.F.A.) — *Normalize company names*, 500 înregistrări/rulare.
- Anularea forțată a unei comenzi de vânzare cu toate livrările, mișcările de stoc și notele contabile (`force_cancel_order_and_moves`), printr-o acțiune de server creată manual (**Setări → Tehnic → Acțiuni → Acțiuni server**, cod `record.force_cancel_order_and_moves()`); ocolește verificările normale.
- Totul se gestionează din secțiunea **Database Cleanup** din **Setări → General**: bifa de activare, caseta *Dry run*, data următoarei rulări și butonul **Run now**, care raportează câte înregistrări (și ce volum) ar fi șterse.

Pașii detaliați, capturile și avertismentele sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account_edi`
- `sale`
- `sale_stock`
- `product`
- `stock`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): curățarea XML-urilor duplicate și a PDF-urilor de factură.
- `sale.order` (extins): curățarea PDF-urilor și `force_cancel_order_and_moves`.
- `stock.picking` (extins): curățarea etichetelor AWB.
- `mail.message` (extins): curățarea mesajelor vechi.
- `product.product` (extins): `create_missing_orderpoint`.
- `res.partner` (extins): unirea contactelor/companiilor și normalizarea denumirilor.
- `res.config.settings` (extins): setările și butoanele *Run now* ale curățărilor.

**Vizualizări**

- `res_config_settings_view_form`: secțiunea *Database Cleanup* din Setări.

**Acțiuni Automate / Acțiuni Server**

Definite în `data/ir_cron_data.xml`, toate dezactivate implicit:

- `ir_cron_delete_xml_attachments`: XML duplicate de pe facturi.
- `ir_cron_delete_pdf_attachments_invoice`: PDF-uri vechi de factură.
- `ir_cron_delete_pdf_attachments_sale_order`: PDF-uri vechi de comenzi de vânzare.
- `ir_cron_delete_pdf_attachments_stock_picking`: etichete AWB vechi.
- `ir_cron_delete_mail_messages`: mesaje vechi din chatter.
- `ir_cron_create_missing_reordering_rules`: reguli de reaprovizionare lipsă.
- `ir_cron_merge_contacts` / `ir_cron_merge_companies`: unirea duplicatelor.
- `cron_normalize_company_names`: normalizarea denumirilor de firme.

#### 5. Conexiuni

- [deltatech_auto_reorder_rule](../deltatech_auto_reorder_rule/index.md): necesar pentru crearea regulilor de reaprovizionare lipsă.
- [deltatech_delivery](../deltatech_delivery/index.md): etichetele AWB golite se regenerează prin `carrier_generate_label()` din acest modul.
