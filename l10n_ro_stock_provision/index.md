# Romania - Ajustări pentru deprecierea stocurilor (39x) (localizat la `l10n_ro_stock_provision/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_provision`
- **Versiune:** `20.0.1.0.7`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_provision
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_provision`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul identifică automat stocurile fără rulaj (slow-moving) și generează notele contabile de ajustare pentru depreciere, conform OMFP 1802/2014 pct. 143–148. Este destinat contabililor care constituie ajustări pe conturile din clasa `39x` la sfârșitul perioadei de raportare: sistemul propune liniile, contabilul le validează, iar la confirmare se generează nota contabilă.

#### 2. Funcționalități Cheie

- **Scanare automată** a stocurilor interne cu stoc pozitiv și fără intrări peste pragul configurat (implicit 180 de zile).
- **Propunere de ajustare delta** față de soldul existent pe contul `39x`: constituire, majorare, diminuare sau reluare completă.
- **Flux de aprobare** Analiză → Propuneri confirmate → Note generate; contabilul bifează sau debifează liniile înainte de postare. Analizele se țin în Contabilitate → Închidere → Provizioane Stocuri (39x).
- **Note contabile:** `Dr 6814 = Cr 39x` la constituire/majorare și `Dr 39x = Cr 7814` la diminuare/reluare.
- **Cont 39x per categorie de produs** (391–398); un produs fără cont 39x pe categorie nu apare în analiză.
- **Procent de depreciere** configurabil global și suprascris per categorie.
- **Cron lunar opțional** care creează analize în stare draft, pentru verificare manuală.
- **Surse de date:** integrare opțională cu `deltatech_stock_valuation` pentru date lunare agregate; altfel `stock.quant`, cu data ultimei intrări din `l10n_ro_last_in_date` (dacă `l10n_ro_stock_aged_report` e instalat) sau din `in_date`.
- Setările (conturile 6814/7814, zilele fără mișcare) se găsesc în Contabilitate → Configurare → Setări, secțiunea „Provizioane Stocuri Slow-Moving". Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- `stock`
- `account`

#### 4. Componente Cheie

**Modele**

- `l10n.ro.stock.provision`: analiza de provizion (cu `mail.thread` și activități), cu stările și nota generată.
- `l10n.ro.stock.provision.line`: linia de propunere per produs (stoc, sold 39x, ajustare delta).
- `product.category`, `res.company`, `res.config.settings` (extinse): cont 39x și procent per categorie, conturi 6814/7814 și zile fără mișcare.

**Vizualizări**

- `view_l10n_ro_stock_provision_form` / `view_l10n_ro_stock_provision_list`: analiza de provizioane și propunerile.
- `view_product_category_form_provision`: fila „Provizioane Stocuri RO (39x)" pe categorie.
- `res_config_settings_view_form_stock_provision`: setările modulului.

**Acțiuni Automate / Acțiuni Server**

- `cron_stock_provision_monthly`: creează lunar analize draft pe fiecare companie; inactiv implicit.

#### 5. Conexiuni

- [l10n_ro_stock_aged_report](../l10n_ro_stock_aged_report/index.md): sursă opțională pentru data ultimei intrări (`l10n_ro_last_in_date`).
- [deltatech_stock_valuation](../deltatech_stock_valuation/index.md): date lunare agregate mai precise, dacă e instalat.
- [l10n_ro_stock_k_coefficient](../l10n_ro_stock_k_coefficient/index.md): celălalt calcul contabil de închidere a lunii pe stocuri.
- [l10n_ro_stock_cmp_periodic](../l10n_ro_stock_cmp_periodic/index.md): corecția lunară CMP, tot la închiderea lunii.
