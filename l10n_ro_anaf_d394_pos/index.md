# Romania - D394 Point of Sale (localizat la `l10n_ro_anaf_d394_pos/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d394_pos`
- **Versiune:** `19.0.1.1.1`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d394_pos
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d394_pos`
- **Ultima Ingestie:** 2026-08-20
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face puntea între declarația **D394** și modulul **Point of Sale**: bonurile fiscale emise prin POS nu produc documente `out_receipt` în Odoo (comenzile nefacturate se agregă în nota contabilă a sesiunii, iar cele facturate produc deja `out_invoice`), așa că modulul reconstruiește corect contribuția POS la declarație direct din comenzile `pos.order`, evitând dubla numărare și fără a atinge jurnalul de TVA normal. Se instalează automat (`auto_install`) când sunt prezente atât `l10n_ro_anaf_d394`, cât și `point_of_sale`.

#### 2. Funcționalități Cheie

- Elimină nota de sesiune POS din colectarea pe `account.move`, scopat **doar** la colectarea D394 — jurnalul de TVA normal rămâne neatins.
- Construiește contribuția POS la op1/op2 direct din comenzile `pos.order` nefacturate.
- `nrBF` = numărul de bonuri (comenzi distincte); `nrAMEF` = jurnale POS distincte, sau serii AMEF distincte dacă sunt configurate.
- Retururile (refund) se agregă cu semn negativ.
- Rutare: comandă nefacturată cu CUI → op1; fără CUI → op2 (tip `L`); comandă facturată → deja în op1 prin `out_invoice`.
- Configurare opțională a „Seriei AMEF" pe fiecare punct de vânzare, pentru ca `nrAMEF` să reflecte numărul real de aparate fiscale.

#### 3. Dependențe

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d394.report.mixin` (extins prin `L10nRoTaxReportHandlerPos`): dedup notele de sesiune POS din colectarea D394 și injectează contribuția POS (op1/op2) în datele XML ale declarației.
- `pos.config` (extins): adaugă câmpul `l10n_ro_amef_series` (Seria AMEF) folosit pentru numărarea `nrAMEF` pe aparat fiscal.

**Vizualizări**

- `pos_config_view_form_d394_amef`: adaugă grupul „D394 Declaration" cu câmpul Seria AMEF în formularul punctului de vânzare (`pos.config`).

**Acțiuni Automate / Acțiuni Server**

*Nu au fost identificate acțiuni automate (`ir.cron`) sau reguli server; colectarea POS se realizează sincron, în fluxul de generare a declarației D394.*

#### 5. Conexiuni

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): modulul de bază al declarației D394, ale cărui puncte de extensie (`_collect_d394_items`, `_query_invoices`, `_prepare_d394_xml_data`) sunt moștenite pentru a integra bonurile POS.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF folosită de raportările de tip D394.
- `point_of_sale`: sursa datelor (`pos.order`, `pos.session`, `pos.config`) pentru contribuția bonurilor fiscale la declarație.
