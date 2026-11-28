# Romania - Popriri pe salarii (`l10n_ro_payroll_garnishment`)

- **Nume Tehnic:** `l10n_ro_payroll_garnishment`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_payroll_garnishment
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_garnishment`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Reținerile din deciziile primite de angajator (pensie de întreținere, poprire, cesiune) se opresc pe fluturaș la plafonul legal din venitul net, nu la suma din decizie. Fluturașul avertizează când suma cerută depășește ce se poate reține, iar restul rămâne datorat pe ajustarea salarială cu sumă totală. Pe ajustare se țin numărul dosarului de executare, executorul sau beneficiarul și contul de virare.

#### 2. Funcționalități Cheie

- Plafoane legale (CPC art. 728; Codul muncii art. 169): pensia de întreținere cel mult 1/2 din venitul net, poprirea pentru alte datorii cel mult 1/3, toate la un loc cel mult 1/2.
- Ordinea aplicată: întreținere, poprire, cesiune (simplificare a ordinii din Codul muncii art. 169 alin. 3).
- Avertizare pe fluturaș când se reține mai puțin decât s-a cerut; restul se reține în lunile următoare.
- Ajustări salariale (*Stat de plată → Fluturași de salariu → Payslip Adjustments*) cu regulile *Pensie alimentară*, *Poprire salarială* și *Alocarea salariilor*, completate cu *Nr. dosar de executare*, *Executor / creditor* și *Cont creditor*.
- Coloanele opționale *Sumă plătită* și *Sumă rămasă* urmăresc datoria totală pe ajustare.
- Protecția salariului minim net, opțională, prin parametrul *Romania Garnishment Parameters* (`salariu_minim_net`; cu 0 nu se aplică).
- Nota contabilă (cu `l10n_ro_hr_payroll_account_enhancement`) înregistrează reținerile 421 = 4271; virarea către executor (427 = 5121) se face separat.
- Fluxul pas-cu-pas este în [fișa consultantului](FISA_CONSULTANT.md).

#### 3. Dependențe

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

- `hr.salary.attachment` (extins): câmpurile dosarului de executare, executor și cont creditor, suma plătită și suma rămasă.
- `hr.payslip` (extins): plafonarea reținerilor și avertizarea de depășire.

**Vizualizări**

- `hr_salary_attachment_view_form_l10n_ro_garnishment`: câmpurile suplimentare pe formularul ajustării salariale.

**Acțiuni Automate / Acțiuni Server**

- Fără cron sau acțiuni server. Datele conțin parametrul `hr.rule.parameter` pentru protecția salariului minim și adaptări ale regulilor salariale de pensie alimentară, poprire și cesiune.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md): fluturașul românesc pe care se aplică plafoanele.
- `l10n_ro_hr_payroll_account_enhancement`: nota contabilă a reținerilor, la instalare opțională.
