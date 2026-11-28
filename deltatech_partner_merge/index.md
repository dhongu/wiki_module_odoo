# Partner Merge in Bulk (localizat la `deltatech_partner_merge/index.md`)

- **Nume Tehnic:** `deltatech_partner_merge`
- **Versiune:** `20.0.1.2.1`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_partner_merge
- **Cale Locală:** `odoo-addons/deltatech/deltatech_partner_merge`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul unifică în masă fișele de parteneri care au același CUI și caută și dublurile probabile dincolo de CUI. Asistentul standard Odoo parcurge grup cu grup toate cele ~158 de coloane care referă `res_partner`, ceea ce nu se termină într-un timp rezonabil pe mii de grupuri. Modulul inversează buclele: o singură instrucțiune per coloană pentru tot lotul, cu cheile externe active pe tot parcursul, deci integritatea e garantată de PostgreSQL. Pe o bază de producție cu 538.000 de parteneri, unificarea a 5.350 de fișe a durat aproximativ patru minute și jumătate.

#### 2. Funcționalități Cheie

- **Loturi de comasare** (*Settings > Partner Merge > Merge Batches*): fluxul *Analyze*, *Simulate*, *Apply* și, după aplicare, *Verify*. Operatorul alege categoriile de grupuri, numărul de grupuri (*Group Limit*, 0 pentru toate) și dacă fișele absorbite se șterg sau se arhivează (*Archive instead of delete*). Partenerii se grupează după CUI și companie, deci cei din companii diferite nu se unesc niciodată.
- **Simulare sigură**: rulează întreaga unificare într-un savepoint și îl anulează, deci nu poate scrie. Aplicarea e un pas separat, rezervat grupului *Partner Merge / Apply* (administratorii îl au); verifică că partenerii sunt în companiile utilizatorului și refuză finalizarea dacă rămâne vreo referință către o fișă absorbită. Grupul *Partner Merge / Prepare and simulate* poate analiza și simula, dar nu aplica.
- **Verificare**: compară rezultatul cu cifrele de la analiză (facturi, comenzi de vânzare, sold nereconciliat per fișă păstrată).
- **Categorii**: A (o fișă deține documentele, restul sunt goale), B (documente pe o singură fișă), C (facturi pe mai multe fișe), D (sold nereconciliat pe mai multe fișe). Implicit se iau A și B; C și D mută cifre între registre și rămân contabilului. Rămân în afară grupurile cu compania proprie, cele cu utilizatori portal pe mai multe fișe și cele cu nume complet diferite pe același CUI.
- **Fișa păstrată** se alege după volumul de documente (cele mai multe facturi, apoi comenzi, apoi vechime); dacă numele pare corupt la import, e marcată, cu numele fișelor absorbite alături.
- **Indexuri**: dacă lipsesc indexuri pe coloanele cu chei externe către parteneri, lotul afișează un avertisment și butonul *Create the indexes*.
- **Scripturi SQL** echivalente pentru rulare în afara Odoo, în repo-ul suitei (`scripts/partner_merge/`), neincluse în pachetul din Odoo Apps.
- **Căutare dubluri** (*Settings > Partner Merge > Find Duplicates*): nu modifică niciun partener. Potriviri exacte pe CUI (fără prefixul de țară), telefon (E.164) și email (litere mici), plus nume asemănătoare (fără diacritice și forme juridice) la aceeași stradă sau cod poștal, ori doar după nume, la alegere. Fiecare grup are scor și motiv; *Merge* deschide asistentul standard Odoo, iar *Not duplicates* reține perechea pentru scanările viitoare. Se exclud utilizatorii interni, companiile proprii, un partener cu propriile contacte, adresele aceluiași client, parteneri din companii diferite și valorile partajate de prea mulți parteneri (listate în raport).
- Compararea numelor folosește `rapidfuzz` dacă e instalat; altfel `difflib`, mai lent și doar pe blocuri de până la 1.500 de parteneri. `phonenumbers` și `unidecode` se folosesc la fel, dacă există; niciunul nu e obligatoriu.
- Fluxul pas cu pas e în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- `base`
- [deltatech_partner_match](../deltatech_partner_match/index.md)

#### 4. Componente Cheie

**Modele**

- `partner.merge.batch`: lotul de unificare (analiză, simulare, aplicare, verificare).
- `partner.merge.batch.line`: o linie per grup de dubluri dintr-un lot.
- `partner.duplicate.scan`: scanarea dublurilor probabile.
- `partner.duplicate.group`: un grup de dubluri găsit, cu scor și motiv.
- `partner.duplicate.ignore`: perechile marcate „Not duplicates”.

**Vizualizări**

- `views/partner_merge_views.xml`: formularul și lista loturilor de comasare.
- `views/partner_duplicate_views.xml`: scanarea și grupurile de dubluri.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau acțiuni server; fluxul se declanșează manual.

#### 5. Conexiuni

- [deltatech_partner_match](../deltatech_partner_match/index.md): oferă unelte de normalizare și potrivire (`tools.partner_match`) folosite la căutarea dublurilor.
