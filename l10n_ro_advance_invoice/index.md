# Romania - Facturi de avans client/furnizor cu TVA (419/4091/4092) (localizat la `l10n_ro_advance_invoice/index.md`)

- **Nume Tehnic:** `l10n_ro_advance_invoice`
- **Versiune:** `19.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_advance_invoice
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_advance_invoice`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru gestionarea facturilor de avans cu TVA conform **Art. 282 alin. 2 Cod Fiscal** (faptul generator = data încasării) și regularizarea automată la factura finală. Este adresat companiilor care încasează sau plătesc avansuri cu TVA înainte de livrarea bunurilor sau prestarea serviciilor.

#### 2. Funcționalități Cheie

- **Factură de avans client** (`out_invoice`, cont 419): marcată cu `l10n_ro_is_advance=True`, ca să poată fi identificată și filtrată. Se emite din wizardul **Factură avans cu TVA** (**Facturare → Clienți → Factură de avans**), cu tip avans, partener, sumă fără TVA, taxă, jurnal, dată și referință; fără taxă se obține un avans fără TVA.
- **Factură de avans furnizor** (`in_invoice`, cont 4091): flux simetric; pentru servicii sau imobilizări contul liniei se schimbă manual în 4092/4093/4094 înainte de confirmare.
- **Regularizare automată** la factura finală: din tabul **Avansuri**, butonul **Aplică avansuri selectate** reia avansul cu minus, pe același cont 419/4091 și cu aceeași taxă ca pe factura de avans, astfel încât baza și TVA-ul facturii scad corect (fără `is_storno` — regularizarea este operațiune normală, nu corecție de eroare). Se pot aplica mai multe avansuri, cu cote de TVA diferite sau în valută (regularizarea se face la cursul avansului); reaplicarea înlocuiește liniile, nu le dublează, iar o sumă de avansuri mai mare decât factura finală este refuzată.
- **Reconciliere automată** pe 419/4091 la confirmarea facturii finale; la trecerea în ciornă sau la stornarea ei reconcilierea se desface, iar avansul redevine neregularizat.
- **D300**: TVA-ul avansului merge în Rd.9/10/11 prin taxele standard `l10n_ro`; nu sunt necesare rânduri distincte.
- **D394**: avansul se raportează ca factură obișnuită (bază + TVA), iar regularizarea cu minus; marcajul `l10n_ro_is_advance` nu este preluat automat de generatorul D394, ci servește doar la filtrare și urmărire.
- **Raport avansuri neregularizate** (**Facturare → Clienți → Avansuri neregularizate**): avansuri clienți/furnizori postate, fără regularizare pe o factură finală confirmată; filtrabil per partener, dată și tip. Regularizările parțiale (editate manual) nu sunt reflectate în listă.
- **Banner vizual** pe factura de avans și tab „Avansuri" pe factura finală.

#### 3. Dependențe

- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `account.move` (extins): câmpul `l10n_ro_is_advance` (marcare factură de avans), legăturile `l10n_ro_advance_ids` (avansuri regularizate pe factura finală), `l10n_ro_final_invoice_ids` („Regularizat în”) și `l10n_ro_settlement_line_ids`, câmpurile calculate `l10n_ro_advance_settled`, `l10n_ro_advance_net` și `l10n_ro_advance_vat`, plus logica de aplicare, reconciliere și eliberare a avansurilor (inclusiv la `_post` și `button_draft`).
- `account.move.line` (extins): `l10n_ro_advance_line` și `l10n_ro_advance_move_id` marchează liniile de regularizare și avansul de origine; cursul liniei se preia de la avans.
- `l10n.ro.advance.wizard`: wizardul de emitere a facturii de avans (tip avans, partener, sumă, taxă, jurnal, dată, referință).

**Vizualizări**

- `view_move_form_l10n_ro_advance`: adaugă bannerul **Factură de avans** pe avans și tabul **Avansuri** (selectarea avansurilor, butonul **Aplică avansuri selectate**) pe factura finală.
- `view_l10n_ro_advance_wizard_form`: formularul wizardului **Factură avans cu TVA**, deschis din meniul `menu_l10n_ro_advance_wizard`.
- `view_l10n_ro_unregularized_advances_list`: lista filtrabilă a avansurilor neregularizate (meniul `menu_l10n_ro_unregularized_advances`).

**Acțiuni Automate / Acțiuni Server**

- `action_l10n_ro_advance_wizard`: deschide wizardul de emitere a avansului (`action_create_advance` creează factura în ciornă, cu `l10n_ro_is_advance=True`).
- `action_l10n_ro_apply_advances` (`_l10n_ro_apply_advances`): aplică avansurile selectate pe factura finală, generând liniile negative de regularizare pe 419/4091 cu taxa avansului.
- `action_l10n_ro_unregularized_advances`: deschide raportul cu avansurile neregularizate.
- Nu există cron-uri sau reguli `base.automation`.

#### 5. Conexiuni

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): declarația D394 preia facturile de avans ca facturi obișnuite; marcajul `l10n_ro_is_advance` nu este citit de generator.
- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): TVA-ul avansului și al regularizării ajunge în decont prin tag-urile taxelor standard.
