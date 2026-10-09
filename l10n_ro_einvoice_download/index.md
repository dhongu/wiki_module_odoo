# Invoice Files Export (Export fișiere facturi SPV)

- **Nume Tehnic:** `l10n_ro_einvoice_download`
- **Versiune:** `19.0.0.0.4`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/19.0/l10n_ro_einvoice_download
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_einvoice_download`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă un asistent care exportă, într-o singură arhivă ZIP, fișierele atașate mesajelor SPV descărcate de la ANAF (e-Factura). Este util pentru predarea periodică a facturilor primite către departamentul de contabilitate sau către un furnizor extern de servicii contabile.

#### 2. Funcționalități Cheie

- Asistentul „Export Attachments" este disponibil ca acțiune din listă pe **Mesaje SPV** (selectezi mesajele, apoi acțiunea din meniul de acțiuni).
- **Grupare după CUI** (activă implicit): fișierele sunt puse în câte un director numit după codul fiscal al partenerului comercial al facturii, ca arhiva să rămână lizibilă când conține mai mulți parteneri. Mesajele fără factură atașată sau cu partener fără CUI ajung în directorul `no_vat`.
- **Ce se descarcă**: `All` (implicit), `Only zip` (arhiva semnată ANAF) sau `Only PDF` (randarea PDF de la ANAF).
- Rezultatul este un fișier `attached_files.zip`, descărcabil direct din asistent după pasul „Apply".
- Stare Beta; modelul tranzitoriu este accesibil oricărui utilizator intern.

#### 3. Dependențe

- `account`
- `l10n_ro_message_spv`

#### 4. Componente Cheie

**Modele**

- `invoice.files.export` (model tranzitoriu): asistentul de export; câmpurile `group_by_vat`, `files_to_download`, `data_file`, `name`, `state`; metoda `do_export` construiește arhiva ZIP din atașamentele `attachment_id` și `attachment_anaf_pdf_id` ale mesajelor SPV selectate.

**Vizualizări**

- `view_working_days_export_form`: formularul asistentului, cu două stări (alegerea opțiunilor, apoi descărcarea fișierului).

**Acțiuni Automate / Acțiuni Server**

- `action_invoice_files_export`: acțiune de fereastră legată (binding) de lista modelului `l10n.ro.message.spv`. Nu există cron-uri.

#### 5. Conexiuni

- `l10n_ro_message_spv`: sursa mesajelor și a atașamentelor exportate (descărcate din SPV/ANAF).
