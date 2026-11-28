# Romania - Corecții la exportul SAF-T D406 (localizat la `l10n_ro_saft_export_fix/index.md`)

- **Nume Tehnic:** `l10n_ro_saft_export_fix`
- **Versiune:** `20.0.1.9.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_saft_export_fix
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_saft_export_fix`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul corectează defecte ale exportului SAF-T D406 din modulul Enterprise `l10n_ro_saft`, descoperite confruntând fișierele generate de Odoo cu validatorul oficial DUK Integrator și cu nomenclatorul ANAF de coduri de taxă. Scopul este ca declarația să poată fi depusă fără respingere și ca valorile raportate să corespundă cu decontul de TVA (D300).

#### 2. Funcționalități Cheie

- **Secțiuni goale:** `SalesInvoices`, `PurchaseInvoices` și `Payments` se scriu doar când au conținut; o lună fără achiziții sau plăți nu mai face fișierul respins de validatorul ANAF.
- **Plăți fără extras bancar:** plățile înregistrate prin „Înregistrează plata” și operațiunile de casă apar în declarație, cu latura de trezorerie citită de pe contul de tranzit (5125 / 581); `PaymentMethod` 01 pentru numerar, 03 pentru transfer. O plată reconciliată cu un extras se raportează o singură dată, prin extras.
- **TVA cu deducere limitată la 50%:** taxa „21% ND 50%” se separă după repartiția ei: partea de pe contul de TVA primește codul deductibil (341104), restul păstrează codul nedeductibil (391104); la fel pe cotele 19%, 11%, 9% și 5%.
- **Taxe de 0%:** linia de bază primește codul SAF-T al taxei (de exemplu 308302 pentru achiziții scutite, 310301 pentru livrări intracomunitare), cu suma zero, iar taxa intră în `TaxTable`; taxa fără tip sau cod SAF-T rămâne pe `000 / 000000`.
- **Cod poștal gol:** tagul `PostalCode` se scrie doar când partenerul are cod poștal.
- **Conturi cu litere în cod:** fiecare grup de litere se înlocuiește cu un cod fix de 3 cifre, dintr-un tabel salvat în bază (`4111RUE5194` devine `41110015194`); `StandardAccountID` primește codul real, iar câmpul opțional **Cod SAF-T** de pe cont are prioritate.
- **Câmpuri suplimentare:** cod SAF-T, funcțiune și tip de taxă pe cont, tip și cod de taxă pe linia contabilă și persoana de contact SAF-T în setări, pentru identificatorii firmei și ai partenerilor.
- Declarația se generează ca înainte, din **Contabilitate → Raportare → Ledgers → General Ledger**, din meniul ⚙ opțiunea **SAF-T (Declarația D406)**; verificările pas cu pas sunt în [fișa consultantului](FISA_CONSULTANT.md).
- Nu sunt acoperite secțiunile `Owners` și `Stocks` din `l10n_ro_saft_stock`.

#### 3. Dependențe

- `l10n_ro_saft` (se încarcă deliberat după el, pentru că moștenește șablonul QWeb și modelul de raport)

#### 4. Componente Cheie

**Modele**

- `account.general.ledger.report.handler`: extins pentru plățile fără extras, separarea TVA la 50%, taxele de 0% și codurile conturilor.
- `account.account`: câmpurile SAF-T ale contului (cod, tip, funcțiune, tip și cod de taxă).
- `account.move.line`: tipul și codul de taxă SAF-T pe linia contabilă.
- `l10n_ro.saft.letter.code`: tabelul care asociază grupurile de litere din codul unui cont cu un cod numeric de 3 cifre.
- `res.company` / `res.config.settings`: persoana de contact SAF-T.

**Vizualizări**

- `views/account_account_views.xml`: câmpurile SAF-T pe formularul contului.
- `views/account_move_line_views.xml`: tipul și codul de taxă SAF-T pe linia contabilă.
- `views/res_config_settings_views.xml`: persoana de contact SAF-T în setări.
- `views/saft_report_templates.xml`: șabloanele QWeb ale raportului SAF-T, cu secțiunile condiționate și adresa fără `PostalCode` gol.

**Acțiuni Automate / Acțiuni Server**

- Nu are.

#### 5. Conexiuni

- [l10n_ro_saft_preview](../l10n_ro_saft_preview/index.md): previzualizarea D406 se construiește peste exportul corectat de acest modul.
- [l10n_ro_saft_fix](../l10n_ro_saft_fix/index.md): modul paralel de corecții SAF-T, încărcat deliberat înaintea lui `l10n_ro_saft`.
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): pre-validarea D406; funcționează independent.
