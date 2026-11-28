# eMAG Marketplace Statement Import (localizat la `deltatech_account_bank_statement_import_emag/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_emag`
- **Versiune:** `20.0.2.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_account_bank_statement_import_emag
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_emag`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Comercianții care vând pe eMAG Marketplace nu încasează direct de la fiecare client: eMAG colectează încasările (card online și ramburs), își reține comisioanele și virează periodic o singură sumă către comerciant. Modulul importă raportul *Account statement details* (XLSX), descărcat exact cum vine din panoul de comerciant eMAG, direct ca extras de cont bancar — fără nicio mapare manuală de coloane — și creează câte un extras pentru fiecare virare, cu liniile pregătite pentru reconciliere și clientul completat automat acolo unde referința permite. Modulul doar citește fișierul încărcat; nu se conectează la eMAG și nu trimite date în afara Odoo.

#### 2. Funcționalități Cheie

- **Import fișier original**: raportul se încarcă exact cum a fost descărcat; rândurile de sold de la începutul și sfârșitul fișierului sunt ignorate automat.
- **Detecție prin semnătură**: fișierul este recunoscut după setul de coloane din antet (Customer ID, Seller company, SAP document ID, Document code, Document amount, Clearing document), în orice ordine și pe orice foaie, deci poate fi importat din orice jurnal de tip bancă, alături de alte formate de extras.
- **Un extras per virare**: liniile sunt grupate după *Clearing document*; un fișier cu mai multe virări produce mai multe extrase, fiecare reconciliabil cu o singură linie bancară.
- **Semn corectat**: eMAG scrie sumele din perspectiva proprie; semnul se inversează la import, astfel încât încasările intră, iar virarea iese spre bancă.
- **Închidere pe zero, verificare obligatorie**: linia de virare (`ZP`) este negativul celorlalte; o sumă nenulă înseamnă fișier incomplet și importul este refuzat (verificarea nu poate fi dezactivată).
- **Identificare automată a partenerului**: pe încasări și restituiri, după numărul comenzii eMAG (`client_order_ref` sau `name` pe `sale.order`); pe documentele proprii eMAG, după numărul facturii de furnizor deja înregistrate. Potrivirile ambigue rămân neasignate.
- **Tipuri de linii**: încasări `KD` (card) și `KX` (ramburs), restituiri `ZC`, documente eMAG `DM` / `C3`, virarea `ZP`, reconciliată cu extrasul bancar real printr-un cont de viramente interne (581).
- **Diferență de curs per virare**: pentru extrasele importate într-un jurnal în altă monedă decât cea a companiei (eMAG HU în HUF, eMAG BG în EUR), fiecare linie este convertită la cursul zilei ei, iar o notă contabilă pe 665/765, la data virării, aduce contul de decontare la zero în RON; butoanele **Exchange difference** și **Recompute exchange difference** apar pe extras.
- **Protecție la duplicate**: identificator unic de import per *SAP document ID* (cu număr de apariție pentru liniile `ZP` cu același ID); reimportul aceluiași fișier este detectat.
- **Situații care cer atenția operatorului**: linie peste soldul rămas al facturii (surplusul rămâne avans client) și diferență egală cu valoarea unui voucher eMAG (reconciliere parțială).
- **Configurare**: jurnal de tip Bancă dedicat marketplace-ului, cu subcont propriu 5125 (sume în curs de decontare) și cont de suspend, **Bank Feeds = Import**. Fluxul pas cu pas este în fișa consultant.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_accountant`
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

*Notă:* `account_bank_statement_import_csv` este inclus special pentru ordinea corectă de MRO — override-ul modulului trebuie să ruleze înaintea interceptorului CSV/XLSX standard. Dependență externă Python: `openpyxl`.

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, completate din `USAGE.md`, `CONFIGURE.md` și `HISTORY.md`. Componentele de mai jos sunt menționate explicit în istoricul modulului (diferența de curs) sau reies din cod.

**Modele**

- `account.journal` (extins): adaugă formatul de import „eMAG Marketplace", recunoaște fișierul după setul de coloane obligatorii (`_read_emag_file`, prin helperul comun `_statement_sheet_matching_header()`), ocolește wizardul de mapare CSV/XLSX, grupează rândurile pe *Clearing document*, inversează semnul, verifică închiderea pe zero și construiește un extras per virare (`_parse_emag_file`); asociază partenerul după numărul comenzii sau al facturii de furnizor (`_emag_partner_from_row`).
- `account.bank.statement` (extins): câmpurile `emag_exchange_move_id` (nota de diferență de curs) și `emag_exchange_applicable` (calculat: jurnal în valută, cu linii eMAG); calculează diferența de curs realizată pe contul de decontare și postează nota pe 665/765 (`_emag_exchange_difference`, `_emag_post_exchange_difference`, `action_emag_recompute_exchange_difference`).

**Vizualizări**

- `view_bank_statement_form_emag_exchange`: extinde formularul extrasului bancar (`account_accountant.view_bank_statement_form_bank_rec_widget`) cu butonul **Recompute exchange difference** în antet și butonul inteligent **Exchange difference**, vizibile doar când se aplică.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): importă comenzile eMAG și scrie numărul comenzii în referință — baza identificării automate a clientului la reconciliere.
- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): același tipar de import prin semnătură de antet, pentru decontările EuPlatesc.ro.
- [deltatech_account_bank_statement_import_gls](../deltatech_account_bank_statement_import_gls/index.md): același tipar, pentru borderourile de ramburs GLS.
