# eMAG Marketplace Statement Import (localizat la `deltatech_account_bank_statement_import_emag/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_emag`
- **Versiune:** `19.0.2.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_emag
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_emag`
- **Ultima Ingestie:** `2026-09-19`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Comercianții care vând pe eMAG Marketplace nu încasează direct de la fiecare client: eMAG
colectează încasările (card online și ramburs), își reține comisioanele și virează periodic o
singură sumă către comerciant. Modulul importă raportul *Account statement details* (XLSX),
descărcat exact cum vine din panoul de comerciant eMAG, direct ca extras de cont bancar — fără
nicio mapare manuală de coloane — și creează câte un extras de cont pentru fiecare virare, cu
liniile pregătite pentru reconciliere și clientul completat automat acolo unde referința permite.

#### 2. Funcționalități Cheie

- **Import fișier original**: se încarcă raportul *Account statement details* exact cum vine de la
  eMAG — rândurile de sold (inițial/final) de la începutul și sfârșitul fișierului sunt ignorate
  automat.
- **Detecție prin semnătură**: fișierul este recunoscut după un **set** de coloane obligatorii din
  antet (Customer ID, Seller company, SAP document ID, Document code, Document amount, Clearing
  document), indiferent de ordinea lor și în oricare foaie a fișierului — nu mai contează un prefix
  fix de coloane în ordine, ca la versiunea anterioară. Detecția folosește helperul comun
  `_statement_sheet_matching_header()` din
  [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md),
  folosit și de modulul Euplatesc.
- **O linie de extras per virare**: liniile sunt grupate după *Clearing document*, deci un fișier
  care acoperă mai multe virări produce câte un extras pentru fiecare, reconciliabil cu o singură
  linie din extrasul bancar real.
- **Semn corectat**: eMAG scrie sumele din propria perspectivă (încasările comerciantului apar cu
  minus, documentele proprii ale eMAG cu plus); modulul inversează semnul, astfel încât încasările
  intră în jurnal și virarea iese spre bancă.
- **Verificare de închidere pe zero, obligatorie**: suma liniilor unei virări este verificată să fie
  zero — linia de virare (`ZP`) este prin construcție negativul tuturor celorlalte. O sumă
  diferită de zero înseamnă fișier incomplet, iar importul este refuzat. Din versiunea 2.0.0
  verificarea **nu mai poate fi dezactivată** (câmpul `emag_check_balance` de pe jurnal a fost
  eliminat) — un borderou tăiat se descarcă din nou, întreg, în loc să fie forțat parțial.
- **Identificare automată a partenerului**: pe încasări și restituiri, referința este numărul
  comenzii eMAG, căutat în comenzile de vânzare; pe documentele proprii ale eMAG (facturi de
  comision), referința este numărul facturii, căutat în facturile de furnizor deja înregistrate.
  Potrivirile ambigue lasă linia neasignată, pentru decizia operatorului.
- **Protecție la duplicate**: fiecare linie primește un identificator unic de import bazat pe *SAP
  document ID*; reimportul aceluiași fișier este detectat.
- **Interfață în română**: mesajele de eroare ale importului sunt traduse (`i18n/ro.po`).

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

*Notă:* `account_bank_statement_import_csv` este inclus special pentru ordinea corectă de MRO —
override-ul modulului trebuie să ruleze înaintea interceptorului CSV/XLSX standard.

#### 4. Componente Cheie

Sumarul și funcționalitățile din secțiunile 1–2 provin din `readme/DESCRIPTION.md` (cu corectarea
notată mai jos); pentru această secțiune s-a analizat suplimentar `models/account_journal.py`,
fiindcă DESCRIPTION.md nu detaliază implementarea tehnică.

**Modele**

- `account.journal` (extins): adaugă formatul de import „eMAG Marketplace" în
  `_get_bank_statements_available_import_formats()`; recunoaște fișierul prin
  `_read_emag_file()`, care deleagă la helperul comun `_statement_sheet_matching_header()` cu
  setul de coloane obligatorii `EMAG_REQUIRED_COLUMNS`; pentru fișierele recunoscute forțează
  fluxul standard de import, ocolind wizardul de mapare CSV/XLSX (`_import_bank_statement`);
  parsează antetul și grupează rândurile pe *Clearing document*, inversează semnul sumelor,
  verifică închiderea pe zero și construiește un extras per virare (`_parse_emag_file`); asociază
  partenerul fiecărei linii după numărul comenzii sau numărul facturii de furnizor
  (`_emag_partner_from_row`).

*Nu mai există câmpuri sau vizualizări proprii pe jurnal în această versiune: câmpul
`emag_check_balance` și view-ul care îl afișa (`views/account_journal_views.xml`) au fost
eliminate odată cu scoaterea opțiunii de dezactivare a verificării de sold.*

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): importă comenzile eMAG și
  scrie numărul comenzii în referință — baza identificării automate a clientului la reconciliere.
- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): același tipar de import prin semnătură de antet, pentru decontările Euplatesc, folosind același helper comun.
- [deltatech_account_bank_statement_import_gls](../deltatech_account_bank_statement_import_gls/index.md): același tipar, pentru borderourile de ramburs GLS.
