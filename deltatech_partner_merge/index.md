# Partner Merge in Bulk (localizat la `deltatech_partner_merge/index.md`)

- **Nume Tehnic:** `deltatech_partner_merge`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_partner_merge
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_merge`
- **Ultima Ingestie:** `2026-08-20`

#### 1. Sumar

Modulul unifică în masă fișele de parteneri duplicate care au același CUI, în minute în loc de ore. Wizardul standard de unificare din Odoo parcurge foaie cu foaie fiecare pereche de duplicate, prin toate cele ~158 de coloane care referă `res_partner` — abordare suficientă pentru câteva duplicate, dar nefezabilă pe mii de grupuri. Acest modul inversează logica — o singură instrucțiune SQL per coloană, pentru tot lotul deodată — și păstrează cheile externe active pe tot parcursul, astfel încât integritatea e garantată de PostgreSQL, nu de corectitudinea procedurii. Pe o bază de producție cu 538.000 de parteneri, unificarea a 5.350 de fișe a durat aproximativ patru minute și jumătate.

#### 2. Funcționalități Cheie

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

- `partner.merge.batch`: modelul central al unui lot de unificare — configurează categoriile și limita de grupuri, rulează analiza (construiește tabelele de lucru `pm_face`/`pm_group`/`pm_map`/`pm_snapshot`), simularea (pe savepoint, cu rollback garantat), aplicarea efectivă (remap FK-uri și legături polimorfe, completare câmpuri goale pe fișa păstrată, ștergere/arhivare fișe absorbite) și verificarea finală a totalurilor.
- `partner.merge.batch.line`: o linie per grup de duplicate dintr-un lot — reține fișa păstrată, CUI-ul normalizat, categoria, numărul și ID-urile fișelor absorbite, numele lor (capturate înainte de ștergere) și un indicator calculat `name_suspect` pentru nume care par corupte la import.
- `models/sql_queries.py`: nu e model Odoo, ci modulul Python cu toate interogările SQL brute folosite de unificare (construirea tabelelor de lucru, deduplicarea coliziunilor pe indecși unici, remap-ul cheilor externe și al legăturilor polimorfe, completarea câmpurilor goale, ștergerea/arhivarea și verificarea totalurilor) — sincronizat manual cu scripturile psql din `deltatech/scripts/partner_merge/`.

**Vizualizări**

- `view_partner_merge_batch_form`: formularul lotului de unificare, cu butoane de flux (Analyze, Simulate, Apply, Verify, Back to draft) condiționate de stare, avertisment pentru coloane FK fără index, lista grupurilor din lot (cu evidențiere pentru nume suspecte) și rapoartele de analiză/simulare/aplicare/clasificare.
- `view_partner_merge_batch_list`: lista loturilor, cu numărul de grupuri, numărul de fișe și starea (badge colorat).
- `action_partner_merge_batch` / meniul `Partner Merge` (sub Setări → Administrare): punctul de intrare în funcționalitate, vizibil doar grupului `group_partner_merge_prepare`.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` — fluxul este integral declanșat manual de utilizator, prin butoanele din formularul lotului (`action_analyze`, `action_simulate`, `action_apply`, `action_verify`, `action_reset`, `action_create_indexes`).

#### 5. Conexiuni

Nu au fost identificate module cu pagină wiki proprie legate funcțional de acest modul; el interoperează direct la nivel de tabele SQL cu modelele `account.move`, `sale.order`, `purchase.order`, `stock.picking` și `res.users` (verificate condiționat prin `to_regclass`, ca modulul să rămână dependent doar de `base`), fără a le declara ca dependențe Odoo.
