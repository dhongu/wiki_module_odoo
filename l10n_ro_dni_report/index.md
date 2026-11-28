# Romania - Raport livrări nefacturate (418)

- **Nume Tehnic:** `l10n_ro_dni_report`
- **Versiune:** `20.0.1.0.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_dni_report
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_dni_report`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Raportul din spatele soldului contului 418 („Clienți - facturi de întocmit”): livrările pe aviz care încă își așteaptă factura, pe client și document, cu vechime și sumă rămasă. La închiderea lunii arată nu doar cât mai e de facturat, ci și pentru ce. Este perechea raportului de recepții nefacturate (408).

#### 2. Funcționalități Cheie

- Grupare pe client, cu drill-down până la documentul individual; pentru fiecare rând: valoare livrată, valoare facturată, rest de facturat și vechimea celei mai vechi înregistrări nefacturate.
- Sold cumulat la sfârșitul perioadei: un aviz de acum trei luni, încă nefacturat, apare în raportul lunii curente; clienții fără sold nu apar.
- La livrările pe aviz din `l10n_ro_stock_account`, coloana „Document” arată avizul (transferul), nu nota contabilă.
- Contul 418 se ia din configurarea companiei (contul de la avizul de livrare); fără ea se folosesc conturile care încep cu 418.
- Filtre de perioadă, client și companie; export PDF / XLSX din framework-ul de rapoarte.
- Meniu: Contabilitate → Raportare → Livrări nefacturate (418).
- Detalii de utilizare în [fișa consultant](FISA_CONSULTANT.md).

#### 3. Dependențe

- `account_reports` (Enterprise)
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.dni.report.handler` (`account.report.custom.handler`): handler-ul raportului, care calculează soldurile pe 418.

**Vizualizări**

- `dni_report` (`account.report`) cu coloanele Document, Livrat, Facturat, Sold și Vechime, definit în `data/dni_report.xml`.

**Acțiuni Automate / Acțiuni Server**

- `action_dni_report` (`ir.actions.client`): deschide raportul din meniu.

#### 5. Conexiuni

- `l10n_ro_stock_account`: livrările pe aviz, afișate cu transferul drept document.
