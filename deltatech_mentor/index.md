# Mentor Interface (localizat la `deltatech_mentor/index.md`)

- **Nume Tehnic:** `deltatech_mentor`
- **Versiune:** `19.0.2.2.1`
- **Cale:** `https://github.com/terrabit-solutions/bitshop/tree/19.0/deltatech_mentor`
- **Cale Locală:** `odoo-addons/bitshop/deltatech_mentor`
- **Ultima Ingestie:** `2026-10-22`

#### 1. Sumar

Modulul permite companiilor care țin contabilitatea în WinMentor, dar lucrează cu vânzările, achizițiile și stocurile în Odoo, să transfere documentele fără reintroducere manuală. Pentru o perioadă aleasă, Odoo generează într-o singură arhivă ZIP fișierele text pe care WinMentor le preia prin meniul „Import date din alte aplicații": parteneri, articole, facturi de furnizor și de client, documente de stoc și producție, plăți și încasări.

#### 2. Funcționalități Cheie

- **Parteneri și articole:** exportate cu codurile după care WinMentor face potrivirea: codul fiscal (CUI, cu RO pentru plătitorii de TVA) sau CNP pentru persoane fizice, respectiv referința internă a produsului sau un cod pe categorie de produs. Partenerii și articolele se importă în WinMentor o singură dată; modificările ulterioare trebuie făcute în ambele sisteme.
- **Achiziții:** facturi și note de credit de furnizor, separate în interne și intracomunitare (cu taxare inversă), importuri din afara UE (cu codul de vamă) și bonuri fiscale de intrare. Opțiunea de filtrare după data facturii (în loc de data contabilă) este dezactivată implicit.
- **Vânzări:** facturi, note de credit și bonuri de vânzare, un fișier per jurnal, cu seria facturii preluată din jurnal (câmpul „Serie Carnet Mentor"); numărul documentului se ia din numele documentului Odoo.
- **Stoc și producție:** bonuri de consum și recepții de producție între locația de stoc și cea de producție, avize de intrare și de ieșire, lista gestiunilor.
- **Plăți și încasări:** opțional, plățile și încasările înregistrate în perioadă, câte un fișier per jurnal; plata către furnizor preia numărul și seria facturii reconciliate.
- **Conturi contabile românești:** conturile Odoo sunt convertite în conturi WinMentor (cont sintetic fără zerourile de la sfârșit, sufix analitic pe numărul de cifre ales).
- **O singură companie o dată:** se exportă doar documentele companiei alese; jurnalele și locațiile altei companii sunt refuzate.
- **Cale de acces:** *Contabilitate > Contabilitate > Mentor > Export Mentor* (pentru managerii contabili). În wizard se aleg perioada, compania, jurnalele (toate dacă rămâne gol), locațiile de stoc și producție și opțiunile: cod de vamă pentru importuri, cod fix pentru persoane fizice, plăți și încasări, produse ca servicii, numărul de cifre analitice.
- **Tratarea erorilor:** un partener fără cod fiscal sau un produs fără cod oprește exportul, cu numele afișat; „Ignore Errors" le listează în rezultat și continuă exportul. O factură de furnizor cu linie fără produs oprește exportul; liniile de tip secțiune, subsecțiune sau notă ajung în observațiile documentului.
- **Configurare în Odoo:** pe categoria de produs se completează Simbol Tip Contabil, Gestiune Mentor, Way Production (pentru categorii de producție), Mentor UOM și, dacă se dorește export ca articol unic, Cod Articol (debifând „Mentor Use Article"); pe locațiile de stoc, Simbol Mentor; pe jurnale, Serie Carnet Mentor.
- **Import în WinMentor:** se despachetează arhiva și fiecare fișier se importă din *Intrări > Import date din alte aplicații*, începând cu partenerii și articolele; pentru facturile de intrare se alege seria NIR („Carnet NIR") și fișierul „Facturi Intrare". Partenerii se mapează după codul fiscal, articolele după cod.

#### 3. Dependențe

- `account`
- `product`
- [deltatech_contact](../deltatech_contact/index.md)
- `stock`
- `stock_account`
- `l10n_ro`

Dependență externă Python: `configparser`.

#### 4. Componente Cheie

**Modele**

- `export.mentor`: wizard de export; generează arhiva ZIP cu fișierele pentru WinMentor.
- `product.category` (extins): câmpurile WinMentor (tip contabil, gestiune, unitate de măsură, cod articol).
- `stock.location` (extins): simbolul gestiunii Mentor.
- `account.journal` (extins): seria de carnet Mentor.
- `res.partner` (extins): adaptări pentru exportul partenerilor.
- `stock.picking` (extins): adaptări pentru exportul avizelor.

**Vizualizări**

- `view_export_mentor_form`: formularul wizardului de export.
- `product_category_form_view`: câmpurile Mentor pe categoria de produs.
- `view_location_form`: simbolul Mentor pe locația de stoc.
- `view_account_journal_form`: seria de carnet Mentor pe jurnal.

**Acțiuni Automate / Acțiuni Server**

- `action_export_mentor`: acțiunea de fereastră care deschide wizardul de export din meniul Mentor.

#### 5. Conexiuni

- [deltatech_contact](../deltatech_contact/index.md): sursa datelor de contact ale partenerilor folosite la export (CUI, potrivire în WinMentor).
