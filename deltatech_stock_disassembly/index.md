# Dezmembrare liberă (Free Disassembly)

- **Nume Tehnic:** `deltatech_stock_disassembly`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_stock_disassembly
- **Cale Locală:** odoo-addons/deltatech/deltatech_stock_disassembly
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Procesul-verbal de dezmembrare scoate din stoc un produs și introduce în stoc produsele obținute din el, fără listă de materiale (BoM) și fără ordin de producție. Costul real al produsului dezmembrat se repartizează pe produsele rezultate, iar modulul postează o singură notă contabilă pentru întregul proces-verbal. Este util în special pentru recuperări de componente, deșeuri recuperabile și pierderi tehnologice.

#### 2. Funcționalități Cheie

- **Document numerotat** (`PVD/<an>/<număr>`), cu stări ciornă → finalizat (și anulare / revenire la ciornă), cu comisie, motiv și raport PDF imprimabil, cu semnături. Se află la **Inventar → Operațiuni → Ajustări → Dezmembrare**.
- **Produsul dezmembrat** se ia dintr-o locație internă, cu lot sau număr de serie, la **costul real** (cost mediu, straturi FIFO sau cost pe lot, conform valorizării stocului). Se poate dezmembra doar stocul propriu al companiei și niciodată mai mult decât există disponibil; costul estimat se afișează în formular.
- **Produsele rezultate** se introduc liber, fiecare cu cantitate, unitate de măsură, locație de destinație și lot (existent sau denumire de lot nou, creat la validare).
- **Alocarea costului** după cantitate, preț de referință × cantitate, procente sau valori fixe. Liniile cu valoare fixă (de exemplu deșeu recuperabil la valoarea realizabilă netă) se scad primele; diferențele de rotunjire merg pe ultima linie. Mișcările rezultate intră în stoc exact la valoarea alocată (se actualizează costul mediu, se creează straturi FIFO / pe lot).
- **Linii de pierdere** (pierdere tehnologică, deșeu nerecuperabil) trimise într-o locație de pierderi: în limita normei tehnologice nu primesc valoare (costul rămâne în produsele rezultate); peste normă (bifa **Peste normă**) trebuie să aibă valoare (fixă sau procent) și se înregistrează pe cheltuială, cu o notă în chatter și pe PDF despre cheltuiala nedeductibilă și ajustarea TVA deductibil.
- **O singură notă contabilă per proces-verbal**, în jurnalul de stoc, la data documentului, în loc de câte una pe mișcare de stoc. Liniile conțin produsul și cantitatea, iar toate mișcările de stoc ale documentului sunt legate de notă (butoane pentru mișcări și nota contabilă).
- **Plan de conturi românesc** (țară fiscală România), pe cont sintetic:
  - stoc → stoc pe același cont sintetic (371 → 371, 302 → 302) și acolo unde planul prevede corespondența: produse proprii folosite ca materiale sau vândute ca mărfuri (341 → 301/302, 345 → 301/302/303/371, 347 → 301/302/371) și materiale vândute ca mărfuri (30x → 371); liniile pe același cont nu se compensează, pentru urma de audit;
  - produsele rezultate pe 34x (ex. produse reziduale, 346) intră prin 711; produsul dezmembrat iese prin contul de cheltuieli (60x/607, sau 711 pentru produse proprii);
  - mărfuri transformate în materiale (371 → 30x) și materiale de alt tip (301 ↔ 302 ↔ 303) doar dacă firma permite din setări, conform politicii contabile;
  - orice altă pereche de conturi (ex. produse reziduale 346 în materiale sau mărfuri) este refuzată înainte de mutarea stocului.
- Produsul dezmembrat și cele rezultate trebuie să aibă aceeași valorizare (automată sau manuală), pentru ca nota contabilă să fie completă.
- **Configurare:** la **Inventar → Configurare → Setări → Valorizare**, doar pentru firme românești, opțiunea **Dezmembrare: reclasificare mărfuri și materiale**. Categoriile produselor trebuie să aibă cont de valorizare a stocului și cont de cheltuieli, iar firma un jurnal de stoc.
- Funcționează cu localizarea românească a contabilității de stoc (se folosesc conturile pe locații) și fără ea.

#### 3. Dependențe

- `stock_account`

#### 4. Componente Cheie

**Modele**

- `stock.disassembly`: procesul-verbal de dezmembrare (mail.thread, activități); calculează alocarea, validează, creează mișcările de stoc și nota contabilă unică.
- `stock.disassembly.line`: linia rezultată (produs sau pierdere), cu metodă de alocare, valoare fixă, procent, lot și locație de destinație.
- `stock.move` (extins): referință și crearea notei contabile adaptate documentului de dezmembrare.
- `res.company`, `res.config.settings` (extinse): opțiunea de reclasificare mărfuri/materiale.

**Vizualizări**

- `view_stock_disassembly_form` / `view_stock_disassembly_list` / `view_stock_disassembly_search`: formular, listă și căutare pentru procesele-verbale.
- `res_config_settings_view_form_stock_disassembly`: opțiunea din setările de valorizare.
- `action_stock_disassembly` și meniul aferent sub Inventar → Operațiuni → Ajustări.
- `action_report_stock_disassembly`: raportul PDF cu semnături.

**Acțiuni Automate / Acțiuni Server**

- Nu există `ir.cron` sau acțiuni server. Secvența `seq_stock_disassembly` generează numerotarea; regulile multi-companie `stock_disassembly_comp_rule` și `stock_disassembly_line_comp_rule` limitează accesul pe companie (drepturi pentru grupul Inventar / Utilizator).

#### 5. Conexiuni

- `l10n_ro_stock_account`: conturile pe locații, folosite opțional pe contabilitatea românească (referit prin contextul `l10n_ro_stock_move`, fără dependență în manifest).
