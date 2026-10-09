# Romania - CNP partener (localizat la `l10n_ro_partner_cnp/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_cnp`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_cnp
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_cnp`
- **Ultima Ingestie:** `2026-10-09`

#### 1. Sumar

Modulul adaugă pe partener codul numeric personal (CNP) al persoanelor fizice din România și verifică la salvare că este corect, inclusiv cifra de control. Este un modul de bază, fără ecrane proprii, folosit de modulele care declară venituri plătite persoanelor fizice (zilieri, drepturi de autor), astfel încât CNP-ul să fie definit o singură dată și validat unitar.

#### 2. Funcționalități Cheie

- Câmpul `CNP` pe partener, tratat ca dată cu caracter personal: vizibil doar utilizatorilor interni.
- Validare la salvare: 13 cifre, prima cifră între 1 și 8 și cifra de control corectă. Un CNP greșit este respins cu mesajul „CNP invalid”, nu este golit.
- Indicatorul stocat `CNP valid`, utilizabil în filtre și în verificări înainte de declarații.
- Fără meniu propriu: CNP-ul se completează din documentele care îl cer, adică registrul zilierilor (`l10n_ro_payroll_day_labourers`, coloana *CNP*) și contractul de drepturi de autor (`l10n_ro_payroll_copyright`, câmpul *CNP* al autorului).
- Cu [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md) instalat, CNP-ul apare și pe formularul partenerului, sub codul fiscal.
- Compatibil cu `l10n_ro_efactura_consumer` (e-Factura B2C): câmpul are aceeași definiție, deci cele două module pot fi instalate împreună și folosesc aceeași valoare, fără migrare.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): câmpurile `l10n_ro_cnp` (CNP) și `l10n_ro_cnp_valid` (calculat, stocat), plus constrângerea `_check_l10n_ro_cnp` care ridică `ValidationError` pentru un CNP invalid. Funcția `validate_cnp` verifică lungimea, prima cifră și cifra de control (ponderi 2-7-9-1-4-6-3-5-8-2-7-9, modulo 11).

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md): același câmp `l10n_ro_cnp`, definit identic; instalate împreună, folosesc aceeași valoare.
- `l10n_ro_payroll_day_labourers`: zilieri (Legea 52/2011), declarați nominal în D112; folosește CNP-ul partenerului.
- `l10n_ro_payroll_copyright`: drepturi de proprietate intelectuală, declarate nominal în D112; folosește CNP-ul partenerului.
