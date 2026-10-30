# Romania - Pachet vânzare POS și bon fiscal

- **Nume Tehnic:** `l10n_ro_pos_pack`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_pos_pack
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_pos_pack`
- **Ultima Ingestie:** `2026-10-30`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Pachet care aduce, dintr-o singură instalare, vânzarea cu amănuntul din Odoo Point of Sale cu bon fiscal pe casa de marcat și evidența fiscală cerută în România. Bonul se emite la plata comenzii, răspunsul aparatului ajunge pe comandă, sesiunea nu se poate închide cu bonuri lipsă, iar returul, declarația D394 și registrul de casă pornesc din aceleași comenzi. Pachetul nu are cod propriu: instalează modulele POS Terrabit. Se adresează magazinelor și punctelor de lucru care vând prin Odoo POS cu casă de marcat fiscală și vor să evite reintroducerea datelor și reconcilierea manuală între casă și contabilitate. Starea de dezvoltare: Beta.

#### 2. Funcționalități Cheie

- **Bon fiscal din fiecare comandă:** comanda plătită devine fișierul de comenzi al casei de marcat (Datecs, Optima, Incotex, Daisy, Succes) și ajunge la aparat prin agentul local Terrabit Connect, cu liniile, cotele de TVA și metodele de plată așteptate de aparat.
- **Rapoarte X și Z, intrări și ieșiri de numerar:** tipărite pe casa de marcat direct din sesiunea POS.
- **Preț blocat la casă:** o bifă pe fiecare casă (peste *Control preț*) interzice schimbarea manuală a prețului pentru toți, managerii incluși; listele de prețuri și pozițiile fiscale rămân active.
- **Închiderea casei de către casier:** cu autentificarea cu angajați, butonul *Închide casa* este disponibil și casierilor cu drepturi de bază; o diferență de numerar peste limita admisă cere în continuare un manager.
- **Starea bonului pe comandă (OUG 28/1999):** seria aparatului, numărul documentului fiscal, numărul bonului în raportul Z și starea (de fiscalizat, emis, eroare), cu mesajul aparatului păstrat.
- **Sesiune blocată fără bonuri:** închiderea sesiunii se oprește dacă rămân comenzi plătite fără bon emis și fără eroare justificată.
- **Raport Z reconciliat și jurnal electronic AMEF:** raportul Z defalcat pe cote de TVA și metode de plată, confruntat cu vânzările și încasările din Odoo; arhiva aparatului se importă și se potrivește bon cu bon pe numărul Z și numărul bonului.
- **Factură de retur:** fiecare bon de retur produce factura cu valori negative pentru ajustarea bazei de TVA (HG 1/2016, pct. 32), cu cumpărătorul identificat obligatoriu și restituirile de numerar pe rândul de plăți al registrului de casă.
- **Bonurile în D394:** comenzile nefacturate intră în op1 (cu CUI) sau op2 (fără CUI), cu numărul de bonuri și de aparate, fără dubla numărare a notei de sesiune; XML-ul se verifică cu validatorul DUK.
- **Registrul de casă:** raport pe interval de zile, cu sold reportat, cont corespondent, drill-down la nota contabilă și export PDF / XLSX.
- **Configurare (per punct de vânzare):** *Punct de vânzare → Configurare → Setări* (transport Terrabit Connect, serie și NUI aparat AMEF, Fiscalizare AMEF obligatorie, Factură de retur automată și Client obligatoriu la retur, Control preț + Managers included, Cashiers Close the Register), **Cod ECR** pe metodele de plată și pe taxe, iar în *Contabilitate → Configurare → Setări* opțiunea de separare a încasărilor de restituirile în numerar din registrul de casă (contul implicit 5311). Pașii detaliați sunt în fișa consultant.
- **Cerințe și preț:** necesită Odoo Enterprise (`account_reports`, pentru registrul de casă) și agentul local Terrabit Connect; pachetul costă 1 EUR, se plătesc modulele incluse.

#### 3. Dependențe

- [deltatech_pos](../deltatech_pos/index.md)
- [deltatech_pos_price_lock](../deltatech_pos_price_lock/index.md)
- [deltatech_pos_cashier_close](../deltatech_pos_cashier_close/index.md)
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md)
- [l10n_ro_pos_fiscal_compliance_ecr](../l10n_ro_pos_fiscal_compliance_ecr/index.md)
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md)
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md)
- [l10n_ro_cash_register_report](../l10n_ro_cash_register_report/index.md)

#### 4. Componente Cheie

**Modele**

Modulul nu are cod propriu (fără modele, vizualizări sau acțiuni); comportamentul vine din modulele incluse.

**Vizualizări**

Nu are.

**Acțiuni Automate / Acțiuni Server**

Nu are.

#### 5. Conexiuni

- [deltatech_pos_base](../deltatech_pos_base/index.md): adus de `deltatech_pos`, baza POS Terrabit.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): transportul spre casa de marcat prin agentul Terrabit Connect (adus de `deltatech_pos`).
- [deltatech_ecr_fiscal](../deltatech_ecr_fiscal/index.md): generarea fișierelor de comenzi pentru casa de marcat (adus de `deltatech_pos`).
- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): declarația D394, completată cu bonurile POS (adus de `l10n_ro_anaf_d394_pos`).
- `pos_hr`: autentificarea cu angajați, adusă de `deltatech_pos_cashier_close`.
- `account_reports`: Odoo Enterprise, necesar registrului de casă.
