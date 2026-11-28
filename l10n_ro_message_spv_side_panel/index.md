# Panou lateral mesaje SPV

- **Nume Tehnic:** `l10n_ro_message_spv_side_panel`
- **Versiune:** `20.0.1.3.0`
- **Cale:** https://github.com/dhongu/l10n-romania/tree/20.0/l10n_ro_message_spv_side_panel
- **Cale Locală:** `odoo-addons/l10n-romania/l10n_ro_message_spv_side_panel`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Vedere împărțită pentru mesajele SPV: facturile primite prin SPV apar în stânga, ca carduri, iar în dreapta, într-un panou, detaliile mesajului selectat, fără a părăsi lista. Este o punte între `l10n_ro_message_spv` și `deltatech_web_side_panel`, instalată la cerere.

#### 2. Funcționalități Cheie

- Meniul *Mesaje SPV* deschide un kanban de carduri (furnizor, sumă, număr, dată, stare, zile până la scadență; un mesaj a cărui arhivă nu e descărcată arată id-ul, tipul și data) și lista obișnuită; un clic selectează mesajul și îl arată în panou. Dezinstalarea modulului readuce meniul la forma inițială.
- Panoul: furnizorul, CUI-ul citit din XML, datele, sumele, starea de verificare și butoanele *Creează factura*, *Acceptă*, *Respinge*, *XML*, *PDF* și *ZIP*; *Reîmprospătează* reîncarcă mesajul după o acțiune.
- Documentul: factura așa cum e în XML, ca o foaie de hârtie, cu trei casete (cealaltă parte, datele facturii, firma noastră), liniile (cod, descriere, UM, cantitate, preț, TVA, valoare) și totalurile. Panoul și formularul complet arată același document, fără taburi. Nimic nu se stochează: XML-ul se citește din ZIP la deschiderea mesajului.
- Pe ecrane mai înguste de 1200 px panoul e oprit, iar un clic deschide formularul mesajului. Flux detaliat: [Fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_message_spv](../l10n_ro_message_spv/index.md)
- [deltatech_web_side_panel](../deltatech_web_side_panel/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.message.spv` (extins): date pentru panou și document redat din XML.

**Vizualizări**

- `view_l10n_ro_message_spv_kanban`: cardurile din stânga.
- `view_l10n_ro_message_spv_list_side_panel`: lista cu panou.
- `view_l10n_ro_message_spv_form_quick`: formularul afișat în panou.
- `view_l10n_ro_message_spv_form_side_panel`: formularul complet cu documentul.
- `action_l10n_ro_message_spv_split`: acțiunea vederii împărțite, care înlocuiește meniul standard.

**Acțiuni Automate / Acțiuni Server**

- Niciuna (`uninstall_hook` restaurează meniul standard).

#### 5. Conexiuni

- [l10n_ro_message_spv_side_panel_online](../l10n_ro_message_spv_side_panel_online/index.md): varianta fără Python pentru Odoo Online; exclusă reciproc.
- [l10n_ro_message_spv_online](../l10n_ro_message_spv_online/index.md): varianta Online a registrului.
