# Romania - D394 pentru punctul de vânzare (localizat la `l10n_ro_anaf_d394_pos/index.md`)

- **Nume Tehnic:** `l10n_ro_anaf_d394_pos`
- **Versiune:** `19.0.1.3.3`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_anaf_d394_pos
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_anaf_d394_pos`
- **Ultima Ingestie:** `2026-11-22`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul face puntea între declarația **D394** și modulul **Point of Sale**: bonurile fiscale emise prin POS nu produc documente `out_receipt` în Odoo (comenzile nefacturate se agregă în nota contabilă a sesiunii, iar cele facturate produc deja `out_invoice`), așa că modulul reconstruiește corect contribuția POS la declarație direct din comenzile `pos.order`, evitând dubla numărare și fără a atinge jurnalul de TVA normal. Se instalează automat (`auto_install`) când sunt prezente atât `l10n_ro_anaf_d394`, cât și `point_of_sale`.

#### 2. Funcționalități Cheie

- Elimină nota de sesiune POS din colectarea pe `account.move`, scopat **doar** la colectarea D394 — jurnalul de TVA normal rămâne neatins.
- Construiește contribuția POS la op1/op2 direct din comenzile `pos.order` nefacturate, pe cote de TVA (un bon cu cote mixte contează ca un singur bon).
- Rutare: bon nefacturat anonim sau cu client fără CUI → **op2**, `tip_op2="I1"` (încasări prin aparat de marcat); bon nefacturat cu client cu CUI → **op1**, tip „L”; comandă facturată → deja în op1 prin `out_invoice`.
- `nrBF` = numărul de bonuri (comenzi distincte); `nrAMEF` = serii AMEF distincte dacă sunt configurate, altfel jurnale POS distincte (aproximare).
- Retururile (refund) se agregă cu semn negativ și se numără ca bon.
- Configurare opțională, dar recomandată, a „Seriei AMEF” pe punctul de vânzare (**Punct de vânzare → Configurare → Setări**, blocul **Declarația D394**), pentru ca `nrAMEF` să reflecte numărul real de aparate fiscale. Dacă rămâne goală și e instalat `l10n_ro_pos_fiscal_compliance`, se folosește **Serie aparat fiscal (AMEF)** de acolo, deci seria nu se introduce de două ori.
- Nu cere pași manuali la generare: în **Contabilitate → Raportare → Declarații ANAF → Declarație 394** bonurile POS intră singure în previzualizare (secțiunile op1/op2) și în export (XDP sau XML).

#### 3. Dependențe

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md)
- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d394.report.mixin` (extins prin `L10nRoTaxReportHandlerPos`): exclude notele de sesiune POS din colectarea D394 (`_query_invoices`), citește comenzile POS din perioadă (`_get_pos_orders_for_d394`), le rutează în op1/op2 (`_get_pos_d394_items`, `_collect_d394_items`) și ajustează agregatele (`_build_d394_aggregates`).
- `pos.config` (extins): câmpul `l10n_ro_amef_series` (Seria AMEF), folosit pentru numărarea `nrAMEF` pe aparat fiscal; `_l10n_ro_fiscal_device_serial` oferă și seria din `l10n_ro_pos_fiscal_compliance`, dacă e instalat.
- `res.config.settings` (extins): expune seria AMEF în setările punctului de vânzare.

**Vizualizări**

- `res_config_settings_view_form_d394_amef`: blocul „Declarația D394” cu câmpul Seria AMEF în setările POS.

**Acțiuni Automate / Acțiuni Server**

- Nu există cron-uri sau reguli server; colectarea POS se realizează sincron, în fluxul de generare a declarației D394.

#### 5. Conexiuni

- [l10n_ro_anaf_d394](../l10n_ro_anaf_d394/index.md): modulul de bază al declarației D394, ale cărui puncte de extensie (`_collect_d394_items`, `_query_invoices`, `_build_d394_aggregates`) sunt moștenite pentru a integra bonurile POS.
- [l10n_ro_anaf_base](../l10n_ro_anaf_base/index.md): infrastructura comună ANAF folosită de raportările de tip D394.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): opțional; furnizează seria aparatului fiscal (AMEF) folosită ca valoare implicită pentru `nrAMEF`.
- `point_of_sale`: sursa datelor (`pos.order`, `pos.session`, `pos.config`) pentru contribuția bonurilor fiscale la declarație.
