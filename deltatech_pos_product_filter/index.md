# POS Order Product Filter

- **Nume Tehnic:** `deltatech_pos_product_filter`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/dhongu/deltatech/tree/19.0/deltatech_pos_product_filter
- **Cale Locală:** `odoo-addons/deltatech/deltatech_pos_product_filter`
- **Ultima Ingestie:** `2026-11-13`

#### 1. Sumar

Personalul din magazin are adesea nevoie să găsească comenzile din Punctul de Vânzare care conțin un anumit articol. Modulul adaugă o opțiune *Product* în căutarea comenzilor POS, astfel încât o comandă poate fi regăsită după ceea ce s-a vândut, fără a parcurge manual liniile fiecărei comenzi.

#### 2. Funcționalități Cheie

- **Opțiunea de căutare *Product*:** la scrierea în caseta de căutare a comenzilor POS apare o opțiune nouă *Product*, plasată imediat după cea pentru partener.
- **Căutare pe liniile comenzii:** opțiunea listează comenzile care au cel puțin o linie al cărei produs se potrivește cu textul introdus; potrivirea este parțială și nu ține cont de majuscule.
- **Doar vizualizarea de căutare:** modulul nu schimbă nimic în afară de această vizualizare — nu are cod Python, câmpuri noi, meniuri sau grupuri de acces. Nu adaugă coloană de produs în listă sau în rapoarte și nu are setări.

#### 3. Dependențe

- `point_of_sale`

#### 4. Componente Cheie

**Modele**

- Modulul nu definește și nu extinde modele Python; adaugă doar un filtru de căutare pe modelul existent `pos.order`.

**Vizualizări**

- `view_pos_order_filter`: extinde vizualizarea de căutare standard a comenzilor POS (`point_of_sale.view_pos_order_filter`) cu câmpul *Product* (`lines`), după `partner_id`, cu domeniul `[('lines.product_id', 'ilike', self)]`.

**Acțiuni Automate / Acțiuni Server**

- Nu sunt definite sarcini `ir.cron`, reguli `base.automation` sau acțiuni server.

#### 5. Conexiuni

Modul independent, parte din ecosistemul Terrabit pentru POS, fără suprapuneri funcționale cu celelalte module:

- [deltatech_pos](../deltatech_pos/index.md) și [deltatech_pos_base](../deltatech_pos_base/index.md): tipărirea bonurilor fiscale și gestiunea numerarului pe casa de marcat certificată.
- [deltatech_ecr_connect](../deltatech_ecr_connect/index.md): model comun al documentelor fiscale, convertor de format pentru casa de marcat și trimiterea prin Terrabit Connect.
- [deltatech_pos_stock](../deltatech_pos_stock/index.md): afișează stocul disponibil direct în interfața POS.
- [deltatech_pos_price_sync](../deltatech_pos_price_sync/index.md): propagă modificările de preț în sesiunile POS deja deschise.
- [deltatech_pos_fix](../deltatech_pos_fix/index.md): corectează calculul totalului POS pentru maparea poziției fiscale cu taxe incluse.
- [l10n_ro_pos_fiscal_compliance](../l10n_ro_pos_fiscal_compliance/index.md): urmărirea bonurilor fiscale AMEF, reconcilierea raportului Z și blocarea sesiunii.
- [l10n_ro_anaf_d394_pos](../l10n_ro_anaf_d394_pos/index.md): raportează bonurile fiscale POS în declarația D394 (op. 2) către ANAF.
- [l10n_ro_pos_returns](../l10n_ro_pos_returns/index.md): factură de retur și linie de registru de casă dedicate pentru fiecare retur POS.
