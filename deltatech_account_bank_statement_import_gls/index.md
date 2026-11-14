# GLS COD Statement Import (localizat la `deltatech_account_bank_statement_import_gls/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_gls`
- **Versiune:** `19.0.1.1.5`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/19.0/deltatech_account_bank_statement_import_gls
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_gls`
- **Ultima Ingestie:** `2026-11-14`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă borderoul de ramburs GLS (fișier XLSX) direct ca extras de cont bancar, fără nicio prelucrare prealabilă a fișierului: o linie pentru fiecare colet plătit la livrare, legată de clientul expedierii, plus o linie pentru suma virată de GLS în banca firmei. Magazinele online care livrează cu ramburs prin GLS încarcă fișierul exact cum îl primesc, pe jurnalul de tip bancă dedicat curierului.

#### 2. Funcționalități Cheie

- **Fișierul așa cum vine**: antetul (client, cont bancar, data transferului) și rândul de total sunt tratate automat.
- **Recunoaștere automată**: fișierul este identificat după semnătura GLS din prima celulă, deci se importă de pe orice jurnal bancar, alături de alte formate de extras, fără wizardul de mapare a coloanelor.
- **O linie per colet**: fiecare sumă ramburs devine o linie de extras cu numărul AWB, referința GLS și numele destinatarului.
- **Clientul găsit după AWB**: linia este legată de clientul livrării care are același AWB în compania curentă, niciodată după nume; când nu se găsește nicio livrare sau se găsesc mai multe, linia rămâne pentru operator.
- **Total verificat**: rândul de total trebuie să egaleze suma coletelor, iar un fișier care acoperă mai mult de un transfer este refuzat, astfel încât fiecare extras corespunde unei singure mișcări bancare.
- **Linie de transfer și duplicate**: o linie negativă opțională cu suma virată echilibrează extrasul la zero; fiecare colet se importă o singură dată, deci reimportul aceluiași fișier este detectat. Importul este refuzat, cu mesaj, și când toate coletele din fișier au fost deja importate.
- **Date trimise în afara Odoo:** niciuna; modulul doar citește fișierul încărcat și nu se conectează la GLS.
- **Flux de utilizare**: din tabloul de bord Contabilitate se deschide jurnalul GLS și se folosește *Upload*; se creează un extras „GLS Borderou" cu data transferului; liniile coletelor se reconciliază cu facturile clienților, iar linia de transfer cu plata GLS din extrasul băncii reale, printr-un cont de viramente interne (581 în planul de conturi românesc).
- **Configurare**: în *Contabilitate → Configurare → Jurnale* se creează un jurnal de tip **Bancă** pentru ramburs GLS, cu propriul cont de sume în curs de decontare (subcont 5125); *Bank Feeds* se setează pe *Import*; în tab-ul **Advanced Settings**, secțiunea **Courier COD Settlement**, se alege **Carrier**-ul GLS și se păstrează bifat **Add Bank Transfer Line**. Pentru găsirea clienților, livrările trebuie să aibă AWB-ul GLS în **Tracking Reference** (ca în conectorul GLS).

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_delivery_cod](../deltatech_delivery_cod/index.md)

*Note:*
- `account_bank_statement_import_csv` este inclus în dependențe special pentru ordinea corectă de MRO — override-ul modulului trebuie să ruleze înaintea interceptorului CSV/XLSX standard.
- `deltatech_delivery_cod` este puntea comună de decontare ramburs pentru curieri (protecție la duplicate, total de control, linia de echilibrare a extrasului), folosită în locul unor verificări locale.
- Dependență externă Python: `openpyxl`.

#### 4. Componente Cheie

**Modele**

- `account.journal` (extins): adaugă formatul de import „GLS Borderou" în `_get_bank_statements_available_import_formats()`; recunoaște fișierul după semnătura `GLS General Logistics Systems` din prima celulă a XLSX-ului (`_read_gls_borderou`); pentru fișierele recunoscute forțează fluxul de import standard, ocolind wizardul de mapare CSV/XLSX (`_import_bank_statement`); parsează antetul (data transferului) și rândurile de ramburs (`_parse_gls_borderou`), apoi delegă construcția extrasului (linii, total de control, linia de transfer, deduplicare, clientul după AWB) către `_cod_prepare_statement()` din [deltatech_delivery_cod](../deltatech_delivery_cod/index.md); `_gls_carrier` alege carrier-ul GLS.

**Migrare**

- `migrations/19.0.1.1.0/post-migration.py`: mută valoarea opțiunii vechi `gls_add_transfer_line` (jurnal) pe câmpul comun `cod_add_transfer_line` din `deltatech_delivery_cod`, apoi șterge coloana veche, păstrând setarea fiecărui jurnal la upgrade.

**Vizualizări**

Modulul nu are vizualizări proprii; opțiunea „Add Bank Transfer Line" de pe formularul jurnalului este câmpul comun expus de `deltatech_delivery_cod`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): același tipar (aceeași punte `deltatech_delivery_cod`) pentru decontările Euplatesc.
- [l10n_ro_account_bank_statement_import_ing_csv](../l10n_ro_account_bank_statement_import_ing_csv/index.md): extrasul ING pe care sosește efectiv transferul GLS către bancă (complementar, opțional).
- [deltatech_stock_delivery](../deltatech_stock_delivery/index.md): AWB-ul (`carrier_tracking_ref`) de pe livrări, folosit pentru identificarea clientului.
