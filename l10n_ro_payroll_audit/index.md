# Romania - Pistă de audit pe salarizare (localizat la `l10n_ro_payroll_audit/index.md`)

- **Nume Tehnic:** `l10n_ro_payroll_audit`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_payroll_audit
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_payroll_audit`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modificările care contează la un control din salarizare (salariul, contractul, ajustările salariale, regulile și parametrii legali) intră în pista de audit imuabilă a modulului `l10n_ro_audit_immutable`: cine a făcut modificarea, când, care a fost valoarea veche și care cea nouă. Se folosește același ecran (*Contabilitate → Rapoarte → Pistă de Audit*), fără un al doilea jurnal. Modulul este în stadiu Alpha.

#### 2. Funcționalități Cheie

- **Contractul salariatului** (`hr.version`): se auditează salariul și tipul de salariu, datele contractului, tipul structurii și al contractului, departamentul, funcția, programul de lucru, CNP, persoanele în întreținere, deducerile și scutirile RO, tichetele de masă.
- **Ajustările salariale** (rețineri, popriri, pensie de întreținere): tipul, sumele, perioada, starea, dosarul și creditorul.
- **Regulile salariale**: codul, secvența, condiția și formula.
- **Parametrii legali** (salariu minim, plafoane): valoarea și data de început.
- **Fluturașul**: salariatul, structura, perioada și starea (validare, anulare).
- **Conturile bancare** ale partenerilor (IBAN-ul salariaților).
- Nu se înregistrează liniile fluturașului și intrările lui, care se recalculează la fiecare calcul și ar umple pista.
- Instalarea `l10n_ro_audit_immutable` activează lanțul de hash pe jurnalele contabile ale companiilor românești.

#### 3. Dependențe

- [l10n_ro_audit_immutable](../l10n_ro_audit_immutable/index.md)
- [l10n_ro_hr_payroll_enhancement](../l10n_ro_hr_payroll_enhancement/index.md)

#### 4. Componente Cheie

**Modele**

Toate modelele sunt extinse cu mixin-ul `l10n.ro.audit.mixin`, care definește prin `_l10n_ro_audit_fields()` lista câmpurilor urmărite.

- `hr.version`: contractul/versiunea salariatului (salariu, date contract, structură, departament, funcție, program, CNP, deduceri RO, tichete de masă).
- `hr.salary.attachment`: rețineri, popriri, pensie de întreținere (sume, perioadă, stare, dosar, creditor).
- `hr.salary.rule`: regula salarială (cod, secvență, condiție, formulă, sumă fixă/procent).
- `hr.rule.parameter.value`: valorile parametrilor legali (parametru, data de început, valoare).
- `hr.payslip`: fluturașul (salariat, contract, structură, perioadă, stare, notă de credit).
- `res.partner.bank`: conturi bancare (număr cont, partener, bancă, activ).

**Vizualizări**

Modulul nu definește vizualizări proprii; folosește ecranul Pistă de Audit din `l10n_ro_audit_immutable`.

**Acțiuni Automate / Acțiuni Server**

Nu există.

#### 5. Conexiuni

- [l10n_ro_hr_payroll_account_enhancement](../l10n_ro_hr_payroll_account_enhancement/index.md): extensia contabilă a salarizării românești, în același ecosistem de salarizare.
