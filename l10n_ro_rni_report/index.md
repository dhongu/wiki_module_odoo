# Romania - Raport recepții nefacturate (408) (localizat la `l10n_ro_rni_report/index.md`)

- **Nume Tehnic:** `l10n_ro_rni_report`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_rni_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_rni_report`
- **Ultima Ingestie:** `2026-09-12`

#### 1. Sumar

Modulul aduce raportul din spatele soldului contului 408 (marfă primită fără factură): soldul contului arată cât se datorează, dar nu și pentru ce anume. Raportul listează recepțiile care încă își așteaptă factura, grupate pe furnizor, cu vechimea fiecăreia și cu drill-down până la documentul individual — exact lista cerută la închiderea lunii.

#### 2. Funcționalități Cheie

- Raport contabil (`account.report`) "Goods Received Not Invoiced (408)", disponibil în meniul Contabilitate → Raportare → Situații legale (Legal Statements).
- Grupare pe furnizor, cu drill-down pe fiecare înregistrare/document individual de pe conturile 408.
- Pentru fiecare nivel afișează: valoare recepționată, valoare decontată prin facturi, sold rămas și vechimea (în zile) a celei mai vechi înregistrări nedecontate.
- Furnizorii cu sold stins (recepționat și facturat integral) nu apar în listă.
- Soldul afișat e cumulat până la data de sfârșit a perioadei selectate (nu doar mișcarea perioadei) — o recepție veche nefacturată continuă să apese soldul lunilor următoare; filtrul de dată restrânge doar ce apare ca document nou.
- Funcționează cu ambele mecanisme de contare a 408 existente în suită, pornind din contabilitate — singura lor sursă comună:
  - `l10n_ro_stock_gestiune`: notă separată `371 = 408` la recepție, stinsă de factură prin rutarea liniei de produs pe 408, fără reconciliere; când legătura către recepție există, raportul afișează transferul (numărul recepției), nu numărul notei contabile.
  - `l10n_ro_stock_account` (OCA): pivotul 408 alimentat din valorizarea mișcării marcate `reception_notice`.
- Conturile 408 luate în calcul provin din configurarea explicită (contul de recepție fără factură de pe gestiune sau de pe companie); dacă nu e configurat, raportul cade pe toate conturile al căror cod începe cu `408`.
- Suportă filtrare pe interval de dată, multi-companie (selector) și pe partener; căutare activă în bara raportului.

#### 3. Dependențe

- `account_reports`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.rni.report.handler` (`AbstractModel`, extinde `account.report.custom.handler`): motorul raportului — determină conturile 408 aplicabile companiei/gestiunii, construiește interogarea SQL pe `account_move_line`/`account_move` filtrată pe aceste conturi și pe stare `posted`, și expune agregările pe totaluri, pe furnizor și pe linie individuală (inclusiv rezoluția documentului de recepție din spatele notei contabile, când legătura există).

**Vizualizări**

Raportul nu are vizualizări XML proprii — este randat prin componenta standard `account_report` (client action), configurată integral din `data/rni_report.xml`.

**Acțiuni Automate / Acțiuni Server**

- Nu conține `ir.cron` sau `base.automation`. Definește un `ir.actions.client` (`action_rni_report`, tag `account_report`) și un `menuitem` (`menu_rni_report`) sub meniul standard de situații legale al contabilității, plus raportul `account.report` (`rni_report`) cu 5 coloane (Document, Received, Invoiced, Remaining, Age) și o linie rădăcină grupată pe `partner_id, id`.

#### 5. Conexiuni

- [l10n_ro_stock_gestiune](../l10n_ro_stock_gestiune/index.md): unul din cele două mecanisme de contare a 408 pe care raportul le poate citi; când modulul e instalat, raportul preferă contul configurat pe gestiune și afișează recepția din spatele notei contabile în locul numărului notei.
- `l10n_ro_stock_account` (OCA): al doilea mecanism suportat — pivotul 408 alimentat din valorizarea mișcării marcate `reception_notice`; modulul nu are încă pagină wiki.
