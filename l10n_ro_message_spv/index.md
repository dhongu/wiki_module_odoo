# Romania - Mesaje SPV (localizat la `l10n_ro_message_spv/index.md`)

- **Nume Tehnic:** `l10n_ro_message_spv`
- **Versiune:** `20.0.2.13.0`
- **Cale:** https://github.com/terrabit-ro/l10n-romania/tree/20.0/l10n_ro_message_spv
- **Cale Locală:** `odoo-addons/l10n-romania-oca/l10n_ro_message_spv`
- **Ultima Ingestie:** `2026-09-27`

#### 1. Sumar

Acest modul facilitează gestionarea mesajelor din Spațiul Privat Virtual (SPV) ANAF, asigurând descărcarea și procesarea automată a facturilor electronice (e-Factura): sincronizează periodic lista de mesaje SPV, descarcă arhivele ZIP semnate, extrage XML-ul semnat și creează automat facturi de furnizor din acesta, mapând furnizorul după codul fiscal (CIF) și oferind vizibilitate asupra stării fiecărui mesaj (Draft, Downloaded, Invoice, Eroare, Finalizat).

#### 2. Funcționalități Cheie

- Descărcare automată mesaje SPV: sincronizare periodică (via cron) a listei de mesaje din SPV pentru facturi primite, trimise sau erori.
- Procesare fișiere ZIP: descărcarea automată a arhivelor ZIP semnate de la ANAF; XML-ul semnat este extras la cerere, în memorie — nu se mai creează un atașament separat pentru el, doar arhiva ZIP semnată rămâne stocată ca dovadă legală.
- Creare automată facturi de furnizor: generează schițe de factură direct din fișierele XML descărcate, mapând automat furnizorul pe baza codului fiscal (CIF), cu deduplicare pe referință/tranzacție/index EDI pentru a evita facturile duplicate.
- Gestionare PDF-uri e-Factura:
  - Generare PDF ANAF: generează la cerere (via controller HTTP dedicat) vizualizarea PDF oficială a XML-ului, folosind serviciul ANAF de transformare (`FACT1`/`FCN`).
  - Extragere PDF încorporat: extrage la cerere PDF-ul atașat direct în fișierul XML (`AdditionalDocumentReference`), dacă există.
- Monitorizare stări: urmărirea stării fiecărui mesaj (Draft, Downloaded, Invoice, Error, Done) și a încercărilor de descărcare — ANAF limitează la 10 descărcări/zi pe mesaj, iar modulul marchează mesajul ca eroare după 3 încercări eșuate într-o zi, reluând automat a doua zi.
- Integrare cu fluxul de facturare: legarea automată a mesajelor de facturile existente pe baza ID-ului de tranzacție, a indexului EDI sau a referinței facturii; la ștergerea unei facturi, arhiva ZIP semnată e detașată (rămâne pe mesajul SPV ca probă legală), în timp ce documentele EDI sintetice de dedup sunt curățate doar pentru facturile de achiziție în ciornă/anulate.
- Căutare produs după codul furnizorului: la importul UBL/CIUS-RO, produsul este identificat automat după codul furnizorului (`SellersItemIdentification` sau `StandardItemIdentification`) folosind `product.supplierinfo`, cu prioritate maximă față de celelalte criterii de căutare.
- Salvare cod furnizor pe linia de factură: codul furnizorului (`l10n_ro_vendor_code`) este salvat pe linia de factură la import, chiar dacă produsul nu a fost găsit, pentru a permite asocierea ulterioară la validarea facturii; descrierea și prețul unitar venite din SPV se păstrează la corectarea produsului pe o linie importată.
- Sincronizarea datelor produselor: la validarea unei facturi de achiziție, dacă linia are cod de furnizor, se creează sau se actualizează automat înregistrarea `product.supplierinfo` corespunzătoare.
- Configurare număr de zile pentru descărcarea e-facturilor (`l10n_ro_download_einvoices_days`, implicit 60 de zile) și pentru reîmprospătarea mesajelor (`l10n_ro_refresh_message_days`, implicit 60 de zile) — accesibile din Setări Contabilitate, secțiunea e-Factura România.
- Meniu dedicat **Contabilitate → Configurare/Intrări contabile → SPV → Messages SPV**, cu acțiuni per mesaj: Refresh (resincronizare listă), Download, Get Invoice, Create Invoice, Show Invoice, plus butoane de descărcare ZIP/XML/PDF ANAF/PDF încorporat.

#### 3. Dependențe

- `l10n_ro_edi`
- `account_edi`
- [l10n_ro_config](../l10n_ro_config/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n.ro.message.spv`: modelul central al modulului — reprezintă un mesaj SPV (facturi primite/trimise, chitanțe, mesaje sau erori), cu starea de procesare (`draft`/`downloaded`/`invoice`/`error`/`done`), numărul de încercări de descărcare, arhiva ZIP semnată (`attachment_id`) și câmpuri calculate spre atașamentele derivate (XML, PDF ANAF, PDF încorporat) materializate pe factura legată.
- `res.company` (extins): adaugă `l10n_ro_download_einvoices_days` / `l10n_ro_refresh_message_days` și metodele de cron (`l10n_ro_download_message_spv`, `l10n_ro_download_zip_message_spv`) care interoghează SPV și creează/actualizează mesajele; include și logica de potrivire a partenerului după CIF (`_l10n_ro_get_partner_from_cif`).
- `account.move` / `account.move.line` (extinse): câmpul invers `l10n_ro_message_spv_ids`, câmpurile tehnice `l10n_ro_edi_transaction` / `l10n_ro_edi_download`, `l10n_ro_vendor_code` pe linie, plus logica de creare a `product.supplierinfo` la validare și de păstrare a descrierii/prețului liniilor importate din SPV.
- `product.product` (extins): plan de căutare a produsului la import UBL, cu prioritate pe codul de furnizor (`l10n_ro_vendor_code`).
- `l10n_ro_edi.document` (extins): cererile HTTP către ANAF pentru descărcarea arhivei ZIP semnate și pentru listarea paginată a mesajelor SPV.
- `account.edi.xml.ubl_ro` (extins): extrage codul de furnizor din XML-ul UBL/CIUS-RO la import și îl propagă pe linia de factură.
- Controller HTTP (`MessageSPVController`): rute `/l10n_ro/message_spv/<id>/xml|anaf_pdf|embedded_pdf` care servesc la cerere fișierele derivate din arhiva ZIP stocată, fără a le persista ca atașamente.

**Vizualizări**

- `view_l10n_ro_message_spv_tree` / `view_l10n_ro_message_spv_form` / `view_l10n_ro_message_spv_search`: listă, formular și căutare pentru mesajele SPV, cu butoane de acțiune (Refresh, Download, Get Invoice, Create Invoice, Show Invoice, descărcări ZIP/XML/PDF) și filtre/grupări pe stare, tip și partener.
- `action_l10n_ro_message_spv` + meniurile `menu_l10n_ro_spv` / `menu_l10n_ro_message_spv`: expun ecranul „Messages SPV” sub Contabilitate, vizibil doar grupului `l10n_ro_config.group_ro_menus`.
- `views/account_invoice.xml`: extinde formularul facturii cu coloana `l10n_ro_vendor_code` pe linii și cu o filă „ANAF SPV Messages” (read-only) ce listează mesajele SPV legate de factură.
- `wizard/res_config_settings_views.xml`: extinde Setările de e-Factura România cu cele două câmpuri de configurare a numărului de zile.

**Acțiuni Automate / Acțiuni Server**

- `ir_cron_res_company_download_message_spv`: rulează zilnic `res.company.l10n_ro_download_message_spv()` — sincronizează lista de mesaje SPV noi din ANAF.
- `ir_cron_download_zip_message_spv`: rulează zilnic `res.company.l10n_ro_download_zip_message_spv(limit=5)` — descarcă arhivele ZIP semnate pentru mesajele în stare `draft`, cu auto-retrigger dacă rămân mai multe de procesat decât limita.

#### 5. Conexiuni

- [l10n_ro_message_spv_purchase](../l10n_ro_message_spv_purchase/index.md): extinde mesajul SPV cu legătura la comanda de achiziție, pentru fluxul procure-to-pay.
- [l10n_ro_efactura_enhancement](../l10n_ro_efactura_enhancement/index.md): folosește mesajele SPV gestionate de acest modul la trimiterea și urmărirea facturilor de e-Factura.
- [l10n_ro_anaf_messages](../l10n_ro_anaf_messages/index.md): tratează separat mesajele SPV generale (notificări și recipise de declarații), complementar acestui modul care acoperă doar mesajele e-Factura.
- `l10n_ro_edi`: modulul standard Odoo de e-Invoicing România, pe care acest modul îl extinde (nu îl înlocuiește) cu interfața dedicată de mesaje SPV.
