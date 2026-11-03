# Romania - Timbru verde (DEEE)

- **Nume Tehnic:** `l10n_ro_green_stamp`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_green_stamp
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_green_stamp`
- **Ultima Ingestie:** `2026-11-03`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Modulul adaugă timbrul verde pe o linie separată în comenzile și facturile de vânzare și de achiziție, pentru echipamentele electrice și electronice (EEE) vândute sau cumpărate în România. Producătorii și distribuitorii de EEE trebuie să arate separat cumpărătorului costurile de colectare, tratare și eliminare a deșeurilor (art. 34 din OUG nr. 5/2015). Suma se setează o singură dată pe produs, iar linia de timbru se generează automat, în același mod ca garanția SGR.

#### 2. Funcționalități Cheie

- **Timbru pe produs:** suma pe unitate, în moneda companiei, se setează pe produs (fila Vânzări, grupul „Timbru verde (DEEE)”), fără TVA. Nu se completează pentru bateriile portabile (art. 12 alin. (4) din HG nr. 1132/2008).
- **Linie automată:** pe comanda de vânzare, în coșul magazinului online și pe comanda de achiziție, fiecare produs cu timbru primește linia „Timbru verde”, cu cantitatea liniei principale. Linia urmează cantitatea și dispare odată cu linia principală.
- **TVA corect:** linia ia taxele liniei principale, cu poziția fiscală aplicată; timbrul intră în baza TVA cu cota echipamentului (art. 286 Cod fiscal) și pleacă în e-Factura ca linie obișnuită, în aceeași categorie de TVA.
- **Fără timbru la extern:** partenerii din altă țară decât compania nu primesc linia.
- **Cost de achiziție:** cu `stock_landed_costs` instalat, produsul „Timbru verde” este cost suplimentar; din factura furnizorului (buton **Creați costuri adiționale**) se repartizează pe recepție și intră în costul mărfii (cont 371).
- **Raport:** **Contabilitate (sau Facturare) → Raportare → Timbru verde**: liniile de timbru din facturile postate, cu produsul generator, în listă și pivot (pe produs, partener, lună), cu filtre Vânzări / Achiziții (implicit Vânzări); stornările apar cu minus.
- **Configurare automată:** produsul „Timbru verde” (cod `TIMBRU-VERDE`, politică de facturare „Cantități comandate”) se creează la instalare pentru companiile din România și la încărcarea planului de conturi RO pe o companie nouă; contul de venit se poate rafina (ex. 707.TV).
- **Limitări:** factura creată direct, fără comandă, nu primește linia automat; POS nu folosește suma de pe produs; fără `stock_landed_costs`, timbrul din factura furnizorului merge pe contul de cheltuieli implicit; o linie principală are o singură linie suplimentară, timbrul având întâietate.

Fluxul pas-cu-pas, cu capturi, este în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md)
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md)
- `account`
- `l10n_ro`

#### 4. Componente Cheie

**Modele**

- `product.template` (extins): câmpul `l10n_ro_green_stamp_amount`, suma timbrului pe unitate.
- `sale.order.line` / `purchase.order.line` (extinse): determină produsul și prețul liniei suplimentare de timbru verde și când se aplică (partener din România).
- `account.move.line` (extins): câmpuri calculate care marchează linia de timbru, produsul principal și suma, folosite de raport.
- `res.company` / `res.config.settings` (extinse): produsul „Timbru verde” al companiei.
- `account.chart.template` (extins): creează produsul la încărcarea planului de conturi.

**Vizualizări**

- `product_template_form_view_green_stamp`: grupul „Timbru verde (DEEE)” în fila Vânzări a produsului.
- `res_config_settings_view_form_green_stamp`: blocul „Timbru verde (DEEE)” în setările de contabilitate.
- `view_green_stamp_line_list` / `view_green_stamp_line_pivot` / `view_green_stamp_line_search`: raportul pe linie (listă, pivot, filtre).
- `action_green_stamp_line` și `menu_green_stamp_line`: acțiunea și meniul Raportare → Timbru verde.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server; `pre_init_hook` și `post_init_hook` pregătesc și creează produsul „Timbru verde” la instalare.

#### 5. Conexiuni

- [deltatech_sale_add_extra_line](../deltatech_sale_add_extra_line/index.md): mecanismul de linie suplimentară pe vânzare, pe care îl folosește timbrul.
- [deltatech_purchase_add_extra_line](../deltatech_purchase_add_extra_line/index.md): același mecanism pe achiziție.
- `stock_landed_costs`: opțional, pentru includerea timbrului în costul mărfii.
