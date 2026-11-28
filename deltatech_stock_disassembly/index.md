# Free Disassembly (localizat la `deltatech_stock_disassembly/index.md`)

- **Nume Tehnic:** `deltatech_stock_disassembly`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_stock_disassembly
- **Cale Locală:** `odoo-addons/deltatech/deltatech_stock_disassembly`
- **Ultima Ingestie:** `2026-11-28`

#### 1. Sumar

Un **proces-verbal de dezmembrare** scoate un produs din stoc și introduce produsele obținute din el, fără listă de materiale și fără ordin de producție. Costul produsului dezmembrat se repartizează pe produsele rezultate, iar modulul înregistrează o singură notă contabilă pentru tot documentul.

#### 2. Funcționalități Cheie

- **Document numerotat** (`PVD/<an>/<număr>`), cu stări ciornă → finalizat, comisie, motiv și raport PDF de tipărit pentru semnături.
- **Produsul dezmembrat** se ia dintr-o locație internă, cu lot sau serie, la **costul real** (mediu, straturi FIFO sau cost pe lot). Se poate dezmembra doar stocul propriu al companiei și niciodată mai mult decât este disponibil.
- **Produse rezultate** introduse liber: cantitate, unitate, locație de destinație și lot (existent sau denumire de lot nou, creat la validare).
- **Repartizarea costului**: după cantitate, după preț de referință × cantitate, după procente sau după valori fixe. Liniile cu valoare fixă (de exemplu deșeuri recuperabile la valoarea realizabilă netă) se scad primele; diferența de rotunjire merge pe ultima linie.
- **Linii de pierdere** (pierdere tehnologică, deșeuri nerecuperabile) către o locație de pierderi: în limita normei tehnologice nu primesc valoare; peste normă (**Above Norm**) primesc valoare și se înregistrează pe cheltuială, cu atenționare în chatter și pe PDF despre cheltuiala nedeductibilă și ajustarea TVA.
- **O singură notă contabilă pe document**, în jurnalul de stoc, la data documentului; mișcările de stoc sunt legate de ea.
- **Plan de conturi românesc**: corespondențe permise între conturi sintetice (371 → 371, 302 → 302, 341/345/347 → 30x/371 etc.); reclasificările bunuri ↔ materiale (371 → 30x, 301 ↔ 302 ↔ 303) doar dacă politica contabilă le permite în setări; orice altă pereche de conturi este refuzată înainte de mișcarea stocului.
- Produsul dezmembrat și cele rezultate trebuie să aibă aceeași evaluare (automată sau manuală). Funcționează cu și fără localizarea de contabilitate de stoc.
- Meniu: *Inventar → Operațiuni → Ajustări → Disassembly*. Configurare: *Inventar → Configurare → Setări → Valuation*, opțiunea **Disassembly: reclassify goods and materials** (doar companii românești); categoriile de produse trebuie să aibă cont de evaluare a stocului și de cheltuieli, iar compania un jurnal de stoc.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.disassembly`: procesul-verbal de dezmembrare (cu `mail.thread` și activități); acțiuni de validare, anulare, revenire la ciornă, mișcări de stoc și notă contabilă.
- `stock.disassembly.line`: liniile rezultate sau de pierdere (inclusiv `lot_name` pentru lot nou).
- `stock.move`, `res.company`, `res.config.settings`: extinse pentru legătura cu documentul și opțiunea de reclasificare.

**Vizualizări**

- `view_stock_disassembly_form` / `_list` / `_search`: interfața documentului.
- `res_config_settings_view_form_stock_disassembly`: opțiunea de reclasificare în setările de stoc.
- `report/report_stock_disassembly.xml`: raportul PDF cu semnături.

**Acțiuni Automate / Acțiuni Server**

- `seq_stock_disassembly`: secvența documentelor (`ir.sequence`).
- Nu există cron-uri sau acțiuni server.

#### 5. Conexiuni

- [deltatech_stock_disassembly_mrp](../deltatech_stock_disassembly_mrp/index.md): punte cu Producția, completează liniile dintr-o listă de materiale.
