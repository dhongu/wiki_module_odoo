# Romania - Corecția metodei de plată POS după bonul fiscal (`l10n_ro_pos_payment_correction`)

- **Nume Tehnic:** `l10n_ro_pos_payment_correction`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_pos_payment_correction
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_payment_correction`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Corectează metoda de plată a unui bon fiscal deja emis fără să strice reconcilierea cu raportul Z. Bonul de pe casa de marcat rămâne cu metoda inițială, iar raportul Z explică diferența pe tipul de plată provocată de corecția din Odoo. Se instalează automat când ambele module de bază sunt prezente.

#### 2. Funcționalități Cheie

- Avertizare la corecție: pentru un bon fiscal emis, managerul vede metoda de pe bon și i se amintește să păstreze nota justificativă lângă raportul Z.
- Metoda de pe bon se păstrează separat pe plată, la prima corecție; corecțiile următoare se raportează față de ea.
- Jurnalul de corecții (*Punct de vânzare → Raportare → Corecții plăți*) marchează corecțiile după emiterea bonului, cu filtru dedicat.
- Raportul Z (*Punct de vânzare → Fiscalizare AMEF → Rapoarte Z*) are pe fiecare tip de plată coloanele *Corecții metodă de plată* și *Diferență neexplicată*; *Reconciliază* trece în *Reconciliat* rapoartele cu diferențe doar din corecții.
- Corecția se permite cu avertizare, în sesiune deschisă, pentru grupul *Punct de vânzare / Administrator*; nu anulează bonul pe aparat. Flux în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_pos_payment_correction](../deltatech_pos_payment_correction/index.md)
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md)

#### 4. Componente Cheie

**Modele**

- `pos.payment`, `pos.order`, `pos.payment.correction` (extinse): metoda de pe bon, avertizarea și marcajul corecției după bon.
- `l10n.ro.pos.z.report` și `l10n.ro.pos.z.report.payment.line` (extinse): coloanele de corecții și diferența neexplicată.

**Vizualizări**

- `view_pos_pos_form`: butonul și câmpurile pe comanda POS.
- `view_pos_payment_correction_list`, `view_pos_payment_correction_form`, `view_pos_payment_correction_search`: jurnalul de corecții.
- `view_l10n_ro_pos_z_report_form`: defalcarea pe tipuri de plată.

**Acțiuni Automate / Acțiuni Server**

- Fără cron sau acțiuni server.

#### 5. Conexiuni

- [deltatech_pos_payment_correction](../deltatech_pos_payment_correction/index.md): corecția de bază a metodei de plată.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): fiscalizarea AMEF și raportul Z.
