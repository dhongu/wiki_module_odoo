# eMAG Marketplace Statement Import (localizat la `deltatech_account_bank_statement_import_emag/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_emag`
- **Versiune:** `19.0.2.1.1`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_emag
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_emag`
- **Ultima Ingestie:** `2026-10-24`
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
  document ID*; reimportul aceluiași fișier este detectat. eMAG dă tuturor liniilor `ZP` ale unei
  virări același *SAP document ID* (numărul virării); liniile al căror ID se repetă în fișier primesc
  în identificator și suma, plus un număr de apariție, ca importul să nu cadă pe constrângerea de
  unicitate. Liniile cu ID unic își păstrează identificatorul, deci extrasele deja importate sunt în
  continuare recunoscute la reimport.
- **Borderouri în valută** (eMAG HU în HUF, eMAG BG în EUR): se importă într-un jurnal în moneda
  borderoului (câte un jurnal și un cont 5125.EMAG separat pentru fiecare monedă). Fiecare linie se
  convertește la cursul BNR din data ei, deci virarea se închide pe zero în valută, dar lasă un sold
  în lei pe contul de decontare. Imediat după import se postează automat o **notă de diferență de
  curs** per payout, datată cu data virării, în jurnalul de diferențe de curs al companiei:
  `665 = 5125.EMAG` pentru sold debitor, `5125.EMAG = 765` pentru sold creditor. Pe extras apar
  butonul **Diferență de curs** (deschide nota) și **Recalculează diferența de curs** (storno al
  notei și postarea alteia din liniile curente). Jurnalele în moneda companiei nu sunt afectate. Fără
  jurnalul de diferențe de curs și conturile 665/765 din setările contabilității, importul în
  valută este refuzat.
- **Moneda extrasului**: se citește și din coloana *Local company currency* când celula *Document
  currency* este goală; un fișier a cărui monedă diferă de cea a jurnalului este refuzat și în acest
  caz (înainte, un fișier EUR putea intra necontrolat într-un jurnal RON).
- **Vouchere eMAG**: linia `KD` / `KX` vine cu suma plătită efectiv de client, iar importul nu are
  reguli speciale pentru vouchere; diferă doar factura cu care se reconciliază. Voucherul vânzătorului
  este reducere comercială obișnuită. Voucherul suportat de eMAG are două variante în conectorul
  eMAG: **pe factură** (linie negativă pe *Produs voucher*, fără TVA) sau **nu pe factură**
  (factura la valoarea întreagă, partea eMAG ca plată pe *Jurnal vouchere*); în ambele cazuri
  creanța la eMAG stă pe 461.EMAG. Cazurile speciale (backend fără configurare de voucher, factură
  postată înaintea voucherului, livrare în locker) sunt în fișa consultant.
- **Codul `KM` (Decont voucher)**: decontul de vouchere al eMAG vine în aceeași virare cu restul
  borderoului, cu o linie `ZP` de aceeași valoare; intră cu sumă pozitivă, de regulă fără partener,
  și se reconciliază cu creanța de voucher deschisă pe 461.EMAG (`Dr 5125.EMAG = Cr 461.EMAG`), nu cu
  factura clientului. Verificarea de închidere pe zero include `KM`: `KD`+`KX`+`KM`−`ZC`−`DM`−`C3` = `ZP`.
- **Interfață în română**: mesajele de eroare ale importului sunt traduse (`i18n/ro.po`).
- **Tratament pe Document code** (detaliat în fișa consultant): `KD` (încasare card) și `KX`
  (ramburs) intră cu sumă pozitivă, cu numărul comenzii eMAG, și se reconciliază cu factura
  clientului; `KM` (decont de vouchere) intră pozitiv și se reconciliază cu creanța de voucher
  de pe 461, nu cu factura; `ZC` (restituire) intră negativ și, dacă anulează o încasare a aceleiași comenzi, se
  reconciliază cu ea, fără factură; `DM` (facturi eMAG) și `C3` (notificări) intră negativ și se
  reconciliază cu factura de furnizor deja înregistrată, parțial când eMAG reține doar o parte;
  `ZP` este suma efectiv virată, reconciliată cu extrasul bancar real prin contul de viramente
  interne (`581000`).
- **Jurnal dedicat eMAG**: jurnal de tip *Bancă*, cu **Bank Feeds = Import**, cont implicit
  propriu din 5125 (*Sume în curs de decontare*, `5125.EMAG`, tip *Bancă și numerar*, nu cont
  bancar 512 — banii sunt la eMAG până la virare) și cont tranzitoriu preferabil dedicat
  (`473.EMAG`) de tip *Active circulante* — domeniul jurnalului nu acceptă alt tip, deci 473000
  standard (*Datorii curente*) nu poate fi ales ca atare. Prezența formatului „eMAG Marketplace" în formatele de import acceptate arată că
  modulul e activ.
- **Fișa consultant**: tabel de definire a jurnalului câmp cu câmp, note contabile pe tip de
  document, secțiune despre comanda anulată după încasare (`KD` + `ZC`; cazul voucherului e marcat
  ca neverificat), despre transport (nu are linie proprie în borderou; este inclus în totalul
  `KD`/`KX` sau în facturile `DM`/`C3`) și despre cazul în care încasarea este deja înregistrată pe
  alt jurnal (vezi mai jos). Partenerul de decontare este Dante International.
- **Încasare deja înregistrată pe alt jurnal**: dacă facturile din borderou sunt deja plătite pe
  jurnalul curierului (sau al altui canal), liniile din extras nu le pot deconta fără a desface
  plata existentă, iar încasarea ar fi numărată de două ori. Fișa explică alegerea unui singur flux
  pentru încasare; verificarea se face înainte de import, iar eroarea de dublare este descrisă în
  tabelul de erori. Pe date de test, importul în sine funcționează, restul mici de factură se
  reconciliază automat, iar perechile `KD`/`ZC` ale comenzilor anulate se reconciliază între ele.
- **Situații cu atenția operatorului**: o linie mai mare decât restul facturii lasă excedentul ca
  avans de client; o diferență egală cu un voucher eMAG se reconciliază parțial, iar restul rămâne
  creanță deschisă până la decontarea de către eMAG.
- **Import din ecranul corect**: importul pornit din altă parte (*Import records* pe lista de
  tranzacții) ocolește modulul și ajunge în wizardul de mapare; se folosește *Import* de pe jurnal.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_accountant` (formularul extrasului, butoanele de diferență de curs)
- `account_bank_statement_import_csv`
- [deltatech_account_bank_statement_import](../deltatech_account_bank_statement_import/index.md)

*Notă:* `account_bank_statement_import_csv` este inclus special pentru ordinea corectă de MRO —
override-ul modulului trebuie să ruleze înaintea interceptorului CSV/XLSX standard.

#### 4. Componente Cheie

Sumarul și funcționalitățile din secțiunile 1–2 provin din `readme/DESCRIPTION.md`, completate din
`readme/USAGE.md`, `readme/CONFIGURE.md`, `readme/HISTORY.md` și fișa consultant; pentru această secțiune s-au analizat suplimentar
`models/account_journal.py`, `models/account_bank_statement.py` și `views/account_bank_statement_views.xml`,
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

- `account.bank.statement` (extins): `emag_exchange_move_id` (nota de diferență de curs a payout-ului),
  `emag_exchange_applicable` (calculat: extras eMAG importat într-un jurnal în altă monedă decât a
  companiei); `_emag_exchange_difference()` calculează soldul în lei al liniilor de pe contul
  jurnalului (doar dacă liniile se închid în valută), `_emag_post_exchange_difference()` postează nota
  pe 665/765 în jurnalul de diferențe de curs, `action_emag_recompute_exchange_difference()`
  stornează nota și o postează din nou, `action_emag_open_exchange_move()` deschide nota.

*Jurnalul nu mai are câmpuri sau vizualizări proprii: `emag_check_balance` și view-ul său au fost
eliminate odată cu scoaterea opțiunii de dezactivare a verificării de sold.*

**Vizualizări**

- `view_bank_statement_form_emag_exchange`: moștenește formularul extrasului din `account_accountant`;
  adaugă butonul **Recalculează diferența de curs** (cu confirmare, vizibil doar pe extrasele în
  valută) și butonul statistic **Diferență de curs** către nota postată.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau acțiuni server; nota de diferență de curs se postează din fluxul de import.

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): importă comenzile eMAG și
  scrie numărul comenzii în referință — baza identificării automate a clientului la reconciliere.
- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): același tipar de import prin semnătură de antet, pentru decontările Euplatesc, folosind același helper comun.
- [deltatech_account_bank_statement_import_gls](../deltatech_account_bank_statement_import_gls/index.md): același tipar, pentru borderourile de ramburs GLS.
