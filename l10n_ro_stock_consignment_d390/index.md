# Romania - Stocuri la dispoziția clientului în D390 (localizat la `l10n_ro_stock_consignment_d390/index.md`)

- **Nume Tehnic:** `l10n_ro_stock_consignment_d390`
- **Versiune:** `19.0.1.0.2`
- **Cale:** https://github.com/terrabit-solutions/l10n_ro_ent/tree/19.0/l10n_ro_stock_consignment_d390
- **Cale Locală:** `odoo-addons/l10n_ro_ent/l10n_ro_stock_consignment_d390`
- **Ultima Ingestie:** `2026-10-20`

#### 1. Sumar

Modulul completează automat **secțiunea III din Declarația 390** (transferul de bunuri în regimul stocurilor la dispoziția clientului, art. 270^1 din Codul fiscal) pe baza evidenței call-off din modulul de stocuri în custodie. Se instalează singur atunci când sunt prezente ambele module de bază, astfel încât contabilul nu mai întocmește manual rândurile `cos`. Rezultatul: declarația include corect expedierile și retururile de bunuri făcute în regim call-off, fără omisiuni tăcute.

#### 2. Funcționalități Cheie

- **Tip A (expediere):** câte un rând pentru fiecare client vizat al expedierilor call-off din lună (art. 325 alin. (2) Cod fiscal: luna expedierii), cu țara și codul de TVA fără prefix.
- **Tip B, motiv 1 (retur):** câte un rând pentru fiecare client cu retur de bunuri în lună.
- **Luna după data locală:** expedierile și retururile se încadrează după data locală (ora României), nu după ora UTC a validării; o validare pe 1 ale lunii după miezul nopții aparține lunii noi.
- **Lună doar cu secțiunea III:** declarația se exportă și fără operațiuni intracomunitare (obligatorie pentru luna expedierii; validatorul ANAF DUKIntegrator o acceptă).
- **Export XDP oprit:** șablonul XDP (Soft A) nu are încă secțiunea III, deci exportul se blochează cu mesaj explicit pentru lunile cu mișcări call-off; se folosește exportul **XML (Soft J)**.
- **Utilizare:** se înregistrează expedierile, preluările și retururile în modulul de stocuri în custodie, apoi se generează D390 din *Contabilitate → Declarații ANAF → Declarație 390* și se exportă XML (Soft J). Secțiunea `cos` apare înaintea operațiunilor.
- **Preluarea de către client** nu intră în secțiunea III: factura de livrare intracomunitară apare la operațiuni ca **L**, în luna exigibilității (luna facturii, cel târziu luna în care cade ziua de 15 după preluare).
- **Validări:** clientul trebuie să aibă țară și cod de TVA, altfel se afișează eroare; rândurile duplicate (același tip, țară, cod) se elimină.
- **Limitări:** înlocuirea clientului (B, motiv 2) și transferul la expirare nu sunt încă generate automat.

#### 3. Dependențe

- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md)
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md)

Modulul este `auto_install` (stadiu de dezvoltare: Beta, licență OPL-1).

#### 4. Componente Cheie

**Modele**

- `l10n_ro_anaf_d390.tax.report.handler` (extins, model abstract): `_get_d390_stocks` adaugă rândurile `cos` (tip A din `l10n.ro.call.off.line` după `date_dispatch`; tip B motiv 1 din mișcările de retur finalizate, după data locală); `_get_d390_cos_partner` determină prefixul de țară VIES și codul de TVA fără prefix; `export_to_xdp` blochează exportul XDP când există mișcări call-off în perioadă.

**Vizualizări**

- Modulul nu definește vizualizări; secțiunea `cos` apare în XML-ul D390 generat.

**Acțiuni Automate / Acțiuni Server**

- Nu are cron-uri sau acțiuni server.

#### 5. Conexiuni

- [l10n_ro_stock_consignment](../l10n_ro_stock_consignment/index.md): sursa evidenței call-off (expedieri, preluări, retururi).
- [l10n_ro_anaf_d390](../l10n_ro_anaf_d390/index.md): declarația D390 în care se inserează secțiunea III.
