# Romania - Import extrase bancare ING (CSV) (localizat la `l10n_ro_account_bank_statement_import_ing_csv/index.md`)

- **Nume Tehnic:** `l10n_ro_account_bank_statement_import_ing_csv`
- **Versiune:** `19.0.1.1.4`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_account_bank_statement_import_ing_csv
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_account_bank_statement_import_ing_csv`
- **Ultima Ingestie:** `2026-11-21`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă fișierele „Istoric conturi” (CSV) exportate din ING Business direct ca extrase de cont, fără nicio prelucrare manuală a fișierului: se încarcă exact cum a fost exportat, fără asistentul de mapare a coloanelor.

#### 2. Funcționalități Cheie

- **Import fișier original:** CSV-ul se încarcă exact cum e exportat din ING Business; antetul, separatorul `;`, sumele în format românesc (`1.234,56`) și codificarea sunt gestionate automat.
- **Detecție după semnătură:** fișierul e recunoscut după antetul ING (`numar cont;data procesarii;...`), deci poate fi importat de pe orice jurnal de tip bancă, alături de alte formate de extras; un CSV fără antetul ING urmează fluxul obișnuit, cu asistentul de mapare.
- **Validare cont:** IBAN-ul din fișier se verifică față de contul bancar al jurnalului (mecanismul standard Odoo); dacă jurnalul nu are încă un cont bancar, IBAN-ul din fișier se setează automat la primul import. Un jurnal per IBAN.
- **Solduri:** soldul inițial și cel final ale extrasului se calculează din coloana „sold intermediar”; extrasul creat se numește **ING <data de la> - <data până la>**, cu tranzacțiile în ordine cronologică.
- **Date pentru reconciliere:** numele contrapartidei, IBAN-ul și CUI-ul contrapartidei se preiau pe linia de extras și apar în widgetul de reconciliere bancară. Partenerul se identifică automat după CUI (cu sau fără prefixul `RO`); dacă mai mulți parteneri au același CUI, linia rămâne nealocată, la decizia operatorului.
- **Protecție la duplicate:** fiecare tranzacție se importă o singură dată (id unic din referința internă/instant ING); reimportul aceluiași fișier este refuzat („You already have imported that file.”), deci se exportă doar perioada nouă.
- **Cum se încarcă:** *Contabilitate → Tablou de bord*, pe cardul jurnalului ING, meniul **⋮** → **Extrase** → **Încărcare**; alternativ, linkul **Importă fișier** din cardul jurnalului sau tragerea fișierului peste lista de tranzacții.
- **Configurare:** jurnal de bancă în RON, cu cont tranzitoriu setat (altfel Odoo nu poate crea liniile de extras); utilizatorul care importă are nevoie de drepturi de contabilitate; modulul necesită mecanismul standard de import al extraselor din Odoo Enterprise.
- **Limitări:** un export fără tranzacții și un fișier cu alt IBAN decât al jurnalului sunt refuzate; modulul nu postează note contabile (acestea rezultă din reconcilierea standard Odoo); un sold final diferit de cel din ING Business indică de regulă un export parțial sau tranzacții în altă monedă. Fluxul pas cu pas este în fișa consultant.

#### 3. Dependențe

- `l10n_ro`
- `account_bank_statement_import`
- `account_bank_statement_import_csv`

> `account_bank_statement_import_csv` este necesar pentru ordinea MRO: suprascrierea acestui modul trebuie să ruleze înaintea interceptorului CSV/XLSX.

#### 4. Componente Cheie

Documentația este derivată din `readme/DESCRIPTION.md` și `readme/USAGE.md`, care descriu funcționalitatea la nivel de utilizator și nu solicită analiza componentelor tehnice; secțiunea nu a fost populată prin analiza codului.

#### 5. Conexiuni

- [l10n_ro_account_bank_statement_import_xlsx](../l10n_ro_account_bank_statement_import_xlsx/index.md): modul soră din aceeași suită, pentru importul extraselor bancare din fișiere XLSX.
