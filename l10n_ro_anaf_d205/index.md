# Romania - ANAF Declarația 205 (WHT PF Nerezidente) (localizat la `l10n_ro_anaf_d205/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d205`
- **Versiune:** `19.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d205
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d205`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modul pentru întocmirea și depunerea Declarației 205 — declarația informativă privind impozitul reținut la sursă pe veniturile plătite persoanelor fizice nerezidente. Este adresat contabililor care gestionează plăți către beneficiari nerezidenți persoane fizice (dividende, dobânzi, redevențe, alte venituri supuse reținerii la sursă) și oferă un flux complet, de la previzualizarea mișcărilor contabile până la exportul fișierului XML gata de depus în Soft J ANAF.

#### 2. Funcționalități Cheie

- Raport de previzualizare live (motor `account.report`) cu mișcările WHT din conturile 446x, grupate pe beneficiar și document contabil
- Generare automată a ciornei D205 dintr-un singur clic, cu import din 446x pentru parteneri PF cu flag WHT activ
- Declarație persistentă (`l10n.ro.anaf.d205`) cu 10 tipuri de venit conform XSD (dividende, dobânzi, redevențe, câștiguri din titluri etc.) și 3 tipuri de plată
- Validare XML față de schema XSD ANAF `d205_2025_v3.xsd` (namespace v2) înainte de export
- Export fișier XML gata de depus în Soft J ANAF
- Workflow ciornă → confirmată, cu verificări obligatorii (NIF beneficiar, linii)
- Integrare în lista de verificări `account.return` pentru fluxul de închidere anuală: verificare automată a prezenței declarației și a completitudinii NIF-urilor
- Suport declarație rectificativă și declarație succesor

#### 3. Dependențe

- `account`
- `l10n_ro`
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md)
- [l10n_ro_partner_screening](../l10n_ro_partner_screening/index.md)
- `l10n_ro_reports`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.anaf.d205`: declarația persistentă D205 (an fiscal, stare ciornă/confirmată, flag rectificativă/succesor, linii beneficiari, totaluri bază/impozit); moștenește `l10n_ro_anaf.report.handler.mixin` și expune generarea/exportul XML.
- `l10n.ro.anaf.d205.line`: linia unui beneficiar nerezident (CIF/CNP România, TIN străin, tip venit, tip plată, bază impozabilă, impozit reținut).
- `l10n_ro_anaf_d205.report.handler` (`AbstractModel`): handler pentru raportul de previzualizare `account.report` — interoghează SQL direct conturile 446x pentru parteneri PF cu `l10n_ro_wht_applicable = True`, oferă butoanele „Generate D205 Draft” și export XML, și populează date demo (`_load_demo_wht`).
- `account.return` (extindere): adaugă termenul legal de depunere (ultima zi a lunii februarie a anului următor) și două verificări noi în fluxul de închidere anuală — generarea ciornei D205 din 446x și beneficiari fără NIF România.

**Vizualizări**

- `views/l10n_ro_anaf_d205_view.xml`: formularul și lista declarației D205, cu acțiunile de import din contabilitate, confirmare/resetare și export XML.

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`); importul, generarea ciornei și exportul XML se declanșează manual, din raportul de previzualizare sau din formularul declarației.*

#### 5. Conexiuni

- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): furnizează mixin-ul comun de handler ANAF (`l10n_ro_anaf.report.handler.mixin`), registrul de profile de declarații și butoanele de export.
- [l10n_ro_anaf_d207](../l10n_ro_anaf_d207/index.md): declarație informativă ANAF înrudită (aceeași familie de declarații WHT/venituri către nerezidenți).
- [l10n_ro_anaf_d107](../l10n_ro_anaf_d107/index.md): declarație informativă ANAF înrudită (același ecosistem de raportare fiscală RO).
- `account.return` (din `account`): fluxul de închidere anuală în care D205 își înregistrează verificările proprii (ciornă generată, NIF-uri complete).
