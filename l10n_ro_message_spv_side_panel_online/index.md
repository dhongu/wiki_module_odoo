# Romania - Panou lateral mesaje SPV pentru Odoo Online

- **Nume Tehnic:** `l10n_ro_message_spv_side_panel_online`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_message_spv_side_panel_online
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_side_panel_online`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Vedere împărțită pentru mesajele e-Factura (SPV) și pe **Odoo Online**: lista sau cardurile mesajelor în stânga, iar în dreapta, într-un panou, factura așa cum e în XML. Modulul nu are cod Python și se importă ca arhivă zip; funcționează peste registrul `l10n_ro_message_spv_online` și panoul lateral `deltatech_web_side_panel`.

#### 2. Funcționalități Cheie

- Meniul *Mesaje SPV (vedere împărțită)* din Facturare: kanban și listă pe mesajele SPV (`l10n_ro_edi.document`), cu aceleași filtre ca registrul; cardurile arată partener, total, număr, stare și direcția *Primit* / *Trimis*.
- Panoul din dreapta: partenerul, factura, totalul, starea, mesajul ANAF, fișierele mesajului și documentul facturii desenat în browser din XML (casete cu cealaltă parte, factura și firma noastră, apoi liniile și totalurile); CUI-ul se citește tot în browser.
- Sursa XML-ului: pentru o factură trimisă aflată în așteptare, XML-ul trimis; altfel, fișierul XML atașat facturii (factura de furnizor descărcată din SPV). La o factură trimisă deja validată modulul standard păstrează doar semnătura ANAF, iar panoul spune că XML-ul nu e disponibil.
- Butonul **Preia starea** din panou întreabă ANAF pentru o factură trimisă și încă în așteptare.
- Nu creează factura din mesaj, nu are **Acceptă** / **Respinge** și nu potrivește produsele după codul furnizorului; pentru acestea există `l10n_ro_message_spv_side_panel`. Cele două module nu se instalează împreună. Flux: [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_message_spv_online](../l10n_ro_message_spv_online/index.md)
- [deltatech_web_side_panel](../deltatech_web_side_panel/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_edi.document` (model standard, folosit în vizualizări noi; fără modele proprii).

**Vizualizări**

- `view_l10n_ro_edi_document_kanban`: cardurile mesajelor.
- `view_l10n_ro_edi_document_list_side_panel`: lista cu panou.
- `view_l10n_ro_edi_document_form_quick`: formularul din panou.
- `action_spv_messages_split`: acțiunea meniului vederii împărțite.

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_message_spv_side_panel](../l10n_ro_message_spv_side_panel/index.md): varianta cu Python; exclusă reciproc.
- [l10n_ro_message_spv_online](../l10n_ro_message_spv_online/index.md): registrul pe care se sprijină panoul.
