# RMA - Marketplace Returns (localizat la `deltatech_rma_marketplace/index.md`)

- **Nume Tehnic:** `deltatech_rma_marketplace`
- **Versiune:** `20.0.1.0.3`
- **Cale:** https://github.com/terrabit-solutions/bitshop_marketplace/tree/20.0/deltatech_rma_marketplace
- **Cale Locală:** `odoo-addons/bitshop_marketplace/deltatech_rma_marketplace`
- **Ultima Ingestie:** `2026-11-28`
- **Fișă Consultant:** [FISA_CONSULTANT.md](FISA_CONSULTANT.md)

#### 1. Sumar

Un retur cerut pe eMAG sau pe Shopify se aprobă acolo și ajunge la noi ca un colet. Puntea duce coletul pe același flux de depozit ca orice retur din [deltatech_rma](../deltatech_rma/index.md) — recepție prin scanare, verificare, transfer de retur, notă de credit —, fără ca echipa să retasteze cererea, și pune banii dați înapoi de marketplace lângă nota de credit. Cererea noastră se naște la recepția coletului, nu la aprobarea din marketplace, iar nimic nu se scrie înapoi în marketplace.

#### 2. Funcționalități Cheie

- O comandă dintr-un marketplace care își importă retururile nu mai e oferită în formularul de retur din portal; pagina comenzii îi spune clientului să ceară returul din contul lui de marketplace.
- O cerere deschisă manual pe o asemenea comandă primește un avertisment cu retururile importate și, la Fulfilled by eMAG, faptul că marfa merge la depozitul eMAG.
- **Recepția prin scanare** găsește coletul unui retur din marketplace: un cod necunoscut se caută în retururile importate (numărul returului, al comenzii din marketplace sau al comenzii Odoo), iar cererea se deschide atunci, din retur, direct în starea „Primit”. Retururile anulate sau refuzate nu primesc cerere.
- Buton **Deschide cererea de retur** pe returul importat, pentru un colet neidentificat la scanare.
- **Retururi → Configurare → Motive din marketplace**: codul motivului din marketplace mapat pe motivul nostru, pe fiecare backend; un motiv nemapat devine „Alt motiv (de clarificat)”.
- Transferul de retur apare în *Transferuri* pe returul din marketplace; o schimbare ulterioară de stare în marketplace se scrie în istoricul cererii, nu se impune.
- Suma rambursată de marketplace apare pe cerere și se pune lângă totalul notei de credit la creare, cu semnalarea diferenței; rambursarea nu devine automat notă de credit.
- Fluxul operațional, cu capturi, în [FISA_CONSULTANT.md](FISA_CONSULTANT.md).

#### 3. Dependențe

- [deltatech_rma](../deltatech_rma/index.md)
- [deltatech_marketplace_sale](../deltatech_marketplace_sale/index.md)

#### 4. Componente Cheie

**Modele**

- `deltatech.rma.marketplace.reason` (nou): corespondența backend + cod de motiv din marketplace → motivul nostru de retur.
- `marketplace.return.request` (extins): legătura cu cererea RMA, deschiderea cererii din retur și scrierea schimbărilor de stare.
- `deltatech.rma` (extins): returul din marketplace, rambursările și mesajul de la nota de credit.
- `sale.order` (extins): punctele de extindere pentru canalul extern de retur și avertisment.
- `deltatech.rma.checkin` (extins, în `wizard/`): căutarea coletului și în retururile importate.

**Vizualizări**

- `view_deltatech_rma_marketplace_reason_list`: motivele din marketplace.
- `view_deltatech_rma_form_marketplace`: legătura cu returul și suma rambursată pe cerere.
- `view_marketplace_return_request_form_rma` / `_tree_rma`: butonul și legătura cu cererea pe returul importat.

**Acțiuni Automate / Acțiuni Server**

Nu are.

#### 5. Conexiuni

- [deltatech_marketplace_emag](../deltatech_marketplace_emag/index.md): importul retururilor eMAG și câmpul Fulfilled by eMAG.
- [deltatech_marketplace_shopify](../deltatech_marketplace_shopify/index.md): importul retururilor și al rambursărilor Shopify.
- [deltatech_marketplace_trendyol](../deltatech_marketplace_trendyol/index.md): retururile (claims) Trendyol, cu motive mapate pe backend.
- [deltatech_rma_helpdesk](../deltatech_rma_helpdesk/index.md), [deltatech_rma_withdrawal](../deltatech_rma_withdrawal/index.md), [deltatech_rma_lot](../deltatech_rma_lot/index.md): celelalte punți ale `deltatech_rma`.
