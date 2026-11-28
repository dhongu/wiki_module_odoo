# Romania - Stocuri la dispoziția clientului în D390 (localizat la `l10n_ro_stock_consignment_d390/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_consignment_d390`
- **Versiune:** `20.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/20.0/l10n_ro_stock_consignment_d390
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_consignment_d390`
- **Ultima Ingestie:** 2026-11-28

#### 1. Sumar

Modulul completează automat secțiunea III din declarația D390 (transferul de bunuri în regimul stocurilor la dispoziția clientului, art. 270^1 Cod fiscal) din evidența call-off a stocurilor în custodie. Se instalează singur când sunt prezente ambele module de bază, deci contabilul nu mai întocmește manual această secțiune.

#### 2. Funcționalități Cheie

- **Tip A:** câte un rând pentru fiecare client vizat al expedierilor call-off din lună (luna expedierii, art. 325 alin. (2) Cod fiscal), cu țara și codul de TVA fără prefix.
- **Tip B, motiv 1:** câte un rând pentru fiecare client cu retur de bunuri în lună.
- **Luna după ora României:** expedierile și retururile se încadrează după data locală, nu după ora UTC a validării.
- **Lună doar cu secțiunea III:** declarația se exportă și fără operațiuni intracomunitare; validatorul ANAF (DUKIntegrator) o acceptă.
- **Fără omisiuni tăcute:** exportul XDP (Soft A), care nu are secțiunea III, se oprește cu mesaj pentru o lună cu mișcări call-off; se folosește exportul XML (Soft J).
- **Flux:** se generează D390 din Contabilitate → Declarații ANAF → Declarație 390 și se exportă XML (Soft J); secțiunea `cos` apare înaintea operațiunilor.
- Preluarea de către client nu intră în secțiunea III: factura intracomunitară apare la operațiuni ca **L**, în luna exigibilității.
- Limitări: înlocuirea clientului (B, motiv 2) și transferul la expirare nu sunt generate automat.

#### 3. Dependențe

- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md)
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md)

#### 4. Componente Cheie

**Modele**

- `l10n_ro.ec.sales.report.handler`: extins (`account_ec_sales_report_handler.py`) pentru a genera secțiunea `cos`.

**Vizualizări**

- Fără vizualizări proprii (modul `auto_install`, `data` gol).

**Acțiuni Automate / Acțiuni Server**

- Niciuna.

#### 5. Conexiuni

- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md): evidența call-off a stocurilor în custodie, sursa datelor.
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): declarația D390 pe care o completează.
