# Romania - Audit corelare declarații fiscale (localizat la `l10n_ro_fiscal_audit/index.md`)

- **Nume Tehnic:** `l10n_ro_fiscal_audit`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_fiscal_audit
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_fiscal_audit`
- **Ultima Ingestie:** `2026-07-02`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul oferă un raport de audit preventiv care corelează automat, pentru o perioadă dată, totalurile dintre declarațiile fiscale românești și sursele de date din contabilitate, semnalând neconcordanțele înainte de depunere sau înainte de un control ANAF. Practic, oferă un „semafor" de consistență fiscală pe mai multe căi de calcul independente (TVA, SAF-T, e-Factura), astfel încât echipa financiară să corecteze eventualele diferențe din timp, fără să aștepte o eroare la depunere sau o notificare de la ANAF.

#### 2. Funcționalități Cheie

- Corelează TVA colectată (rd. 17) și deductibilă (rd. 27) din D300 cu totalurile din jurnalele de TVA (D394), refolosind reconcilierea FR-49 din `l10n_ro_anaf_d300`.
- Pre-validează datele pentru SAF-T (D406): parteneri fără CUI, conturi nemapate, taxe fără tip SAF-T, refolosind `l10n_ro_saft_validator`.
- Detectează facturi furnizor e-Factura recepționate în dublu exemplar (aceeași amprentă: CUI + serie/nr + dată + sumă), refolosind `l10n_ro_efactura_dedup`.
- Prezintă neconcordanțele grupate pe arii, cu valoare așteptată, valoare găsită, diferență și drill-down către documentul vizat, pe framework-ul standard `account.report` (export PDF/XLSX inclus).
- Constatările sunt avertismente de verificat (necesită confirmare umană), nu verdicte automate; când datele sunt consistente, lista de neconcordanțe este goală.
- Fiecare verificare degradează grațios (afișează „indisponibil", nu eroare) dacă modulul-sursă corespunzător nu este instalat, fără a reimplementa logica declarațiilor existente.

#### 3. Dependențe

- `account_reports`
- [l10n_ro](../l10n_ro/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro_fiscal_audit.report.handler` (`L10nRoFiscalAuditReportHandler`, `_inherit = account.report.custom.handler`): handler-ul raportului de audit; construiește liniile de neconcordanțe pe cele trei arii (TVA↔D394, SAF-T, e-Factura duplicate) și expune gate-ul `_l10n_ro_fa_has_findings` folosit înainte de depunere.

**Vizualizări**

- Raportul `l10n_ro_fiscal_audit_report` (model `account.report`): „Audit corelare declarații (RO)", cu coloanele Așteptat / Găsit / Diferență, expus prin acțiunea client `action_l10n_ro_fiscal_audit_report` în meniul rapoartelor legale de contabilitate (`account.account_reports_legal_statements_menu`).

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite `ir.cron`, `base.automation` sau `ir.actions.server` — raportul rulează la cerere, din meniul de rapoarte contabile.

#### 5. Conexiuni

- [l10n_ro_anaf_d300](../l10n_ro_anaf_d300/index.md): sursa reconcilierii TVA colectată/deductibilă (D300) cu jurnalele de TVA, reutilizată direct de handler.
- [l10n_ro_saft_validator](../l10n_ro_saft_validator/index.md): sursa pre-validărilor SAF-T (parteneri fără CUI, conturi nemapate, taxe fără tip SAF-T).
- [l10n_ro_efactura_dedup](../l10n_ro_efactura_dedup/index.md): sursa detecției de facturi furnizor e-Factura duplicate.
