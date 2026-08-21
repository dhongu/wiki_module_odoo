# GLS Borderou Bank Statements Import (localizat la `deltatech_account_bank_statement_import_gls/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_gls`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_gls
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_gls`
- **Ultima Ingestie:** `2026-08-20`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă borderourile de ramburs GLS (fișiere Excel) direct ca extrase de cont bancar,
fără nicio prelucrare manuală prealabilă a fișierului. Magazinele online care livrează cu plata
ramburs prin GLS primesc periodic aceste borderouri cu sumele încasate de curier și virate în
banca firmei; în loc să fie „curățate" manual (șters antetul și rândul de total) și mapate
coloană cu coloană în asistentul standard de import, fișierul original este încărcat ca atare
pe jurnalul de tip bancă dedicat curierului, generând automat o linie de extras per colet.

#### 2. Funcționalități Cheie

- **Import fișier original**: se încarcă borderoul exact cum vine de la GLS — antetul (client,
  cont bancar, dată transfer) și rândul de total sunt tratate automat.
- **Detecție prin semnătură**: fișierul este recunoscut după semnătura GLS din prima celulă, deci
  poate fi importat de pe orice jurnal de tip bancă, alături de alte formate de extras.
- **O linie per colet**: fiecare sumă ramburs devine o linie de extras cu numărul AWB, referința
  GLS și numele destinatarului.
- **Verificare de control**: rândul de total din fișier este verificat față de suma liniilor
  importate; o neconcordanță blochează importul.
- **Linie opțională de transfer bancar**: se poate adăuga automat (configurabil per jurnal) o
  linie negativă cu totalul virat, astfel încât extrasul jurnalului de curier se echilibrează la
  zero, iar transferul poate fi reconciliat cu extrasul băncii reale printr-un cont de viramente
  interne.
- **Protecție la duplicate**: fiecare colet are un id unic de import (per AWB); reimportul
  aceluiași fișier este detectat și refuzat.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_delivery_cod](../deltatech_delivery_cod/index.md)

*Note:*
- `account_bank_statement_import_csv` este inclus în dependențe special pentru a asigura ordinea
  corectă de MRO — override-ul modulului trebuie să ruleze înaintea interceptorului CSV/XLSX
  standard.
- Dependența nouă față de versiunea anterioară este `deltatech_delivery_cod`: puntea comună de
  decontare ramburs pentru curieri (protecție la duplicate, total de control, linia de
  echilibrare a extrasului), pe care modulul o folosește acum în loc să reimplementeze aceste
  verificări local (vezi Componente Cheie).

#### 4. Componente Cheie

Sumarul și funcționalitățile din secțiunile 1–2 provin din `readme/DESCRIPTION.md`; conform
fluxului de ingestie nu s-a mai analizat codul pentru acele secțiuni. Pentru această secțiune
(neacoperită explicit de DESCRIPTION.md) s-a analizat `models/account_journal.py`:

**Modele**

- `account.journal` (extins): adaugă formatul de import „GLS Borderou" în
  `_get_bank_statements_available_import_formats()`; recunoaște fișierul după semnătura
  `GLS General Logistics Systems` din prima celulă a XLSX-ului (`_read_gls_borderou`); pentru
  fișierele recunoscute forțează fluxul de import standard, ocolind wizardul de mapare CSV/XLSX
  (`_import_bank_statement`); parsează antetul (data transferării banilor) și rândurile de
  ramburs, apoi delegă construcția efectivă a extrasului (linii, total de control, linia de
  transfer, deduplicare) către puntea comună `_cod_prepare_statement()` din
  [deltatech_delivery_cod](../deltatech_delivery_cod/index.md) (`_parse_gls_borderou`,
  `_gls_carrier`).

**Migrare**

- `migrations/19.0.1.1.0/post-migration.py`: la trecerea de la versiunea `19.0.1.0.0`, mută
  valoarea câmpului de opțiune vechi `gls_add_transfer_line` (jurnal) pe câmpul comun
  `cod_add_transfer_line` din puntea `deltatech_delivery_cod`, apoi șterge coloana veche —
  păstrează setarea „adaugă linie de transfer bancar" a fiecărui jurnal la upgrade.

*Nu au fost introduse vizualizări sau acțiuni automate proprii în acest modul — bifa „GLS
Borderou: Add Bank Transfer Line" de pe formularul jurnalului este acum câmpul comun expus de
`deltatech_delivery_cod`.*

#### 5. Conexiuni

- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): același tipar (bazat pe aceeași punte `deltatech_delivery_cod`) pentru decontările Euplatesc.
- [l10n_ro_account_bank_statement_import_ing_csv](../l10n_ro_account_bank_statement_import_ing_csv/index.md): extrasul ING pe care sosește efectiv transferul GLS către bancă (complementar, opțional).
- [deltatech_stock_delivery](../deltatech_stock_delivery/index.md): AWB-ul (`carrier_tracking_ref`) de pe livrări, bază pentru identificarea automată a partenerului într-o fază viitoare (opțional).
