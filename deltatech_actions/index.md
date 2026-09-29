# Deltatech Actions (localizat la `deltatech_actions/index.md`)

- **Nume Tehnic:** `deltatech_actions`
- **Versiune:** `19.0.0.9.3`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_actions
- **Cale Locală:** `odoo-addons/deltatech/deltatech_actions`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul Deltatech Actions este un set de acțiuni programate (cron) de mentenanță care mențin o bază de date Odoo curată și performantă: eliminarea atașamentelor duplicate sau vechi (XML ANAF, PDF-uri de facturi, comenzi de vânzare și livrări, etichete AWB), ștergerea mesajelor vechi din chatter, unirea contactelor și companiilor duplicate, crearea regulilor de reaprovizionare lipsă și normalizarea denumirilor de firme. Toate sarcinile sunt gândite să fie sigure: vin dezactivate implicit, iar cele care șterg date rulează în mod „dry run” (doar loghează ce ar șterge) până când administratorul le activează conștient. Tot controlul se face dintr-o secțiune dedicată, **Database Cleanup**, din Setări > Setări generale.

#### 2. Funcționalități Cheie

- **Curățări programate** (toate dezactivate implicit, cu `dry_run` activ acolo unde se șterg date):
  - *Delete duplicate xml attachments* – șterge atașamentele XML (EDI/ANAF) duplicate de pe facturi; parametri: facturi pe rulare, număr minim de duplicate, ștergeri maxime per factură, vechime în zile (o copie creată azi nu se atinge niciodată).
  - *Delete pdf invoice attachments* – șterge PDF-urile de factură vechi, inclusiv cele atașate mesajelor de e-mail trimise (unde se află de fapt marea majoritate a lor, câte o copie la fiecare retrimitere).
  - *Delete pdf sale order attachments* – același lucru pentru PDF-urile de comenzi/oferte de vânzare.
  - *Delete pdf pickings attachments* – golește eticheta AWB (`label_attachment`) de pe livrările vechi; se poate regenera de la curier, deci trebuie confirmată în prealabil perioada de retenție a curierului. Are comutatoare „doar livrări finalizate” / „doar livrări anulate” (ambele active implicit).
  - *Delete mail messages* – șterge mesajele vechi din chatter și atașamentele lor non-ANAF; modelele excluse implicit: `business.%`, `project.%`, `helpdesk.%`.
  - *Merge duplicate contacts by email* și *Merge duplicate companies by VAT* – unesc duplicatele prin `base.partner.merge.automatic.wizard`; **fără dry run**, doar prin cron.
  - *Create missing reordering rules (0/0)* – creează regulile de reaprovizionare lipsă (necesită `deltatech_auto_reorder_rule`).
  - *Normalize company names* – standardizează formele juridice (SRL → S.R.L., SA → S.A., PFA → P.F.A., II → I.I.), până la 500 de înregistrări pe rulare.
- **Activare din Setări** (Setări generale > Database Cleanup): bifa fiecărei curățări este legată direct de câmpul `active` al cron-ului; se poate vedea și modifica data următoarei execuții (`nextcall`). Un cron dezactivat de la instalare păstrează un `nextcall` vechi și pornește la primul tick după activare.
- **Buton „Run now”** pentru curățările cu dry run: salvează setările, rulează curățarea pe loc și raportează într-o notificare câte înregistrări (și ce volum) ar fi șterse sau au fost șterse. Fuziunile de parteneri nu au buton, intenționat.
- **Rulare din auto-vacuum** (opțional, dezactivat implicit): curățările de facturi, comenzi și etichete AWB pot rula și din jobul zilnic de auto-vacuum al Odoo, util pe copii restaurate/neutralizate unde toate cron-urile sunt oprite. Hook-urile raportează dimensiunea reală a lotului (evită dezactivarea jobului de auto-vacuum) și nu cer reluare dacă timpul rămas e insuficient; un dry run nu cere niciodată reluare.
- **Cron-uri fără argumente în cod**: parametrii se citesc din parametrii de sistem `deltatech_actions.*` (setați din ecranul de Setări); o migrare a rescris cron-urile existente și a preluat argumentele vechi în parametri.
- **Corecții de robustețe**: un atașament cu `file_size` NULL nu mai oprește curățarea; interogările SQL pentru XML-uri și PDF-uri de livrări sunt construite cu `SQL()`; suprascrierile care apelau `super()` îi returnează acum rezultatul.
- **Anulare forțată a unei comenzi de vânzare** (`force_cancel_order_and_moves`): anulează comanda împreună cu livrările, mișcările de stoc, liniile de mișcare și mișcările contabile, scriind direct starea `cancel` (ocolește verificările normale). Din motive de securitate trebuie legată manual de o acțiune server (Setări > Tehnic > Acțiuni > Acțiuni server, model `Sale Order`, cod Python `record.force_cancel_order_and_moves()`).
- Modulul are pictogramă proprie (din 19.0.0.9.3).

#### 3. Dependențe

- `account_edi`
- `sale`
- `sale_stock`
- `product`
- `stock`

Dependență funcțională opțională (pentru crearea regulilor de reaprovizionare): [deltatech_auto_reorder_rule](../deltatech_auto_reorder_rule/index.md).

#### 4. Componente Cheie

**Acțiuni Automate / Acțiuni Server**

Cron-urile sunt definite în `data/ir_cron_data.xml` (fișier `noupdate`), dezactivate implicit și fără argumente în cod; parametrii vin din setări.

- `Delete duplicate xml attachments`, `Delete pdf invoice attachments` (`account.move`)
- `Delete pdf sale order attachments` (`sale.order`)
- `Delete pdf pickings attachments` (`stock.picking`)
- `Delete mail messages` (`mail.message`)
- `Merge duplicate contacts by email`, `Merge duplicate companies by VAT`, `Normalize company names` (`res.partner`)
- `Create missing reordering rules (0/0)` (`product.product`)
- `force_cancel_order_and_moves` (`sale.order`): metodă de service, expusă doar printr-o acțiune server creată manual.

**Modele extinse și fișiere**

- `models/account_move.py`, `sale_order.py`, `stock_picking.py`, `mail_message.py`, `product.py`, `res_partner.py`: logica curățărilor și a normalizărilor.
- `models/res_config_settings.py` și `views/res_config_settings_views.xml`: secțiunea Database Cleanup din Setări generale (parametri, dry run, „Run now”, data următoarei execuții).
- `models/cleanup_summary.py`: funcții ajutătoare (sumarul din notificarea „Run now”, prefixul de log, rularea din auto-vacuum).

#### 5. Conexiuni

- [deltatech_auto_reorder_rule](../deltatech_auto_reorder_rule/index.md): necesar pentru cron-ul de creare a regulilor de reaprovizionare lipsă.
- [deltatech_delivery](../deltatech_delivery/index.md): eticheta AWB ștearsă din `label_attachment` se poate regenera cu `carrier_generate_label()` din acest modul, pe baza `carrier_tracking_ref`.
