# Romania - CNP partener (localizat la `l10n_ro_partner_cnp/index.md`)

- **Nume Tehnic:** `l10n_ro_partner_cnp`
- **Versiune:** `19.0.1.1.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_partner_cnp
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_partner_cnp`
- **Ultima Ingestie:** `2026-10-12`

#### 1. Sumar

Modulul adaugă pe partener codul numeric personal (CNP) al persoanelor fizice din România și verifică la salvare că este corect, inclusiv cifra de control. Totodată păstrează codul fiscal al partenerilor din România curat: conține doar CUI/CIF, iar CNP-ul stă în câmpul propriu, iar persoanele cu CUI valid (PFA, II, IF, ONG) sunt marcate ca entități, ca e-Factura să le trimită în fluxul B2B. Este un modul de bază, fără ecrane proprii, folosit de modulele care declară venituri plătite persoanelor fizice (zilieri, drepturi de autor), astfel încât CNP-ul să fie definit o singură dată și validat unitar.

#### 2. Funcționalități Cheie

- Câmpul `CNP` pe partener, tratat ca dată cu caracter personal: vizibil doar utilizatorilor interni.
- Validare la salvare: 13 cifre, prima cifră între 1 și 8 și cifra de control corectă. Un CNP greșit este respins cu mesajul „CNP invalid”, nu este golit.
- Indicatorul stocat `CNP valid`, utilizabil în filtre și în verificări înainte de declarații.
- Fără meniu propriu: CNP-ul se completează din documentele care îl cer, adică registrul zilierilor (`l10n_ro_payroll_day_labourers`, coloana *CNP*) și contractul de drepturi de autor (`l10n_ro_payroll_copyright`, câmpul *CNP* al autorului).
- Codul fiscal conține doar CUI/CIF: un CNP introdus în codul fiscal al unui partener din România se mută automat în câmpul CNP (și în `cnp` din [deltatech_contact](../deltatech_contact/index.md), dacă există și e gol). Dacă partenerul are deja alt CNP, salvarea este refuzată.
- Partenerul din România marcat ca persoană fizică, dar cu CUI/CIF valid în codul fiscal (PFA, II, IF, ONG), devine automat entitate (Companie), regulă care reproduce calculul `is_company` din Odoo 20. Excepții: dacă există deja o companie cu același CUI (contact desprins de firmă), partenerul rămâne persoană fizică și apare doar în log; contactele copil, partenerii arhivați, partenerii străini și NIF-ul 9000… nu se ating.
- Datele existente se corectează la instalare și la update; fiecare modificare, dublură sau conflict se scrie în log. Facturile deja transmise în SPV nu se retransmit.
- Cu [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md) instalat, CNP-ul apare și pe formularul partenerului, sub codul fiscal.
- Compatibil cu `l10n_ro_efactura_consumer` (e-Factura B2C): câmpul are aceeași definiție, deci cele două module pot fi instalate împreună și folosesc aceeași valoare, fără migrare.

#### 3. Dependențe

- `base`

#### 4. Componente Cheie

**Modele**

- `res.partner` (extins): câmpurile `l10n_ro_cnp` (CNP) și `l10n_ro_cnp_valid` (calculat, stocat), plus constrângerea `_check_l10n_ro_cnp` care ridică `ValidationError` pentru un CNP invalid. Funcția `validate_cnp` verifică lungimea, prima cifră și cifra de control (ponderi 2-7-9-1-4-6-3-5-8-2-7-9, modulo 11). Suprascrie `create` și `write` (la schimbarea `vat`, `country_id`, `parent_id`, `active`, `is_company`) și apelează `_l10n_ro_sync_vat_identity`, care mută CNP-ul din `vat` și setează `is_company` după CUI; `_l10n_ro_fix_vat_identity_all` face corecția pe datele existente, fără erori, totul în log.

**Vizualizări**

- Modulul nu definește vizualizări proprii.

**Acțiuni Automate / Acțiuni Server**

- `post_init_hook` (la instalare) și `migrations/19.0.1.1.0/post-migrate.py` (la update): rulează corecția `_l10n_ro_fix_vat_identity_all` pe partenerii din România de nivel superior cu cod fiscal.

#### 5. Conexiuni

- [l10n_ro_efactura_consumer](../l10n_ro_efactura_consumer/index.md): același câmp `l10n_ro_cnp`, definit identic; instalate împreună, folosesc aceeași valoare.
- [deltatech_contact](../deltatech_contact/index.md): câmpul opțional `cnp`, completat la mutarea unui CNP din codul fiscal, dacă este gol.
- `l10n_ro_payroll_day_labourers`: zilieri (Legea 52/2011), declarați nominal în D112; folosește CNP-ul partenerului.
- `l10n_ro_payroll_copyright`: drepturi de proprietate intelectuală, declarate nominal în D112; folosește CNP-ul partenerului.
