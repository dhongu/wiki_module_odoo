# Account Analytic Split (localizat la `deltatech_account_analytic/index.md`)

- **Nume Tehnic:** `deltatech_account_analytic`
- **Versiune:** `20.0.0.0.11`
- **Cale:** https://github.com/dhongu/deltatech/tree/20.0/deltatech_account_analytic
- **Cale Locală:** `odoo-addons/deltatech/deltatech_account_analytic`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul îmbunătățește contabilitatea analitică din Odoo în două direcții. Pe de o parte, leagă distribuțiile analitice și articolele analitice de pe facturi de **echipa de vânzări** și păstrează categoria produsului pe fiecare articol analitic, pentru rapoarte mai fine pe echipe și categorii. Pe de altă parte, oferă un instrument de **împărțire a sumelor pe mai multe conturi analitice**, pe baza unor șabloane procentuale reutilizabile — util când o sumă (comision, cost partajat, alocare) trebuie distribuită după o cheie fixă, fără calcule manuale.

#### 2. Funcționalități Cheie

- **Echipă de vânzări pe modelele de distribuție analitică**: pe facturile, notele de credit și chitanțele de vânzare, liniile de produs preiau distribuția modelului a cărui echipă coincide cu echipa facturii, atunci când există exact un astfel de model; distribuția se recalculează când se schimbă echipa facturii.
- **Echipă de vânzări și categorie de produs pe articolele analitice**: echipa provine din factura/nota de credit/chitanța de client; pentru notele contabile ale unui transfer de stoc (cu `stock` și `sale_stock` instalate) din comanda de vânzare a transferului; pe facturile și notele de credit de furnizor, din echipa al cărei nume este identic cu numele contului analitic.
- **Grupare suplimentară** în **Contabilitate → Contabilitate → Tranzacții → Articole analitice** și în **Raportul analitic**: după echipă de vânzări și după categoria produsului.
- **Șabloane de împărțire analitică**: listă de conturi analitice cu procent; procentele trebuie să însumeze 100.
- **Împărțiri analitice**: distribuie o sumă fixă (*Amount*) sau un articol analitic existent (*Line*) după un șablon. *Compute* completează liniile din șablon; *Confirm* creează câte un articol analitic pe linie, la data împărțirii, și verifică totalul (la tipul *Line* articolul original e șters și înlocuit); *Reset* șterge articolele create și readuce în ciornă împărțirea de tip sumă (cea de tip *Line* nu poate fi resetată).
- **Meniuri** sub **Contabilitate → Configurare → Contabilitate analitică** (modele de distribuție, șabloane, împărțiri), vizibile administratorilor contabili când setarea *Analytic Accounting* este activă; accesul la șabloane și împărțiri cere grupul *Analitic split user*.
- **Limitări**: pe facturile de furnizor echipa se găsește doar prin potrivire exactă de nume; o împărțire fără *Name* nu poate fi confirmată (articolele analitice cer descriere). În Community aplicația se numește *Invoicing*.

Fluxul pas-cu-pas, bazele legale și verificările pentru consultant sunt în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account`
- `analytic`
- `sale`
- `purchase`

#### 4. Componente Cheie

**Modele**

- `account.analytic.line` (extins): adaugă `team_id` și `product_category_id` (related stocat din produs).
- `account.move.line` (extins): calculează distribuția analitică după echipa facturii și determină echipa pe facturile de furnizor la generarea liniilor analitice.
- `account.analytic.distribution.model` (extins): adaugă `team_id` (echipă de vânzări).
- `account.analytic.split.template` / `account.analytic.split.template.line`: șablonul de împărțire procentuală.
- `account.analytic.split` / `account.analytic.split.line`: împărțirea propriu-zisă, cu stări `draft` / `confirmed`.
- `res.config.settings` (extins): conține doar extinderea de setări, fără opțiuni active în interfață.

**Vizualizări**

- `view_account_analytic_default_form`: câmpul echipă de vânzări pe modelul de distribuție analitică.
- `view_account_analytic_line_filter`: gruparea după echipă și categorie de produs pe articolele analitice.
- `view_account_analytic_split_form` / `view_account_analytic_split_tree` + `action_analytic_split`: interfața împărțirilor.
- `view_account_analytic_split_t_form` / `view_account_analytic_split_t_tree` + `action_analytic_split_template`: interfața șabloanelor.

**Acțiuni Automate / Acțiuni Server**

Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server`.

#### 5. Conexiuni

Nu au fost identificate conexiuni funcționale către alte module cu pagină în wiki. Modulul extinde modele standard din `account`, `analytic` și `sale` (`crm.team`).
