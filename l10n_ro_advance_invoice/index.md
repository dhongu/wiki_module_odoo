# Romania - Facturi de avans client/furnizor cu TVA (419/4091/4092) (localizat la `l10n_ro_advance_invoice/index.md`)

- **Nume Tehnic:** `l10n_ro_advance_invoice`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_advance_invoice
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_advance_invoice`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru gestionarea facturilor de avans cu TVA conform **Art. 282 alin. 2 Cod Fiscal** (faptul generator = data încasării) și regularizarea automată la factura finală. Este adresat companiilor care încasează sau plătesc avansuri cu TVA înainte de livrarea bunurilor sau prestarea serviciilor.

#### 2. Funcționalități Cheie

- **Factură de avans client** (`out_invoice`, cont 419): marcată cu `l10n_ro_is_advance=True`, ca să poată fi identificată și filtrată. Se emite din wizardul **Factură avans cu TVA** (*Facturare → Clienți → Factură de avans*), în care se aleg tipul avansului, partenerul, suma fără TVA, taxa, jurnalul, data și referința.
- **Factură de avans furnizor** (`in_invoice`, cont 4091): flux simetric cu cel de client.
- **Regularizare automată** la factura finală: în tabul **Avansuri** se aleg avansurile partenerului și se apasă **Aplică avansuri selectate**. Avansul se reia cu minus, pe același cont 419/4091 și cu aceeași taxă ca pe factura de avans, astfel încât baza și TVA-ul facturii scad corect (fără `is_storno` — regularizarea este operațiune normală, nu corecție de eroare). Un avans cu altă cotă de TVA își păstrează cota la regularizare.
- Avansurile deja regularizate nu mai pot fi alese din nou; dacă factura finală este anulată, trecută în ciornă sau stornată, avansul redevine disponibil.
- **D300**: TVA-ul avansului merge în Rd.9/10/11 prin taxele standard `l10n_ro`; nu sunt necesare rânduri distincte.
- **D394**: avansul se raportează ca factură obișnuită (bază + TVA), iar regularizarea cu minus; marcajul `l10n_ro_is_advance` nu este preluat automat de generatorul D394.
- **Raport avansuri neregularizate**: sold 419/4091 deschis, filtrabil per partener/dată.
- **Banner vizual** pe factura de avans și tab „Avansuri" pe factura finală.
- Configurare: nu cere setări proprii; folosește conturile 419/4091 din planul de conturi `l10n_ro`, taxele standard de 21%, 11% sau 5% și jurnalele de vânzări/achiziții existente. Fluxul pas-cu-pas este în fișa consultant.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move`: extins cu câmpul `l10n_ro_is_advance` (marcare factură de avans), legăturile către avansurile regularizate / facturile finale și metodele de aplicare, reconciliere și eliberare a avansurilor.
- `account.move.line`: extins pentru liniile de regularizare a avansului.
- `l10n.ro.advance.wizard`: wizardul de emitere a facturii de avans (tip avans, partener, sumă netă, taxă, jurnal, dată, referință).

**Vizualizări**

- `account_move_views.xml`: bannerul pe factura de avans și tabul „Avansuri" (selectare avansuri, buton „Aplică avansuri selectate") pe factura finală.
- `l10n_ro_advance_wizard_views.xml`: formularul wizardului de emitere.
- `l10n_ro_advance_report_views.xml`: raportul avansurilor neregularizate.

**Acțiuni Automate / Acțiuni Server**

- `action_create_advance()`: creează factura de avans cu TVA din wizard, marcată cu `l10n_ro_is_advance=True`.
- `_l10n_ro_apply_advances()`: aplică avansurile selectate, generând liniile negative de regularizare pe 419/4091.
- `action_l10n_ro_unregularized_advances()`: deschide raportul avansurilor neregularizate.
- Nu există sarcini `ir.cron`.

#### 5. Conexiuni

- `l10n_ro`: furnizează conturile 419/4091 și taxele standard folosite de avans.
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): avansul apare în declarație ca factură obișnuită; marcajul de avans nu este preluat automat.
