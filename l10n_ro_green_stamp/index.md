# Romania - Timbru verde (DEEE)

- **Nume Tehnic:** `l10n_ro_green_stamp`
- **Versiune:** `20.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_green_stamp
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_green_stamp`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Timbrul verde pe linie separată în comenzi și facturi, pentru echipamentele electrice și electronice (EEE) vândute sau cumpărate în România. Producătorii și distribuitorii de EEE trebuie să arate separat cumpărătorului costurile de colectare, tratare și eliminare a deșeurilor (art. 34 din OUG nr. 5/2015); modulul le adaugă ca linie proprie, la fel ca garanția SGR.

#### 2. Funcționalități Cheie

- **Timbru pe produs**: suma pe unitate, în moneda companiei, se setează pe produs (fila Vânzări, grupul „Timbru verde (DEEE)”).
- **Linie automată** „Timbru verde” pe comanda de vânzare, în coșul magazinului online și pe comanda de achiziție, cu cantitatea liniei principale; urmează cantitatea și dispare odată cu linia principală.
- **TVA corect**: linia ia taxele liniei principale, cu poziția fiscală aplicată (art. 286 Cod fiscal), și pleacă în e-Factura ca linie obișnuită, în aceeași categorie de TVA.
- **Fără timbru la extern**: partenerii din altă țară decât compania nu primesc linia.
- **Cost de achiziție**: cu `stock_landed_costs` instalat, produsul „Timbru verde” este cost suplimentar, repartizat pe recepție din factura furnizorului.
- **Raport** în **Contabilitate → Raportare → Timbru verde**: liniile de timbru din facturile postate, în listă și pivot.
- **Configurare automată**: produsul „Timbru verde” se creează la instalare pentru companiile din România și la încărcarea planului de conturi RO pe o companie nouă. Fluxul pas cu pas este în fișa consultantului.

#### 3. Dependențe

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md)
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md)
- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `product.template`: suma timbrului verde pe produs.
- `sale.order.line`, `purchase.order.line`: linia automată de timbru.
- `account.move.line`: baza raportului pe liniile de timbru.
- `account.chart.template`, `res.company`, `res.config.settings`: produsul și setările de timbru verde.

**Vizualizări**

- `product_template_form_view_green_stamp`: câmpul pe produs.
- `res_config_settings_view_form_green_stamp`: setările.
- `view_green_stamp_line_list` / `_pivot` / `_search`: raportul.

**Acțiuni Automate / Acțiuni Server**

- `pre_init_hook` / `post_init_hook`: pregătesc produsul „Timbru verde” la instalare.

#### 5. Conexiuni

- [l10n_ro_green_tax_analytic](../l10n_ro_green_tax_analytic/index.md): alternativă (taxa verde în analitic, fără linie separată); cele două module se exclud reciproc.
