# RMA - Marketplace Returns (localizat la `deltatech_rma_marketplace/index.md`)

- **Nume Tehnic:** `deltatech_rma_marketplace`
- **Versiune:** `19.0.1.0.0`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/19.0/deltatech_rma_marketplace
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_rma_marketplace`
- **Ultima Ingestie:** 2026-09-24
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un retur cerut pe eMAG sau pe Shopify se aprobă acolo și ajunge la noi ca un colet. Puntea duce coletul acela pe același flux de depozit ca orice retur din [deltatech_rma](../deltatech_rma/index.md) — recepție prin scanare, verificare, transfer de retur, notă de credit —, fără ca echipa să retasteze cererea, și pune banii dați înapoi de marketplace lângă nota de credit. Cererea noastră se naște la recepție, nu la aprobarea din marketplace, iar nimic nu se scrie înapoi în marketplace. Se instalează automat când [deltatech_rma](../deltatech_rma/index.md) și [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md) sunt prezente.

#### 2. Funcționalități Cheie

- O comandă dintr-un marketplace care își importă retururile (conector cu `<provider>_import` pe `marketplace.return.request`, import neoprit pe backend) nu mai e oferită în formularul de retur din portal; pagina comenzii îi spune clientului să ceară returul din contul lui de marketplace. Un backend fără import de retururi (WooCommerce, PrestaShop, Magento…) rămâne pe portalul nostru.
- O cerere deschisă de mână pe o asemenea comandă primește un avertisment, cu retururile importate pentru comandă și, la *Fulfilled by eMAG*, faptul că marfa merge la depozitul eMAG.
- **Recepția prin scanare** găsește coletul unui retur din marketplace: un cod care nu se potrivește cu nicio cerere de-a noastră se caută în retururile importate — numărul returului, numărul comenzii din marketplace sau al comenzii Odoo — și cererea se deschide atunci, din retur, direct în *Primit*: linii pe liniile comenzii, la prețul plătit după discount, motive mapate, rezolvare din tipul returului (rambursare → *Returnăm banii*, schimb → *Înlocuire*).
- Nu se deschide cerere pentru retururi anulate sau refuzate în marketplace și nici pentru *Fulfilled by eMAG*; un retur scanat din nou, după alt cod, găsește aceeași cerere.
- Buton **Deschide cererea de retur** pe returul importat, pentru un colet neidentificat la scanare; după deschidere, legătura *Cerere de retur* și coloana cererii în lista retururilor.
- **Retururi → Configurare → Motive din marketplace**: codul motivului din marketplace (eMAG: id numeric pe țară; Shopify: numele) mapat pe motivul nostru, pe fiecare backend; nemapat → *Alt motiv (de clarificat)*.
- Transferul de retur apare în *Transferuri* pe returul din marketplace; o schimbare ulterioară de stare în marketplace e scrisă în istoricul cererii, nu impusă.
- *Rambursat de marketplace* pe cerere; la crearea notei de credit, un mesaj pune suma rambursată lângă totalul notei și semnalează o diferență. Rambursarea din marketplace nu devine notă de credit. **Atenție:** registrul `marketplace.refund` există, dar în `19.0` niciun conector nu îl populează încă (nici eMAG, nici Shopify), deci *Rambursat de marketplace* apare abia când importul rambursărilor va fi implementat.

#### 3. Dependențe

- [deltatech_rma](../deltatech_rma/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.rma.marketplace.reason` (nou): corespondența backend + cod de motiv din marketplace → motivul nostru de retur, cu `_reason_for`.
- `marketplace.return.request` (extins): `deltatech_rma_id`, `_rma_open` (creează sau întoarce cererea), `_rma_prepare_values`, `_rma_fulfilled_by_marketplace` (citește `emag_fulfilment_type` dacă există) și `write`, care scrie pe cerere schimbarea de stare.
- `deltatech.rma` (extins): `marketplace_return_id`, rambursările (`marketplace_refund_ids`, `marketplace_refunded`), `submitted_via = marketplace`, transferul de retur adăugat pe returul din marketplace și mesajul de la nota de credit; avertismentul de canal extern ascuns pe cererile născute din retur.
- `sale.order` (extins): `_rma_marketplace_backend`, `_rma_external_return_channel` și `_rma_external_return_warning` — punctele de extindere din `deltatech_rma` 19.0.1.4.0.
- `deltatech.rma.checkin` (extins, în `wizard/`): `_find_rma` caută și în retururile importate.

**Vizualizări**

- `view_deltatech_rma_marketplace_reason_list` + meniul *Motive din marketplace*.
- `view_deltatech_rma_form_marketplace`: legătura cu returul și suma rambursată pe cerere.
- `view_marketplace_return_request_form_rma` / `_tree_rma`: butonul și legătura cu cererea pe returul importat.

Fluxul operațional pas-cu-pas, cu capturi, e în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): importul retururilor eMAG și câmpul *Fulfilled by eMAG*.
- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): importul retururilor Shopify.
- [deltatech_rma_helpdesk](../deltatech_rma_helpdesk/index.md), [deltatech_rma_withdrawal](../deltatech_rma_withdrawal/index.md), [deltatech_rma_lot](../deltatech_rma_lot/index.md): celelalte punți ale `deltatech_rma`.
