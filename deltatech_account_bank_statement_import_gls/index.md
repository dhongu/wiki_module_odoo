# GLS COD Statement Import (localizat la `deltatech_account_bank_statement_import_gls/index.md`)

- **Nume Tehnic:** `deltatech_account_bank_statement_import_gls`
- **Versiune:** `20.0.1.1.4`
- **Cale:** https://github.com/terrabit-solutions/bitshop_ent/tree/20.0/deltatech_account_bank_statement_import_gls
- **Cale Locală:** `odoo-addons/bitshop_ent/deltatech_account_bank_statement_import_gls`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul importă borderoul de ramburs GLS (fișier XLSX) direct ca extras de cont bancar, fără prelucrare manuală: o linie per colet plătit la livrare, legată de clientul expedierii, plus o linie pentru suma pe care GLS o virează în bancă. Magazinele online care livrează cu plata ramburs prin GLS încarcă fișierul original pe jurnalul curierului, fără să șteargă antetul sau rândul de total. Modulul doar citește fișierul încărcat; nu se conectează la GLS.

#### 2. Funcționalități Cheie

- **Fișierul așa cum vine**: borderoul se încarcă exact cum îl trimite GLS; blocul de antet (client, cont bancar, data transferului) și rândul de total sunt tratate automat.
- **Recunoaștere prin semnătură**: fișierul este identificat după semnătura GLS din prima celulă, deci poate fi importat din orice jurnal bancar, fără wizardul de mapare a coloanelor.
- **O linie per colet**: fiecare sumă ramburs devine o linie cu numărul AWB, referința GLS și numele destinatarului (*COD AWB ... - destinatar*).
- **Clientul găsit după AWB**: linia este legată de clientul livrării care poartă același AWB în compania curentă, niciodată după nume; fără livrare sau cu mai multe potriviri, linia rămâne pentru operator.
- **Total verificat**: rândul de total trebuie să egaleze suma coletelor; un fișier care acoperă mai multe transferuri este refuzat, astfel încât fiecare extras corespunde unei singure mișcări bancare. Importul mai este refuzat și când toate coletele au fost deja importate.
- **Linie de transfer și duplicate**: o linie negativă opțională cu suma virată echilibrează extrasul la zero; fiecare colet se importă o singură dată (id unic per AWB).
- **Configurare**: jurnal de tip Bancă (de ex. *GLS COD*) cu cont propriu 5125, **Bank Feeds = Import**; în tabul **Advanced Settings**, secțiunea **Courier COD Settlement**, se alege **Carrier**-ul GLS și se păstrează bifat **Add Bank Transfer Line**. Livrările trebuie să aibă AWB-ul în **Tracking Reference**. Transferul se reconciliază cu extrasul bancar real printr-un cont de viramente interne (581). Pașii detaliați sunt în fișa consultant.

#### 3. Dependențe

- `account_bank_statement_import`
- `account_bank_statement_import_csv`
- [deltatech_delivery_cod](../deltatech_delivery_cod/index.md)

*Note:*
- `account_bank_statement_import_csv` este inclus special pentru ordinea corectă de MRO — override-ul modulului trebuie să ruleze înaintea interceptorului CSV/XLSX standard.
- `deltatech_delivery_cod` este puntea comună de decontare ramburs pentru curieri (protecție la duplicate, total de control, linia de echilibrare), aceeași logică folosită și de ceilalți conectori de curier Terrabit. Dependență externă Python: `openpyxl`.

#### 4. Componente Cheie

Sumarul și funcționalitățile provin din `readme/DESCRIPTION.md`, completat din `USAGE.md` și `CONFIGURE.md`. Componentele de mai jos reies din cod.

**Modele**

- `account.journal` (extins): adaugă formatul de import „GLS Borderou" (`_get_bank_statements_available_import_formats`); recunoaște fișierul după semnătura GLS din prima celulă (`_read_gls_borderou`); forțează fluxul standard de import, ocolind wizardul CSV/XLSX (`_import_bank_statement`); parsează antetul și rândurile de ramburs (`_parse_gls_borderou`) și delegă construcția extrasului (linii, total de control, linia de transfer, deduplicare) către `_cod_prepare_statement()` din [deltatech_delivery_cod](../deltatech_delivery_cod/index.md); curierul este dat de opțiunea de jurnal (`_gls_carrier`).

**Vizualizări**

- Modulul nu definește vizualizări proprii; opțiunile **Carrier** și **Add Bank Transfer Line** sunt câmpurile comune expuse de `deltatech_delivery_cod` pe formularul jurnalului.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` în acest modul.

#### 5. Conexiuni

- [deltatech_account_bank_statement_import_euplatesc](../deltatech_account_bank_statement_import_euplatesc/index.md): același tipar de import, pentru decontările EuPlatesc.ro.
- [deltatech_account_bank_statement_import_emag](../deltatech_account_bank_statement_import_emag/index.md): același tipar, pentru decontările eMAG Marketplace.
- [deltatech_stock_delivery](../deltatech_stock_delivery/index.md): AWB-ul (`carrier_tracking_ref`) de pe livrări, folosit la identificarea clientului.
- [l10n_ro_account_bank_statement_import_ing_csv](../l10n_ro_account_bank_statement_import_ing_csv/index.md): extrasul ING pe care sosește efectiv transferul GLS (complementar, opțional).
