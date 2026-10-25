# Partner Merge in Bulk (localizat la `deltatech_partner_merge/index.md`)

- **Nume Tehnic:** `deltatech_partner_merge`
- **Versiune:** `19.0.1.2.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_partner_merge
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_merge`
- **Ultima Ingestie:** `2026-10-23`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul curăță duplicatele din nomenclatorul de parteneri cu două unelte complementare. **Loturile de comasare** unifică în masă fișele care au același CUI, în minute în loc de ore. **Caută dubluri** găsește partenerii probabil duplicați (după CUI, telefon, email sau nume asemănător) și lasă operatorului decizia, grup cu grup. Wizardul standard de unificare din Odoo parcurge foaie cu foaie fiecare pereche de duplicate, prin toate cele ~158 de coloane care referă `res_partner` — abordare suficientă pentru câteva duplicate, dar nefezabilă pe mii de grupuri. Acest modul inversează logica — o singură instrucțiune SQL per coloană, pentru tot lotul deodată — și păstrează cheile externe active pe tot parcursul, astfel încât integritatea e garantată de PostgreSQL, nu de corectitudinea procedurii. Pe o bază de producție cu 538.000 de parteneri, unificarea a 5.350 de fișe a durat aproximativ patru minute și jumătate.

#### 2. Funcționalități Cheie

**Caută dubluri** (meniul `Partner Merge` › `Find Duplicates` / `Duplicate Groups`; nu modifică niciun partener)

- Potriviri exacte pe CUI (fără prefixul de țară), telefon în format E.164 (`0722 …` și `+40 722 …` se întâlnesc) și email (litere mici).
- Nume asemănătoare (fără diacritice și forme juridice, cuvinte sortate) la aceeași stradă sau același cod poștal, sau doar după nume, dacă operatorul alege așa. Compararea se face doar în interiorul unui bloc (același oraș sau aceleași prime litere), ca să nu se compare tot cu tot pe baze mari.
- Fiecare grup are scor (0–100) și motiv („același telefon +40722…”, „nume 92% + aceeași stradă”). **Îmbină** deschide asistentul standard Odoo pe grup, unde operatorul alege fișa păstrată; **Nu sunt dubluri** reține perechea, iar căutările următoare o sar. Un utilizator non-administrator poate îmbina doar fișe cu același email.
- Excluse: partenerii utilizatorilor interni și ai companiilor proprii, un partener și propriile contacte, adresele de facturare/livrare ale aceluiași client, partenerii din companii diferite și valorile comune prea multor parteneri (placeholdere, centrale telefonice), care apar în raport.
- Folosește opțional `rapidfuzz`, `phonenumbers` și `unidecode`, dacă sunt instalate; fără ele revine la `difflib` (mai lent, blocuri de maximum 1.500 parteneri, cele mai mari fiind listate în raport). Niciuna nu e obligatorie.
- Traducere în română inclusă (`i18n/ro.po`). Pașii detaliați și capturile sunt în fișa consultant.

**Loturi de comasare în masă (același CUI)**

- Grupează automat partenerii companii active cu același CUI (normalizat) și îi clasifică în 4 categorii: A (restul fișelor sunt complet goale), B (documente pe o singură fișă), C (facturi pe mai multe fișe) și D (sold nereconciliat pe mai multe fișe) — ultimele două se lasă pe mâna contabilului, deoarece mută bani între jurnale.
- Alege automat fișa păstrată după volumul de documente (facturi, apoi comenzi de vânzare, apoi vechime), și semnalează cu un steag fișele al căror nume pare corupt la import, alături de numele fișelor absorbite pentru corectare ulterioară.
- Exclude automat din unificare grupurile care conțin compania proprie, grupurile cu utilizatori portal pe mai multe fișe și grupurile ale căror denumiri diferă complet pe același CUI.
- Etapă de simulare obligatorie: rulează întreaga unificare pe un savepoint separat și îl anulează, deci nu poate scrie date chiar dacă procedura ar avea o eroare; aplicarea efectivă e un pas distinct, protejat de un grup de securitate propriu.
- Refuză să finalizeze aplicarea dacă a rămas vreo referință care încă indică o fișă absorbită.
- Verificare post-unificare: compară totalurile reale ale fișelor păstrate (facturi, comenzi, sold) cu o fotografie luată înainte de unificare.
- Opțiune de arhivare în loc de ștergere a fișelor absorbite (recomandat pentru primele rulări în producție, recuperabil fără restaurare din backup).
- Detectează și oferă creare cu un click pentru coloanele cheie externă către `res_partner` care nu au index — altfel ștergerea partenerilor devine lentă din cauza scanărilor complete de tabel.
- Aceeași procedură e disponibilă și ca scripturi SQL simple în `deltatech/scripts/partner_merge/`, pentru rulare directă din psql, în afara Odoo.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `partner.duplicate.scan`: o căutare de dubluri — opțiunile (inclusiv `use_name` pentru nume asemănător), rularea potrivirilor pe CUI/telefon/email/nume și raportul căutării.
- `partner.duplicate.group`: un grup de parteneri probabil duplicați, cu scor, tip de potrivire, motiv și stare; de aici se deschide asistentul standard de îmbinare.
- `partner.duplicate.ignore`: perechile marcate „nu sunt dubluri”, excluse din căutările viitoare.
- `models/duplicate_tools.py`: funcții ajutătoare de normalizare (nume, telefon, CUI) pentru potrivire.
- `partner.merge.batch`: modelul central al unui lot de unificare — configurează categoriile și limita de grupuri, rulează analiza (construiește tabelele de lucru `pm_face`/`pm_group`/`pm_map`/`pm_snapshot`), simularea (pe savepoint, cu rollback garantat), aplicarea efectivă (remap FK-uri și legături polimorfe, completare câmpuri goale pe fișa păstrată, ștergere/arhivare fișe absorbite) și verificarea finală a totalurilor.
- `partner.merge.batch.line`: o linie per grup de duplicate dintr-un lot — reține fișa păstrată, CUI-ul normalizat, categoria, numărul și ID-urile fișelor absorbite, numele lor (capturate înainte de ștergere) și un indicator calculat `name_suspect` pentru nume care par corupte la import.
- `models/sql_queries.py`: nu e model Odoo, ci modulul Python cu toate interogările SQL brute folosite de unificare (construirea tabelelor de lucru, deduplicarea coliziunilor pe indecși unici, remap-ul cheilor externe și al legăturilor polimorfe, completarea câmpurilor goale, ștergerea/arhivarea și verificarea totalurilor) — sincronizat manual cu scripturile psql din `deltatech/scripts/partner_merge/`.

**Vizualizări**

- `view_partner_duplicate_scan_form` / `view_partner_duplicate_scan_list`: formularul și lista căutărilor de dubluri.
- `view_partner_duplicate_group_list` / `_form` / `_search`: grupurile găsite, cu acțiunile Îmbină și Nu sunt dubluri.
- Meniurile `Find Duplicates` și `Duplicate Groups`, sub `Partner Merge`.
- `view_partner_merge_batch_form`: formularul lotului de unificare, cu butoane de flux (Analyze, Simulate, Apply, Verify, Back to draft) condiționate de stare, avertisment pentru coloane FK fără index, lista grupurilor din lot (cu evidențiere pentru nume suspecte) și rapoartele de analiză/simulare/aplicare/clasificare.
- `view_partner_merge_batch_list`: lista loturilor, cu numărul de grupuri, numărul de fișe și starea (badge colorat).
- `action_partner_merge_batch` / meniul `Partner Merge` (sub Setări → Administrare): punctul de intrare în funcționalitate, vizibil doar grupului `group_partner_merge_prepare`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` — fluxul este integral declanșat manual de utilizator, prin butoanele din formularul căutării de dubluri și al lotului (`action_analyze`, `action_simulate`, `action_apply`, `action_verify`, `action_reset`, `action_create_indexes`).

#### 5. Conexiuni

Nu au fost identificate module cu pagină wiki proprie legate funcțional de acest modul; el interoperează direct la nivel de tabele SQL cu modelele `account.move`, `sale.order`, `purchase.order`, `stock.picking` și `res.users` (verificate condiționat prin `to_regclass`, ca modulul să rămână dependent doar de `base`), fără a le declara ca dependențe Odoo.
