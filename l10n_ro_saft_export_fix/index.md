# Romania - Corecții la exportul SAF-T D406 (localizat la `l10n_ro_saft_export_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_export_fix`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_saft_export_fix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_export_fix`
- **Ultima Ingestie:** `2026-09-29`

#### 1. Sumar

Modulul corectează două defecte ale exportului SAF-T D406 din modulul Enterprise `l10n_ro_saft`, descoperite prin confruntarea fișierelor generate de Odoo cu validatorul oficial `D406Validator` din DUK Integrator. Primul defect face declarația nedepunabilă (secțiuni goale respinse de ANAF), al doilea lasă în afara declarației plățile care nu provin dintr-un extras bancar. Corecțiile se aplică fără a modifica codul Enterprise, iar declarațiile care validează deja pe baza extraselor rămân identice. Defectele sunt raportate și către Odoo; modulul acoperă perioada până la rezolvarea în amonte.

#### 2. Funcționalități Cheie

- **Eliminarea secțiunilor goale:** `SalesInvoices`, `PurchaseInvoices` și `Payments` sunt scrise doar dacă au cel puțin un document. O lună fără achiziții nu mai duce la respingerea întregului fișier (eroarea „elementul 'Payment' ar fi trebuit sa apara de minimum 1 ori").
- **Raportarea plăților fără extras:** plățile înregistrate prin „Înregistrează plata" și operațiunile de casă (jurnalele de casă nu mai lucrează cu extrase din 17.0) apar acum în secțiunea `Payments`.
- **`PaymentMethod`:** `01` pentru numerar (jurnal de casă), `03` pentru transfer.
- **Latura de trezorerie corectă:** pentru plățile fără extras, linia de trezorerie este citită de pe contul de tranzit (5125 / 581), astfel încât fiecare `Payment` are cel puțin un `PaymentLine`.
- **Fără dublare:** o plată reconciliată cu un extras se raportează o singură dată, prin nota extrasului (care poartă referința și data bancară).
- **Fără meniuri sau câmpuri noi:** declarația se generează ca înainte, din Contabilitate → Raportare → Cartea Mare, butonul „SAF-T (Declarația D406)".
- **Verificare:** pentru o lună fără plăți prin extras, secțiunea `Payments` lipsește cu totul, iar DUK Integrator întoarce „Validare fara erori".
- **Flux recomandat:** se rulează întâi `l10n_ro_saft_validator` (semnalează secțiunile care ar ieși goale și plățile nelegate de un extras), apoi se generează declarația și se validează cu DUK Integrator înainte de depunere.

#### 3. Dependențe

- `l10n_ro_saft` (modul Enterprise; fără pagină wiki). Spre deosebire de [l10n_ro_saft_fix](../l10n_ro_saft_fix/index.md), care nu depinde de el ca să se încarce înaintea lui, aici modulul trebuie încărcat DUPĂ, ca să poată moșteni șablonul și modelul de raport.

#### 4. Componente Cheie

**Modele**

- `account.general.ledger.report.handler` (abstract, extins): suprascrie `_l10n_ro_saft_fill_payment_values` (construiește `payment_vals` și include și notele plăților fără extras, cu liniile de trezorerie corecte) și adaugă `_l10n_ro_saft_get_payment_move_ids`, care clasifică notele candidate (jurnale bancă/casă) printr-o singură căutare pe `account.payment` după `move_id`, nu prin `origin_payment_id`, gol pentru plățile create din wizardul „Înregistrează plata".

**Vizualizări**

- `saft_template` (moștenește `l10n_ro_saft.saft_template`): mută condiția `t-if` pe tag-urile `SalesInvoices`, `PurchaseInvoices` și `Payments`, legată de numărul de documente.

**Acțiuni Automate / Acțiuni Server**

- Nu există.

#### 5. Conexiuni

- [l10n_ro_saft_fix](../l10n_ro_saft_fix/index.md): modul distinct, care rezolvă o problemă de instalare a `l10n_ro_saft` (construit fără `depends` pe acesta); nu se suprapune cu corecțiile de export de aici.
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): validare înainte de export; testele sale acoperă avertizarea pentru secțiuni goale și pentru plăți fără linie de extras (verificat în teste, fără dependență în manifest).
