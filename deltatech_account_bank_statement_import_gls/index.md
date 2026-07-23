# GLS Borderou Bank Statements Import (localizat la `deltatech_account_bank_statement_import_gls/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_gls`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-ro/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_gls
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_gls`
- **Ultima Ingestie:** `2026-07-23`
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

*Notă:* `account_bank_statement_import_csv` este inclus în dependențe special pentru a asigura
ordinea corectă de MRO — override-ul modulului trebuie să ruleze înaintea interceptorului
CSV/XLSX standard.

#### 4. Componente Cheie

Sumarul și funcționalitățile de mai sus provin din `readme/DESCRIPTION.md`; conform fluxului de
ingestie, analiza suplimentară a codului pentru modele/vizualizări/acțiuni a fost omisă
(DESCRIPTION.md nu o cere explicit). Din manifest se observă că modulul adaugă o opțiune pe
formularul jurnalului de tip bancă (`views/account_journal_views.xml`, model extins în
`models/account_journal.py`) — „GLS Borderou: Add Bank Transfer Line" — pentru activarea liniei
de transfer bancar automate.

#### 5. Conexiuni

- `deltatech_account_bank_statement_import_euplatesc`: același tipar de import pentru
  decontările Euplatesc (frate, opțional).
- `l10n_ro_account_bank_statement_import_ing_csv`: extrasul ING pe care sosește transferul GLS
  către bancă (complementar, opțional).
- `stock_delivery`: AWB-ul (`carrier_tracking_ref`) de pe livrări, bază pentru identificarea
  automată a partenerului într-o fază viitoare (opțional).
